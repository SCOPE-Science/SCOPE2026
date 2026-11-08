"""Exact finite-horizon verification of balanced urn identities.
Scientific check only; no implication of infinite-horizon certification.
"""
from fractions import Fraction as Q
from itertools import product


def walk(initial, a, b, xi):
    s = a+b
    states = {(Q(initial[0]),Q(initial[1])): Q(1)}
    for rule in xi:
        nxt = {}
        for (u,v),pr in states.items():
            t=u+v
            for sign,select in [(1,u/t),(-1,v/t)]:
                if rule:
                    du,dv=(a,b) if sign==1 else (b,a)
                else:
                    du,dv=(s,0) if sign==1 else (0,s)
                pair=(u+du,v+dv)
                nxt[pair]=nxt.get(pair,Q(0))+pr*select
        states=nxt
    return states

def moment(states,k):
    return sum(p * ((u-v)/(u+v))**k for (u,v),p in states.items())

checks=0
# All rule strings through length six, several mixed cases and asymmetric initials.
for (u,v,a,b) in [(1,1,1,1),(2,1,1,2),(1,3,2,1),(3,2,1,3),(1,2,2,2)]:
    s=a+b
    for n in range(7):
        for xi in product((0,1),repeat=n):
            states=walk((u,v),a,b,xi)
            assert sum(states.values())==1
            checks+=1
            # exact quenched conditional mean product
            t=Q(u+v)
            predicted=(Q(u-v)/t)
            for k,r in enumerate(xi,1):
                predicted*=Q(1)-Q(2*b*r,t+k*s)
            assert moment(states,1)==predicted
            checks+=1
            # exact recurrence for second moment
            mu2=(Q(u-v)/t)**2
            for k,r in enumerate(xi,1):
                Tk=t+(k-1)*s; Tnew=Tk+s; kk=s-2*b*r
                mu2=((Tk**2+2*Tk*kk)*mu2+kk**2)/(Tnew**2)
            assert moment(states,2)==mu2
            checks+=1

# Independent random rules, brute-force integration vs exact one-step annealed formulas.
for (u,v,a,b) in [(1,1,1,2),(1,2,2,1),(3,2,2,2)]:
    s=a+b; t0=u+v
    for n in range(1,6):
        ps=[Q((i%3)+1,5) for i in range(n)]
        qmu=Q(u-v,t0); q2=qmu*qmu
        for k,p in enumerate(ps,1):
            T=t0+(k-1)*s; Tn=T+s
            qmu*=Q(1)-Q(2*b,Tn)*p
            q2=((T*T+2*T*(s-2*b*p))*q2+(1-p)*s*s+p*(s-2*b)**2)/Tn**2
        fullmean=Q(0); full2=Q(0); total=Q(0)
        for xi in product((0,1),repeat=n):
            wp=Q(1)
            for x,p in zip(xi,ps): wp*=p if x else (1-p)
            st=walk((u,v),a,b,xi)
            fullmean+=wp*moment(st,1)
            full2+=wp*moment(st,2)
            total+=wp
        assert total==1 and fullmean==qmu and full2==q2
        checks+=3

print(f'PASS: {checks} exact finite-horizon assertions; maximum 6 updates; rational masses and moments.')
