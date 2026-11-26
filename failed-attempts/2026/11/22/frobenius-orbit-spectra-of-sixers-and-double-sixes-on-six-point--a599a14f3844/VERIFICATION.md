---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The usual 27 exceptional divisor classes over the algebraic closure are E_i, the transforms L_ij of lines through two points, and Q_i, the transforms of conics through the other five. Their incidence follows from the integral blowup intersection form, and Galois relabels their indices. One can exhaust the sixers without assuming an orbit table. If both E and Q occur they must share the same index i, and there can be at most one of each. Four remaining edges L must avoid i and pairwise share a vertex, so all four have common center j. If E but no Q occurs, the remaining edges on the unused labels must be pairwise intersecting; only a triangle on three unused labels or no unused labels can supply enough edges. The Q-only argument is the same; six distinct pairwise-intersecting edges on six labels are impossible. Intersections give the displayed complementary pairs and the standard unique-complement property applies. Consequently the two marked sets have exactly the indicated relabeling actions, and the half swap fixes the underlying pair but exchanges its two labels. The independent run of /workspace/branches/sixer_cycles_audit.py (Python 3) used coefficients of the cycle-subset polynomial for each power and divisor inversion, reproducing both orbit spectra, all eleven rows and the exchanged-half counts. It does not use the frozen expected values or its exhaustive intersection program. The six-cycle has no rational lines because no E/Q label or 2-subset is fixed. A Galois-stable sixer contracts by descent (a geometric contraction of its disjoint curves is unique up to target isomorphism), and its Severi–Brauer plane splits over the finite field. The finite étale zeta factors count the marking orbits, not points of the cubic surface. The computation is conditional on the stipulated blowup and does not address realization of all types at each q.

## originality

FAIL

Buckley–Košir's explicit three-family list already provides the equivariant indexing and the complementary pairs on the labeled blowup, not just the cardinalities 72 and 36. Relabeling the list by any permutation and evaluating its powers mechanically gives the entire claim about Frobenius spectra. No assertion that the identical table was printed is needed for the prior-implication finding.

## value

FAIL

Counting rational contractions is a natural question, and the table is a useful illustration, but this claim is a routine cycle-count recoding of a complete published, relabeling-equivariant list. The half exchange and finite étale zeta factors are mechanically implied as well. The scope expressly omits questions such as realization of the orbit types, and no genuinely distinct valuable remainder is established by the frozen proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
