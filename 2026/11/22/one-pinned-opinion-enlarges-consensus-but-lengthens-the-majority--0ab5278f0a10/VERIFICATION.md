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

# Reproducibility of finite counts

The domain, local Boolean rule and integer transition implementation are stated in RESULT.md. The two included source programs `check_a.cpp` and `check_b.py` cover, respectively, all 32,768 pinned and all 65,536 ordinary initial configurations; they use different successor implementations and different methods to classify finite directed cycles and transient depths.

`check_a.cpp` builds a successor digraph, removes its noncyclic vertices in indegree order and propagates each state back to the attractor. `check_b.py` explicitly materializes the Boolean opinions, follows successor paths from each unprocessed word, and identifies the first repeated state. They reproduce the eleven nonzero entry-period cells, 425/301 recurrent orbit counts, sharp time six, 24 last-layer states, and two named basin sizes. A direct witness trace confirms the sharp depth, and comparison against the unpinned map confirms 8,229 versus 9,383 all-one basin members among the same initial words.

These are complete finite integer enumerations; the code itself and its outputs, not a timing estimate or a sampled log, form the checkable finite certificate. C++17 and Python 3 are sufficient; no external packages are required. The general isotonicity argument used for zero consensus loss is explained in the proof.

The checked computation does not address other cube dimensions, random dynamics or historical priority. External independent validation has not been performed.
