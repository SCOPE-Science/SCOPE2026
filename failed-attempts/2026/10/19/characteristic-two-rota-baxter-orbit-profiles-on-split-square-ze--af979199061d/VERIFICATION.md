---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The weight-zero equations at (v,v) and (1,1) eliminate the scalar components; (1,v) gives T²=0, and all remaining equations hold because products in V vanish and 2=0. Thus u is free, P²(a+v)=aT(u), and P³=0. The image–kernel flag and quotient isomorphism count T of rank r by H_(n,r). For fixed T, choose matched coordinates for its image and a complement to its kernel; commuting automorphisms act by the same invertible map on the matched coordinates and by independent translations between the relevant blocks. This is transitive on each of the four vector strata and does not change stratum. Their sizes are 1, q^r−1, q^(n−r)−q^r and q^n−q^(n−r); multiplying by H yields the exact class sizes. Only two types are present at r=0 and three at r=n/2>0, giving the stated parity totals. Index three is exactly the last type and is realized for n>=2. Fresh full ambient-map and group enumeration (branches/7576d6ef-8a28-4ebc-8ef2-37e82e822169/independent_rb_check.py and independent_rb_gf4_check.py) tested 512, 65536 and 262144 maps for (q,n)=(2,2),(2,3),(4,2). It found respectively 16, 176 and 256 operators, sorted orbit sizes (1,3,3,3,6), (1,7,21,21,42,84), (1,15,15,45,180), and index-three counts 6,84,180. This bounded verification includes a nonprime field and does not replace the proof. The frozen checker was inspected, not executed.

## originality

FAIL

The 2026/10/12 Resultary entry daddf5c855da states the very same characteristic-two weight-zero classification on the same split square-zero algebra, the same four possible conjugacy strata with their exact per-stratum class sizes, and the same total and index-three counts. The earlier catalog coverage is exact at statement level. Independently, the same-day assignment 2 gives the same strata and their rank weights, from which its explicit class sizes follow. No relative priority is inferred from that shared date. There is no surviving distinct claim in the frozen finding; its numerical examples are specializations, not a repair. This is documented equivalent coverage, not a finding of incorrect mathematics or a historical priority adjudication.

## value

FAIL

The orbit-size invariant is natural, but the entire proposed contribution is a known census: both the general table and its nilpotency split are already stated, and even the slightly less explicit same-day classification implies the table by multiplying the established rank counts by the cardinalities of four vector strata. The small examples and bounded independent replay confirm correctness; they do not furnish a new exact invariant or surviving structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
