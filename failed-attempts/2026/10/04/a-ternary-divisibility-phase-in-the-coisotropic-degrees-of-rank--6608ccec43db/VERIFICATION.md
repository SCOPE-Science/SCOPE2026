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

Independent coefficient extraction from \(c(TX_n)=(1+x)^3(1+y)^{n+1}\), \(H=x+y\), and the smooth polar transform reproduces the five formulas; the dual determinantal codimension gives the cutoff after index four. The gcd proof from \(\delta_0-\delta_4=n+1\) and \(\delta_2=3n^2\) is valid. Fresh symbolic checks for n=2 through 8 reproduced the formulas and gcd.

## originality

FAIL

The explicit polar vector is already a direct specialization of Çelik--Jamneshan--Montúfar--Sturmfels--Venturello Corollary 16, which gives the polar degrees of every rank-one \(m_1\times m_2\) Segre variety. Their Table 3 even prints the assigned vectors for \(3\times5\) and \(3\times6\): \((15,40,48,30,10)\) and \((21,60,75,48,15)\). Once the general vector is specialized to \(m_1=3,m_2=n+1\), the gcd law follows in two elementary steps from \(\delta_0-\delta_4=n+1\) and \(\delta_2=3n^2\). This is mechanically implied prior coverage.

## value

FAIL

The arithmetic phase law is neat, but the complete polar vector is already supplied by a published general formula and sample tables, and the gcd is obtained by an elementary subtraction plus coprimality. Under the common bar this is a routine corollary of known exact data rather than an independently valuable new classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
