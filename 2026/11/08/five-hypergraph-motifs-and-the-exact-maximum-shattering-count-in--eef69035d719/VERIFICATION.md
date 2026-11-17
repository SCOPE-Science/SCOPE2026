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

PASS — Four distinct triples in J(n,3) are encoded up to ambient relabeling by fifteen membership-cell multiplicities m_t>=0 with four margins each equal to three. A three-element center has 0..3 outside coordinates; its trace on support i is positive iff it meets A_i in exactly two elements. This incidence encoding is necessary and sufficient for all supports and all n. Independent recursive exhaustive enumeration of the entire finite cell-margin space found 862 feasible vectors, exactly 40 shattered distinct-row vectors distributed (u,required outsiders)=(5,1):12,(6,0):12,(6,1):13,(7,0):3, compatible with five support orbits. Independent direct all-center/all-four-support test gave s4(5)=0,s4(6)=720,s4(7)=7035,s4(8)=28980. Orbit weighting produces s4(n)=(n)_5(6n²-17n-41)/48 for n>=7. Finite membership-census is an exhaustive proof thanks to complete incidence reduction, unlike direct finite-n tests.

## originality

PASS

PASS, qualified — Earlier Adler–Benediktsson–Macpherson establish VC dimension four for Johnson open neighborhoods and enumerate local cases rooted at a distinguished witness, so neither maximal size nor local feasibility is new. The unrooted rank-three complete five-hypergraph classification, smallest ambient embedding thresholds, exact labeled polynomial and asymptotic probability are additional evaluated invariant counts. The inspected full accepted manuscript did not state these formulas; its local classification is a substantial prerequisite and could be transformed into the census by separate work.

## value

PASS

PASS — The exact number of maximal shattered supports is a natural quantitative refinement of a sharp VC-dimension bound, and five motif classes explain which configurations contribute to maximum shattering. The asymptotic 3888/n^5 measures rarity of maximal supports; this is a useful finite combinatorial invariant even without the full shattering polynomial. Value is in the unrooted census, not merely re-proving VC dimension four.

The dated certificate retains the supplied scientific assessment, sources and limitations.
