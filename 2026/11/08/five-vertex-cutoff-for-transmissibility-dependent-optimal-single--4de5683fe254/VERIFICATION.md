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

# Verification

The derivation uses the identity that, for a uniformly chosen seed among the remaining vertices, expected outbreak size equals the expected sum of squared percolation-component sizes divided by the number of remaining vertices. The strict five-vertex comparison is exact, not inferred from a numerical graph search.

The included `verify.py` uses Python 3 standard-library enumeration of all bond configurations. Running `python verify.py` reproduces: 75 labelled simple graphs on one through four vertices; equality of residual polynomials for tied degrees; exact witness polynomials in vertex order \((a,b,c,d,e)\); exact symbolic coefficient difference \(2p^2(1-4p)\) before division by four; and proper containment of a spanning four-vertex path after the other two deletions.

The analytical argument supplies the continuum-in-\(p\) proof. Computation is limited to independent checking of identities on the fully specified finite objects, not a claim of an infinite proof by sampling. The model does not assert equivalence to general stochastic SIR transmission with dependent or directed contacts.
