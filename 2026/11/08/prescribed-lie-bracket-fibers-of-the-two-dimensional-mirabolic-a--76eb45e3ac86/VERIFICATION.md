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

# Verification

The theorem is proved by centralizer and rank-one-image arguments in `RESULT.md`, not by extrapolation from finite samples. Execute the two Python-standard-library checkers next to this document:

```sh
python check_aff2.py
python check_aff2_extension.py
```

`check_aff2.py` directly multiplies each pair of six-coordinate mirabolic elements over \(\mathbb F_2\) and \(\mathbb F_3\). It examines exactly \(4096\) and \(531441\) input pairs, then checks every target, including targets outside the trace-zero hyperplane. `check_aff2_extension.py` uses explicit polynomial arithmetic modulo a quadratic irreducible polynomial in characteristic two to implement \(\mathbb F_4\); it enumerates all \(65536\) first matrix pairs and computes translation image spaces, testing all \(1024\) target pairs, accounting for \(16777216\) inputs. Their output appears in `verification_output.txt`.

The programs are distinct: the first directly enumerates all translation pairs; the second computes images and ranks to sum over translations. Finite computations cannot certify a statement about all prime-power fields or publication priority. Independent audit status remains not performed.
