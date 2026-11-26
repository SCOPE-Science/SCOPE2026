---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The labeled specialization t=-1 is exactly the eight-factor product, up to units. An independent finite-field replay found eight zero triple determinants in the quadratic integral model and norm one for the other 48; the zero triples share no pair and all reduced lines are distinct. This gives eight ordinary triples and four nodes in both characteristics. The local Tjurina length at a triple is four even in characteristic three: after a linear change and removing a unit take f=uv(u-v), and with w=u+v the Tjurina ideal is (uw,w²,u³), with basis 1,u,w,u². The node has length one. The replay reconstructed the cubic and quintic syzygies and primitive relation, dimensions [0,0,0,1,3,8] through coefficient degree five, all nine stated grevlex leaders and the exact all-degree numerator 1-3T^7+T^10+2T^12-T^13. The exhibited relation spans the relation module over the fraction field because U and B are independent; primitivity and unique factorization force polynomial multiples over S. The submodule presentation has the full Hilbert numerator, so its graded quotient in the full syzygy module vanishes; all differentials have positive-degree entries, giving minimality. Flat field extension preserves the result and minimality. The complex comparator follows from the cited nearly-free exponents (4,4) in Proposition 2.1 combined with Theorem 1.6, and its numerator is 1-3T^7+3T^11-T^12. Their difference is T^10(1-T)^3, so dimensions are 37 and 36 in degree ten and equal elsewhere. Supplied verify.py was inspected, not executed. Separate replay: branches/3201ff35-2dcd-45cd-be5c-f76b4ce78a4c/replay.py and replay.log. The calculation concerns only this model and the unsaturated homogeneous quotient.

## originality

FAIL

The stated characteristic-three minimal resolution, not merely its nonfreeness or low-degree Frobenius syzygy, is mechanically implied by existing finite-field freeness and free-deletion theorems. Adjoining z=0 covers all F3 points, and deleting it leaves a nonfree arrangement with a three-line restriction. Yoshinaga and Abe therefore directly give the exact graded shifts. The characteristic-zero comparator is already known; subtraction gives the degree-ten invariant without a new ingredient. No earlier exact MacLane table was located; direct implication is the decisive prior coverage.

## value

FAIL

The MacLane arrangement and its global-versus-local comparison are well motivated, and the independent computation is a useful reproducibility check. But the claimed exact invariant is already mechanically implied by stronger published results, with the characteristic-zero comparator already explicit. Recomputing that consequence by a different certificate does not constitute a separately valuable new finding under the exact-invariant standard; no nonroutine remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
