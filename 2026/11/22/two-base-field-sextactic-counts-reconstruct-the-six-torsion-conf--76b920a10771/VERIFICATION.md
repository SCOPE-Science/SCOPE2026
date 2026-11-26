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

A rational flex O makes the hyperplane class 3O and Frobenius act linearly on the elliptic-curve torsion. Restriction identifies all line and conic sections with the complete linear systems of 3O and 6O: it is injective because a cubic is not contained in a degree-one or degree-two curve, and the vector spaces have matching dimensions 3 and 6 by genus-one Riemann–Roch. Abel's criterion reduces contact 6P and distinct three/six-point incidence to the respective torsion sum tests. A factored conic with divisor 6P would have both line divisors equal to 3P, so P would be a flex; this leaves precisely E[6] minus E[3] for genuine sextactic contact. A conic through six distinct points has no repeated component, and over the algebraic closure its singular/reducible cases exactly correspond to two disjoint zero-sum triples. Characteristic prime to six makes the torsion étale. CRT gives the two matrix factors; the Weil pairing gives det B=q mod 3. The GL₂(F₂) classes are identity, one nontrivial Jordan class and one irreducible quadratic class; GL₂(F₃) has two scalar, two Jordan, one split-distinct and three irreducible quadratic classes. Conjugate elements have the same permutation spectra. Fresh exact enumeration tested all three- and six-subsets of the 27 points, constructed the reducibles from disjoint line pairs, then computed the induced cycle decompositions for all 24 class pairs. The five sizes are 27,81,8244,2268,5976; the 19 keys match the RESULT lists, every key has exactly one joint spectrum and there are exactly 19 distinct joint spectra. All 24 rows of the actual frozen class_table.csv match the independently computed matrices, class sizes, determinants, cycles, listed fixed counts and second-extension counts field by field. The (2,3,76) example gives K: 1^76 2^4084, reducible 1^54 2^1107, smooth 1^22 2^2977. Each length-d cycle contributes d points exactly when d divides the extension degree, and the corresponding zeta factor is (1−T^d)^(-1).

## originality

PASS

The sextactic torsion description, geometric cardinalities and specific Fermat Frobenius spectra are known. In particular the illustrative (2,3,76) spectrum is exactly covered by prior Fermat arithmetic. The distinct supported claim is the universal 24-class, 19-spectrum classification for rational-flex cubics and separation by the two counts plus the known determinant; the strongest inspected special-case and analogous results do not establish it.

## value

PASS

The two easy-to-state base-field invariants recover cycle structure and all extension counts simultaneously for several naturally associated schemes, even for conics whose individual sextactic points need not be rational. This is an exact separation result for a motivated arithmetic configuration, not recomputation of its geometric sizes or a one-field coincidence. Identifying the 19 joint spectra rather than forcing uniqueness of 24 class pairs is useful precisely because the observations do not determine the actual conjugacy pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
