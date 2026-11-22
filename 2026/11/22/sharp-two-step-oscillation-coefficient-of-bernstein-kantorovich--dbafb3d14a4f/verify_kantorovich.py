"""Exact-rational checks for two-step classical Bernstein-Kantorovich oscillation modulus."""
from fractions import Fraction as Q
from math import comb

def a_entry(n,k,j):
    # (n+1) times integral on cell k of the jth Bernstein basis
    lo=Q(k,n+1); hi=Q(k+1,n+1)
    return (n+1)*comb(n,j)*sum(((-1)**r)*comb(n-j,r)*(hi**(j+r+1)-lo**(j+r+1))/Q(j+r+1) for r in range(n-j+1))

def end_probability(n,j):
    # independent representation: integrate after substituting u=(n+1)t
    return Q(comb(n,j),(n+1)**j)*sum(Q((-1)**r*comb(n-j,r), (j+r+1)*(n+1)**r) for r in range(n-j+1))

def defect(n):
    p=[end_probability(n,j) for j in range(n+1)]
    return sum((min(p[j],p[n-j]) for j in range(n+1)),Q(0))

def test():
    for n in range(1,15):
        A=[[a_entry(n,k,j) for j in range(n+1)] for k in range(n+1)]
        assert all(sum(row)==1 for row in A)
        p=A[0]; rev=A[-1]
        assert p==[end_probability(n,j) for j in range(n+1)]
        assert rev==list(reversed(p))
        assert all(p[j]>p[n-j] for j in range((n+1)//2))
        delta=defect(n)
        assert delta==sum(min(p[j],rev[j]) for j in range(n+1))
        if n%2==0:
            mid=n//2
            assert delta==p[mid]+2*sum(p[mid+1:],Q(0))
        else:
            assert delta==2*sum(p[(n+1)//2:],Q(0))
        # endpoint difference maximal among transition laws at rational x on 1/10 grid
        def p_of(x):
            return [sum((Q(comb(n,k))*x**k*(1-x)**(n-k)*A[k][j] for k in range(n+1)),Q(0)) for j in range(n+1)]
        vals=[p_of(Q(k,10)) for k in range(11)]
        for aa in range(11):
            for bb in range(aa+1,11):
                tv=sum((abs(vals[aa][j]-vals[bb][j]) for j in range(n+1)),Q(0))/2
                assert tv<=1-delta, (n,aa,bb,tv,delta)
        print(f'n={n:2d} deficit={delta} modulus={1-delta} decimal={float(1-delta):.12g}')
    print('EXACT_ALL_TRANSITION_AND_TV_CHECKS_PASS')

if __name__=='__main__':test()
