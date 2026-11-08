# Complete automorphism characters of the Möbius–Kantor independence complex

## Finding

For the 16-vertex Möbius–Kantor graph \(M=\operatorname{GP}(8,3)\), the complete graph-automorphism group \(G=\operatorname{Aut}(M)\) has order 96 and 13 conjugacy classes. The complete rational characters on the only nonzero reduced homology groups are given in the table below. The 4-dimensional third-homology character has self-inner-product two, and neither degree has a nonzero \(G\)-invariant rational class.

| Class | Size | Order | Permutation representative on 0–15 | \(\chi_3\) | \(\chi_4\) |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | `0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15` | 4 | 1 |
| 2 | 1 | 2 | `4,5,6,7,0,1,2,3,12,13,14,15,8,9,10,11` | 4 | 1 |
| 3 | 2 | 4 | `10,15,12,9,14,11,8,13,2,7,4,1,6,3,0,5` | -4 | -1 |
| 4 | 6 | 2 | `1,0,7,6,5,4,3,2,9,8,15,14,13,12,11,10` | 0 | -1 |
| 5 | 6 | 4 | `2,3,4,5,6,7,0,1,10,11,12,13,14,15,8,9` | 0 | 1 |
| 6 | 8 | 3 | `0,7,15,12,4,3,11,8,1,6,10,9,5,2,14,13` | 1 | 1 |
| 7 | 8 | 12 | `1,2,10,13,5,6,14,9,0,3,15,8,4,7,11,12` | -1 | -1 |
| 8 | 8 | 6 | `2,10,15,7,6,14,11,3,1,13,12,0,5,9,8,4` | 1 | 1 |
| 9 | 8 | 12 | `3,4,12,15,7,0,8,11,2,5,9,10,6,1,13,14` | -1 | -1 |
| 10 | 12 | 2 | `0,1,9,12,4,5,13,8,7,2,14,15,3,6,10,11` | -2 | 1 |
| 11 | 12 | 2 | `1,0,8,13,5,4,12,9,2,7,11,10,6,3,15,14` | 2 | -1 |
| 12 | 12 | 8 | `1,2,3,4,5,6,7,0,9,10,11,12,13,14,15,8` | 0 | -1 |
| 13 | 12 | 8 | `2,3,11,14,6,7,15,10,1,4,8,9,5,0,12,13` | 0 | 1 |

## Assumptions and scope

Let the vertices be \(u_0,\ldots,u_7,v_0,\ldots,v_7\), with subscripts modulo eight. The edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). The complex \(X\) contains all independent subsets; vertex permutations are in the displayed order \((u_0,\ldots,u_7,v_0,\ldots,v_7)\). The characters \(\chi_j(g)\) are traces on \(\widetilde H_j(X;\mathbb Q)\). A representative tuple records the images of vertices 0 through 15. The 13 rows are in increasing order of class cardinality, then lexicographically by their least representative. No assertion about integral representation lattices or equivariant homotopy types is made.

## Proof

First enumerate all independent vertex sets by checking every nonempty subset of the 16 vertices against the 24 edges. The resulting numbers of faces in dimensions zero through seven are \((16,96,272,376,240,72,16,2)\). With each face canonically ordered, construct the signed integer simplicial boundary \(\partial_k[v_0,\ldots,v_k]=\sum_{i=0}^k(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_k]\). Exact rational ranks for \(\partial_1,\ldots,\partial_7\) are \((15,81,191,181,58,14,2)\); direct subtraction establishes \(\widetilde H_3(X;\mathbb Q)\cong\mathbb Q^4\), \(\widetilde H_4(X;\mathbb Q)\cong\mathbb Q\), with all other reduced rational homology zero.

Enumerate graph automorphisms as all permutations preserving adjacency. Exact backtracking enumerates 96 maps, and conjugation divides them into 13 classes with sizes shown. For a map \(g\), the signed fixed-face sum \(\widetilde L(g)=-1+\sum_{k=0}^7(-1)^k\sum_{\sigma\in X_k: g\sigma=\sigma}\operatorname{sgn}(gert_\sigma)\) is its reduced Lefschetz number. Thus \(\widetilde L(g)=-\chi_3(g)+\chi_4(g)\).

To determine the degree-four sign, compute the one-dimensional \(H^4(X;\mathbb F_{101})\), verify the same degree-four dimension as the rational calculation, and act on an explicit nonzero cocycle modulo row coboundaries. Its eigenvalue is \(+1\) or \(-1\) for every one of the 96 group maps. Because rational degree-four homology is one-dimensional and reduction has the same dimension, this modulo-101 sign agrees with the rational degree-four character: any rational one-dimensional representation of a finite group with integer trace is a sign representation. Subtracting the signed fixed-face sums gives the degree-three character in every row.

Class-size averaging gives \(\sum_{g\in G}\chi_3(g)=\sum_{g\in G}\chi_4(g)=0\). Character orthogonality gives \(96^{-1}\sum_{g\in G}\chi_3(g)^2=2\). These statements determine the entire rational character, rather than only its restriction to the eightfold rotation subgroup.

## Verification

The standalone programs `mk_rank_exact.py` and `mk_character_certificate.py` each construct the graph and independence complex independently. The former calculates all boundary ranks exactly over \(\mathbb Q\) using integer-domain algebra. The latter verifies \(\partial_4\partial_5=0\), checks the degree-four cocycle modulo 101, enumerates all 96 graph automorphisms and 13 conjugacy classes, computes every signed fixed-face Lefschetz number, and checks each degree-four sign. Their exact recorded standard outputs are included. These are exhaustive finite verifications for the fixed 16-vertex object, not extrapolations from a sample.

## Relationship to prior work

Barmak's 2010 study of independence complexes develops the suspension and star-cluster framework for triangle-free graph independence complexes; its general results do not determine this specific automorphism character. An indexed earlier calculation of the same Möbius–Kantor complex determines only the natural order-eight cyclic restriction of the homology representation. Here all 96 automorphisms and 13 conjugacy classes are treated, giving eight additional noncyclic class types and distinguishing the two homology degrees. A prior exact nonequivariant homotopy computation establishes the underlying ranks, which are independently recomputed here and not claimed as original.

## Limitations

The result gives rational group characters, not integral \(G\)-lattices, torsion information, an equivariant homotopy type, or results for other generalized Petersen graphs. Definitive priority assessment is not established. A closely relevant indexed cyclic-representation record was accessible as a search abstract, but its full repository package was not retrievable; its stated scope cannot cover all noncyclic character values, yet unindexed equivalent computations remain a residual originality risk. Independent mathematical validation has not been performed.

## References

- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02; especially introduction and Theorem 3.4.
- Indexed prior record, *Cyclic symmetry on Möbius–Kantor independence homology*, identifier `2026/10/11/SCOPE-cyclic-symmetry-on-m-bius-kantor-independence-homology--1c198fd64c4e` (only indexed synopsis could be read).
- Indexed prior record, *Integral homotopy type of the Möbius–Kantor independence complex*, identifier `2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3` (nonequivariant prior result).
