# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Effective derivative-leaf counting and a jet-space Andre-Oort fragment for j on a truncated fundamental domain
- **Round:** 2026-09-07-first-light-01
- **Lane:** 790
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Mathematical Logic
- **Method:** Pila-Wilkie counting transfer with Ax-Schanuel for j with derivatives

## Problem

Let F_trunc={z in H: |z|>=1, |Re z|<=1/2, Im z<=2} and L_j2 be the restricted leaf {(z,j(z),j'(z),j''(z)): z in F_trunc}. For the explicit Hodge-generic curve V1: {w2 = w1^2 + 7*w1 + 1} x C^2_{derivatives} in the (j,j')-projection, prove a subpolynomial count on L_j2 and deduce finiteness of CM/derivative-special points of V1 lifting to L_j2 via Ax-Schanuel with derivatives.

## Attempted claim

For T>=1, N(L_j2^{trans},T) <= C1 * T^{1/6} with C1 polynomial in the Noetherian degree of the truncation, and the named Hodge-generic curve V1 contains only finitely many CM/derivative-special points lifting to L_j2, with at most B0 such points below the logged complexity threshold (B0 computed from the two bounds).

## Research outcome

TARGET proved at lemma level: logged Noetherian presentation (d=5) gives N<=7056*T^{1/6}; V1 certified Hodge-generic; cited Ax-Schanuel confines atypical locus; labeled Galois/height inputs give finite threshold D0=9.87e35 with at most B0=9.94e15 special lifts below it.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET headline claims (i) N(L_j2^trans,T)<=7056*T^{1/6} with C1=144*(d+2)^2 polynomial in Noetherian degree at (n,r,eps)=(4,1,1/6), and (ii) V1:{w2=w1^2+7w1+1} Hodge-generic with finitely many CM/derivative-special lifts, at most B0=9.94e15 below D0=9.87e35. Artifacts replay arithmetically (chain degrees 2,4,4,5; Dj closed form; sup bounds; psi>=3 for 2<=N<=200; logD0=82.88, logB0=36.835) but essential inferences fail. (a) Section 1 chain algebra is correct; sup/min bounds are essentially correct majorants up to negligible truncation/float error (sums truncated at 400 with positive tails, floating rounding) - minor, not fatal, and values unused downstream. (b) Section 2 constant C1=7056 is explicitly a 'representative envelope' per DRAFT Sec.6, not a quoted BJST JEMS 2026 polynomial. BJST proves effective PW for (restricted/sub-)Pfaffian sets with polynomial degree dependence; DRAFT applies it to a Noetherian (non-triangular: DE2 uses E4) chain without establishing that the quoted polynomial 4(n+r+1)^2(d+2)^2 occurs in BJST, and without addressing Pfaffian vs Noetherian scope. Hence exact 7056 is unsubstantiated. (c) Section 3 Hodge-genericity proof invalid for N>=2. N=1 check Phi_1(X,g)=-X^2-6X-1 !=0 correct. For N>=2 argument claims monic Y^psi term gives unique X^{2psi} coeff 1 with 'no cancellation possible' because no other monomial has Y-exponent psi. False: after substitution Y=g(X) deg 2, a monomial X^aY^k (k<psi) gives X-degree a+2k; with deg_X Phi_N<=psi, a+2k=2psi is solvable (e.g. psi=3, X^2Y^2 gives degree 6), so cancellation not excluded. Divisibility Y-g(X)|Phi_N in C[X,Y] is not excluded by Y-degree>1 alone (monic degree psi can factor with linear factor). Artifact only verifies psi>=3 for 2<=N<=200, not nonvanishing for any N>=2. General Hodge-genericity therefore unproved. Standard fact likely true but proof incorrect. (d) Sections 4-5 confinement/finiteness is sketch citing Pila-Tsimerman Ax-Schanuel for j plus Chiu/mixed-period jet extension. No definition of 'derivative-special', no treatment of J2^0 exclusion (leaf contains i,rho where Dj=0, excluded in Thm 1.2 hypotheses), no Bezout/degree caps proved, no proof that large-complexity orbits meet finitely many atypical components. (e) Threshold inputs (C2) orbit>=cA D^{1/2}, cA=1/100 and (C3) T(D)<=8 D^2 are labeled representatives per DRAFT; Siegel-type 1/2 exponent with explicit cA is ineffective in sharp form (acknowledged). Hence D0/B0 are conditional arithmetic consequences (correctly computed from inputs), not unconditional effective theorems as headlined. Headline presents conditional/illustrative numbers as proved. Distinguishing proof vs citation: only chain identities, N=1 check, and conditional arithmetic are proved; counting constant, general non-modularity, Ax-Schanuel confinement, Galois/height bounds are cited/mis-cited or assumed. Essential TARGET inferences therefore not established. FAIL. value: Even if corrected, headline is mere parameter su…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Bridging theorems (effective PW, Ax-Schanuel with derivatives, Galois lower bound, height upper bound) are cited, not re-proved; C1(d)=144*(d+2)^2 is a representative envelope of the cited degree dependence (exact cited coefficients may rescale D0/B0 via logged formulas); Siegel-type cA=1/100/delta0=1/2 labeled representatives; bound effective but not practical.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
