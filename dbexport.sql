-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: rohit
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookname` varchar(40) DEFAULT NULL,
  `author` varchar(40) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `section` varchar(40) DEFAULT NULL,
  `serial_no` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (3,'java','prince',99,'academic','1221.0'),(4,'python','rana',98,'academic','1207.0'),(6,'cpp','tom',97,'academic','1205.0'),(7,'javascript','tim',95,'academic','1214.0'),(8,'alchemyst','jim',99,'academic','1209.0'),(9,'maluha','jack',99,'academic','1215.0'),(10,'pk','amir',100,'academic','1211.0'),(11,'deep learning','rock',99,'academic','1219.0'),(12,'DBMS','rohit',99,'academic','1222.0'),(13,'CN','pratyush',98,'academic','1206.0'),(20,'M3','kundu',100,'academic','1202.0'),(21,'ADS','viru',101,'academic','1223.0'),(22,'DS','verma',100,'academic','1201.0'),(23,'physics','adarsh',100,'academic','1200.0'),(24,'chemistry','mehta',99,'academic','1203.0'),(25,'GATE','badaprince',100,'academic','1217.0'),(26,'JEE','swapnil',99,'academic','1204.0'),(27,'flask','amir',99,'academic','1211.0'),(29,'ISEE','raman',102,'academic','1210.0'),(30,'CG','nihal',101,'academic','1218.0'),(32,'SEPM','pranav',101,'academic','1212.0'),(33,'M2','sumit',101,'academic','1213.0'),(34,'M1','rishi',101,'academic','1208.0'),(36,'EGR','mohan',98,'academic','1224.0'),(38,'ml','rahul',100,'academic','1216.0');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookcn`
--

DROP TABLE IF EXISTS `bookcn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookcn` (
  `bookname` varchar(40) DEFAULT NULL,
  `bookcount` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookcn`
--

LOCK TABLES `bookcn` WRITE;
/*!40000 ALTER TABLE `bookcn` DISABLE KEYS */;
INSERT INTO `bookcn` VALUES ('python',55),('cpp',30),('GATE',30),('ISEE',46),('DBMS',45),('javascript',30),('ADS',30),('DS',30),('EGR',30),('physics',30),('M2',30),('CG',45),('CN',52),('maluha',30),('ml',45),('flask',30),('alchemy',45),('deeplearning',30),('M1',30),('M3',30),('SEPM',30),('chemistry',30),('java',30),('pk',30),('JEE',30);
/*!40000 ALTER TABLE `bookcn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue`
--

DROP TABLE IF EXISTS `issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue` (
  `username` varchar(40) DEFAULT NULL,
  `issuedate` date DEFAULT NULL,
  `bookname` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue`
--

LOCK TABLES `issue` WRITE;
/*!40000 ALTER TABLE `issue` DISABLE KEYS */;
INSERT INTO `issue` VALUES ('suraj','2019-10-22','EGR'),('suraj','2019-10-22','CN'),('suraj','2019-10-22','chemistry'),('suraj','2019-10-23','CG'),('prince','2020-05-01','deep learning'),('prince','2020-05-01','CG'),('prince','2020-05-01','python');
/*!40000 ALTER TABLE `issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(40) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'w','w','w'),(2,'prince','prince','1234'),(3,'suraj','surajrana@gmail.com','1234'),(4,'prince','princeroshan17104','1234');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usersadmin`
--

DROP TABLE IF EXISTS `usersadmin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usersadmin` (
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersadmin`
--

LOCK TABLES `usersadmin` WRITE;
/*!40000 ALTER TABLE `usersadmin` DISABLE KEYS */;
INSERT INTO `usersadmin` VALUES ('prince','1234');
/*!40000 ALTER TABLE `usersadmin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usersbook`
--

DROP TABLE IF EXISTS `usersbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usersbook` (
  `username` varchar(40) DEFAULT NULL,
  `bookname` varchar(40) DEFAULT NULL,
  `bookcount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usersbook`
--

LOCK TABLES `usersbook` WRITE;
/*!40000 ALTER TABLE `usersbook` DISABLE KEYS */;
INSERT INTO `usersbook` VALUES ('prince','cpp',NULL),('prince','ADS',NULL),('prince','python',NULL),('prince','ISEE',NULL),('prince','CG',NULL),('suraj','SEPM',NULL),('suraj','cpp',NULL),('suraj','python',NULL),('suraj','CG',NULL),('suraj','ISEE',NULL),('suraj','DS',NULL),('suraj','ml',NULL),('prince','1218.0',NULL),('prince','1206.0',NULL),('prince','1216.0',NULL),('prince','CN',NULL);
/*!40000 ALTER TABLE `usersbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userscart`
--

DROP TABLE IF EXISTS `userscart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userscart` (
  `bookname` varchar(40) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userscart`
--

LOCK TABLES `userscart` WRITE;
/*!40000 ALTER TABLE `userscart` DISABLE KEYS */;
INSERT INTO `userscart` VALUES ('ml','suraj');
/*!40000 ALTER TABLE `userscart` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-01 20:43:30
