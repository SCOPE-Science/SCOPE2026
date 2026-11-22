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

# Verification notes

The general result is established by the explicit proof in `RESULT.md`. The executable checks are `verify_coning.py` and `verify_coning_independent.py`, using Python 3 with no extra dependencies. Their observed output is recorded in `CHECKS.txt`.

The first checker computes full finite functional graphs from an adjacency bit representation. All isolate-free labelled simple base graphs on two through five vertices were tested for one and two added clique vertices; a seeded sample of six-vertex bases was additionally tested. The second independently constructs graph edges and states as Python sets, classifies complete attractor basins, and tests the same structural theorem through three added clique vertices on all isolate-free bases of orders two through four.

Both checks agree with the proof's formula and with the labelled identification of every attractor and basin in their stated finite domains. The seed only fixes reproducibility of the six-vertex random sample. No enumeration or computational test is asserted to prove the unrestricted theorem, and no independent external scientific audit has been performed.
