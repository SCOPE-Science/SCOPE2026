"""Reproducible finite diagnostics for a critical logistic impulsive SIR model.
The infinite-time claims rely on the proof, not on this script.
Requires Python 3 with mpmath and sympy.
"""
import math
import mpmath as mp
import sympy as sp

S, I, A, beta, delta, q, T, tau=sp.symbols('S I A beta delta q T tau', positive=True)
Sd=S*(A-S-beta*I)
Id=I*(beta*S-delta)
identity=sp.simplify(beta*Sd/S+Id/I+beta*sp.log(q)/T+beta**2*I)
assert sp.simplify(identity.subs(delta,beta*(A+sp.log(q)/T)))==0
print('symbolic weighted-logarithmic derivative: PASS')

# RK4 with pulses at t=nT. Check the exact recurrence and the universal limit.
def run(A,beta,delta,T,S0,I0,nsteps=3000,substeps=40):
    q=math.exp(-(A-delta/beta)*T)
    assert 0<q<1 and 0<delta<beta*A
    S_star=A*(q*math.exp(A*T)-1)/(math.exp(A*T)-1)
    def bar_s(t):
        z=math.exp(A*t)
        return A*S_star*z/(A+S_star*(z-1))
    def w(t):
        return q**(-beta*t/T)*bar_s(t)**(-beta)
    mp.mp.dps=35
    C=beta**2*float(mp.quad(lambda s: mp.mpf(q)**(-beta*s/T)*(A*S_star*mp.exp(A*s)/(A+S_star*(mp.exp(A*s)-1)))**(-beta),[0,T]))
    def smp(t):
        z=mp.exp(A*t)
        return A*S_star*z/(A+S_star*(z-1))
    def weight_mp(t):return mp.mpf(q)**(-beta*t/T)*smp(t)**(-beta)
    def eB(t):return mp.exp(A*t)*S_star/smp(t)
    k0=beta*float(mp.quad(lambda u:eB(u)*weight_mp(u),[0,T]))/(math.exp(delta*T/beta)-1)
    susc_target=-S_star*k0/C
    dt=T/substeps
    def deriv(s,i): return s*(A-s-beta*i), i*(beta*s-delta)
    def rk4(s,i):
        a,b=deriv(s,i)
        c,d=deriv(s+dt*a/2,i+dt*b/2)
        e,f=deriv(s+dt*c/2,i+dt*d/2)
        g,h=deriv(s+dt*e,i+dt*f)
        return s+dt*(a+2*c+2*e+g)/6,i+dt*(b+2*d+2*f+h)/6
    s,i=S0,I0
    max_error=0.0
    positive=True
    last=None
    for n in range(nsteps):
        L0=s**beta*i
        integral=0.0
        mid_i=None
        for k in range(substeps):
            v0=q**(-beta*(k*dt)/T)*s**(-beta)
            s1,i1=rk4(s,i)
            v1=q**(-beta*((k+1)*dt)/T)*s1**(-beta)
            integral+=dt*(v0+v1)/2
            s,i=s1,i1
            if k+1==substeps//2: mid_i=i
            positive &= s>0 and i>0
        s*=q
        L1=s**beta*i
        # quadrature error is bounded by O(dt^2), so use a loose finite-check bound
        rel=abs((1/L1-1/L0)-beta**2*integral)/max(1, beta**2*integral)
        max_error=max(max_error,rel)
        if n==nsteps-1: last=(s,i,mid_i)
    s,i,mid_i=last
    predicted0=w(0)/C
    predicted_half=w(T/2)/C
    measured0=nsteps*i
    measured_half=nsteps*mid_i
    err0=abs(measured0/predicted0-1)
    errhalf=abs(measured_half/predicted_half-1)
    print(f'A={A}, beta={beta}, delta={delta}, T={T}, q={q:.7f}, n={nsteps}')
    print(f'  nI(nT) {measured0:.8g} predicted {predicted0:.8g} relerr={err0:.4g}')
    print(f'  nI(nT+T/2) {measured_half:.8g} predicted {predicted_half:.8g} relerr={errhalf:.4g}')
    print(f'  n(S_n-S*) {nsteps*(s-S_star):.8g} predicted {susc_target:.8g}')
    err_susc=abs(nsteps*(s-S_star)-susc_target)/max(abs(susc_target),1e-10)
    print(f'  susceptible correction relative error={err_susc:.4g}')
    print(f'  inverse-L period identity quadrature max relative error={max_error:.3g}')
    assert positive and max_error<0.001 and err0<0.08 and errhalf<0.08 and err_susc<0.08

run(.8,2.0,.6,1.0,.3,.1)
run(1.1,1.8,.9,.75,.08,.25)
run(1.2,1.5,.7,2.0,.2,.05)
print('finite analytic-identity and asymptotic diagnostics: PASS')
