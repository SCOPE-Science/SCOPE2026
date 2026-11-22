"""Exact rational checks for the disphenoid radius/eccentricity profile.

Run with Python >=3.9, no third-party packages required.
The analytic proof, not this finite grid, establishes the universal theorem.
"""
from fractions import Fraction as Q

def inverse_h2(E, t):
    return (E*E + t*t + 1) * (1/(E*E) + 1/(t*t) + 1)

def limits(E):
    return (E + 1 + 1/E)**2, 5 + 2*(E*E + 1/(E*E))

def run():
    count=0
    for num in range(1,37):
        for den in range(1,num+1):
            E=Q(num,den)
            lo,hi=limits(E)
            for j in range(0,22):
                t=1+(E-1)*Q(j,21)
                x=inverse_h2(E,t)
                assert lo <= x <= hi
                assert x-lo == (1+1/E**2)*(t-E/t)**2
                assert hi-x == (1+1/E**2)*((t*t-1)*(E*E-t*t)/(t*t))
                assert x == inverse_h2(E,E/t)
                z=(x-(E*E+1/(E*E)+3))/(1+1/(E*E))
                assert z == t*t+E*E/(t*t)
                count+=5
            assert inverse_h2(E,Q(1))==hi
            assert inverse_h2(E,E)==hi
            assert inverse_h2(E*E,E)==limits(E*E)[0]  # t=sqrt(E^2)
            count+=3
    # Motivating tetrahedron with normalized box semiaxes (2,2,1)/3.
    assert inverse_h2(Q(2),Q(2))==Q(27,2)
    assert inverse_h2(Q(2),Q(1))==Q(27,2)
    assert 1/(4*(1-Q(2,27)))==Q(27,100)
    count+=3
    print('PASS:',count,'exact rational assertions; all identities agree.')

if __name__=='__main__': run()
