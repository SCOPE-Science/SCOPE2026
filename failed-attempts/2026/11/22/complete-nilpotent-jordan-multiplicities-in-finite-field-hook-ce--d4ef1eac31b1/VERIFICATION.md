---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Using R=k[t]/(tⁿ), the module maps between R and k are respectively evaluation at zero and injection into ktⁿ⁻¹. A centralizing map therefore has diagonal residues f(0),c on the triangular quotient by tR; these must vanish and suffice for nilpotence. For nilpotent maps, the square multiplies R by f²+ab tⁿ⁻¹ and is zero on k. All higher powers multiply R by fᵏ: tⁿ⁻¹f=0, and the square operator annihilates the scalar coordinate and has zero constant residue on R. For 1≤s=vₜ(f)≤n−2, X(tR)=tˢ⁺¹R and X(1,0) adds one independent direction, while X(0,1) lies in X(tR); hence rank X=n−s. The square has rank n−2s if 2s<n−1, otherwise rank zero or one according to f_s²+ab or ab at the stated threshold. The numbers of pairs with prescribed product are q−1 for a nonzero product and 2q−1 for zero, including characteristic two. For f in ktⁿ⁻¹ the image is determined by the two columns (f,b),(a tⁿ⁻¹,0); rank is two with square rank one exactly when ab≠0, zero only for f=a=b=0, and one otherwise. These give the stated residual multiplicities. Jordan reconstruction by second differences and the total qⁿ⁺¹ follow. For n≥4 only s=1 can give (n,1). For each fixed s and large n, the nilpotency index is ceil(n/s); vₜ(f) has the asserted geometric weights up to a vanishing terminal atom, with uniformly geometric tails. Uniform boundedness yields the stated log expectation. The 19 documented checker configurations are finite corroboration, not a proof for all extension fields.

## originality

FAIL

Britnell–Wildon's Proposition 4.4 states support, but its proof already analyzes the actual matrices in explicit coordinates and gives their rank-of-powers profiles by least nonzero coefficient, the product of the two off-diagonal scalars and the vanishing of the square at the threshold. This is stronger evidence than a support-only comparison. The exact threshold square equation and counts are also in the credited square-zero source 50a5542dfb83. Counting the already-described coordinate profiles is a direct free-coefficient count and count of a prescribed scalar product, not a new classification of the fibers. The limit follows from the same earlier rank profiles and the geometric distribution of the first nonzero polynomial coefficient. Separate aggregate tuple counts do not themselves imply this law; the coverage finding is based on the per-element proof, not on those counts or a date inference.

## value

FAIL

Exact similarity-type fiber sizes and a largest-block law are mathematically natural. Here the already classified elementwise profiles reduce all extra weights to free coefficient choices and prescribed products, and the asymptotic statement is the immediate geometric-valuation limit of the same profiles. The frozen result is a useful summary of those consequences, but does not meet the requirement of a distinct exact invariant not mechanically implied by the existing analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
