---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Euclidean division z=qm+r gives z in <m,m+1> iff q>=r. Thus for 0<=j<m, j² is a gap iff (j² mod m)/m > [m/(m+1)](j/m)². Completion by differencing yields |sum_j e((hj+kj²)/m)|²<=m gcd(2k,m)<=2|k|m, valid for composite as well as prime moduli, with k=0,h nonzero geometric sums zero. Two-dimensional Erdős–Turán–Koksma gives D*<<m^(-1/3) log(2m) at H=floor m^(1/3), and K=ceil m^(1/6) monotone strips produce O(m^(5/6) log m) uniform in u,v. Replacing m/(m+1)x² by x² changes main term <1. Independent small-modulus exact counts checked membership and approximate 2/3 trend; not proof of limit.

## originality

PASS

Best-of-knowledge new quantitative distribution of square-gap ROOTS of <m,m+1> with profile 1-t² and composite-uniform O(m^(5/6) log m); earlier primary sources address the maximal missing square (square Frobenius number) and known quotient/remainder membership, not the global count or interval distribution. Analytical discrepancy theory could imply an unstated equivalent and remains a priority risk.

## value

PASS

A natural enumeration problem for all square gaps in the classical two-consecutive-generator numerical semigroup, providing its previously undetermined asymptotic root distribution and a uniform power-saving interval estimate. The limit is mass 2/3 rather than a normalized probability law; precise counting profile can be used in further semigroup-square statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
