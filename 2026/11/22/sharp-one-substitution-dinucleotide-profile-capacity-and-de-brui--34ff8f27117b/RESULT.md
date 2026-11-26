# Sharp one-substitution dinucleotide-profile capacity and de Bruijn extremizers

## Finding

Let \(\Sigma\) be a fixed labeled alphabet of \(q\ge3\) symbols. For a linear length-\(n\) word \(w\), \(n\ge3\), write \(P_2(w)\) for the vector of multiplicities of all oriented, overlapping adjacent pairs. Let \(B_2(w)\) count the distinct vectors \(P_2(v)\) from words \(v\) differing from \(w\) at exactly one position. Then
\[
B_2(w)\le M_q=(q-1)(q^3-q+2).
\]
The bound is first attained at \(N_q=q^3+2\) and is attained at every larger length. At length \(N_q\), equality holds exactly for the words whose consecutive three-letter factors include every possible triple once. The number of such indexed, labeled words is \((q!)^{q^2}\). For \(q=3,4,5,6\), the respective capacities are \(52,186,488,1060\), first attained at lengths \(29,66,127,218\).

## Assumptions and scope

The first and last symbols are not adjacent. A substitution changes one original symbol to a different symbol and leaves length unchanged. The observable is the complete \(q^2\)-coordinate count vector with orientation and multiplicity, not the edited word. Coincident vectors are counted once. No quotient by alphabet permutation or by rotation is taken in counting the linear maximizers.

## Proof

Write \(E_{ab}\) for the unit matrix in ordered coordinate \((a,b)\). For a substitution \(b\to d\), \(d\ne b\), at the center of \(abc\), the change is
\[
\Delta(a,b,c;d)=E_{ad}+E_{dc}-E_{ab}-E_{bc}=R_a+C_c,
\quad R_a=E_{ad}-E_{ab},\quad C_c=E_{dc}-E_{bc}.
\]
Both row- and column-sum vectors are \(e_d-e_b\), so equal interior differences must use the same ordered replacement. For fixed \((b,d)\), a collision cannot change only one neighbor, because the individual row and column terms are each injective in their neighbor. If both neighbors change in \(R_a+C_c=R_{a'}+C_{c'}\), the nonzero rows of \(R_a-R_{a'}\) force \(\{a,a'\}=\{b,d\}\). Comparing nonzero columns similarly forces \(\{c,c'\}=\{b,d\}\). The only equality amongst the four possible neighbor pairs is
\[
\Delta(b,b,d;d)=\Delta(d,b,b;d)=E_{dd}-E_{bb}.
\]
Indeed, the two remaining pairs \((b,b)\), \((d,d)\) give \(E_{bd}+E_{db}-2E_{bb}\) and \(2E_{dd}-E_{db}-E_{bd}\), respectively. Hence the full interior inventory has \(q(q-1)(q^2-1)\) distinct elements.

Changing the first letter gives \(E_{dc}-E_{bc}\), with nonzero row-sum vector \(e_d-e_b\) and zero column sums. Changing the last gives \(E_{ad}-E_{ab}\), with zero row sums and column-sum vector \(e_d-e_b\). These two families and the interior are disjoint, and for either end the \(q-1\) alternatives are distinct. Adding their counts gives the bound \(q(q-1)(q^2-1)+2(q-1)=M_q\).

For any fixed context \(abc\), at least one admissible \(d\) avoids the colliding contexts \((a,c)=(b,d),(d,b)\) when \(q\ge3\). If exactly one neighbor equals \(b\), omit the other neighbor from the replacements; otherwise every replacement is admissible for this purpose. The resulting difference is private to the context, including against boundary differences. An equality word must therefore contain every triple. As a linear word has only \(n-2\) triple windows, equality requires \(n\ge q^3+2\). Linearize a cyclic order-three de Bruijn word by appending its first two letters. It contains all triples, realizes the interior inventory in full, and realizes both sets of end differences. Appending letters preserves all its triple windows and cannot affect the boundary count. At the first equality length there are exactly \(q^3\) windows, so the triple coverage is exact.

For the count, use the digraph on \(q^2\) ordered pairs with an arc \((a,b)\to(b,c)\) for every triple. It is strongly connected and Eulerian with degree \(q\). Its adjacency matrix \(A\) satisfies \(A^2=J\), the all-ones matrix. On the all-ones direction \(A\) acts by \(q\); its restriction to the zero-sum space squares to zero. Thus the product of nonzero eigenvalues of the Laplacian \(qI-A\) is \(q^{q^2-1}\). Its \(q^2\) directed Matrix-Tree cofactors are equal by the Eulerian condition, so the number of in-arborescences to a specified root is \(q^{q^2-3}\). Fixing the first arc of a circuit chooses one representative modulo rotation, since every triple arc occurs once. The BEST formula gives \(q^{q^2-3}((q-1)!)^{q^2}\) cyclic de Bruijn words. Each has \(q^3\) distinct marked starts by uniqueness of triples. Hence there are \(q^3 q^{q^2-3}((q-1)!)^{q^2}=(q!)^{q^2}\) linear equality words at the first length.

## Verification

The bundled standard-library scripts `verify_local.py`, `verify_enumeration.py` and `verify_tree_count.py` check the local classification, literal mutant profiles including de Bruijn witnesses, and exact Laplacian cofactors, respectively. Their recorded outputs end with `LOCAL_CHECK_PASS`, `ENUMERATION_CHECK_PASS`, and `TREE_COUNT_PASS`. The analytic argument, rather than finite sampling, proves the all-parameter claims.

## Relationship to prior work

Profile multiplicities and the local deleted/added-factor bookkeeping are standard. Kiah, Puleo and Milenkovic study profile codes and reconstruction [1]; Simmonds et al. use local mutation accounting for dinucleotide frequencies [2]. En Gad treats long-spectrum uniqueness and linear hashing for multiple edit conflicts [3]. He, Kari and Millan Arias use the Euler/de Bruijn correspondence for reconstruction from a prescribed profile [4]. Published binary insertion and deletion profile-ball findings concern different edits [5, 6]; the ternary bigram multispectrum counts profiles over all words rather than one mutation image from a fixed source [7]. The classical de Bruijn enumeration is used here after establishing the saturation/rigidity theorem; it is not a new count of de Bruijn cycles.

## Limitations

The binary alphabet has the same one-collision-per-replacement classification and the same capacity formula, but the private-difference argument for each triple fails when there is no third symbol. For example, the binary word `00010111` already produces eight distinct profiles at length eight. No general spectrum of the capacities below first attainment, cyclic analogue, multiple-substitution theorem, code-size bound, or historical priority over uninspected work is asserted.

## References

1. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, https://arxiv.org/abs/1502.00517.
2. Simmonds et al., *Modelling mutational and selection pressures on dinucleotides in eukaryotic phyla*, *BMC Genomics* **14** (2013), 610, https://doi.org/10.1186/1471-2164-14-610.
3. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, https://arxiv.org/abs/2609.19493v2.
4. H. He, L. Kari and P. Millan Arias, *Bridging Chaos Game Representations and k-mer Frequencies of DNA Sequences*, https://arxiv.org/abs/2506.22172.
5. *Exact single-insertion dinucleotide-profile ambiguity in binary words*, Resultary, `SCOPE-exact-single-insertion-dinucleotide-profile-ambiguity-in-binary--7545727346c0`.
6. *The complete one-deletion dinucleotide-profile ball distribution for binary words*, Resultary, `SCOPE-the-complete-one-deletion-dinucleotide-profile-ball-distribution--294c530e44d7`.
7. *Exact ternary ordered-bigram multispectrum counts and the degree-six law*, Resultary, `SCOPE-exact-ternary-ordered-bigram-multispectrum-counts-and-the-degree--f0497779133f`.
