# Integral critical group of the Steiner–Plücker incidence graph

## Finding

Let six distinct points in sufficiently general position lie on a smooth conic over an algebraically closed field of characteristic zero. The classical Steiner–Plücker configuration of the complete Pascal hexagon has twenty Steiner points and fifteen Plücker lines, with three lines through each point and four points on each line. Let \(\Gamma\) be its unweighted bipartite incidence graph. Then \(\Gamma\) is connected, has 35 vertices and 60 edges, and

\[
K(\Gamma)\cong (\mathbb Z/2\mathbb Z)^2\oplus(\mathbb Z/10\mathbb Z)^2\oplus(\mathbb Z/30\mathbb Z)^2\oplus(\mathbb Z/180\mathbb Z)^4.
\]

In particular, its exponent is \(180\), its order is \(2^{14}3^{10}5^8\), and its spanning-tree count is
\[
\tau(\Gamma)=377913600000000.
\]

Consequently every regular split semistable smoothing with unit node thicknesses of a stable genus-26 rational-component curve with this dual graph has this geometric Néron component group. The latter is conditional on the stated smoothing and does not identify the Jacobian of the original conic.

## Assumptions and scope

The configuration is the generic characteristic-zero classical Steiner–Plücker configuration, not a special sextuple in which distinct prescribed incidences may collide. Its graph is an *abstract incidence graph*: the two vertex classes are distinct and its edges carry unit weight. For any connected finite graph \(G\), write \(L_G\) for the degree-minus-adjacency Laplacian, and define \(K(G)\) to be the torsion subgroup of \(\operatorname{coker}_{\mathbb Z}L_G\); equivalently it is the cokernel of any reduced Laplacian, for a connected graph. A semistable application assumes every irreducible component of the special fibre is a smooth rational curve, each node is an ordinary split double point, the total space is regular and each node has thickness one.

## Proof

**Canonical labelled incidence.** Boben–Gévay–Pisanski, Lemma 4.5, identifies this configuration with the incidence structure on three-element and two-element subsets of a six-element label set: a two-set \(a\) is incident with a three-set \(t\) precisely when \(a\subset t\). Indeed their seven-hyperplane construction singles out one distinguished hyperplane; stripping its index from the quadruple and triple indices leaves exactly these subset ranks. Consequently, in lexicographic order, the full integer incidence matrix is uniquely specified by
\[
B_{a,t}=\mathbf 1_{a\subset t},\qquad a\in\binom{[6]}2,\quad t\in\binom{[6]}3.
\]
There are \(15\) two-sets, \(20\) three-sets, \(4\) incidences per two-set and \(3\) per three-set. Its \(35\)-vertex Laplacian is
\[
L=\begin{pmatrix}4I_{15}&-B\\-B^{\mathsf T}&3I_{20}\end{pmatrix}.
\]

**Connectivity and spectrum.** Let \(N\) be the \(6\)-by-\(15\) singleton/two-set incidence matrix. Counting common containing three-sets gives
\[
BB^{\mathsf T}=2I_{15}+N^{\mathsf T}N,
\qquad NN^{\mathsf T}=4I_6+J_6.
\]
Thus \(BB^{\mathsf T}\) has eigenvalues \(12\) (multiplicity one), \(6\) (multiplicity five), and \(2\) (multiplicity nine). The nonzero eigenvalues of \(L\) consist of \(7\) (once), \(1,6\) (five times each), \(2,5\) (nine times each), and \(3\) (five times); zero occurs once. This follows by solving \((4-\lambda)(3-\lambda)=\mu\) for each positive Gram eigenvalue \(\mu\), with five additional \(3\)'s from \(\ker B\). There is exactly one zero eigenvalue, so \(\Gamma\) is connected. The matrix-tree theorem then gives
\[
\tau(\Gamma)=\frac{7\cdot 6^5\cdot 5^9\cdot 3^5\cdot2^9}{35}=2^{14}3^{10}5^8.
\]
The cycle rank is \(60-35+1=26\).

**Integral structure.** Remove the first two-set vertex and denote the resulting \(34\)-by-\(34\) integer matrix by \(R\). The exact finite calculation is fully specified by the preceding entry formula. An independent prime-local Smith elimination over \(\mathbb Z/(p^9)\) yields the following valuations of its 34 nonzero invariant factors:

| Prime \(p\) | Valuation zero | Valuation one | Valuation two |
| --- | ---: | ---: | ---: |
| \(2\) | 24 | 6 | 4 |
| \(3\) | 28 | 2 | 4 |
| \(5\) | 26 | 8 | 0 |

At each step the algorithm selects a trailing entry of minimal \(p\)-adic valuation, applies row and column permutations and clears that pivot row and column with a unit inverse modulo \(p^{9-v}\), where \(v\) is the pivot valuation. All 34 pivots have valuation at most two, so the finite modulus loses no Smith valuation information. The determinant already determines that no other primes occur. Pairing the sorted elementary divisors prime by prime gives exactly 24 unit invariant factors, followed by
\[
2,2,10,10,30,30,180,180,180,180.
\]
The product of these factors equals the matrix-tree determinant. The same prime-local counts arise when a three-set vertex is deleted instead, and an independent exact integer Smith computation agrees. This establishes the asserted group, not merely its order.

**Semistable interpretation.** A connected stable nodal curve formed by gluing 35 rational components along these 60 incidence edges has arithmetic genus 26; all components have at least three nodes. For any regular unit-thickness split semistable smoothing, the standard intersection-matrix description of the geometric Néron component group identifies it with \(K(\Gamma)\).

## Verification

Two complete reproducible programs are included. Run `python3 verify_integral.py` (standard library only), which constructs the incidence graph from combinations, proves the Gram identity entrywise, computes two 34-by-34 cofactors using fraction-free integer elimination and independently computes the prime-local Smith valuation profiles at \(p=2,3,5\). Run `python3 verify_sympy.py` with SymPy installed for a separate exact characteristic-polynomial computation and the complete integer Smith form after deleting a vertex of each bipartition class. The first script ends with `STEINER_PLUCKER_INTEGRAL_CERTIFICATE_OK`; the second ends with `STEINER_PLUCKER_SYMPY_CROSSCHECK_OK`. Neither depends on a previously saved matrix or another research record.

## Relationship to prior work

The Steiner–Plücker incidence itself, its dual Cayley–Salmon configuration, and their occurrence as subconfigurations of the Danzer configuration are classical and explicitly documented by Boben–Gévay–Pisanski (2013, Sections 2 and 4). Those facts are not claimed as new. The rectangular subset-inclusion Smith form is covered by established methods such as Wilson's results and Ducey et al. (2023). That rectangular map is not the square degree-minus-adjacency Laplacian above; in particular, its own Smith invariants do not directly supply the component group or its \(p\)-local valuations. Ducey–Hill–Sin's Kneser graph critical-group results concern a graph on just one rank of subsets, not this 35-vertex bipartite incidence graph. An earlier calculation of the Pascal-line/opposite-chord-intersection graph uses 105 vertices and a different incidence relation, hence does not imply this 35-vertex answer. The dual Cayley–Salmon realization shares the *same* abstract graph and is included in this single claim rather than counted as a separate finding.

## Limitations

The claim concerns the generic characteristic-zero geometric incidence lattice, not special moduli, collisions in positive characteristic, weighted dual graphs, or arbitrary nonregular smoothings. The critical group is not the Picard discriminant of the conic or the Jacobian of a general plane quartic. The computation gives one exact naturally defined graph invariant; it is not a formula for all rank-selected Boolean incidence graphs. The literature comparison is not an assertion of exhaustive historical priority, and independent review has not been carried out.

## References

1. M. Boben, G. Gévay and T. Pisanski, *Danzer's configuration revisited*, arXiv:1301.1067 (first version 2013-01-06), especially Sections 2 and 4 and Lemma 4.5. https://arxiv.org/abs/1301.1067
2. J. E. Ducey, L. Engelthaler, J. Gathje, B. Jones, I. Pfaff and J. Plute, *Integer diagonal forms for subset intersection relations*, arXiv:2310.09227 (first version 2023-10-13), especially introduction and Sections 1–4. https://arxiv.org/abs/2310.09227
3. J. E. Ducey, I. Hill and P. Sin, *The critical group of the Kneser graph on 2-subsets of an n-element set*, arXiv:1707.09115 (2017-07-28). https://arxiv.org/abs/1707.09115
