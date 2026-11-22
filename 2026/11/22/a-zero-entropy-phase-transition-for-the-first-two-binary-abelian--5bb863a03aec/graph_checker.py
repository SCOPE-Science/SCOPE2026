"""Construct the complete five-symbol presentation of binary words avoiding
Abelian cubes with block lengths one or two, and verify its path census.
Python 3, standard library only. No external dependencies.
"""
from collections import Counter

def abelian_cube(w, p):
    if len(w) != 3*p:
        raise ValueError('bad window')
    return len(set(w[j*p:(j+1)*p].count('1') for j in range(3))) == 1

def allowed(w):
    return all(not abelian_cube(w[i:i+3*p],p)
               for p in (1,2) for i in range(len(w)-3*p+1))

S=tuple(w for k in range(32) if allowed(w:=format(k,'05b')))
E={s:tuple(s[1:]+c for c in '01' if allowed(s+c)) for s in S}
assert len(S)==16
assert sum(map(len,E.values()))==18

cycles=(('00100','01001','10010'),('01101','11011','10110'))
for cyc in cycles:
    for i,s in enumerate(cyc):
        assert cyc[(i+1)%3] in E[s]

# Check all permitted edges and exact entire graph (proof uses this table).
expected={
 '00100':('01001',),'00101':('01010','01011'),
 '00110':('01100','01101'),'01001':('10010','10011'),
 '01010':('10100',),'01011':(), '01100':(),
 '01101':('11011',),'10010':('00100',),'10011':(),
 '10100':(), '10101':('01011',),'10110':('01100','01101'),
 '11001':('10010','10011'),'11010':('10100','10101'),
 '11011':('10110',),
}
assert E==expected, (E,expected)
# Direct weighted path matrix enumeration; each length-5 word gives one start.
d={s:1 for s in S}
for n in range(5,501):
    count=sum(d.values())
    formula=({5:16,6:18,7:12}.get(n,
             10+2*(n%3==0)))
    assert count==formula,(n,count,formula)
    nd={s:0 for s in S}
    for s,v in d.items():
        for t in E[s]:nd[t]+=v
    d=nd
print('PASS complete state graph: 16 states, 18 edges, two period-three cycles')
print('PASS transfer count through length 500; symbolic graph decomposition proves all n')
for s in S:
    print(s, '->',','.join(E[s]) or 'terminal')
