# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Heegner-hypothesis obstruction for the Gross-Zagier test case (15a1, Q(sqrt(-23)))

## 1. Objects
E/Q: 15a1, y^2+xy+y = x^3+x^2-10x-10, conductor 15=3*5.
K = Q(sqrt(-23)), discriminant -23. Prime p=13.

## 2. Proven statements
(a) Gate. a_13 = -2 (Legendre-symbol sum, cross-checked by brute-force affine
enumeration: 15 affine points, so #E(F_13)=16, a=13+1-16=-2); hence good
ordinary at 13 (a_13 mod 13 = 11 != 0). Kronecker(-23,p): p=3 gives 1=1^2
(split); p=5 gives 2, a non-residue mod 5 (inert); p=13 gives 3=4^2 (split).
Mod-13 irreducibility: Frob_2 has charpoly X^2+X+2 with discriminant -7=6
mod 13, and 6 is not in {0,1,3,4,9,10,12}, so the polynomial is irreducible
mod 13. Invariants: c4=481 (coprime to 15), Delta=50625=3^4*5^4, so
semistable. Singular loci: (2,0) mod 3, (3,3) mod 5; tangent-cone
discriminants 2 mod 3 (non-residue: nonsplit I_4) and 1 mod 5 (residue:
split I_1).
(b) Root number. W_inf=-1, W_3=+1 (nonsplit), W_5=-1 (split), so W(E/Q)=+1.
The twist discriminant -23 is coprime to 15; chi(-15)=chi(-1)chi(3)chi(5)
=(-1)(+1)(-1)=+1, so the twist has W=+1 and W(E/K)=+1, i.e. r=(1-w)/2=0.
(c) No classical conductor-1 Heegner datum. Since 5 is inert, 5O_K is prime
of norm 25; every O_K-ideal norm has even 5-adic valuation, so no ideal of
norm 15 exists. A conductor-1 Heegner datum on X_0(15) requires such an
ideal; hence none exists over K. Exhaustive norm-equation search
(u^2+23v^2)/4 in {3,5,15} is empty, and a (1,w)-basis K-grid search with
|coords|<=6 in exact arithmetic finds only known rational torsion points.
(d) Consequence. The TARGET's classical ratio L^{(r)}(E/K,1)/h(P) with finite
R cannot be formed: P does not exist classically, and r=0 would in any case
force any Heegner point to be torsion with h(P)=0. This is a structural
obstruction, not a gate failure and not a full Gross-Zagier disproof (a
generalized Shimura-curve analogue is not excluded here).

## 3. What is heuristic vs proved
Proved (exact integer arithmetic): everything in (a)-(c) above; scripts
output/artifacts/gate_exact.py and output/artifacts/recovery_test.py with
logs gate_exact.log and recovery_test.log. Heuristic only: Dokchitser-type
values L(E,1)~0.3501507605831505, L(twist,1)~0.6656790232819436, product
~0.2330880163064213 (script output/artifacts/Lvals_doc.py, log
Lvals_doc.log), recorded as consistency evidence, not used for any proved
clause. No rigorous L-interval or certified height is claimed.

## 4. Reproduction
Run: python3 output/artifacts/gate_exact.py; python3
output/artifacts/recovery_test.py; python3 output/artifacts/Lvals_doc.py.
All proofs use only integer/Fraction arithmetic except the explicitly
labeled heuristic L-script (mpmath).
