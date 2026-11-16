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

Two complete exact integer computations are supplied. `verify_walsh.cpp` enumerates undirected Hamiltonian paths and performs the Walsh butterfly. `verify_zeta.cpp` independently enumerates linear-forest forced-edge subsets and performs a subset-zeta transform. Their complete \(38\)-level absolute histograms agree, and their global counts agree with Parseval. The standard-library Python dynamic program `verify_dp.py` additionally checks the path enumeration and a signed cancellation witness. The verification is finite at nine graph vertices; no general infinite-order assertion is claimed. A separate independent scientific audit has not been performed.
