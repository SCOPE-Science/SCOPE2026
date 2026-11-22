"""Exact ridge-face dimension and Gram-sign checks for canonical multipartite edge polytopes."""
from itertools import combinations,product
from fractions import Fraction

def rank(vs):
    a=[list(map(Fraction,v)) for v in vs]; d=len(a)
    if not a:return 0
    n=len(a[0]);h=0
    for j in range(n):
        piv=next((i for i in range(h,d) if a[i][j]),None)
        if piv is None:continue
        a[h],a[piv]=a[piv],a[h];v=a[h][j]
        for l in range(j,n): a[h][l]/=v
        for i in range(h+1,d):
            c=a[i][j]
            if c:
                for l in range(j,n):a[i][l]-=c*a[h][l]
        h+=1
        if h==d:break
    return h

def check(parts):
    n=sum(parts); classes=[];groups=[]
    for a in parts:
        g=list(range(len(classes),len(classes)+a));groups.append(g);classes += [len(groups)-1]*a
    es=[(i,j) for i in range(n) for j in range(i+1,n) if classes[i]!=classes[j]]
    pts=[tuple(int(t in edge) for t in range(n)) for edge in es]
    normals=[]
    for v in range(n):normals.append(tuple(Fraction(1,n)-int(t==v) for t in range(n)))
    for g in groups:normals.append(tuple(int(t in g)-Fraction(len(g),n) for t in range(n)))
    facets=[lambda x,v=v: x[v]==0 for v in range(n)] + [lambda x,g=g:sum(x[t] for t in g)==1 for g in groups]
    dims=rank([tuple(pts[j][i]-pts[0][i] for i in range(n)) for j in range(1,len(pts))]); assert dims==n-1
    vals={};good=0;bad=0
    for i,j in combinations(range(n+len(parts)),2):
        supporting=[p for p in pts if facets[i](p) and facets[j](p)]
        fdim=rank([tuple(p[k]-supporting[0][k] for k in range(n)) for p in supporting[1:]]) if supporting else -1
        expected=i<n or j<n
        assert (fdim==n-3)==expected,(parts,i,j,fdim,expected)
        if not expected:bad+=1;continue
        dot=sum(x*y for x,y in zip(normals[i],normals[j])); norms=[sum(t*t for t in normals[z]) for z in (i,j)]
        cos2=dot**2/(norms[0]*norms[1]); assert cos2>0
        if j<n: want=Fraction(1,(n-1)**2);sign=-1; label='cc'
        elif i<n:
            a=parts[j-n]
            if classes[i]==j-n:want=Fraction(n-a,a*(n-1));sign=-1;label='inside'
            else:want=Fraction(a,(n-a)*(n-1));sign=1;label='outside'
        else:raise AssertionError
        assert cos2==want and (dot>0)==(sign>0),(parts,i,j,cos2,want)
        vals[label]=vals.get(label,0)+1;good+=1
    assert vals=={'cc':n*(n-1)//2,'inside':n,'outside':n*(len(parts)-1)},(parts,vals)
    return good,bad

if __name__=='__main__':
    data=[(3,3,3),(3,3,4),(3,4,5),(4,4,4),(3,3,3,3),(3,3,4,4)]
    t=[check(parts) for parts in data]
    print('MULTIPARTITE_EDGE_RIDGE_PASS profiles=%d ridge_pairs=%d nonridge_pairs=%d' %(len(t),sum(a for a,b in t),sum(b for a,b in t)))
