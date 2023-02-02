-- PI - projekcio
Select név, kor
from R;

-- SZIGMA - szelekcio
Select *
from R
WHERE kor<18;

-- RÓ - átnevezés
Select név AS "18 év alattiak"
from R
WHERE kor<18;

-- Halmazműveletek

Select név, kor
from R
union
select név, kor
from S;

Select név, kor
from R
intersect
select név, kor
from S;

Select név, kor
from R
MINUS
select név, kor
from S;

-- descartes - szorzat
Select *
from R,S;

-- theta-join
Select *
from R,S
where R.kor<18;

-- netural join
Select *
from R natural join S;



