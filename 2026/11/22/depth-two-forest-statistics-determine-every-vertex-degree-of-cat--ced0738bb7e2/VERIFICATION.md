---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The vertices are precisely the Dyck up-step incidence vectors, and a neighbor differs by one swapped U and D by the matroid-base edge theorem. A swap with the earlier step D always raises intervening heights; with the earlier step U it is legal iff all affected heights are ≥2. As an independent count, let t_j be the size of top-level component j. Between two components only raising swaps are possible, giving t_j t_l for j<l. Within one component its root's two steps cannot participate in a legal internal swap. Between two different depth-two blocks only raising swaps are legal, giving s_i s_h for i<h; within any one block all s_i² pairs of unlike symbols are legal. Thus the total inside component j is binom(t_j,2)+sum_i binom(s_i,2) over its depth-two blocks, using t_j=1+sum_i s_i. Adding cross-component swaps gives the stated formula. A block of size s contains C_{s−1} choices and has weight z^s q^binom(s,2); a root is z times a sequence of these blocks, and the forest is a sequence of roots. This gives (1−H)/(1−z−H) and the stated recurrence with the s=n term cancelled. Excess zero means each block has size one, i.e. path height ≤2; there is one such forest per composition of n. For n≥3, binom(sum_i s_i,2)≤binom(n−1,2), with equality in the excess iff there is one root with one block of size n−1, giving UUQDD and C_{n−2} choices. The n=1,2 cases tie as stated. The finite checker was read; its checks are corroboration only.

## originality

PASS

The matroid, adjacency criterion, local legal-swap rule and aggregate edge count are prior. The supported distinct claim is the evaluated depth-two formula for each undirected degree, with its refined series and equality families. The best indexed near match has a different adjacency relation, despite sharing the maximum value.

## value

PASS

In the natural basis graph of a classical matroid, the subtree reduction gives an exact local connectivity invariant without enumerating exchanges. Its distribution refines known total edge counts and identifies every extremal path. The rigid equality families and the ease of evaluating the degree can inform study of this exchange graph independently of any new mixing bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
