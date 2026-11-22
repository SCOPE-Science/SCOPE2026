#!/usr/bin/env python3
"""Exact finite-field spot tests for the projective Galois-line stabilizer theorem.
The proof of the infinite classification is in RESULT.md; these tests are supplementary.
"""

class Field2:
    def __init__(self, m, polynomial):
        self.m, self.poly, self.size = m, polynomial, 1 << m
    def mul(self, a, b):
        z = 0
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & self.size:
                a ^= self.poly
        return z
    def power(self, a, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, a)
            a = self.mul(a, a)
            n >>= 1
        return z
    def inv(self, a):
        assert a
        return self.power(a, self.size - 2)
    def linearized(self, a, q):
        z = 0
        t = a
        for _ in range(q.bit_length() - 1):
            z ^= t
            t = self.mul(t, t)
        return z
    def transform(self, a, b, u, v, P):
        X,Y,Z,W = P
        aa = self.mul(a,a)
        ab = self.mul(a,b)
        bb = self.mul(b,b)
        va = self.mul(v,self.inv(a))
        gamma = self.mul(va,va)
        return (
            self.mul(aa,X) ^ self.mul(ab,Y) ^ self.mul(bb,W) ^ self.mul(u,Z),
            self.mul(a,Y) ^ self.mul(v,Z),
            self.mul(aa,Z),
            W ^ self.mul(gamma,Z),
        )
    def check(self, q, all_pairs):
        F = list(range(self.size))
        cases=[]
        if all_pairs:
            for a in F[1:]:
                for b in F:
                    for u,v in ((0,0),(1,1),(2,3)):
                        cases.append((a,b,u,v))
        else:
            for j in range(48):
                cases.append((1+(7*j)%(self.size-1),(11*j)%self.size,(5*j)%self.size,(13*j)%self.size))
        count = 0
        for a,b,u,v in cases:
            ia = self.inv(a)
            ia2 = self.mul(ia,ia)
            for t in F:
                target = self.mul(a,t)^b
                for P in ((t,1,0,0),(self.mul(t,t),0,0,1)):
                    X,Y,Z,W=self.transform(a,b,u,v,P)
                    assert Z==0
                    assert X^self.mul(target,Y)^self.mul(self.mul(target,target),W)==0
                dtarget=self.mul(a,t)
                for P in ((1,0,0,0),(0,t,0,1)):
                    X,Y,Z,W=self.transform(a,b,u,v,P)
                    assert Z==0 and (Y^self.mul(dtarget,W))==0
                ctarget=self.mul(t,ia)^self.mul(v,ia2)
                for P in ((1,0,0,0),(0,t,1,self.mul(t,t))):
                    X,Y,Z,W=self.transform(a,b,u,v,P)
                    assert (Y^self.mul(ctarget,Z))==0
                    assert (W^self.mul(self.mul(ctarget,ctarget),Z))==0
                count+=1
        assert len({self.linearized(u,q) for u in F}) == self.size//(q//2)
        assert len([u for u in F if self.linearized(u,q)==0]) == q//2
        print(f'q={q} field={self.size}: checked {len(cases)} matrices * {self.size} parameters = {count} cases for each of three line families; ker Lq has {q//2} elements: PASS')

if __name__=='__main__':
    Field2(4,0b10011).check(4,True)
    Field2(6,0b1000011).check(8,False)
