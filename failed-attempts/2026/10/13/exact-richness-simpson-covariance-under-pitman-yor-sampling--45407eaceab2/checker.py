from fractions import Fraction
from math import comb

def rising(x,m,step=1):
    z=Fraction(1)
    for j in range(m): z*=x+j*step
    return z

def partitions(n):
    # canonical restricted-growth strings -> blocks
    out=[]
    def rec(i, lab, mx):
        if i==n:
            blocks=[[] for _ in range(mx+1)]
            for x,a in enumerate(lab): blocks[a].append(x)
            out.append(blocks); return
        for a in range(mx+2):
            if a<=mx+1:
                lab.append(a); rec(i+1,lab,max(mx,a)); lab.pop()
    # first label 0; next label <= max+1
    def rr(i,lab,mx):
        if i==n:
            blocks=[[] for _ in range(mx+1)]
            for x,a in enumerate(lab): blocks[a].append(x)
            out.append(blocks); return
        for a in range(mx+2):
            lab.append(a); rr(i+1,lab,max(mx,a)); lab.pop()
    rr(1,[0],0)
    return out

def prob(blocks,a,t,n):
    k=len(blocks)
    num=rising(t+a,k-1,a) if k>1 else Fraction(1)
    den=rising(t+1,n-1)
    for b in blocks: num*=rising(1-a,len(b)-1)
    return num/den

def R(n,a,t):
    z=Fraction(1)
    for j in range(2,n): z*=Fraction(t+j+a,t+j)
    return z

def check(n,a,t):
    ps=partitions(n)
    total=EK=EQ=EKQ=Fraction(0)
    pS=kS=pD=kD=Fraction(0)
    for bs in ps:
        p=prob(bs,a,t,n); total+=p
        k=len(bs)
        pair=sum(len(b)*(len(b)-1) for b in bs)
        q=Fraction(pair,n*(n-1))
        EK += p*k; EQ += p*q; EKQ += p*k*q
        same=any(0 in b and 1 in b for b in bs)
        if same: pS+=p; kS+=p*k
        else: pD+=p; kD+=p*k
    assert total==1
    r=R(n,a,t)
    A=Fraction((1-a)*(t+a),(t+1)*(t+1))*r
    assert EQ==Fraction(1-a,t+1)
    assert EKQ-EK*EQ == -A
    assert kD/pD-kS/pS == r
    H=Fraction(1,n)+Fraction(n-1,n)*EQ
    covH=Fraction(n-1,n)*(EKQ-EK*EQ)
    assert covH == -Fraction(n-1,n)*A
    return len(ps)

cases=[(Fraction(0),Fraction(1)),(Fraction(0),Fraction(3)),(Fraction(1,3),Fraction(2)),(Fraction(1,2),Fraction(1,2)),(Fraction(2,3),Fraction(0))]
count=0; objs=0
for a,t in cases:
    for n in range(2,9):
        objs += check(n,a,t); count+=1
# recurrence/closed form checks rational many n
recur=0
for a,t in [(Fraction(1,3),Fraction(2)),(Fraction(2,5),Fraction(7,4)),(Fraction(0),Fraction(5,2))]:
    for n in range(2,501):
        r=R(n,a,t)
        rn=R(n+1,a,t)
        assert rn==r*Fraction(t+n+a,t+n)
        if a==0: assert r==1
        recur+=1
print('VERIFY_OK')
print('parameter_n_enumeration_cases=',count,sep='')
print('set_partitions_evaluated=',objs,sep='')
print('recurrence_checks=',recur,sep='')
print('max_recurrence_n=500')
