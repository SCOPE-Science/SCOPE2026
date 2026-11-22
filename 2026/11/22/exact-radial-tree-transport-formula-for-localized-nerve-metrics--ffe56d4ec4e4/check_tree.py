"""Exact finite tests of the radial-tree representation of localized nerve costs.

Requires Python 3, NumPy and SciPy. The proof for all finite ultrametrics is in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations
import random
import numpy as np
from scipy.optimize import linprog


def direct_cost(d, m, r):
    n = len(d)
    k = [max(0.0, r-d[m][i]) for i in range(n)]
    return np.array([[min(k[i], k[j])*d[i][j] + 2*r*abs(k[i]-k[j])
                      for j in range(n)] for i in range(n)], dtype=float)


def radial_tree(d, m, r):
    n = len(d)
    edges = []
    sites = {m: 0}
    num_nodes = 1
    def node(parent, length):
        nonlocal num_nodes
        assert length >= -1e-9, (parent, length)
        child = num_nodes
        num_nodes += 1
        edges.append((parent, child, max(0., length)))
        return child

    def shell(cluster, parent, upper, alpha):
        if len(cluster) == 1:
            sites[cluster[0]] = node(parent, alpha*upper)
            return
        diameter = max(d[i][j] for i,j in combinations(cluster,2))
        here = parent if abs(upper-diameter) <= 1e-9 else node(parent, alpha*(upper-diameter))
        unseen = set(cluster)
        pieces=[]
        while unseen:
            x=unseen.pop()
            component = {y for y in unseen if d[x][y] < diameter-1e-9}
            # Ultrametricity makes this transitive, so pairwise comparison to x suffices.
            unseen -= component
            pieces.append([x]+sorted(component))
        for part in pieces:
            shell(part, here, diameter, alpha)

    radii=sorted({d[m][i] for i in range(n) if 0 < d[m][i] < r})
    prev=0.
    trunk=0
    H=lambda t: (5*r*t-t*t)/2
    for t in radii:
        trunk=node(trunk, H(t)-H(prev))
        cluster=[i for i in range(n) if abs(d[m][i]-t)<1e-9]
        shell(cluster, trunk, t, (r-t)/2)
        prev=t
    outside=node(trunk, H(r)-H(prev))
    for i in range(n):
        if d[m][i]>=r-1e-9:sites[i]=outside
    assert len(sites)==n, (sites, n)
    return edges, sites, num_nodes


def tree_distance(edges, sites, num_nodes, i, j):
    g=defaultdict(list)
    for u,v,w in edges:
        g[u].append((v,w));g[v].append((u,w))
    target=sites[j]
    stack=[(sites[i],-1,0.)]
    while stack:
        u,p,dis=stack.pop()
        if u==target:return dis
        for v,w in g[u]:
            if v!=p:stack.append((v,u,dis+w))
    raise AssertionError('disconnected tree')


def tree_transport(edges, sites, num_nodes, mu, nu):
    imbalance=np.zeros(num_nodes)
    for i,leaf in sites.items():imbalance[leaf]+=mu[i]-nu[i]
    total=0.
    for parent,child,length in reversed(edges):
        total+=length*abs(imbalance[child])
        imbalance[parent]+=imbalance[child]
    assert abs(imbalance[0])<1e-8
    return total


def linear_transport(cost, mu, nu):
    n=len(mu)
    A=np.zeros((2*n,n*n))
    for i in range(n):
        for j in range(n):
            A[i,i*n+j]=1.
            A[n+j,i*n+j]=1.
    out=linprog(cost.flatten(),A_eq=A,b_eq=np.r_[mu,nu],bounds=(0,None),method='highs')
    assert out.success,out.message
    return out.fun


def random_ultrametric(n,seed):
    rg=random.Random(seed)
    d=[[0.]*n for _ in range(n)]
    groups=[{i} for i in range(n)]
    height=0.
    while len(groups)>1:
        a,b=rg.sample(range(len(groups)),2)
        height+=rg.choice([1.,2.,3.])
        for i in groups[a]:
            for j in groups[b]:d[i][j]=d[j][i]=height
        groups=[group for idx,group in enumerate(groups) if idx not in (a,b)]+[groups[a]|groups[b]]
    return d,height


def four_point(c):
    n=len(c)
    for a,b,x,y in combinations(range(n),4):
        sums=sorted((c[a,b]+c[x,y],c[a,x]+c[b,y],c[a,y]+c[b,x]))
        if abs(sums[-1]-sums[-2])>1e-8:return False
    return True


def main():
    count=0
    examples=[]
    for n in range(2,10):
        for seed in range(30):
            d,diam=random_ultrametric(n, 10000*n+seed)
            for r in [diam/4, diam/2, diam]:
                mu=np.arange(1,n+1,dtype=float);mu/=mu.sum()
                nu=np.arange(n,0,-1,dtype=float);nu/=nu.sum()
                for m in range(n):
                    cost=direct_cost(d,m,r)
                    assert four_point(cost)
                    edges,sites,num_nodes=radial_tree(d,m,r)
                    for i in range(n):
                        for j in range(n):
                            got=tree_distance(edges,sites,num_nodes,i,j)
                            assert abs(got-cost[i,j])<1e-8,(n,m,r,i,j,got,cost[i,j])
                    for a,b in [(mu,nu), (np.eye(n)[0],np.eye(n)[-1])]:
                        got=tree_transport(edges,sites,num_nodes,a,b)
                        exp=linear_transport(cost,a,b)
                        assert abs(got-exp)<1e-7,(n,m,r,got,exp)
                    count+=1
                    if n==4 and seed==0 and m==0 and r==diam:examples.append((n,r,len(edges),tree_transport(edges,sites,num_nodes,mu,nu)))
    # The ultrametric restriction matters: a 4-point line gives a non-tree cost.
    line=[[abs(i-j) for j in range(4)] for i in range(4)]
    non_tree=direct_cost(line,1,2.)
    assert not four_point(non_tree)
    print('Verified finite ultrametric (n,seed,r,center) cases:',count)
    print('Every tree distance, four-point test, and two independent transport LPs: PASS')
    print('Representative n=4:',examples)
    print('4-point line boundary is not a tree pseudometric: PASS')

if __name__=='__main__': main()
