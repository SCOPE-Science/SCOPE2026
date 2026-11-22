from fractions import Fraction as Q
from math import comb

def geometric_rise_prob(b,n):
    """Independent rational partition of [0,1] at orbit-comparison roots."""
    acc=Q(0)
    B=b**n
    for j in range(B):
        lo,hi=Q(j,B),Q(j+1,B)
        intercept=[]
        for i in range(n+1):
            intercept.append(j//(b**(n-i)))
        cuts=[lo,hi]
        for i in range(n):
            # (b^i x - floor(b^i x)) - (b^(i+1)x-floor(b^(i+1)x))=0
            den=b**(i+1)-b**i
            crossing=Q(intercept[i+1]-intercept[i],den)
            if lo<crossing<hi:cuts.append(crossing)
        cuts=sorted(set(cuts))
        for l,r in zip(cuts,cuts[1:]):
            m=(l+r)/2
            if all(b**i*m-intercept[i] < b**(i+1)*m-intercept[i+1] for i in range(n)):
                acc+=r-l
    return acc

def formula(b,n):
    return Q(comb(n+b-1,b-2),(b-1)*b**n)

def digit_sum(b,n):
    return sum((b-1-v)*comb(n+v-1,n-1) for v in range(b)) / Q((b-1)*b**n)

if __name__=='__main__':
    count=0
    for b in range(2,8):
      for n in range(1,6):
        if b**n>5000:continue
        g=geometric_rise_prob(b,n)
        f=formula(b,n)
        d=digit_sum(b,n)
        assert g==f==d,(b,n,g,f,d)
        print(f'b={b} n={n} P={g}')
        count+=1
    for b in range(2,25):
      for n in range(1,40):
        assert formula(b,n)==digit_sum(b,n)
        count+=1
    print('PASS',count,'exact rational probability comparisons')
