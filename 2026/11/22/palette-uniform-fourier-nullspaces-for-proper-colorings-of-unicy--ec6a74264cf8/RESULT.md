# Palette-uniform Fourier nullspaces for proper colorings of unicyclic graphs

## Finding

Let \(G=(V,E)\) be any finite connected simple unicyclic graph, with \(N=|V|=|E|\), unique cycle of length \(c\ge3\), and \(b=N-c\) bridge edges. Let \(H\) be any finite abelian group of order \(q\ge3\). The proper-coloring indicator \(f:H^V\to\{0,1\}\) is \(1\) when adjacent vertices have unequal group labels and \(0\) otherwise. Define unnormalized convolution \(T_f g=f*g\) on \(\mathbb C^{H^V}\).

**Complete multiplier formula.** For a frequency \(\xi\in\widehat H^V\), put \(\prod_{v\in V}\xi_v\) for its total character. If this character is nontrivial, then \(\widehat f(\xi)=0\). Otherwise orient the cycle coherently, orient the bridges arbitrarily, and choose edge characters \(s_e\in\widehat H\) with
\[
\prod_{v\in V}\xi_v(x_v)=\prod_{e=(u,v)\in E}s_e(x_v-x_u)
\qquad\text{for every }x\in H^V.
\]
Such characters exist, and their only ambiguity is multiplication by one common character around the directed cycle. Define \(B(s)=q-1\) when \(s\) is the trivial character and \(B(s)=-1\) otherwise. For each \(\eta\in\widehat H\), let \(m_\eta=|\{e\in C:s_e=\eta\}|\). Then
\[
\boxed{\widehat f(\xi)=\left(\prod_{e\in E\setminus C}B(s_e)\right)(-1)^c
\sum_{\eta\in\widehat H}(1-q)^{m_\eta}.}
\]
This signed integer formula specifies every complex Fourier multiplier and therefore every singular value by taking absolute values. The expression is independent of the allowed choice of edge characters.

**Exact extra-zero and rank classification.** The balanced frequencies (those with total trivial character) have an additional zero **if and only if** the cycle-character multiplicities, in some order, are
\[
\boxed{(m+1,m,\ldots,m),\quad c=qm+1,\quad m\ge1.}
\]
Thus additional Fourier zeros occur if and only if \(c\equiv1\pmod q\). With \(m=(c-1)/q\) in the resonant case, set
\[
Z_{q,c}=\begin{cases}
\displaystyle\frac{c!}{(m+1)!(m!)^{q-1}},& c=qm+1\text{ for some }m\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
Then the **exact convolution rank** and **nullity** on the full \(q^N\)-dimensional signal space are
\[
\boxed{\operatorname{rank}T_f=q^{N-1}-q^{N-c}Z_{q,c},\qquad
\operatorname{nullity}T_f=q^N-q^{N-1}+q^{N-c}Z_{q,c}.}
\]
For fixed \(q\) and resonant cycle lengths \(c\to\infty\), the fraction of balanced Fourier modes additionally lost is
\[
\boxed{\frac{Z_{q,c}}{q^{c-1}}\sim
\frac{q^{1+q/2}}{(2\pi c)^{(q-1)/2}}.}
\]
In particular the rank depends on the graph only through the palette order, the number of vertices and the unique cycle length; it is independent of where the trees are attached and of the isomorphism type of \(H\).

## Assumptions and scope

All graphs are connected, simple and have one cycle; the cycle is necessarily of length at least three. The palette group may be noncyclic. The indicator counts every proper vertex coloring exactly once, without quotienting by translation or permuting colors. Fourier transforms and convolutions are **unnormalized**; the Fourier multiplier at \(\xi\) is \(\sum_{x\in H^V}f(x)\prod_v\xi_v(x_v)\), with consistent character signs. Replacing every character by its complex conjugate does not change the rank or singular values. The theorem excludes \(q=2\), where the proper-coloring set is empty for odd cycles and consists of only two colorings for an even unicyclic graph.

## Proof

**1. Dual edge representation.** Write the coboundary map \(d:H^V\to H^E\) as \((dx)_e=x_v-x_u\) for an oriented edge \(e=(u,v)\). Its kernel is the constant diagonal \(H\), since \(G\) is connected, and its image consists precisely of edge assignments whose oriented sum around the unique cycle is zero. To see the latter assertion, remove one cycle edge; arbitrary values on the remaining spanning tree integrate uniquely after fixing the root value, and the omitted cycle difference is then forced.

A vertex character is trivial on the constant diagonal exactly when its total character is trivial. In this case it is the pullback along \(d\) of an edge character \(s\). Any two such choices differ by a character in the one-dimensional cycle flow, i.e. by a simultaneous cycle shift. For an unbalanced vertex character, translation of all vertex colors leaves the coloring indicator invariant but multiplies the character by a nontrivial scalar; summation forces its Fourier multiplier to vanish.

**2. Character filter.** For a group character \(s\in\widehat H\), orthogonality gives
\[
\sum_{h\in H\setminus\{0\}}s(h)=B(s)=\begin{cases}q-1,&s=1,\\-1,&s\ne1.\end{cases}
\]
For a balanced vertex frequency, sum first over the \(q\) root values, and then over nonzero edge differences satisfying the one cycle relation. Introduce the character filter for the latter relation:
\[
\mathbf 1_{\{d_1+\cdots+d_c=0\}}=\frac1q\sum_{t\in\widehat H}t(d_1+\cdots+d_c).
\]
The \(q\) root choices cancel the denominator. Independent summation of every bridge and cycle edge yields
\[
\widehat f(\xi)=\prod_{e\notin C}B(s_e)\sum_{t\in\widehat H}\prod_{e\in C}B(s_et).
\]
If \(m_\eta\) counts the cycle edges with a specified \(s_e\), the cycle product associated with \(t\) is \((-1)^{c-m_{t^{-1}}}(q-1)^{m_{t^{-1}}}\). Summing over the group proves the displayed integer multiplier formula. A cycle shift permutes the indices \(\eta\), proving choice independence.

**3. Classification of zeros by a smallest-exponent argument.** All bridge factors \(B(s_e)\) are nonzero. It remains to solve \(\sum_{j=1}^q(1-q)^{m_j}=0\) for nonnegative integers \(m_j\) summing to \(c\). Write \(r=q-1\ge2\), let \(m\) be the smallest exponent and let \(t\) be the number of occurrences of \(m\). Divide by \((-r)^m\) and reduce modulo \(r\): \(t\equiv0\pmod r\). Because \(1\le t\le r+1<2r\), necessarily \(t=r\). The remaining exponent \(M>m\) then satisfies \(r+(-r)^{M-m}=0\), which forces \(M=m+1\). Conversely that pattern plainly gives zero. Since \(c=qm+1\), and \(c\ge3\), one has \(m\ge1\). This is an if-and-only-if classification for every finite abelian palette of order at least three.

**4. Exact multiplicity.** Balanced vertex characters correspond bijectively to edge-character assignments modulo the free action of the \(q\)-element cycle-flow character group. There are \(q^{N-1}\) balanced frequencies. Bridge choices contribute \(q^b\). In a resonant cycle, the number of labelled cycle-character words having the zero-forcing multiplicity pattern is
\[
q\frac{c!}{(m+1)!(m!)^{q-1}}.
\]
The leading factor \(q\) chooses the character appearing \(m+1\) times. The free cycle-shift action divides the count by \(q\). Hence exactly \(q^{N-c}Z_{q,c}\) balanced vertex frequencies have zero multiplier, proving the rank and nullity.

**5. Asymptotic.** For fixed \(q\), apply Stirling's formula to \(Z_{q,c}=c!/((m+1)!(m!)^{q-1})\) with \(c=qm+1\). Its ratio to \(q^c\) is asymptotic to \(q^{q/2}/(2\pi c)^{(q-1)/2}\). Multiplication by \(q\) gives the stated fraction among balanced modes. This is along the resonant subsequence only, not an assertion for all cycle lengths.

## Verification

The included self-contained `check.py` independently enumerates all proper colorings and evaluates additive character sums exactly: for cyclic palettes of orders three, four and five it uses integer root-of-unity residue counts, and for the noncyclic Klein-four palette it uses integer sign characters. Its eleven exhaustive instances compare **5,209** character coefficients to a separately computed edge formula. They include the resonant cycles of lengths four with three colors and five with four colors, nonresonant cycles, and graphs with different pendant-tree attachments. Four additional selected frequency comparisons include a zero multiplier for the resonant five-color six-cycle. Run `python3 check.py` (Python 3.10 or later, standard library only). These finite checks corroborate the independent all-parameter proof; they cannot establish its infinite quantifiers.

## Relationship to prior work

Goodall's finite Fourier treatment of graph tensions and flows establishes the general duality and chromatic-weight-enumerator machinery used here. It does not explicitly give the palette-uniform **all-frequency unicyclic zero classification**, the additional-nullity formula, or its palette-dependent asymptotic. Previous work on ternary proper colorings of a single cycle supplies the \(q=3\), no-bridge case; that case is included here rather than claimed as new. Published first-coordinate Fourier sampling analyses of arbitrary-color cycles and pendant decorations concern degree-one Gram matrices, not the complete convolution multiplier array. The new contribution is the exact arithmetic cancellation classification across *all* finite abelian palettes and *all* unicyclic graph shapes.

## Limitations

The theorem concerns unweighted proper colorings on connected graphs with exactly one cycle, not graphs with several independent cycles, list-coloring constraints, nonuniform Potts weights, or the exact distribution of all nonzero singular-value multiplicities after aggregation. The multiplier formula nonetheless determines each individual singular value. The historical-priority comparison was bounded: an earlier specialized complete-weight-enumerator or transfer-matrix result may state an equivalent modulo-palette resonance under different terminology. No independent mathematical audit has been performed.

## References

1. A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1, first publicly submitted 2008-06-30, https://arxiv.org/html/0806.4848v1. Especially Section 4.4 on chromatic tensions and MacWilliams duality.
2. D. Garijo, A. Goodall and J. Nešetřil, *On the number of B-flows of a graph*, European Journal of Combinatorics 35 (2014), 273–285, DOI:10.1016/j.ejc.2013.06.009. This concerns flow-counting contractors, not a full signed vertex-coloring Fourier spectrum.
