"""Pure-integer enclosure for the King degree-1--9 BV/L1 boundary comparison."""
from math import comb

Q = 1 << 20
M = 10080  # divisible by every degree 1,...,9


def rho_floor(n, i):
    # r+(n-1)r^2 = n(i/M)^2, with r replaced by integer k/Q.
    lo, hi = 0, Q
    while lo < hi:
        k = (lo + hi + 1) // 2
        if M*M*(k*Q+(n-1)*k*k) <= n*i*i*Q*Q:
            lo = k
        else:
            hi = k-1
    return lo


def tail_numerators(n, k):
    # P(Bin(n,k/Q)>=j)*Q^n, j=1,...,n
    b = [comb(n,ell)*pow(k,ell)*pow(Q-k,n-ell) for ell in range(n+1)]
    tails=[0]*(n+1)
    v=0
    for j in range(n,0,-1):
        v+=b[j]
        tails[j]=v
    return tails


def intervals(n):
    d = Q**n
    lo = [[0]*(M+1) for _ in range(n+1)]
    hi = [[0]*(M+1) for _ in range(n+1)]
    for i in range(M+1):
        k=rho_floor(n,i)
        t0=tail_numerators(n,k)
        t1=tail_numerators(n,min(k+1,Q))
        for j in range(1,n+1):
            lo[j][i]=t0[j]
            hi[j][i]=t1[j]
    out={}
    for j in range(1,n+1):
        # prefix low at left nodes and high at right nodes
        pre_l=[0]*(M+1); pre_h=[0]*(M+1)
        for i in range(M):
            pre_l[i+1]=pre_l[i]+lo[j][i]
            pre_h[i+1]=pre_h[i]+hi[j][i+1]
        for edge,k in [('R',(j-1)*M//n),('L',j*M//n)]:
            low_num=pre_l[k]+(M-k)*d-(pre_h[M]-pre_h[k])
            high_num=pre_h[k]+(M-k)*d-(pre_l[M]-pre_l[k])
            assert 0<=low_num<=high_num<=M*d
            out[(j,edge)]=(low_num,high_num,M*d)
    return out

if __name__=='__main__':
    import time
    start=time.monotonic()
    for n in range(1,10):
        out=intervals(n)
        b=out[(1,'R')]
        print('n=',n,'boundary interval=',tuple(round(z/b[2],9) for z in b[:2]))
        if n<=8:
            for key,(lo,hi,denom) in out.items():
                if key!=(1,'R'):
                    assert b[0]>hi, ('boundary gap not verified',n,key,float(b[0]/denom),float(hi/denom))
            print('  strictly dominates all',len(out)-1,'competitors')
        else:
            j4=out[(4,'R')]
            for key,(lo,hi,denom) in out.items():
                if key!=(4,'R'):
                    assert j4[0]>hi, ('degree-nine unique optimum unverified',key)
            print('  interior j=4 interval=',tuple(round(z/j4[2],9) for z in j4[:2]))
            print('  interior j=4 strictly dominates all', len(out)-1, 'competitors')
    print('EXACT_INTEGER_RIEMANN_ENCLOSURE_PASS; elapsed:',round(time.monotonic()-start,3),'seconds')
