"""Exact algebra checks for the normalized coexistence wedge (Python 3, SymPy)."""
import sympy as s


def check():
    v, k, tau, rho, eta = s.symbols('v k tau rho eta', real=True)
    H = 2/(1+k*(1-v))-1-tau*v
    P = 2-(1+tau*v)*(1+k*(1-v))
    K = (1-tau*v)/((1-v)*(1+tau*v))
    assert s.cancel(H*(1+k*(1-v))-P) == 0
    assert s.cancel(P.subs(k,K)) == 0
    T = 1-rho**2/2
    for sign in (-1,1):
        root = (1+sign*rho)/T
        assert s.cancel(s.diff(K,v).subs({tau:T,v:root},simultaneous=True)) == 0
        assert s.cancel(K.subs({tau:T,v:root},simultaneous=True)-2*T/(2+sign*rho)**2) == 0
    assert s.cancel(1-2*T/(2-rho)**2-2*(1-rho)**2/(2-rho)**2) == 0
    jet = s.series((2*tau/(2-s.sqrt(2*(1-tau)))**2).subs(tau,s.Rational(1,2)+eta),eta,0,4)
    assert jet.removeO() == 1-2*eta**2+2*eta**3
    assert s.simplify(s.diff(H.subs(k,1),v).subs(v,0)) == s.Rational(1,2)-tau
    case = P.subs({k:s.Rational(99,100),tau:s.Rational(3,5)})
    roots = [(17+sign*2*s.sqrt(31))/99 for sign in (-1,1)]
    assert all(0<x<1 and s.simplify(case.subs(v,x))==0 for x in roots)
    print('PHYSICAL_FOLD_ALGEBRA_OK')


if __name__ == '__main__':
    check()
