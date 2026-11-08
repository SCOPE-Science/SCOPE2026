"""Exact finite checks for sharp Lipschitz variance on rectangular disjointness graphs.

Run with Python 3 (standard library only). This is finite corroboration;
the theorem for all parameters is proved by the analytic/combinatorial argument.
"""
from itertools import product


def predicted_numerator(a, b):
    n = a * b
    return max(n*n//4, n*max(a,b) - max(a,b)%2,
               n*(a+b-1) - (a+b-3)**2)


def independent_direct_search(a, b):
    n=a*b
    edges=[(i*b+j, k*b+l) for i in range(a) for j in range(b)
           for k in range(i+1,a) for l in range(b) if j!=l]
    best=-1
    count=0
    for x in product(range(3),repeat=n):
        if min(x)!=0:continue
        if any(abs(x[u]-x[v])>1 for u,v in edges):continue
        numer=n*sum(t*t for t in x)-sum(x)**2
        if numer>best: best=numer;count=0
        if numer==best:count+=1
    assert best==predicted_numerator(a,b),(a,b,best,predicted_numerator(a,b))
    print('INDEPENDENT_DIRECT_ALL_INTEGER_LIPSCHITZ_ASSIGNMENTS_OK',a,b,best,count)


def exhaustive_cross_groups(a,b):
    n=a*b;full=(1<<n)-1
    rook=[]
    for i in range(a):
        for j in range(b):
            rook.append(sum(1<<(k*b+l) for k in range(a) for l in range(b)
                            if k==i or l==j))
    cands=[0]*(1<<n);cands[0]=full
    best=-1;classes={}
    for A in range(1,1<<n):
        low=A&-A
        cands[A]=cands[A^low]&rook[low.bit_length()-1]
        allowed=cands[A]&~A
        B=allowed
        while B:
            va=A.bit_count();vb=B.bit_count()
            v=n*(va+vb)-(va-vb)**2
            if v>=best:
                if v>best: best=v;classes={}
                supp=A|B
                row=any(all(not((supp>>(i*b+j))&1) or i==r
                            for i in range(a) for j in range(b)) for r in range(a))
                col=any(all(not((supp>>(i*b+j))&1) or j==s
                            for i in range(a) for j in range(b)) for s in range(b))
                if row or col:
                    label='full_row_or_column' if va+vb==max(a,b) and abs(va-vb)<=1 else 'OTHER'
                elif min(va,vb)==1 and max(va,vb)==a+b-2:
                    label='full_cross_star'
                elif va==vb==2 and a==b==3:
                    label='checkerboard'
                else:label='OTHER'
                classes[label]=classes.get(label,0)+1
            B=(B-1)&allowed
    assert 'OTHER' not in classes,(a,b,classes)
    assert max(best,n*n//4)==predicted_numerator(a,b),(a,b,best)
    print('EXHAUSTIVE_ALL_SEPARATED_EXTREME_SETS_OK',a,b,best,classes)


def phase():
    for a in range(3,300):
        for b in range(a,300):
            n=a*b
            nums=[n*n//4,n*b-b%2,n*(a+b-1)-(a+b-3)**2]
            mx=max(nums)
            phase={
                'star':nums[2]==mx,
                'row':nums[1]==mx,
                'binary':nums[0]==mx}
            expected={
                'star':(a==3 and b<=6) or (a==4 and b<=9) or (a==5 and b<=6),
                'row':(a==3 and b>=6) or (a==4 and b>=10 and b%2==0),
                'binary':(a==4 and b>=10) or (a==5 and b>=7) or a>=6}
            assert phase==expected,(a,b,phase,expected,nums)
    print('EXACT_THREE_REGIME_PHASE_AND_TIE_CERTIFICATE_OK',sum(300-a for a in range(3,300)))

if __name__=='__main__':
    for a,b in [(3,3),(3,4)]:independent_direct_search(a,b)
    for a,b in [(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]: exhaustive_cross_groups(a,b)
    phase()
    print('ALL_RECTANGULAR_DISJOINTNESS_SPREAD_CHECKS_OK')
