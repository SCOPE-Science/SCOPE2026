---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Differencing D commutes with circulant L+ and maps periodic real functions onto the zero-sum increment hyperplane. The dual norm of any row g on the zero-sum infinity cube is min_c sum|g_j-c|, with median signs/ties characterizing all extremizers. The Green row G_j=(n^2-1)/(12n)-j(n-j)/(2n) solves LG=delta_0-1/n and has mean zero. Distance-shell multiplicities determine the four medians and finite sums yield the stated four-case rational formulas; n=3,4 boundaries follow directly. Independently exhausted zero-sum slope vectors with entries -1,0,1 for n=3..12 and matched exact median values. Correctness PASS, but finite experiments do not establish universal formula alone.

## originality

FAIL

FAIL by mathematical implication of earlier 2026-10-25 exact cycle heat-Lipschitz theorem for n>=5: it gives min_c sum|p_t(j)-c| for every t, proves strict radial ordering independent of t, and explicitly constructs a single time-independent signed-gradient extremizer for ALL t. Since L+=integral_0^infty(e^{-tL}-Pi)dt on the quotient, integrating the heat row gives precisely quadratic Green G; the SAME extremizer can be kept outside the integral, so the inverse-Poisson sharp norm equals the median sum of G. The closed four-residue arithmetic and full equality face follow by known kernel (Ellis 2003) and elementary shell/tied-gradient optimization. Also a Nov 1 exact heat result covers n>=7. n=3,4 are two routine boundaries, not originality.

## value

FAIL

FAIL as a new standalone finding: the four-class constants and median extremizers are directly obtainable from the published stronger all-time heat-seminorm classification and previously known Green kernel via standard semigroup integration and finite sums; no distinct motivated structural gap beyond this routine implied special case survives. This is not a rejection of correctness or usefulness as a reference computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
