#!/usr/bin/env python3
"""Independent exhaustive checks of finite-field two-dimensional idempotent counts.

Enumerates every invertible 2x2 matrix and all vector solutions over
F_2,F_3,F_4,F_5,F_7,F_8,F_9,F_11, comparing the complete histogram to
closed formulas. Uses no third-party packages.
"""
from collections import Counter

class Field:
    def __init__(self, p, mod):
        self.p = p
        self.mod = mod
        self.k = len(mod)-1
        self.q = p**self.k
        self.a = [[(i+j)%p if self.k==1 else self._plus(i,j) for j in range(self.q)] for i in range(self.q)]
        self.m = [[self._times(i,j) for j in range(self.q)] for i in range(self.q)]
        self.neg = [next(j for j in range(self.q) if self.a[i][j]==0) for i in range(self.q)]
    def digits(self,n):
        a=[]
        for _ in range(self.k):a.append(n%self.p);n//=self.p
        return a
    def _plus(self,i,j):
        return sum(((x+y)%self.p)*self.p**r for r,(x,y) in enumerate(zip(self.digits(i),self.digits(j))))
    def _times(self,i,j):
        p=self.p;k=self.k
        a=self.digits(i);b=self.digits(j)
        z=[0]*(2*k-1)
        for r in range(k):
            for s in range(k):z[r+s]=(z[r+s]+a[r]*b[s])%p
        for t in range(2*k-2,k-1,-1):
            h=z[t]
            for s in range(k):z[t-k+s]=(z[t-k+s]-h*self.mod[s])%p
        return sum(z[r]*p**r for r in range(k))
    def square(self,x):return self.m[x][x]

def run(p,mod):
    F=Field(p,mod)
    q=F.q;add=F.a;mul=F.m;neg=F.neg
    cnt=Counter()
    nGL=0
    for a in range(q):
     for b in range(q):
      for c in range(q):
       for d in range(q):
        det=add[mul[a][d]][neg[mul[b][c]]]
        if not det:continue
        nGL+=1
        # Direct idempotent equations: x^2=a*x+b*y, y^2=c*x+d*y.
        found=0
        for x in range(q):
         for y in range(q):
          if x==0 and y==0:continue
          if F.square(x)==add[mul[a][x]][mul[b][y]] and F.square(y)==add[mul[c][x]][mul[d][y]]:
           found+=1
        assert 0<=found<=3,(q,a,b,c,d,found)
        # Independently count projective zeros of binary cubic b*Y^3+a*X*Y^2-d*X^2*Y-c*X^3.
        roots=0
        for t in range(q):
            t2=F.square(t);t3=mul[t2][t]
            value=add[add[mul[b][t3]][mul[a][t2]]][add[neg[mul[d][t]]][neg[c]]]
            if value==0:roots+=1
        if b==0:roots+=1
        assert found==roots,(q,a,b,c,d,found,roots)
        cnt[found]+=1
    assert nGL==(q*q-1)*(q*q-q)
    L=nGL;h=(q-1)**3 if p%2 else 0
    expected={0:L//3,1:(L-h)//2,2:h,3:(L-3*h)//6}
    assert dict(sorted(cnt.items()))=={k:v for k,v in expected.items() if v},(q,cnt,expected)
    print('q=%d: GL2=%d, histogram=%s, exact_formulas=OK'%(q,L,[cnt[k] for k in range(4)]))

if __name__=='__main__':
    for p,mod in [(2,[0,1]),(3,[0,1]),(2,[1,1,1]),(5,[0,1]),(7,[0,1]),(2,[1,1,0,1]),(3,[1,0,1]),(11,[0,1])]:
        run(p,mod)
    print('VERIFY_OK')
