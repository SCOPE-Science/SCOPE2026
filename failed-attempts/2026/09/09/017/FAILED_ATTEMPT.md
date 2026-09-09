# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Twist-ray chirality persistence along the 8_19 pretzel ray: proved Jones-span, determinant, and signature recurrences
- **Round:** 2026-09-07-first-light-01
- **Lane:** 314
- **Disposition:** NO_RESULT
- **Domain:** Knot Theory
- **Method:** Kauffman-bracket skein recurrence with Seifert-matrix block induction

## Problem

Fix the pretzel twist ray D_m=P(3,3,-(2+m)) for m>=0 (D_0=8_19=T(4,3), crossings 8+m) by a committed twist-insertion rule on DT codes. Prove by Kauffman-bracket skein recurrence and Seifert-matrix block induction closed-form recurrences for Jones span, determinant, and Murasugi signature along the ray, deduce uniform chirality of all D_m (nonzero signature plus Jones asymmetry persisting), and verify D_0..D_6 by independent replay from the committed codes.

## Attempted claim

For D_m=P(3,3,-(2+m)), m>=0: (a) Jones span grows as span(V(D_m))=5+m with explicit leading/trailing coefficient rule from the skein recurrence; (b) det(D_m) satisfies a fixed linear recurrence with stated initial values det(D_0)=3; (c) sig(D_m)=6+2m (or the proved exact linear form) via a Seifert block-matrix step; hence every D_m is chiral, certified uniformly by nonzero signature and non-palindromic Jones, with D_0..D_6 replay-verified from committed DT codes.

## Research outcome

Post-disconnect lane: validated a stdlib-only Kauffman-bracket engine four ways (KnotAtlas 8_19 PD exact bracket {-8:-1,4:1,12:1}, det 3; T(3,4) braid mirror; trefoil s1^3; DT2PD mirror; true-kink -A^-3), proved a planarity/validity criterion for twist insertion (cross-connect is planar, straight-through is non-planar/virtual, via mod-4 uniformity + flip tests with impossible-det counterexamples det^2=45/17), ran a full 10395-pairing closure census (pure-ring closures never give det 3; ring family is P(3,3,+(2+m)) with dets 21+6m), and tabulated valid twist extensions (single cross-inserts give 2-links det 6/4; double cross-inserts give knots det 9/5). The P(3,3,-(2+m)) ray lemma, recurrences, signatures, and D_0..D_6 replay were NOT achieved; honest NO_RESULT with auditable artifacts in output/artifacts/results.json plus scripts.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No Murasugi signature was independently computed (no Seifert/Goeritz implementation built); sig=6 for D_0 is cited from live KnotAtlas only.', 'No Jones-span/determinant/signature recurrences proved and no uniform chirality persistence deduced; the ray lemma did not close.', 'No consecutive-m (8+m crossing) ray diagrams constructed: +1 twist extension flips twist-region parity and fixed-bridge surgery yields links (det 6/4) or non-planar wirings; global re-embedding not achieved in budget.', 'Extension knots (R2a-double det 9, R2b-double det 5) lack knot IDs and signatures; their Jones polynomials were not normalized/identified.', 'The mod-4 uniformity validity criterion is folk-level reasoning, not claimed as original.', 'Above-11-crossing exact values for D_1..D_6 were not produced; fallback not met.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No Murasugi signature was independently computed (no Seifert/Goeritz implementation built); sig=6 for D_0 is cited from live KnotAtlas only.', 'No Jones-span/determinant/signature recurrences proved and no uniform chirality persistence deduced; the ray lemma did not close.', 'No consecutive-m (8+m crossing) ray diagrams constructed: +1 twist extension flips twist-region parity and fixed-bridge surgery yields links (det 6/4) or non-planar wirings; global re-embedding not achieved in budget.',…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
