---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Analytical and computational verification

The exact sign-pattern decomposition, dot products and hyperbolic-area Jacobian appear in `RESULT.md`. The two lower-order error classes have area \(O_h(\varepsilon^2)\); the dominant class has area \(8h(x)^2\varepsilon^2\log(1/\varepsilon)+o_x(\varepsilon^2\log(1/\varepsilon))\). The probability coefficient follows after multiplying the exact sorted-coordinate factor and boundary-sign probability. The marked total-variation limit uses convergence of rescaled densities on compacts plus tightness of excluded strips. The sharp shape coefficient bounds use Jensen and Berwald with admissible equality/approximation profiles.

Execute `python verify.py` in an environment with `numpy` installed (see `requirements.txt`). The checker evaluates actual Euclidean acute tests on random boundary triples, with Euclidean-arclength importance weights normalized by Gaussian quadrature, for the parabolic and tent profiles, three million triples each at \(\varepsilon=0.02\). An observed execution produced `THIN_LENS_ACUTENESS_TWO_SHAPES_OK`: parabolic probability `0.0024653939402832464` versus leading term `0.0025036947234740137`; tent probability `0.001631` versus leading `0.0015648092021712584`. These finite random experiments do not establish infinite-dimensional sharpness, total variation or asymptotic convergence by themselves.

Known limits: the proof is for each fixed Lipschitz concave profile; smooth ovals with unbounded tip slopes and other sampling conventions are not included. The already known thin-ellipse special value is expressly excluded from novelty. Independent validation and exhaustive priority research remain unperformed.
