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

Uniqueness of the degree-four rule follows by testing each of the five cardinal polynomials; exactness follows by expanding any degree-at-most-four polynomial in those cardinals. The five L_j were independently constructed from their product formulas, and clearing ∏_{i=1}^5(k+i) verifies the five reported moment identities as polynomial identities in k, not just at a sample. The resulting signs are positive for j=1,3,4 at every integer k≥0, positive/zero/negative for j=0 at k=0,1,≥2 respectively, and positive through k=2 then negative for j=2. The absolutely convergent exponential series therefore gives strict positivity for j=1,3,4. W_0 is strictly decreasing on (0,∞) and goes to −∞ by bounding its negative tail by the k=2 term alone. W_2/λ² is strictly decreasing there: its k=0,1 terms decrease, its k=2 term is constant, and all k≥3 negative terms decrease. It tends to −∞ by bounding the negative tail by the k=3 term alone. Both unscaled weights start positive, so each has one unique positive zero. The independent standard-library rational replay reconstructs M_0=1957/90, M_2=1142/15 and checks e⁴<55 with a geometric tail. It certifies |W_j(z)−P_{j,N}(z)|≤55 M_j z^(N+1)/(N+1)! and compares rationals, certifying W_0(63/20)>0>W_2(63/20) with N=30 and the signs (+,−) at both stated rational brackets with N=42. The positive comparison margins at the four endpoints are about 4.42e−7, 4.87e−7, 1.26e−7 and 1.34e−7 respectively; decisions used fractions, not these decimal renderings. Reflection L_j(1−x)=L_{4−j}(x) gives W_j(−λ)=e^(−λ)W_{4−j}(λ), including the stated index reversal and the inclusive and strict positivity intervals. At zero the reconstructed weights are classical Boole weights, and symmetry gives the extra degree-five exactness. The frozen verify.py was inspected, not executed. Independent replay: python3 /workspace/branches/aacad24e-17f3-4a24-85ca-91af4e6d5124/check_record2_exact.py; check_record2_exact.out in the same directory records the exact assertions' successful run.

## originality

PASS

Pass the full sign classification as a function of exponential tilt at the fixed interval stencil, not the classical Boole stencil, the general formula for interpolatory weights, or the unweighted coefficients. The inspected closest matches vary nodes or order under different exactness spaces and densities. The general construction determines each weight but gives neither the all-tilt sign control for three weights nor the number and order of positive roots. This is a bounded, best-of-knowledge decision, with the inaccessible paper explicitly unresolved.

## value

PASS

Nonnegative quadrature weights are exactly what preserves positivity of arbitrary nonnegative nodal data, and their loss permits a negative output for some such data despite the strictly positive integrating density. On the standard five-node Boole stencil, the largest allowable exponential tilt and the identity and order of the failing nodes are therefore meaningful, independently useful facts. The complete classification and certified sharp bounds are more useful than example weights at a few tilt values. This is not evidence of a general error advantage or of node-set optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
