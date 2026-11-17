"""Exact, finite verification of 2-by-q Monge ridge classification (q=2..7).
Checks the face rank against a separately generated exact vertex list.
This finite check is supplementary to the general symbolic proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def matrix_rank(rows):
    if not rows: return 0
    a=[[Fraction(v) for v in row] for row in rows]
    n,m=len(a),len(a[0]); pivot=0
    for j in range(m):
        k=next((i for i in range(pivot,n) if a[i][j]),None)
        if k is None:continue
        a[pivot],a[k]=a[k],a[pivot]
        z=a[pivot][j]
        for t in range(j,m):a[pivot][t]/=z
        for i in range(pivot+1,n):
            if a[i][j]:
                mult=a[i][j]
                for t in range(j,m):a[i][t]-=mult*a[pivot][t]
        pivot+=1
        if pivot==n:return pivot
    return pivot


def verts(q):
    vs=[]
    for row in range(2):
        v=[Fraction(0) for _ in range(2*q)]
        for j in range(q):v[row*q+j]=Fraction(1,q)
        vs.append(tuple(v))
    for j in range(q):
        v=[Fraction(0) for _ in range(2*q)]
        for r in range(2):v[r*q+j]=Fraction(1,2)
        vs.append(tuple(v))
    for b in range(1,q):
        for row,cols in ((0,range(q-b,q)),(1,range(0,b))):
            v=[Fraction(0) for _ in range(2*q)]
            for j in cols:v[row*q+j]=Fraction(1,b)
            vs.append(tuple(v))
    assert len(set(vs))==3*q
    return vs


def facets(q):
    out=[]
    for j in range(q-1):out.append(('F',j))
    for r in range(2):
        for j in range(q):out.append(('G',r,j))
    return out


def tight(v,f,q):
    if f[0]=='F':
        j=f[1]
        return v[j]+v[q+j+1]==v[j+1]+v[q+j]
    return v[f[1]*q+f[2]]==0


def normal(f,q):
    n=2*q
    if f[0]=='F':
        j=f[1];v=[Fraction(0)]*n
        for at,c in ((j,1),(j+1,-1),(q+j,-1),(q+j+1,1)):v[at]=Fraction(c)
        return v
    at=f[1]*q+f[2]
    v=[Fraction(1,n)]*n
    v[at]-=1
    return v


def gram_cosine(f,g,q):
    a,b=normal(f,q),normal(g,q)
    dot=sum(x*y for x,y in zip(a,b))
    aa=sum(x*x for x in a);bb=sum(y*y for y in b)
    return dot, dot*dot/(aa*bb)


def expected(f,g,q):
    if f[0]=='F' and g[0]=='F':return True
    if f[0]=='F' or g[0]=='F':return True
    if f[1]==g[1]:return True
    i=f[2] if f[1]==0 else g[2]
    k=g[2] if g[1]==1 else f[2]
    return i<=k


def main():
    for q in range(2,8):
        vs=verts(q);fs=facets(q)
        classes={'F-adjacent':0,'F-disjoint':0,'FG-negative':0,'FG-positive':0,'FG-orthogonal':0,'GG':0}
        for f,g in combinations(fs,2):
            common=[v for v in vs if tight(v,f,q) and tight(v,g,q)]
            rank=matrix_rank([[v[i]-common[0][i] for i in range(2*q)] for v in common[1:]]) if common else -1
            isridge=rank==2*q-3
            assert isridge==expected(f,g,q),(q,f,g,rank,isridge,expected(f,g,q))
            if not isridge:continue
            if f[0]==g[0]=='F':key='F-adjacent' if abs(f[1]-g[1])==1 else 'F-disjoint'
            elif f[0]==g[0]=='G':key='GG'
            else:
                ff=f if f[0]=='F' else g
                gg=g if f[0]=='F' else f
                j=ff[1];r,k=gg[1:]
                normal_dot={ (0,j):1,(0,j+1):-1,(1,j):-1,(1,j+1):1}.get((r,k),0)
                key='FG-positive' if normal_dot>0 else ('FG-negative' if normal_dot<0 else 'FG-orthogonal')
            dot,cos_sq=gram_cosine(f,g,q)
            target={
                'F-adjacent':(Fraction(-2),Fraction(1,4)),
                'F-disjoint':(Fraction(0),Fraction(0)),
                'FG-positive':(Fraction(-1),Fraction(q,2*(2*q-1))),
                'FG-negative':(Fraction(1),Fraction(q,2*(2*q-1))),
                'FG-orthogonal':(Fraction(0),Fraction(0)),
                'GG':(Fraction(-1,2*q),Fraction(1,(2*q-1)**2))
            }[key]
            assert (dot,cos_sq)==target,(q,f,g,key,dot,cos_sq,target)
            classes[key]+=1
        assert classes=={'F-adjacent':q-2,'F-disjoint':(q-2)*(q-3)//2,
         'FG-negative':2*(q-1),'FG-positive':2*(q-1),
         'FG-orthogonal':2*(q-1)*(q-2),'GG':(3*q*q-q)//2},(q,classes)
        assert sum(classes.values())==(2*q-1)**2
        print(f'q={q}: vertices={len(vs)} facets={len(fs)} ridges={sum(classes.values())}; counts={classes}')
    print('MONGE_RIDGE_CLASSIFICATION_PASS dimensions=2..7 all_facet_pairs=checked_exactly')

if __name__=='__main__':main()
