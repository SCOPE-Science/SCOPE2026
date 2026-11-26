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

For row sum k, the constants are an invariant line with eigenvalue k. In quotient coordinates x_i−x_3, the quotient matrix is D_ij=A_ij−A_3j for i,j<3. Trace zero, determinant zero, and positive sum q of the principal 2-minors give exactly the quotient polynomial t(t²+q); the resulting four eigenvalues are simple. The frozen analytic bound q≤3 at k=3 follows from tr(A²)≥Σ A_ii²≥3. I independently enumerated all row choices at k=1,2,3 using the quotient predicate and weak connectivity. Simultaneous conjugacy and balanced-block testing over all 13 proper partitions reproduced labeled counts 1560/840/176, orbit counts 65/36/8, synchrony counts (0,47,18)/(1,27,8)/(2,5,1), all 109 frozen CSV entries, and the three displayed representatives. Equal incoming multiplicities give equal multisets and hence equal derivatives on the polydiagonal; unequal multiplicities can be detected by a smooth input-symmetric sum of interpolating functions. The k=1 replay had no cases; k=2 had 216 labeled cases in nine classes, five with one proper partition and four with two. Valency zero cannot have the imaginary pair. Thus three is minimal independently of the cited lower-valency results.

## originality

PASS

The supported distinct advance is the complete valency-three spectral and synchrony census and the primitive representatives, which settle the minimum when combined with the already known lower-valency exclusions. The leading primary source supplies those exclusions, not the decisive upper bound or the census. No independent equivalent table was established in the checked sources.

## value

PASS

This is the full census at the first valency where the known four-cell spectral mechanism is not constrained by a proper robust synchrony space. Exact representatives and the joint distribution by frequency and synchrony make the result useful for choosing and comparing networks in subsequent bifurcation studies; the cutoff is determined by the onset, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
