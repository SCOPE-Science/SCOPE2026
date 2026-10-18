---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Cayley sqrt maps disk conformally to convex sector; translating gives normalized convex univalent f. Exact differentiation yields A=(T+1)(T²+1)/(4T), P=(3T^4+1)/(4T²). With T=(29/54)(1−99999 i/100000), z=(T²−1)/(T²+1) belongs to disk. Independent rational-complex arithmetic (not sampled floating point) gives Re P>0 and exact Re h_{1/2}=-393604134232598370597082686478721497781923239383876934628488346374094310839195813073936519/1003500319773081662035210917844648202605964049927384209786136637010545649385413321556380886 in (−1/2,−1/4). One rigorous counterexample falsifies the universal positivity conjecture.

## originality

FAIL

FAIL on current published-statement comparison: Resultary/SCOPE simultaneously publishes the strictly stronger same-map theorem “Only endpoint parameters preserve Carathéodory positivity for all convex maps” (source record SCOPE-20261011-82f2dcfb52c7), proving inf_{z in D} Re h_alpha[f](z)=−∞ for EVERY 0<alpha<1 with the identical sector f and the same component. It entails sign failure at alpha=1/2. The separate exact rational point is a checkable certificate but not a distinct unknown mathematical phenomenon. IMPORTANT priority caveat: source Git commits are only four seconds apart on 2026-10-11, weaker 13:01:14Z and stronger 13:01:18Z; that establishes commit ordering, NOT historical first-public priority or derivation direction. Scientific originality rejected as a standalone uncovered claim under current corpus, without claiming the stronger was earlier in time.

## value

PASS

PASS (historical/mathematical motivation): A rigorous explicit convex counterexample with rational-certified interior witness directly refutes a substantive named conjecture that motivated a higher-dimensional extension argument. The exact point makes the negative result independently checkable; this would be useful notwithstanding later all-interior-parameter strengthening. However independent acceptance fails originality because the same-map stronger classification covers the core claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
