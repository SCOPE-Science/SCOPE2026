---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The formula itself is correct. The primary source's complete normal forms show that a fixed positive balanced off-degree allocation has two quotient classes and its central-space theorem selects exactly one central combination; a zero-off-degree allocation has one quotient class, central precisely for even skew parity. Therefore the proper-central dimension is 2^(n-1) plus the positive balanced multinomial sum. The constant-term identity for (2+x+x^{-1})^n reduces this to binom(2n,n)-2^(n-1). The analogous complete normal-form count gives total codimension binom(2n+2,n+1)-2^n and hence the exact shift c_delta(n)=c_total(n-1). Fresh arithmetic reconstruction through n=20 and the inspected package checker through n=40 agree, but the infinite result follows from the symbolic count.

## originality

FAIL

Originality fails under the required implication standard. The complete primary source gives linearly independent normal forms for every multihomogeneous class in the non-order-two elementary branch and a complete description of the central-polynomial space. Counting those published classes is exactly the audited formula: the no-off-degree central contribution is the even-parity half of 2^n, while every positive balanced off-degree allocation contributes one central dimension. The closed binomial expression and one-step shift require only routine multinomial coefficient extraction from those complete published ingredients.

## value

FAIL

Proper-central codimensions are a legitimate invariant, but in this record the exact sequence is obtained by routine enumeration of a complete published normal-form and central-classification theorem followed by an elementary coefficient extraction. The shift and one-quarter asymptotic are algebraic consequences of that same count. Under the required value bar, this does not constitute an independently worthwhile unknown exact fact because the answer is mechanically implied by existing structural results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
