---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For n>=6, Proposition 8.3 gives all n(n-1) maximal pure strong matchings from a path after deleting a last vertex. Reflections s_a(v)=a-v exchange incidence signs on edge e_i with partner e_(a-i-1). Their geometric fixed points are precisely equal-barycentric-weight unions of eligible two-element incidence orbits, giving a canonical PL orbit-face realization. The necessary two-consecutive-omitted-edge condition selects the exact P/N interval families; all subsets of either family fit one rooted-path facet and a mixed choice either double-uses an edge or forces four alternations of signs, forbidden by the single-block structure. For odd n=2m+1 both components have m-1 orbit vertices, for even n=2m vertex axes m-1 and edge axes m-2, so the dimensions and all n boundary cases are correct. Ordinary fixed Euler=2 implies reduced Lefschetz=1 after equivariant barycentric subdivision. Independently reconstructed all rooted-path facets from graph endpoints and root positions, formed incidence orbits and maximal orbit-face sets for 38 conjugacy-representative (n,axis) cases at n=6..30, including n=6, and all were exactly two simplices of predicted sizes. Independently serialized the eight retrieved actual Git blob identifiers into a Git tree and obtained assigned tree SHA 24f209329c0ba261c1932a6717f2604629654773. Finite enumeration corroborates, and is not relied on for the unrestricted n theorem.

## originality

FAIL

The final theorem is already published verbatim in substance, with the same object SM_pure(C_n), every n>=6 and every reflection, the identical PL two-disjoint-simplices description and precisely the same odd/even axis-dependent simplex dimensions, plus S^0 and reduced Lefschetz number +1. The October 25 2026 Resultary RESULT.md explicitly states all of these facts, and a November 1 2026 Resultary theorem independently restates and proves the identical classification. A second November 1 theorem includes the same fixed-space classification inside a broader integral dihedral homology result. This source claim dated November 8 contains no surviving separate theorem. This is decisive implication/identity evidence, not a failed-search inference.

## value

FAIL

Geometric reflection fixed-set types are intrinsically meaningful for the pure strong cycle complexes, but this submission reproduces exactly the already-published October 25 classification and November 1 restatement. It does not add an unclassified axis, boundary length, group action, distinct integral invariant or new structural lemma; its proof repeats the same orbit-barycenter and alternating-sign method. Therefore the submitted final fact is a known result, not a worthwhile new exact invariant, even though the earlier theorem itself is valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
