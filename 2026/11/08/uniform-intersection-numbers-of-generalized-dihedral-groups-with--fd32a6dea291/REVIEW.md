# Self-review

## Correctness — PASS
The statement fixes the odd-order abelian kernel, the inversion action, the meaning of distinct maximal subgroups and both intersection-number quantifiers. The maximal-subgroup classification and their coset multiplicities are proved directly. Counting hyperplanes omitting a given vector yields the exact maximal containment number, with reflections counted separately. The minimum-intersection lower bound uses the solvability of independent affine constraints; the matching construction is explicit. The four independent exhaustive subset enumerations and script replay agree with the formulas, but finite checking is not used to infer the universal theorem.

## Originality — PASS with residual historical-priority risk
The closest primary source, Choudhury and Khanra (arXiv:2610.22268, Section 2, Theorem 2.6), states and proves the uniform result for ordinary dihedral groups with **cyclic** rotation subgroup, including the formulas recovered here when all Sylow ranks are one. Archer and collaborators (arXiv:1907.02898, Section 4, Proposition 4.1) treat minimal intersections for the same cyclic family. Neither inspected full text states the generalized-dihedral all-abelian-Sylow-rank formula or the worst-case rotation-versus-reflection containment comparison. Related prior work on generalized-dihedral independence and generating graphs concerns different graph invariants and is not automatically equivalent. The proposed formula could nonetheless be an unrecorded consequence of older maximal-subgroup literature; independent historical verification remains outstanding.

## Mathematical value — PASS
Uniform intersections are the all-choices strengthening of minimal Frattini intersections. The existing exact dihedral theorem leaves a natural, potentially much larger family untreated. The new rank-profile formula handles all odd abelian kernels, distinguishes minimum from worst-case behavior, and exhibits an unbounded gap already for the elementary-abelian kernel of fixed rank two. It is a complete invariant in a mathematically motivated family rather than an arbitrary numerical example. The odd-order hypothesis matters for the subgroup and reflection-fiber structure, and broader semidirect products remain unclassified.

## Closest sources and limitations
The main literature overlap is the cyclic-kernel theorem of Choudhury–Khanra (2026), itself built on Archer and collaborators (2019). Full-text examination of generalized-dihedral minimum-size independence-graph work found pair-adjacency and degree results, not the present maximal-subgroup intersection invariant. The checker uses exact enumeration of groups of orders 18, 30, 54 and 90 and cannot verify infinite families. Potential equivalent terminology in earlier group theory remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
