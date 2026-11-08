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

# Verification guide

The theorem is proved in `RESULT.md`. The standalone `checker.py` is a reproducibility aid, not an oracle for an infinite lower bound. Using Python 3 without third-party libraries, run:

```sh
python3 checker.py
```

The code deterministically checks 600 parameter pairs (including boundary cases), all witness state counts, acceptance at an explicit range of input lengths, a proper transition-compatible 2-coloring, graph connectedness, and that each undirected graph is a tree or has one cycle. Expected first line: `PASS: 600 independently replayed deterministic witness constructions`.

Critical noncomputational checks are: (1) a repeated state in a bipartite path gives a positive even-length detachable subrun; (2) for odd modulus the second allowed multiple is the earliest accepted word of the other parity; (3) the return arc creates one directed cycle of length the modulus (even case) or twice the modulus (odd case); (4) the two accepting residue classes in the odd construction cover exactly all allowed multiples.

The checker cannot establish historical originality, validate unrelated graph definitions that silently permit loops, or replace independent mathematical review. No independent audit has been conducted.
