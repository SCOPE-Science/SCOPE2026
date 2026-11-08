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

# Reproducibility checks and limits

Both included standard-library programs can be run in the same directory with Python 3.10 or later:

```sh
python verify_direct.py
python verify_transfer.py
```

`verify_direct.py` enumerates all \(531441=3^{12}\) assignments on the cuboctahedral graph, counts the minimal monochromatic-bond energies at each favored occupancy, and verifies the three coexistence degeneracies \(3054,2232,689\). An independent recursion counts all cube matchings by size, yielding \((1,12,42,44,9)\), hence \(M_{Q_3}(2)=689\). The same program evaluates \(K_4\), \(K_{3,3}\) and the triangular prism as distinct checks of the general exact-envelope and weighted-matching identities.

`verify_transfer.py` contracts the cuboctahedral model through local three-spin factors on the cube's eight vertices. The exact integer generating function has \(122\) nonzero occupancy/frustration coefficients and total coefficient sum \(531441\); its independently recovered thirteen sector rows coincide with direct enumeration.

Neither verifier certifies the infinite family by testing finitely many graphs. That scope is established by the four local triangle inequalities and a globally proper three-edge-coloring construction in the mathematical proof. These checks do not assess experimental realization, finite-temperature physics or absolute historical novelty. No independent audit has been performed.
