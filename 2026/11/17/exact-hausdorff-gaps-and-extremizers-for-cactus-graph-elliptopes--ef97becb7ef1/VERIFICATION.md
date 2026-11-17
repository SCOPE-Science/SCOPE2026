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

# Finite reproducibility and proof boundaries

The standalone `verify.py` requires Python 3.9 or later and no nonstandard packages. Execute `python verify.py` in the directory containing the script. A successful run prints `PASS: 9057 finite numerical and combinatorial assertions` and returns exit code zero. The exact printed check count is obtained by tallying the assertion statements actually evaluated, including the repeated per-edge parity assertions; the program intentionally uses floating-point tolerances for trigonometry.

The checks include all odd-sign patterns for cycle lengths \(3\) through \(9\), a canonical sample through length \(12\), complete enumeration of small cut sign vectors for selected weights, randomized weighted support-function inequalities for lengths \(3\) through \(8\), explicit planar PSD Gram witnesses, exact parity and nearest-point barycenters, the signed-cycle Fourier top eigenvalue, and Pythagorean composition on pairs of cycles with three unrestricted bridge coordinates. All computations refer to coordinates and formulas in `RESULT.md`.

The proof, not these checks, establishes the unrestricted result for every finite cactus. Essential infinite proof steps are: (i) the support formula for even-parity cut signs; (ii) the trace bound from the antiperiodic signed-cycle Fourier spectrum; (iii) uniqueness of its maximizer from unit-diagonal constraints on the top eigenspace; (iv) strictness of the minimum-weight bound away from equal absolute support weights; (v) orthogonal projection of extreme Gram points onto an actual cut facet; and (vi) one-vertex product assembly of cut and elliptope bodies. The no-cycle tree boundary gives zero Hausdorff gap; the triangle is included without an exceptional formula.

Scientific limitations: no independent expert or formal proof audit was performed; the finite tests cannot establish uniqueness in arbitrary dimensions, and historical priority is provisional. Coordinates matter: switching to the conventional \(0\)-\(1\) cut realization divides the reported Euclidean distances by two.
