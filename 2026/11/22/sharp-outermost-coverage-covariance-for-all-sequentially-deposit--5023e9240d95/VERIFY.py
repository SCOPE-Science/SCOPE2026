"""Independent finite-priority checks for outermost correlations in random sequential covering.

Run: python3 VERIFY.py
No nonstandard Python modules are required. Finite enumeration checks cannot replace
proofs for arbitrary polymer length or real time.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, factorial, exp


def independent_variance_infinity(k):
    # E h^2 - (E h)^2, with h(Y)=Y^(k-1)/(k-1)-Y^k/k,
    # Y uniform on [0,1].
    second = (Q(1, (k-1)**2*(2*k-1))
              - Q(1, k*k*(k-1))
              + Q(1, k*k*(2*k+1)))
    mean = Q(2, k*(k*k-1))
    return second-mean*mean


def claimed_variance_infinity(k):
    return Q(5*k+2, k*k*(k+1)**2*(2*k-1)*(2*k+1))


def conditional_polynomial_by_orders(k):
    """Exact E[K_0 | exp(-U_{k-1})=y] via all local clock orders.

    If the common clock has r earlier (smaller U) competitors, a specified
    ordering of its N other clocks has conditional probability
    (1-y)^r y^(N-r)/(r! (N-r)!).
    """
    positions = tuple(range(-2*k+2, k))
    common = k-1
    N = len(positions)-1
    coef = [Q(0) for _ in range(N+1)]
    checked = 0
    for ordered in permutations(positions):
        ranks = {position: rank for rank, position in enumerate(ordered)}
        c0 = 0
        for i in range(-k+1,1):
            accepted = False
            for site in range(i,i+k):
                if ranks[i] == min(ranks[j] for j in range(site-k+1,site+1)):
                    accepted = True
                    break
            c0 += accepted
        r = ranks[common]
        # Expand (1-y)^r*y^(N-r).
        multiplier = Q(c0, factorial(r)*factorial(N-r))
        for j in range(r+1):
            coef[N-r+j] += multiplier*comb(r,j)*(-1)**j
        checked += 1
    assert checked == factorial(N+1)
    return coef, checked


def poly_integral(p):
    return sum((a/Q(i+1) for i,a in enumerate(p)), Q(0))


def poly_squared_integral(p):
    return sum((a*b/Q(i+j+1) for i,a in enumerate(p)
                for j,b in enumerate(p)), Q(0))


def J(k,t):
    return (1-exp(-k*t))/k


def finite_time_formula(k,t):
    a = J(k,t)-J(k+1,t)
    b = 2*(a/(k*(k-1))-(J(2*k-1,t)-J(2*k,t))/(k-1)
           +(J(2*k,t)-J(2*k+1,t))/k)
    return b-a*a


def g(k,t):
    return ((1-exp(-(k-1)*t))/(k-1) - (1-exp(-k*t))/k)


def quadrature_expectation(k,t,num=12000):
    # Numerically integrate E[g(U wedge t)] and E[g(U wedge t)^2]
    # under an exponential first-attempt clock, independently of the J formula.
    h=t/num
    values=[]
    for power in (1,2):
        sm=g(k,0)**power
        for i in range(1,num):
            x=i*h
            sm += (4 if i%2 else 2)*exp(-x)*g(k,x)**power
        sm += exp(-t)*g(k,t)**power
        values.append(sm*h/3 + exp(-t)*g(k,t)**power)
    return values[1]-values[0]**2


def main():
    count=0
    for k in range(2,2001):
        assert independent_variance_infinity(k)==claimed_variance_infinity(k)
        count+=1
    print('Exact all-length saturated rational identity:',count,'sizes')
    for k in (2,3):
        coef,total=conditional_polynomial_by_orders(k)
        # The predicted dependence on y is constant - y^(k-1)/(k-1)+y^k/k.
        assert coef[k-1]==-Q(1,k-1) and coef[k]==Q(1,k)
        for j in range(1,len(coef)):
            if j not in (k-1,k):assert coef[j]==0
        e=poly_integral(coef)
        var=poly_squared_integral(coef)-e*e
        assert var==claimed_variance_infinity(k), (k,var)
        print(f'Exact first-arrival order enumeration: k={k}, {total} orders, V={var}')
    cases=0
    for k in (2,3,4,5,6,9):
        for t in (0.15,0.4,0.9,2.0,4.5):
            v=finite_time_formula(k,t)
            vind=quadrature_expectation(k,t,3000)
            assert v>0
            assert abs(v-vind)<4e-9, (k,t,v,vind)
            assert v< float(claimed_variance_infinity(k))+1e-11
            cases+=1
    print('Independent finite-time exponential quadrature:',cases,'comparisons')
    print('PASS')

if __name__=='__main__':main()
