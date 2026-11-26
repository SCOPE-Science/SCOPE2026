---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The signed edge-gradient map identifies the quotient by constants with the zero-sum hyperplane. Differentiating there gives the stated two-dimensional block on opposite gradients and decay e^(-2t) for the side-edge difference. The intersection of the unit cube and the hyperplane has only the six two-plus/two-minus vertices. On those vertices the opposite-edge row norms are X+(2-r)Y and X+rY and the side-edge norms are Z+|r-1|Y in the notation of the proof. The other vertex type gives strictly smaller magnitudes for all four edges at positive time. Comparing Z with X+Y using the power series gives the claimed strict edge-selection rule. The vertices maximizing each signed row give its whole exposed face, including the segment for a weak edge and the unweighted degeneracy. At t=0 all functions extremize. For r<1 the derivative is a difference of two exponentials with negative initial derivative and the negative term decaying slower. For r>1 the sign of the derivative is obtained from the bracket in RESULT.md lines 112–117: the bracket falls from 2D_r to a negative minimum, then approaches zero from below. This proves the strict threshold and uniqueness of the peak. Each finite r gives norm strictly below 3/2, whereas t=(log r)/r sends the two relevant exponentials to 1 and 0 respectively as r grows. On a triangle the gradient norm is the oscillation and cannot increase under Markov averaging.

## originality

FAIL

An earlier distinct Resultary record gives the identical sharp all-time profile with the same counting measure, conductance defect, and fixed unit metric, as well as the threshold 3 and unattained envelope 3/2. Its explicit signed-edge optimization already supplies the coefficients and inequalities that specify the equality faces by saturation. The stated strict unimodality is a further explicit observation, but follows by differentiating the already known two-branch formula and comparing two exponentials; it does not make the submitted exact profile and transition original.

## value

FAIL

The model and sharp profile would be worthwhile in isolation. In this record the profile, threshold and envelope recompute known exact results, and the remaining strict faces and peak shape use respectively saturation and differentiation of the prior proof and formula. No independently motivated unknown invariant survives as presented.

The dated certificate retains the supplied scientific assessment, sources and limitations.
