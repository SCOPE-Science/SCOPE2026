#!/usr/bin/env python3
"""Numerical checks of exact reactive-center run-and-tumble moments.

Uses only Python's standard library. Numeric checks corroborate, but do not
replace, the uniform analytic estimates in RESULT.md.
"""
from decimal import Decimal as D, getcontext
getcontext().prec = 65
one = D(1)

def eval_at(a, z):
    a,z=D(str(a)),D(str(z))
    t=z/a
    y=(-z).exp()
    q=y/(one-y)
    Q=q*(one+q)
    P=D(3)/4+2*t+D(37)/12*t*t+D(5)/2*t**3+D(28)/45*t**4
    A=one+2*t+4*t*t+D(8)/3*t**3
    B=(one+2*t)**2
    m=D(1)/2+D(3)/2*t+D(2)/3*t*t+q*(one+2*t)
    V=P+q*A+Q*B
    dm=D(3)/2+D(4)/3*t+2*q-a*Q*(one+2*t)
    dP=2+D(37)/6*t+D(15)/2*t*t+D(112)/45*t**3
    dA=2+8*t+8*t*t
    dB=4*(one+2*t)
    dV=dP+q*dA-a*Q*A+Q*dB-a*Q*(one+2*q)*B
    return m,V,dm,dV

def optimum(a, which):
    a=D(str(a))
    lo=D('1e-35'); hi=D('1e35')
    assert eval_at(a,lo)[which]<0 and eval_at(a,hi)[which]>0
    for _ in range(275):
        mid=(lo+hi)/2
        if eval_at(a,mid)[which]>0: hi=mid
        else: lo=mid
    z=(lo+hi)/2
    return a/z,z

passed=0
for a_s in ['0.000000001','0.000001','0.0001','0.01','0.1','1','2','10','100','10000','100000000','1000000000000']:
    a=D(a_s)
    vm,zm=optimum(a,2)
    vv,zv=optimum(a,3)
    assert vm>0 and vv>0
    for z0 in (zm,zv):
        t=z0/a; q=(-z0).exp()/(one-(-z0).exp()); Q=q*(one+q)
        Vfirst=D(3)/4+2*t+D(37)/12*t*t+D(5)/2*t**3+D(28)/45*t**4
        Vreturn=one+2*t+4*t*t+D(8)/3*t**3
        Mreturn=one+2*t
        assert abs(eval_at(a,z0)[1]-(Vfirst+q*Vreturn+Q*Mreturn*Mreturn)) < D('1e-45')*max(one,a)
        passed+=1
    assert abs(eval_at(a,zm)[2])<D('1e-24')*max(one,a)
    assert abs(eval_at(a,zv)[3])<D('1e-24')*max(one,a)
    assert eval_at(a,zm)[0] <= eval_at(a,zm*D('0.97'))[0]
    assert eval_at(a,zv)[1] <= eval_at(a,zv*D('1.03'))[1]
    if a <= D('0.01'): assert vv>vm
    if a >= D('10'): assert vm>vv
    passed+=6
    if a_s in ['0.000001','1','2','10','100000000']:
        print('a=',a,'mean_speed=',float(vm),'variance_speed=',float(vv))

# Probe precisely the analytic first corrections and the strong-log offset.
c=(D(4)/D(3))**(one/3)
for aa in ['1e-12','1e-15','1e-18']:
    a=D(aa); e=a**(one/3)
    vm,_=optimum(a,2); vv,_=optimum(a,3)
    assert abs((vm-c*e)/(e*e)-c*c/8)<D('0.000005')
    assert abs((vv-c*e)/(e*e)-c*c/5)<D('0.000005')
    passed+=2
for aa in ['1e12','1e15','1e18']:
    a=D(aa); vm,zm=optimum(a,2); vv,zv=optimum(a,3)
    assert abs((zm-(2*a/3).ln()))<D('0.0001')
    assert abs((zv-a.ln()))<D('0.0001')
    passed+=2
# Exact q and Q hyperbolic lower bounds on a broad logarithmic range.
for zz in ['0.000000001','0.001','0.1','1','3','10','30']:
    z=D(zz); q=one/(z.exp()-one); Q=q*(one+q)
    assert q >= one/z-D(1)/2
    assert Q >= one/(z*z)-one/12
    passed+=2
print('PASS',passed,'deterministic assertions')
