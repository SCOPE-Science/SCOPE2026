# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Nonexistence of binary linear [48,12,18] by residual MacWilliams classification: closing the open 17-18 interval
- **Round:** 2026-09-07-first-light-01
- **Lane:** 123
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Coding Theory
- **Method:** Jaffe-style residual-code classification with MacWilliams/Krawtchouk integer feasibility and Griesmer shortening cascade

## Problem

Decide the live-open binary linear entry [48,12] (Grassl BKLC 17/18): prove there is no binary linear [48,12,18] code, so the optimal minimum distance is exactly d*(48,12)=17, by classifying the weight-18 residual family (length-30 codes in the assigned window) under MacWilliams/Krawtchouk integer feasibility and the Griesmer shortening cascade from Ub(29,11)=9.

## Attempted claim

There is no binary linear [48,12,18] code over GF(2); hence the optimal minimum distance at (n,k)=(48,12) is exactly 17, attained by the known Goppa-derived [48,12,17]. Proof route: for any putative [48,12,18], the residual with respect to a weight-18 codeword is a length-30 code whose parameters violate the Griesmer/shortening cascade chained to Ub(29,11)=9, and exact-rational MacWilliams/Krawtchouk integer feasibility eliminates every compatible weight enumerator for the parent and residual — a Jaffe-style residual classification, not a pure LP-dual bound.

## Research outcome

Partial theorem on the open BKLC [48,12] 17/18 entry: any putative binary [48,12,18] is pinned to length-30 residuals with 9<=d'<=10, weight-18 overlaps <=9, z<=4, and an exact moment system, with a validated stdlib residual-audit pipeline; second-order MacWilliams moments provably cannot close the case (exact order-2 feasible witness). Full nonexistence remains open.

## Why this attempt failed

Failed axes: originality, value.

originality: The proved content is a textbook instantiation at parameters (48,12,18), not the advertised new nonexistence theorem. Nearest priors substantively cover each item: (a) residual lemma with dim k-1 and distance >=ceil(d/2) — standard Hill / Huffman-Pless, cited in draft itself; (b) Griesmer bound G(k,d)=sum ceil(d/2^i) — standard; (c) Pless/MacWilliams moments B_j=M^-1 sum A_i K_j(i), B1=z — standard; (d) BKLC provenance Ub(48,12)=18 via one-step Griesmer from Ub(29,11)=9 Ja and Lb via Goppa-shortening — already on live [48,12] page, so item (1) reprints the table's own inference as a 'residual argument'; (e) Ub(30,11)=10 — already closed on live page. Items (2)-(5) are one-line corollaries obtained by substituting n=48,k=12,d=18 into (a)-(d). The only numerically new object, the rational order-2 witness, is a solution to 3 linear equations in 3 unknowns with support {18,24,30}; it is non-integral by construction and proves weakness (moments do not suffice), not a new constraint. No higher-order classification, no integral shortlist, no residual elimination is produced — draft explicitly states 'no exhaustive integer-enumerator classification is claimed' and 'gradient LP search inconclusive'. The empty arXiv phrase search for '[48,12,18]' supports absence of a full nonexistence proof (which is NOT supplied), but does not establish priority for elementary corollaries that follow mechanically from cited lemmas plus table lookups. Hence no substantively new mathematical object, gap closure, or method is contributed. value: Independently worth finding later? No. Draft states 'Full nonexistence of [48,12,18] remains open; this report closes nothing' and 'No complete MacWilliams-feasible enumerator shortlist is produced (topic fallback envisioned one); only the exact moment system + one order-2 feasible witness.' The envisioned fallback (complete feasible shortlist + infeasibility logs + verified [48,12,17] witness enumerator + reusable audit pipeline constraining the open entry) was not achieved: no shortlist, no elimination log, no [48,12,17] witness verification, pipeline validated only on textbook Hamming [7,4,3]. What remains is: a restated table bound, a residual interval [9,10] that any specialist derives immediately, elementary overlap/degeneracy arithmetic, a standard moment formula, and a rational non-solution demonstrating that order-2 moments fail — i.e. textbook restatement + mere parameter substitution + a negative witness. This falls squarely under reject categories (textbook restatements, parameter substitutions, unexplained/unmotivated enumerations) even though correct and narrowly new as numbers. No downstream cascade is advanced because nothing is eliminated.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Full nonexistence of binary linear [48,12,18] NOT proved; optimal distance d*(48,12) remains 17-or-18.', 'No complete MacWilliams-feasible enumerator shortlist produced; only the moment system plus one order-2 feasible witness.', 'Higher Krawtchouk constraints (j>=3) and full integrality unresolved; gradient LP search for full Delsarte feasibility inconclusive and unclaimed.', 'Residual stratum bounds depend on cited live-table values Ub(29,11)=9 (Jaffe, unpublished) and Ub(30,11)=10, used as…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
