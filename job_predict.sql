-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 20, 2024 at 09:11 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `job_predict`
--

-- --------------------------------------------------------

--
-- Table structure for table `job_data`
--

CREATE TABLE `job_data` (
  `id` int NOT NULL,
  `age` int DEFAULT NULL,
  `business_travel` int DEFAULT NULL,
  `department` int DEFAULT NULL,
  `distance_from_home` int DEFAULT NULL,
  `education` int DEFAULT NULL,
  `education_field` int DEFAULT NULL,
  `environment_satisfaction` int DEFAULT NULL,
  `gender` int DEFAULT NULL,
  `job_involvement` int DEFAULT NULL,
  `job_level` int DEFAULT NULL,
  `job_role` int DEFAULT NULL,
  `job_satisfaction` int DEFAULT NULL,
  `marital_status` int DEFAULT NULL,
  `monthly_income` int DEFAULT NULL,
  `salary_slab` int DEFAULT '0',
  `overtime` int DEFAULT NULL,
  `total_working_years` int DEFAULT NULL,
  `work_life_balance` int DEFAULT NULL,
  `years_at_company` int DEFAULT NULL,
  `years_in_current_role` int DEFAULT NULL,
  `prediction_result` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `job_data`
--

INSERT INTO `job_data` (`id`, `age`, `business_travel`, `department`, `distance_from_home`, `education`, `education_field`, `environment_satisfaction`, `gender`, `job_involvement`, `job_level`, `job_role`, `job_satisfaction`, `marital_status`, `monthly_income`, `salary_slab`, `overtime`, `total_working_years`, `work_life_balance`, `years_at_company`, `years_in_current_role`, `prediction_result`) VALUES
(1, 20, 2, 2, 3, 4, 5, 3, 2, 1, 2, 4, 2, 1, 1, 2, 4, 5, 7, 2, 2, 'YA'),
(2, 60, 1, 2, 1, 4, 5, 3, 0, 1, 3, 2, 4, 2, 10883, 3, 0, 19, 4, 1, 0, 'TIDAK'),
(3, 30, 1, 1, 30, 2, 4, 3, 0, 2, 3, 3, 1, 1, 8000000, 0, 0, 2, 1, 2, 2, 'TIDAK'),
(4, 20, 0, 2, 6, 3, 2, 4, 1, 2, 1, 6, 4, 1, 2926, 1, 0, 1, 3, 1, 0, 'Stayed'),
(5, 30, 0, 0, 34, 1, 0, 1, 0, 1, 3, 6, 2, 0, 3000000, 2, 1, 6, 3, 10, 24, 'Stayed'),
(6, 50, 1, 1, 30, 2, 2, 2, 1, 3, 4, 2, 2, 1, 4000000, 0, 1, 6, 3, 7, 0, 'STAYED'),
(7, 31, 1, 1, 20, 2, 1, 2, 0, 2, 3, 2, 3, 2, 3000000, 2, 1, 4, 3, 5, 2, 'STAYED'),
(8, 60, 2, 2, 5, 3, 3, 2, 0, 3, 1, 0, 4, 1, 1051, 1, 0, 0, 3, 0, 0, 'STAYED'),
(9, 58, 1, 2, 7, 3, 5, 3, 1, 2, 3, 4, 1, 0, 10008, 3, 1, 31, 2, 10, 9, 'STAYED');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `job_data`
--
ALTER TABLE `job_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `job_data`
--
ALTER TABLE `job_data`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
