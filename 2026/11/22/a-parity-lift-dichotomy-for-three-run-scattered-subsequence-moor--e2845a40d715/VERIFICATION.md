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

# Verification of the three-run parity Moore-counter theorem

The claimed machine reads binary inputs and outputs the parity of positional scattered occurrences of \(0^a1^b0\). The all-parameter proof in `RESULT.md` supplies the exact phase period, the reachable base orbit, explicit bit-independence witnesses or exceptional invariant, and distinguishing suffixes. The programs below are finite, independently implemented supporting checks, not exhaustive proofs of the infinite domain.

Run from the directory containing the files:

```
python3 check_prefix_automata.py
python3 check_phase_witnesses.py
```

The first implementation maintains a complete vector of all prefix-pattern counters, applies one-letter subsequence recurrences, and breadth-first enumerates the reachable full vectors. It checks every parameter pair \(1\le a\le11\), \(1\le b\le6\), independently minimizes the reachable Moore machines for \(1\le a\le5\), \(1\le b\le4\) by output partition refinement, and compares dynamic-program parity against literal positional embeddings for lengths at most eleven. Captured output:

```
PASS orbit_cases=66 visited_states=26604 minimized_cases=20 literal_checks=65520
```

The second implementation maintains the compressed phase, middle-run vector and final parity directly, and checks explicit same-base opposite-parity witnesses, a complete family of distinguishing suffix signatures on each enumerated state, and the combinatorial exceptional-identity formula on a broad finite domain. Captured output:

```
PASS witness_pairs=4914 signature_cases=40 signature_states=7148 invariant_checks=877440
```

The corresponding `.out` files contain the literal captured results. No randomized oracles, external solvers, undisclosed certificates, or independent audit are involved. The proof does not rely on any bounded computation being mistaken for all-length exhaustiveness.
