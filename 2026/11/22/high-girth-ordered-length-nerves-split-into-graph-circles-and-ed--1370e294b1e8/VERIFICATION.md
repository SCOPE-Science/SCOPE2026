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

## Reproducing the finite corroborations

Run `python3 checks/length_three_checker.py` with standard Python 3. No external libraries or remote services are required. The output should match `checks/check_output.txt`, including `ALL FINITE CHECKS PASSED`.

The program enumerates normalized ordered simplicial cells, verifies the integer chain identities \(\partial^2=0\), verifies closure of the integral alternating-edge top cycles, and computes all homology dimensions over two different prime fields. Checks cover girth-seven and longer graphs at cutoff three, a figure-eight and a tree, and cycles at cutoffs four and five. Short-even-cycle boundary tests show additional intermediate homology at the forbidden girth threshold.

## Mathematical verification and limits

The infinite theorem is not inferred from those computations. Its proof has three independent mathematical ingredients: the published exact-length magnitude homology of trees and the explicitly reconstructed length-one spectral differential; the coherent unique-geodesic lifting of ordered simplices under the strict girth inequality; and the universal-cover homology comparison upgraded by Whitehead's theorem. The hypotheses and the parity sign on every edge cycle are stated in RESULT.md.

The finite-field tests do not certify torsion-freeness for arbitrary inputs. That integrality follows instead from the primitive chain calculations on trees and the universal-cover argument. There is no independent audit or external certification.
