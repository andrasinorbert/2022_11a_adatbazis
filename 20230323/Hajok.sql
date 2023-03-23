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
-- Tábla szerkezet ehhez a táblához `Hajok`
--

CREATE TABLE `Hajok` (
  `Hajónév` varchar(50) NOT NULL,
  `Osztály` varchar(50) NOT NULL,
  `felavatva` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- A tábla adatainak kiíratása `Hajok`
--

INSERT INTO `Hajok` (`Hajónév`, `Osztály`, `felavatva`) VALUES
('California', 'Tennessee', 1921),
('Haruna', 'Kongo', 1915),
('Hiei', 'Kongo', 1914),
('Iowa', 'Iowa', 1943),
('Kirishima', 'Kongo', 1915),
('Kongo', 'Kongo', 1913),
('Missuri', 'Iowa', 1944),
('Musashi', 'Yamato', 1942),
('New Jersey', 'Iowa', 1943),
('North Carolina', 'North Carolina', 1941),
('Ramillies', 'Revenge', 1917),
('Renown', 'Renown', 1916),
('Repulse', 'Renown', 1916),
('Resolution', 'Revenge', 1916),
('Revenge', 'Revenge', 1916),
('Royal Oak', 'Revenge', 1916),
('Royal Sovereign', 'Revenge', 1916),
('Tennesse', 'Tenesse', 1920),
('Washington', 'North Carolina', 1941),
('Wisconsin', 'Iowa', 1944),
('Yamato', 'Yamato', 1941);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
