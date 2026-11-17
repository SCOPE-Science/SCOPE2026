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

# Verification notes

The included `verify.py` was executed in the current package directory using Python, NumPy and SciPy. It uses a Sobol integration grid inside a fundamental cell to check the predicted two- and three-coverage area fractions. For four Bernoulli failure probabilities it compares direct cell multiplicity averages with the predicted random-erasure area densities. For six distinct finite deletion sets it checks the edge and path counts, and compares exact formulas against direct nearest-surviving-center integration and separately sampled visible arcs of surviving circles. Finally it checks the derived exact area–perimeter relation.

Successful check signal: `HONEYCOMB_ERASURE_AREA_PERIMETER_CHECK_OK 6 finite deletion cases`. The finite numerical tolerance is given in the executable; these tests are illustrative, and rigorous global claims depend on the proof in `RESULT.md`, not quadrature or finite enumeration.

The oldest public-source date in `METADATA.json` follows a precisely dated 2007 bibliography entry for the original honeycomb deployment; a 2006 draft is also reported in a public record, but its exact initial public availability was not verified.

No independent mathematical or historical audit was performed.
