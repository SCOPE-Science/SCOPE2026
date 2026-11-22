# Dihedral identifying-code penalties in Lucas cubes through dimension seven

## Finding

For every integer \(2\le n\le7\), let \(\Lambda_n\) be the undirected Lucas cube: its vertices are the binary words of length \(n\) with no two cyclically consecutive ones, and edges join words differing in exactly one coordinate. A radius-one *identifying code* is a vertex set \(C\) for which the signatures \(N[v]\cap C\), over all vertices \(v\), are nonempty and pairwise distinct. Let \(I_n\) be the smallest code size, let \(A_n\) count labeled minimum codes, let \(I_n^{D}\) be the minimum subject to invariance under *all* rotations and reflections of coordinate positions, and let \(A_n^{D}\) count these minimum invariant codes.

The complete exact finite census is:

| \(n\) | Vertices | \(I_n\) | \(A_n\) | \(I_n^{D}\) | \(A_n^{D}\) | Dihedral orbit sizes of unrestricted minimum codes |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 3 | 2 | 1 | 2 | 1 | \(1\) |
| 3 | 4 | 3 | 4 | 3 | 1 | \(1,3\) |
| 4 | 7 | 4 | 13 | 4 | 1 | \(1,4,8\) |
| 5 | 11 | 5 | 21 | 5 | 1 | \(1,5,5,10\) |
| 6 | 18 | 7 | 18 | 8 | 1 | \(6,12\) |
| 7 | 29 | 11 | 259 | 14 | 3 | nine orbits of size \(7\), fourteen of size \(14\) |

Consequently, dimension six is the first dimension \(n\ge2\) in which full coordinate dihedral symmetry strictly increases the required sensor population, and the penalty grows from one sensor to three at dimension seven:

\[
I_6=7<I_6^{D}=8,\qquad I_7=11<I_7^{D}=14.
\]

In dimension seven the three size-fourteen invariant optimal codes are precisely the union of the orbit of all seven weight-one words with, respectively, one of the three remaining nonzero weight-two/weight-three orbits of size seven. The three choices have orbit representatives `0000101`, `0001001`, and `0010101`. Thus all 259 unrestricted minimum codes form exactly 23 dihedral orbits. These are complete classifications in the stated finite domain, not extrapolations.

## Assumptions and scope

Vertices are **labeled** coordinate words. The graph is simple and undirected, and \(N[v]\) denotes its **closed** radius-one neighborhood, including \(v\). No sensor erasures, graph-directed edges, or larger identification radii are admitted. The dihedral action rotates or reverses the \(n\) *positions*, not the binary symbols. It is the natural full automorphism action for \(n\ge3\); for \(n=2\) its induced action has duplicate representatives but is still well defined. Dimensions zero and one are outside the theorem.

Write

\[
V_n=\{w\in\{0,1\}^{n}:w_iw_{i+1}=0\ \text{for all cyclic indices }i\},
\qquad N[v]=\{u\in V_n:d_{\mathrm H}(u,v)\le1\}.
\]

The integer \(A_n\) counts distinct subsets of \(V_n\), not symmetry classes. An invariant code must be fixed *setwise* by every dihedral transformation, not pointwise by each.

## Proof

**1. A complete finite covering criterion.** For a candidate \(C\subseteq V_n\), put \(S_v=N[v]\cap C\). The signatures are nonempty exactly when \(C\cap N[v]\ne\varnothing\) for every \(v\). They are distinct exactly when, for every two different vertices \(u,v\), the symmetric difference \(S_u\triangle S_v=C\cap(N[u]\triangle N[v])\) is nonempty. Thus \(C\) is identifying if and only if it hits every member of the explicit constraint family

\[
\mathcal F_n=\{N[v]:v\in V_n\}\cup\{N[u]\triangle N[v]:u,v\in V_n,\ u\ne v\}.
\]

This equivalence is exact and applies to every possible code. A superscript-free identifying set is therefore closed upward under enlargement. Consequently, showing that **no** code of size \(k-1\) exists excludes *every* smaller size as well.

**2. Exhaustive lower bounds and complete counts.** Enumerate the admissible binary words in integer order. For each vertex form a bitmask of its closed neighborhood and, for every unordered pair, a mask of their symmetric difference. For a candidate \(k\)-subset, form its bitmask and test that its bitwise intersection with each constraint is nonzero. There are exactly \(\binom{|V_n|}{k}\) candidates. The primary verifier enumerates every candidate of sizes \(I_n-1\) and \(I_n\), without sampling or a solver timeout. It finds zero at the smaller size and exactly the listed \(A_n\) at the larger size. In the largest case it checks all \(20{,}030{,}010\) ten-subsets and all \(34{,}597{,}290\) eleven-subsets of the 29-vertex cube. A second implementation independently checks all vertex signatures directly and recursively enumerates the same subset sizes; its results agree.

For example, an attaining eleven-sensor code in \(\Lambda_7\) is

`0000000 0000010 0000101 0001000 0001010 0010000 0010100 0100000 0100001 1000000 1000010`.

Every listed word is a Lucas word; the direct signature test verifies all 29 signatures are nonempty and distinct. This gives the constructive upper bound, while the exhaustive ten-subset exclusion gives the lower bound.

**3. Full symmetry quotient and invariant optima.** Each rotation/reflection maps \(V_n\) to itself and preserves Hamming adjacency, hence preserves identifying codes. Apply each of the \(2n\) transformations to every enumerated minimum code and partition the complete set into distinct orbits; this yields the orbit-size multiset in the table. A code is invariant under the entire dihedral group exactly when it is a union of full **vertex** orbits. Enumerating all unions of the vertex-orbit masks, and testing the same exact hitting condition, proves every stated \(I_n^{D}\) and \(A_n^{D}\).

In \(\Lambda_6\), the five vertex orbits have sizes \(1,6,6,3,2\); the unique smallest invariant identifying set has size eight and is all six weight-one words plus `010101` and `101010`. In \(\Lambda_7\), the vertex orbits have sizes \(1,7,7,7,7\), so an invariant code of size at most 13 may contain at most one seven-orbit plus (optionally) the zero word. None of these possibilities meets all identification constraints. Exactly three of the six unions of two seven-orbits work, and they are precisely the three described in the finding. Thus \(I_7^{D}=14\) independently has a transparent 32-case orbit-union certificate.

## Verification

The package contains `verify_lucas.cpp` and the independently implemented `alternate_lucas.cpp`, both requiring only standard C++17. From their directory, run:

```sh
g++ -O3 -std=c++17 verify_lucas.cpp -o verify
./verify
g++ -O3 -std=c++17 alternate_lucas.cpp -o alternate
./alternate
```

The expected terminal markers are `VERIFY_OK` and `ALTERNATE_OK`. Both completed successfully on the delivered source bytes. The primary implementation uses a bitmask hitting-family test and fixed-cardinality mask iteration. The alternate implementation constructs the actual word signatures, uses recursive combination generation and separately computes the group action. `CENSUS.json` records the verified values and concrete witnesses. The proofs of lower bounds are finite and exhaustive for the declared dimensions; neither an integer-programming status code nor an uninspected solver log substitutes for enumeration.

## Relationship to prior work

Castro, Klavžar, Mollard and Rho determined domination and two-packing information for Fibonacci and Lucas cubes, and described the dihedral automorphisms of Lucas cubes; these invariants are not identifying-code minima, since domination alone does not ensure pairwise distinct signatures and two-packing instead requires disjoint radius-one balls. Ashrafi and collaborators subsequently determined vertex and edge **orbits** of Fibonacci and Lucas cubes in all dimensions, but not orbits of identifying-code sets or their minima. The exact group action used here agrees with those prior graph automorphisms.

Mollard proved that ordinary Lucas cubes of dimension at least four do not admit *perfect error-correcting codes*, i.e. disjoint radius-one balls covering all vertices. That is a different condition from requiring all closed-neighborhood intersections with a sensor set to be nonempty and different, so it neither implies nor rules out the present codes. General identifying-code set-cover formulations and exact values on other graph families also do not supply these Lucas-cube counts. A known small-dimensional identifying-code census on *Fibonacci* cubes uses linear rather than cyclic adjacency constraints and has different vertex sets and symmetry groups; its exact numbers do not imply the Lucas results.

## Limitations

Only integer dimensions \(2\) through \(7\) are claimed. The conclusions do not establish a formula or growth law for larger cubes, nor robustness to defective sensors. The closed-neighborhood convention and full coordinate-dihedral invariance are essential. Although relevant inspected references and scientific search records do not supply this exact classification, an unindexed earlier computation cannot be excluded.

## References

1. A. Castro, S. Klavžar, M. Mollard, Y. Rho, *On the domination number and the 2-packing number of Fibonacci cubes and Lucas cubes*, public preprint hal-00535686v1 (November 12, 2010), *Computers & Mathematics with Applications* **61** (2011), 2655–2660. [Public preprint record](https://hal.science/hal-00535686); [accessible manuscript](https://www.academia.edu/164533876/On_the_domination_number_and_the_2_packing_number_of_Fibonacci_cubes_and_Lucas_cubes).
2. A. R. Ashrafi, J. Azarija, K. Fathalikhani, S. Klavžar, M. Petkovšek, *Vertex and edge orbits of Fibonacci and Lucas cubes*, arXiv:1407.4962 (first posted July 18, 2014). [arXiv record](https://arxiv.org/abs/1407.4962).
3. M. Mollard, *The (non-)existence of perfect codes in Lucas cubes*, arXiv:2004.10198 (April 21, 2020). [arXiv record](https://arxiv.org/abs/2004.10198).
4. *Polyhedra associated with identifying codes in graphs*, *Discrete Applied Mathematics* (2017), DOI:10.1016/j.dam.2017.06.005. [Article](https://doi.org/10.1016/j.dam.2017.06.005).
