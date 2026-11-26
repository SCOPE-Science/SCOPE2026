# The integral Steiner-trihedral reconstruction lattice of cubic-surface tritangents

## Finding

Let \(S\) be a smooth cubic surface over an algebraically closed field of characteristic zero. Write \(\mathcal T\) for its 45 geometric tritangent planes and \(\mathcal P\) for its 120 unordered Steiner trihedral pairs. A pair consists of six tritangent planes, arranged as two conjugate triples. Define the unsigned incidence homomorphism
\[
\Phi:\mathbb Z^{\mathcal P}\longrightarrow\mathbb Z^{\mathcal T},\qquad [P]\longmapsto\sum_{T\in P}[T].
\]
Then its complete integral Smith normal form is
\[
\operatorname{SNF}(\Phi)=\operatorname{diag}(1^{24},2^{20},12),
\qquad
\operatorname{coker}(\Phi)\cong(\mathbb Z/2\mathbb Z)^{20}\oplus\mathbb Z/12\mathbb Z.
\]
In particular \(\Phi\) has rational rank 45, its image has index \(12{,}582{,}912=3\cdot2^{22}\), and **each** individual formal tritangent basis vector has exact order 12 in the quotient. Thus 12 is the smallest positive integer \(m\) such that, for every tritangent \(T\), \(m[T]\) is an integral combination of the 120 unsigned six-plane sums. In the coordinates of the certificate, membership requires 20 parity conditions and divisibility of one further coordinate by 12. That last condition requires divisibility by both four and three; reducing it to parity and divisibility by three would omit the mod-four obstruction.

## Assumptions and scope

Fix a blowdown of six mutually skew exceptional lines to six points in general position of \(\mathbb P^2\), indexed by \(0,\ldots,5\). Label all 27 lines by \(E_i\), \(Q_i\), and \(L_{ij}\), with \(0\le i<j\le5\). Their divisor classes are \(E_i\), \(Q_i=2H-\sum_{k\ne i}E_k\), and \(L_{ij}=H-E_i-E_j\). The 45 tritangent planes, represented by their three component lines, are precisely
\[
\{E_i,L_{ij},Q_j\}\ (i\ne j),\quad
\{L_{ij},L_{kl},L_{mn}\}\ (\{\{i,j\},\{k,l\},\{m,n\}\}\text{ a partition into pairs}).
\]
The \(30\) first-type and \(15\) second-type triples have distinct line supports.

A Steiner trihedron is a triple of tritangent planes with pairwise disjoint component-line supports, possessing three conjugate planes, each meeting all three original planes along one of the surface's 27 lines. The three conjugates constitute the second Steiner trihedron; the unordered union is a **pair**. Thus each pair determines an unordered six-element subset of \(\mathcal T\). The calculation concerns free abelian groups on these geometric **plane labels**, not divisor classes or the Picard group; no orientations, multiplicities or signs are inserted into the incidence map. The result is invariant under relabelling of the six blowup points.

## Proof

**1. The finite geometric model is complete.** The standard cubic-surface line classification gives exactly the two displayed types of tritangent planes. From a triple \(a\) of planes with disjoint line supports, construct each triple \(b\) of planes such that its members are pairwise line-disjoint and each member shares exactly one surface line with each plane of \(a\). For a Steiner trihedron these are exactly its conjugate planes, by the geometric definition. The enumeration in `verify.py` checks every three-subset of the 45 planes and every compatible conjugate triple, without quotienting by an assumed group order. It finds precisely 120 distinct unordered six-plane supports; each contains exactly nine distinct surface lines, with every such line appearing in two of its six planes. This agrees with the classical enumeration of the 120 Steiner trihedral pairs, and rules out extra or missing columns.

**2. The exact integral certificate.** Sort the 45 three-line tritangents lexicographically using the explicit labels, and the 120 six-element plane-index supports lexicographically. Form the integer \(45\times120\) zero-one matrix \(M\) with \(M_{T,P}=1\) precisely when \(T\in P\). In `smith_ops.json` are 2,710 explicitly ordered elementary integer row and column operations. `verify.py` reconstructs \(M\) from the preceding geometric definitions, replays *every* operation using only exact integers, and checks that the resulting matrix has diagonal entries
\[
\underbrace{1,\ldots,1}_{24},\quad
\underbrace{2,\ldots,2}_{20},\quad12,
\]
with every remaining entry zero. The permitted operations are row swaps, column swaps, multiplication of a row by \(-1\), and adding an integer multiple of one row or column to another. Each is unimodular. Hence they preserve the isomorphism class of the integer cokernel; the displayed diagonal also satisfies the Smith divisibility ordering. This is a finite **proof certificate**, not a numerical approximation or an appeal to an unverified software Smith routine.

**3. Exact order of each generator.** While replaying row operations, the verifier also applies those same operations to the \(45\times45\) identity matrix, obtaining a unimodular row transformation \(U\). Column operations preserve the column lattice. Thus the image of the original tritangent basis element \(e_T\) in the diagonal cokernel has coordinates \(Ue_T\). In a diagonal cokernel with diagonal \(d_j\), the additive order of this element is
\[
\operatorname{lcm}_{j=1}^{45}\frac{d_j}{\gcd(d_j,(Ue_T)_j)}.
\]
The verifier evaluates this exact expression for all 45 columns of \(U\) and obtains 12 each time. Together with the Smith form this proves the optimality of the universal multiplier 12, and yields a constructive lattice-membership test: a vector \(x\in\mathbb Z^{45}\) belongs to \(\operatorname{im}\Phi\) exactly when every coordinate \((Ux)_j\) is divisible by the corresponding \(d_j\). In particular, \(6[T]\) satisfies every homogeneous linear congruence modulo two or three, but is not in the image. Such congruences alone cannot characterize the lattice.

**4. Independent internal consistency checks.** Every tritangent occurs in exactly 16 pairs, and every pair contains six planes. Distinct planes occur together in four pairs when they share a surface line, and in one pair otherwise; the two counts have frequencies 270 and 720, respectively. Consequently the Gram matrix is \(MM^{\mathsf T}=15I+J+3A\), where \(A\) is the adjacency matrix for sharing a surface line. Its eigenvalues are 12, 3, and \(-3\), with multiplicities 1, 20, and 24; hence the Gram eigenvalues are 96, 24, and 6. This separately verifies full rational rank and consistency of the incidence construction. The Smith proof itself rests on the stronger exact unimodular certificate.

## Verification

Place `verify.py` and `smith_ops.json` in the same directory and execute `python3 verify.py` with a standard Python 3 installation; no third-party package or external data is required. The script builds all 27 lines, 45 tritangent triples, and 120 unordered pairs; checks the classical valencies and Gram intersection counts; replays the entire integer-operation certificate; checks the full rectangular diagonal matrix entry by entry; and determines the order of every formal tritangent class from the resulting unimodular row transformation. Its successful final line states the Smith factors and the index. The data and the code are included in the same delivered package.

## Relationship to prior work

The 27 lines, 45 tritangent planes, 240 Steiner trihedra and 120 pairs are classical. Elsenhans--Jahnel (2010, §§2.1--2.8) describe their geometry and Galois descent. Betten--Hirschfeld--Karaoglu (2017, §§2,4) enumerate the three 120-pair types and use these pairs to construct cubic surfaces; their claim is about surfaces and incidence combinatorics, not an integer cokernel. Das (2020) studies arithmetic statistics of marked cubic surfaces and associated Weyl representations, but not this unsigned integral presentation.

The published calculation *The 540 indispensable quartic trades of the cubic-surface tritangent configuration* determines **signed** three-tritangent exchanges in a 45-variable toric kernel. Its 120 cubic relations are differences of the two Steiner trihedra, whereas the present columns are **unsigned sums of all six tritangent planes** in a pair. Counting signed exchanges does not determine the image or Smith form of this different \(45\times120\) unsigned map. Likewise *Integral tritangent presentation of the \(E_6\) weight lattice* computes the \(27\times45\) plane-to-line incidence map, and the published double-six lattice computes a \(27\times36\) map on lines. Neither statement implies the asserted \(45\times120\) cokernel. The novelty claim is limited to this full unsigned integral presentation and the sharp reconstruction multiplier, not the existence or enumeration of Steiner pairs.

The related nine-line-support calculation [7] uses the same 120 pairs. If \(C\) is the plane-to-line incidence matrix and \(N\) the nine-line-support matrix, then \(CM=2N\) because each of the nine lines appears in two of the six planes. The rank-21 line image does not determine the integral plane image or the per-plane obstruction.

## Limitations

This is an integral calculation for **formal tritangent labels** in the universal classical incidence configuration; it is not a computation of torsion in \(\operatorname{Pic}(S)\), the Chow groups or a descent obstruction on a particular surface. A finite search cannot exclude an equivalent older calculation in incidence-design or integer-lattice literature. No claim is made about characteristic-dependent automorphism phenomena or singular cubic surfaces. The result does not classify other modules associated with the \(W(E_6)\)-configuration.

## References

1. A. Betten, J. W. P. Hirschfeld and F. Karaoglu, *Classification of cubic surfaces with twenty-seven lines over the finite field of order thirteen*, European Journal of Mathematics (published online 2017-09-27), https://doi.org/10.1007/s40879-017-0182-0, especially §§2,4.
2. A.-S. Elsenhans and J. Jahnel, *Cubic surfaces with a Galois invariant pair of Steiner trihedra*, arXiv:1006.1474 (2010-06-08), https://arxiv.org/abs/1006.1474, especially §2.
3. R. Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183 (2020-02-25), https://arxiv.org/abs/2002.11183.
4. *The 540 indispensable quartic trades of the cubic-surface tritangent configuration*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-the-540-indispensable-quartic-trades-of-the-cubic-surface-tritan--511e3e06b7dc.
5. *Integral tritangent presentation of the \(E_6\) weight lattice*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-integral-tritangent-presentation-of-the-e-6-weight-lattice--d458bb2de263.
6. *The order-four integral reconstruction obstruction for Schläfli double-sixes*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-the-order-four-integral-reconstruction-obstruction-for-schl-fli--0aac314408f8.
7. *The index-three Steiner trihedral support lattice on a smooth cubic surface*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-the-index-three-steiner-trihedral-support-lattice-on-a-smooth-cu--8a178617dee9.
