"""Independent exhaustive validation for the crown-graph induced-forest enumerators.

Run: python verify.py. Standard library only. This is a finite diagnostic, not a proof.
"""
from collections import Counter
from math import comb


def crown_adj(n):
    N=2*n
    adj=[0]*N
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i]|=1<<(n+j)
                adj[n+j]|=1<<i
    return adj


def forest(mask,adj):
    unseen=mask
    while unseen:
        root=unseen&-unseen
        unseen^=root
        stack=[(root.bit_length()-1,-1)]
        while stack:
            u,parent=stack.pop()
            neighbors=adj[u]&mask
            while neighbors:
                b=neighbors&-neighbors
                neighbors^=b
                v=b.bit_length()-1
                if v==parent:
                    continue
                if not (unseen&b):
                    return False
                unseen^=b
                stack.append((v,u))
    return True


def coefficients(n):
    adj=crown_adj(n)
    allforests=Counter(); maximal=Counter(); observed=0
    for mask in range(1<<(2*n)):
        if not forest(mask,adj):continue
        allforests[mask.bit_count()]+=1
        rest=((1<<(2*n))-1)^mask
        maxed=True
        while rest:
            b=rest&-rest; rest^=b
            if forest(mask|b,adj):maxed=False;break
        if maxed:maximal[mask.bit_count()]+=1
        observed+=1
    return allforests,maximal,observed


def expected(n):
    # Coefficients from the derived all-forests closed form.
    a=Counter(); m=Counter()
    for k in range(n+1):
        a[k]+=2*comb(n,k)
        a[k+1]+=2*n*comb(n,k)
    a[0]-=1
    a[1]-=2*n
    a[2]-=n*n
    a[4]+=comb(n,2)*(2*n-3)
    a[5]+=n*(n-1)*(n-2)
    if n==3:
        m[5]=6
    elif n>=4:
        m[5]=n*(n-1)*(n-2)
        m[n+1]+=2*n
    return +a,+m


def main():
    tests=0;total=0
    for n in range(3,10):
        a,m,count=coefficients(n)
        ea,em=expected(n)
        assert a==ea,(n,'all',a,ea)
        assert m==em,(n,'maximal',m,em)
        assert sum(a.values())==count
        total+=(1<<(2*n));tests+=1
    print('VERIFY_OK graph_orders',tests,'all_candidate_subsets',total,'maximal_and_all_forest_polynomials',True)
if __name__=='__main__':main()
