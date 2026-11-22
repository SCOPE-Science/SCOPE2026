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

# Reproducibility and checks

The embedded `prefix_verify.py` generates rooted full ordered binary trees as nested pairs and breadth-first searches all reachable image subsets, using a precomputed transition lookup. The independently implemented C++17 program `prefix_verify.cpp` generates parenthesized trees, parses them into proper-prefix states, and searches subsets by direct statewise image updates.

Execute `python3 prefix_verify.py` and `c++ -std=c++17 -O2 prefix_verify.cpp -o prefix_verify && ./prefix_verify`. Both programs have built-in assertions for the \(651\)-tree height-four count, the complete distance histogram, \(19\) nonsynchronizing decoders and two extremal height-four codes with shortest reset length \(17\). They were both run and returned their expected output. The Python program prints explicit words that reset the two extremal decoders; both have length \(17\). The alternate textbook-form word `00011110001111000` was separately simulated and resets the decoder whose unique three-letter codeword is `000`.

The exhaustive procedure uses no guessed word-length cutoff. Every reachable subset is explored, and no arbitrary-length or infinite-height assertion is inferred. Source availability and literature coverage cannot establish that no equivalent unpublished computation exists. No independent audit has been performed.
