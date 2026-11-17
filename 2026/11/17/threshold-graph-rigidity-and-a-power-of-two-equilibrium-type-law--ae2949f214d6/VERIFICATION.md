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

# Reproduction and limits

Run `python3 verify.py` for the canonical creation-word criteria, sparse-word recursion, complement checks, and labelled count polynomial through 15 vertices. Run `c++ -O2 -std=c++17 -Wall -Wextra brute.cpp -o brute && ./brute` for a separately implemented exhaustive original majority update on all graph states for \(3\le n\le7\). The captured output files `verify_output.txt` and `brute_output.txt` both end in `PASS`. Files are standalone, using the Python standard library and a C++17 compiler; no external data files are required.

The proof in RESULT.md applies to all \(n\ge3\). Neither finite enumeration nor software runtime is evidence of an infinite universal claim. The theorem does not classify nonfixed cycles, convergence depths or basin sizes. The historical-priority comparison is necessarily limited to accessed sources. Independent mathematical validation has not been performed.
