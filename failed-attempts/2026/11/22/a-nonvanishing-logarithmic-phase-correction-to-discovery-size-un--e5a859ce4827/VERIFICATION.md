---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

At fixed R>1 the independent miss product equals exp(c-cR^n), including n=0, with c=aR/(R-1). Expanding R^K by telescoping and interchanging the nonnegative terms gives the convergent exact expectation. Set h(u)=u exp(-u) and c=R^(-m-theta); reindexing sum_{n≥0} h(cR^n) removes only the left tail of the bilateral profile, bounded by c/(R-1) uniformly. The remaining profile converges uniformly by geometric decay on the left and faster decay on the right, and exp(c)=1+O(c). Fourier integration changes variables from j-theta to u=R^(j-theta), producing Gamma(1+2πik/log R)/log R with the stated sign convention. Gamma has no zeros, so the phase profile is nonconstant for each fixed R>1. Exactly prescribed phase sequences realize every profile value; compactness and continuity of the phase circle give the full interval of limits. The R=10 phase examples were independently evaluated by summing j=-22 through 5 (the omitted tails there are negligible at the reported precision), giving 3.805605035176776 and 3.227809993075674. Supplied check.py was inspected, not executed. There is no claim of uniformity in R down to 1, or of validity for a carrying-capacity or randomized-phase model.

## originality

FAIL

The core mathematical finding is a direct specialization of the established geometric harmonic-sum expansion, not just an application of a related method. The modeled expectation is an elementary affine rescaling of the differentiated geometric exponential sum. The standard residues supply all-R nonvanishing modes and uniform error, and the interval is an immediate consequence of a continuous periodic leading term. The available applied papers do not establish an exact duplicate of this surveillance setting; the negative decision rests on the positive mathematical implication from the earlier full-text harmonic-sum result, not on missing full texts.

## value

FAIL

The phase warning is a useful illustration of geometric-lattice sampling, and the example shows how large the effect can be in the idealized model. As a standalone new finding, however, the asserted exact profile, uniform leading error, nonvanishing and interval are a routine reduction to the known analytic result. The unbounded fixed-phase model contributes no further nonroutine invariant or independent empirical or model-comparison result; the numerical phase example does not remedy that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
