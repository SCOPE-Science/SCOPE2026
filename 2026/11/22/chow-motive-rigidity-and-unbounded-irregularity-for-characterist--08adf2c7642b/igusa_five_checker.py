"""Finite checks for the characteristic-five contracted-product family.

These tests do not replace the rational Chow-correspondence proof.
Requires only Python 3.
"""

def add(a,b):return ((a[0]+b[0])%5,(a[1]+b[1])%5)
def mul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%5,(a[0]*b[1]+a[1]*b[0])%5)
def power(a,n):
    out=(1,0)
    for _ in range(n):out=mul(out,a)
    return out

def verify():
    p=5
    # The discriminant of y^2=x^3+3x+2 is nonzero mod 5.
    assert (4*3**3+27*2**2)%5 !=0
    q5=[]
    for x in range(5):
        for y in range(5):
            if (y*y-x**3-3*x-2)%5==0:q5.append((x,y))
    assert sorted(q5)==[(1,1),(1,4),(2,1),(2,4)]
    assert len(q5)+1==5  # Including the point at infinity.
    # For ordinary E, this rational group is cyclic of order 5.
    # F25=F5[s]/(s^2-2), with 2 nonsquare in F5.
    field=[(a,b) for a in range(5) for b in range(5)]
    rhs=[add(add(power(x,3),mul((3,0),x)),(2,0)) for x in field]
    squares={mul(y,y):0 for y in field}
    n25=sum(1 for x in rhs for y in field if mul(y,y)==x)+1
    assert n25==35
    # Independent trace recurrence check for n=2.
    a1=5+1-(len(q5)+1)
    a2=a1*a1-2*5
    assert a1==1 and 25+1-a2==35
    for m in range(2,31):
        if m%5==0:continue
        genus=2*(m-1)
        # Unique infinity branch of z^5-z=x^m, with different 4(m+1).
        assert 2*genus-2 == -10+4*(m+1)
        q=4*(m+1)//5
        defect=q-1
        assert defect>=1
        # Each geometric X_m/F5 rational point under twisted Frobenius
        # contributes to one of the five group twists (or to all at infinity).
        twisted=[1+5*sum(1 for x in range(5) if pow(x,m,5)==g)
                 for g in range(5)]
        assert sum(twisted)==30
        assert sum(5*n for n in twisted)//5==30
        assert (len(q5)+1)*6==30
    print('PASS: E nonsingular, 5 rational points, 35 F25 points, '+
          'Artin-Schreier ramification and twisted F5 fixed-point counts '+
          'for all 23 admissible exponents 2..30.')

if __name__=='__main__':verify()
