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

# Verification

Run `python3 verify_even_isolation.py` from the directory containing this file. Standard Python 3 suffices; there are no external packages or downloaded datasets. All arithmetic in the checker uses exact fractions and integer counts.

Checks performed: exhaustive enumeration of all labeled even simple graphs with \(3\le n\le6\) at seven rational probabilities, parity-space dimension checks, the uniform \(p=1/2\) covariance identity for \(3\le n\le18\), the \(n=4\) exact rational identity at 99 positive rational probabilities, sign instances for even \(4\le n\le22\), plus positive odd dense signs and relative asymptotic-ratio checks through \(n=23\). Output recorded: `PASS: 189 exact comparisons; exhaustive parity-filtered graph enumeration for n=3..6.`

These are finite computational checks, not proofs of the universal sign change. The infinite assertions are proved directly in RESULT.md by Fourier parity projection and the parity-dependent minimum complement edge sets. Cross-checking does not constitute independent validation.
