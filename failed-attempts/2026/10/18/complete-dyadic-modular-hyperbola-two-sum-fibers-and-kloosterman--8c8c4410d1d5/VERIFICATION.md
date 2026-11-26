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

For the ordered pair x,y with s=x+y, oddness forces even s and z=s/(xy) forces matching valuations; s=0 separately gives z=0 with every odd x allowed. For nonzero s, dividing by 2^a and translating x by s/2 gives the stated square congruence. The right-hand side has the parity forced by odd x and every root has 2^a lifts, with no division by a nonunit after passing to the smaller ring. Odd square roots are counted by the squaring homomorphism on the odd units, with kernel sizes 1,2,4 at moduli 2,4,≥8; zero and nonzero even roots then follow by valuation and lifting. For completeness the s/2 square is independent of representative since m≤k−1. Summing the supported z-values with a≥2 and the zero row gives 4+sum_{m=3}^{k−2}4^{m−2}; the remaining 2^{k−2} rows each have precisely L_{k−1} entries. Independently, if P_j is the collision probability of two independent uniform squares modulo 2^j, separating both-even and both-odd inputs gives P_j=P_{j−2}/4+2^{1−j} for j≥3, with P_1=P_2=1/2. Thus P_j=j/2^j. The a=1 row at k≥4 compares even squares, yielding P_{k−3}; the a≥2 strata with m≥3 each contribute 4n², the last two strata contribute 3n², and the zero row contributes n², with n=2^{k−1}. This proves 6(k−3)n². For k=2,3 all odd units are self-inverse, and each even diagonal target has exactly n ordered representations, giving energies 8 and 64. Two-dimensional character orthogonality gives the factor N² for the joint moment, and n^4 division gives the stated normalized values. The independent square-pushforward program compared all 87,376 target coordinates for 2≤k≤8 to direct row counts, including support and energy. Replay: python3 /workspace/branches/audit-3.py.

## originality

FAIL

The distinct indexed Resultary record 41fad24c7e81 states the same ordered pointwise square-root law, sumset size, energy and joint fourth moment throughout k≥4. Removing its redundant parity filter on the roots and evaluating the finite sum L_{k−1} give exactly the frozen formulas. The extra k=2,3 cases both have a diagonal inverse graph, so they supply no substantive distinct remainder. The archive's November date does not establish that it preceded the frozen October record; the decision concerns demonstrable equivalent scientific coverage, not priority, origin or dependence between the records.

## value

FAIL

The complete dyadic two-sum invariant is scientifically motivated, but all nontrivial levels are already present in the equivalent indexed theorem. The only uncovered cases are moduli 4 and 8 where inversion is the identity on odd units, and the normalization is elementary orthogonality. These residual facts do not make a separately useful exact-invariant result. No weighted extension claim or other substantive remainder is proved by the frozen work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
