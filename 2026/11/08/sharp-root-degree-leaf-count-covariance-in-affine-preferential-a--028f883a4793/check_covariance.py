from fractions import Fraction as F
from collections import defaultdict
from math import gamma

def calc(delta, nmax=10):
    a=F(1)+delta; beta=F(2)+delta;den=beta+a
    assert a>0
    state={(1,2):F(1)}
    r=a; m=F(2); h=F(1); c=F(0)
    output=[]
    for n in range(2,nmax+1):
        em=sum(pr*L for (d,L),pr in state.items())
        er=sum(pr*(d+delta) for (d,L),pr in state.items())
        ewl=sum(pr*(d+delta)*L for (d,L),pr in state.items())
        eh=sum(pr for (d,L),pr in state.items() if d==1)
        ec=ewl-er*em
        assert (er,em,eh,ec)==(r,m,h,c), (delta,n,(er,em,eh,ec),(r,m,h,c))
        S=beta*n-2
        assert m==(S+2*beta*h)/den
        assert r==(S-a)*h
        output.append((n,c,r,m,h))
        if n==nmax:break
        new=defaultdict(F)
        for (d,L),p in state.items():
            x=F(d)+delta
            if d==1:
                new[(d+1,L)]+=p*x/S
            else:
                new[(d+1,L+1)]+=p*x/S
            others=(L-(d==1))*a/S
            new[(d,L)]+=p*others
            rest=1-x/S-others
            assert rest>=0
            new[(d,L+1)]+=p*rest
        state=dict(new)
        c=(1-delta/S)*c +a*r*m/S**2-a*h/S
        r=r*(1+1/S)
        m=m*(1-a/S)+1
        h=h*(1-a/S)
    return output

for delta in (F(-3,4), F(-1,2), F(0), F(1,2), F(1), F(5)):
    o=calc(delta,11)
    assert o[0][1]==o[1][1]==0 and all(o[i][1]>0 for i in range(2,len(o)))
    assert all(o[i][1]>o[i-1][1] for i in range(3,len(o)))
    print('delta',str(delta),'cov4',o[2][1],'cov11',round(float(o[-1][1]),8),'ratio',round(float(o[-1][1]/o[-1][2]),7),'target',round(float(1/(3+2*delta)),7))

# Recurrences, compared with large n limit
for delta in (-0.75,-0.5,0,0.5,2,8):
    a=1+delta;beta=2+delta
    r=a;m=2.0;h=1.0;c=0.0
    for n in range(2,100001):
        S=beta*n-2
        c=(1-delta/S)*c + a*r*m/S**2 - a*h/S
        r*=1+1/S
        m=m*(1-a/S)+1
        h*=1-a/S
    print('limit delta',delta,'ratio',c/r,'target',1/(3+2*delta),'relative error',(c/r)*(3+2*delta)-1)
print('ALL CHECKS PASS')
