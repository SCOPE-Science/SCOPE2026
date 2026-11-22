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

# Computation and mathematical verification

Execute `python3 verify.py` with Python 3. No additional packages are required. It directly evaluates each polynomial and its shifted neighbour, computes integer two-adic valuations independently of the two-centre proof, and compares results with the proposed exact cell table.

Checked: 128 positive coefficient triples with odd leading and linear coefficients and even constant; for each, all 81 cells indexed by \(1\le i,j\le9\) on the entire dyadic interval \(0\le n<2^{13}\), plus all 49 cell conditions indexed by \(1\le i,j\le7\) through one complete own residue modulus. Explicit zero-resultant, negative-covariance and positive-covariance boundary examples are included. The script prints PASS on success and raises an assertion on any mismatch.

These computations are finite tests only. The unlimited coefficient, index and valuation claims require the Hensel-root two-centre proof in `RESULT.md`, including the second-moment tail bound; no arithmetic oracle or independent expert certification is asserted.
