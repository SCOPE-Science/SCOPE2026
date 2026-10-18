---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For compact invariant probability support in strict positive octant, log Z is a bounded smooth observable and invariance yields 0=gamma2 E[m2P/(alpha2+P)]-D2. Rewriting P/(a+P)=1-a/(a+P) gives E[(a+P)^(-1)]=(a+p*)^(-1), p*=D2 a/(gamma2 m2-D2), if gamma2*m2>D2. Expanding 1/(a+P) exactly around the mean m=E[P] yields m-p*=(a+p*)/(a+m) E[(P-m)^2/(a+P)]; nonnegative, zero iff P constant. Stationarity with P=p*, Z positive constant and strictly monotone f1 forces N constant and hence the unique coexistence equilibrium. Continuous nonconstant cycles must take prey values strictly below and above p* to have the stated reciprocal average. Check numerical p*=1/4 (D2=1) and p*=13/34 (D2=13/10) with a=1/2, gamma2*m2=3. No assertion of existence of a cycle or boundary measures.

## originality

FAIL

Direct same-statement published generic Holling-II result transfers by literal substitutions u2=P, u3=Z, d3=alpha2, w3=gamma2*m2, c3=D2 to give the entire shifted mean, exact finite-amplitude mean defect and recurrent crossing, without using chemostat N or P equations. Equality equilibrium classification follows from routine positivity/monotone remaining equations. Matching implications—not titles—make this covered.

## value

FAIL

The valid result only specializes an already published invariant-measure Holling-II mean-defect law to another food-chain labeling. It does not derive a materially different invariant, natural classification or sharp new threshold. A model-specific use of a generic one-equation equilibrium average, plus Jensen inversion, is a routine application, not a separately motivated mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
