"""Exact test harness for positivity thresholds of Heun steps on weighted multipartite diffusion.

No external dependencies are used for exact-rational checks. Optional NumPy
is used only in the independent fractional-spectral reconstruction.
"""
from fractions import Fraction as F
from itertools import product
import math


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for a in range(minimum, n + 1):
            for tail in partitions(n - a, a):
                yield (a,) + tail


def matmul(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def exact_check(parts, weights):
    n = sum(parts)
    part_index = [k for k, num in enumerate(parts) for _ in range(num)]
    assert len(weights) == len(parts)
    L = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i):
            w = F(1) if part_index[i] != part_index[j] else weights[part_index[i]]
            L[i][j] = L[j][i] = -w
            L[i][i] += w
            L[j][j] += w
    L2 = matmul(L,L)
    limits = [F(2)]
    for r, size in enumerate(parts):
        if size < 2: continue
        a = F(n-size,n)
        e = a + (1-a)*weights[r]
        if weights[r]>1:
            limits.append(F(2)*(e-a)/(e*e-a))
    limit = min(limits)
    for t in [F(0), limit/F(2),limit,limit+F(1,10),F(2),F(3)]:
        h=t/n
        P=[[F(i==j)-h*L[i][j]+h*h*L2[i][j]/2 for j in range(n)] for i in range(n)]
        assert all(sum(row)==1 for row in P)
        positive=all(z>=0 for row in P for z in row)
        assert positive == (t<=limit), (parts,weights,t,limit,'matrix threshold')
        assert all(P[i][i]>0 for i in range(n))
        f=lambda z: 1-z+z*z/2
        for i in range(n):
            for j in range(n):
                if i==j: continue
                if part_index[i]!=part_index[j]:
                    predicted=t/F(n)*(1-t/2)
                else:
                    r=part_index[i]; a=F(n-parts[r],n); e=a+(1-a)*weights[r]
                    predicted=t/(n*(1-a))*((e-a)-t*(e*e-a)/2)
                assert P[i][j]==predicted, (parts,weights,i,j,t,P[i][j],predicted)
    return 1


def main():
    cases=0
    choices=[F(0),F(1,2),F(1),F(3,2),F(3)]
    for n in range(2,9):
        for parts in partitions(n):
            if len(parts)<2:continue
            # only weights of nonsingleton blocks matter
            r=[i for i,z in enumerate(parts) if z>1]
            for vals in product(choices,repeat=len(r)):
                weights=[F(0)]*len(parts)
                for i,val in zip(r,vals):weights[i]=val
                cases+=exact_check(parts,weights)
    print('EXACT_RATIONAL_CASES',cases)
    try:
        import numpy as np
    except ImportError:
        print('NO_NUMPY_SPECTRAL_TEST')
        return
    checked=0
    for parts in [(2,2),(2,3),(1,2,3),(3,3),(1,2,2,3),(2,2,4)]:
        n=sum(parts)
        idx=[r for r,nr in enumerate(parts) for _ in range(nr)]
        L=np.zeros((n,n))
        for i in range(n):
            for j in range(i):
                if idx[i]!=idx[j]:
                    L[i,j]=L[j,i]=-1
                    L[i,i]+=1;L[j,j]+=1
        eigen,U=np.linalg.eigh(L)
        for alpha,beta in [(0.2,1.0),(0.5,1.0),(0.5,7.0),(0.81,15.0)]:
            Lalpha=(U*(np.where(eigen>1e-9,eigen,0)**alpha))@U.T
            newW=np.zeros((n,n))
            for i in range(n):
                for j in range(i):
                    w=1 if idx[i]!=idx[j] else -beta*Lalpha[i,j]
                    newW[i,j]=newW[j,i]=w
            newL=np.diag(newW.sum(axis=1))-newW
            for r,m in enumerate(parts):
                if m<2:continue
                a=(n-m)/n
                wr=beta*n**(alpha-1)*(a**alpha-a)/(1-a)
                ix=[i for i in range(n) if idx[i]==r]
                if m>1:
                    assert abs(newW[ix[0],ix[1]]-wr)<1e-9
            q=np.sort(np.linalg.eigvalsh(newL))
            target=[0]+[n]*(len(parts)-1)
            for r,m in enumerate(parts):
                a=(n-m)/n
                wr=beta*n**(alpha-1)*(a**alpha-a)/(1-a)
                target.extend([n*(a+(1-a)*wr)]*(m-1))
            assert np.max(np.abs(q-np.sort(target)))<1e-7, (parts,alpha,beta,q,target)
            checked+=1
    print('FRACTIONAL_SPECTRAL_CASES',checked)
    print('VERIFY_OK')

if __name__=='__main__':main()
