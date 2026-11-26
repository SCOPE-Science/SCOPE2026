---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The eight-ballot score differences give the stated covariance, full lattice and zero step. Scaling Fourier inversion of the pinned marginal gives pair masses 2/(pi n) and sqrt(2/(pi(p^2+q^2)n)) and a centered nondegenerate conditional gap. Thus half of tied pairs beat the third at leading order, and the full-lattice triple events have orders at most n^-2 and n^-1. Read the proof's pair-count discussion as counting strict winners once and then adding the triple probability once, or counting weak pair ties and subtracting two triple probabilities. The finite assertion follows from (U,V)=(kp,-kq) and |V|<=n, and q=1 makes n<q vacuous for n>=1. This is a pair equality statement only. Exact ordered-profile replay through four voters (python3 /workspace/replay_thiele.py) confirms score differences, covariance, exact pair identity and winning-tie examples.

## originality

FAIL

The frozen core duplicates record 1 in the same culture; no priority between the same-day packages is asserted. The additional n<q clause is not itself stated in record 1, but is an immediate coprimality-and-range corollary of its explicit integer score-difference expression and does not establish a distinct substantive tie asymptotic. In fact |U|+|V|<=n from the mutually exclusive ballot contributions, so the same argument gives the stronger n<p+q cutoff; the frozen bound is not sharp in general.

## value

PASS

The submitted theorem as a whole has useful quantitative content about maximal committee ties and fixed score arithmetic. Its finite equality condition clarifies a regime where a denominator cannot generate new pair equalities, but on its own it is an elementary and generally nonsharp corollary rather than a worthwhile standalone repair for the duplicated main theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
