"""Direct checks of acyclic sink enumerators on clique bouquets."""
from itertools import product
from math import factorial


def graph_edges(sizes):
    parts=[]
    v=1
    for s in sizes:
        parts.append(tuple(range(v,v+s)))
        v+=s
    edges=[]
    for part in parts:
        block=(0,)+part
        for i,a in enumerate(block):
            for b in block[i+1:]:
                edges.append((a,b))
    return v,edges


def direct_polynomial(sizes):
    n,edges=graph_edges(sizes)
    hist=[0]*(len(sizes)+1)
    for mask in range(1<<len(edges)):
        indeg=[0]*n
        outdeg=[0]*n
        adj=[[] for _ in range(n)]
        for k,(u,v) in enumerate(edges):
            if mask>>k&1: u,v=v,u
            adj[u].append(v)
            indeg[v]+=1
            outdeg[u]+=1
        avail=[i for i in range(n) if indeg[i]==0]
        num=0
        while avail:
            i=avail.pop();num+=1
            for j in adj[i]:
                indeg[j]-=1
                if indeg[j]==0:avail.append(j)
        if num==n:
            hist[sum(d==0 for d in outdeg)]+=1
    return hist


def theorem_polynomial(sizes):
    p=[1]
    for a in sizes:
        q=[0]*(len(p)+1)
        for i,v in enumerate(p):
            q[i]+=v
            q[i+1]+=a*v
        p=q
    p[0]-=1
    p[1]+=1
    scale=1
    for a in sizes:scale*=factorial(a)
    return [scale*v for v in p]


def discriminant(a,b,c):
    e1=a+b+c;e2=a*b+a*c+b*c;e3=a*b*c
    return e2*e2-4*e3*(1+e1)


def run():
    cases=0
    for r in range(2,6):
        for sizes in product((1,2,3),repeat=r):
            n,edges=graph_edges(sizes)
            if len(edges)>14:continue
            direct=direct_polynomial(sizes)
            pred=theorem_polynomial(sizes)
            assert direct==pred,(sizes,direct,pred)
            cases+=1
    print('DIRECT_EDGE_ORIENTATIONS_OK',cases)
    lc_cases=0
    for r in range(3,8):
        for sizes in product((1,2,3,5),repeat=r):
            if lc_cases>120000:break
            p=theorem_polynomial(sizes)
            assert sum(p)==__import__('math').prod(factorial(s+1) for s in sizes)
            for i in range(2,r):
                assert p[i]**2>p[i-1]*p[i+1],(sizes,i)
            lc_cases+=1
    print('PRODUCT_SUM_AND_STRICT_LOG_CONCAVITY_OK',lc_cases)
    for a,b,c in product(range(1,45),repeat=3):
        assert discriminant(a,b,c)==a*a*(b-c)**2-2*a*b*c*(b+c+2)+b*b*c*c
    for k in range(1,55):
        for a in range(1,55):
            assert (discriminant(a,k,k)>=0)==(4*a*(k+1)<=k*k)
    assert discriminant(1,5,5)>0 and discriminant(2,5,5)<0
    assert discriminant(1,1,1)<0
    for a in range(1,1001):
        assert (discriminant(a,5,6)>=0)==(a==1 or a>=779)
    print('DISCRIMINANT_EXACT_AND_PARITY_BOUNDARIES_OK')
    print('VERIFY_OK')

if __name__=='__main__':run()
