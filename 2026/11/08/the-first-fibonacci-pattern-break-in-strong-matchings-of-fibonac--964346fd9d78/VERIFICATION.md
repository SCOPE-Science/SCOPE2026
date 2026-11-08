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

# Reproducibility and proof boundaries

Run `python exact_search.py` with standard-library Python 3.10 or later. The generated output has the same eight lines as `exact_output.txt`. The algorithm constructs every admissible word, every allowed edge, and the compatibility graph; proper greedy colorings upper-bound each remaining clique, and strict-incumbent pruning preserves every tie. It exhaustively obtains twelve optimal induced matchings at dimension eight, and computes six two-element reversal orbits.

Run `python ilp_check.py` with a compatible NumPy/SciPy installation. The independently reconstructed conflict graph has 130 edge variables and 2,385 pairwise conflicts at dimension eight. Exact mixed-integer optimization returns twelve. Its output is `ilp_output.txt`.

`optima.json` lists twelve optimal matchings as twelve arrays of twelve unordered binary endpoint pairs. The matching arrays can be directly checked against the Fibonacci-word condition and pairwise endpoint-distance condition. The upper bound and exhaustiveness require the supplied search algorithm; the list alone only certifies a lower bound and orbit representatives. No proof for dimensions above eight is asserted. Algorithmic correctness and non-exhaustive supporting computation are distinguished; an independent scholarly audit has not been performed.
