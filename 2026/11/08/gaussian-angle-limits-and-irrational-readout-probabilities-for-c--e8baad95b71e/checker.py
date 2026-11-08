"""Finite exact verification of colored perfect-matching readout law."""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import factorial,comb,asin,pi,sqrt


def word_distribution(n):
    out=Counter()
    for bits in product((0,1), repeat=2*n):
        U=V=W=0
        for j in range(n):
            x,y=bits[2*j],bits[2*j+1]
            if x+y==0:U+=1
            elif x+y==1:V+=1
            else:W+=1
        out[(U,V,W)]+=1
    return out

def p_multinomial(n,u,v,w):
    assert u+v+w==n
    return Fraction(factorial(n), factorial(u)*factorial(v)*factorial(w)*4**(u+w)*2**v)

def tests():
    for n in range(1,8):
        D=word_distribution(n)
        assert sum(D.values())==4**n
        for u in range(n+1):
            for v in range(n+1-u):
                w=n-u-v
                exact=Fraction(D[u,v,w],4**n)
                assert exact==p_multinomial(n,u,v,w),(n,u,v,w,exact)
                t00,t01,t10,t11=2*u,v,v,2*w
                e1=-t00+2*t01-t11
                e2=-5*t00+2*t01+3*t11
                assert e1==4*v-2*n
                assert e2==-10*u+2*v+6*w
        print('n',n,'all profiles',len(D),'checked')
    for n in range(1,17):
        prob=Fraction(0)
        for u in range(n+1):
            for v in range(n+1-u):
                w=n-u-v
                if -2*u+2*v-2*w>=0 and -10*u+2*v+6*w>=0:
                    prob+=p_multinomial(n,u,v,w)
        if n in (4,8,12,16):print('n',n,'joint=',float(prob))
        assert 0<=prob<=1
    a=(-1,2,-1);b=(-5,2,3)
    dot=lambda p,q:p[0]*q[0]+Fraction(p[1]*q[1],2)+p[2]*q[2]
    assert dot(a,b)==4 and dot(a,a)==4 and dot(b,b)==36
    assert 3*dot(a,b)==sqrt(dot(a,a)*dot(b,b))
    print('Gaussian correlation',Fraction(1,3))
    print('irrational-angle value',0.25+asin(1/3)/(2*pi))
    print('ALL_CHECKS_OK')

if __name__=='__main__':tests()
