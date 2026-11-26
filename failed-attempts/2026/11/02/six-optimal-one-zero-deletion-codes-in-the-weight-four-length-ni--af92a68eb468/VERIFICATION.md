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

The five labeled zero runs (including prefix and suffix) give a bijection from the 126 length-nine words to weak compositions of 5 into 5 parts; an output corresponds to decrementing one positive coordinate. Distinct inputs share an output iff they differ by a single unit transfer, i.e. their ordinary ℓ1 distance is 2. The checksum changes by a nonzero residue on each transfer. The zero fiber has size (126+4)/5=26 by the root-of-unity filter, since every nontrivial Fourier term has generating function (1−z^5)^{-1}. The frozen verify.py branches exhaustively on membership of still-available vertices; a nonnegative clique cover with total weight W bounds every remaining independent set by W, so its strict rational prunes have the right direction. The supplied verifier and certificate were inspected as evidence, not executed. An independent exact computation at /workspace/branches/d3ebd70a-26e7-4975-ba94-879b723cb5c8/independent_check.py uses the complementary compatibility graph and greedy proper-coloring bounds on the remaining vertex prefixes; choosing vertices in reverse order partitions all extensions by their first chosen candidate. It found no 27-clique and exactly six 26-cliques; all are the orbit from 120 coordinate permutations (saved independent_check_output.txt). The affine group of size 20 preserves the zero checksum since the total is 5; orbit size six makes it the entire stabilizer. This is the normalizer of the cyclic translation subgroup: a normalizing permutation sends translation by 1 to translation by a nonzero a and has form i↦ai+b. Thus the orbit is indexed by the conjugate cyclic order-five subgroups. The result is specific to a single zero deletion and uses a complete finite enumeration, not a numerical optimizer or a general deletion theorem.

## originality

FAIL

Resultary 18af41f331e1 explicitly gives the same six labeled maximal-size codes, checksum orbit, stabilizer and size, under its five-symbol size-five multiset formulation. Zero-run counts identify the input and output sets and preserve each possible deletion, so this is exact equivalent coverage. The older profile-graph work also contains the optimum 26; the distinct part claimed in the frozen record, the six-code classification, is itself fully covered by the indexed multiset record.

## value

FAIL

A complete maximum packing classification is a natural question, but at this scope the frozen record recodes a known complete classification with the same labeled conflict graph and checksum orbit. The additional rational branch certificate and the interpretation of the affine stabilizer in terms of cyclic subgroups do not supply a new mathematical boundary or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
