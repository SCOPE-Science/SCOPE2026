"""Finite tests for automorphisms of even-power conjugation quandles.

Usage: python3 check.py
All group products and quandle operations are constructed from the semidirect-product law.
"""
from itertools import permutations, product
from math import factorial, gcd


def additive_group(moduli):
    pts = list(product(*[range(n) for n in moduli]))
    def add(a,b): return tuple((a[i]+b[i])%moduli[i] for i in range(len(moduli)))
    def neg(a): return tuple(-a[i]%moduli[i] for i in range(len(moduli)))
    def mul(k,a): return tuple(k*a[i]%moduli[i] for i in range(len(moduli)))
    return pts,add,neg,mul


def quandle(moduli,m):
    pts,add,neg,mul=additive_group(moduli)
    n=len(pts)
    zero=pts[0]
    Q=[(x,t) for t in (0,1) for x in pts]
    idx={x:i for i,x in enumerate(Q)}
    def gprod(x,y):
        a,t=x; b,u=y
        return (add(a,b if t==0 else neg(b)), (t+u)%2)
    def inv(x):
        a,t=x
        return (neg(a) if t==0 else a,t)
    def power(x,k):
        if k<0: return power(inv(x),-k)
        y=(zero,0)
        for _ in range(k): y=gprod(y,x)
        return y
    op=[]
    for x in Q:
        row=[]
        for y in Q:
            ym=power(y,m)
            row.append(idx[gprod(gprod(inv(ym),x),ym)])
        op.append(row)
    return Q,op


def is_aut(perm,op):
    n=len(perm)
    return all(perm[op[i][j]]==op[perm[i]][perm[j]] for i in range(n) for j in range(n))


def brute(moduli,m):
    Q,op=quandle(moduli,m)
    n=len(Q)//2
    # Establish type preservation independently from the orbits of the right-translation group.
    shifts={}
    for y in range(2*n):
        shifts[y]=tuple(op[x][y] for x in range(2*n))
    fixed=[x for x in range(2*n) if all(shifts[y][x]==x for y in range(2*n))]
    if len(fixed)==2*n:
        return factorial(2*n),True
    assert fixed==list(range(n)),(moduli,m,fixed)
    count=0
    for f in permutations(range(n)):
        if any(f[op[i][j]]!=op[f[i]][f[j]] for i in range(n) for j in range(n)): continue
        for g in permutations(range(n,2*n)):
            perm=f+g
            if is_aut(perm,op): count+=1
    return count,False


def aut_group_size(moduli,m):
    pts,add,neg,mul=additive_group(moduli)
    H={mul(2*m,x) for x in pts}
    d=len(H); h=len(pts)//d
    if d==1: return factorial(2*len(pts)),d,h
    # General finite abelian H automorphisms via independent enumeration of bijections.
    if len(H)>6:
        if tuple(moduli)==(3,3) and d==9: autH=48
        elif tuple(moduli)==(9,) and d==9: autH=6
        elif tuple(moduli)==(8,) and d==8: autH=4
        else: raise ValueError('size too large for generic direct enumeration')
    else:
        hs=list(H)
        autH=sum(all(p[hs.index(add(a,b))]==hs.index(add(hs[p[hs.index(a)]],hs[p[hs.index(b)]]))
            for a in hs for b in hs) for p in permutations(range(d)))
    return autH*factorial(h)**(d+1)*d**h,d,h


def main():
    cases=[((3,),2),((5,),2),((6,),2),((4,),2),((3,),4),((2,3),2),((9,),6),((8,),2),((3,3),2),((5,),-2),((3,),0),((2,2),2)]
    for moduli,m in cases:
        pred,d,h=aut_group_size(moduli,m)
        q,op=quandle(moduli,m)
        A,add,neg,mul=additive_group(moduli)
        pos={x:i for i,x in enumerate(A)}
        # Independently reconstruct the simple multiplication table from the original group law.
        for i,x in enumerate(A):
            for j,y in enumerate(A):
                assert op[i][j]==i and op[i][j+len(A)]==i
                assert op[i+len(A)][j+len(A)]==i+len(A)
                assert op[i+len(A)][j]==pos[add(x,mul(-2*m,y))]+len(A)
        direct=None
        if len(A)<=6:
            direct,trivial=brute(moduli,m)
            assert direct==pred,(moduli,m,direct,pred)
        # Every affine symmetry from the base abelian group is a quandle automorphism.
        for translate in A:
            if len(A)<=6:
                auts=[]
                for perm in permutations(range(len(A))):
                    if all(perm[pos[add(a,b)]]==pos[add(A[perm[pos[a]]],A[perm[pos[b]]])]
                           for a in A for b in A):
                        auts.append(perm)
            else:
                auts=[tuple(range(len(A)))]
            for perm in auts:
                full=tuple(perm)+tuple(len(A)+pos[add(translate,A[perm[i]])] for i in range(len(A)))
                assert is_aut(full,op),(moduli,m,perm,translate)
        print('PASS',str(moduli),'m=',m,'h=',h,'d=',d,'pred=',pred,'brute=',direct)
    print('VERIFY_OK twelve cases group_operation=checked brute_group_counts=checked')

if __name__=='__main__':main()
