-- MySQL dump 10.13  Distrib 5.7.30, for Linux (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

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
-- Table structure for table `Answer`
--

DROP TABLE IF EXISTS `Answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Answer` (
  `question_id` int(11) NOT NULL,
  `developer_id` int(11) NOT NULL,
  `score` int(11) DEFAULT NULL,
  PRIMARY KEY (`question_id`,`developer_id`),
  KEY `developer_id` (`developer_id`),
  CONSTRAINT `Answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `Question` (`question_id`),
  CONSTRAINT `Answer_ibfk_2` FOREIGN KEY (`developer_id`) REFERENCES `Developer` (`developer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Answer`
--

LOCK TABLES `Answer` WRITE;
/*!40000 ALTER TABLE `Answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comment`
--

DROP TABLE IF EXISTS `Comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `discussion_id` int(11) DEFAULT NULL,
  `comment_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `description` varchar(512) DEFAULT NULL,
  UNIQUE KEY `comment_id` (`comment_id`),
  KEY `discussion_id` (`discussion_id`),
  CONSTRAINT `Comment_ibfk_1` FOREIGN KEY (`discussion_id`) REFERENCES `Discussion` (`discussion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment`
--

LOCK TABLES `Comment` WRITE;
/*!40000 ALTER TABLE `Comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `Comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Developer`
--

DROP TABLE IF EXISTS `Developer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Developer` (
  `developer_id` int(11) NOT NULL AUTO_INCREMENT,
  `regDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`developer_id`),
  CONSTRAINT `Developer_ibfk_1` FOREIGN KEY (`developer_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Developer`
--

LOCK TABLES `Developer` WRITE;
/*!40000 ALTER TABLE `Developer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Developer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Discussion`
--

DROP TABLE IF EXISTS `Discussion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Discussion` (
  `discussion_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  UNIQUE KEY `discussion_id` (`discussion_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `Discussion_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `Question` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Discussion`
--

LOCK TABLES `Discussion` WRITE;
/*!40000 ALTER TABLE `Discussion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Discussion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Job`
--

DROP TABLE IF EXISTS `Job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Job` (
  `developer_id` int(11) NOT NULL,
  `compRep_id` int(11) NOT NULL,
  `jobDescription` varchar(512) DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  PRIMARY KEY (`developer_id`,`compRep_id`),
  KEY `compRep_id` (`compRep_id`),
  CONSTRAINT `Job_ibfk_1` FOREIGN KEY (`developer_id`) REFERENCES `Developer` (`developer_id`),
  CONSTRAINT `Job_ibfk_2` FOREIGN KEY (`compRep_id`) REFERENCES `compRep` (`compRep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Job`
--

LOCK TABLES `Job` WRITE;
/*!40000 ALTER TABLE `Job` DISABLE KEYS */;
/*!40000 ALTER TABLE `Job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Leaderboard`
--

DROP TABLE IF EXISTS `Leaderboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Leaderboard` (
  `leaderboard_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(32) DEFAULT NULL,
  `track_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`leaderboard_id`),
  KEY `track_id` (`track_id`),
  CONSTRAINT `Leaderboard_ibfk_1` FOREIGN KEY (`track_id`) REFERENCES `Track` (`track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Leaderboard`
--

LOCK TABLES `Leaderboard` WRITE;
/*!40000 ALTER TABLE `Leaderboard` DISABLE KEYS */;
/*!40000 ALTER TABLE `Leaderboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Question`
--

DROP TABLE IF EXISTS `Question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(32) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL,
  `test_case` varchar(512) DEFAULT NULL,
  `difficulty` varchar(16) DEFAULT NULL,
  `approval` int(4) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Question`
--

LOCK TABLES `Question` WRITE;
/*!40000 ALTER TABLE `Question` DISABLE KEYS */;
/*!40000 ALTER TABLE `Question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Score`
--

DROP TABLE IF EXISTS `Score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Score` (
  `leaderboard_id` int(11) DEFAULT NULL,
  `developer_id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  KEY `leaderboard_id` (`leaderboard_id`),
  KEY `developer_id` (`developer_id`),
  CONSTRAINT `Score_ibfk_1` FOREIGN KEY (`leaderboard_id`) REFERENCES `Leaderboard` (`leaderboard_id`),
  CONSTRAINT `Score_ibfk_2` FOREIGN KEY (`developer_id`) REFERENCES `Developer` (`developer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Score`
--

LOCK TABLES `Score` WRITE;
/*!40000 ALTER TABLE `Score` DISABLE KEYS */;
/*!40000 ALTER TABLE `Score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Track`
--

DROP TABLE IF EXISTS `Track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Track` (
  `track_id` int(11) NOT NULL AUTO_INCREMENT,
  `no_questions` int(11) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `question_id` int(11) DEFAULT NULL,
  `track_name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Track`
--

LOCK TABLES `Track` WRITE;
/*!40000 ALTER TABLE `Track` DISABLE KEYS */;
/*!40000 ALTER TABLE `Track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `user_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'adafsda','jalkd@gmail.com','$5$rounds=535000$wPp1Zd0.aEyrfN8E$sCXqqXeVt2y7Ch5sRFSz5f1T.9yV9FDQy4HhU49vyJ2','2020-05-20 04:30:44'),(2,'adafsda','jalkd@gmail.com','$5$rounds=535000$7X6huEaVu0DUNJpD$0iYdmBfcOVymltHLNt2hqS2rEaLHxSCpQlYa6ra8H35','2020-05-20 04:33:36'),(3,'adafsda','jalkd@gmail.com','$5$rounds=535000$dLeRTwO5tyGkPGUm$75KW1coEhUyzrgGc6Sl6JebxaGdz4f/azAQ5V/FPjh/','2020-05-20 04:33:39'),(4,'adafsda','jalkd@gmail.com','$5$rounds=535000$J7SRAuM0wLlsyWoA$l2s2WSmfgl9PZIGuHzyDaBOWjH9po35lc2JmBJgtzZA','2020-05-20 04:33:52'),(5,'adafsda','jalkd@gmail.com','$5$rounds=535000$lhYNssm0rtr1ATUl$0Pfh5cdjUvn81p.EEYb9C0rtijpU8iEbs14URSl2Uz1','2020-05-20 04:37:37'),(6,'adafsda','jalkd@gmail.com','$5$rounds=535000$8njYv7uAJB3Idf8C$GMX.5DuYKCMKY3fL/S8kVYx7w98j8BeNQo2F45y0Ap8','2020-05-20 04:37:54'),(7,'adafsda','jalkd@gmail.com','$5$rounds=535000$VKgrNj34Ger4skbm$6G4h7crDtdr5jCu2OETw5PJO0xelTftfc7vxGrdb0dA','2020-05-20 04:37:59'),(8,'adafsda','jalkd@gmail.com','$5$rounds=535000$Hb1lCHIZeGNb3P0D$2myj21Yc/ztg6HgKcc98WWXZomAJaFfexNxkZnBfWq3','2020-05-20 04:38:09'),(9,'adafsda','jalkd@gmail.com','$5$rounds=535000$C6B1vDPlvBoJ/3J.$/7MZ4SmzOMVKEJFygcLk93Tqjo/fIAIg.ZJ3PsQnX2C','2020-05-20 04:39:12'),(10,'adafsda','jalkd@gmail.com','$5$rounds=535000$zkNBJEywjZgQSjTN$qhhifiYdkAXmrcCX5/eAFEDSRkLte6LOJAf6ETK/Vc9','2020-05-20 04:40:41'),(11,'adafsda','jalkd@gmail.com','$5$rounds=535000$yUzbyRj598oN4zZ4$kzAs/7H3dm5xDNaeTZWOGYxWwPNZ1dWaY/pn79X/4ZD','2020-05-20 04:40:54'),(12,'adafsda','jalkd@gmail.com','$5$rounds=535000$RAM0KqBuUEo3ya7i$PMVK01vWYlnUhDpWlRytwr6PmZXP65Md6wRA4EmaP6B','2020-05-20 04:41:13'),(13,'adafsda','jalkd@gmail.com','$5$rounds=535000$dF3KsYCrLuXYzaYY$A88iuXYcbMjltyX45V3N7vDdOACikLzpxZqaB97qbID','2020-05-20 04:41:24'),(14,'adafsda','jalkd@gmail.com','$5$rounds=535000$hL72RetdUBQDl5JV$2K9AS5IXhBXq8MAA0msxManDULEvEih65IRf1Cp1Sa0','2020-05-20 04:41:37'),(15,'adafsda','jalkd@gmail.com','$5$rounds=535000$GgTUYmWaksfNpeXr$2WIt1RdAXzVypHVEJ6tOFJO/eOow94jC1W.QsSX/yy1','2020-05-20 04:42:01'),(16,'adafsda','jalkd@gmail.com','$5$rounds=535000$JUomCCtt4tS1tgX2$zCGfZsQcyy83fn4db13olhp4iXq9IRgs/FWXVkwTgx9','2020-05-20 04:42:07'),(17,'adafsda','jalkd@gmail.com','$5$rounds=535000$s0.sThJpLJPqfA76$G8R0hct/d4CFYSbl6y73pYwDV.eIfvEIKLeG5yRO5C.','2020-05-20 04:42:21'),(18,'adafsda','jalkd@gmail.com','$5$rounds=535000$mqPwIHGb3rhIEf0J$wLCQPRr6qyEKwFahY17UiAs4P1zmCoDQcOh8qb09vVC','2020-05-20 05:18:47');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compRep`
--

DROP TABLE IF EXISTS `compRep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compRep` (
  `compRep_id` int(11) NOT NULL AUTO_INCREMENT,
  `comp_name` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`compRep_id`),
  CONSTRAINT `compRep_ibfk_1` FOREIGN KEY (`compRep_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compRep`
--

LOCK TABLES `compRep` WRITE;
/*!40000 ALTER TABLE `compRep` DISABLE KEYS */;
/*!40000 ALTER TABLE `compRep` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-20  9:30:58
