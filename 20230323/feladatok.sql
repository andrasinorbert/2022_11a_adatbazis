-- 1) Melyek azok a hajók, 
--      amelyeket 1921 előtt avattak fel?

SELECT `Hajónév`
FROM `Hajok`
WHERE `felavatva` < '1921';

-- 2) Adjuk meg azokat a hajóosztályokat
--  a gyártó országok nevével együtt,
--  amelyeknek az ágyúi legalább 16-os kaliberűek!

SELECT Osztály, Ország
FROM Hajoosztalyok
WHERE kaliber >=16 ;

-- 3) Adjuk meg az adatbázisban szereplő
--      összes hadihajó nevét!

SELECT Hajónév
FROM Hajok
UNION
SELECT Hajónév
FROM Kimenetelek;

-- 4) Adjuk meg a 
--      Denmark Strait-csatában elsüllyedt
--      hajók nevét!

SELECT Hajónév
FROM Kimenetelek
WHERE Csatanév = "Denmark Strait"
    and eredmény ="elsüllyedt";

-- 5) Melyek azok az országok,
--      amelyeknek csatahajóik (bb) is
--      és cirkálóhajóik (bc) is voltak?
SELECT Ország
from Hajoosztalyok
where típus like "bb"
    and ország IN
(select ország
from Hajoosztalyok
where típus like "bc");

-- 6) Melyik hajó melyik országban készült?

select Hajónév, Ország
from Hajok natural join Hajoosztalyok
order by Ország desc;

-- 7) Adjuk meg a Guadalcanal csatában
--      részt vett hajók nevét, vízkiszorítását
--      és ágyúinak a számát!

