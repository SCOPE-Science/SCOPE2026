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

Condition on |A|=u>0 and rotate input and output. The map z^2-u zbar is proper of degree two and its critical circle has radius u/2. The critical value curve has nonzero radius and strictly monotone lifted argument (derivative vanishes only at the cusps), with one clockwise turn. This gives one bounded and one unbounded regular region; simple roots at zero and degree at infinity give four and two respectively. The Gaussian target avoids the caustic. The rotating phase preserves the conditional circular target law. Integrating the unit exponential |A|^2 gives the stated Laplace transform with strictly positive rate, which proves strict derivative signs. Changing argument to boundary parameter and integrating the Rayleigh variable gives the erfc expression. Expanding at small noise uses bounded reciprocal radii and finite Rayleigh moments; the first two angular moments give the stated elliptic expression and 2/3. At large noise the area and second area moment of the deltoid are 2 pi and 3 pi, and the exponential radial dilation moments give 1/4 and -9/32. The supplied checker.py was inspected, not run. The independent area-formula quadrature inside the negative-Jacobian disk in python /workspace/reproductions/reproduce.py gave p(1)=0.14635487513720 and independently reproduced the two large-noise coefficients.

## originality

FAIL

Demonstrably covered as a specialization of the earlier Resultary finding 9c1cf2345cea. The probability law, asymptotics and complete monotonicity in the new parameter are already explicit or immediate in its general probability representation. Re-expressing a radial moment by standard elliptic integrals does not rescue the frozen finding.

## value

FAIL

The four-zero probability is a motivated benchmark, but the earlier general law already yields it, its two noise limits and its strict derivative signs directly. The remaining change of notation, standard elliptic evaluation and sample decimal do not supply a distinct useful result that merits a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
