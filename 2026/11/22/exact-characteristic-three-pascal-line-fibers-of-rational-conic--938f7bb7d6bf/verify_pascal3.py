#!/usr/bin/env python3
"""Independent finite-field checks for rational Pascal-line fibers in characteristic 3.

Run with Python 3 and SymPy. No external data or network access is required.
"""
from itertools import permutations, combinations
from collections import Counter
from math import comb
from sympy import Poly, symbols

x = symbols('x')


def irreducible(m):
    if m == 1:
        return [0, 1]
    for n in range(3**m, 3**(m+1)):
        c = [(n // 3**j) % 3 for j in range(m+1)]
        if c[-1] != 1:
            continue
        f = Poly(sum(c[j]*x**j for j in range(m+1)), x, modulus=3)
        if f.is_irreducible:
            return c
    raise RuntimeError('irreducible polynomial missing')


class Field:
    def __init__(self,m):
        self.m=m; self.q=3**m; self.mod=irreducible(m)
        self.add=[[0]*self.q for _ in range(self.q)]
        self.neg=[0]*self.q
        self.mul=[[0]*self.q for _ in range(self.q)]
        self.inv=[None]*self.q
        p3=[3**j for j in range(m)]
        coeff=[[(a//p3[j])%3 for j in range(m)] for a in range(self.q)]
        for a in range(self.q):
            self.neg[a]=sum((-coeff[a][j]%3)*p3[j] for j in range(m))
            for b in range(self.q):
                self.add[a][b]=sum(((coeff[a][j]+coeff[b][j])%3)*p3[j] for j in range(m))
                prod=[0]*(2*m-1)
                for j in range(m):
                    for k in range(m): prod[j+k]=(prod[j+k]+coeff[a][j]*coeff[b][k])%3
                for j in range(2*m-2,m-1,-1):
                    r=prod[j]
                    for k in range(m): prod[j-m+k]=(prod[j-m+k]-r*self.mod[k])%3
                self.mul[a][b]=sum(prod[j]*p3[j] for j in range(m))
        for a in range(1,self.q):
            self.inv[a]=next(b for b in range(1,self.q) if self.mul[a][b]==1)
        self.square={self.mul[a][a] for a in range(1,self.q)}
        self.chi=[0 if a==0 else 1 if a in self.square else -1 for a in range(self.q)]

    def A(self,*args):
        r=0
        for a in args:r=self.add[r][a]
        return r
    def M(self,*args):
        r=1
        for a in args:r=self.mul[r][a]
        return r
    def N(self,a):return self.neg[a]
    def S(self,a,b):return self.add[a][self.neg[b]]
    def D(self,a,b):return self.mul[a][self.inv[b]]


def normalized_counts(F):
    q=F.q; out=Counter()
    exc_char=[0]*4; exc_zero=[0]*4
    for a in range(2,q):
        for b in range(2,q):
            if a==b:continue
            ab=F.M(a,b)
            excluded=[F.A(a,1),F.A(ab,1),F.A(a,b),
                      F.A(a,1,F.D(F.M(a,F.S(b,1)),b))]
            assert len(set(excluded))==4
            for j,z in enumerate(excluded):
                disc=F.S(F.M(z,z),ab)
                exc_char[j]+=F.chi[disc]
                exc_zero[j]+=disc==0
            for c in range(2,q):
                if c in (a,b):continue
                # Pascal line in [infinity,0,1,a,b,c] has coefficients
                # [-c, ab+ac-a+c, -abc].
                B=F.D(F.N(F.A(ab,F.M(a,c),F.N(a),c)),c)
                disc=F.S(F.M(B,B),ab)  # 4=1 in characteristic three
                kind = 'tangent' if disc==0 else 'secant' if F.chi[disc]==1 else 'exterior'
                out[kind]+=1
    pair_count=(q-2)*(q-3)
    assert exc_char==[-2*(q-3),(q-3)**2,pair_count,-2*(q-3)],exc_char
    assert exc_zero==[q-3,q-3,0,q-3],exc_zero
    want={'tangent':(q-3)*(q-6),
          'secant':(q-3)*(q-5)**2//2,
          'exterior':(q-3)**2*(q-1)//2}
    assert dict(out)==want, (q,out,want)
    total=(q-2)*(q-3)*(q-4)
    assert sum(out.values())==total
    assert q*(q-1)*out['tangent']%12==0
    T=q*(q-1)*out['tangent']//12
    S=(q-1)*out['secant']//6
    E=(q+1)*out['exterior']//6
    assert (T,S,E)==(q*(q-1)*(q-3)*(q-6)//12,
        (q-1)*(q-3)*(q-5)**2//12,
        (q+1)*(q-1)*(q-3)**2//12)
    assert (q+1)*T+(q*(q+1)//2)*S+(q*(q-1)//2)*E==60*comb(q+1,6)
    print('Normalized q=',q, 'poly=',F.mod,'counts=',dict(out),'fibers=',(T,S,E), 'excluded=',exc_char,exc_zero)
    return T,S,E


def cross(F,u,v):
    return (F.S(F.M(u[1],v[2]),F.M(u[2],v[1])),
            F.S(F.M(u[2],v[0]),F.M(u[0],v[2])),
            F.S(F.M(u[0],v[1]),F.M(u[1],v[0])))


def canonical(F,u):
    t=next(a for a in u if a)
    return tuple(F.D(a,t) for a in u)


def full_hexagon_check(F,T,S,E):
    assert F.q == 9
    pts=[(F.M(t,t),t,1) for t in range(F.q)]+[(1,0,0)]
    chords={(i,j):cross(F,pts[i],pts[j]) for i in range(10) for j in range(i+1,10)}
    def chord(i,j):return chords[tuple(sorted((i,j)))]
    line_count=Counter()
    dihedral={}
    for subset in combinations(range(10),6):
        for p in permutations(subset):
            rotations = [p[j:]+p[:j] for j in range(6)]
            reflected=p[::-1]
            rotations.extend(reflected[j:]+reflected[:j] for j in range(6))
            if p!=min(rotations):continue
            Q0=cross(F,chord(p[0],p[1]),chord(p[3],p[4]))
            Q1=cross(F,chord(p[1],p[2]),chord(p[4],p[5]))
            Q2=cross(F,chord(p[2],p[3]),chord(p[5],p[0]))
            L=cross(F,Q0,Q1)
            assert L!=(0,0,0)
            assert F.A(*[F.M(L[j],Q2[j]) for j in range(3)])==0
            line_count[canonical(F,L)]+=1
    assert len(line_count)==F.q*F.q+F.q+1
    by_type=Counter()
    for line,mult in line_count.items():
        A,B,C=line
        d=F.S(F.M(B,B),F.M(A,C))
        kind='tangent' if d==0 else 'secant' if F.chi[d]==1 else 'exterior'
        want={'tangent':T,'secant':S,'exterior':E}[kind]
        assert mult==want, (line,mult,want)
        by_type[kind]+=1
    assert by_type=={'tangent':10,'secant':45,'exterior':36}
    assert sum(line_count.values())==12600
    print('Independent direct q=9 enumeration:',len(line_count),'lines, 12600 hexagons,',dict(by_type))


if __name__=='__main__':
    for m in (2,3,4):
        F=Field(m); v=normalized_counts(F)
        if m==2: full_hexagon_check(F,*v)
    print('All checks passed.')
