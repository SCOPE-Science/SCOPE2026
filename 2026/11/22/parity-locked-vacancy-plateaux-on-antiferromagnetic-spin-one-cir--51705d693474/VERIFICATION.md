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

# Reproduction and boundaries

Two standalone programs are provided. Run both in a directory containing the corresponding files using Python 3 and its standard library:

```
python verify_prism_dp.py
python verify_prism_bruteforce.py
```

`verify_prism_dp.py` computes the exact finite-size minimum energy and the full occupancy-resolved degeneracies using rational dynamic programming over the nine possible spin pairs on each rung, with a periodic closure. It compares the analytical classification at 300 parameter instances over \(3\le n\le12\), five strictly positive rung ratios, and fields across the proposed boundary values. It passed.

`verify_prism_bruteforce.py` independently enumerates all \(3^{2n}\) spin configurations at each of 48 exact rational parameter instances for \(n=3,4,5,6\), compares ground energy and all occupied-spin counts, and passed. Its algorithm directly constructs the Hamiltonian by leg, rung and onsite contributions rather than using the frustration-square identity.

Critical mathematical checks beyond finite computations: the odd lower-bound \(F+2z\ge8\), its complete equality configurations, the odd upper-bound \(F\ge2K/(n-1)\) and its equality configurations, and the connected-bipartite zero-cost criterion in even circumference are explicitly proved in `RESULT.md`. The assertions for arbitrarily large \(n\) follow from those arguments, not from the verified finite cases.

The calculation is restricted to the stated uniform zero-field classical Hamiltonian with strictly positive rung coupling. No independent audit of the science or historical priority has been performed.
