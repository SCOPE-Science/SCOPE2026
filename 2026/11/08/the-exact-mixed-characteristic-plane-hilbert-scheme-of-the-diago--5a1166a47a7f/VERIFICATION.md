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

# Verification of the plane Hilbert scheme

Run `python3 verify.py` using Python 3 and the standard library only. The printed output is recorded verbatim in `verify_output.txt`. The checker enumerates all projective points and lines over \(\mathbb F_2\) and \(\mathbb F_4\), evaluates the cubic **on whole lines** by testing all four polynomial coefficients, and checks Frobenius orbits and the alternating pairing on each of the 27 surface lines. Results: 15 lines over \(\mathbb F_2\), 27 over \(\mathbb F_4\), 15 rational special planes and six degree-two special plane points, with exactly twelve pairing-nonisotropic geometric planes.

For the characteristic-zero/special comparison, the 15 matching planes are actual integral sections and the special cubic is a smooth-cubic-surface cone by the displayed exact coordinate identity. The first-order obstruction is an **algebraic proof**: its \(tuv\) coefficient divided by two equals \(B(a,b)\) modulo two under *every* Grassmannian perturbation, and no normal derivative can contribute an \(uv\) term multiplied by \(t\). The finite-field checker confirms precisely which of the 27 lines have \(B\ne0\); it does not enumerate all infinite Witt lifts or prove the Henselian local-ring lemma computationally. The Hensel and Nakayama arguments are in `RESULT.md`. An independent audit has not been performed.
