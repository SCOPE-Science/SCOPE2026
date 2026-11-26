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

On the real scalar decay test the implicit stage gives Y/(1+rT); multiplying the resulting scalar update over independent fractions makes the mean-square factor F_mu(r)^N. The Gauss nodes satisfy g(t)=t^2-t+1/6=0; equal weights and reduction by g give exactly the four moments. Inverting the rational denominator modulo g^2 reconstructs the cubic contact polynomial and the exact affine-in-t factor C+B t of its remainder. The denominator is strictly positive, C(1/2)=9/8, and C and C+B are strictly increasing on r>0; (C+B)(1/2)=-5/8 and (C+B)(3/5)>0. Thus the remainder is nonnegative exactly above the proposed certificate threshold, where its zero set is the two nodes, with possible extra t=1 at the boundary. The matched moment E g=0 excludes mass at that extra point. To show necessity rather than just a failure of certification, add epsilon mass at 1 and solve the four moment equations by varying both Gauss weights and both interior nodes. The weighted confluent Vandermonde is nonsingular: its transpose tests whether a cubic can have two distinct double zeros. At zero epsilon the variation of the residual at the two original nodes vanishes to first order, leaving f_r(1)-H_r(1)<0. The perturbation is genuinely admissible and improving. The Gaussian amplification minus 1 has sign of r^3-2r^2-12r-12 for r>0, which changes sign only once; R_G>r_c. For all other laws strict inequality at R_G persists immediately to its left by continuity, so even the initial stability interval is strictly shorter. The uniform integral gives r^2/(1+r)-2 log(1+r), with derivative (r^2-2)/(1+r)^2, one positive zero and the claimed gain.

## originality

PASS

Pass for the exact all-law transition where the Gaussian principal representation becomes uniquely optimal, including necessity below the sign threshold. Not for Gauss moment exactness, the uniform RK analysis, the Gaussian stability cubic, or a large-r optimum in isolation. Indeed the usual fourth-derivative condition already gives sharp Gaussian optimality for r>=2/3 and, combined with the known Gaussian cubic, gives the maximal radius as a corollary. The extra optimality band [r_c,2/3) and the sharp converse are not obtained from that broader sufficient condition.

## value

PASS

The first three uniform moments are the natural Gaussian-exact calibration class, not an arbitrary parameter slice. The exact loss of optimality for the canonical design (demonstrated by a feasible improving law) and the extra range below the textbook sign cutoff are substantive information about stage design. The numerical stability gain is useful context, not the basis for accepting a previously implied radius statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
