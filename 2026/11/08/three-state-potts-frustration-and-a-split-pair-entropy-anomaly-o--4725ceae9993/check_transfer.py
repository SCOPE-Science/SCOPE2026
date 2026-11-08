"""An independent transfer count over color population and split pairs."""
from collections import defaultdict
from math import factorial, log, pi, sqrt, lgamma, exp


def exact_by_transfer(m):
    # State (N0,N1,split_count); N2 is inferred from elapsed vertices.
    states={(0,0,0):1}
    for i in range(m):
        nxt=defaultdict(int)
        for (a,b,d),v in states.items():
            for x in range(3):
                for y in range(3):
                    nxt[(a+(x==0)+(y==0),b+(x==1)+(y==1),d+(x!=y))] += v
        states=nxt
    min_e = None
    total=split=mono=0
    for (a,b,d),v in states.items():
        c=2*m-a-b
        E=(a*(a-1)+b*(b-1)+c*(c-1))//2-(m-d)
        if min_e is None or E<min_e:
            min_e,total,split,mono=E,0,0,0
        if E==min_e:
            total+=v
            split+=v*(d==1)
            mono+=v*(d==0)

    return min_e,total,split,mono


def theory(m):
    t,s=divmod(m,3)
    E=2*(3*t*t+2*s*t+s)-2*m
    base=factorial(m)//(factorial(t+1)**s*factorial(t)**(3-s))
    if s==0:
        return E,base,0,base
    mono=3*base
    return E,mono*(2*t+3),mono*(2*t+2),mono

if __name__=='__main__':
    for m in range(2,19):
        got=exact_by_transfer(m)
        expected=theory(m)
        assert got==expected,(m,got,expected)
        print('m',m,'E,ground,split,mono',*got)
    for m in [300,301,302,3000,3001,3002]:
        t,s=divmod(m,3)
        logg=lgamma(m+1)-s*lgamma(t+2)-(3-s)*lgamma(t+1)
        if s:logg+=log(3*(2*t+3))
        a=3*sqrt(3)/(2*pi*m) if s==0 else 3*sqrt(3)/pi
        ratio=exp(logg-m*log(3))/a
        assert abs(ratio-1)<0.002 if m>1000 else abs(ratio-1)<0.02
        print('m',m,'asymptotic ratio',round(ratio,8))
    print('TRANSFER_PASS')
