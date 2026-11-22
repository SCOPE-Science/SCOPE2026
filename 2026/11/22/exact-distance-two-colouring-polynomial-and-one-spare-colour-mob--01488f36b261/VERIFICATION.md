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

Two standalone, dependency-free verifiers are included. Run `python3 verify_cyclic.py`; its output includes the eight nonincidence matching numbers, the count of 1740 canonical states, the degree histogram 1596 states of degree eight and 144 of degree fourteen, the 1008/588 return-to-seven split, the 1740-vertex quotient connectivity result, and the chromatic and edge counts. Run `g++ -std=c++17 -O2 verify_binary.cpp -o verify_binary && ./verify_binary` for an independent realization using the dot-product plane over the binary field.

The matching polynomial calculation is a complete 128-subset dynamic program for seven lines, not a sample. The recolouring adjacency calculation is exhaustive over all 1740 canonical colour-name orbits, and two-change generation of all global colour permutations from each shared-colour perfect-matching state supplies the lift to named colourings. The published 2021 mixing theorem gives an independent logical justification of full eight-colour connectedness. Neither script claims to enumerate all 70156800 named configurations individually; the exact lifting factor is \(8!\). No claim is made about exact graph diameter or stationary mixing time.
