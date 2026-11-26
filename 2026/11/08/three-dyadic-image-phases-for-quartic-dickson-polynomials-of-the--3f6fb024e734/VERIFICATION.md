---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For h(Y)=Y²−3aY+a² the difference factor Y+Z−3a is a unit on equal-parity arguments. The induced bijections on finite ball quotients send the square branches for odd x and x≡2 mod 4 to the stated balls. For x=4s, choose the root U(s)≡1 mod 8 of 1+16s²/b: v↦v+4v² is an isometry and bijective on each finite quotient. The square-root difference identity gives U(s)−U(t) divisible by 8(s−t); thus s↦sU(s) is an isometry, bijective on all finite quotients and hence on Z₂. The third branch is exactly a²+16b times the square image translated by a² (i.e. a²+16b S₂). Reducing the three images mod 8 gives 2−3a, 5, 1; coincidences are absorptions into the first, full ball. Unit squares have measure 1/8, and the valuations of nonzero squares are even, giving square measure 1/6 by summing 4⁻ʲ/8. The residue count follows by truncating the same square classes and including zero; direct reduction checks k=1,2. For k≥5 each point in the first and second regular balls has four and eight preimages in its respective input branch (the latter uses unit squares mod 2^(k−2) and two lifts); in the third, the normalized isometry gives precisely four lifts per square root mod 2^(k−4). Overlaps sum the separate fibers. Own replay: `python /workspace/reproductions/check_discrete_claims.py 2` checked all odd parameters at k=1,…,9 for image counts, plus 174592 exact target multiplicities at k=5,…,9 using valuation-based square-root counts. Finite checks are corroboration only; fibers are asserted in the record for k≥5.

## originality

PASS

The exact three-branch second-kind image, its density trichotomy, and the target-wise fibers are distinct on available evidence. Priority is qualified, not certified.

## value

PASS

A complete, all-unit-parameter classification of the first nonpermuting quartic in this family is informative beyond permutation status. It identifies three distinct image densities and exact fiber multiplicities even on overlapping parts, resolving local arithmetic data for the whole family rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
