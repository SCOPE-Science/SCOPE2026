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

The proof uses the explicit integer-lattice Lie group and an equivariant Chevalley–Eilenberg differential. The key identities have been checked symbolically in the text; in addition, the standalone `checker.py` performs finite modular computations on exterior powers for every permutation through four arms. Replay with `python3 checker.py`, which needs only the Python standard library. The expected output ends with `PASS: separate chain-level finite-field tests for all n=1..4`.

The computed test counts by number of arms are \(4,12,48,240\) degree-and-permutation comparisons, respectively. These are exact over \(\mathbb F_{1009}\), not a claim about torsion, arbitrary coefficient fields or a computer proof for all \(n\). The all-rank characteristic-zero theorem is established by the written \(\mathfrak{sl}_2\) argument and graded-symmetric-power construction. Quotient cohomology is rational ordinary singular cohomology, not Borel equivariant cohomology. Literature-priority uncertainties are listed in the scientific review.
