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

# Reproducible checks

Run `python3 check_direct.py` to group all fixed-content words by actual counts of every contiguous one- and two-symbol factor. This independently checks the number and cardinality of profile fibers for 43 parameter pairs with total length at most ten. The checker explicitly verifies the number \(k\) of nonempty return gaps is invariant across each observed fiber, the prescribed size \((r-1)!/(r-1-k)!\), and the total source-word count.

Run `python3 check_lists.py` to construct all unordered sets of ordered lists containing a distinguished token, turn each into a word, and compute its observation. This separately verifies that the construction is injective and that the complete Lah stratum enumeration holds in 56 cases; it reports the first seven saturated values.

Both scripts use only the Python standard library. The exact stdout of completed checks appears in `check-output.txt`. These experiments do not establish the infinite theorem; the proof's endpoint identities, forced-singleton path decomposition, and return-permutation counting do. Limitations: all payload letters must occur once and be labeled; the statements do not cover multi-delimiter alphabets or noisy/cyclic observations.
