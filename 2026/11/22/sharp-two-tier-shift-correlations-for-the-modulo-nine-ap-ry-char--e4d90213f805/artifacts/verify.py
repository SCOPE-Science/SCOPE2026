"""Exact checks for shifted mod-nine generalized Apéry character correlations."""
from fractions import Fraction as F
from math import comb

M = {
    0: ((F(1), F(0)), (F(1,3), F(1,3))),
    1: ((F(1,3), F(1,3)), (F(1,3), F(1,3))),
    2: ((F(1,3), F(1,3)), (F(0), F(1))),
}
OMEGA_POWERS = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

def digit_one_count(n):
    s=0
    while n:
        s += n%3 == 1
        n//=3
    return s

def digit_list(h):
    out=[]
    while h:
        out.append(h%3)
        h//=3
    return out

def corr(h):
    if h == 0:
        return F(1)
    v=(F(1),F(1,2))
    for d in reversed(digit_list(h)):
        a=M[d]
        v=(a[0][0]*v[0]+a[0][1]*v[1], a[1][0]*v[0]+a[1][1]*v[1])
    return v[0]

def expected(h):
    if h==0:
        return F(1)
    ds=digit_list(h)
    pos=[i for i,d in enumerate(ds) if d]
    if len(pos)==1:
        return F(1,2)
    if len(pos)==2 and pos[1]==pos[0]+1:
        return F(1,3)
    return None

def character_vector(n):
    return OMEGA_POWERS[digit_one_count(n)%6]

def finite_pair_sum(h,length):
    ab=[0,0]
    for n in range(length):
        a,b=OMEGA_POWERS[(digit_one_count(n+h)-digit_one_count(n))%6]
        ab[0]+=a;ab[1]+=b
    return ab

def apery_mod9(n,r,s):
    return sum(pow(comb(n,j),r,9)*pow(comb(n+j,j),s,9) for j in range(n+1))%9

def run():
    total=0
    for r,s in [(2,2),(5,2),(2,8),(8,8)]:
        for n in range(72):
            assert apery_mod9(n,r,s) == pow(5,digit_one_count(n),9), (n,r,s)
            total+=1
    for h in range(1,3**8):
        c=corr(h)
        assert F(0)<c<=F(1,2)
        pattern=expected(h)
        if pattern is None:
            assert c<F(1,3)
        else:
            assert c==pattern, (h,c,pattern)
        assert corr(3*h)==c
        total+=3
    for length in [3**5, 3**6]:
        for h in range(1,121):
            a,b=finite_pair_sum(h,length)
            # x=a+b*omega has real part a+b/2 and imaginary part sqrt(3)*b/2.
            # Each carry-over summand changes by no more than two in modulus.
            assert abs(F(a)+F(b,2)-length*corr(h)) <= 4*h+2
            assert abs(b)<=4*h+2
            total+=2
    for m in range(1,25):
        assert corr((3**m-1)//2)==F(1,2)*F(2,3)**(m-1)
        total+=1
    print('PASS:',total,'exact assertions')

if __name__=='__main__':
    run()
