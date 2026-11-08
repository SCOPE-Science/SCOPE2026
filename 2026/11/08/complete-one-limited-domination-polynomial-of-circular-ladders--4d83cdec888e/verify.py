import sympy as sp
from collections import Counter
z,t=sp.symbols('z t'); states=[(a,b) for a in range(4) for b in range(4)]
def allowed(a,b,c):
    for h in range(2):
        in_s=(b>>h)&1
        ns=((a>>h)&1)+((c>>h)&1)+((b>>(1-h))&1)
        if in_s and ns==3:return False
        if not in_s and ns>=2:return False
    return True
T=sp.zeros(16)
for i,(a,b) in enumerate(states):
    for c in range(4):
        if allowed(a,b,c):T[i,states.index((b,c))]=z**(2-b.bit_count())
q=sp.Poly(T.charpoly(t).as_expr(),t).as_expr()
P1=(t-z)
P2=t*t-z*t+z**3
P5=t**5-z**2*t**4-z**3*t**3-(z**5+2*z**4)*t**2-(z**6+z**5+z**4)*t-z**6
assert sp.expand(q-t**8*P1*P2*P5)==0
print('CHAR_POLY_CERT_OK')
for n in range(3,9):
    F=sp.Poly(sp.trace(T**n),z)
    count=Counter()
    mask=(1<<(2*n))-1
    nbr=[]
    for i in range(n):
        for b in range(2):
            nbr.append(tuple([2*((i-1)%n)+b,2*((i+1)%n)+b,2*i+(1-b)]))
    for S in range(1<<(2*n)):
        D=mask^S
        ok=True
        for v in range(2*n):
            inS=(S>>v)&1
            sN=sum((S>>w)&1 for w in nbr[v])
            if (inS and sN==3) or (not inS and sN>=2):ok=False;break
        if ok: count[(D.bit_count())]+=1
    assert F==sp.Poly.from_dict({(k,):v for k,v in count.items()},gens=(z,)), (n,F,count)
    assert min(count)==n and count[n]==(6 if n%4==0 else 2)
    print('EXHAUSTIVE_OK',n,'configs',2**(2*n),'valid',sum(count.values()),'minimum_count',count[n])
for n in range(9,21):
    Tn=T**n
    assert int(sp.Poly(sp.trace(Tn),z).coeff_monomial(z**n))==(6 if n%4==0 else 2)
print('LONGER_TRACE_MIN_COUNTS_OK 9..20')
print('VERIFY_OK')
