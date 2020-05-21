-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.4.11-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `question_id` int(11) NOT NULL,
  `developer_id` int(11) NOT NULL,
  `score` int(11) DEFAULT NULL,
  PRIMARY KEY (`question_id`,`developer_id`),
  KEY `developer_id` (`developer_id`),
  CONSTRAINT `Answer_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`),
  CONSTRAINT `Answer_ibfk_2` FOREIGN KEY (`developer_id`) REFERENCES `developer` (`developer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `discussion_id` int(11) DEFAULT NULL,
  `comment_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `description` varchar(512) DEFAULT NULL,
  UNIQUE KEY `comment_id` (`comment_id`),
  KEY `discussion_id` (`discussion_id`),
  CONSTRAINT `Comment_ibfk_1` FOREIGN KEY (`discussion_id`) REFERENCES `discussion` (`discussion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comprep`
--

DROP TABLE IF EXISTS `comprep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comprep` (
  `compRep_id` int(11) NOT NULL AUTO_INCREMENT,
  `comp_name` varchar(256) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`compRep_id`),
  CONSTRAINT `compRep_ibfk_1` FOREIGN KEY (`compRep_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comprep`
--

LOCK TABLES `comprep` WRITE;
/*!40000 ALTER TABLE `comprep` DISABLE KEYS */;
INSERT INTO `comprep` VALUES (20,'AITools','2020-05-20 12:31:31'),(22,'Askldna','2020-05-20 12:33:02'),(23,'Bilkent','2020-05-20 13:42:25'),(24,'123','2020-05-20 13:43:29'),(26,'123','2020-05-20 18:21:27');
/*!40000 ALTER TABLE `comprep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `developer`
--

DROP TABLE IF EXISTS `developer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `developer` (
  `developer_id` int(11) NOT NULL AUTO_INCREMENT,
  `regDate` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`developer_id`),
  CONSTRAINT `Developer_ibfk_1` FOREIGN KEY (`developer_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `developer`
--

LOCK TABLES `developer` WRITE;
/*!40000 ALTER TABLE `developer` DISABLE KEYS */;
INSERT INTO `developer` VALUES (27,'2020-05-20 18:34:00');
/*!40000 ALTER TABLE `developer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discussion`
--

DROP TABLE IF EXISTS `discussion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discussion` (
  `discussion_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  UNIQUE KEY `discussion_id` (`discussion_id`),
  KEY `question_id` (`question_id`),
  CONSTRAINT `Discussion_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `question` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discussion`
--

LOCK TABLES `discussion` WRITE;
/*!40000 ALTER TABLE `discussion` DISABLE KEYS */;
/*!40000 ALTER TABLE `discussion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job` (
  `developer_id` int(11) NOT NULL,
  `compRep_id` int(11) NOT NULL,
  `jobDescription` varchar(512) DEFAULT NULL,
  `endDate` date DEFAULT NULL,
  PRIMARY KEY (`developer_id`,`compRep_id`),
  KEY `compRep_id` (`compRep_id`),
  CONSTRAINT `Job_ibfk_1` FOREIGN KEY (`developer_id`) REFERENCES `developer` (`developer_id`),
  CONSTRAINT `Job_ibfk_2` FOREIGN KEY (`compRep_id`) REFERENCES `comprep` (`compRep_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leaderboard`
--

DROP TABLE IF EXISTS `leaderboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `leaderboard` (
  `leaderboard_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(32) DEFAULT NULL,
  `track_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`leaderboard_id`),
  KEY `track_id` (`track_id`),
  CONSTRAINT `Leaderboard_ibfk_1` FOREIGN KEY (`track_id`) REFERENCES `track` (`track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leaderboard`
--

LOCK TABLES `leaderboard` WRITE;
/*!40000 ALTER TABLE `leaderboard` DISABLE KEYS */;
/*!40000 ALTER TABLE `leaderboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(32) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL,
  `test_case` varchar(512) DEFAULT NULL,
  `difficulty` varchar(16) DEFAULT NULL,
  `approval` int(4) DEFAULT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'Algorithms','Very interesting question!','','low',1),(2,'Database','Very interesting question2!','','medium',1),(3,'Graphs','Very interesting question3!','','high',1),(4,'Graphs','Very interesting question4!','','high',1);
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `score`
--

DROP TABLE IF EXISTS `score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `score` (
  `leaderboard_id` int(11) DEFAULT NULL,
  `developer_id` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  KEY `leaderboard_id` (`leaderboard_id`),
  KEY `developer_id` (`developer_id`),
  CONSTRAINT `Score_ibfk_1` FOREIGN KEY (`leaderboard_id`) REFERENCES `leaderboard` (`leaderboard_id`),
  CONSTRAINT `Score_ibfk_2` FOREIGN KEY (`developer_id`) REFERENCES `developer` (`developer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `score`
--

LOCK TABLES `score` WRITE;
/*!40000 ALTER TABLE `score` DISABLE KEYS */;
/*!40000 ALTER TABLE `score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `track`
--

DROP TABLE IF EXISTS `track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `track` (
  `track_id` int(11) NOT NULL AUTO_INCREMENT,
  `no_questions` int(11) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `track_name` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`track_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `track`
--

LOCK TABLES `track` WRITE;
/*!40000 ALTER TABLE `track` DISABLE KEYS */;
INSERT INTO `track` VALUES (1,5,'2020-05-20 19:43:08','track1'),(2,4,'2020-05-20 19:52:27','track2');
/*!40000 ALTER TABLE `track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trackquestions`
--

DROP TABLE IF EXISTS `trackquestions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trackquestions` (
  `question_id` int(11) NOT NULL,
  `track_id` int(11) NOT NULL,
  PRIMARY KEY (`question_id`,`track_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trackquestions`
--

LOCK TABLES `trackquestions` WRITE;
/*!40000 ALTER TABLE `trackquestions` DISABLE KEYS */;
/*!40000 ALTER TABLE `trackquestions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (20,'Askari Iqbal','ai@g.com','$5$rounds=535000$s7YCwiwEZWcjkM.R$7kQ.RSC0Siu/gwjLrwNzT6/u0nBsn0Z203ZZiU4yvz/','2020-05-20 12:16:27'),(22,'Abdullah Qutb','aasfkjasndai@g.com','$5$rounds=535000$6ToEchMwP2mgMO02$o1MrAdlEUa8rfmD/Lz7Ob4eTEX9VekHkcq.XaxHLLjA','2020-05-20 12:33:02'),(23,'asdasd','123','$5$rounds=535000$lZTzS8xp0ZBtLfrR$YS7Yi3Osb6KQfbhaVwqUm.szxMa2OjKUFmK75haUz.6','2020-05-20 13:42:25'),(24,'123','1234','1234','2020-05-20 13:43:29'),(25,'123','12345','$5$rounds=535000$2oTd92KRbW6wxMJX$AJx9OeoHQf/HyrhKOaXVwvHMtsDacNiwZQQx2c0dV1C','2020-05-20 15:01:23'),(26,'123','12','123','2020-05-20 18:21:27'),(27,'test','test','test','2020-05-20 18:34:00');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-21 14:46:42
