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

# Reproducibility and scope

Run `python verify.py` with Python 3 and SymPy. The script computes the exact four signed maximal minors of the specified \(3\times4\) matrix, verifies the degree-six hyperdeterminant restriction, differentiates all six coordinates and checks the characteristic-two reduction to \((x^2,xy,y^2,tx,ty)\). It computes Gröbner reductions that certify the length-three transverse algebra and the length-two odd-characteristic transverse comparator. Its standard output is recorded in `verification_output.txt`. These checks are finite exact symbolic identities rather than enumerations used as an infinite proof. The valuation-based generic inseparability statement and the local chart argument are justified separately in `RESULT.md`.

Independent audit has not been performed.
