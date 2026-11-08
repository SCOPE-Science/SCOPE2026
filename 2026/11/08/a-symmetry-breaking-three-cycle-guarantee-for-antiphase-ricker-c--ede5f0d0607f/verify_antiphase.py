"""Finite-precision diagnostics for the analytical Ricker antiphase multiplicity theorem.
This diagnostic is not an exhaustive or independent proof.
"""
import mpmath as mp
mp.mp.dps = 65

def solve(L, c):
    L=mp.mpf(L);c=mp.mpf(c)
    U=lambda t: 2*mp.atanh(t/L)
    A=lambda t:t-U(t)
    F=lambda t:A(t)/c
    phi=lambda t:mp.atanh(t)/t+1/(1-t*t)
    tc=mp.findroot(lambda t: phi(t)-L,(mp.mpf('.1'),mp.mpf('.8')))
    cc=1-2*mp.atanh(tc)/(L*tc)
    q=mp.findroot(lambda t:U(t)/t-(1-c),(mp.mpf("1e-8"),L*(1-mp.mpf("1e-40"))),solver="bisect",maxsteps=300)
    assert 0<c<cc<1-2/L
    assert F(q)==mp.mpf(q) or abs(F(q)-q)<mp.mpf('1e-55')
    assert (1-2/(L*(1-(q/L)**2)))/c<-1
    # Use two-variable high precision root from a starting point off the diagonal.
    guesses={3:(mp.mpf('1.2'),mp.mpf('2.4')),4:(mp.mpf('1.5'),mp.mpf('3.4'))}
    if L in guesses: g=guesses[int(L)]
    else: g=(q*mp.mpf('.45'),q*mp.mpf('1.1'))
    try:
        u,w=mp.findroot(lambda u,w:(A(u)-c*w,A(w)-c*u),g)
    except Exception:
        u,w=mp.findroot(lambda u,w:(A(u)-c*w,A(w)-c*u),(q*.6,q*1.15))
    assert min(u,w)>0 and max(u,w)<L and abs(u-w)>mp.mpf('1e-20')
    assert abs(A(u)-c*w)<mp.mpf('1e-55') and abs(A(w)-c*u)<mp.mpf('1e-55')
    growth=mp.exp((1+c)*L)
    T=lambda x,y:(growth*x*mp.exp(-x-c*y), growth*y*mp.exp(-c*x-y))
    for aa,bb in [(u,w),(w,u),(q,q)]:
        x,y=L+aa,L-bb
        xx,yy=T(x,y)
        assert abs(xx-(L-aa))<mp.mpf('1e-55')
        assert abs(yy-(L+bb))<mp.mpf('1e-55')
        xxx,yyy=T(xx,yy)
        assert abs(xxx-x)<mp.mpf('1e-55')
        assert abs(yyy-y)<mp.mpf('1e-55')
    print('L=',mp.nstr(L,6),'c=',mp.nstr(c,6),'c_critical=',mp.nstr(cc,18), 'q=',mp.nstr(q,16),'u=',mp.nstr(u,16),'w=',mp.nstr(w,16))

if __name__=='__main__':
    solve('3','0.15')
    solve('4','0.2')
    print('VERIFY_OK log_cycle_relation_checked=1 three_distinct_cycles_per_case=3 parameter_cases=2 high_precision=65')
