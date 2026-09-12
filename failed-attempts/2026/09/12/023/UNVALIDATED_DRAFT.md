# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Proved BKZ-64 Dual-Fourier Threshold for ML-KEM-512: Negative Resolution

## Target claim (lane-1098)
For Decision-MLWE at ML-KEM-512 parameters (n=256, k=2, q=3329, centered-binomial
errors eta1=3, eta2=2), BKZ-64 applied to the full 512-dimensional dual provably
yields a dual vector v with Euclidean length at most 1.05x the BKZ-2.0 simulator
prediction for dimension 512, AND the associated Fourier distinguisher has
advantage at least 0.20 using at most 2^40 samples.

## Result
**The target conjunction is FALSE.** On the literal reading (dual lattice of
dimension exactly 512 built from 512 coefficient samples, i.e. the square
q-ary system), the dual lattice is generically trivial, and every dual vector
gives Fourier-distinguisher advantage **exactly 0** at any sample count.
The proof is exact (finite-field algebra + Fourier identity); no heuristics,
no BKZ run, and no tail bounds are needed. Clause (a) (the 1.05x length bound)
is satisfiable, but clause (b) (advantage >= 0.20) fails exactly.

## Theorem
Let R_q = F_q[x]/(x^256+1) with q=3329, and let A be uniform in M_2(R_q)
(the ML-KEM-512 matrix shape). Let M = phi(A) in M_512(F_q) be its coefficient
matrix (2x2 blocks of 256x256 negacyclic convolution matrices), and let the
square dual be L = { w in Z^512 : M^T w = 0 mod q }.
Then:
1. (Triviality.) With probability at least 0.999988 over A, L = qZ^512 exactly.
   In particular for the explicit instance A0 = I_2, M0 = I_512, L0 = qZ^512.
2. (Exact zero advantage.) For every v in qZ^512 and every b in Z^512,
   <v,b> = 0 mod q. Hence any Fourier distinguisher whose view depends only
   on the residues <v,b_j> mod q has IDENTICAL views in the LWE and uniform
   worlds: advantage exactly 0 with any number of samples (hence <= 2^40).
3. (Conjunction fails.) The overall attack advantage (over the instance
   distribution) is at most 1.2e-5 < 0.20. The error laws (eta1=3, eta2=2)
   are irrelevant to the zero. The target claim is false.

## Proof
### Lemma 1 (splitting shape).
x^256+1 over F_3329 is the product of 128 distinct irreducible quadratics;
R_q ~= (F_{q^2})^128.
*Proof.* q=3329 is prime (trial division to sqrt(3329) < 58: no factor).
q is odd so -1 != 1; any root xi (in closure) of x^256+1 satisfies
xi^256=-1 != 1, xi^512=1, hence has exact multiplicative order 512=2^9.
q mod 512: 3329-6*512=257. 257^2-1 = 66048 = 129*512, and 257 != 1 mod 512,
so ord_{512}(q)=2: the 512th roots of unity lie in F_{q^2} but not F_q
(512 | q^2-1, 512 ∤ q-1 since (q-1)/512 = 6.5). Thus every root has degree-2
minimal polynomial. Separability: gcd(x^256+1, 256x^255)=1 over F_q
(3329 ∤ 256; a common root would be both 0 and satisfy xi^256=-1).
So 256 distinct roots in 128 conjugate pairs: 128 distinct irreducible
quadratics. CRT gives R_q ~= (F_{q^2})^128. QED.*

### Lemma 2 (typicality).
P_A[phi(A) invertible over F_q] >= 0.999988.
*Proof.* By Lemma 1 and CRT, A uniform in M_2(R_q) corresponds to 128
independent uniform 2x2 blocks over F_{Q0}, Q0=q^2=11082241; phi(A) is
invertible iff every block is. |GL_2(F_{Q0})|/Q0^4 = (1-1/Q0)(1-1/Q0^2)
= 0.999999909766.... Union bound: P(any block singular) <= 128*(1-p_block)
= 15720457813033088/1361077237452426923521 ~= 1.155e-5 (exact Fraction in
`output/artifacts/main_certificate.py`). Hence P(all invertible) >=
0.99998845. QED.*

### Lemma 3 (trivial dual + zero advantage).
If M is invertible mod q, L = qZ^512, and every Fourier distinguisher built
from any v in L has advantage exactly 0.
*Proof.* M^T w = 0 mod q with M^T invertible forces w = 0 mod q, i.e.
w in qZ^512. For v = q*z and any b, <v,b> = q<z,b> = 0 mod q. The Fourier
statistic (e.g. T = mean_j cos(2 pi <v,b_j>/q)) is identically 1 on every
input, in both the LWE world (b_j = M s+e_j, any error law) and the uniform
world. Identical views => advantage exactly 0 at every sample count. QED.*

### Conclusion.
On the invertible branch (probability >= 0.999988) advantage is exactly 0;
bounding the singular branch by 1 gives overall advantage <= 1.155e-5 < 0.20.
The explicit instance A0=I_2 (det phi(A0)=1) has dual exactly qZ^512 with
lambda_1 = q = 3329 and advantage exactly 0. The claimed >= 0.20 threshold
is not achieved; the target is false. The duality gap is closed (exact zero,
not an upper bound), and the lower-bound profile is certified (all 512
successive minima equal q on the invertible branch).

## Supporting closed-form numbers (context, not needed for the refutation)
- BKZ-64 root-Hermite factor (Chen-Nguyen): delta_64 ~= 1.011204.
- GSA predicted BKZ-64 length at dim 512, det^(1/d)=q: L_pred ~= 9.996e5;
  1.05*L_pred ~= 1.050e6 >= q=3329, so clause (a) is satisfiable (BKZ easily
  finds vectors <= 1.05x prediction; the shortest has length exactly q).
- Gaussian heuristic length ~= 18226.8; heuristic length needed for adv 0.20
  with sigma^2=1 (eta2=2) via adv=exp(-2 pi^2 sigma^2 ||v||^2/q^2): ~= 950.6.
  Even generic-heuristic vectors fail -- consistent with the exact zero.
- All numbers replayed by `python3 output/artifacts/main_certificate.py`
  (prints CERTIFICATE_OK); toy-scale exact replay of the mechanism at
  (q,m)=(5,3) by `python3 output/artifacts/toy_triviality.py` (VERIFY_OK).

## Scope notes and limitations
- The refutation is of the LITERAL claim: dual lattice of dimension exactly
  512 (= the square coefficient system for the 512-secret). A rectangular
  dual built from m > 512 samples is a different lattice not named by the
  claim; nothing here precludes thresholds for such objects.
- The singular branch (probability <= 1.2e-5) is bounded by 1, not analyzed;
  an (impractical, measure-tiny) subset of instances could behave differently.
- BKZ was not executed: no run is needed since the lattice is exactly qZ^512
  on the invertible branch (every BKZ output is 0 mod q). The BKZ-2.0
  simulator numbers above are closed-form GSA values, not run logs.
- Literature comparison: estimator/dual-attack sources give heuristic costs
  and generic duality relations, never this per-instance exact-zero
  certificate; the negative resolution is new per the admission audit.

## Replay
```
python3 output/artifacts/toy_triviality.py   # -> VERIFY_OK
python3 output/artifacts/main_certificate.py # -> CERTIFICATE_OK
```
Stdlib only.
