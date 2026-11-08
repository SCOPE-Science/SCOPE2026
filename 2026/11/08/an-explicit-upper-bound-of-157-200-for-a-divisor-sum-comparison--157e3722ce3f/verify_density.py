"""Exact finite certificate for an upper bound on a divisor-sum comparison density.
Uses only Python's standard library, integer arithmetic and elementary bounds.
"""
from math import log, ceil, factorial
from fractions import Fraction
from itertools import count

K=4000
B=503
THRESH=-41  # upper log prefix <= -41/4001 < -1/100

def primes_up_to(n):
    a=bytearray([1])*(n+1)
    a[:2]=b'\0\0'
    for j in range(2,int(n**.5)+1):
        if a[j]: a[j*j:n+1:j]=b'\0'*((n-j*j)//j+1)
    return [j for j in range(n+1) if a[j]]

def E(p):
    if p<=3: return 16
    if p<=7: return 10
    if p<=17: return 7
    if p<=47: return 5
    return 3

def divisors(n): return [i for i in range(1,n+1) if n%i==0]

def is_upper_shift(j, numerator, denominator):
    if j >= 0:
        return denominator*pow(K+1,j)>=numerator*pow(K,j)
    j=-j
    return denominator*pow(K,j)>=numerator*pow(K+1,j)

def shift_for_ratio(numerator, denominator):
    if numerator == denominator: return 0
    j=ceil(log(numerator/denominator)/log((K+1)/K))
    while not is_upper_shift(j,numerator,denominator): j+=1
    while is_upper_shift(j-1,numerator,denominator): j-=1
    assert is_upper_shift(j,numerator,denominator)
    assert not is_upper_shift(j-1,numerator,denominator)
    return j

def exact_prefix_distribution():
    weights=[1]; offset=0; total=1
    for p in primes_up_to(B):
        e=E(p); D=p**e
        branches=[]
        for a in range(e):
            if a==0: num,den=1,1
            elif a==1: num,den=p+1,p
            else: num,den=p**a+1,sum(p**d for d in divisors(a))
            j=shift_for_ratio(num,den)
            count=(p-1)*p**(e-a-1)
            branches.append((j,count))
        branches.append((0,1)) # valuations >=e: local quotient <=1
        assert sum(w for _,w in branches)==D
        low=min(j for j,_ in branches); high=max(j for j,_ in branches)
        new=[0]*(len(weights)+high-low)
        for j,c in branches:
            z=j-low
            for i,v in enumerate(weights):
                if v: new[i+z]+=v*c
        offset+=low
        total*=D
        weights=new
    assert sum(weights)==total
    count_good=sum(weights[:max(0,THRESH-offset+1)])
    return count_good,total,offset,len(weights)

# The mgf of S=sum_{p>B,p|n} 1/p is at most exp(F(t/B)),
# F(x)=sum_{j>=1} x^j/(j*j!). At t=1400, B=503, bound F<7.
# Thus P(S>=1/100) <= exp(7-14) = exp(-7) < 1/1000.
# The last inequality is certified by the elementary Taylor bound e^7>1000.
def verify_tail():
    x=Fraction(1400,B)
    term=Fraction(1)
    summ=Fraction(0)
    for j in range(1,31):
        term*=x/j
        summ+=term/j
    # remainder from j=31 onwards <= first term /(1 - x/32)
    nextterm=term*x/31
    remainder=(nextterm/31)/(1-x/32)
    assert summ+remainder < 7
    # exp(7)>1000 using rational finite sum
    assert sum((Fraction(7)**j / factorial(j) for j in range(14)), Fraction(0))>1000
    return summ+remainder

def main():
    f=verify_tail()
    good,total,lo,length=exact_prefix_distribution()
    # Prefix probability above 0.216, plus bad tail < .001 ==> 0.215 negative density.
    print('prefix_probability',float(Fraction(good,total)))
    print('F_upper',float(f),'count_good_digits',len(str(good)),'total_digits',len(str(total)))
    print('bins',length,'offset',lo,'primes',len(primes_up_to(B)))
    print('above_216_thousandths', good*1000>216*total)
    assert good*1000>216*total
    print('CERTIFICATE_PASS density_less_than_157_over_200')
if __name__=='__main__':main()
