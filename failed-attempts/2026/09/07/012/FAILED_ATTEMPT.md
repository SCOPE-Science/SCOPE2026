# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Doubly-sorted BH(6,3) with fixed third row [1,omega,1,omega^2,omega,omega^2]: certified completion-or-gap by exact cyclotomic backtracking
- **Round:** 2026-09-07-first-light-01
- **Lane:** 16
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Quantum Information
- **Method:** phase-pattern backtracking with defect-bound pruning and exact cyclotomic unitarity verification

## Problem

Let omega=exp(2*pi*i/3). Decide by certified exhaustive search whether there exists a dephased Butson matrix H in H(6,3) (entries in {1,omega,omega^2}, first row and column all 1, H*conj(H^T)=6I) with doubly-sorted 2-border R2=[1,1,omega,omega,omega^2,omega^2], C2=[1,1,omega,omega,omega^2,omega^2]^T, and fixed third row R3*=[1,omega,1,omega^2,omega,omega^2]. R3* is exactly orthogonal to R1,R2 (<R1,R3*>=<R2,R3*>=0 in Z[omega]). Enumerate all completions R4,R5,R6 with col1=1 and col2 per C2 border via exact cyclotomic backtracking with Haagerup/defect pruning; output either an explicit H with exact Gram check or a machine-checkable unsatisfiability (gap) log.

## Attempted claim

Either (A) exhibit an explicit dephased BH(6,3) matrix extending the R3* border with exact Z[omega] unitarity check and defect/Haagerup certificate of equivalence or inequivalence to the known Tao example, or (B) prove by exhaustive pruned search with replayable log that no such completion exists, establishing a certified non-existence gap for this bordered subfamily.

## Research outcome

Certified EXISTENCE verdict (claim A): explicit symmetric BH(6,3) extending the doubly-sorted 2-border plus R3*, with exact Gram, uniqueness-in-slice, defect-0/Haagerup-3 certificates proving inequivalence to Fourier and Tao-type profile. Search: 48 checks, milliseconds. All artifacts rerunnable in <1 min.

## Why this attempt failed

Failed axes: originality, value.

originality: No substantively new mathematical object or gap is established. The exhibited H is admitted by the draft (Sec.8: 'the matrix coincides (up to the bordered gauge) with the known Tao-type example') to be monomial-equivalent to the known isolated Tao/S6 BH(6,3) example listed in Tadej-Zyczkowski quant-ph/0607136 as the single BH(6,3) class. It shares the characteristic Tao profile: alphabet mu3, defect 0, Lambda subset mu3 size 3, symmetric diagonal-1 form. No new inequivalent Hadamard is claimed or proved; no explicit monomial map to a frozen published S6 array was built, so even catalog-equivalence is not machine-checked, only invariant-match + citation. Fourier-inequivalence (defect 0 vs 4, Lambda 3 vs 6) is not original: any mu3 matrix has Lambda subset mu3, while F6 contains zeta=exp(pi i/3) not in mu3, so inequivalence follows trivially from alphabet without frequency counts; defect 0 for Tao vs 4 for F6 is textbook literature recomputed with the same code. The only novelty asserted is 'first certified completion-or-gap verdict for this doubly-sorted R3* slice' — i.e., that one coordinate prefix extends with slice-local uniqueness. This is timestamp/failed-search reasoning, not substantive difference: it is a coordinate-dependent corollary of the known singleton classification (take Tao representative, sort to R2/C2, read off third-row orbit). Independent check shows R3* is one of 4 prefixes with [0,1] orthogonal to R1,R2 ([0,1,0,2,1,2],[0,1,0,2,2,1],[0,1,2,0,1,2],[0,1,2,0,2,1]) in the same R2-stabilizer orbit (swap cols 3<->4, 5<->6), and all 4 give identical outcome (1 R4, 2 ordered sols). Choosing R3* among them is arbitrary gauge choice, not a new equivalence class. A gap (which would be structural restriction beyond n-mod-3) was not found; existence of a Tao-equivalent completion was. Compared substantively to nearest priors — Tadej-Zyczkowski catalog (Tao/S6 + Fourier F6 + defect/equivalence), Bengtsson et al. MUB-6 bases, Szollosi/Karlsson continuous families (positive defect, transverse to Butson locus) — the candidate adds no inequivalent family, no new invariant, and no decided gap. Hence originality FAIL. value: Result is not independently worth finding later. The slice R3*=[1,w,1,w2,w,w2] is an arbitrary third-row pattern among 4 equivalent prefixes (9 total orthogonal to R1,R2 without col2 fixing), with no independent motivation for this pattern over its orbit-mates; all 4 extend identically, so no distinctive structural insight. Outcome (A) existence of a Tao-equivalent matrix provides no new quantum-design input (same monomial class gives same design up to relabeling/phases) and no structural gap (which would have restricted BH(6,3) beyond trivial divisibility); it is a re-expression of a known object in canonical border gauge. Enumeration is trivial (48 inner checks, 1e-4 s, pools 12) — not a reusable pruning benchmark; column pruning is noted redundant, defect/Haagerup are standard textbook verifications for Tao…

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Uniqueness is slice-local (fixed R3*), not a new global BH(6,3) classification. Tao identification rests on invariant match (defect 0, alphabet mu3, Lambda size 3) plus cited single-class catalog; no explicit machine-checked monomial map to a frozen published S6 array was built offline. Defect uses convention dim ker-(2n-1) (dephased null reported too). No floating point is used anywhere; ranks are exact over Q.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
