---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

On the labelled 2×n torus with n even, north and south refer to the same opposite-row site but must count twice as two directed neighbors. A full checkerboard Q2R step can be fixed only if the first half-phase flips no site, since the second phase never touches the first color; then no site in the second phase may flip either. This is the exact no-two-one-neighbors criterion. The 16 pair-column transfer T(u) checks both central-row predicates with a_r+c_r+2b_{1−r}≠2, has 36 allowed transitions, and accumulates 2 vertical plus 2 horizontal bond-disagreement terms per step, hence labelled cyclic words ↔ trace(T(u)^n) with E correctly counted over 4n bonds. Independently reconstructed the symbolic charpoly factorization into degrees (2,4,4,6) and verified it is IDENTICAL as a polynomial in y and u, not a finite-n fit. The trace/log-det identity gives the all-even-n energy polynomial. At u=1 the factor roots give the stated Lucas and cosine formula with leading φ^{2n}; per-spin entropy logφ. Checkerboard xor gauge preserves the no-two predicate and flips every bond disagreement, giving Z_n(u)=u^{4n}Z_n(1/u), mean E=2n. A separately coded original-site brute-force enumeration of all 2^{2n} states for n=4,6,8 found 36,400,2116 frozen configurations and symmetric full histograms; those finite checks corroborate, while the finite exact 16×16 determinant and universal trace bijection prove every n.

## originality

PASS

Best-of-knowledge PASS for the energy-resolved two-row Q2R frozen-state zeta, exact Lucas total and gauge-energy reflection under the *four-direction multigraph convention*. The original Vichniac dynamics and checkerboard two-stage rule are known, as explained in Kari–Taati full accessible 2013/2015 primary text, but it studies Gibbs measures/invariants, not exact 2×n stationary energy polynomials. The nearest published ladder metastability census is for three-neighbor simple C_n×K_2 under weak one-spin energy stability in an antiferromagnetic field, not Q2R four-direction tie avoidance; its counts cannot imply this polynomial. Another same-date two-row Critters CA zeta has a different rule. Exact source Vichniac 1984 full text remains inaccessible so historical priority is provisional, but that access gap alone does not invalidate the strong positive statement and proof comparison.

## value

PASS

A complete energy-by-energy frozen-state distribution at all even circumferences is a natural microcanonical invariant of reversible energy-conserving Q2R and the thinnest checkerboard-valid toroidal quotient. The polynomial transfer determinant, exact golden-ratio entropy and energy reciprocity give structural facts rather than a small numerical census, with substantive sensitivity to duplicated vertical bonds. No all-cycle dynamics or wider lattice claims are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
