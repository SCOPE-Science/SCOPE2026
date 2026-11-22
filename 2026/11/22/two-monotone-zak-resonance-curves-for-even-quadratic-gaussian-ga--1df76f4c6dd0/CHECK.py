"""Finite numerical cross-checks for the two Zak-fiber quadratic-Gaussian resonance curves.

Run: python3 CHECK.py. Standard library only. These tests do not prove the theorem.
"""
import math
import cmath

PI=math.pi

def c_plus(a):
    v=a*a
    if a<=0.7:
        num=sum(((-1)**j)*j*j*math.exp(-PI*j*j/v) for j in range(-10,11))
        den=sum(((-1)**j)*math.exp(-PI*j*j/v) for j in range(-10,11))
        return 1/(2*PI)-num/(v*den)
    vals=[math.exp(-PI*v*(k+0.5)**2) for k in range(-30,30)]
    return v*sum((k+0.5)**2*z for k,z in zip(range(-30,30),vals))/sum(vals)

def c_minus(a):
    return 1/(2*PI)-c_plus(1/(2*a))

def zak(a,c,x,omega):
    return sum((((x+a*k)**2-c)*math.exp(-PI*(x+a*k)**2)*cmath.exp(-2j*PI*k*omega) for k in range(-75,76)),0j)

def small_grid_dual(a):
    v=a*a
    z=sum((-1)**j*math.exp(-4*PI*v*j*j) for j in range(-30,31))
    assert z>0
    return 4*v*sum((-1)**j*j*j*math.exp(-4*PI*v*j*j) for j in range(-30,31))/z

count=0
for a in [0.32,0.40,0.5,0.65,0.8,1.0,1.25,1.75,2.5]:
    cp=c_plus(a)
    cm=c_minus(a)
    assert cp>1/(2*PI)-1e-12 and cm<1e-11
    count+=2
    for c,omega,x in [(cp,0,a/2),(cm,0.25,0)]:
        z0=zak(a,c,x,omega)
        z1=zak(a,c,x,omega+0.5)
        assert abs(z0)<4e-11 and abs(z1)<4e-11, (a,c,omega,z0,z1)
        count+=2
    if a>=0.32:
        assert abs(small_grid_dual(a)-cm)<2e-8, (a,small_grid_dual(a),cm)
        count+=1
    for c in [cp-0.17,cp+0.23]:
        S=sum(math.exp(-PI*a*a*(k+0.5)**2) for k in range(-30,30))
        err=abs(zak(a,c,a/2,0))**2+abs(zak(a,c,a/2,0.5))**2
        assert abs(err-S*S*(c-cp)**2)<3e-10, (a,c,err)
        count+=1
    for c in [cm-0.17,cm+0.23]:
        D=sum((-1)**j*math.exp(-4*PI*a*a*j*j) for j in range(-30,31))
        err=abs(zak(a,c,0,0.25))**2+abs(zak(a,c,0,0.75))**2
        assert abs(err-2*D*D*(c-cm)**2)<3e-10, (a,c,err)
        count+=1
for i in range(45,500):
    a=i/150
    assert c_plus(a+1/150)>=c_plus(a)-1e-12
    assert c_minus(a+1/150)>=c_minus(a)-1e-12
    count+=2
assert c_plus(2)>0.99 and c_minus(.25)<-.7
count+=2
print('PASS:',count,'standalone checks, with finite tests not used as proof')
