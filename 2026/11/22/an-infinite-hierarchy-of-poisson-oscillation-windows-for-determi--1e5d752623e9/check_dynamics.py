"""Independent direct finite-state check of open-neighborhood plurality with retained ties."""
import itertools, math, sys

def step(x, q):
    n=len(x); out=[]
    for i,a in enumerate(x):
        count=[0]*q
        for j,b in enumerate(x):
            if j!=i: count[b]+=1
        m=max(count)
        top=[v for v,c in enumerate(count) if c==m]
        out.append(top[0] if len(top)==1 else a)
    return tuple(out)

def predicted(x,q):
    c=[x.count(k) for k in range(q)]
    mx=max(c)
    nmax=c.count(mx)
    if nmax==1:
        return 1 # one update to a fixed state, perhaps initial unanimity already fixed
    if nmax==2:
        return 2 # initially period 2
    return 0 # initially fixed

def closed_count(n,q):
    from fractions import Fraction
    z=0
    for m in range(1,n//2+1):
        rem=n-2*m
        # coefficient of (E_{m-1}(z))^(q-2): exact factorial weighting via DP
        dp=[0]*(rem+1);dp[0]=1
        # use integer coefficients of exponential series times rem! via multinomial recurrence
        # represent coefficient a_j * j!
        for _ in range(q-2):
            nd=[0]*(rem+1)
            for k,a in enumerate(dp):
                if a:
                    for j in range(min(m-1,rem-k)+1):
                        nd[k+j] += a*math.comb(k+j,j)
            dp=nd
        z+=math.comb(q,2)*math.comb(n,m)*math.comb(n-m,m)*dp[rem]
    return z

if __name__=='__main__':
    for q in range(2,6):
        for n in range(2,9):
            osc=0;fixed=0;cons=0
            for x in itertools.product(range(q),repeat=n):
                y=step(x,q); yy=step(y,q)
                p=predicted(x,q)
                if p==2:
                    assert y!=x and yy==x, (x,y,yy)
                    osc+=1
                elif p==0:
                    assert y==x, (x,y)
                    fixed+=1
                else:
                    assert len(set(y))==1 and step(y,q)==y,(x,y)
                    cons+=1
            expected=closed_count(n,q)
            assert osc==expected,(n,q,osc,expected)
            print('n=%d q=%d states=%d oscillatory=%d fixed=%d immediate_consensus=%d formula=%d'%(n,q,q**n,osc,fixed,cons,expected))
    print('ALL_CHECKS_PASSED')
