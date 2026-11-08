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

# Reproduction and scope

Run from this directory using a standard Python 3 interpreter:

```sh
python3 verify.py
```

Expected output:

```text
PASS: 240 labeled perfect codes; 2 alphabet-relabeling orbits of 120 each; reversal exchanges orbits
```

The checker constructs every admissible maximum-size word centered at each alphabet symbol, independently generates all six ordered subsequences from the six position pairs, and searches for six pairwise disjoint masks spanning all \(36\) ordered pairs. It then relabels the symbols using all \(720\) alphabet permutations, tests the sizes of both relabeling orbits, and checks that reversal switches them. It uses only the Python standard library; it does not fetch external data.

The structural proof in RESULT.md is independent of this program. The classification requires exact two-position deletion (not adjacent burst deletion) and simultaneous alphabet relabeling, with word reversal considered separately. The prior existence and minimum-cardinality result is not new. Independent mathematical validation has not been performed.
