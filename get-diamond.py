import function
import json
import pymysql

url_example = "http://www.zbird.com/apidiamond/ajaxdiamondNative/cert_state/ags/symmetryName/Ideal,EX/fluorescence/None,Faint/clearityName/FL,IF/polishName/Ideal,EX/cutName/Ideal,EX/locationName/undefined/salePrice/1000-10000/shapeId/003,001/colorName/D/priStoneWeight/0.3-9.87/pnum/1/isgn/1/groupby/2/psize/8/promot/undefined/fifteen/0"

url_example1 = "http://www.zbird.com/apidiamond/ajaxdiamondNative/pnum/1/isgn/2/groupby/2/psize/8/promot/undefined/fifteen/0"

# 连接数据库
connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    db='diamond',
    charset='utf8'
)
res = function.request_api(url_example1)
res = json.loads(res)
page = res['pagenav']['lastpage']
for i in range(1, page + 1):
    url_example = "http://www.zbird.com/apidiamond/ajaxdiamondNative/pnum/" + str(
        i) + "/isgn/5/groupby/0/psize/20/promot/undefined/fifteen/0"
    res = function.request_api(url_example)
    res = json.loads(res)
    sql = "INSERT INTO diamonds (id,shape_id,shape_name,strone_weight,clearity,color,cut,polish,symmetry,fluorescence,bar_code,certificate,certificate_code,sale_price,slide_price,market_price,discount,sale_status,stock_status,location,location_chinese_name,diamond_params,img_info) VALUES "
    sql_value = ""
    sql_data = []
    for row in res['rows']:
        print(row)
        sql_value += "("
        sql_data.append('"' + str(row['id']) + '"')
        sql_data.append('"' + str(row['shapeId']).strip() + '"')
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
        continue
