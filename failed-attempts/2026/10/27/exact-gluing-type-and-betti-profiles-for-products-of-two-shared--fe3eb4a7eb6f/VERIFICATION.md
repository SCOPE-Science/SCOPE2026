---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Distributing the ideal product gives the four displayed generators. The first three lie in [m²,2m²), and the fourth exceeds each and is not divisible by m, proving minimality. Since d∈H and d is invertible modulo m, the bounded normal form exists by carrying md and is unique. For a pseudo-Frobenius gap, addition of d forces the top digit m−1; testing positive mH gives the necessary PF condition on h. Conversely, addition of a positive mH term or the carry of d adds a positive member of H to h, proving the lift. The Apéry representatives modulo m² are m u_r+jd, yielding the genus formula by summing. Type invariance and the three-generator criterion force the asserted pair-gcd test. The monic regular relation has coefficients in the graded maximal ideal, so the minimal mapping cone multiplies the 3-generator Betti polynomial by 1+z, in every field. For the defect, each PF gap other than F has a gap as its complement under x↦F−x, giving 2g−F≥t; substitution then proves the exact defect and excludes almost symmetry in type two. The stated m=3 extremum gives (F,g,t)=(46,25,2). At the endpoint family the residue costs come from steps ±1, so the two candidate costs suffice. Only branch endpoints P and Q can be maximal in Apéry order. With e_0=(2m−1) mod 3, their difference is P−Q=m(2−e_0)−1; it is 2m−1 when m≡2 mod 3, otherwise m−1 or −1, so only the first case has domination. This closes the implicit step at RESULT.md line 62. Frozen support was inspected, not executed. Direct membership enumeration, independently checking endpoint PF and genus at m=3,…,35, is replayable with python3 /workspace/branches/independent_bounded_checks.py. It is corroboration, not the general proof.

## originality

FAIL

The main theorem is a specialization of general gluing and three-generator results after expanding the four generator products. In particular, Chen et al. Proposition 4.5, not merely their distinct-scope Proposition 4.9, already gives the entire PF/type lift and its residue decomposition. Gimenez–Srinivasan's gluing resolution gives the asserted Betti multiplication. The exact defect identity is algebraic substitution into the general Frobenius, genus and type formulas. The strongest candidate for a distinct remainder, the extremal-offset ordinary Apéry law, also specializes explicitly from Morales–Dung Theorem 3.8 with a closed one-line evaluation of its Euclidean parameters, and the displayed PF set follows by taking the two maxima of that specialization. This finding is correct but the stated package does not establish a distinct scientific claim. No repair is claimed.

## value

FAIL

The exact invariants are useful descriptive data for the new ideal-product setting, but the proposed contribution consists of expanding the product definition and specializing existing gluing, three-generator and near-arithmetic formulas. The genus/defect algebra and the smallest sharpness witness do not supply an independently unknown invariant, obstruction or boundary after those implications are credited. No nonroutine substantive remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
