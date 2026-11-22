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

# Reproducible checks and boundaries

`verify_kernel.py` enumerates the complete physically allowed excitation configurations independently of the local-cube proof and constructs the weighted constrained spin-flip Hamiltonian. It compares the exact rational nullity and the vacuum orthogonal spectral projector against the signed-sum formulas for 17 independent three- and four-part cases, including the specified odd-part tuned and detuned examples. All 17 cases passed.

`verify_resolvent.py` constructs the allowed-state adjacency Hamiltonian with a separate enumeration and compares its exact rational scalar vacuum resolvent at three energies with the sum of the local weighted-cube resolvents. All 24 comparisons across eight physical configurations passed.

`CHECKS.txt` contains the full actual success output. Run with `python verify_kernel.py` and `python verify_resolvent.py`, with Python 3 and SymPy available. The two methods differ (kernel/projector versus rational resolvent) and have distinct constrained-configuration constructors. They check finite instances only. The infinite all-size and arbitrary-real-drive result rests on the explicit Walsh and gluing proof in `RESULT.md`. No independent external scientific audit has been performed. All source-priority claims are restricted to examined evidence.
