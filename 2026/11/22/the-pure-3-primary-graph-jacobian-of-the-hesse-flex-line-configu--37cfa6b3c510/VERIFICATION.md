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

# Verification scope

Run `python3 verify_hesse.py` with a standard Python 3 installation. There are no package dependencies, network calls, or unstated inputs. The checker builds all nine points, twelve incidence triples, 21-by-21 integral Laplacian entries and six 20-by-20 reduced Laplacians. It verifies the affine-plane triple characterization, the 9-by-9 incidence Gram matrix, the graph's 36 edges, six full exact 3-adic Smith diagonals (precision \(3^6\), all actual valuations at most three), six exact fraction-free integer determinants, and their agreement with the spectral tree count.

The arithmetic checker does not mechanize the general existence of stable nodal curves or the standard Néron component-group comparison: these are cited mathematical results used under explicit hypotheses. The checker is a finite exact certificate, not evidence that all earlier literature has been exhausted. The scientific review is same-model; independent audit has not been performed.
