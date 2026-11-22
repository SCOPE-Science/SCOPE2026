"""Finite-field matrix census for the free rank-two Lie derivation spectral criterion."""
from itertools import product

class Field:
    def __init__(self,p,u,v):
        self.p,self.u,self.v=p,u,v
        self.q=p*p
    def add(self,a,b):
        p=self.p
        return (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(self,a):
        p=self.p
        return ((-(a%p))%p)+p*((-(a//p))%p)
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):
        p,u,v=self.p,self.u,self.v
        x,y=a%p,a//p;z,w=b%p,b//p
        return ((x*z-v*y*w)%p)+p*((x*w+y*z-u*y*w)%p)
    def scalar(self,j):return j%self.p
    def pow(self,a,k):
        out=1
        while k:
            if k&1:out=self.mul(out,a)
            a=self.mul(a,a);k//=2
        return out

def actual_count(F,c):
    p,q=F.p,F.q;count=0
    for a,b,c0,d in product(range(q),repeat=4):
        t=F.add(a,d);det=F.sub(F.mul(a,d),F.mul(b,c0))
        if not det:continue
        okay=True
        for n in range(2,c+1):
            for i in range(1,n):
                j=n-i
                # Norm of spectral weight (i*alpha+j*beta).
                z=F.add(F.mul(F.scalar(i*j),F.mul(t,t)), F.mul(F.scalar((i-j)**2),det))
                if z==0:
                    okay=False;break
            if not okay:break
        count+=okay
    return count

def predicted(F,c):
    p,q=F.p,F.q
    if c>=2*p:return 0
    bad={(-j*pow(i,-1,p))%p for i in range(1,c) for j in range(1,c+1-i) if i%p and j%p}
    r=q-1-len(bad)-int(1 not in bad)
    irr=q*q*(q-1)**2//2 if p==2 else q*(q-1)**3//2
    return irr+q*(q+1)*(q-1)*r//2 + (q-1)*q*q*int(1 not in bad)

if __name__=='__main__':
    for p,u,v,cmax in [(2,1,1,4),(3,0,1,6)]:
        F=Field(p,u,v)
        for c in range(2,cmax+1):
            a=actual_count(F,c);e=predicted(F,c)
            assert a==e,(F.q,c,a,e)
            print(f'q={F.q}, class={c}, matrices={a}, closed formula={e}, PASS')
    print('FREE_LIE_EXTENSION_FIELD_CHECK_OK')
