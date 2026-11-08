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

# Reproduction

Use Python 3.10 or later with no third-party dependencies. From the directory containing the files, run:

```sh
python3 check_reset_neutral.py
```

The included checker was executed against the actual source and printed:

```
PASS: 2382 exact rational assertions (full absorbing chains, pgfs, exit laws, ordering).
```

It independently solves the complete finite absorbed Markov systems by rational Gauss–Jordan elimination. It checks domain sizes 4, 5, 6, 7, 8, 9, and 10 with the specified rational parameters, exact exit probabilities, conditional transforms and strict pair rankings. It does not certify the analytic proof over arbitrary domain sizes or real-valued parameters. Those claims depend on the explicit linear-recurrence and renewal arguments in `RESULT.md`. In particular, neither finite testing nor failure to locate a prior statement establishes independence or historical priority.
