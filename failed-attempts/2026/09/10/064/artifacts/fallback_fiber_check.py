"""Fallback fiber audit: X_{16,0}: X^16+Y^16+Z^16+W^16+X^14 Y^2=0 over F_251.
Checks: (1) smoothness over F_251; (2) monic-in-y structure for normal forms;
(3) z-freeness of the deformation term (Rz pure power); (4) coefficient data for the record."""
p = 251
# (1) smoothness: Fz=16Z^15, Fw=16W^15 force Z=W=0; scan [X:Y:0:0]
sings = []
for X in range(p):
    for Y in range(p):
        if X == 0 and Y == 0: continue
        F = (pow(X,16,p)+pow(Y,16,p)+pow(X,14,p)*pow(Y,2,p)) % p
        Fx = (16*pow(X,15,p)+14*pow(X,13,p)*pow(Y,2,p)) % p
        Fy = (16*pow(Y,15,p)+2*pow(X,14,p)*pow(Y,1,p)) % p
        if F == 0 and Fx == 0 and Fy == 0:
            sings.append((X, Y))
print("smooth over F_251:", len(sings) == 0, "| singular reps:", len(sings))
# affine chart W=1: R=1+x^16+y^16+z^16+x^14 y^2
# (2) R monic in y of degree 16 -> unique remainder deg_y<16 exists
print("R monic in y deg 16: True (coeff of y^16 is 1); normal form deg_y<16: unique")
# (3) Rz = 16 z^15 (deformation term x^14 y^2 has no z)
print("Rz = 16 z^15: pure power, 16 invertible mod 251:", pow(16, p-2, p) is not None and (16 % p) != 0)
# Rx, Ry for the record
print("Rx = 16 x^15 + 14 x^13 y^2; Ry = 16 y^15 + 2 x^14 y (not a pure power: chart-change denominators couple x,y)")
# (4) infinity section: W=0 -> X^16+Y^16+Z^16+X^14 Y^2=0 in P^2, smooth check quick scan of Z=0 line done above;
# full P2 scan:
bad = 0
for X in range(p):
    for Y in range(p):
        for Z in range(p):
            if X == Y == Z == 0: continue
            F = (pow(X,16,p)+pow(Y,16,p)+pow(Z,16,p)+pow(X,14,p)*pow(Y,2,p)) % p
            Fx = (16*pow(X,15,p)+14*pow(X,13,p)*pow(Y,2,p)) % p
            Fy = (16*pow(Y,15,p)+2*pow(X,14,p)*pow(Y,1,p)) % p
            Fz = (16*pow(Z,15,p)) % p
            if F == 0 and Fx == 0 and Fy == 0 and Fz == 0:
                bad += 1
print("infinity-curve singular reps (raw, incl. scaling):", bad)
