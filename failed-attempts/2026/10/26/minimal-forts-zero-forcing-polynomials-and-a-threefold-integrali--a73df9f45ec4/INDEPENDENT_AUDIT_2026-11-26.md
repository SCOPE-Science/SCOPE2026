# Independent mathematical audit

## correctness

PASS

For a proposed fort with index sets P,Q, an exterior a_i sees |Q|−1_{i∈Q} selected vertices, and analogously for b_i. A same-shore triple is a fort, but no same-shore singleton or pair is. Thus a minimal fort other than a triple has both side sizes ≤2. A singleton selected on one side forces every outside vertex on the other side to be its matched non-neighbor. The only surviving size possibility is n=3 with one selected vertex on one side and the two complementary indices on the other; this fails the neighbor test at an outside vertex on the singleton side. With two on each side, the test requires identical pairs. The resulting aligned quartet is a fort, and the preceding size tests exclude every proper nonempty subfort. Complementing the minimal fort test yields the displayed ordinary forcing polynomial, whose lowest degree is 2n−4 with C(n,2)(C(n,2)−1) sets. For the fort-cover LP, the constant vector 1/3 is feasible. For each shore, summing the triple inequalities gives total weight at least n/3 by the exact incidence multiplicity C(n−1,2), proving the optimum. Equality forces all triple sums to be one. For n≥4 each pair of weights can be compared by using the same two other vertices in the two triples, forcing equality; for n=3 weight one at a_1 and b_2 and zero elsewhere is also feasible and optimal. For K_{n,n}, the same-side pairs are its minimal forts, giving fractional value n and ordinary value 2n−2. Independent literal adjacency/forcing and subset DP for 3≤n≤7 matched exact fort families, every polynomial coefficient, and the triple incidence LP certificate; fort totals were 5,14,30,55,91 and minimum-set counts 6,30,90,210,420. Replay: python3 /workspace/reproductions/check_fan_crown_skew.py crown. The finite check does not prove the all-order result; the LP uniqueness argument is exact. The frozen checker was inspected, not run, and its Python 3.8 note should be 3.10 or later because it uses int.bit_count().

## originality

FAIL

An indexed crown result already gives the exact ordinary membership test and polynomial. Its test mechanically supplies the same minimal-fort hypergraph, from which the fractional optimum and its equality conditions follow directly. Another indexed result states the exact structural and fractional-gap core as well. The explicit optimizer uniqueness clause was not found verbatim in that comparison, but follows directly from tightness of the known triple constraints. No publication priority is inferred from directory dates.

## value

FAIL

A complete cover and gap analysis for crowns is naturally motivated, but the frozen exact quantities already occur in equivalent results or follow immediately from the indexed all-set test. The added uniqueness assertion follows from elementary tight-constraint subtraction on the already determined triple family, not a distinct unresolved structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
