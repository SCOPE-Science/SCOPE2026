#!/usr/bin/env python3
"""Independent finite-field conic/tangent incidence enumeration.
Science: pairs of osculating conics of intersection type (3,1).
"""
class Field:
    def __init__(self,p,r):
        assert r in (1,2) and p%2
        self.p,self.r,self.q=p,r,p**r
        self.d=next((a for a in range(2,p) if pow(a,(p-1)//2,p)==p-1),None) if r==2 else None
        assert r==1 or self.d is not None
    def add(self,x,y):
        p=self.p
        return (x+y)%p if self.r==1 else ((x%p+y%p)%p + p*((x//p+y//p)%p))
    def neg(self,x):
        p=self.p
        return -x%p if self.r==1 else ((-x%p)+p*((-(x//p))%p))
    def sub(self,x,y):return self.add(x,self.neg(y))
    def mul(self,x,y):
        p=self.p
        if self.r==1:return x*y%p
        a,b=x%p,x//p;c,d=y%p,y//p
        return ((a*c+self.d*b*d)%p)+p*((a*d+b*c)%p)
    def sq(self,x):return self.mul(x,x)
    def from_int(self,x):return x%self.p

def count(p,r):
    f=Field(p,r); z=f.from_int(0);o=f.from_int(1);two=f.from_int(2)
    flags=set()
    for t in range(f.q):
        for s in range(f.q):
            # C point (t^2,t,1), tangent at D point (s^2-s,s,1)
            # line: X+(1-2s)Y+s^2 Z
            on_line=f.add(f.add(f.sq(t),f.mul(f.sub(o,f.mul(two,s)),t)),f.sq(s))
            if on_line==z: flags.add((t,s))
    assert len(flags)==f.q,(p,r,'flags',len(flags))
    nxt={}
    for t,s in flags:
        tp=f.sub(f.sub(f.mul(two,s),o),t)
        sp=f.sub(f.mul(two,tp),s)
        assert (tp,sp) in flags,(p,r,t,s,tp,sp)
        nxt[t,s]=tp,sp
    covered=set();valid=[];degenerate=[]
    for flag in flags:
        if flag in covered:continue
        orbit=[];cur=flag
        while cur not in orbit:
            assert cur in flags
            orbit.append(cur);covered.add(cur);cur=nxt[cur]
        assert cur==flag and len(orbit)==p,(p,r,orbit)
        verts=[x for x,_ in orbit];tans=[x for _,x in orbit]
        if len(set(verts))==p and len(set(tans))==p:
            # no chord tangent to the inscribed conic, no backtracking
            assert all(verts[i]!=verts[(i+1)%p] for i in range(p))
            valid.append(orbit)
        else: degenerate.append(orbit)
    assert len(degenerate)==1,(p,r,len(degenerate))
    assert len(valid)==f.q//p-1,(p,r,len(valid))
    # Reversal fixes the vertex set, so unoriented polygons correspond to vertex sets.
    vertex_sets={frozenset(t for t,_ in orbit) for orbit in valid}
    assert len(vertex_sets)==(f.q-p)//(2*p),(p,r,len(vertex_sets))
    print('p=%d r=%d q=%d flags=%d good_oriented=%d good_unoriented=%d degenerate=%d OK'%
          (p,r,f.q,len(flags),len(valid),len(vertex_sets),len(degenerate)))

if __name__=='__main__':
    for p in (3,5,7,11):
        for r in (1,2):count(p,r)
    print('VERIFY_FLAGS_OK')
