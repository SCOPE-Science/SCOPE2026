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
# Verification details

`verify.py` uses successive Euclidean divisions for factorial digits. It exhausts the closed state interval \([1,40319]\), reports all cycles, checks the two translations for every periodic point and prints the complete paths into both targets. `verify_greedy.py` reconstructs each factorial expansion by descending factorial weights and independently enumerates the cycles and both translations.

The required independent checks are obtained by running:

```sh
python3 verify.py
python3 verify_greedy.py
```

The recorded outputs are stored in `witnesses.txt`; the first program should finish with `verification=PASS` and the second with `independent_greedy_check=PASS`. No special libraries, network calls, probabilistic assumptions, or external certificates are required. Scientific verification is limited to the displayed elementary proof plus repeatable finite arithmetic; an external independent audit has not been performed.
