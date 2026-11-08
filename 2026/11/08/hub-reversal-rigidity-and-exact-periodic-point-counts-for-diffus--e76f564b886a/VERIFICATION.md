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
# Reproduction and bounded checks

The mathematical theorem is the exact integer-diffusion periodic-point count and three-valued hub-change spectrum for every labelled friendship graph with \(r\ge2\), with the single-triangle consistency check supplied separately. Source code and captured outputs are embedded in the same package.

Run `python direct_dynamics.py` with Python 3 and NumPy. This uses a generic graph-edge update, not a lookup of the local-pair proof. It tests all normalized integer states in \([-5,5]^2\), \([-7,7]^4\), and \([-6,6]^6\), respectively \(121\), \(50{,}625\), and \(4{,}826{,}809\) configurations for one, two, and three blades. It checks exact signed hub-movement distributions, including the absence of intermediate nonzero jumps for the final two examples. The proven classification guarantees that no periodic state lies outside the tested bounds in those cases. The expected final line is `DIRECT_EXHAUSTIVE_PASS`.

Run `python local_poly_checker.py` with Python 3 and the standard library. The code enumerates every local two-vertex state satisfying all three edge-reversal conditions for a proposed hub change, builds the possible hub-change polynomial by repeated convolution, and checks all \(1\le r\le14\) against the proposed closed form. Its bounded local domain follows from the proof, not from experimental extrapolation. The expected final line is `LOCAL_POLYNOMIAL_PASS`.

The captured results are supplied as `direct_out.txt` and `local_out.txt`; these were obtained by executing the stated programs from the package source. No finite list, output log, or numerical equality independently certifies the unrestricted theorem. The written mathematical argument supplies the infinite proof. A separate external audit has not been conducted.
