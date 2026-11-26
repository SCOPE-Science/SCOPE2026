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

By character modulation the supremum of the Fourier max-to-fourth-norm ratio equals that for the zero-frequency numerator, and scaling normalizes sum f=1. With this normalization the fourth-power objective is coercive and strictly convex on the finite-dimensional complex affine space (injective Walsh transform), so its unique minimizer is fixed by complex conjugation and by the permutation group of the m=d+1 parity coordinates. Under x→(x,sum x), the support becomes exactly zero and the complete edge shell. The two real orbit coefficients are 1-u and u/binom(m,2). Uniform sign vectors count each character twice; the edge sum ((sum eta_i)^2-m)/2 gives the stated t_j and counting factor 2^(-d/4). The real quartic is strictly convex and coercive, with derivative -4 at zero, so the cubic has one root u>0. Independently expanded the moment-generating polynomial of sum eta_i and recovered the second, third and fourth edge moments and the polynomial for M'_m(1); its sign is positive for m=3,4,5 and negative for m>=6. The support indicator is optimal precisely for m=3,4, since its normalized derivative is -32(m-4)(m-3)(m-2)/(m^2-m+2)^3. Jensen and the u=1 competitor imply |u_m-1|=O(1/m). From the exact edge moments, mt has moments through degree four tending to (1,0,2,8,60), so the rescaled objective converges uniformly on bounded v=m(u-1) to Q(v). Comparing the bounded minimizers with every fixed v, all subsequential limits minimize the strictly convex Q, with unique minimizer satisfying v^3+6v-8=0. This also gives the exact asymptotic prefactor. Every extremizer is consequently a modulation and scalar of the unique zero-frequency profile, and all such profiles attain the ratio. Exact replay: python3 /workspace/review_evidence/algebra.py (SymPy; Walsh block).

## originality

PASS

The strongest distinct same-day Resultary hit really does use the same edge-shell representation and a Gaussian quadratic model, but its full Finding defines an infimum of counting l1/l2 on a radial two-dimensional input space. That is not this sharp counting linfinity/l4 synthesis, which starts on the entire supported complex space and has a different finite optimizer and limiting moment equation. No priority claim is needed. General finite synthesis and transitive-support background provide methods, not the nonuniform profile, threshold or asymptotic read here.

## value

PASS

The radius-two Hamming ball is a standard finite Fourier support and the sharp synthesis ratio is a pre-existing exact-norm question. The result goes beyond using visible coordinate symmetry: the parity embedding forces the two noncentral layers together even though the indicator stops being optimal. The exact low-dimensional sign boundary and all extremizers determine when positivity can or cannot be imposed without losing the sharp constant, and the chi-square quartic fixes a sharp asymptotic coefficient rather than only order of growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
