---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The no-inversions row action fixes every face vertex whenever it stabilizes a face, because columns are distinct, giving cellular orbit counts (n,C(n,2),2C(n,3),2C(n,4)). A4 is transitive on ordered one/two-row injections and has two parity orbits on triples/quads. Both triangle orbits have standard edge boundary, making the quotient 2-skeleton contain the complete-graph simplex 2-skeleton and π1=0. The integral ker ∂2 splits into negative-positive triangle differences δ_abc and positive tetrahedron cycles w_0ijk. The two signed 3-cell boundaries ∂F+ = w_abcd+δ_bcd+δ_abd and ∂F−=w_abcd−δ_acd−δ_abc permit unit eliminations with z_ij=δ_0ij, leaving one relation ∑_{pairs in any 4-subset}z_pair=0. Thus H2 is integer coker W_(2,4)(n−1), not just a rational rank identity. Wilson inclusion-matrix diagonal-form theorem (full lawful Ghorbani et al. reproof, Corollary 3) applies for v=n−1≥6 and yields factors 6 once, 3 with multiplicity v−1, others units. H3 follows by Euler characteristic and freeness of kernel of top boundary. Independent reconstruction of inclusion matrices v=6 and v=7 gave exact Smith factors [3×5,6] and [3×6,6] respectively; finite tests corroborate, while the all-size claim relies on the symbolic elimination plus general theorem.

## originality

PASS

PASS only for the all-width n≥8 alternating-row quotient cellular reduction and unbounded three-primary torsion rank, **not** for the known n=7 instance or Wilson’s 1990 diagonal matrix theorem. Substantially overlapping prior homotopy classifications at n=7 and pre-stable widths are explicitly credited.

## value

PASS

A uniform exact integer homology theorem exhibits linearly unbounded three-primary torsion in a natural nonfree geometric quotient of classical chessboard complexes. The canonical incidence-matrix connection explains the torsion structure for every stable width, beyond a known finite first example; a full homotopy splitting or downstream theorem is not required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
