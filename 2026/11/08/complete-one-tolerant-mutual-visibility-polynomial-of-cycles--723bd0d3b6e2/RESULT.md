# Complete one-tolerant mutual-visibility polynomial of cycles

## Finding

For an integer \(n\ge 3\), label the vertices of the cycle \(C_n\) by \(\mathbb Z/n\mathbb Z\). A set \(S\) is *one-tolerant mutually visible* when each two selected vertices have a shortest connecting path with at most one further selected vertex in its interior. Define
\[
\mathcal V_1(C_n;z)=\sum_{S\subseteq V(C_n):\,S\text{ is one-tolerant mutually visible}}z^{|S|}.
\]

**Theorem.** For \(n=3,4\), the polynomial is \((1+z)^n\). For all \(n\ge5\) it has degree exactly five and is
\[
\mathcal V_1(C_n;z)=\sum_{j=0}^{3}\binom nj z^j+A_4(n)z^4+A_5(n)z^5.
\]
For \(n=2m\), \(m\ge3\), the two new coefficients are
\[
A_4(2m)=\frac{m(m-1)(2m^2+2m-9)}6,\qquad
A_5(2m)=\frac{m(m-2)(m-1)(m+1)(m+12)}{60}.
\]
For \(n=2m+1\), \(m\ge2\), they are
\[
A_4(2m+1)=\frac{m(m-1)(m+1)(2m+1)}6,\qquad
A_5(2m+1)=\frac{m(m-1)(m+1)(m+2)(2m+1)}{120}.
\]
Thus the complete number of maximum one-tolerant mutual-visibility sets is \(A_5(n)\). The asymptotic proportion of five-vertex sets with this property is exactly
\[
\lim_{n\to\infty}\frac{A_5(n)}{\binom n5}=\frac1{16}.
\]

**Geometric characterization.** List the selected vertices cyclically and let the positive integers \(g_1,\ldots,g_s\) be consecutive clockwise gap lengths, summing to \(n\); indices are cyclic. For \(s=4\), feasibility is equivalent to \(g_i\le\lfloor n/2\rfloor\) for every \(i\). For \(s=5\), feasibility is equivalent to \(g_i+g_{i+1}\le\lfloor n/2\rfloor\) for every \(i\). Every set of at most three vertices is feasible, and no set of six or more vertices is feasible.

## Assumptions and scope

The graph is the unweighted, finite, simple undirected cycle \(C_n\) on *labelled* vertices, with \(n\ge3\). The tolerance parameter is exactly one: the allowed interior selected-vertex count on at least one shortest path is at most one. The empty set is included by vacuous feasibility. Counts distinguish vertex-labelled subsets, not rotation or reflection orbits. All formulas are exact in integers, with no asymptotic assumption except in the explicitly stated limit.

## Proof

**1. Degree bound and the first four coefficients.** The empty set and all sets of size at most three qualify: between any two selected vertices there is at most one other selected vertex anywhere in the graph. If \(|S|\ge6\), select six of its elements in circular order \(x_1,\ldots,x_6\). Each of the two simple arcs from \(x_1\) to \(x_4\) contains at least two other selected elements (respectively \(x_2,x_3\) and \(x_5,x_6\)). Every shortest path on a cycle is one of these arcs. Hence \(S\) is not one-tolerant mutually visible. This proves the degree bound (which also follows from the previously established scalar invariant).

For four selected vertices the only possible obstruction is a pair whose uniquely shortest arc has the other two selected vertices internally. Such an arc exists exactly when one complementary cyclic gap has length *strictly greater* than \(n/2\). At a tie, the other shortest arc contains no selected internal vertices. Put \(m=\lfloor n/2\rfloor\). The four-point condition is therefore precisely that all four gaps are at most \(m\).

There are \(\binom{n-1}{3}\) positive ordered compositions of \(n\) into four gaps. A specified gap exceeding \(m\) occurs in \(\binom{n-m-1}{3}\) of them; two such gaps cannot coexist because \(2(m+1)>n\). The number of feasible ordered compositions is consequently
\[
Q_4(n)=\binom{n-1}{3}-4\binom{n-m-1}{3}.
\]
The \(n\) choices of a marked first selected vertex, divided by the four possible marks in each labelled four-set, yield \(A_4(n)=nQ_4(n)/4\). Elementary binomial simplification gives the displayed parity formulas.

**2. Five-point geometric criterion.** Among five selected vertices, a bad pair cannot be antipodal: two equal shortest half-cycle paths together contain the other three selected vertices, so at least one half contains at most one of them. Thus failure occurs exactly when a *uniquely shorter* arc between selected endpoints contains at least two other selected vertices. In that case it contains a span of four consecutive selected vertices; conversely any arc spanning four consecutive selected vertices and having length strictly less than \(n/2\) is a bad shortest arc. Writing the five gaps cyclically, feasibility is therefore equivalent to requiring every sum of three consecutive gaps to be at least \(n/2\). For odd \(n\) this means at least \(\lfloor n/2\rfloor+1\), and for even \(n\) at least \(n/2\). Since the complementary two-gap sum is \(n\) minus the three-gap sum, both cases are equivalent to
\[
g_i+g_{i+1}\le m\qquad(i=1,\ldots,5).
\]

**3. Inclusion-exclusion for the five-point coefficient.** Among all \(\binom{n-1}{4}\) positive ordered five-gap compositions, define the violation event \(E_i\) by \(g_i+g_{i+1}\ge m+1\). Two nonconsecutive violation events use four disjoint positive gap variables and cannot occur together, because their sums would total at least \(2(m+1)>n\). The five event indices form a five-cycle, which has no three pairwise adjacent distinct vertices. Hence no triple intersection is nonempty. Denoting \(B=|E_i|\) and \(I=|E_i\cap E_{i+1}|\), the number of feasible positive five-gap compositions is exactly
\[
Q_5(n)=\binom{n-1}{4}-5B+5I.
\]
Set \(t=n-m-1\). Count a composition in \(E_i\) by the sum \(h\) of its complementary three gaps. The allowed range is \(3\le h\le t\). For each \(h\) the complementary three gaps have \(\binom{h-1}{2}\) compositions and the offending pair has \(n-h-1\) compositions, giving
\[
B=\sum_{h=3}^{t}(n-h-1)\binom{h-1}{2}
=(n-1)\binom t3-3\binom{t+1}{4}.
\]
For adjacent events \(E_1,E_2\), fix the shared gap \(b=g_2\) and put \(a=\max\{1,m+1-b\}\). Then \(g_1,g_3\ge a\), while \(g_4,g_5\ge1\), so
\[
I=\sum_{b=1}^{n-4}\binom{n-b-2a+1}{3}
=\begin{cases}
\binom{m-1}{4}+\binom m4,&n=2m,\\
\binom m4+\binom{m+1}{4},&n=2m+1.
\end{cases}
\]
Here binomial coefficients with an upper index smaller than the nonnegative lower index are interpreted as zero. Each feasible five-set determines five choices of marked selected vertex, whereas there are \(n\) ways to realize a cyclic five-gap composition with a prescribed marked start. Thus \(A_5(n)=nQ_5(n)/5\). Substituting the displayed expressions for \(B\) and \(I\) and expanding binomial coefficients gives the claimed even and odd closed forms.

**4. Endpoints and density.** For \(n=3,4\), every geodesic has at most one internal vertex, so all subsets qualify. For \(n\ge5\), the formulas above give \(A_5(n)>0\), proving exact degree five. In either parity \(n=2m\) or \(2m+1\), \(A_5(n)=m^5/60+O(m^4)\) while \(\binom n5=4m^5/15+O(m^4)\); their ratio tends to \(1/16\).

## Verification

The standalone script `verify.py` constructs each labelled cycle and, for every subset, checks every pair of chosen vertices against all shortest clockwise and anticlockwise paths. It exhaustively compares the resulting full polynomial against the displayed coefficients for every \(3\le n\le18\). In a separate check, it enumerates positive cyclic gap compositions of lengths four and five and compares the geometric conditions with both coefficients for \(5\le n\le32\). These finite tests corroborate the formulas but do not replace the unrestricted argument above.

For concrete reference,
\[
\mathcal V_1(C_8;z)=1+8z+28z^2+56z^3+62z^4+32z^5
\]
and
\[
\mathcal V_1(C_9;z)=1+9z+36z^2+84z^3+90z^4+27z^5.
\]

## Relationship to prior work

Tonny and Shikhi's 2026 *Mutual k-Visibility in Graphs* introduces \(k\)-mutual visibility and establishes \(\mu_k(C_n)=\min\{n,2k+3\}\) (cycle proposition, numbered 14 in the inspected third arXiv version). In particular, it determines the maximum size five for tolerance one, but does not define or enumerate the present fourth- and fifth-order cycle set-counting coefficients or give the cyclic-gap characterization of all maximum sets. Our argument independently derives that degree and supplies the missing full enumeration. Their paper's other results concern general bounds, block graphs, complexity and related graph classes.

The earlier ordinary visibility polynomial treated by Bujtás, Klavžar and Tian (2025) and by Tonny and Shikhi (2025) has *zero* tolerance; on cycles its degree is three. The distinction is essential: the fourth- and fifth-order coefficients in this theorem are absent from that older polynomial and are not determined by it. OEIS A392421 likewise tabulates three-element, zero-tolerance visibility sets of cycles, not the five-element one-tolerance sets counted here.

## Limitations

The enumeration is specific to cycles and tolerance exactly one. It does not give the full \(k\)-visibility polynomial for general \(k\), nor results for arbitrary graphs. The independent literature comparison cannot exclude an undiscovered equivalent enumeration in differently named work. The computer checks are finite, and independent mathematical validation has not been performed.

## References

1. Tonny K. B. and Shikhi M., *Mutual k-Visibility in Graphs*, arXiv:2602.14500v1, publicly submitted 2026-02-16, especially its definition of \(k\)-mutual visibility and the cycle result (Proposition 14 in version 3). https://arxiv.org/abs/2602.14500
2. Tonny K. B. and Shikhi M., *On the Visibility Polynomial of Graphs*, arXiv:2507.01851v1, publicly submitted 2025-07-02, especially Theorem 6 (zero tolerance). https://arxiv.org/abs/2507.01851
3. C. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes mathematicae 99 (2025), 1883–1901, DOI 10.1007/s00010-025-01197-y, especially Section 3. https://doi.org/10.1007/s00010-025-01197-y
4. OEIS A392421, *Number of mutual-visibility sets of size 3 in the n-cycle graph* (zero-tolerance sequence). https://oeis.org/A392421
