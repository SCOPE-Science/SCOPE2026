#!/usr/bin/env python3
import sympy as sp

Lh=sp.Rational(871,5000)
Lv=sp.Rational(121,400)
muh=sp.Rational(1,10)
muv=sp.Rational(1,2)
beta1=beta2=sp.Rational(1)
alpha1=alpha2=sp.Rational(1,10)
delta=sp.Rational(1,10)
gamma=sp.Rational(2)
u=sp.Rational(1)
b=sp.Rational(20)

Sh=sp.Rational(1313,1500)
Ih=sp.Rational(1,10)
Rh=sp.Rational(2,3)
Sv=sp.Rational(101,200)
Iv=sp.Rational(1,10)

rhs = [
    Lh-beta1*Sh*Iv/(1+alpha1*Iv)-muh*Sh,
    beta1*Sh*Iv/(1+alpha1*Iv)-(muh+delta)*Ih-gamma*u*Ih/(1+b*u*Ih),
    gamma*u*Ih/(1+b*u*Ih)-muh*Rh,
    Lv-beta2*Sv*Ih/(1+alpha2*Ih)-muv*Sv,
    beta2*Sv*Ih/(1+alpha2*Ih)-muv*Iv,
]
assert all(sp.simplify(z)==0 for z in rhs)

R0sq=sp.simplify(beta1*beta2*Lh*Lv/(muv**2*muh*(muh+delta+gamma*u)))
assert R0sq == sp.Rational(9581,10000)
assert R0sq < 1

assert sp.simplify(Sh+Ih+Rh) == sp.Rational(821,500)
assert sp.simplify(Lh/muh) == sp.Rational(871,500)
assert Sh+Ih+Rh < Lh/muh
assert sp.simplify(Sv+Iv) == sp.Rational(121,200)
assert sp.simplify(Lv/muv) == sp.Rational(121,200)

I=sp.symbols("I", positive=True)
SvI=sp.simplify(Lv*(1+alpha2*I)/(beta2*I+muv*(1+alpha2*I)))
IvI=sp.simplify(beta2*SvI*I/(muv*(1+alpha2*I)))
ShI=sp.simplify(Lh/(muh+beta1*IvI/(1+alpha1*IvI)))
res=sp.factor(beta1*ShI*IvI/(1+alpha1*IvI)-(muh+delta)*I-gamma*u*I/(1+b*u*I))
expected=-I*(10*I-1)*(286420*I-4609)/(50*(20*I+1)*(14321*I+1000))
assert sp.simplify(res-expected)==0

Sh0=Lh/muh
Sv0=Lv/muv
printed_38 = (
    -(beta2*Lv*muh/muv)*(Sh-Sh0)**2/Sh
    -muv*(muh+delta+gamma*u)*(Sv-Sv0)**2/Sv
    -beta2*Sv0*b*u*(muh+delta)*Ih**2/(1+b*u*Ih)
    -(muh+delta+gamma*u)*muv*alpha1*Iv**2/(1+alpha1*Iv)
    -Iv/(1+alpha1*Iv)*(muh+delta+gamma*u)*muv*(1-R0sq)
)
assert sp.simplify(printed_38) == -sp.Rational(264869,3030000)
assert printed_38 < 0

print("VERIFY_OK")
print("R0_squared", R0sq)
print("equilibrium", (Sh,Ih,Rh,Sv,Iv))
print("endemic_equation", res)
print("printed_equation_3_8_at_equilibrium", sp.factor(printed_38))
