---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For F(c)=c-D sign(D^Tc), a two-cycle makes D(sign(D^Tc)+sign(D^Tc_next))=0; its inner product with c+c_next enforces edge-sign reversal or tie preservation. A hub has degree n, a leaf degree two, so edge differences in a two-cycle have magnitude <=n+1 and the normalization range is finite/exhaustive. The five bands y<0,y=0,0<y<d,y=d,y>d yield independent integer intervals conditional on band populations; the multinomial formula counts all labeled leaves with no missing global constraints. The sharp d<=2n-2 and all values 1..2n-2 are witnessed, with unique extreme leaves n-1. Independently enumerated complete bounded domains n=1,2,3 yielding N=9,47,299, sharp d=4 at n=3; the infinite-n claim uses the band proof and cited general period<=2 theorem, not the finite checks.

## originality

PASS

Earlier Duffy–Lidbetter–Messinger–Nowakowski and Long–Narayanan results establish eventual periodicity/period bound, not the labeled K2n initial recurrent census and hub-gap multiplicities. The related SCOPE cycle transfer law is for C_n, not K2n. Resultary search did not surface an exact all-n five-band enumeration; this is best-of-knowledge and an unindexed exact recurrence remains possible.

## value

PASS

A complete labelled periodic-state census and sharp attainable hub imbalance for a basic complete-bipartite graph family is a natural dynamical invariant. The five-band coupling of two hubs creates a substantive classification beyond previously known eventual periodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
