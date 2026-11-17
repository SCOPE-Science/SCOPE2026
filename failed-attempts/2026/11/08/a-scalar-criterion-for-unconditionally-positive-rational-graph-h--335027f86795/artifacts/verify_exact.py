"""Exact-rational spot checks for the stated spectral step formulas."""
from fractions import Fraction as Q
from itertools import product

def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))] for i in range(len(a))]

def eye(n):
    return [[Q(i==j) for j in range(n)] for i in range(n)]

def solve(a,b):
    n=len(a)
    c=[row[:] + rhs[:] for row,rhs in zip(a,b)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if c[i][j])
        c[j],c[pivot]=c[pivot],c[j]
        q=c[j][j];c[j]=[x/q for x in c[j]]
        for i in range(n):
            if i==j:continue
            z=c[i][j]
            if z:c[i]=[c[i][k]-z*c[j][k] for k in range(2*n)]
    return [row[n:] for row in c]

def lap(parts):
    n=sum(parts); labels=sum(([j]*v for j,v in enumerate(parts)),[])
    return [[Q((n-parts[labels[i]]) if i==j else (-1 if labels[i]!=labels[j] else 0)) for j in range(n)] for i in range(n)],labels

def r(z):
    return (z*z-6*z+12)/(z*z+6*z+12)

def step(L,h):
    n=len(L);L2=mul(L,L);I=eye(n)
    denom=[[I[i][j]+h*L[i][j]/2+h*h*L2[i][j]/12 for j in range(n)] for i in range(n)]
    numer=[[I[i][j]-h*L[i][j]/2+h*h*L2[i][j]/12 for j in range(n)] for i in range(n)]
    return mul(solve(denom,I),numer)

def spectral(parts,labels,h):
    n=sum(parts)
    ans=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if labels[i]!=labels[j]: value=(1-r(Q(n)*h))/n
            else:
                a=parts[labels[i]]
                value=Q(1,n)+(Q(1,a)-Q(1,n))*r(n*h)+(Q(i==j)-Q(1,a))*r((n-a)*h)
            row.append(value)
        ans.append(row)
    return ans

def main():
    cases=0; comparisons=0
    for parts,h in product([(1,1),(1,2),(1,5),(2,2),(2,3),(3,4),(1,1,3),(2,3,4),(3,3,3)],
                           [Q(1,20),Q(1,3),Q(1),Q(5),Q(20)]):
        L,labels=lap(parts)
        t=step(L,h)
        s=spectral(parts,labels,h)
        assert t==s,(parts,h,'spectral mismatch')
        assert all(x>0 for row in t for x in row),(parts,h,'sign mismatch')
        assert all(sum(row)==1 for row in t),(parts,h,'stochastic mismatch')
        cases+=1;comparisons+=len(t)**2
    L,_=lap((1,1,1,1))
    # A four-vertex path is not a complete multipartite graph.
    L=[[Q(v) for v in row] for row in [[1,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,1]]]
    t=step(L,Q(20))
    assert t[0][1]<0
    print('PASS cases=%d exact_entries=%d P4_h20_entry01=%s'%(cases,comparisons,t[0][1]))

if __name__=='__main__':main()
