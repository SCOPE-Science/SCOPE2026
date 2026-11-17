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

Identify a Johnson vertex with a base edge; inclusive closed neighborhood of base edge e intersects query support S in precisely the edges meeting e. An empty trace forces two distinct isolated base vertices. A singleton trace for each support edge forces at least one endpoint of every support edge to be degree one, hence every nontrivial connected support component is a star. The full trace needs no more than two components. To realize a three-edge subset but omit another in one star forces star size <=3, and with two components each size <=2. Conversely choose two base endpoint representatives: star centers for full component, leaves for singleton/two selected edges, isolated vertices for omissions. This realizes all traces for exactly the classified shapes. Counting one-star and two-star cases yields coefficients s_1=1[n>=4] C(n,2), s_2=1[n>=5] n C(n-1,2)+1[n>=6]3C(n,4), s_3=1[n>=6]nC(n-1,3)+1[n>=7]nC(n-1,2)C(n-3,2), s_4=1[n>=8]C(n,2)C(n-2,2)C(n-4,2), zero for k>4. The exceptional n=2,3 cases and all cutoffs are covered. Literal independent enumeration verifies every size-<=4 support for n=2..8; upper bound for arbitrary sizes follows from proof, not enumeration.

## originality

PASS

The source's coefficientwise closed-neighborhood star-forest classification is not supplied by the primary Johnson graph open-neighborhood VC bound, either published open-neighborhood triangular graph polynomial, or the closed-J( n,3 ) four-query case. An all-n finite-support enumeration is stronger than knowing maximum VC dimension; no equivalent exact closed triangular coefficient census located.

## value

PASS

Natural complete classification of the shattered-support complex of a highly symmetric graph family, with all support-size counts, sharp ambient-size cutoffs and a structural characterization useful for learning-theoretic sample complexity and motif counting. It is not a mere new proof of the known VC dimension: all lower coefficients and the closed/open threshold shift are additional precise invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
