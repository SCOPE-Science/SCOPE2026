"""Bounded recovery test for GM-threefold point-projection tilt wall at beta=-1.

Provisional Chern arithmetic (unverified constants flagged):
- H^3 = 10, td = 1 + H/2 + 17/60 H^2 + H^3/10.
- Assumes h0(U^vee)=5 and vanishing of higher cohomology so chi(O,U^vee)=5,
  forcing d = H.c2(U^vee) = 4 via chi = 9 - d.
- Assumes Ku1 projection pr = L_U L_O (order unconfirmed) vs alternative
  L_O L_{U^vee}; both give rank 5 but ch1 = -3H vs -2H.

Shows:
1. tilt slope of provisional v1 at beta=-1 as function of alpha;
2. rank-one numerical wall equation nu(F)=nu(v1) has infinite integer
   solutions (x=H^2.ch1^beta, y=H.ch2^beta) without a generalized-BG bound;
3. wall radius/centre depends on unverified d and unknown BG constant.
Conclusion printed: BLOCKED.
"""
H3 = 10

def tilt_slope(r, x, y, alpha, beta=-1.0):
    # x = H^2.ch1^beta, y = H.ch2^beta
    # mu = -(y - alpha^2/2*H^3*r)/x  (for x>0)
    if x == 0:
        return float("inf")
    return -(y - 0.5*alpha**2*H3*r)/x

# Provisional v1 variants
for label, r, H2c1, Hc2 in [("L_O L_Uvee order",5,-20,None),("L_U L_O order",5,-30,None)]:
    # ch1^beta = ch1 + r*H (beta=-1): H^2.ch1^beta = H2c1 + r*H3
    x = H2c1 + r*H3
    print(label, "rank",r,"H2c1",H2c1,"x(beta=-1)",x)

# Take x1=30 (first convention: -20+50=30)
r1, x1 = 5, 30
# y1 = H.ch2^beta depends on d; with d=4 provisional: compute roughly
# ch2(U^vee)=(H^2-2c2)/2 -> H.ch2 = (10-2d)/2 = (10-8)/2=1
# ch(pr) ch2 = ? L_O L_Uvee: ch2(pr)= ch2(Ox)-2 ch2(U^vee)+9*0? Ox ch2=0.
# ch2(Ox)=0 so ch2(pr) = -2*ch2(U^vee) = -(H^2-2c2) -> H.ch2(pr)= -(10-8)=-2? then
# ch2^beta = ch2 + H.ch1 + H^2 r/2 -> H.ch2^beta = -2 + (-20) + 5*10/2=+3? gives y1=3.
y1 = 3.0
print("provisional y1(beta=-1) =",y1,"(depends on unverified d=4)")
for a in [0.1,0.3,0.5,1.0]:
    print(f"  alpha={a} nu(v1)={(3-0.5*a*a*H3*r1)/x1:.6f} (formula (y-..)/x signconv) mu={tilt_slope(r1,x1,y1,a):.6f}")

# Rank-one numerical candidates: nu(F)=nu(v1) at some alpha>0.
# Write X=H^2.ch1^beta(F), Y=H.ch2^beta(F), rF=1.
# Equality: (Y-2.5 a^2)/X = (y1-12.5 a^2)/x1  (since .5*H3*r =2.5 / 12.5)
# For each integer X in 1..50, Y integer/half-integer, there is a>=0 solving unless degenerate.
# Count solutions with small height to show infinitude without BG bound.
sols=[]
for X in range(1,51):
    for Y2 in range(-50,101):  # Y = Y2/2
        Y=Y2/2
        # solve for a^2: (Y x1 - y1 X) = a^2(2.5 x1 -12.5 X)
        num = Y*x1 - y1*X
        den = 2.5*x1 - 12.5*X
        if abs(den)<1e-9:
            if abs(num)<1e-9:
                sols.append((X,Y,"all-alpha"))
        else:
            a2=num/den
            if a2>0 and a2<10:
                sols.append((X,Y,a2))
print(f"rank-one numerical solutions with X<=50,|Y|<=25,0<a^2<10: {len(sols)} (infinite family; BG bound missing)")
print("e.g.",sols[:8])
print("RESULT: BLOCKED — finite BG-compatible destabilizer list not closable; d, chi-vanishings, Li boundary constant, heart membership unverified.")
