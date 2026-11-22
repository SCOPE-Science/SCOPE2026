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

# Verification and reproducibility

The mathematical proof is in `RESULT.md`, including the precise interval lemma, consecutive-edge classification, exhaustive rigidity condition and integral top-boundary argument. The independent finite check script is `CHECK.py` and requires only Python 3's standard library.

Run `python3 CHECK.py` from this directory. Actual execution checked all top-size antichains for \(m=1,\ldots,8\), comparing direct ideal traces with the theorem's predicted supports. The script reported 328 antichain/parity comparisons, equality of the expected extremal counts, failure of the single size-\(m+1\) antichain, and the predicted top boundary ranks for \(m\le5\). The ideal counts checked at these values are \(5,13,34,89,233,610,1597,4181\).

The result is **all-order** by proof, not by numerical extrapolation. Direct verification does not certify the absence of equivalent published work, nor does it amount to independent mathematical validation. The top-homology claim does not determine any lower homology group.
