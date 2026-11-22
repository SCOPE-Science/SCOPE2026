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

The proof is analytic. For any nonnegative edge investment vector, directly enumerate every pair of path vertices and multiply the independent transmission probabilities of the intervening edges; this gives \(1+2F/n\) for expected burned patch count. The sum of interval exponentials is strictly convex because its Hessian quadratic form contains the positive length-one terms \(e^{-g_k}v_k^2\). Check the gradients of the proposed center-only or center-pair solutions against all zero-investment edges using the simplex first-order inequalities. This is a global certificate, not a local numerical optimum.

Run `python3 check_firebreak.py` from the directory containing the complete files. Python 3 standard library suffices. The script reports `PASS 6952 finite/exact checks` and independently exhausts bond outcomes through eight patches, tests exact-rational gradient identities through half-size twelve, compares the four-patch closed reduction with dense grids, and checks positive Hessian quadratic forms at representative vectors. These computations are finite and do not substitute for the all-size proof.

The theorem does not verify the exponential width-to-transmission law experimentally, nor address heterogeneous fuel, unknown sources, multiple ignitions, fire jumping gaps, fire intensity, or a general post-threshold support characterization. Historical novelty is based on an inspected but nonexhaustive publication comparison. No independent audit or external certificate is claimed.
