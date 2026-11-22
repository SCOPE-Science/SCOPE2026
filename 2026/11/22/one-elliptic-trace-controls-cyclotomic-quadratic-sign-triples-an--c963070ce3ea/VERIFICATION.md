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

The proof uses the exact character-sum substitution identities and the elliptic Hasse bound. In the packaged `verify.py`, arithmetic in each prime field is checked using independently generated Euler-criterion and square-set characters; arithmetic in the quadratic extension fields \(\mathbb F_{25}\) and \(\mathbb F_{49}\) is checked using both explicit square sets and quadratic norms to the prime field. Direct eight-word histograms match the trace expressions at each tested order. The finite certificate `finite_cases.json` contains every eligible field of order below \(71\) and the separate characteristic-three field \(\mathbb F_3\). It records the exact two extension-field exceptions and the prime-field exceptions, while an additional 76 primes through \(499\) are checked as nonessential corroboration.

To rerun, place `verify.py` in a writable directory and execute `python3 verify.py`. It regenerates `finite_cases.json` deterministically and exits on any contradictory count. No external libraries, data files, or network services are required. A passing run is a finite verification, not a proof of the infinite claim; the complete proof is in `RESULT.md`.

The result makes no exact-histogram assertion in characteristic three and makes no assertion in characteristic two. No independent mathematical validation has been carried out.
