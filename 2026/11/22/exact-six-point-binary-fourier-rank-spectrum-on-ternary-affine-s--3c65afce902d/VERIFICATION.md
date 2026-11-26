---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The convolution is over C; the only rational relation on the three cube roots forces a Fourier zero precisely at phase counts (2,2,2). Restricting to the unique intrinsic affine r-flat has fibers of size 3^(d-r) on frequencies, so the normalized rank is unchanged; r is 2 through min(d,5). In a plane the complement triple is either a line, with rank 3, or noncollinear, with rank 7 (exactly one projective direction gives distinct phases to its three points). The independent integer sweep of all 296010 subsets in ambient dimension 3 verifies the rank-to-count table 9:468, 15:10530, 21:78624, 23:113724, 25:75816, 27:16848; separate affine row reduction gives planar counts 468 at rank 9 and 2808 at rank 21. In dimension 4 the unique projective affine relation cuts out the phase words modulo a common translation. Its five signed support patterns have counts 20,45,30,1,10 with respectively 12,12,6,30,12 balanced words modulo translation: a triple of equal coefficients must see all three labels, the two-sign four-support pattern requires equal pair sums, and the five-support pattern identifies the label at the omitted coordinate with that at the minority sign. For six-support patterns the condition is automatic for equal coefficients and reduces to a distinct-label triple for three entries of each sign. The 106 relation vectors account for disjoint labeled realizations, each with 3^4|GL_4(3)| choices; division by 6! is legitimate after summing labeled patterns. For an affine simplex all 243 relative phase words occur, of which 30 are balanced. Multiplication by the numbers of intrinsic flats proves the stratum counts and their binomial sum for all d, the 2/6/7/8 thresholds and the planar rigidity; no sampling extrapolation is used.

## originality

PASS

The planar component is elementary and anticipated by planar direction results. The distinct claim is the complete higher-dimensional indicator rank spectrum and its multiplicity formulas by intrinsic affine dimension, including the universal lower bound and identification of all possible equality supports. No examined prior statement supplies or implies that complete claim.

## value

PASS

After size three, six is the next support size at which a ternary unit indicator can have a Fourier zero. The complete spectrum quantifies missing character directions and the counts distinguish sporadic and abundant deficiencies across affine dimensions; for instance full rank comes from intrinsic dimension three, not from the affine simplex. Those data and the exact minimizer geometry are useful in analyzing fixed-weight convolution masks and are not an arbitrary cut of a numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
