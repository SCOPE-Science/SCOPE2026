#!/usr/bin/env python3
"""Independent ODE checks for strict-dominance log-evidence flows."""
import math
from scipy.integrate import solve_ivp

def softplus(z): return max(z,0)+math.log1p(math.exp(-abs(z)))
def check(a0,a1,b0,b1,u0,v0):
    # a1 is payoff gap against opponent's dominant (first) action.
    lam=math.sqrt(a1*b1)
    def f(t,z):
        u,v=z
        return [a1*softplus(v)+a0*softplus(-v), b1*softplus(u)+b0*softplus(-u)]
    end=5/lam
    sol=solve_ivp(f,(0,end),(u0,v0),rtol=2e-12,atol=2e-12,dense_output=True)
    assert sol.success
    c=[]
    for t in [end*.85,end*.925,end]:
        u,v=sol.sol(t)
        L=math.exp(-lam*t)*(math.sqrt(b1)*u+math.sqrt(a1)*v)
        c.append(L)
    assert c[-1]>0
    assert abs(c[-1]-c[-2])<1e-5*max(1,c[-1]),(a0,a1,b0,b1,c)
    u,v=sol.y[:,-1]
    assert abs(math.sqrt(b1)*u-math.sqrt(a1)*v)<0.1*max(1,u+v)
    return c[-1]

def main():
    trials=[(1,1,1,1,0,0),(3,1,4,2,-1,2),(1,4,2,1,2,-2),(.2,1.2,3,2,-3,-1),(2,2,1,3,3,-3)]
    values=[check(*row) for row in trials]
    print('PASS 5 coupled log-odds integrations:',values)
if __name__=='__main__':main()
