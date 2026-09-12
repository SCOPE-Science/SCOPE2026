import math, json
g=9.81
lammin = 6-2*math.sqrt(5)
assert lammin > 1.52
inv0 = 1/lammin
assert inv0 < 0.66
Gfro = math.sqrt(12); Gn = 3.5
gradU = math.sqrt(2)*g
Umin=-3*g
KEmax = -8-Umin; P0=math.sqrt(2*KEmax)
assert KEmax < 21.5 and P0 < 6.6
P = 8.0
h1=2*P**2; h2=2*(2*P)**2
rhs=math.sqrt((2*g+h1)**2+h2**2)
lammax=inv0*rhs
assert rhs < 540 and lammax < 360
M0 = math.sqrt(P**2+(gradU+Gn*lammax)**2)
assert M0 < 1300
R=0.02
dG = 2*math.sqrt(6)*R
pert = dG*(2*Gfro+dG)
assert pert < lammin/2*0.95
invC = 1/(lammin-pert)
assert invC < 1.25
Gc = Gfro+dG; Pc = P+R
hc1=2*Pc**2; hc2=2*(2*Pc)**2
rhsc=math.sqrt((2*g*(1+R)+hc1)**2+hc2**2)
lamc=invC*rhsc
Mc=math.sqrt(Pc**2+(gradU*(1+R)+Gc*lamc)**2)
M=3000.0
assert M > Mc*1.2, (M,Mc)
D=12.0
K = 2000*M**7/R**6
print("M=%.0f Mc=%.1f M/R=%.3e K=%.3e"%(M,Mc,M/R,K))
L1=30000.0; Mreal=1300.0
F2 = 10*L1*Mreal*(1+L1)
B2real = D*F2
F4 = 10*(L1**4)*Mreal**2
B4real = D*F4
print("B2real=%.3e B4real=%.3e"%(B2real,B4real))
B2a=2e15; B4a=2e27; Ka=1e38  # Htilde=H+h^2 H2+h^4 H4 (symmetric: even powers only); one-step drift |Htilde(y+)-Htilde(y)|<=Ka h^6
assert B2a>B2real*1.2 and B4a>B4real*1.2 and Ka>K*1.2
h0=1e-9; c=1e-23; C=1e16
assert h0<=0.01 and h0*M/R < 0.08
Cneed = 2*B2a + 2*B4a*h0**2 + Ka*c*h0  # |H-H0|<=2 B2a h^2+2 B4a h^4+Ka c h^3; Cneed per h^2
print("Cneed=%.3e C=%.3e"%(Cneed,C))
assert Cneed < C*0.8
Emargin = C*h0**2
print("C*h0^2=%.4f T(h0)=%.3e steps=%.3e"%(Emargin,c/h0**2,c/h0**3))
assert Emargin < 0.4
# energy tube stays inside momentum ball
Htop=-7.9+0.0  # worst H after drift 0.1 above -8
KEworst = (-8+Emargin)-Umin
Pworst = math.sqrt(2*KEworst)
print("KEworst=%.3f Pworst=%.3f < P=%.1f"%(KEworst,Pworst,P))
assert Pworst < P*0.95
# ledger constant
LH = max(P,gradU)
smin = math.sqrt(lammin)
C2need = LH*(0.6+0.81+0.3)
print("LH=%.2f smin=%.3f C2need=%.1f"%(LH,smin,C2need))
C2=200.0
assert C2 > C2need*3
json.dump({"lammin":lammin,"inv0":inv0,"P0":P0,"M0":M0,"R":R,"M":M,
 "B2a":B2a,"B4a":B4a,"Ka":Ka,"h0":h0,"c":c,"C":C,"C1":C,"C2":C2,
 "Cneed":Cneed,"Emargin":Emargin,"Pworst":Pworst,"K":K,"B2real":B2real,"B4real":B4real},
 open("output/artifacts/final_certificate.json","w"),indent=1)
print("ALL CERTIFICATE CHECKS PASSED")
