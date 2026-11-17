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

`theta_bruteforce.cpp` implements the strict-majority rule with incumbent tie retention and independently enumerates all configurations, testing two-step return with nonfixed first step. It checked all 77 nondecreasing path-length triples in the stated finite range (5,294,176 configurations), plus six selected graphs. The recorded output is `theta_bruteforce.out`.

`theta_construct.py` constructs every candidate from alternating active paths and no-singleton-run stationary paths, verifies its images under the original update rule, and compares the resulting counts with an independently implemented run-composition formula. It checked 113 parameter triples and 6,357 constructed orbits, plus eight selected examples. The recorded output is `theta_construct.out`.

Commands: `g++ -std=c++17 -O3 theta_bruteforce.cpp -o theta_bruteforce && ./theta_bruteforce`; `python3 theta_construct.py`. The compiled executable is generated locally from the standalone source; there are no third-party dependencies.

Verification proves the stated finite checks occurred; it does not convert finite testing into a proof for every path length. The universal claim is established by the local propagation, frozen-run, and terminal-majority lemmas in RESULT.md. Mathematical priority remains qualified and no independent external audit has been conducted.
