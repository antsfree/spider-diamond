# ************************************************************
# Sequel Pro SQL dump
# Version 4529
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.22)
# Database: diamond
# Generation Time: 2018-07-29 15:00:57 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table diamonds
# ------------------------------------------------------------

DROP TABLE IF EXISTS `diamonds`;

CREATE TABLE `diamonds` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `shape_id` varchar(5) NOT NULL DEFAULT '' COMMENT '形状 ID',
  `shape_name` varchar(10) NOT NULL DEFAULT '' COMMENT '形状名称',
  `strone_weight` varchar(10) NOT NULL DEFAULT '' COMMENT '钻石大小',
  `clearity` varchar(5) NOT NULL DEFAULT '' COMMENT '纯净度',
  `color` varchar(5) NOT NULL DEFAULT '' COMMENT '颜色',
  `cut` varchar(5) NOT NULL DEFAULT '' COMMENT '切工',
  `polish` varchar(5) NOT NULL DEFAULT '' COMMENT '抛光',
  `symmetry` varchar(5) NOT NULL DEFAULT '' COMMENT '对称',
  `fluorescence` varchar(5) NOT NULL DEFAULT '' COMMENT '荧光',
  `bar_code` varchar(20) DEFAULT NULL COMMENT '编号',
  `certificate` bigint(5) DEFAULT NULL COMMENT '证书类型',
  `certificate_code` varchar(20) DEFAULT NULL COMMENT '证书编号',
  `sale_price` varchar(20) DEFAULT '0' COMMENT '销售价格',
  `slide_price` varchar(20) DEFAULT '0' COMMENT '滑动价格',
  `market_price` varchar(20) DEFAULT '0' COMMENT '市场价',
  `discount` varchar(5) DEFAULT '100' COMMENT '折扣(百分比)',
  `sale_status` tinyint(1) DEFAULT '0' COMMENT '销售状态（0未知，2已售完，1销售中',
  `stock_status` tinyint(1) DEFAULT '0' COMMENT '是否现货（0未知，1是现货，2不是现货）',
  `location` varchar(20) DEFAULT NULL COMMENT '所在地',
  `diamond_params` text COMMENT '钻石参数',
  `img_info` text COMMENT '图片信息',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
