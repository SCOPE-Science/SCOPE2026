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

# Exact verification and scope

From this directory run:

```bash
python3 verify_terminal.py
python3 verify_kinetics.py
```

The scripts require only Python 3 standard-library modules. The terminal script enumerates every reachable residual free-site mask and uses `fractions.Fraction` for the exact probabilities of all labeled terminal independent sets. It also independently verifies valency and common-neighbor counts, maximality and residual four-site graph types. The kinetics script uses a separate subset recurrence over every integer mask in \(0\le m<2^{16}\), with exact rational sums by subset cardinality. It checks all differences against `KINETICS_COEFFICIENTS.csv` values as built-in constants, and independently enumerates all \(inom{16}{4}\cdot 24\) ordered four-site arrival scenarios on each graph.

The two expected success markers are `SHRIKHANDE_ROOK_TERMINAL_OK` and `SHRIKHANDE_ROOK_KINETICS_OK`. The positive coefficient table, not a numerical plot, proves strict expectation separation for all positive times. The absorbing terminal distribution is a finite exact law; no unexamined higher-dimensional or infinite-graph conclusion follows.

No independent scientific audit has been performed. Full text of the earliest foundational graph RSA reference (Pippenger, 1989) was unavailable, so bibliographic priority remains uncertain.
