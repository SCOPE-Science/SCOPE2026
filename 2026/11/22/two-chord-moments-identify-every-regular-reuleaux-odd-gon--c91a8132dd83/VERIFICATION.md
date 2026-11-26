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

At unit width the opposite-side endpoints of the generating arc have angles ±t from the inward radial direction as seen from its center. Each arc has length 2t, so taking a uniform arc index and uniform U on [−1,1] gives normalized arclength; the squared radius is 1+sec²(t)/4−sec(t)cos(tU). Integrating cos and cos² gives the frozen m and m4, and the rotational center has zero mean and covariance mI/2 for n≥3. Independence eliminates the linear cross terms and gives E[(X·Y)²]=m²/2, hence M2/w²=2m, M4/w⁴=2m4+4m² and H=Var(|X|²)/(2m²) at unit width. This variance is positive. For absolute arc parameters u>v, cos(tv)−cos(tu) is positive and strictly increasing in t on (0,π/6], since u sin(tu)>v sin(tv). The pair-difference variance identity and positive increasing sec²(t) give strict growth of the radial variance. Independently checked the sign criterion for m': m'<0 iff 2t cot t>2cos²t+t². The stated Taylor bounds give a lower bound t²/3−5t⁴/6>0 on the whole interval, and m remains positive as a squared-radius expectation. H therefore strictly increases with t, hence decreases with odd n. For the expansion, Var(U²)=4/45 and Cov(U²,U⁴)=8/105 give Var(cos(tU))=t⁴/45−t⁶/315+O(t⁸), hence Var(|X|²)=t⁴/45+2t⁶/105+O(t⁸). Using m=1/4−t²/12+O(t⁴) in the quotient gives 8t⁴/45+256t⁶/945+O(t⁸), exactly the reported coefficients after substitution. For a circle the radial variance is zero; the width recovery follows directly from M2. The finite midpoint quadrature is only a supplement.

## originality

PASS

Same-measure diameter tails already identify the arc count from different data; interior moment and Crofton-line statistics are also indexed. The distinct result supported here is exact identification with only the second and fourth Euclidean-arclength endpoint distance moments and their quantified scale-free separation, not the first determination of order from any chord law.

## value

PASS

Two fixed population moments are a practical low-information target for a natural shape-sensing question, whereas an endpoint tail coefficient uses the extreme tail and scale normalization. The exact, global-in-order uniqueness addresses that distinction and the leading quartic loss explains why the invariant becomes weak near a circle. This is a useful inverse benchmark with clear limits, not a claim of statistical robustness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
