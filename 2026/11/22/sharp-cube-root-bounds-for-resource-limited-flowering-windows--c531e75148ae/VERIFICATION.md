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

For fixed w>0, evenness and strict radial decrease of the Gaussian density make the derivative in c strictly negative for c>0 and positive for c<0. With y=w/σ and k=B/(2σ), the centered shape is (1−e^(−k/y))I(y); its logarithmic derivative times y is R(y)−h(k/y), where R(y)=yI′(y)/I(y) decreases strictly from 1 to 0 and h(z)=z/(e^z−1) decreases strictly in z. These facts follow from the two inverse integral representations in the source. There is one crossing and a unique maximum; increasing k lowers h(k/y) at a fixed y and strictly raises the optimizer. Writing a=y²/2,z=k/y, the crossing equates E exp(aX) and E exp(zU), with X=1−U² and U uniform on [0,1]. Coupling by common quantiles gives X>U almost surely in that coupling. To check the upper bound directly, Q_X(s)=2s−s² and Q_Y(s)=4s/3 for Y=4U/3 cross at s=2/3, x_0=8/9, and X,Y have the same mean. On each side of x_0, Q_X is closer to x_0 than Q_Y. Applying the strict decrease then strict increase of x↦exp(ax)−a exp(ax_0)x and using equal means proves the strict exponential-moment inequality E exp(aX)<E exp(aY) for a>0. Thus a<z<4a/3, equivalently 3/4<w³/(Bσ²)<1. Small k forces a,z→0 and first moments give z/a→4/3. Large k forces both to infinity, and their normalized log moment generating functions tend to the common essential supremum 1, giving z/a→1. This proves sharpness at both ends. Independent Simpson quadrature and bisection of the stationarity equation gave y=1.155298807994 and score 0.435570340282 at k=1, and normalized width cubes 0.750002184 and 0.999449612 at k=10⁻⁶ and 10⁶. These are diagnostics only; the supplied check.py was inspected, not executed. The conclusions use one freely centered contiguous uniformly funded interval, one Gaussian opportunity and the stated conditional saturation, not an unconstrained display function or an empirical flowering law.

## originality

PASS

The distinct supported claim is the unique resource-dependent width and the strict sharp global bounds with two limiting constants for the stated Gaussian-window saturation model. Gaussian centering, the general stochastic-order tools, and Poisson saturation as a modeling ingredient are not separately credited.

## value

PASS

The width of a contiguous window matters when prolonging coverage dilutes a fixed display budget. The result resolves that tradeoff in a natural one-event benchmark with a unique width, a narrow uniform enclosure, and distinct sharp low- and high-budget constants. It offers an exact comparison point for other model assumptions without claiming an empirically calibrated intervention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
