# SZ(N,GY)

| N | GY |
| :-- | :--: |
| MM | málna |
| MM | méz |
| Füles | körte |
| Malacka | méz |
| Malacka | málna |
| Malacka | körte |
| Kanga | banán|
|Tigris |méz|

1. Melyek azok a gyümölcsök, amelyeket ’Micimackó’ szeret?

$\Pi_{GY}(\sigma_{N='MM'}(SZ))$

```sql
select GY
from SZ
where N='MM';
```

2. Melyek azok a gyümölcsök, amelyeket ’Micimackó’ nem szeret? (de valaki más igen)

$\Pi_{GY}(SZ) - \Pi_{GY}(\sigma_{N='MM'}(SZ))$

```sql
(select GY
    from SZ)
except
(select GY
    from SZ
    where N='MM');
```

3. Melyek azok a gyümölcsök, amelyeket valaki szeret és nem csak egyedül Micimackó?

$\Pi_{GY}(SZ-\sigma_{N='MM'}(SZ))$

```sql
select GY
from (select *
    from SZ
    except
    select *
    from SZ
    where N='MM');
```

4. Kik azok akik legalább azokat a gyümölcsöket szeretik, mint Micimackó?

$\Pi_{N}(SZ)-\Pi_{N}(\Pi_{N}(SZ)$ X $\Pi_{GY}(\sigma_{N='MM'}(SZ))-SZ)$

```sql
select N
from SZ
except
select N
from
((select N
from SZ,
    (select GY from SZ where N='MM'))
except
SZ
)
```