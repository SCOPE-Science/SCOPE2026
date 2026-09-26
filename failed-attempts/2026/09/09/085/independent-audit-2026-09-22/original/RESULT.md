# Nonzero torsion in M^6 tensor M^7 over the E7 Kleinian surface singularity

## Context
Let R_E7 = C[[x,y,z]]/(x^2+y^3+y z^3) be the E7 Kleinian (ADE) surface
singularity, a 2-dimensional complete local CM domain. Finitely generated
maximal Cohen-Macaulay (MCM) modules over R_E7 correspond via Eisenbud's
equivalence to matrix factorizations of the defining equation, and are
classified by the E7 Dynkin diagram (finite CM type). Whether tensor products
of MCM modules remain MCM (torsion-free) is the recognized MCM-tensor /
Tor-rigidity boundary question (Auslander-Lichtenbaum, Huneke-Wiegand;
Celikbas-Sadeghi arXiv:1712.03663 Q1.1, Conj. 1.2-1.3, open even for isolated
singularities), with downstream use for NCCR tensor-closure, McKay tensor
products, and homological-mirror reuse. Published E7 tables (Omer
arXiv:1602.00788 Sec. 4.4; Yoshino) list only single indecomposable matrix
factorizations, and general theorems prove only a dim-vs-codim criterion,
deciding no explicit E7 pair.

## Definitions
Work first over k = QQ with f_O = -y^2+x^3+x z^3 in k[x,y,z] and
R_O = k[x,y,z]/(f_O), Omer's E7 equation. Input matrix factorizations
(transcribed as inputs from Omer Sec. 4.4):
S6 = [[0,0,x^2,xz],[0,0,z^2,-x],[x,xz,0,0],[z^2,-x^2,0,0]],
Phi6 = S6 - y I4, Psi6 = S6 + y I4, M6 = coker(Phi6);
S7 = [[0,z^3+x^2],[x,0]], Phi7 = S7 - y I2, Psi7 = S7 + y I2,
M7 = coker(Phi7).
Over CC, (x_T,y_T,z_T) = (i y_O, x_O, z_O) gives
(i y)^2+x^3+x z^3 = -y^2+x^3+x z^3 = f_O, i.e. an isomorphism between
Omer's equation and the topic equation x^2+y^3+y z^3; everything below
transfers along it and passes to C[[x,y,z]] by flat base change/completion.
The tensor product T = M6 tensor_R M7 = coker(Q) has the logged 8x16
Kronecker presentation Q with row r = 2i+a (i in 0..3, a in 0..1):
A-block columns 2j+a carry Phi6[i,j], B-block columns 8+2i+b carry
Phi7[a,b], else 0 (explicit nonzero entries listed in DRAFT; every entry
lies in (x,y,z), so Q(0) = 0).

## Result
For the two named adjacent-node indecomposable MCM modules M6 (rank 2) and
M7 (rank 1) over the E7 singularity, T = M6 tensor M7 has nonzero torsion,
witnessed by an explicit element with annihilator (x), a nonzero nonunit
nonzerodivisor; hence T is not maximal Cohen-Macaulay. A second independent
witness is also given.

## Proof / evidence
MF identities (machine-checked): Phi6 Psi6 = f I4, Phi7 Psi7 = f I2,
det(Phi6) = f^2, det(Phi7) = -f. Ranks over Frac(R): all 16 3x3 minors of
Phi6 are 0 or divisible by f, while the 2x2 minor on rows (2,3), cols (0,1)
equals -x^3-x z^3, and minor+y^2 = -f, i.e. equals -y^2 != 0 in R; hence
rank(Phi6) = 2 and rk(M6) = 2 (same for Psi6); Phi7 has nonzero entry x and
det 0 in R, so rk(M7) = 1.
Torsion: let v = (0,0,0,1,-z,0,x,0) and c = -e_2+e_10. Exactly over
QQ[x,y,z], Q c = x v (all 8 rows, zero remainder; row check: col 2
contributes -Phi6[i,1] on even rows, col 10 contributes Phi7[a,0] on rows
(1,a); sum = (0,0,0,x,-xz,0,x^2,0) = x v). So x [v] = 0 in T.
[v] != 0: if v = Q c' + f s' then evaluating at (0,0,0) gives
0 = v(0) = (0,0,0,1,0,0,0,0) since Q(0) = 0 and f(0) = 0, contradiction;
this evaluation argument is complete with no degree bound
(a bounded 672x480 rational inconsistency certificate for deg <= 3 is also
computed). R is a domain: f = -(y^2-g), g = x^3+x z^3, monic quadratic in y
over the domain QQ[x,z]; g = x(x^2+z^3) has x-adic valuation 1 (odd), hence
is not a square, so f is irreducible; x is a nonzero (x(0)=0, so nonunit)
nonzerodivisor. Thus [v] is nonzero torsion with annihilator (x).
Second witness: w = (-z,0,1,0,0,0,0,1), Q(-e_6+e_14) = x w exactly,
w(0) = (0,0,1,0,0,0,0,1) != 0, same conclusion.
Non-MCM: R (resp. completion) is a 2-dim CM domain; T is nonzero finite of
generic rank rk(M6)rk(M7) = 2 (witnessed by a 6x6 minor of Q with
determinant not divisible by f, remainder -x^2 y^4 z^2). Associated primes
of an MCM module over a CM ring are minimal; over a domain the only minimal
prime is (0), so every nonzero r would be T-regular. Since x != 0 kills
[v] != 0, T is not MCM. AR comparison (tau(M6) = coker(Psi6), rank 2
nonfree; middle-term rank equation 2+2 = 3+1) is logged only; no claim that
AR shape forces torsion.

## Limitations
Computation is over QQ[x,y,z]/(f_O), transferred to the topic equation and
completion via the logged linear isomorphism and flat base change;
evaluation/irreducibility arguments repeat verbatim (over C[[..]],
f_T = x^2+h with h = y(y^2+z^3) is irreducible by the same valuation
argument, so the completion is a domain). Indecomposability and Dynkin
labelling are cited from Omer/Yoshino as inputs, not re-proved. The full
target's Knorrer-lift torsion-transfer lemma to R[u,v]/(f+uv) is NOT
established; only the torsion core (exact preset-fallback criterion) is
claimed.

## Reproducibility
`python3 output/artifacts/verify.py` (stdlib + sympy only) prints VERIFY_OK.
It replays: MF identities and determinants; divisibility of all 3x3 minors
of Phi6 by f and the 2x2 minor identity; Q(0) = 0; exact relation
Q c = x v with v(0) != 0; bounded non-membership inconsistency
(672x480 system); domain/nonzerodivisor facts; 6x6 Frac-rank minor with
remainder -x^2 y^4 z^2.

## References
- H. Omer, Matrix Factorizations for Local F-Theory Models,
  arXiv:1602.00788 (single E7 factorizations S1..S7, quiver; inputs only).
- I. Burban, Y. Drozd, Maximal Cohen-Macaulay modules over surface
  singularities, arXiv:0803.0117 (MF equivalence, AR, McKay background).
- O. Celikbas, A. Sadeghi, Maximal Cohen-Macaulay tensor products,
  arXiv:1712.03663 (MCM-tensor question, general dim-vs-codim criterion;
  decides no E7 pair).
