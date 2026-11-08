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

Use Python 3 with the standard library only. Run `python3 checker.py` in the directory containing `checker.py`. The checker constructs the explicit modulo-counting automata, performs independent partition refinement against the stated minimum, verifies residue-reachability witnesses and direct scattered-occurrence values, and samples exact period candidates.

Observed successful output:

```text
VERIFIED period_cases=117 minimized_cases=243 reachable_states=2849 direct_word_checks=163820
```

The period tests cover \(1\le d\le9\), \(2\le m\le14\) and finite index ranges; minimizations cover automata with at most \(330\) states and up to three target residues; reachability and direct-count comparisons are finite. Such experiments are not a certificate for all \(d,m,r\). For the universal theorem, inspect the explicit period proof (including the converse prime-power argument), state reachability construction, and the subgroup argument distinguishing all states in `RESULT.md`. Independent mathematical audit has not been performed.
