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

# Computational and deductive verification

The theorem for all \(n\ge3\) is proved in `RESULT.md` by the exact undominated-edge identity, complete legal-move classification, sharp length bound, equality rigidity, and explicit enumeration. Finite enumeration alone is not an infinite proof.

`verify_open_neighborhood_dp.py` builds the triangular graph directly from two-element subsets of \([n]\), constructs open-neighborhood bit masks independently of the matching argument, and uses memoized exact dynamic programming to count *longest total* legal sequences. Every order \(3\le n\le11\) passes, with exact length and formula comparisons recorded in `dp_output.txt`. It counts paths ending with total domination; intermediate prefix counts are not falsely counted as completed optima.

`verify_matching_attachment.py` constructs ordered near-perfect matchings and then all attachment choices for odd \(n=3,5,7\). It separately evaluates legality, total coverage, unique ordered sequences and the factorial count. The observed counts \(6,720,453600\) agree. Its successful output is `construct_output.txt`. This generator is structurally distinct from the direct neighborhood DP and checks the bijection's forward direction; the general converse and upper bound remain mathematical deductions.

For reproducibility from this package, save the two Python scripts and text artifacts to a common folder, then run `python3 verify_open_neighborhood_dp.py` and `python3 verify_matching_attachment.py` under standard Python 3. No external libraries are needed. Expected outputs are supplied as full text. Independent scholarly validation has not been performed.
