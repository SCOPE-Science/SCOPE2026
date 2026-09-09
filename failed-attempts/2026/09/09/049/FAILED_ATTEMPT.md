# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Asymptotic unconditional-constant growth in every block subspace of the Gowers-Maurey HI space via uniform norming-set control
- **Round:** 2026-09-07-first-light-01
- **Lane:** 400
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Functional Analysis
- **Method:** Gowers-Maurey hereditarily-indecomposable construction with rapidly increasing sequences and dependent-sequence norm estimates

## Problem

Let X_GM be the Gowers-Maurey hereditarily indecomposable space with f(t)=log2(t+1), sparse coding set J, and norming set D. Does every infinite-dimensional block subspace Y of X_GM contain, for each n, a normalized successive n-block forming a dependently-coded RIS whose unconditional constant satisfies K_n >= (1/4)*f(n)^{1/2}, via uniform control over all of D at each coding level?

## Attempted claim

For X_GM as above, every infinite-dimensional block subspace Y contains for each positive integer n a normalized successive n-block (x_1,...,x_n) forming a dependently-coded RIS such that its unconditional constant satisfies K(x_1,...,x_n) >= (1/4)*f(n)^{1/2} with f(n)=log2(n+1), certified at each coding level by uniform estimates over all of D (three-case weight analysis) together with the associated special functionals.

## Research outcome

Target assessed non-viable as stated: GM92 index parity (min J in L\K, specials only for K-lengths) makes every-n dependent coding and the min-J paired special ill-posed; quantitative repairs fail via 25/9-window and sqrt(F)/n-violation. Consolidated emergent finding with sharp repair along K (1/3)f^1/2, k>=10 sharp) and 5 replay-OK stdlib verifiers.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Index parity core (Thms 1-2, Lemma floor) verified correct against GM92 HTML Sec.3: J={j1,j2,...}, K={j2,j4,...}, L={j1,j3,...}, D_N''=union_{k in K} B_k(D_N), implicit norm sup over k in K only; hence j*=j1 has odd J-index, j1 in L\K, no length-j1 special enters D/norm. j1>=2^36-1 from f(j1)>=36 correct; j2>>2^144-1 from logloglog gap correct (2*j1~=1.37e11 vs lnlnln(2^144)~1.53). Ratio algebra (k-2)/(2.4k)>=1/3 iff k>=10 correct but vacuous for actual K (all >>2^144). HOWEVER headline part (2) fails: Thm 3 prefix-window claim 'ratio >=(1/4)sqrt(f(n)) requires f(k)/f(n)<=25/9' omits the (k-2)/n factor. Correct condition from the stated bounds is sqrt(Fk/Fn)<=(k-2)/(0.6n), i.e. Fk/Fn<=[(k-2)/(0.6n)]^2. For k>>n (the K-gap regime) RHS is astronomically large (quadratic in k dominates log k), so the condition is SATISFIED not violated; the draft's 'k+1<=(n+1)^2.78' bound and 'violated across gaps' conclusion are reversed. Artifact B5 only checks same-length case (4/2.4)^2 and does not verify cross-length claim. Thm 4 chunk lower bound ||v||>=(s/2-2)/sqrt(F) asserts without proof existence of a 'valid length-k special continuing the first chunk's functionals' with k^-2 cross terms for arbitrary continuation (sigma fixes M_{s+1} but choice/validity/RIS-cross bounds for j>s not proved), and compares ||v|| (k-vector object, scale s/sqrt(F)) against a 'hoped' 1.2n/f(n) bound that is never shown to be needed by any repair (strawman: chunks y_j are not normalized RIS vectors, so Lemma-5 n-scale upper does not apply to v). Stand-in integers (1000/200/1e9 etc.) are explicitly illustrative, not J/K values, so no quantitative violation about the actual construction is proved. Thm 5 repair proof sketches GM HI verbatim but does not verify Lemma-7 [log N,exp N] coverage for each M_i step nor the a_i=(-1)^i unconditional-constant direction; scripts verify only algebra (thresholds, e-cert, tail=1, cross=1/n), not norm estimates. Hence not every essential inference is proved; proof vs arithmetic-demo conflated. originality: Nearest priors checked substantively: GM92 math/9205204 (HTML Secs.1-3 full text) defines K/L/D''/implicit norm and proves the HI estimate with (k/2-1)/sqrt(f(k)) lower and Lemma-5 upper yielding (1/3)f(k)^{1/2} ratio (draft Sec.5 admits Thm 5 is 'Gowers-Maurey's own' with only scope-correction/sharp-boundary audit); Schlumprecht S-space Lemmas 1-5 are background RIS machinery; Argyros-Haydon 0903.3921 is a different HI object (l1-dual scalar-plus-compact). The index fact 'no length-j1 special / dependent lengths only in K' is a one-step definitional read-off from GM's stated 'lengths in K' plus j1 odd-index -- mechanically implied by the prior definitions, not a substantive new theorem (no prior states the negative corollary only because it is immediate). The repaired (1/3)f^{1/2} law along K is prior art. The only candidates for novelty (25/9-window, sqrt(F)/n-violation) are not in priors but are mathematically incorrect/incompl…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Obstruction theorems concern the 1992/1993 X_GM construction as published; other HI constructions may differ. No claim is made about non-dependent every-n rates (left open). Theorem-5 repair is a corrected-scope re-derivation of GM's estimate, not a new growth law. Stand-in integers in Sec.3 scaling demos are illustrative only; all J/K theorems use only the published gap condition.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
