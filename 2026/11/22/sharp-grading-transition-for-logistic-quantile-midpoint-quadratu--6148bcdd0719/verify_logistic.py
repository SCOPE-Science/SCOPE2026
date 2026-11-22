"""Numerical checks of explicit logistic weighted-Sobolev quadrature identities.

Requires mpmath. This is a finite diagnostic; limiting theorems require the proof.
"""
from mpmath import mp
mp.dps = 75

def psi(t,p):
    a=t**p; b=(1-t)**p
    return a/(a+b)

def primitive(u,c):
    if c==0 and u==0: return mp.mpf(1)
    if c==1 and u==1: return mp.mpf(-1)
    return -c*c/u + (1-c)**2/(1-u) + 2*c*(c-1)*mp.log(u/(1-u))

def error_squared(n,p):
    n=int(n); p=mp.mpf(str(p)); ans=mp.mpf(0)
    for j in range(1,n+1):
        a=psi(mp.mpf(j-1)/n,p)
        b=psi(mp.mpf(j)/n,p)
        mid=psi((mp.mpf(j)-mp.mpf('0.5'))/n,p)
        ans += primitive(mid,a)-primitive(a,a) + primitive(b,b)-primitive(mid,b)
    return ans

checks=0
for n in [1,2,3,4,5,8,16,24,48,80]:
    e=error_squared(n,1)
    assert e>0
    if n==1:
        assert abs(e-2)<mp.mpf('1e-60')
    checks+=1
for p in [mp.mpf('1.5'),mp.mpf('2'),mp.mpf('2.5'),mp.mpf('3')]:
    for n in [2,4,8,16,40]:
        e=error_squared(n,p)
        assert e>0
        checks+=1
C1=2*mp.log(2)
C2=mp.mpf(4)/3
C3=mp.mpf(9)/2+2*mp.sqrt(3)*mp.pi
C25=mp.mpf('2.5')**2/2+2*mp.pi*mp.mpf('2.5')/(3*mp.sin(mp.pi/mp.mpf('2.5')))+mp.pi*mp.mpf('2.5')/(3*mp.sin(2*mp.pi/mp.mpf('2.5')))
# Rigorous identities of the symbolic constants, checked at high precision.
assert abs(C3-(mp.mpf('4.5')+2*mp.sqrt(3)*mp.pi))<mp.mpf('1e-70'); checks+=1
assert abs(mp.mpf(3)**2/2+2*mp.pi*3/(3*mp.sin(mp.pi/3))+mp.pi*3/(3*mp.sin(2*mp.pi/3))-C3)<mp.mpf('1e-70'); checks+=1
# Approach to the exact leading constants, without treating it as proof.
assert abs(80*error_squared(80,1)-C1)<mp.mpf('0.06'); checks+=1
assert abs(40**2*error_squared(40,3)-C3)<mp.mpf('0.3'); checks+=1
assert abs(40**2*error_squared(40,mp.mpf('2.5'))-C25)<mp.mpf('0.2'); checks+=1
print('VERIFY_OK',checks)
for p in ['1','1.5','2','2.5','3']:
    n=80
    e=error_squared(n,p)
    if mp.mpf(p)<2: scale=n**mp.mpf(p)
    elif p=='2': scale=n*n/mp.log(n)
    else: scale=n*n
    print('p',p,'n',n,'scaled E2',mp.nstr(e*scale,16))
print('C1',mp.nstr(C1,16),'C2',mp.nstr(C2,16),'C2.5',mp.nstr(C25,16),'C3',mp.nstr(C3,16))
