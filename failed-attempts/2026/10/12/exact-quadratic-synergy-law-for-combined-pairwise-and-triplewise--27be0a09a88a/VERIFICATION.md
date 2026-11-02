---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Starting from the actual source model Eq. (3.7) (open-access Springer full text), let R=τ(n−2)>1, κ=(n−1)/n, δ=(n−2)/n. For x,z>0 put P=c_p z,T=c_t z². The threshold equations give κP+κδT=R−1; τx=1+P+κT=Ry; and z=[1−(1−q)(1+P+κT)/R]/(a+R). Nonnegative P,T uniquely parameterize the branch via t∈[0,1], P=(1−t)(R−1)/κ,T=t(R−1)/(κδ), and z(t)>0 because q>2(R−1)/(nR−2). Hence x,y,z>0; endpoints are C_p,C_t. Independently substituting exact previous parametric solution in SymPy gives identically zero residual for submitted c_t−L(C_p−c_p)−Q(C_p−c_p)², C_t−L C_p−Q C_p² and chord gap, for symbolic n,R,a,q. Since 0<q<1 implies L,Q>0, interior strict gap holds; q=1 yields linear equality directly without invalid 1/(1−q) division. Git source tree computed exactly from seven actual blob IDs equals 415c284d0126f3e28f2b4a7ed97f951df85ba215. Inspected exact 599-byte verify.py reconstructed to Git blob SHA b4c9ae7fd76a26c6d91e7367e18f08417eeed63d and executed successfully with VERIFY_OK; its finite rational test is corroborative, not a proof for all parameters.

## originality

FAIL

Decisive existing full-result coverage. The published October 4 Resultary record (and its earlier-dated SCOPE source record) already proves the entire mixed pairwise/triplewise fast-variable threshold branch and strict partial-compliance / zero full-compliance chord gap under the same n,R0,a,q hypotheses. The new explicit quadratic graph is obtained by solving the prior rational parameterization for its parameter and expanding: L=C_t r/C_p, Q=C_t(1-r)/C_p^2. Symbolic elimination verifies the submitted formulas identically, so a different polynomial representation cannot be counted as an original scientific claim. The September 6 model paper supplies the four governing equations and pure thresholds and analyzes mixed tracing numerically. A Resultary publication_date 2026-10-04 and source record path 2026/10/04 document the earlier-dated claim; the associated later sync date is not used as a scientific argument. No alternative new mathematical remainder remains in the unchanged submitted theorem.

## value

FAIL

A complete mixed-intervention threshold curve and compliance-dependent synergy are mathematically motivated objects. But that natural classification, all endpoint values, strict interior chord gap and full-compliance equality were already obtained in the prior complete October 4 parametric theorem. Expressing the SAME already-solved curve as a quadratic graph requires only a bijective scalar substitution and coefficient collection; it yields no independently unknown exact invariant, novel boundary or mathematical obstruction. The new numerical rational example is merely an evaluation of the covered identity. The presentation may have expository utility, but no separate research-level value survives after existing result coverage. This V assessment is not a penalty for the small scope of the problem; it is about the absence of a new mathematically motivated fact beyond the prior complete solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
