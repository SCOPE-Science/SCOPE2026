---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The terminality proof agrees with the general two-heavy Reid--Tai classification. Fletcher's subset criterion reduces to the singleton heavy variable \(a\): the possible degree conditions are exactly \(a\mid D\), \(a\mid D-1\), or \(a\mid D-b\), which reduce to the stated three divisibilities; the other heavy singleton and pair conditions are automatic. Inclusion--exclusion gives the exact count using \(\gcd(r,2r-2)=\gcd(r,2)\) and coprimality with \(2r-1\). Standard divisor-summatory identities give the stated main term and linear coefficient. Independent exact finite checks of the divisor criterion and count agreed with the package; the infinite assertion is supported by the symbolic proof.

## originality

FAIL

A stronger published SCOPE theorem already gives an iff quasismoothness criterion for every two-heavy \(\mathbb P(1^r,a,b)\): with \(d=b-a\), the \(a\)-condition is divisibility by one of \(r,r+d,r+d-1\), and the \(b\)-condition by one of \(r,r-d,r-d-1\). Substituting the audited first terminal layer \(d=r-1\), \(b=a+r-1\), makes the \(b\)-condition automatic because \(b\mid0\) and gives exactly \(a\mid r\), \(a\mid2r-1\), or \(a\mid2r-2\). The published triangular theorem also supplies terminality for exactly \(1\le a\le2r-2\). The remaining count and summatory asymptotic are routine inclusion--exclusion and standard divisor-summatory identities. Thus the whole final claim is prior-implied under the required implication standard.

## value

FAIL

The first terminal layer is a natural slice, but after the stronger all-two-heavy iff theorem is available, the layer criterion is obtained by direct parameter substitution and the count/asymptotic by standard divisor-function bookkeeping. Under the stated value bar against routine substitutions and mechanically implied results, this does not retain sufficient independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
