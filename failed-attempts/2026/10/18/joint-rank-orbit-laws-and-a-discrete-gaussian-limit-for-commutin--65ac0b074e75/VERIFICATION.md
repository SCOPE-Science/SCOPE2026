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

The product E fixes its own image and f_iE=E for every i, so c=E(0) is a common fixed point. Writing x=c+y yields commuting linear projections. The products of P_i or I−P_i are pairwise orthogonal, sum to I, and identify labelled simultaneous eigenspaces in every characteristic. Their dimensions determine the linear conjugacy class; the stabilizer is block diagonal. Centers giving the same affine parts differ by the all-ones block, so there are q^{n−d_[k]} affine offsets and all are translation-conjugate. This proves the orbit formula. The product indexed by T is identity precisely on the blocks containing T and zero on every other block, giving the affine ranks and generating monomials. Regrouping monomials by block gives the product series; for k=2 the dimensions are (n−a−b+c,a−c,b−c,c). At n=2, the single nonzero block contributes 1+3q² and the two unit blocks contribute 3(q+q²)q(q+1), giving the displayed total. Independently enumerating the 64 affine maps of F_2² as functions gave 17 idempotents and 121 ordered commuting pairs; the supplied checker was not executed. For q=2,n=3 the profile types 3, 2+1, and 1+1+1 contribute 25, 1848, and 3360, giving 5233. For fixed q,k and n=2^kℓ+r with r fixed, removing the common powers of q leaves the weight q^{−Σe_S²−e_[k]}/Πφ_{ℓ+e_S} on e≥−ℓ. The denominators have the uniform positive Euler-product lower bound and converge pointwise to a common factor. Completing the square gives a summable dominating weight on the fixed integer hyperplane. Dominated convergence in the sum of absolute differences and convergence of the positive normalizers prove total variation for the stated uniform tuple distribution. n=0 gives one tuple; there is no uniform asymptotic for varying field or arity.

## originality

FAIL

There is demonstrable exact coverage in the distinct Resultary record 0167a18ca8af: its affine profile orbit sizes and centered TV law are equivalent, and its Boolean decomposition mechanically implies the joint product-image polynomial. It moreover supplies a sharp total-count asymptotic and a commutativity-probability limit. Its catalog date is 2026-10-25, later than the frozen record's 2026-10-18 catalog date; this is a finding of overlapping established content in the indexed corpus, not a finding that the other record predates this one or that either has historical priority. The explicit polynomial presentation, pair specializations and trivial zero-dimensional extension do not leave a substantial uncovered theorem to repair. The exhibited coverage, not any unavailable paper or a title match, is the reason for the originality failure.

## value

PASS

As a mathematical result, an exact simultaneous conjugacy and product-rank classification on the full affine monoid is a natural structural problem. The nondegenerate bounded-scale fluctuation law and its genuinely affine tilt are meaningful in fixed-field random projections. This assessment is not credit for a second distinct contribution: under the exact coverage established above, the generating-polynomial notation and small examples do not supply a valuable independent remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
