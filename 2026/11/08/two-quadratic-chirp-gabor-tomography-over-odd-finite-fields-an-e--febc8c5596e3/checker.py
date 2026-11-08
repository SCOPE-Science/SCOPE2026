"""Independent finite-field enumeration of quadratic-pair Gabor ambiguity coefficients.
Usage: python checker.py. Standard library only. All equalities use analytic integer traces
and a fixed floating tolerance for roots of unity; this is not an infinite proof.
"""
import cmath, math
from collections import Counter

class F:
    def __init__(self,p,poly):
        self.p=p;self.poly=poly;self.r=len(poly)-1;self.q=p**self.r
        assert poly[-1]==1
        self.el=[tuple((i//(p**j))%p for j in range(self.r)) for i in range(self.q)]
        self.to_idx={v:i for i,v in enumerate(self.el)}
        self.zero=0;self.one=self.to_idx[(1,)+(0,)*(self.r-1)]
        self.addtable=[[self.to_idx[tuple((x+y)%p for x,y in zip(a,b))] for b in self.el] for a in self.el]
        self.negtable=[self.to_idx[tuple(-x%p for x in a)] for a in self.el]
        self.multable=[[self._mulpoly(a,b) for b in self.el] for a in self.el]
        self.powertable={}
        for u in range(1,self.q):
            assert any(self.multable[u][v]==self.one for v in range(1,self.q)), 'irreducibility failed'
        for a in range(1,self.q):
            t=self.one
            for e in range(1,self.q):
                t=self.multable[t][a]
                if t==self.one: break
            assert e==self.q-1 or a==self.one or t==self.one, 'not a field!'
        self.trace_table=[]
        for a in range(self.q):
            t=0;s=a
            for _ in range(self.r):
                t=self.addtable[t][s];s=self.power(s,self.p)
            assert self.el[t][1:]==(0,)*(self.r-1)
            self.trace_table.append(self.el[t][0])
        self.psi=[cmath.exp(2j*math.pi*t/p) for t in self.trace_table]
    def _mulpoly(self,a,b):
        p=self.p;r=self.r
        z=[0]*(2*r-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):z[i+j]=(z[i+j]+x*y)%p
        for i in range(2*r-2,r-1,-1):
            c=z[i]
            for j in range(r):z[i-r+j]=(z[i-r+j]-c*self.poly[j])%p
        return self.to_idx[tuple(z[:r])] if hasattr(self,'to_idx') else sum(z[i]*p**i for i in range(r))
    def add(self,a,b):return self.addtable[a][b]
    def neg(self,a):return self.negtable[a]
    def sub(self,a,b):return self.addtable[a][self.negtable[b]]
    def mul(self,a,b):return self.multable[a][b]
    def power(self,a,n):
        t=self.one
        while n:
            if n&1:t=self.mul(t,a)
            a=self.mul(a,a);n>>=1
        return t
    def inv(self,a):return self.power(a,self.q-2)
    def scalar(self,i):return self.to_idx[((i%self.p),)+(0,)*(self.r-1)]


def verify(p,poly,slopes=None):
    f=F(p,poly);q=f.q
    if slopes is None:slopes=[(f.zero,f.one), (f.one, f.scalar(2)), (f.zero,f.scalar(2))] + ([(f.zero, f.to_idx[(0,1)+(0,)*(f.r-2)])] if f.r>1 else [])
    two=f.scalar(2);four=f.scalar(4)
    for c,d in slopes:
        if c==d:continue
        h=f.sub(c,d);iv=f.inv(f.mul(two,h));inv4h=f.inv(f.mul(four,h))
        gauss=sum(f.psi[f.mul(h,f.mul(x,x))] for x in range(q))
        chisign=1 if q%4==1 else -1
        assert abs(gauss.conjugate() - chisign*gauss)<2e-7
        assert abs(abs(gauss)-math.sqrt(q))<2e-7
        g=[f.psi[f.mul(c,f.mul(x,x))]+f.psi[f.mul(d,f.mul(x,x))] for x in range(q)]
        vals=[];zeros=0;off_phase_multiplicities=Counter()
        for a in range(q):
            for b in range(q):
                D=f.mul(f.neg(iv),f.mul(f.sub(b,f.mul(two,f.mul(c,a))),f.sub(b,f.mul(two,f.mul(d,a)))))
                phase=f.trace_table[D]; psiD=f.psi[D]
                if b!=f.mul(two,f.mul(c,a)) and b!=f.mul(two,f.mul(d,a)):
                    off_phase_multiplicities[phase]+=1
                    m=math.sqrt(q)*abs(psiD+chisign)
                elif a!=0:
                    m=abs(q+(1+chisign)*gauss)
                else:
                    m=abs(2*q+(1+chisign)*gauss)
                direct=sum(g[f.add(x,a)]*g[x].conjugate()*f.psi[f.neg(f.mul(b,x))] for x in range(q))
                a2=f.mul(a,a)
                U=f.sub(f.mul(c,a2),f.mul(f.mul(f.sub(f.mul(two,f.mul(c,a)),b),f.sub(f.mul(two,f.mul(c,a)),b)),inv4h))
                V=f.add(f.mul(d,a2),f.mul(f.mul(f.sub(f.mul(two,f.mul(d,a)),b),f.sub(f.mul(two,f.mul(d,a)),b)),inv4h))
                exact=gauss*f.psi[U]+chisign*gauss*f.psi[V]
                if b==f.mul(two,f.mul(c,a)):exact+=q*f.psi[f.mul(c,a2)]
                if b==f.mul(two,f.mul(d,a)):exact+=q*f.psi[f.mul(d,a2)]
                if abs(direct-exact)>1e-7 or abs(abs(direct)-m)>1e-7:
                    raise AssertionError((q,c,d,a,b,direct,exact,m,D,phase))
                if m<1e-7:zeros+=1
                vals.append(m)
        expected=(q-1)*(q//p-1) if q%4==3 else 0
        assert zeros==expected,(q,c,d,zeros,expected)
        for t in range(p):
            expect=(q-1)*(q//p-(1 if t==0 else 0))
            assert off_phase_multiplicities[t]==expect,(q,t,off_phase_multiplicities[t],expect)
        zero_line=abs(2*q+(1+chisign)*gauss)
        single_line=abs(q+(1+chisign)*gauss)
        assert abs(vals[0]-zero_line)<1e-7
        assert sum(abs(x-single_line)<1e-7 for x in vals)>=2*(q-1)
        assert abs(max(vals)-zero_line)<1e-7
        if chisign==1:
            predicted_min=min(single_line, 2*math.sqrt(q)*math.sin(math.pi/(2*p)))
        elif q==p:
            predicted_min=2*math.sqrt(q)*math.sin(math.pi/p)
        else:
            predicted_min=0
        assert abs(min(vals)-predicted_min)<1e-7,(q,predicted_min,min(vals))
        normsq=sum(abs(z)**2 for z in g)
        assert abs(normsq-zero_line)<1e-7
        # Moyal identity: the complete ambiguity energy is q times the fourth norm of g.
        assert abs(sum(v*v for v in vals)-q*normsq*normsq)<1e-6*q*q
        print('PASS',f'q={q}', f'p={p}', 'slopes=',(f.el[c],f.el[d]),'rank=',q*q-zeros, 'nullity=',zeros,'min=',round(min(vals),10),'max=',round(max(vals),10),'Gauss=',round(gauss.real,6),round(gauss.imag,6))

if __name__=='__main__':
    verify(3,[0,1]);verify(5,[0,1]);verify(7,[0,1]);verify(11,[0,1]);verify(13,[0,1]);verify(17,[0,1]);verify(19,[0,1])
    verify(3,[1,0,1]);verify(5,[2,0,1]);verify(3,[2,2,0,1]);verify(7,[1,0,1]);
    print('ALL_QUADRATIC_PAIR_AMBIGUITY_CHECKS_PASS')
