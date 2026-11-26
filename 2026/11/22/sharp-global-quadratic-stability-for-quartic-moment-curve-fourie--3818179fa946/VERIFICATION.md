---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For each fixed support multiset the coefficient of its monomial in F_4 is the square of its rearrangement count. The five multiplicity profiles give coefficients 1,16,36,144,576; expanding in elementary symmetric polynomials with e_1=1 gives 1+12e_2+6e_2^2+60e_3+132e_4. When averaging coordinates i,j at fixed sum, write v=theta_i*theta_j and z for the remaining coordinates. Then e_2=e_2(z)+(theta_i+theta_j)e_1(z)+v, and e_r=e_r(z)+(theta_i+theta_j)e_(r-1)(z)+v*e_(r-2)(z). The derivative of e_r/e_2 in v has numerator (6), nonnegative by inclusion of squarefree monomials in the products. Repeatedly averaging a maximum and a minimum decreases squared distance to uniform by half the squared range, so it converges to uniform. Thus (F_4-1)/(2e_2)=6+3e_2+30e_3/e_2+66e_4/e_2 attains its maximum only at uniform for e_2>0; the 3e_2 term ensures strictness. Using 2e_2=1-s_2 yields the displayed c_q=(A_q-1)/(1-1/q), with point masses the only other equality cases and forcing sharpness. In characteristic >4, the four power sums determine the multiset via the invertible Newton recursions. Character orthogonality contributes q^4 to the q^-8 expansion, giving q^-4*(sum |f|^2)^4 F_4=N^4 F_4. The alternative amplitude remainder follows by direct rescaling. This is an analytic check, also covering q=2,3 and zero coordinates; the archived exact rational and complex numerical sanity checks were inspected, not rerun.

## originality

PASS

Best of current knowledge: the exact all-simplex fourth-draw quadratic coefficient and its sharpness are distinct. The baseline uniform extremality, Fourier reduction, and polynomial tools receive no originality credit.

## value

PASS

This gives the strongest global quadratic quantitative rigidity at a natural endpoint beyond the cubic case, improving the known coefficient 6 to an exact field-size-dependent one. The global constant is fixed by one-point-supported amplitudes rather than infinitesimal deviations at uniformity, and the complete equality cases distinguish remainder saturation from extremizers. The matching dimension-free-in-form probability theorem also covers alphabet sizes without a field interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
