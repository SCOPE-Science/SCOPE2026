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

# Verification record

The complete mathematical statement and its unrestricted proof are in `RESULT.md`. The standalone Python 3 program `check_triple.py` is a reproducible arithmetic checker, requiring only the Python standard library. It uses `fractions.Fraction` throughout; no floating-point tolerances or external data are used.

Reproduction command:

```sh
python3 check_triple.py
```

Observed output from the actual packaged source before embedding:

```text
exact base-two breakpoint certificate: 11 candidate breakpoints
exact rational universal-regime spot checks: 174
PASS: exact rational checks completed
```

The eleven breakpoint values result from all possible crossings of endpoint lines for the three integer frequencies \(1,3,7\). Between successive breakpoints, the intersection measure is affine, so equality at all of them establishes the entire base-two piecewise law. The finite checks for \(2\le a\le30\) are diagnostic only and do not replace the unrestricted signed-coordinate proof. Neither formal proof-assistant verification nor independent review has been performed. The result does not imply an infinite-time distribution law.
