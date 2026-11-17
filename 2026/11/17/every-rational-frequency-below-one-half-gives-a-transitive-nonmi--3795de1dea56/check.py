#!/usr/bin/env python3
"""Independent finite spot checks of a rational-frequency shift theorem.
Does not replace the all-parameter mathematical argument."""
from math import gcd

def transition(p,q,h,last,bit):
    if last == 1 and bit != (1 if h >= 0 else 0):
        raise ValueError('forbidden transition')
    return h + (p if bit == 0 else -q), bit

def replay(p,q,word,h=0,last=0):
    for b in word:
        h,last=transition(p,q,h,last,int(b))
    return h,last

def connector(p,q,h,target):
    assert 0<p<q and gcd(p,q)==1
    out=''
    if h>=q:
        out+='1'; h-=q
        while h>=0:
            out+='1'; h-=q
        out+='0'; h+=p
    assert h<q
    while not ((target-h)%p==0 and h<=target):
        out+='10'; h-=q-p
    out+='0'*((target-h)//p)
    return out

def marker(p,q):
    m=next(j for j in range(1,2*q+2) if p*j%q==1 and p*j>=q+1)
    r=(p*m-1)//q+1
    return '1'+'0'*m+'1'*r+'0'

def sample_factors(p,q,max_len=16,size=4):
    frontier=[('',0,0)]
    seen={}
    for i in range(max_len):
        new=[]
        for w,h,last in frontier:
            for bit in (0,1):
                try: hh,ll=transition(p,q,h,last,bit)
                except ValueError: continue
                nw=w+str(bit); new.append((nw,hh,ll))
                if len(nw)>=size:
                    for at in range(len(nw)-size+1):
                        word=nw[at:at+size]
                        if word not in seen:
                            pre=nw[:at]
                            H,L=replay(p,q,pre)
                            seen[word]=H
        frontier=new
    return seen

def tests():
    for p,q in [(1,2),(1,3),(1,4),(2,3),(2,5),(3,4),(3,5),(3,7),(4,5)]:
        w=marker(p,q)
        good=[h for h in range(-50,51) if attempt(p,q,h,w)]
        assert good==[q-1],(p,q,good)
        h,_=replay(p,q,w,q-1,0)
        s=connector(p,q,h,q-1)
        assert replay(p,q,w+s+w,q-1,0)[1]==0
        assert (len(w)+len(s))%(p+q)==0
        for a in range(-12,13):
            for b in range(-12,13):
                c=connector(p,q,a,b)
                H,L=replay(p,q,c,a,0)
                assert (H,L)==(b,0),(p,q,a,b,c,H,L)
        fs=sample_factors(p,q,14,3)
        for u,hu in fs.items():
            for v,hv in fs.items():
                eu,Lu=replay(p,q,u,hu,0)
                completion=''
                if Lu==1:
                    if eu>=0:
                        completion+='1'; eu-=q
                        while eu>=0:
                            completion+='1'; eu-=q
                    completion+='0';eu+=p
                middle=completion+connector(p,q,eu,hv)
                H,L=replay(p,q,u+middle+v,hu,0)
                assert u+middle+v and H==hv+sum(p if b=='0' else -q for b in v)
        print('PASS p,q=',p,q,'marker_length=',len(w),'factor_samples=',len(fs),'pairs=',len(fs)**2)
    print('PASS: all finite spot checks; infinite claims depend on proof')

def attempt(p,q,h,w):
    try:
        replay(p,q,w,h,0)
        return True
    except ValueError: return False

if __name__=='__main__':tests()
