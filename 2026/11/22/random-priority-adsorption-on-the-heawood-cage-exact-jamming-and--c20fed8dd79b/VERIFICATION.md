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

The accompanying `heawood_rsa_check.py` is a complete, executable, Python-standard-library-only verification script. It enumerates exactly all 16,384 vertex subsets and all 37 maximal independent sets of the Fano incidence graph, calculates each specified output probability using exact polynomial simplex integrals, and independently calculates the terminal distribution by a residual-graph rational dynamic program. The two probability calculations agree in every asserted rational entry. It also evaluates the exact 15-coefficient finite-time mean-occupancy law and checks the density, amplification and total-variation claims.

The certificate is exhaustive for this fourteen-vertex finite graph, not for arbitrary graphs or asymptotic claims. The previously established infinite cubic-tree density is cited as external literature and is used only as a comparison. Independent mathematical audit has not been performed.
