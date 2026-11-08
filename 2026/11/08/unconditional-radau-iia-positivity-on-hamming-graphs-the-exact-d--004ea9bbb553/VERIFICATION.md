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

## Reproduction
Run `python3 verify.py` in the same directory as the extracted files. It requires only the Python standard library. The expected terminal result is `VERIFY_OK` followed by counts of ten positive-case rational identities, nine Bernstein controls and the negative distance-five coefficient.

## Actual checks and limitations
The exact-rational verifier was executed successfully. It builds the Hamming tensor spectral entries from first principles; verifies every listed rational-function entry by polynomial cross-multiplication; independently obtains the negative Bernstein coefficient arrays by a change of variable; checks the explicit scalar witness values; and obtains the fifth Taylor coefficient by a recurrence. Separate direct dense-matrix computations confirmed stochastic row sums and signs for representative \((d,q,h)\) including \((2,2,0.2)\), \((2,3,0.3)\), \((3,2,2)\), \((2,4,1.5)\), \((3,3,1)\), and \((4,2,2)\). They are sample checks only. The infinite statement is supported by the proof, not by interpolation or a finite scan. Independent mathematical validation has not been performed.
