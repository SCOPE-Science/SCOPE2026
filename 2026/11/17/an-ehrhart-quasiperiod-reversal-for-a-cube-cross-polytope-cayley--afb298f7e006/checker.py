"""Independent finite checks of the exact Ehrhart generating function.
Requires SymPy (tested with locally installed SymPy). Mathematics proof is in RESULT.md.
"""
from itertools import product
import math
import sympy as S

u,z = S.symbols('u z')

def sphere_series(d):
    return 1 + sum(S.binomial(d,j)*(-2)**j*(1+u)**(d-j)*(u**j-1)*u**(j+1)/(1-u**(j+1))
                   for j in range(1,d+1))/(1-u)**d

def ehrhart_series(d):
    a=sphere_series(d)
    h=S.cancel(((1+u)**2*a + (1-u)**2*a.subs(u,-u))/(2*(1-u*u)**2))
    num,den=S.fraction(h)
    assert all(power[0]%2==0 for power,_ in S.Poly(num,u).terms())
    assert all(power[0]%2==0 for power,_ in S.Poly(den,u).terms())
    numz=sum(co*z**(power[0]//2) for power,co in S.Poly(num,u).terms())
    denz=sum(co*z**(power[0]//2) for power,co in S.Poly(den,u).terms())
    return S.cancel(numz/denz)

def direct(d,n):
    total=0
    for xs in product(range(-n,n+1),repeat=d):
        l1=sum(abs(x) for x in xs)
        linf=max(map(abs,xs))
        total+=max(0,2*n-l1-linf+1)
    return total

def first_coeffs(d,N):
    # Exact coefficient recurrence from rational H(z), not numerical evaluation.
    h=ehrhart_series(d)
    a,b=map(lambda x:S.Poly(x,z),S.fraction(h))
    an=[int(a.nth(i)) for i in range(N+1)]
    bn=[int(b.nth(i)) for i in range(b.degree()+1)]
    assert bn[0] in (-1,1)
    out=[]
    for k in range(N+1):
        v=S.Rational(an[k]-sum(bn[j]*out[k-j] for j in range(1,min(k,len(bn)-1)+1)),bn[0])
        assert v.q==1
        out.append(int(v))
    return out

assert S.simplify(ehrhart_series(1)-(1+z)**2/(1-z)**3)==0
assertions=1
for d,maxn in [(1,16),(2,12),(3,8),(4,4),(5,2)]:
    coeff=first_coeffs(d,maxn)
    for n in range(maxn+1):
        assert coeff[n]==direct(d,n),(d,n,coeff[n],direct(d,n))
        assertions+=1
    assert coeff[1]==2*d+3
    assertions+=1
for d,expected in [(4,[1,2,3,5]),(5,[1,3,5])]:
    h=ehrhart_series(d)
    a,b=S.fraction(h)
    assert S.gcd(a,b)==1
    fac=S.factor_list(b)[1]
    roots={}
    for q in range(1,7):
        poly=S.cyclotomic_poly(q,z)
        roots[q]=sum(p==poly for p,k in fac)
    assert sorted(q for q,v in roots.items() if v)==expected,(d,roots)
    per=math.lcm(*expected)
    assert per=={4:30,5:15}[d]
    assertions+=3
for d in (1,3,5,7):
    a,b=S.fraction(ehrhart_series(d))
    assert S.rem(b,z+1)!=0
    assertions+=1
for d in (2,3,4,5,6):
    h=ehrhart_series(d)
    a,b=S.fraction(h)
    pole=S.limit((1-z)**(d+2)*h,z,1)
    vol=S.Rational(2*4**d, (d+1)*math.factorial(d+1))
    assert S.simplify(pole-vol*math.factorial(d+1))==0,(d,pole,vol)
    assertions+=1
print('PASS',assertions,'exact count/series/pole/period checks')
print('Ehrhart period in dimension 5:',30,'; dimension 6:',15)
print('d=4 generating function:',S.factor(ehrhart_series(4)))
print('d=5 generating function:',S.factor(ehrhart_series(5)))
