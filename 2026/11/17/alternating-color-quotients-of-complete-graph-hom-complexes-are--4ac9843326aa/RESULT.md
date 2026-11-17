# Alternating-color quotients of complete-graph Hom complexes are integral sphere wedges

## Finding

Let \(2\le m\le n\) be integers and let \(X_{m,n}=\operatorname{Hom}(K_m,K_n)\) be the polyhedral graph-homomorphism complex. The alternating group \(A_n\) acts by even permutations of the target-color labels. Its ordinary geometric orbit space has the integral homotopy type

\[
\boxed{|X_{m,n}|/A_n\simeq\bigvee^{\binom{n-2}{m-2}}S^{n-m}.}
\]

For \(n=m\), the right side means two discrete points (one copy of \(S^0\)); for \(n=m+1\) it is a wedge of \(m-1\) circles. In every dimension at least two, the quotient is simply connected and has no torsion in integral homology. The assertion is a homotopy equivalence of ordinary orbit spaces, not a homeomorphism, an equivariant wedge decomposition, or a Borel-homotopy statement. In particular, it upgrades the previously established *rational* alternating-color quotient Betti rank to a complete integral homotopy classification.

## Assumptions and scope

The graphs \(K_m,K_n\) are finite loopless complete graphs. A cell of \(X_{m,n}\) is an ordered \(m\)-tuple \((A_1,\dots,A_m)\) of pairwise disjoint nonempty subsets of \([n]\), with cell closure \(\prod_i\Delta(A_i)\). Equivalently, a point is a nonnegative \(m\)-by-\(n\) real matrix with every row summing to one and pairwise disjoint nonzero row supports. A target-color permutation acts by permuting columns. We write \(d=n-m\). The ordinary orbit-space quotient is defined using the actual finite group action on the geometric realization. The zero-dimensional convention is stated in the finding.

## Proof

**1. An explicit cell model for the full symmetric quotient.** For any point, sort the positive weights *independently within each row* into weakly decreasing order \(x_{i,1}\ge x_{i,2}\ge\dots\ge0\). The unordered multiset of nonzero columns is a complete invariant for the \(S_n\)-orbit, because each column has at most one positive entry. Put \(x_{i,n+1}=0\) and define

\[
t_{i,j}=j(x_{i,j}-x_{i,j+1}),\qquad 1\le j\le n.
\]

Then \(t_{i,j}\ge0\) and \(\sum_jt_{i,j}=\sum_jx_{i,j}=1\). Conversely, \(x_{i,j}=\sum_{h\ge j}t_{i,h}/h\). For each row let \(S_i=\{j:t_{i,j}>0\}\) and \(\ell_i=\max S_i\). Exactly \(\ell_i\) colors occur in that row, so the permissible points satisfy \(\ell_1+\cdots+\ell_m\le n\). Hence the compact Hausdorff quotient \(B=|X_{m,n}|/S_n\) is homeomorphic to the finite union of product simplices

\[
B=\bigcup_{\substack{S_i\subseteq[n],\ S_i\ne\varnothing\\\sum_i\max S_i\le n}}\prod_{i=1}^m\Delta(S_i)
\subseteq (\Delta^{n-1})^m,
\]

with disjoint relative interiors indexed by the indicated \(m\)-tuples of nonempty supports. Each product cell has dimension \(\sum_i(|S_i|-1)\le d\). For every \(b=(t_i)\in B\), the segment from \(b\) to the common vertex \(v=(e_1,\dots,e_1)\) remains in the product cell obtained by adjoining \(1\) to each row support: its largest index is unchanged. Thus straight-line contraction proves \(B\) contractible.

**2. The two-sheeted/one-sheeted quotient cell structure.** Consider \(Y=|X_{m,n}|/A_n\) and the natural surjection \(p:Y\to B\). The stabilizer in \(S_n\) of a point contains an odd permutation if and only if two columns are identical. Since columns have disjoint positive row supports, this happens exactly when either (a) at least two colors are unused, or (b) two positive entries in some row are equal. In the sorted-coordinate interior labeled by \((S_i)\), (b) means a missing index strictly below \(\max S_i\), because \(x_{i,j}=x_{i,j+1}\) precisely when \(t_{i,j}=0\). Consequently an open product cell has exactly *two* distinct lifts to \(Y\) if and only if every \(S_i\) is the complete initial interval \(\{1,\ldots,a_i\}\) and \(\sum_i a_i=n\) or \(n-1\); every other open cell has exactly *one* lift. Its closure is a finite CW cell mapping homeomorphically under \(p\) to the corresponding closed product cell in \(B\), with possible identifications of boundary faces but no identifications within each closed product cell: a parity label of a representative is unique in the interior without odd stabilizers and collapses precisely along branching faces. These characteristic maps give a finite cellular quotient and cellular projection \(p\), with an orientation inherited from the product-simplex coordinates \(t_{i,j}\).

**3. The integral difference-chain complex.** The induced map of integral cellular chains \(p_\#:C_*(Y;\mathbb Z)\to C_*(B;\mathbb Z)\) is degree \(+1\) on each oriented lifted cell (choose its orientation using \(p\)), and is surjective. Its kernel \(D_*\) has one integral generator \([a,+]-[a,-]\) for each unbranched product cell of the preceding step, and no other generators. A two-sheet cell with intervals of sizes \(a_1,\dots,a_m\) has dimension \(\sum_i(a_i-1)=\sum_i a_i-m\). It follows that the *only* possible nonzero groups of \(D_*\) are

\[
D_d\cong\mathbb Z^{\binom{n-1}{m-1}},\qquad
D_{d-1}\cong\mathbb Z^{\binom{n-2}{m-1}},
\]

where a binomial coefficient is zero if its upper index is smaller than the lower. The top generators are positive compositions \(a_1+\dots+a_m=n\); lower generators are positive compositions with sum \(n-1\).

Give each product cell the standard orientation, ordering rows \(1,\dots,m\) and initial interval simplex coordinates increasingly. Removing any vertex other than the last one in a row introduces an equality between adjacent sorted coordinates and hence lands in a branched single-sheet cell; the two sheet-boundaries cancel there in \(D_*\). Removing the last vertex of row \(i\) gives a lower unbranched cell exactly when \(a_i\ge2\). The ordinary oriented-simplex face sign is \((-1)^{\sum_{j<i}(a_j-1)+a_i-1}\). Moving the released target-color label past the \(\sum_{j>i}a_j\) later-row labels to the canonical unused slot changes sheet parity by that number modulo two. The combined difference-chain coefficient is therefore the integral unit \((-1)^{n-i}\), independent of \(a\). Hence the complete boundary is

\[
\partial_D[a_1,\ldots,a_m]
=\sum_{\substack{1\le i\le m\\a_i\ge2}}
(-1)^{n-i}[a_1,\ldots,a_i-1,\ldots,a_m].
\]

This is a genuine integral cellular differential, not a rational-rank inference. To see it is surjective, select among its columns those indexed by \(a=b+e_m\) as \(b\) runs through all positive compositions of \(n-1\) into \(m\) parts. In the column \(a=b+e_m\), the \(i=m\) face has coefficient \(1\) and target \(b\). Every other face, if present, has a strictly larger *last part* than \(b\). Ordering compositions by increasing last part therefore makes this selected square submatrix triangular with diagonal entries \(1\). It is unimodular. Consequently \(\partial_D\) is split-surjective over \(\mathbb Z\), and

\[
\widetilde H_j(D_*)\cong
\begin{cases}
\mathbb Z^{\binom{n-2}{m-2}},&j=d,\\
0,&j\ne d.
\end{cases}
\]

Since the chain sequence \(0\to D_*\to C_*(Y;\mathbb Z)\xrightarrow{p_\#}C_*(B;\mathbb Z)\to0\) is exact and \(B\) is contractible, the long exact sequence gives the same *reduced* integral homology for \(Y\) when \(d\ge1\). In particular it shows that \(Y\) is connected and all its integral homology is torsion-free.

**4. Recovering homotopy, not just homology.** For \(d=1\) the quotient has a connected finite one-dimensional CW structure, hence is a wedge of its first Betti number \(m-1\) circles. For \(d\ge2\), the established complete-graph Hom-complex theorem of Babson and Kozlov gives \(X_{m,n}\simeq\bigvee S^d\); in particular \(X_{m,n}\) is simply connected. Armstrong's orbit-space fundamental-group theorem identifies \(\pi_1(Y)\) with \(A_n\) modulo the normal subgroup generated by elements having fixed points. Every 3-cycle in \(A_n\) has a fixed point in \(X_{m,n}\): put equal positive weights on its three target colors in one row, and use \(m-1\) distinct other colors for the remaining rows. The required inequality \(n\ge m+2\) is precisely \(d\ge2\). Because the 3-cycles generate \(A_n\), the quotient \(Y\) is simply connected. Hurewicz then realizes a basis of the sole nonzero reduced integral homology group by maps of \(d\)-spheres; the resulting map \(\bigvee^{\binom{n-2}{m-2}}S^d\to Y\) is an integral homology equivalence between simply connected CW spaces, and is a homotopy equivalence by the homological Whitehead theorem. For \(d=0\) the complex \(X_{m,m}\) consists of the \(m!\) bijective colorings; even permutations have precisely two orbits, yielding \(S^0\). This exhausts the stated parameter range.

## Verification

The standalone standard-library program `verify.py` constructs the explicit quotient CW cell types as products of simplices and assigns each its single or double parity sheet using the odd-stabilizer criterion, then constructs its integer cellular boundary with the correct parity transition. It checks all consecutive boundary compositions exactly, computes homology ranks in characteristics two, three and five, and checks the integer triangular unimodular differential for every pair \(2\le m\le5\), \(m+1\le n\le\min(m+4,8)\), covering fifteen cases. The output is `verification_output.txt`. To reproduce: `python3 verify.py`. These finite checks independently test the essential incidence and parity formulas; the unrestricted theorem follows from the proof above, not by extrapolation from finite computations.

## Relationship to prior work

Babson and Kozlov's 1997 ordered-disjoint-block construction and their 2003 Hom-complex work establish the underlying face poset and the *unquotiented* wedge-of-spheres homotopy classification. Their relevant earlier block-permutation quotient is not the color-label alternating quotient here. The previously published complete two-sided character calculation for \(\operatorname{Hom}(K_m,K_n)\) identifies precisely \(\binom{n-2}{m-2}\) top-dimensional **rational** alternating-color invariants, while explicitly leaving open integral torsion and quotient homotopy type; this is the strongest direct overlap. The present proof adds the two-sheeted integral quotient-cell model, a unimodular difference differential, fundamental-group vanishing and the resulting integral homotopy type, none of which follows from rational Betti ranks alone. Other published color-permutation character results likewise constrain only rational invariants. This distinction is a comparison of mathematical implications, not a claim that differing titles imply novelty.

## Limitations

The conclusion concerns ordinary geometric quotients of complete-graph Hom complexes for the stated integer parameters; it does not classify their integral equivariant homology lattices, isotropy representations, Borel constructions, or quotient homeomorphism types. The established Hom-complex sphere-wedge theorem and Armstrong's fundamental-group theorem are inputs, not new proofs of those classical results. The 1997 ordered-disjoint-block primary preprint was available at abstract level but its complete original text could not be retrieved through the attempted lawful routes; similarly the geometric comparison of Pfeifle was checked at abstract level only. An unindexed equivalent result in these or other sources remains a publication-priority risk; independent mathematical validation has not been performed. Finite verification covers only the specified cases, not all integers.

## References

1. E. Babson and D. Kozlov, *Diagrams of classifying spaces and k-fold Boolean algebras*, initial public preprint 1997-04-29, arXiv:math/9704227, https://arxiv.org/abs/math/9704227. See the ordered nonempty disjoint-subset construction and Theorem 6.2 in the accessible descriptions.
2. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, preprint first public 2003-10-05, arXiv:math/0310056, https://arxiv.org/html/math/0310056v4, especially Definition 1.2, Propositions 4.5–4.6.
3. M. A. Armstrong, *On the fundamental group of an orbit space*, Proceedings of the Cambridge Philosophical Society 61 (1965), 639–646, https://doi.org/10.1017/S0305004100038974.
4. J. Pfeifle, *Dissections, Hom-complexes and the Cayley trick*, initial public preprint 2005-12-22, arXiv:math/0512529, https://arxiv.org/abs/math/0512529.
5. *Full two-sided symmetry character of complete-graph Hom complexes*, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-full-two-sided-symmetry-character-of-complete-graph-hom-complexe--ce942485ca98/RESULT.md (rational alternating-color ranks; comparison source).
6. *Color-permutation characters of complete-graph Hom complexes*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-color-permutation-characters-of-complete-graph-hom-complexes--50c1a3944425 (character comparison source).
