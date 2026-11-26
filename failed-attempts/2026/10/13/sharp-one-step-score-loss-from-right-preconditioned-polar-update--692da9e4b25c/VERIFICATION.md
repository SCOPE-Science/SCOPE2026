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

Put X=GB⁻¹=P₁Y with Y=(XᵀX)^(1/2) positive definite. Then G=P₁YB; the two denominators equal tr B and the alignments are tr(YB)>0 and ||G||*=||YB||*. Thus the ratio is exactly (tr(YB)/||YB||*)². The thin polar maximizer is unique at full rank, so upper equality means P₀=P₁, equivalently YB is symmetric positive definite. This is equivalent to H=(GᵀG)^(1/2) commuting with B: in one direction H=YB when YB is positive definite; in the other direction GB⁻¹=P₀HB⁻¹ has positive definite right factor. For each unit v, put a=vᵀBv and b=vᵀB²v. The endpoint polynomial gives b≤(L+μ)a−Lμ, and a²−[4Lμ/(L+μ)²][(L+μ)a−Lμ]=(a−2Lμ/(L+μ))²≥0. Expanding Y=Σσⱼvⱼvⱼᵀ gives tr(YB)≥[2√(Lμ)/(L+μ)]Σσⱼ||Bvⱼ||≥[2√(Lμ)/(L+μ)]||YB||*, which proves the lower bound. For B=diag(1,κ), v=(√κ,1)/√(1+κ), take Yε=vvᵀ+ε(I−vvᵀ). It is SPD for all ε>0; in the rank-one limit the trace and nuclear norm tend to 2κ/(1+κ) and √κ. This supplies full-rank sharpness by continuity. The lower bound is strict at full rank for κ>1: the alternative bound ||YB||*≤√(tr Y tr(YB²)) is Frobenius Cauchy–Schwarz applied to Y^(1/2)Q and Y^(1/2)B at the maximizing square orthogonal Q. Equality requires B to be proportional to Q, hence scalar by positivity, and the normalized spectral weights give (tr(YB))²≥[4κ/(1+κ)²]tr Y tr(YB²). For scalar B the ratio is one. Expanding the positive quadratic along the direction and completing the square gives decrease S_B/2. An independent diagnostic at κ=4 and ε=0.1, 0.001, 10⁻⁶ found ratios 0.763407707911, 0.641437929468, 0.640001439998, against 0.64; the commuting test gave one. The claimed all-input inequality is analytic, not certified by these checks or the recorded verifier output. The uploaded script was not executed.

## originality

FAIL

Demonstrable older coverage, not a search or access failure. Bourin (2006), Corollary 2.6, bounds every singular value of AZ by ((a+b)/(2√ab)) times its corresponding positive eigenvalue, for A≥0 and Z>0 of extreme eigenvalues a,b. In the record write GB⁻¹=P₁Y. Then the score ratio is exactly the square of the eigenvalue sum divided by the singular-value sum of YB. The specialization A=Y, Z=B and summation therefore give the same lower bound directly from a stronger result. Bourin's rank-one sharpness already gives the limiting family by continuity in real dimension two. The upper endpoint and its commutation test follow from uniqueness of the ordinary polar maximizer. The optimizer framing does not make these facts a distinct sharp inequality.

## value

FAIL

The named optimizer comparison is a natural question, and the interpretation can be useful as exposition. But with the score normalization common to both directions, the claimed sharp invariant is an immediate trace specialization of the known stronger singular-value bound with its existing rank-one sharpness mechanism. Full-rank approximation and polar commutation add no separate substantive fact here. No noncovered comparison, such as one with anisotropic output curvature where the denominators differ, is proved in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
