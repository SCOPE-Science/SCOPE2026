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

For odd residue order the trace pairing on sl_2(R) is unimodular. A permitted X is primitive, and ad_X has residue rank two. In a basis extending X its first column is zero and the other two columns have a unit minor; they give exactly the orthogonal hyperplane by reduction and Nakayama, so each admissible X gives q^k second factors. If Z has valuation j, the annihilator of pi^j is (pi^{k-j}). Solve the resulting primitive linear equation modulo pi^{k-j} by a unit pivot: each allowed residue X has q^{2(k-1)}q^j lifts, including at j=0 and j=k-1. Over the residue field any nonzero trace-zero leading coefficient is similar to the companion matrix with columns (0,1) and (t,0), t=Q(leading coefficient); its orthogonal plane has form c^2-t b^2. At t=0 this gives square values only and q(q-1) square-norm vectors; at t nonzero the split product or nonsplit field norm gives q-chi(t) vectors per nonzero value. At Z=0, summing ab=t-c^2 gives q^2+q chi(t) vectors per t nonzero and q^2 at t=0; multiplying by first- and second-factor lift counts proves the zero fiber and summing nonzero isotropic leading coefficients proves the missing-target count. The proof uses no ring coefficient field. A fresh exhaustive replay checked every target and both types in F_3, Z/9 and F_3[t]/(t^2); the original C++ was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the two conditioned labeled fiber formulas and the resulting exact image obstruction, not for regular commutator existence or classical quadratic form counts.

## value

PASS

Regular semisimple witness types are intrinsic, not arbitrary filters. The result replaces qualitative existence by exact uniform conditioned counts and shows an actual asymmetry of images: all targets occur in the split type, while the nonsplit type misses precisely the nonzero isotropic leading coefficients, at every valuation. This supplies a usable baseline for finer bracket statistics over chain rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
