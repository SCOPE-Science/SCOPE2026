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

Every monotone (0,0)–(2,b) path corresponds to 0<=r<=s<=b, with column predicates L_i=[r>=i], M_j=[r<=j<=s], R_h=[s<=h]. Exactly 3b+1 singleton queries vary, 2b²+b-2 two-query supports shatter by four geometric types, while every triple misses a trace by interval-convexity/nested-threshold obstruction. Thus Phi_b=1+(3b+1)z+(2b²+b-2)z² for b>=2. The k² subfamily with 0<=r<k and k<=s<2k supports two independent balanced binary threshold searches, depth 2floor(log2 k), k=floor((b+1)/2); hypothesis count gives upper floor(log2((b+1)(b+2)/2)), so Ldim=2log2 b+O(1), VCdim=2. Independent exhaustive path trace/pair/triple checks for b=2..10 (triples b<=6) matched the formula. The original checker and source path were read; we do not claim an exact finite Ldim formula.

## originality

PASS

PASS qualified: All monotone fixed-endpoint path vertex traces on a three-column grid differ from tie-broken all-pairs shortest path range systems, geodesic-convex sets, or shortest-path trees. Prior general VC bounds and threshold learning facts do not logically give this polynomial plus unbounded VC/Littlestone separation for this precise incidence family.

## value

PASS

The fixed-width natural graph path concept class has an exact all-height VC-shattering polynomial and a sharp-order adaptive-versus-static separation; it provides a concrete family with VC dimension two but unbounded Littlestone dimension despite only three columns. The exact Ldim additive constant remains open, but the quantified gap is a meaningful independent result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
