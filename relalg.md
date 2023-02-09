# Relációs algebra
## halmazműveletek
### halmazműveletek

- első
- második
- harmadik

1. egy
1. egynegyed
1. másfél
1. kettő
1. három

## Műveletek jelölései

$\Pi_{név, kor}(Adattábla)$
$\sigma_{feltétel}(Tábla)$
$\rho_{ujnévlista}(Tábla)$
R $\cup$ S
R $\cap$ S
R $-$ S
R &#8904; S
R &#8904;$_{feltétel}$ S

```python
def atlag(lista):
    s=0
    for i in lista:
        s+=i
    return s/len(lista)
```