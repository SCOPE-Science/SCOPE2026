---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

From L(u)/b=alpha*u/(1+u²)+r*u/(1+r²u²), derivative sign is cubic P(Y)=alpha(1-Y)(1+r²Y)²+r(1-r²Y)(1+Y)². Positive stationary points lie in 1/r²<Y<1. Solving P=P'=0 with y=u²,z=r²u² eliminates alpha and gives z=(3-y)/(1-3y), A(y) and R(y) for 0<y<1/3. The derivative of log A is -3(y²-6y+1)²/[2y(3-y)(1-y)(1+y)(1-3y)], hence unique threshold per alpha; root continuation gives one vs two maxima, and triple-root symmetry gives quartically flat center. Exact Taylor expansion yields the 2/3 cusp and r_*(alpha)~8max(alpha,alpha^-1). Independently evaluated the older published exact reciprocal wedge at five strength ratios; its thresholds match the new curve, and its cusp converts to K=6.181980515339463 precisely. Finite comparisons corroborate proof, not generality.

## originality

FAIL

Decisively covered by the fully read October 26, 2026 publication 'A sharp loss-peak resolution wedge and cusp law for two Debye relaxations'. It gives the exact iff criterion for two peaks for ALL positive unequal strengths and times, the symmetric equal-strength threshold 3+2sqrt2, reciprocal strength boundaries and sharp 3/2 wedge cusp. Inverting its explicit strength boundaries gives the submitted unique r_*(alpha), 2/3 inverse cusp and extreme-contrast coefficient. The later submission is a reparametrization of the same full phase boundary, not an independent new claim.

## value

FAIL

FAIL as an independent mathematical contribution: although the spectral modality problem and its cusp are meaningful, the later all-parameter threshold, exact asymptotes and singularity are already supplied by a stronger earlier complete wedge theorem. Reversing the dependent and independent parameters and rewriting the 3/2 cusp as a 2/3 inverse cusp does not create a new unknown mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
