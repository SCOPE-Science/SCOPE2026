# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Extremal Salem braid-word witness forcing sharpness in the punctured-torus face
- **Round:** 2026-09-07-first-light-01
- **Lane:** 763
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Low-Dimensional Topology
- **Method:** Nielsen-Thurston train-track Perron-Frobenius dilatation with Teichmuller-polynomial cross-check

## Problem

Exhibit and certify an extremal low-dilatation 3-braid word w* in the named punctured-torus-bundle face: prove w* is pseudo-Anosov, compute its dilatation exactly as the largest root lambda(w*) ~= 1.401 of the explicit degree-6 Salem polynomial to be logged, and prove w* represents a fibered class forcing sharpness of the neighboring face gap.

## Attempted claim

w* is pseudo-Anosov with dilatation lambda(w*) equal to the largest root of the logged Salem polynomial (approx 1.401), the root is a Salem number, and w* is the monodromy of the minimal-entropy fiber in the named face, so the face gap (topics 1-2) is sharp up to the stated tolerance.

## Research outcome

Target refuted exactly: w* is pseudo-Anosov but with dilatation 10+3*sqrt(11) in (19.948,19.951) (quadratic Pisot), not ~1.401 degree-6 Salem; 23/23 replay checks pass.

## Why this attempt failed

Failed axes: value.

value: TARGET route: admitted target required w* pseudo-Anosov with ~1.401 degree-6 Salem dilatation and face-minimal sharpness. Submission proves the opposite for the literal core (19.95 quadratic Pisot) and concedes clause (d) unauditable (no face name, no polynomial, no tolerance, no M_s/marking). The remaining exact invariant (trace 20 / 10+3*sqrt(11)) is a textbook SL(2,Z) multiplication on a failed low-dilatation candidate. Under the exact-invariant rule, a narrow datum is valuable only when object+invariant were motivated before computation, value not mechanically implied, and future work could need the precise fact. Here motivation (low Salem face-sharp anchor, Lehmer adjacency, entropy-rigidity citation) attaches to the claimed 1.401 Salem value, not to the actual 19.95 Pisot value which has no sharpness/Lehmer/downstream use; DRAFT cites no future use for 19.95. The value is mechanically implied by 2x2 integer multiplication. The only reusable part (D3 minimum >=2.618, quadratic-only) is already-published textbook (Lanneau-Thiffeault/Hironaka-Kin) and correctly presented as obstruction, not as new citable advance. This is a correct disproof of an ad-hoc false target, not an independently retrievable extremal witness, template, or gap theorem. No bounded addition (identity, literature position, interpretation) without changing the object or starting a new direction can make this arbitrary large-dilatation word independently worth finding later. Intrinsic low value / arbitrary scope after refutation. Hence value FAILS and, per policy, requires REJECT not REPAIRABLE.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Refutation covers the literal word-to-dilatation core; inputs name no face/polynomial/tolerance so clause (d) is unauditable as stated; higher-genus re-reading untestable from the word alone with no M_s/marking data; integer-arithmetic proof only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
