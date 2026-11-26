---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Assessed the corrected /workspace/repairs/3/RESULT.md. The frozen line 48 infers that f_a*f_b is C² merely from an integrable second weak derivative of f_b; when f_a is only L¹ that does not establish continuity or pointwise evaluation at overlapping singular endpoints. The replacement supplies the missing estimates: for 0<a<1 and b>2, choose conjugate finite P,Q with 1/P>1−a and 1/Q>max(0,3−b), possible exactly under the sufficient total-rate condition a+b>3 in the singular b<3 subcase. Hölder and continuity of translations in L^Q give continuous derivatives through order two. For both rates above one, the second derivative is f_a' * f_b' and the analogous endpoint exponents max(0,2−a), max(0,2−b) sum to less than one. At a=1, b>2 makes f_b continuously differentiable through its support endpoints and gives p''(0)=0. The stationary center calculation cancels the interaction exactly; the single filter's two stationary orientation fluxes vanish at the endpoints, giving the normalized beta law with no boundary atoms. The half-sum has density 2(f_a*f_b)(2z), so its curvature is 8 times the centered differentiated convolution. Pairing the two terms and using B(3/2,s−3)=B(1/2,s−2)/(2(s−3)) gives the claimed positive coefficient for the mixed sector. Positivity, the strict central minimum and zero edge values force an interior maximum on each side by compactness. For a,b>1 the odd-derivative pairing yields a strictly negative integral at every positive interior argument; the uniform case has an explicit strictly negative derivative. Substitution x=1−2εt on the convolution interval gives factors 4εt and 4ε(1−t) at leading order and an integrable beta weight, proving the endpoint coefficient independently for every positive a,b. This also settles the equal-rate comparison directly: a=b=2 gives coefficient 6 and exponent 3. Only RESULT.md is corrected; the independent argument establishes the continuum theorem, not the frozen finite output.

## originality

PASS

Reassessed the repaired statement. Force cancellation, beta filter marginals, the immediate convolution representation and its routine endpoint scaling are not the basis of the pass. The distinct claim is the exact mixed-rate curvature and the resulting sharp central minimum versus unique maximum dichotomy for a+b>3. No inspected stronger result implies that threshold by merely reparameterizing. The proof repair justifies the relevant derivative without changing the mixed-rate prediction.

## value

PASS

The repaired proof yields a quantitative phase boundary for an interaction-independent collective observable. An arbitrarily large total switching rate does not prevent loss of a central peak when one rate is sufficiently slow. The exact positive curvature certifies that change throughout a natural open parameter sector, rather than presenting a single numerical example or just the standard filtered-heading convolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
