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

# Reproducibility and verification

`verify.py` is a standalone Python 3 program requiring only the standard library. Run `python3 verify.py` from a directory containing the extracted file. Its expected terminal output is:

```
PASS profiles 516 all_permutation_pairs 4368 position_profiles 2896 random_large_profiles 1440
```

The program enumerates all distinct independent run permutations for \(516\) multisets of positive lengths at most \(4\) with \(1\le k\le3\), giving \(4{,}368\) arrangement pairs. It checks every cyclic factor length \(1\) through the entire period. The occurrence-span routine checks its direct positional condition on \(2{,}896\) profiles. With fixed random seed `301128`, a further \(1{,}440\) larger profiles with \(4\le k\le9\) are checked against the direct window maxima and the positional condition. The code's period-doubled cyclic-window search is independent of the proof's multiset-window argument. The same file was executed before and after extracting it from the saved package.

These comparisons are finite and do not certify the theorem for all parameters. The complete universal proof is the multiset-window lemma followed by span dominance and the factor-to-prefix implication in `RESULT.md`. The strict length-five example was also checked directly. No external or independent audit has been performed.
