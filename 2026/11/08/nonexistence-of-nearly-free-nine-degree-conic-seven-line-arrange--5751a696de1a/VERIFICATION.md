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

# Reproducible checks and their limits

Run `python3 verify_constraints.py` with Python 3 standard library. Its expected output includes the marker `DEGREE9_ONE_CONIC_SEVEN_LINES_NO_NEARLY_FREE_PASS` and counts of \(63\), \(42\), \(22\), and \(0\) successive admissibility tests. Exact fractions avoid numerical rounding. The script checks the consequences of two established inequalities and the incidence relations, not their proofs.

The critical published premises have these precise inputs: Gałecka's Proposition 4.1 gives \(r\ge4\), Theorem 3.4 gives the nearly-free exponents \((4,5)\), Proposition 4.4 gives \(8+n+3s/4\ge7+5t/2\). Hirzebruch's 1985 strong inequality (Section 6, equation (9)) gives \(t_2+3t_3/4\ge7\) for seven lines when the top three multiplicities vanish. The present hypothesis implies all seven-line multiplicities are at most three. The arithmetic contradiction is \(57\le9u+4v\le56\).

Reproducibility requires no data files or third-party packages. The script is independent arithmetic corroboration, not a geometric solver, exhaustive search over curves, or independent mathematical validation. The distinction between the ordinary line Hirzebruch inequality and the **strong** coefficient-\(3/4\) version is essential.
