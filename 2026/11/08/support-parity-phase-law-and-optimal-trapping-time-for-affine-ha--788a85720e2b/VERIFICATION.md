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

# Reproducibility and scientific limits

Run `python verify.py` after installing the dependencies in `requirements.txt` using a compatible Python 3 interpreter. The verifier constructs the full non-Hermitian hypercube propagator and compares its squared norm against the independently implemented scalar two-level expression. It checks all initially untrapped vertices in small cubes for several positive loss strengths and times and both affine shifts of a non-coordinate parity detector.

A separate Lyapunov-equation solve tests every nonzero singular mode through support size twenty; direct matrix ranks verify the dark-space count through support size ten. The recorded successful execution reported 1207 independent full-matrix/time comparisons and 220 Lyapunov-mode checks, and checked dark ranks at all sizes from two through ten. Large-support binomial sums were also evaluated at 1000, 1001, 4000 and 4001 to corroborate the two local-limit constants, without treating these tests as proofs.

The infinite result follows from exact tensor reduction, the Walsh spectrum, the dissipative Lyapunov identity and a uniform local central-limit argument. The numerical checks are finite; they do not establish an unbounded claim by enumeration. The theorem assumes uniform hopping, identical trap strengths and an entire affine parity hyperplane. The even-support conditional mean excludes the permanent dark-state survival mass. Historical originality is provisional, and independent audit has not been performed.
