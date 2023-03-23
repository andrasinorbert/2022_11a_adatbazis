-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: localhost
-- Létrehozás ideje: 2023. Már 23. 11:14
-- Kiszolgáló verziója: 10.4.27-MariaDB
-- PHP verzió: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `11e`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `Kimenetelek`
--

CREATE TABLE `Kimenetelek` (
  `Hajónév` varchar(50) NOT NULL,
  `Csatanév` varchar(50) NOT NULL,
  `eredmény` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `Kimenetelek`
--

INSERT INTO `Kimenetelek` (`Hajónév`, `Csatanév`, `eredmény`) VALUES
('Arizona', 'Denmark Strait', 'elsüllyedt'),
('Bismark', 'Pearl Harbour', 'elsüllyedt'),
('California', 'Surigao Strait', 'ok'),
('Duke of York', 'North Cape', 'ok'),
('Fuso', 'Surigao Strait', 'elsüllyedt'),
('Hood', 'Denmark Strait', 'elsüllyedt'),
('King George V', 'Denmark Strait', 'ok'),
('Kirishima', 'Guadalcanal', 'elsüllyedt'),
('Prince of Wales', 'Denmark Strait', 'sérült'),
('Rodney', 'Denmark Strait', 'ok'),
('Scharnhorst', 'North Cape', 'elsüllyedt'),
('South of Dakota', 'Guadalcanal', 'sérült'),
('Tennessee', 'Surigao Strait', 'ok'),
('Washington', 'Guadalcanal', 'ok'),
('West Wirginia', 'Surigao Strait', 'ok'),
('Yamashiro', 'Surigao Strait', 'elsüllyedt');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
