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

The standalone `verify.cpp` and `check_interfaces.py` were executed from their included source files. Outputs appear verbatim in `verify_output.txt` and `interfaces_output.txt`. Compile/run commands: `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify`, followed by `python3 check_interfaces.py`. All integer counts and interface identities matched. Source files use no external packages and no data files.

`verify.cpp`: complete finite state spaces for rings of size 3 through 10, and all positive iterate times through the circumference; independently checks the proposed recurrent-sector classification and the exact counts. `check_interfaces.py`: all 64 local edge triples, all ring states through length eight, nonincreasing interface count and collision-free propagation condition in equality cases. The finite checks do not establish an all-length claim or historical novelty. The all-length argument is in `RESULT.md`.

Scientific scope is limited to the four-color synchronous ring rule. Independent external mathematical audit: not performed.
