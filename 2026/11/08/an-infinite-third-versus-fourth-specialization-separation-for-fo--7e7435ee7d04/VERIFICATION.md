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

Run `python3 artifacts/verify.py` with Python 3.9 or later; it has no third-party dependencies.

The verifier performs exact polynomial arithmetic. It checks the two critical cancellation identities for the three-color proof, constructs the proper three-color spine sums at \(h=0,\ldots,12\), and independently enumerates vertex-by-vertex colorings (including the number of colors used) at \(h=0,1,2\). For the proof of the four-color separation, it computes \([q^8]\) of the difference using an exact degree-eight truncation, verifies the entire table for \(h=0,\ldots,16\), and spot-checks \(h=19,25,40\). In particular, the nine values for \(h=8,\ldots,16\) support a valid infinite-degree argument because the proof establishes that this coefficient is a polynomial in \(h\) of degree at most eight throughout \(h\geq8\).

Finite enumeration alone does not prove equality for every \(h\), nor does it prove the separation at every \(h\). Those parts follow from the algebraic cancellation and degree-bound arguments in `RESULT.md`. The independent audit is not performed; no certification by an independent reviewer is implied.
