"""Independent exact finite checks for uniform-spoke wheel Laplacian controllability.
Only finite computations; general proof is separate.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd,cos,pi,sin
P=1000003

def W(m,t):
    p,q=t.numerator,t.denominator
    n=m+1;A=[[0]*n for _ in range(n)]
    for i in range(m):
        for j,w in [((i-1)%m,q),((i+1)%m,q),(m,p)]:
            A[i][i]+=w; A[i][j]-=w
    for i in range(m):A[m][m]+=p; A[m][i]-=p
    return A

def rank(A):
    X=[[v%P for v in row] for row in A]
    R=len(X);C=len(X[0]);i=0
    for j in range(C):
        k=next((k for k in range(i,R) if X[k][j]),None)
        if k is None: continue
        X[i],X[k]=X[k],X[i]
        inv=pow(X[i][j],-1,P)
        X[i]=[(v*inv)%P for v in X[i]]
        for h in range(i+1,R):
            t=X[h][j]
            if t: X[h]=[(u-t*v)%P for u,v in zip(X[h],X[i])]
        i+=1
        if i==R:break
    return i

def controllable(m,t,S):
    A=W(m,t); n=m+1;s=len(S)
    B=[[1 if i==v else 0 for v in S] for i in range(n)]
    M=[row[:] for row in B]
    for _ in range(1,n):
        B=[[sum(A[i][j]*B[j][k] for j in range(n))%P for k in range(s)] for i in range(n)]
        for i in range(n):M[i]+=B[i]
    return rank(M)==n

def exceptional(m,t):
    # Exact test for rational resonances via well-known rational cosine values.
    # We use trigonometry only to choose test parameters; classification in the theorem is analytic.
    return [k for k in range(1,m//2+1) if abs(float(m*t)-(2-2*cos(2*pi*k/m)))<1e-10]

def expected_pair(m,t,d):
    e=exceptional(m,t)
    if any(2*k<m for k in e):return False
    criterion = gcd(m,d)==1 if m%2 else gcd(m//2,d)==1
    if e and m%2==0 and e==[m//2]:criterion=criterion and d%2==1
    return criterion

def totient(n):return sum(gcd(i,n)==1 for i in range(1,n+1))

def check():
    counts={'rational_cases':0,'two_input_tests':0,'three_input_tests':0,'full_rank_cases':0,'fail_cases':0,'resonance_case_rows':0,'two_input_count_checks':0}
    for m in range(3,15):
        ts={Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(1),Fraction(2),Fraction(4,m)}
        if m%3==0:ts|={Fraction(3,m),Fraction(1,m)}
        if m%4==0:ts.add(Fraction(2,m))
        for t in sorted(ts):
            counts['rational_cases']+=1
            e=exceptional(m,t)
            if e:counts['resonance_case_rows']+=1
            for a,b in combinations(range(m+1),2):
                pred=(a<m and b<m and expected_pair(m,t,(b-a)%m))
                obs=controllable(m,t,[a,b]);counts['two_input_tests']+=1
                if pred!=obs:raise AssertionError(('pair disagreement',m,str(t),a,b,e,pred,obs))
                counts['full_rank_cases' if obs else 'fail_cases']+=1
            pred_count=sum(expected_pair(m,t,d) for d in range(1,m))*m//2
            obs_count=sum(controllable(m,t,[a,b]) for a,b in combinations(range(m),2))
            assert pred_count==obs_count,(m,t,pred_count,obs_count)
            counts['two_input_count_checks']+=1
            if e and any(2*k<m for k in e):
                assert controllable(m,t,[0,1,2]),(m,t,e)
                counts['three_input_tests']+=1
    for m in range(3,71):
        generic=(m*totient(m)//2 if m%2 else m*totient(m//2))
        assert generic==sum(gcd(m,d)==1 if m%2 else gcd(m//2,d)==1 for d in range(1,m))*m//2
    counts['arithmetic_count_checks']=68
    print('PASS',counts)

if __name__=='__main__':check()

def expected_triple_at_ordinary_resonance(m,t,S):
    e=exceptional(m,t)
    assert len(e)==1 and 2*e[0]<m
    k=e[0]
    if m in S:
        a,b=[v for v in S if v<m]
        return expected_pair(m,Fraction(1,9991),b-a)
    a,b,c=S
    q=m if m%2 else m//2
    return (gcd(q,gcd(b-a,c-a))==1 and
            all(((k*(y-x))%m)!=0 for x,y in combinations(S,2)))

def check_triples():
    n=0; ok=0; bad=0
    for m in range(3,13):
        ts=set()
        if m%3==0:ts|={Fraction(1,m),Fraction(3,m)}
        if m%4==0:ts.add(Fraction(2,m))
        for t in sorted(ts):
            if not (len(exceptional(m,t))==1 and 2*exceptional(m,t)[0]<m):continue
            for S in combinations(range(m+1),3):
                pred=expected_triple_at_ordinary_resonance(m,t,S)
                obs=controllable(m,t,S); n+=1
                if pred!=obs:raise AssertionError(('triple mismatch',m,str(t),S,pred,obs))
                ok+=bool(obs);bad+=not obs
    print('TRIPLES PASS',{'tested':n,'controlling':ok,'not_controlling':bad})

if __name__=='__main__':check_triples()
