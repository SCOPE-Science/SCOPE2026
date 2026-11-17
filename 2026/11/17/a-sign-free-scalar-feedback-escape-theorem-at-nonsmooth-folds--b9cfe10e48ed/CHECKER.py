#!/usr/bin/env python3
"""Exact-rational spot checks for a sign-free nonsmooth-fold escape identity."""
from fractions import Fraction as Q

def verify(g, dleft, dright, alpha, mu, eta):
    for xx in range(-6, 7):
        for yy in range(-6, 7):
            x = Q(xx, 6) * eta
            y = Q(yy, 6) * eta
            if x*x + y*y > eta*eta:
                continue
            delta = dleft if x <= 0 else dright
            nx = (1+delta-alpha)*x+y+mu if x <= 0 else (1+delta+alpha)*x+y+mu
            ny = -delta*x-g(y)
            phi = lambda u,v: u+v-g(v)-abs(g(v))
            increment = phi(nx,ny)-phi(x,y)
            identity = mu+alpha*abs(x)+abs(g(y))-g(ny)-abs(g(ny))
            assert increment == identity
            assert increment >= mu
    return True

def main():
    gs = [lambda y: y*y, lambda y: -y*y,
          lambda y: y*y+y*y*y, lambda y: y*y*y-y*y]
    count = 0
    for g in gs:
        for dl,dr in [(Q(-3),Q(2)),(Q(5),Q(-7)),(Q(-1),Q(-2)),(Q(0),Q(0))]:
            for alpha in [Q(1,3),Q(2)]:
                D=max(abs(dl),abs(dr))
                eps=min(Q(1,8),alpha/(8*(1+D)))
                # For all listed feedback choices, |g(z)| <= eps |z| on |z| <= eps/4.
                r=eps/4
                eta=min(Q(1),r/(2*(1+D)))
                assert verify(g,dl,dr,alpha,Q(1,1000),eta)
                count+=1
    print(f'NONSMOOTH_FOLD_SIGN_FREE_GAUGE_OK cases={count} rational_grid=13x13_per_case')

if __name__=='__main__':main()
