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

The local phase criterion reduces the four-state graph dynamics to successor-neighbor color assignments. `verify_transfer.py` reconstructs the complete 256-state transfer graph, the five recurrent components, all four 40-state Fourier blocks, and tests the exact four symbolic characteristic polynomials with SymPy; it also checks the all-length formula against direct transfer traces at ten distinct ring lengths, from three through twelve. The program was run successfully.

`direct_check.cpp` is an independent microscopic state-update implementation. Compiled with a C++17 compiler, it exhaustively compared every state on three-, four-, and five-rung prisms and found the specified 120, 264 and 2120 primitive-four periodic configurations. It was run successfully. These finite checks are not an all-length search: the infinite-family statement follows from the exact transfer determinant certificate and the phase-local proof. There is no independent external validation.
