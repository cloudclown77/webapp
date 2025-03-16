-- MySQL dump 10.13  Distrib 8.4.4, for Win64 (x86_64)
--
-- Host: localhost    Database: customerpanelapp
-- ------------------------------------------------------
-- Server version	8.4.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `domain` varchar(255) NOT NULL,
  `product` varchar(3) NOT NULL,
  `sku` varchar(255) NOT NULL,
  `creation_date` date NOT NULL,
  `renew_date` date NOT NULL,
  `sub_status` varchar(10) NOT NULL,
  `payment_plan` varchar(20) NOT NULL,
  `assigned_licence` int NOT NULL,
  `purchaced_licence` int NOT NULL,
  `customer_id` varchar(255) NOT NULL,
  `cloud_id` varchar(255) NOT NULL,
  `provision_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_id` (`customer_id`),
  UNIQUE KEY `cloud_id` (`cloud_id`),
  UNIQUE KEY `provision_id` (`provision_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'www.rahulbd.com','GWS','Google Meet, Google Voice, Gmail','2025-03-01','2025-04-01','Active','Monthly',3,3,'xq2408ubw4adc','gcloud-1242452dsfdss','1242452dsfdss-gcloud'),(3,'www.rahulbd.com','GWS','Google Meet, Google Voice, Gmail','2025-03-01','2025-04-01','Active','Monthly',3,3,'xq2408ubw4ad1','gcloud-1242452dsfdss1','1242452dsfdss1-gcloud'),(4,'www.rahulbd.com','GCP','Compute Engine, Firewall','2025-04-04','2025-07-01','Inactive','Yearly',3,2,'vwkz1secqj12','google.cloud.112','1.cloud.google12'),(5,'www.rahulbd.com','GWS','Google Meet, Google Voice, Gmail','2025-02-28','2025-03-28','Active','Monthly',3,3,'xq2408ubw4ad112','gcloud-1242452dsfdss12','1242452dsfdss1-gcloud12'),(6,'www.rahulbd.comq','GWS','Google Meet, Google Voice, Gmail','2025-03-01','2025-03-30','Active','Monthly',4,1,'12dd23r8nnss','0nnnxu883','sdh20udjnw23'),(7,'hwd.wiedhw.wiehi','gws','edfsc,0022,293u','2008-12-12','2025-08-15','inactive','yearly',23,23,'007bd2bbd8bv91','w0002bdb92end','9003bddbwuw');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-12 15:30:56
