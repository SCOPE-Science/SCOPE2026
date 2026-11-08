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

# Reproducibility and boundaries

Execute `python3 check_desargues_integral.py`. It requires only Python's standard library. The expected exact output is `verification_output.txt`.

The certificate checks the 20 vertices, 30 edges and 6,212 independent faces; all 30,380 oriented incidences of the complete augmented face poset; 3,103 matched pairs and the complete acyclicity topological sort; all five induced six-edge matchings and their 64-term integral cycles; vanishing signed boundaries; maximality of all five detecting 5-simplices; the integral identity pairing matrix; and chain-level actions for all 120 label permutations on five cycles plus complementation.

The rank bound is an application of integral discrete Morse theory to the completely enumerated finite complex, not a guess based on field ranks. The five unit pairings demonstrate a primitive integral basis, not just rational linear independence. The 1979 source supplies only a month of first publication; the first exactly day-verified public online version of that source is 2004-10-19. No day is imputed to the earlier 1979 print publication. The method is a finite graph-specific calculation, not an all-parameter theorem. Independent assessment of mathematical novelty has not been performed.
