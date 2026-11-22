"""Independent direct finite-field group enumeration for reflection-product laws."""
from fractions import Fraction
from collections import Counter


def field(q):
    assert q in (3, 5, 7, 9, 11)
    if q != 9:
        plus = lambda a,b: (a+b)%q
        times = lambda a,b: (a*b)%q
        neg = lambda a: (-a)%q
    else:
        # F_9 = F_3[z]/(z^2 + 1)
        plus = lambda a,b: ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        times = lambda a,b: (((a%3)*(b%3)+2*(a//3)*(b//3))%3)+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)
        neg = lambda a: ((-(a%3))%3)+3*((-(a//3))%3)
    sub = lambda a,b: plus(a,neg(b))
    return plus,times,neg,sub


def run(q,max_k):
    add,mul,neg,sub=field(q)
    one=1; zero=0; I=(1,0,0,1)
    def mat(A,B):
        a,b,c,d=A; e,f,g,h=B
        return (add(mul(a,e),mul(b,g)), add(mul(a,f),mul(b,h)),
                add(mul(c,e),mul(d,g)), add(mul(c,f),mul(d,h)))
    def det(A):
        a,b,c,d=A
        return sub(mul(a,d),mul(b,c))
    def trace(A): return add(A[0],A[3])
    R=[]; H=[]
    for a in range(q):
      for b in range(q):
        for c in range(q):
          for d in range(q):
            M=(a,b,c,d)
            if det(M)==1:H.append(M)
            if d==neg(a) and det(M)==neg(1):R.append(M)
    assert len(H)==q*(q*q-1), (q,len(H))
    assert len(R)==q*(q+1), (q,len(R))
    quad={mul(x,x) for x in range(1,q)}
    def chi(x):return 0 if x==0 else (1 if x in quad else -1)
    def frac_formula(g,k):
        t=trace(g); disc=sub(mul(t,t),(4%3 if q==9 else 4%q))
        if g==I or g==tuple(neg(a) for a in I):
            st=q
            co=Fraction((q-3)*(q+1)**2,4)
            kind='central'
        elif disc==0:
            st=0
            co=Fraction((q-3)*(q+1),4)
            kind='unipotent'
        elif chi(disc)==1:
            st=1
            co=-(q+1)
            kind='split'
        else:
            st=-1
            co=0
            kind='nonsplit'
        relative=1+Fraction(st,q**(2*k-1))+Fraction(2,q+1)**(2*k)*co
        return relative/Fraction(len(H)), kind
    counts=Counter(mat(a,b) for a in R for b in R)
    for g in H:
        t=trace(g); disc=sub(mul(t,t),(4%3 if q==9 else 4%q))
        if g==I or g==tuple(neg(a) for a in I): predicted=q*(q+1)
        elif disc==0:predicted=2*q
        else:predicted=q-chi(disc)
        assert counts[g]==predicted,(q,g,counts[g],predicted)
    dist=counts
    for k in range(1,max_k+1):
        Z=len(R)**(2*k)
        kinds=Counter()
        for g in H:
            expected,kind=frac_formula(g,k)
            assert Fraction(dist[g],Z)==expected,(q,k,g,dist[g],Z,expected,kind)
            kinds[kind]+=1
        tv=sum(abs(Fraction(dist[g],Z)-Fraction(1,len(H))) for g in H)/2
        chi2=sum((Fraction(dist[g]*len(H),Z)-1)**2 for g in H)/len(H)
        tv_exp=Fraction(2,q**(2*k-1)*(q*q-1))+Fraction((q-3)*(q+1),2*(q-1))*Fraction(2,q+1)**(2*k)
        chi2_exp=Fraction(q*q,q**(4*k)) + Fraction((q-3)*(q+1)**2,4)*Fraction(2,q+1)**(4*k)
        assert tv==tv_exp,(q,k,tv,tv_exp)
        assert chi2==chi2_exp,(q,k,chi2,chi2_exp)
        print('PASS',f'q={q}',f'k={k}',f'group={len(H)}',f'reflections={len(R)}',f'TV={tv}',f'chi2={chi2}',f'types={dict(kinds)}')
        if k<max_k:
            nxt=Counter()
            for g,x in dist.items():
                if x:
                    for h,y in counts.items():
                        nxt[mat(g,h)]+=x*y
            dist=nxt
    print('PASS full pair-convolution character formula for',q)

if __name__=='__main__':
    for q,k in ((3,4),(5,3),(7,2),(9,2),(11,1)):
        run(q,k)
    print('ALL TESTS PASSED')
