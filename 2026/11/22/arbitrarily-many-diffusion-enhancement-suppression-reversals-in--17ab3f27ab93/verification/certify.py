"""Exact rational sign witnesses for telegraph-switched periodic transport."""
from fractions import Fraction

def H(t, modes):
    t = Fraction(t)
    return sum((Fraction(w)*(t-k*k)/(t+k*k)**2 for k,w in modes), Fraction(0))

modes = [(1, Fraction(1)), (25, Fraction(50))]
times = [Fraction(1, 2), Fraction(2), Fraction(25), Fraction(1250)]
expected = [Fraction(-472678,1565001),Fraction(4177,131043),Fraction(-6,169),Fraction(379003,39125025)]
for t, e in zip(times,expected):
    a = H(t,modes)
    assert a == e
    print('2nu=',t,'H=',a,'sign=', '-' if a<0 else '+')
assert all(expected[i]*expected[i+1]<0 for i in range(3))
assert H(Fraction(1,2),[(1,Fraction(1))])<0
assert H(Fraction(2),[(1,Fraction(1))])>0
print('All rational sign witnesses pass')
