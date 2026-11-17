---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Write high-count h_i, value rL+(H−L)h_i. For target with a low good, removing low is strongest EFX inequality (H−L)(h_j−h_i)≤L; for all-high target, inequality (H−L)(r−h_i)≤H. When H≤2L, evenly spaced high counts h_i differing by ≤1 meet both; when H>2L, any not-full bundle must share the minimum high count a since integer positive differences violate first inequality. If full bundle coexists with mixed, (r−a)(H−L)≤H=(H−L)+L and H−L>L forces r−a=1; so either q multiple n or q>(r−1)n. Equal-count and top-layer constructions prove converse. Exact labelled goods multinomial counts follow by partitioning distinct high and low items into fixed h_i profiles, including q=nr. Independently enumerated all high-count vectors in 12 (n,r,H,L) small parameter tuples and verified feasibility iff. For iid high goods B_n~Bin(nr,p), exact event B_n>n(r−1) or B_n=jn for j≤r−1 gives CLT critical p*=(r−1)/r with scale β r^(3/2)/sqrt(r−1), Chernoff exponential tails, resonant local CLT n^-1/2 at j/r (1≤j≤r−2). At p=p* limit 1/2. Identical valuation total sum fixed makes every allocation fPO trivially, but does not prove EFX. These rigorous universal statements do not rely on finite checks.

## originality

PASS

The closest balanced fair-allocation theorems guarantee EF1+fPO (Kawase–Mahara and Cookson–Shah–Verma), which does not imply EFX; the two-good-type EFX+PO existence theorem imposes no exact equal bundle sizes. The new iff criterion H<=2L or n|q or q>(r−1)n, complete labelled-allocation counts and binomial window/arithmetically resonant probabilities are not consequences of those earlier existence statements, and Resultary searches found no equivalent known fixed-cardinality two-valued formula. The conclusion is best-of-knowledge with named limitation: relevant complete arXiv primary texts were not retrievable in HTML in this run, so noncoverage is only established at the inspected statement level.

## value

PASS

Exact-cardinality balanced EFX versus guaranteed weaker EF1 is a substantive natural fairness boundary: the ratio H/L=2 and arithmetic conditions on q create explicit impossibility patterns. Full labelled assignment counts and random sample-size threshold with exceptional resonance peaks can guide fair-division feasibility in identical two-valued drafts; not a routine rephrasing of known unconstrained EFX+PO existence, and precise invariant is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
