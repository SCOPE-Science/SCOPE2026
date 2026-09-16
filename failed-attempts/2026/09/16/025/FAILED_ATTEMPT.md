# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp O(n^2) extremal refinement for the single tight 7-cycle
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20461
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Extremal Combinatorics
- **Method:** flag-algebra and stability analysis

## Problem

Let C^3_7 be the 3-uniform tight 7-cycle on {1,...,7} with edges all 7 consecutive triples cyclically. Let brec(n) be the maximum number of edges in an n-vertex B_rec-construction (empty for n<=2; for n>=3, from a partition V1 union V2 as B[V1,V2] union H[V2] with B[V1,V2]={e:|e cap V1|=2} and H[V2] a B_rec-construction). Does there exist an absolute constant C such that for all n, ex(n,C^3_7) <= brec(n)+C*n^2, and is this order best possible?

## Attempted claim

Let C^3_7 be the 3-uniform tight 7-cycle on {1,...,7} with edges all 7 consecutive triples cyclically. Let brec(n) be the maximum number of edges in an n-vertex B_rec-construction (empty for n<=2; for n>=3, from a partition V1 union V2 as B[V1,V2] union H[V2] with B[V1,V2]={e:|e cap V1|=2} and H[V2] a B_rec-construction). Does there exist an absolute constant C such that for all n, ex(n,C^3_7) <= brec(n)+C*n^2, and is this order best possible?

## Research outcome

Proved order-sharpness for the tight-7-cycle extremal problem: a one-vertex W-star extension of B_rec is C_7-free with Theta(n^2) surplus (constant ~0.0269), so any O(n^2)-envelope upper bound is best possible in order.

## Why this attempt failed

Failed axes: originality, value.

originality: The order-level emergent claim ex(n,C^3_7)>=brec(n)+Omega(n^2), ruling out o(n^2), is already explicitly recorded in Bodnar-Leon-Liu-Pikhurko (2025) Introduction for all ell>=7 with ell=1 mod 3, which includes ell=7: v* in V1 plus all triples {v*,y1,y2} with y1,y2 in V2,2 is stated C-free with brec+Omega(n^2). The submitted W-star (x0 plus pairs from W=V2,1) is the same single-vertex-star template with the second-level part swapped (V2,1 vs V2,2); it does not create a new boundary and its order corollary is substantively implied by the prior Omega(n^2) remark. The report's 'first explicit Theta(n^2) family' is therefore materially false. value: Order-sharpness for C^3_7 was already settled at order level by the prior V2,2-star Omega(n^2); the residual novelty is a larger lower-order constant (~0.0269 vs implicit ~0.009) within the same single-vertex-star idea. Since brec is Theta(n^3) and Turan density is unaffected, this is a numerically small lower-order constant gain with no demonstrated density, classification, benchmark, or downstream significance, i.e. a parameter substitution / tiny unmotivated gain under STANDARD. It does not independently advance the recognized question and the admitted upper-bound half remains open.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The admitted target's upper-bound half (ex(n,C^3_7) <= brec(n)+C*n^2 for an absolute C and all n) is NOT proved here and no upper-bound constant is asserted; WORKLOG sections 3 and 6 record only a credible skeleton (envelope contraction, rigidity template, small-n cover evidence). The surplus constant ~0.0269 is proved as a limit/lower constant, not claimed optimal (deeper-level iteration already adds more). Literature originality rests on two capped search calls plus self-contained proof, not…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
