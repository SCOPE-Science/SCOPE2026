"""Independent contour-cycle and transfer check for adjacent and separated missing spokes.
Run: python3 cycle_and_transfer.py. Python standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def build(n,missing):
    adj=[set() for _ in range(n+1)]
    for i in range(n):
        j=(i+1)%n
        adj[i].add(j);adj[j].add(i)
        if i not in missing:
            adj[i].add(n);adj[n].add(i)
    return adj


def cycles(adj):
    n=len(adj); found=set()
    for root in range(n):
        def visit(path):
            x=path[-1]
            for y in adj[x]:
                if y==root and len(path)>=3:
                    p=tuple(path)
                    found.add(min(p,(p[0],)+tuple(reversed(p[1:]))))
                elif y>root and y not in path:
                    visit(path+[y])
        visit([root])
    return sorted(found,key=lambda p:(len(p),p))


def delta(a,b):
    d=(b-a)%3
    return 1 if d==1 else -1 if d==2 else 0


def rate(color,cycs):
    best=Fraction(0)
    for c in cycs:
        winding=abs(sum(delta(color[x],color[y]) for x,y in zip(c,c[1:]+c[:1])))
        best=max(best,Fraction(winding,len(c)))
    return best

M=((1,1,1),(1,1,0),(1,0,1))

def count_5(a,b):
    return sum(abs(delta(0,a)+delta(a,u)+delta(u,v)+delta(v,b)+delta(b,0))==3 for u,v in product(range(3),repeat=2))

N=tuple(tuple(count_5(a,b) for b in range(3)) for a in range(3))
assert N==((2,3,3),(3,2,6),(3,6,2)),N


def matrix_powers(A,k):
    B=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(k):
        B=[[sum(B[i][t]*A[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
    return B


def theoretical(n):
    P=matrix_powers(M,n-3)
    # W-word has L=n-2 vertices and L-1=n-3 edges.
    F=sum(P[i][j] for i in range(3) for j in range(3))
    T=sum(P[i][j]*N[j][i] for i in range(3) for j in range(3))
    zero=27*F-3*T;middle=3*T;high=3**(n+1)-27*F
    return (zero,middle,high),F,T


def main():
    checked=0
    for n in range(5,9):
        C=cycles(build(n,{0,1}))
        counts=Counter(rate(s,C) for s in product(range(3),repeat=n+1))
        pred,F,T=theoretical(n)
        assert [counts[Fraction(i)] for i in (0,Fraction(3,5),1)]==list(pred),(n,counts,pred)
        assert set(counts)=={Fraction(0),Fraction(3,5),Fraction(1)}
        checked+=3**(n+1)
        print('adjacent rim',n,'cycles',len(C),'counts',pred,'F',F,'T',T)
    for n in range(6,9):
        C=cycles(build(n,{0,2}))
        counts=Counter(); six_cycle_high_without_rainbow=0
        for s in product(range(3),repeat=n+1):
            actual=rate(s,C)
            triangles=[c for c in C if len(c)==3]
            rainbow=any(abs(sum(delta(s[x],s[y]) for x,y in zip(c,c[1:]+c[:1])))==3 for c in triangles)
            c1=sum(delta(s[x],s[y]) for x,y in zip((n,n-1,0,1),(n-1,0,1,n)))
            c2=sum(delta(s[x],s[y]) for x,y in zip((n,1,2,3),(1,2,3,n)))
            expected=(Fraction(1) if rainbow or c1*c2>0 else Fraction(3,4) if c1 or c2 else Fraction(0))
            assert actual==expected,(n,s,actual,expected,c1,c2,rainbow)
            if not rainbow and actual==1:six_cycle_high_without_rainbow+=1
            counts[actual]+=1
        assert set(counts)=={Fraction(0),Fraction(3,4),Fraction(1)},(n,counts)
        checked+=3**(n+1)
        print('separated rim',n,'cycles',len(C),'counts', [(str(x),counts[x]) for x in sorted(counts)],'maximal-without-rainbow-triangle',six_cycle_high_without_rainbow)
    for n in range(5,31):
        pred,F,T=theoretical(n)
        assert sum(pred)==3**(n+1)
        assert min(pred)>=0
    print('PASS: independently enumerated simple cycles for',checked,'colourings, transfer checks through rim 30')

if __name__=='__main__':main()
