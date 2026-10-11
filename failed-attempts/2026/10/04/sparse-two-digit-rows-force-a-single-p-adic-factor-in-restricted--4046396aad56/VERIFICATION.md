---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Kummer's theorem gives the valuation as the minimum borrow count. For \(N=p^s+p^t\), the only no-borrow lower indices are \(0,p^s,p^t,N\); the two proper nonzero possibilities are not divisible by \(m\) because \(p\) is a unit modulo \(m\). Hence every admissible lower index has at least one borrow. The explicit index \(k=mp^{t-1}\) has exactly one borrow because \(m<p\), including the adjacent-digit case \(s=t-1\). A fresh independent replay over 86 admissible small parameter quadruples confirmed both the minimum borrow count and the witness; this finite check is corroborative only.

## originality

FAIL

A primary paper posted on 1 October 2026 proves the sharp universal row-by-row bound \(v_p(G(N;m))\le r_p(m)\) for every admissible row when \(p\nmid m\). Under the audited hypothesis \(p>m\), one has \(r_p(m)=1\), so that theorem supplies the entire upper bound for every row, not merely sparse rows. The remaining lower bound is the immediate Kummer no-borrow observation that a two-one-digit row has only \(0,p^s,p^t,N\) as no-borrow subdigits and none of the proper ones is selected. Thus the final equality is a direct special-case consequence of a strictly broader theorem plus the standard digit criterion.

## value

FAIL

After the universal \(p>m\) upper bound is published, the sparse two-digit equality is obtained by the elementary no-borrow subdigit check. The modulus-five residue formulation is a convenient corollary but does not add a substantive structural gap beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
