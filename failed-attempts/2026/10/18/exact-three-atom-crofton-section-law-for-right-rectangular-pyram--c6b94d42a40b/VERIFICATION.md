---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Haar motion-invariant affine-plane measure is spherical area times offset length; the quotient by orientation reversals cancels. For A=a|u_x|+b|u_y| and B=h|u_z| the directional width is 2A+(B−A)_+, so the integrated width is 4π(a+b)+8J=4Z with J the positive-octant excess integral. For azimuth φ and v=a cosφ+b sinφ, the elevation integral gives [h−v arctan(h/v)]/2. The remaining integration by parts uses v″=−v, v²+(v′)²=a²+b² and the two endpoint terms. With s=tanφ the quadratic denominator completes a square with determinant h²D², giving arctan(hD/ab)/(hD) and the stated J. A planar cut cannot separate the two opposite pairs of base vertices, since the diagonals meet. A 2/2 adjacent base split cuts two base edges and two spokes; a 1/3 split cuts two base edges and either one or three spokes. Thus precisely the lone base vertex sharing its side with the apex can lead to five crossings. The positive-octant height interval gives (B−|au_x−bu_y|)_+−(B−A)_+. Shifting the azimuths of the plus and minus projections and folding their absolute cosines gives J_-+J=2J(S,0,h)=π(D−S)/2, using the continuous b=0 limit of the excess formula. This yields the displayed p₅. For any edge of length ℓ the integrated offset length is 2πℓ, giving the stated mean and fixing p₃,p₄ by normalization. Base-corner clipping, apex clipping and an open interval of five-edge cuts near au_x=bu_y ensure strictly positive masses in all three classes. The two shape parameters really vary independently: write v=S/(a+b) and k=h/(a+b). For a nonsquare base near k=0, p₄=2v−1+O(k³), and EN=2(1+v)+k²/v+O(k³), analytically, so the Jacobian in (v,k) is nonzero for sufficiently small positive k. The limiting flat pyramid is not in scope. Independent replay `python3 /workspace/review_checks.py 3` sweeps every offset interval in each of 360² equal-area orientation cells for each of three shapes; the largest discrepancy is 5.05×10⁻⁶. This is quadrature corroboration, not proof. Frozen verification material and checker were inspected, not executed.

## originality

FAIL

The exact motion-invariant rectangular law on the entire domain a,b,h>0 is separately supplied by the Nov. 8 catalogue result, with the same width and mean and an exact integral for the remaining free probability. Its denominator is the frozen Z. To see that the extra quadrature is a directly reducible presentation, put I_±=∫₀^{π/2}c_± arctan(h/c_±)dφ in the notation of that result. Its pentagon numerator is I_+−I_−. Folding the two azimuth phases around the absolute cosine maximum gives I_++I_−=2I_+(S,0,h); also I_+(a,b,h)=πh/2−2J_frozen from the support-width identity. Substitution of the width formula, also valid in its continuous b→0 limit, reduces the pentagon numerator to π(D−S)−4J_frozen. The same mean then fixes the entire vector. Thus the frozen elementary formulas are an evaluation of the covered law, not a second invariant. The exact square specialization is independently in a distinct same-day record. This is verified equivalent catalogue coverage, not a historical priority determination. Voss is a material historical risk, not the basis of the verdict.

## value

FAIL

The complete motion-invariant section-type law is a natural stereological invariant and genuinely depends on shape. The scientific invariant itself is already exactly decided by the covering rectangular law; the elementary version is obtained by phase symmetry and evaluating the already explicit width formula at a boundary. It does not add an independent classification, structural constraint, or an exact invariant beyond the coextensive source.

The dated certificate retains the supplied scientific assessment, sources and limitations.
