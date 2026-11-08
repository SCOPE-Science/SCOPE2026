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

# Reproduction and verification

Use Python 3.9+ from the directory containing `verify_shift_dfa.py`:

```sh
python3 verify_shift_dfa.py
```

The independent finite checks produce the line:

`PASS: 2048 shift/modulus automata; 163840 numerical input checks; 8192-symbol fixed-point checks for 8 alphabet sizes`

The checker enumerates all reachable residual states for each \(2\le m\le9\), \(0\le c\le255\), independently minimizes them using iterative output/transition partition refinement, checks that their count equals \(\lceil\log_2(c+1)\rceil+2m\), evaluates the DFAO on \(80\) inputs including extra zero padding, and generates the substitution fixed point directly for comparison with \(\nu_2(n+1)\bmod m\). The script uses only Python's standard library. The exact all-parameter theorem is proved mathematically in `RESULT.md` by explicit residual classification and separation; finite tests are not the proof.

Limitations: no independent mathematical audit has been performed. The verification does not test most-significant-digit-first representations, alphabet size one, or shifts outside the stated natural-number domain.
