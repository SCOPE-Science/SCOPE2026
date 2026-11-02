from fractions import Fraction as F

n=5
tau=F(7,10)
a=F(1,1)
q=F(3,5)
R=tau*(n-2)
Fp=(R*(n*q-1)+(1-q))/(n*R)
Cp=(a+R)*(R-1)/Fp
Ft=F(n-1,n*n*(n-2))*((R*(n*q-2)+2*(1-q))/R)**2
Ct=(a+R)**2*(R-1)/Ft
B=R*(n*q-2)+2*(1-q)
H=n*(R*(n*q-1)+(1-q))
L=R*n*(R+a)/B
Q=H*(1-q)/((n-1)*B**2)
assert Cp == F(7161,920)
assert Ct == F(13985433,134560)
assert L == F(651,58)
assert Q == F(230,841)
assert Ct == L*Cp + Q*Cp*Cp
cp=Cp/2
ct=L*(Cp-cp)+Q*(Cp-cp)**2
chord=Ct*(1-cp/Cp)
gap=chord-ct
assert ct == F(592049997,12379520)
assert gap == F(51279921,12379520)
assert gap == Q*cp*(Cp-cp) and gap > 0
print('VERIFY_OK')
