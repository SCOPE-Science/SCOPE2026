---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility and limits

Run `python3 verify.py` using Python 3 standard library only. The verifier implements maximum matching of each induced path via a separate dynamic program, not by reusing the closed-form payoffs. The tested domain is all proper positive-worth coalitions for each path order from 3 through 16, with exact `Fraction` arithmetic, and the complete rational core grid with denominator `m+1` for even orders 4, 6, 8, 10. It checks the formulas, all coalition core constraints, the claimed sharp second-layer witnesses, and the unique optimum over those finite grids.

Recorded verification result: `VERIFIED: 124293 positive coalitions; 633 rational-grid candidates`. There is no time limit or numerical tolerance in these finite loops. The infinitely many path orders are established by the analytic argument in `RESULT.md`; finite checks alone cannot establish them. The complete array of real-valued possible core vectors is not exhaustively enumerated by the rational grid; the uniform-gap inequality in the proof covers them. The cited 2026 general algorithm and the 1998 original treatment are prior work, not reproduced or re-run here.
