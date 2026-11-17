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

# Verification procedures and actual scope

`certificate.py` reconstructs the local Rule 22 temporal-height graphs from their bit-level truth table, computes complete recurrent components, compares the period-two and period-four recurrent cores, and checks that the two eighteen-vertex components are interchanged by temporal rotation. It calculates their common determinant using integer Newton identities, independently enumerates nine directed simple cycles and their shared vertices, and checks the resulting semigroup/exact-count support through length one hundred. Replay printed `PASS`. Its exact graph/cycle checks are the finite certificates underpinning the universal proof.

`bruteforce.py` instead uses bit-parallel local updating and checks **every** labelled binary initial state on each cyclic ring from three to twenty sites. It explicitly tests second and fourth temporal returns, divides the surviving fourth-period states by four, and matches the generating-function counts. Replay printed `PASS`. The exact outputs are embedded as `certificate_output.txt` and `bruteforce_output.txt`. Both programs require only standard-library Python 3.10 or newer.

The exhaustive program alone proves only its tested finite cases; infinite-length statements are consequences of the finite graph's complete component/cycle enumeration and standard determinant and Perron–Frobenius arguments. No independent third-party verification or mathematical audit has been carried out.
