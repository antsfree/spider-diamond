import function
import json
import pymysql
from config import *
import time
from multiprocessing import cpu_count, Pool

# 最大进程数
MAX_PROCESS = cpu_count()


def get_page_num(search_mode):
    """
    获取页码
    :param search_mode:
    :return:
    """
    url = BASE_API_URL + DEFAULT_SEARCH_CONDITION + "isgn/" + str(search_mode)
    result = function.request_api(url)
    result = json.loads(result)
    page_num = result['pagenav']['lastpage']
    return page_num + 1


def save_diamonds(res, search_mode):
    """
    数据存储
    :param res:
    :param search_mode:
    :return:
    """
    if res is None:
        return False
    # 连接数据库
    connect = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DATABASE,
        charset=DB_CHARSET
    )
    sql = "INSERT INTO diamonds (id,shape_id,source_type,shape_name,strone_weight,clearity,color,cut,polish,symmetry,fluorescence,bar_code,certificate,certificate_code,sale_price,slide_price,market_price,discount,sale_status,stock_status,location,location_chinese_name,diamond_params,img_info) VALUES "
    sql_value = ""
    sql_data = []
    for row in res['rows']:
        sql_value += "("
        sql_data.append('"' + str(row['id']) + '"')
        sql_data.append('"' + str(row['shapeId']).strip() + '"')
        sql_data.append('"' + str(search_mode) + '"')
        sql_data.append('"' + str(row['shapeName']).strip() + '"')
        sql_data.append('"' + str(row['priStoneWeight']).strip() + '"')
        sql_data.append('"' + str(row['clearityName']).strip() + '"')
        sql_data.append('"' + str(row['colorName']).strip() + '"')
        sql_data.append('"' + str(row['cutName']).strip() + '"')
        sql_data.append('"' + str(row['polishName']).strip() + '"')
        sql_data.append('"' + str(row['symmetryName']).strip() + '"')
        sql_data.append('"' + str(row['fluorescence']).strip() + '"')
        sql_data.append('"' + str(row['barCode']).strip() + '"')
        sql_data.append('"' + str(row['cert_state']).strip() + '"')
        sql_data.append('\'\'')
        sql_data.append('"' + str(row['salePrice']).strip() + '"')
        sql_data.append('"' + str(row['slide_price']).strip() + '"')
        sql_data.append('"' + str(row['marketPrice']).strip() + '"')
        sql_data.append('"' + str(row['discount']).strip() + '"')
        sql_data.append('\'0\'')
        sql_data.append('\'0\'')
        sql_data.append('"' + str(row['location']).strip() + '"')
        sql_data.append('"' + str(row['locationName']).strip() + '"')
        sql_data.append('\'\'')
        sql_data.append('\'\'')
        sql_value += ','.join(sql_data) + '),'
        sql_data = []
    sql += sql_value[:-1]
    cursor = connect.cursor()
    try:
        cursor.execute(sql)
    except Exception:
        return False


def get_diamonds(search_mode, start_page, end_page):
    """
    获取钻石数据
    :param search_mode:
    :param start_page:
    :param end_page:
    :return:
    """
    for i in range(start_page, end_page + 1):
        diamonds_api = BASE_API_URL + \
                       DEFAULT_SEARCH_CONDITION + \
                       "pnum/" + str(i) + \
                       "/isgn/" + str(search_mode)
        res = function.request_api(diamonds_api)
        res = json.loads(res)
        print("当前正在获取搜索模式为 " + str(search_mode) + " 的第 " + str(i) + " 页数据\n")
        save_diamonds(res, search_mode)
        if i == end_page:
            print(diamonds_api)
            print("\n")


def delivery_num(num):
    """
    进程处理数量分配
    :param num:
    :return:
    """
    while (num % MAX_PROCESS) != 0:
        num += 1
    return int(num / MAX_PROCESS)


def diamond_process(search_mode):
    """
    多进程处理数据
    :param search_mode:
    :return:
    """
    total_page = get_page_num(search_mode)
    per_num = delivery_num(total_page)
    # 开启线程池
    pool = Pool(cpu_count())
    for p in range(1, MAX_PROCESS + 1):
        end = per_num * p
        start = end - per_num + 1
        pool.apply_async(get_diamonds, args=(search_mode, start, end))
    pool.close()
    pool.join()


def main():
    start_time = time.time()
    diamond_process(DOMESTIC_SEARCH)
    diamond_process(GLOBAL_SEARCH)
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main()
