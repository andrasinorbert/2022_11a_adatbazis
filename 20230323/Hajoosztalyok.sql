-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: localhost
-- Létrehozás ideje: 2023. Már 23. 11:06
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
-- Tábla szerkezet ehhez a táblához `Hajoosztalyok`
--

CREATE TABLE `Hajoosztalyok` (
  `Osztály` varchar(50) NOT NULL,
  `típus` varchar(2) NOT NULL DEFAULT 'bb',
  `Ország` varchar(50) NOT NULL,
  `ágyúkSzáma` int(11) NOT NULL,
  `kaliber` int(11) NOT NULL,
  `vízkiszorítás` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `Hajoosztalyok`
--

INSERT INTO `Hajoosztalyok` (`Osztály`, `típus`, `Ország`, `ágyúkSzáma`, `kaliber`, `vízkiszorítás`) VALUES
('Bismark.', 'bb', 'Németország', 8, 15, 42000),
('Iowa', 'bb', 'USA', 9, 16, 46000),
('Kongo', 'bc', 'Japán', 8, 14, 32000),
('North Carolina', 'bb', 'USA', 9, 16, 37000),
('Renown', 'bc', 'Nagy Britannia', 6, 15, 32000),
('Revenge', 'bb', 'Nagy Britannia', 8, 15, 29000),
('Tennessee', 'bb', 'USA', 12, 14, 32000),
('Yamato', 'bb', 'Japán', 9, 18, 65000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
