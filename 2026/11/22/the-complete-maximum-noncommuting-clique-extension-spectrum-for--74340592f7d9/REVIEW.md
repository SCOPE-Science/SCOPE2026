# Independent mathematical audit

## correctness

PASS

The central commutator pairing is nondegenerate and identifies noncommutation with pairing one. The Gram matrix J+I has full rank at even size and only the all-ones kernel at odd size. A 2r-clique basis exists by equivalence of nondegenerate alternating forms; adjoining its sum realizes the 2r+1 bound. Any ordered maximum clique is such a basis and its sum, giving a sharply transitive symplectic action and the full symmetric unordered stabilizer. For an even t-clique its span splits off, and the simultaneous neighbors are its sum plus the orthogonal complement; translating preserves the pairings between new vectors, so the count is the complement's maximum-clique count (or a singleton at t=2r). At odd t a vanishing sum makes the neighbor equations inconsistent, including a central singleton; otherwise the last fixed vector corresponds to a fixed nonzero vector of a complement of dimension d=2r-t+1. Its clique incidence is (d+1)/(2^d-1) of that complement's total by transitivity. This gives both denominators and the exact power of 2; each unprescribed coset has z independent lifts. The empty, maximum and rank-one cases agree. The independent transvection-orbit and clique-incidence calculation /workspace/audit-replay/1.py (output 1.txt) checked every clique in ranks 1–3: 8, 192, 26896 total clique instances and 1, 6, 288 projected maximum cliques. The proof, not the finite tests, covers all ranks.

## originality

PASS

Best-of-knowledge pass on the all-arity prescribed-clique incidence law, not on the maximum-size bound or the underlying graph. The total follows directly from the simplex orbit and stabilizer and is not by itself a distinct contribution. No inspected statement establishes the full even/odd law with its dependence split; classical complement geometry and incidence counting explain the additional reduction required.

## value

PASS

The result measures how the natural maximum simplices intersect and extends a known clique-size invariant to every prescribed clique, with a sharp dependence obstruction and unique projected completion two below full even rank. The incidence and lift formula is reusable for counting configurations in central extensions without recovering the group's power map. The simple total by itself would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
