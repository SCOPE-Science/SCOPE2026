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

# Reproducibility checks

The two standalone programs require no external scientific data or libraries. The C++17 program `exhaustive_cycles.cpp` is compiled with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic exhaustive_cycles.cpp -o exhaustive_cycles`, then run with `./exhaustive_cycles`. The Python 3 program `cover_certificate.py` is run with `python3 cover_certificate.py`.

The C++ program covers each of the 18,432 labelled states by a direct forward cycle trace, reconstructs a true predecessor for every state, and checks that its independently computed cycle count map equals \(\{18:24,30:24,42:24,66:24,70:72,74:72,78:24,102:24\}\). It ends in `FULL_ENUMERATION_OK states=18432 cycles=288`.

The Python program independently builds the transition permutation, checks equivariance for all 72 extended spatial transformations on every state, then proves exact disjoint coverage from eight specified primitive-cycle representatives. Its final marker is `CERTIFICATE_OK states=18432 cycles=288 symmetry_period_classes=8`. Exact actual outputs are stored in the accompanying `.out` files.

These checks establish precisely the finite torus claim, and are not a proof for larger boards or altered movement conventions. The theoretical argument for reversibility and for symmetry commutation is additionally given in `RESULT.md`. The comparison with earlier literature is limited to the identified sources and does not establish absolute priority.
