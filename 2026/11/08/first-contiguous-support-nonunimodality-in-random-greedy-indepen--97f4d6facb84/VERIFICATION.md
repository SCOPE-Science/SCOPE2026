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

# Exact verification of the finite tree cutoff

Execute `python3 check.py` with a standard Python 3 interpreter. No third-party libraries or downloaded data are required. Prüfer decoding enumerates all labeled trees on \(n\ge2\) vertices. Directly enumerating all \(n!\) vertex orders gives an exact count \(c_k\) for every size \(k\), so \(\Pr(X=k)=c_k/n!\). All comparisons in the checker are integer comparisons, with rational fractions used only to print the canonical witness law.

The checks cover \(n=1,2,3,4,5,6\) with tree totals \(1,1,3,16,125,1296\) respectively and gap-free nonunimodal totals \(0,0,0,0,0,360\). At order six, each exceptional labeled tree must have precisely the three arm lengths \(1,1,3\), and output counts \((190,160,370)\) for sizes \((2,3,4)\). A separate first-arrival rational recursion, described in the proof, confirms the same witness fractions. The script's ending `CERTIFICATE PASSED` means all checks executed successfully, not an external certification.

Limitations: the finite census has no implications for larger order, and literature priority cannot be certified by a computation. No independent audit has been performed.
