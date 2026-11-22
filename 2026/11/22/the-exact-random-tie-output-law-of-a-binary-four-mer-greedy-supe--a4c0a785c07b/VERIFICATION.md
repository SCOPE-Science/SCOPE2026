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
# Exact verification

`verify_paths.py` evaluates the probability generating polynomial on 428 canonical endpoint-path states, without sampling. `verify_strings.py` independently enumerates 418 canonical literal-merged-string states. Both use Python `fractions.Fraction` and enumerate **all** ordered maximum-overlap ties at each stage. Their output files give every exact rational probability and the total mass one; their tables coincide at each of the seven lengths. For the stated input, the length-11 witness is checked by the eight-factor list, and the elementary factor-position lower bound proves optimality. Neither computational proof addresses other inputs; no independent third-party audit has occurred.
