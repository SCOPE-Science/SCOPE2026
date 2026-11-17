---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The k-step derivative is a bijection for any additive cyclic alphabet. One tandem duplication inserts k zeros in one zero run; common descendants of different roots are exactly legal transfers k(e_i−e_j). Residues r_i mod k and nonzero skeleton are invariant; quotient counts u_i=floor(r_i/k) move one unit between distinct runs. The color sum i*u_i mod d changes by a nonzero i−j; active d=s+1 is ≤n−2k+1 since there are at least k zeros and s nonzero derivative symbols. For n≤2k edges cannot occur; for n≥2k+1 a skeleton of n−2k nonzeros with k zeros placed in any of d runs produces a d-clique. These are universal constructive proofs. Independently enumerated full descendant balls for q,k,n=(2,1,3),(2,1,5),(2,2,5),(3,1,4) and confirmed claimed cliques and proper coloring; finite checks supplement rather than replace proof.

## originality

PASS

PASS on inspected primary and published record statements. The Jain–Farnoud–Schwartz–Bruck source introduced derivative and zero-run insertion, and October 4 published work counts edges and uniqueness of common descendants in the SAME graph, but neither gives a globally optimal proper coloring or matching maximum clique in the inspected material. The Dolecek–Anantharam repetition-code paper considers deletion/repetition correction and modular constructions but its accessed beginning does not provide this all-q,k fixed-one-operation chromatic equality. A 2015 simplicial rook paper uses arbitrary positive transfers rather than one-unit transfers; its distinct adjacency does not imply these parameters. Historical priority remains bounded, not guaranteed.

## value

PASS

PASS. Determining the minimum number of disjoint one-duplication-correcting codebooks necessary to cover all length-n words is a natural exact invariant of a canonical zero-error coding graph. The explicit linear-time coloring and sharp clique obstruction work uniformly for every q,k,n, not just a numerical instance, and are not determined by known edge counts or correction-code rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
