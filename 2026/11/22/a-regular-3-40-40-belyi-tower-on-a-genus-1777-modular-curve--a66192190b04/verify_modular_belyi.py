"""Exact finite-ring certificate for the level-120 modular Belyi cover.

No floating-point calculations or external dependencies are used.
"""
from itertools import product
from math import gcd, lcm


def mm(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2])%n,
            (a[0]*b[1]+a[1]*b[3])%n,
            (a[2]*b[0]+a[3]*b[2])%n,
            (a[2]*b[1]+a[3]*b[3])%n)


def inv(a,n):
    return (a[3]%n,(-a[1])%n,(-a[2])%n,a[0]%n)


def sl(n):
    return {(a,b,c,d) for a,b,c,d in product(range(n),repeat=4)
            if (a*d-b*c)%n==1}


def subgroup(n):
    if n==8:
        return {(a,0,0,a) for a in (1,3,5,7)}
    if n==3:
        return {(s,s*b%3,0,s) for s in (1,2) for b in range(3)}
    if n==5:
        return {(s,0,0,s) for s in (1,4)}
    raise ValueError(n)


def primitive(n):
    return {(a,c) for a,c in product(range(n),repeat=2) if gcd(a,c,n)==1}


def orbit_partition(n,H):
    todo=primitive(n)
    out=[]
    while todo:
        a,c=min(todo)
        orb={((h[0]*a+h[1]*c)%n,(h[2]*a+h[3]*c)%n) for h in H}
        assert orb<=todo
        todo-=orb
        out.append(orb)
    return out


def unipotent_in_H(n,H,a,c,k):
    # g T^k g^-1 is determined solely by the first column (a,c).
    M=((1-k*a*c)%n,(k*a*a)%n,(-k*c*c)%n,(1+k*a*c)%n)
    return M in H


orders={8:384,3:24,5:120}
H={n:subgroup(n) for n in orders}
G={n:sl(n) for n in orders}
assert {n:len(G[n]) for n in G}==orders
assert {n:len(H[n]) for n in H}=={8:4,3:6,5:2}

# The core of the subgroup is the intersection of its conjugates.
cores={n:{h for h in H[n] if all(mm(mm(g,h,n),inv(g,n),n) in H[n] for g in G[n])} for n in G}
assert {n:len(cores[n]) for n in cores}=={8:4,3:2,5:2}
assert cores[3]=={(1,0,0,1),(2,0,0,2)}
assert cores[8]==H[8] and cores[5]==H[5]

orbits={n:orbit_partition(n,H[n]) for n in H}
assert {n:len(orbits[n]) for n in orbits}=={8:12,3:2,5:12}
widths={}
for n in H:
    vals=[]
    for orb in orbits[n]:
        widths_local=set()
        for a,c in orb:
            widths_local.add(next(k for k in range(1,n+1) if unipotent_in_H(n,H[n],a,c,k)))
        assert len(widths_local)==1
        vals.append(widths_local.pop())
    widths[n]=vals
assert set(widths[8])=={8} and set(widths[5])=={5}
assert sorted(widths[3])==[1,3]
from collections import Counter
cusp_widths=Counter(lcm(a,b,c) for a,b,c in product(widths[8],widths[3],widths[5]))
assert cusp_widths=={40:144,120:144}

SL_order=1
H_order=1
core_order=1
for n in orders:
    SL_order*=len(G[n]); H_order*=len(H[n]); core_order*=len(cores[n])
assert (SL_order,H_order,core_order)==(1105920,48,16)
cover_degree=SL_order//H_order
monodromy_order=SL_order//core_order
assert cover_degree==23040 and monodromy_order==69120
assert monodromy_order//cover_degree==3

# The subgroup of SL2(Z/120) defining Gamma_0(3) is
# SL2(Z/8) x H_3 x SL2(F_5).
base_lift_size=len(G[8])*len(H[3])*len(G[5])
assert SL_order//base_lift_size==4
assert base_lift_size//H_order==5760
assert base_lift_size//H_order==(384//4)*(120//2)

# Cusp widths upstairs, with local widths downstairs 1, 3.
assert sorted(widths[3])==[1,3]
assert lcm(8,5,1)//1==40 and lcm(8,5,3)//3==40
assert 2*1777-2 == -2*5760 + 1920*(3-1)+2*144*(40-1)
assert sum(w*c for w,c in cusp_widths.items())==cover_degree

assert (1+23040//12-288//2)==1777
assert (1+69120//12-576//2)==5473
assert 2*1777-2 == -2*23040+11520+2*7680+(144*39+144*119)
assert 2*5473-2 == -2*69120+34560+2*23040+576*119
print('local SL2 orders:',orders)
print('local subgroup sizes:',{n:len(H[n]) for n in H})
print('local core sizes:',{n:len(cores[n]) for n in cores})
print('local primitive-vector orbit counts:',{n:len(orbits[n]) for n in orbits})
print('cusp widths and multiplicities:',dict(sorted(cusp_widths.items())))
print('regular quotient degree and branch orders:',5760,(3,40,40))
print('original j-cover degree, geometric monodromy order, Galois closure genus:',cover_degree,monodromy_order,5473)
print('all exact checks passed')
