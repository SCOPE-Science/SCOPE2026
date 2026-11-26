---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The affine normal form is x=0, y=0, x+y=c with c=0 or 1; changing coordinates on the frequency plane preserves the sum of kernel magnitudes. With the stated q⁻² normalization the complex operator norm is the absolute row sum, attained by a conjugate-phase input. Inclusion–exclusion gives pencil numerator values 3q−2, q−2, and −2 with multiplicities 1, 3(q−1), and (q−1)(q−2). For the triangle the origin contributes 3q−3 and the three punctured exceptional directions each contribute A_q; off those directions the contribution is B_q. Root-of-unity multiplicity q/p and correction for the common origin give A_q=(q/p)U_p(q)−(q−3) for q≥3 and B_q=(q/p)²R_p−3(q/p)T_p+6, yielding the claimed constant correction +12. Independently checked the second moments: on one punctured direction it is (q−1)(q−2)²+3q−5, and off all three it is 3q²−15q+18. Cauchy–Schwarz gives the stated A_q and strict B_q bounds; the gap lower polynomial is positive at q=4 and increasing thereafter. At q=3 the off-direction magnitudes vanish and the triangle numerator absolute sum is 6+6√3; at q=2 the pencil is the whole plane and the triangular magnitudes are 3,1,1,1 before q⁻². The characteristic-two reduction and fixed-p limit follow by the stated root sums; the O(1/q) remainder for U_p follows from cancellation of the real parts of the p-th roots. Read the supporting verification and checker without running the uploaded code. Its finite checks do not underwrite the universal comparison.

## originality

PASS

The operator equals a classical Fourier-algebra indicator norm, and exact adjacent calculations exist. The inspected exact-norm, synthesis and sampling results do not give the classification of both three-line geometries and their sharp comparison. This conclusion is limited to the inspected literature and catalogue.

## value

PASS

Three lines with pairwise distinct directions are the first such line arrangement that can differ by triple incidence; two lines do not have the same concurrency question. Exact sup-norm amplification for the two natural affine orbits, its characteristic dependence and the strictly reversed binary case are useful information not furnished by line counts, a generic coset bound or a rank theorem. The computational burden is not the rationale for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
