# Multiplicity-free rational homology of triple Kneser neighborhood complexes

## Finding

For every integer \(n\ge7\), let \(G_n=\mathrm{KG}(n,3)\) be the graph on the three-element subsets of \([n]=\{1,\dots,n\}\), with two vertices adjacent precisely when disjoint. Let \(X_n=\mathcal N(G_n)\) be its ordinary **open** Lovász neighborhood complex: a nonempty family of graph vertices is a simplex exactly when those vertices possess a common neighbor. Relabeling \([n]\) defines a canonical action of \(\mathfrak S_n\) on \(X_n\).

Its reduced rational homology vanishes outside degree \(n-6\), and the **full** rational homology representation is the following multiplicity-free sum of Specht modules:

\[
\widetilde H_{n-6}(X_n;\mathbb Q)\cong
S^{(5,1^{n-5})}\oplus S^{(4,2,1^{n-6})}\oplus S^{(3,3,1^{n-6})}.
\]

Here \(S^\lambda\) is the irreducible rational Specht module indexed by the indicated partition of \(n\); all three partitions are valid and different for every \(n\ge7\). In particular, the representation has no invariant vector under either \(\mathfrak S_n\) or its alternating subgroup.

For \(\sigma\in\mathfrak S_n\), let \(a\) be its number of fixed letters and \(b\) its number of two-cycles. Its homology character is **exactly**

\[
\operatorname{tr}\bigl(\sigma\mid\widetilde H_{n-6}(X_n;\mathbb Q)\bigr)
=\frac{\operatorname{sgn}(\sigma)}4
\bigl(a^4-10a^3-4a^2b+31a^2+12ab-30a+4b^2-12b+4\bigr).
\]

At the identity the dimension is \(\frac{n(n-5)(n-3)(n-2)}4+1\), agreeing with the previously known number of wedge summands. Thus the new statement concerns the **action** on homology rather than its already known rank or homotopy concentration.

## Assumptions and scope

Everything is finite and simplicial. The neighborhood condition means that for a family \(F\) of three-subsets there exists a three-subset disjoint from every member of \(F\). Equivalently, with \(\operatorname{supp}(F)=\bigcup_{e\in F}e\),

\[
F\in X_n\quad\Longleftrightarrow\quad |\operatorname{supp}(F)|\le n-3.
\]

This criterion includes the empty face. The coefficients in the claimed representation are \(\mathbb Q\), not a modular coefficient field. The argument uses the established theorem that \(\mathcal N(\mathrm{KG}(n,3))\) has the homotopy type of a wedge of spheres in degree \(n-6\) for \(n\ge7\); the multiplicity was computed in prior work. No equivariant homotopy equivalence to a wedge is assumed or claimed.

## Proof

**1. The fixed-face Lefschetz sum.** Fix \(\sigma\in\mathfrak S_n\) with \(c\) cycles on \([n]\). A \(\sigma\)-invariant simplex is a union of orbits of the induced permutation of the three-subsets. If such a simplex \(F\) contains \(r\) three-subsets in \(o(F)\) orbits, its contribution to the alternating simplicial-chain trace is

\[
(-1)^{r-1}\operatorname{sgn}(\sigma|_F)=(-1)^{o(F)-1}.
\]

The empty face contributes \(-1\) in the reduced trace. Define \(w(F)=(-1)^{o(F)}\) for invariant \(F\), including \(w(\varnothing)=1\). Then the reduced Lefschetz number is

\[
\widetilde L(\sigma)=-\sum_{\substack{F\subseteq\binom{[n]}3\\ \sigma F=F,\ |\operatorname{supp}(F)|\le n-3}}w(F).
\]

**2. Möbius inversion on permutation cycles.** A \(\sigma\)-stable subset \(U\subseteq[n]\) is a union of cycles. Put \(\Phi(U)=\sum_{\sigma F=F,\operatorname{supp}(F)=U}w(F)\). For any stable \(T\), the sum over all invariant triple-families supported in \(T\) is \(\prod_{\mathcal O\subseteq\binom T3}(1-1)\), the product being over orbits of triples. Consequently,

\[
\sum_{U\subseteq T\text{ stable}}\Phi(U)=
\begin{cases}1,&|T|\le2,\\0,&|T|\ge3.\end{cases}
\]

Let \(c(U)\), \(a(U)\), and \(b(U)\) denote the numbers of cycles, one-cycles, and two-cycles contained in the stable set \(U\). Boolean Möbius inversion over cycles gives the **exact** formula

\[
\Phi(U)=(-1)^{c(U)}P(a(U),b(U)),\qquad
P(a,b)=1-a+\binom a2-b.
\]

Indeed the only stable subsets of \(U\) of size at most two are the empty set, one fixed letter, two distinct fixed letters, and one two-cycle, yielding these four terms with the indicated signs.

The unrestricted sum of \(\Phi(U)\) is zero since \(n\ge3\). Thus the allowed supports \(\lvert U\rvert\le n-3\) can be counted as minus the supports whose complements have size \(0\), \(1\), or \(2\). Write \(a=a([n])\), \(b=b([n])\). Such complements are exactly the empty set, one fixed letter, two fixed letters, or one two-cycle. Their total is

\[
(-1)^c E(a,b),\quad
E(a,b)=P(a,b)-aP(a-1,b)+\binom a2P(a-2,b)-bP(a,b-1).
\]

For \(a<2\) terms with zero binomial coefficient are omitted, so no values at negative cycle counts are needed. Expanding gives

\[
E(a,b)=\frac{a^4-10a^3-4a^2b+31a^2+12ab-30a+4b^2-12b+4}{4}.
\]

It follows that \(\widetilde L(\sigma)=(-1)^cE(a,b)\). By homology concentration in degree \(n-6\), the Lefschetz number equals \((-1)^{n-6}\) times the homology trace. Because \((-1)^{n+c-6}=\operatorname{sgn}(\sigma)\), the stated character formula follows for **every** \(n\ge7\) and **every** permutation \(\sigma\), with no finite-parameter extrapolation.

**3. Irreducible decomposition.** Let \(h_j=s_{(j)}\) and let \(s_\lambda\) be Schur functions. The horizontal-strip Pieri rule, equivalently the interlacing condition \(\lambda_i\ge\mu_i\ge\lambda_{i+1}\), gives for all \(n\ge7\):

\[
\begin{aligned}
&s_{(n-4,1^4)}+s_{(n-4,2,1,1)}+s_{(n-4,2,2)}\\
&=h_n-2h_{n-1}s_{(1)}+h_{n-2}\bigl(s_{(2)}+3s_{(1,1)}\bigr)\\
&\quad-2h_{n-3}\bigl(s_{(2,1)}+s_{(1,1,1)}\bigr)
+h_{n-4}\bigl(s_{(2,2)}+s_{(2,1,1)}+s_{(1^4)}\bigr).
\end{aligned}
\]

For verification of the cancellation, each product \(h_{n-r}s_\mu\) expands with coefficient one into all partitions \(\lambda\) containing \(\mu\) as a horizontal strip of length \(n-r\). Substituting the displayed nine coefficients leaves exactly the three partitions on the left, including at \(n=7\).

Under the Frobenius characteristic map, \(h_{n-r}s_\mu\) is the character of \(\operatorname{Ind}_{\mathfrak S_{n-r}\times\mathfrak S_r}^{\mathfrak S_n}(\mathbf1\boxtimes S^\mu)\). On a permutation with \(m_j\) cycles of length \(j\), its value equals

\[
\sum_{\nu\vdash r}\chi^\mu(\nu)\prod_{j=1}^{r}\binom{m_j}{m_j(\nu)},
\]

because an invariant \(r\)-subset must be a union of cycles and carries the restricted cycle type \(\nu\). Substitution of the ordinary character tables of \(\mathfrak S_r\), \(r\le4\), into the nine-term Pieri identity cancels the three- and four-cycle terms and yields precisely \(E(a,b)\). Hence \(E\) is the sum of the three irreducible characters corresponding to the three partitions on the left. Tensoring with the sign representation conjugates their diagrams and yields the three Specht partitions stated in the Finding.

For \(n\ge7\), none of these three partitions is \((n)\) or \((1^n)\). The restriction to the alternating subgroup therefore has no fixed vector: a fixed vector would give a trivial or sign constituent after inducing to \(\mathfrak S_n\), contradicting the decomposition. This finishes the proof.

## Verification

The included `verify.py` uses only the Python 3 standard library. It independently generates the neighborhood complex from the maximal support sets for \(n=7,8\); enumerates **all** faces; and compares direct oriented simplicial fixed-face Lefschetz traces with the claimed character on every conjugacy class (15 classes at \(n=7\), 22 at \(n=8\)). The independently implemented Murnaghan–Nakayama rule verifies the character decomposition on every conjugacy class for \(7\le n\le11\), and the horizontal-strip interlacing identity is checked for the same parameters. The exact output includes `DIRECT_LEFSCHETZ_OK` for both finite sizes and `VERIFY_OK`.

The direct face counts, including the empty face, are \(421\) for \(n=7\) and \(54{,}475\) for \(n=8\). These are corroborations of the universal proof, **not** its justification for unbounded \(n\). The input theorem on homology concentration is used as published and is not re-proved by the finite verifier.

## Relationship to prior work

Lovász introduced neighborhood complexes in the proof of the Kneser conjecture. Björner and de Longueville established sphere homotopy types for **stable** Kneser graphs (2003). Kozlov's *Combinatorial Algebraic Topology* (2007/2008), Proposition 17.28 as cited in Nilakantan–Singh, gives wedge-of-spheres concentration for **ordinary** Kneser neighborhood complexes. Nilakantan and Singh (arXiv:1807.11732, first posted 31 July 2018), Theorem 1.3 and its proof, establish the exact wedge multiplicity for the triple-set family. These existing homotopy and dimension results are **not** claimed to be new.

The calculation here is finer: a closed formula for the trace of every coordinate permutation and a multiplicity-free decomposition into three rational irreducibles. Published work on **stable** Kneser equivariant topology studies the dihedral action on a different graph and does not imply the present natural full-symmetric-group module of the **ordinary** triple-subset complex. An earlier result on the two-subset Kneser family similarly has a different vertex set and does not imply the displayed three-subset representation.

## Limitations

The result concerns rational homology representations, not integral representation lattices, modular representations, equivariant homotopy types, or canonical integral bases. The proof relies on published homology concentration; the accompanying finite checker is not a proof of that input theorem. The complete text of Kozlov's book and some specialized equivariant literature was not available in this review; an equivalent unindexed character computation cannot be excluded. The claim begins at \(n=7\); the degenerate \(n=6\) case is not part of the theorem.

## References

1. D. N. Kozlov, *Combinatorial Algebraic Topology*, Springer, Algorithms and Computation in Mathematics 21, 2007/2008, DOI: 10.1007/978-3-540-71962-5. Publisher records first hardcover publication 24 October 2007.
2. N. Nilakantan and A. Singh, *Neighborhood Complexes of Kneser Graphs, \(KG_{3,k}\)*, arXiv:1807.11732v1 (31 July 2018), especially Theorem 1.3, Section 4 and its references.
3. A. Björner and M. de Longueville, *Neighborhood Complexes of Stable Kneser Graphs*, Combinatorica 23 (2003), 23–34, DOI: 10.1007/s00493-003-0012-5. Only year-level original publication dating was recovered.
4. C. Schultz, *The equivariant topology of stable Kneser graphs*, FPSAC 2011, DOI: 10.46298/dmtcs.2960. This concerns the stable, dihedrally symmetric construction.
