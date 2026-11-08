# Scientific review

## Correctness — PASS

The claim is precisely the maximum number of length-\(n\) binary words that can be selected under distinct one-deletion descendant multiplicity at most two, for \(2\le n\le7\). It is encoded by a complete \(0/1\) incidence matrix with all binary words and all shorter outputs. Explicit feasible codes give every lower bound. For every upper bound, a complete branch tree checks either a forbidden output multiplicity, a trivial remaining-word count, or nonnegative rational dual multipliers satisfying the inequality for **every** unassigned word. The scaled-integer inequalities prove the strict upper bound below the next integer; no floating-point assertions are trusted. Extracted `checker.py` and `certificate.json` verified all six values, with \(103\) exact proof nodes at \(n=7\). A separate 25-node capacity-one proof tree also independently verifies the known length-seven unique-decoding maximum \(16\), needed for the non-decomposability consequence. There is no claim beyond this finite range.

## Originality — PASS against the inspected literature

The 2026 list-deletion work of Lin (arXiv:2609.26650) gives the general hypergraph definition and asymptotic existence theorem, not these length-seven finite cardinalities. The 2026 work of Kiah–Wei–Zeng (arXiv:2609.21395) discusses the length-two list-two example and general constant-list bounds, not the length-seven optimum or the non-decomposability statement. No's 2019 single-deletion MILP study concerns unique correction (capacity one), while the present model permits capacity two. Published nearby finite two-deletion/two-list and mixed deletion–substitution computations concern different incidence matrices. published-finding corpus search was performed for the claim, aliases, parameters, VT equivalences, and broader covering results. The priority risk is an unindexed small-blocklength list-decoding table or an equivalent two-fold hypergraph packing census.

## Value — PASS

The bound \(33\) at length seven is the first finite length in the tested complete profile where two-list decoding strictly exceeds both a pair of VT syndrome classes (size \(32\)) and twice the maximal unique single-deletion code size (also \(32\)). Thus list-size two offers more than concatenating two disjoint uniquely decodable codebooks, a distinct structural phenomenon with direct relevance to worst-case short-blocklength synchronization storage. The finite exact optimum is a natural channel invariant, and the calculation comes with portable rational proof rather than solely numerical optimization.

## Limitations and literature comparison

The result does not determine longer blocklengths, q-ary alphabets, or all extremizers. The separate uniqueness bound \(A_2(7;1,1)=16\) is established published work, independently re-certified here only as a supporting lemma and not claimed novel. The exact code profile is independently checkable but has no independent mathematical audit. Search failure does not prove universal historical novelty.

Self-review: passed. Independent audit: not yet performed.
