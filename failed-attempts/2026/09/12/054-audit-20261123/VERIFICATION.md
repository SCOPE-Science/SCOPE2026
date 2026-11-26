---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The exact counterexample is correct for the specified fixed shift and continuous uniform-overlap model. After centering at v/2, the maximum of the two l1 norms for v=beta e1 is ||u||_1+beta/2, so the overlap is a translated cross-polytope of radius R-beta/2. Its volume relative to the original is (1-beta/(2R))^N, and volume equality gives R=gamma1(N!)^(1/N). The box loses beta along just one axis. The conditional-to-original density ratio is constant 1/delta on the accepted support, giving logarithmic Renyi and KL divergences -log(delta). For x=beta/(2 gamma1) and M=(N!)^(1/N), the log inequalities and AM–GM give D2(cross)/D2(box) >= N(1-x)/M >= 2N(1-x)/(N+1) > 1, which also implies strictly lower acceptance. Independent Decimal evaluation of the exact factorial and formulas gives delta_cross approximately 0.9991949648934575 and the acceptance ratio approximately 0.9994923602337981, with divergence ratio 2.70626542764506. The frozen acceptance decimals lose roughly two trailing digits from floating-point subtraction before exponentiation; this does not affect the exact formulas or strict inequalities. FIPS 204 supplies numerical parameters only. The claim does not concern valid signatures, a shared shift-independent target law, all directions individually, or a guarantee about alternative models.

## originality

PASS

Only the exact comparison of these two equal-volume continuous bodies at this fixed axis shift is distinct on the inspected evidence. Neither the overlap-density identity nor cross-polytope masking, the axial covariogram, or polytope rejection sampling in general is new. The related prior rejection theorem and its concrete 1.5 parameter address a different model and performance quantity.

## value

FAIL

The proof shows a valid elementary overlap comparison, but not a substantive tradeoff refutation as presented. A 1.5-fold gain over 0.9997 is impossible for any acceptance probability, and smaller divergence to each body's own uniform law is exactly the same objective as higher acceptance, not a second competing criterion. The genuine strict reversal is a useful worked example but the frozen package establishes no scientifically motivated claim that calls for this particular model and witness: the cited proposal's 1.5 parameter is an unrelated geometric cutoff, and FIPS supplies only dimensions and bounds. The calculation does not test the shift-independent rejection construction in the cited work or an acceptance/security comparison for ML-DSA. No substantive design boundary is established by relabeling the continuous example with standard parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
