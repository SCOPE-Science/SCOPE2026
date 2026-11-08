"""Independent exact point-enumeration checks for twisted triangular line divisors.

Run: python3 verify.py . Requires Python 3 standard library only.
"""
from itertools import product
from math import gcd


def projective_points(p):
    return [(1,y,z) for y in range(p) for z in range(p)] + [(0,1,z) for z in range(p)] + [(0,0,1)]


def check_prime(p,n,a,b,c):
    assert gcd(p,n)==1 and all(x % p for x in (a,b,c))
    pts=projective_points(p)
    actual=sum(1 for x,y,z in pts if ((pow(x,n,p)-a*pow(y,n,p))%p==0 or (pow(y,n,p)-b*pow(z,n,p))%p==0 or (pow(z,n,p)-c*pow(x,n,p))%p==0))
    na=sum(pow(x,n,p)==a for x in range(p))
    nb=sum(pow(x,n,p)==b for x in range(p))
    nc=sum(pow(x,n,p)==c for x in range(p))
    corrected=2*na*nb if (a*b*c)%p==1 else na*nb+nb*nc+nc*na
    predicted=3+p*(na+nb+nc)-corrected
    assert actual==predicted,(p,n,a,b,c,actual,predicted,na,nb,nc)
    return actual


def gf343_cube_table():
    """GF(7^3)=F7[u]/(u^3-2); t^3-2 has no F7 root."""
    p=7
    elems=list(product(range(p),repeat=3))
    def mul(a,b):
        q=[0]*5
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                q[i+j]+=x*y
        q[0]+=2*q[3]
        q[1]+=2*q[4]
        return tuple(x%7 for x in q[:3])
    cube={v:mul(mul(v,v),v) for v in elems}
    return elems,cube


def test_extension():
    els,cubes=gf343_cube_table()
    zero=(0,0,0); one=(1,0,0)
    def twice(x):return tuple((2*v)%7 for v in x)
    # Homogeneous equation with (a,b,c)=(2,2,2), n=3, Q=343.
    count=0
    for y in els:
        y3=cubes[y]
        pA=(one==twice(y3))
        for z in els:
            z3=cubes[z]
            if pA or y3==twice(z3) or z3==(2,0,0):
                count+=1
    for z in els:
        if cubes[z]==zero or twice(cubes[z])==one:
            count+=1
    count+=1 # [0:0:1]
    assert count==3072,(count,3072)
    assert len(set(cubes.values()))== 1+(343-1)//3
    return count


def main():
    tested=0
    for p in (2,3,5,7,11,13):
        for n in (2,3,4,5):
            if gcd(p,n)!=1: continue
            for a,b,c in product(range(1,p),repeat=3):
                check_prime(p,n,a,b,c)
                tested+=1
    # One extreme arithmetic phenomenon: 9 geometric lines, but 3 F7- and F49-points.
    assert check_prime(7,3,2,2,2)==3
    assert test_extension()==3072
    print('TWISTED_CEVA_EXACT_CHECK_OK',f'prime_cases={tested}', 'F7=3', 'F343=3072')

if __name__=='__main__':main()
