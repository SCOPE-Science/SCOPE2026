"""Independent arithmetic checks of the complete coadjoint orbit-size distribution."""
from math import prod

def gaussian(n,s,q):
    if s<0 or s>n:return 0
    numerator=prod(q**(n-i)-1 for i in range(s))
    denominator=prod(q**(s-i)-1 for i in range(s))
    assert numerator%denominator==0
    return numerator//denominator

def gl(n,q):return prod(q**n-q**i for i in range(n))

def orbit_table(a,b,q):
    assert a>=1 and b>=1 and q>=2
    table={}
    def put(size,count):
        if count:
            assert count>0 and isinstance(count,int)
            table[size]=table.get(size,0)+count
    put(1,q**3)
    put(q*(q-1),q*q*((q**a-1)+(q**b-1))//(q-1))
    put(q*q*(q-1)**2,q*(q**a-1)*(q**b-1)//(q-1)**2)
    for s in range(1,min(a,b)+1):
        N=gaussian(a,s,q)*gaussian(b,s,q)*gl(s,q)
        assert N*q**2%(q-1)==0
        put((q-1)*q**(2*s+1),N*q**2//(q-1))
        assert N*q*(q**(a+b-2*s)-1)%(q-1)**2==0
        put((q-1)**2*q**(2*s+2),N*q*(q**(a+b-2*s)-1)//(q-1)**2)
    return table

def run():
    total=0
    for q in (2,3,4,5,7,8,9,11):
      for a in range(1,7):
        for b in range(1,7):
            tab=orbit_table(a,b,q)
            dimension=3+a+b+a*b
            assert sum(size*orbits for size,orbits in tab.items())==q**dimension
            # Independently stratify by zero / nonzero bilinear form rank.
            assert sum(gaussian(a,s,q)*gaussian(b,s,q)*gl(s,q) for s in range(min(a,b)+1))==q**(a*b)
            total+=1
    print('Checked',total,'field/arrow-parameter configurations.')
    print('Every orbit table consists of nonnegative integers.')
    print('Every weighted orbit table sums to the complete dual space size.')
    print('Every matrix-rank stratum sum equals the number of all bilinear forms.')
    print('ALL_PATH_ORBIT_MASS_IDENTITIES_PASS')

if __name__=='__main__':run()
