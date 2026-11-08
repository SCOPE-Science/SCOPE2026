"""Independent enumerative check for the finite-variable chain-spectrum product."""
from functools import lru_cache
from collections import Counter

@lru_cache(None)
def partitions(n, maxpart=None):
    if n == 0: return ((),)
    if maxpart is None: maxpart = n
    ans=[]
    for p in range(min(n,maxpart),0,-1):
        ans.extend((p,)+rest for rest in partitions(n-p,p))
    return tuple(ans)


def recurrence(maxn,k):
    a=[0]*(maxn+1);a[0]=1
    for ell in range(1,maxn+1):
        b=[0]*(maxn+1)
        for n in range(maxn+1):
            for m in range(min(k,n//ell)+1):
                b[n]+=a[n-m*ell]
        a=b
    return a

if __name__=='__main__':
    import json
    for k in (2,3,4,5):
        b=recurrence(13,k)
        for n in range(1,14):
            lhs=sum(max(Counter(p).values())<=k for p in partitions(n))
            rhs=sum(all(ell%(k+1)!=0 for ell in p) for p in partitions(n))
            assert b[n]==lhs==rhs,(k,n,b[n],lhs,rhs)
        print(json.dumps({'width':k,'minimum_order_coefficients_1_to_13':b[1:],'all_partition_correspondences_pass':True},sort_keys=True))
    print('PARTITION_VERIFY_OK')
