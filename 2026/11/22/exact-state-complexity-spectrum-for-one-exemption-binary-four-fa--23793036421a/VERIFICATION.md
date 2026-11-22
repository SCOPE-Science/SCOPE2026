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

# Verification of the factor-monitor spectrum

The complete DFA tracks a sixteen-bit seen-factor mask and a suffix of up to three bits. Both executable programs enumerate exactly \(19{,}205\) reachable states by closure under both letters. For each of the sixteen optional patterns, the acceptance predicate is checked against the other fifteen factors. Moore's algorithm refines the finite state set until stable; Hopcroft's algorithm independently refines it by predecessor splitters. Each stable partition is transition-congruent and respects acceptance; Moore's induction yields the exact Myhill–Nerode equivalence. The state counts in `RESULT.md` are asserted for every pattern.

Run from the directory containing both supplied programs:

```text
python3 verify_moore.py
g++ -O2 -std=c++17 verify_hopcroft.cpp -o verifier
./verifier
```

The actually observed terminal lines on the supplied package source files were:

```text
Positive witnesses of length 18: ALL 16 PASS
Moore refinement: ALL 16 EXACT COUNTS PASS
Hopcroft refinement: ALL 16 EXACT COUNTS PASS
```

The Python checker also verifies maximum distinguishing suffix length \(17\) for optional constant factors and \(18\) for all others. Both checkers run with assertions enabled. This is an exact computational proof for a fixed finite graph and an infinite regular-language input domain. It is not a claim about arbitrary larger factor orders, and no independent third-party verification is asserted.
