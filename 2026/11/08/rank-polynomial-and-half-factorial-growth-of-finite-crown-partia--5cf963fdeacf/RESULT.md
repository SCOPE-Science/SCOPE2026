# Rank polynomial and half-factorial growth of finite crown partial-automorphism monoids

## Finding

Let \(N\ge4\) be even. Give the vertices \(\mathbb Z/N\mathbb Z\) the height-two crown order in which every even vertex is below its two neighboring odd vertices, with no other strict comparisons. Let \(\mathcal I_N\) be the inverse monoid of all isomorphisms between induced subposets (including the empty map), and let \(r_{N,k}\) count its elements whose domain has size \(k\).

The following finite, explicit two-state coefficient formula determines the **entire rank polynomial** \(R_N(u)=\sum_{k=0}^N r_{N,k}u^k\), for every even \(N\ge4\).

Define a finite alphabet of path types \(\mathcal T_N\): \(s\) (one isolated point), \(e_\ell\) for even \(2\le\ell<N\), and \(o_{\ell,p}\) for odd \(3\le\ell<N\) and \(p\in\{0,1\}\). Give these types sizes \(|s|=1\), \(|e_\ell|=\ell\), and \(|o_{\ell,p}|=\ell\), and internal automorphism numbers \(h_s=h_{e_\ell}=1\), \(h_{o_{\ell,p}}=2\). For each formal variable \(X_t\) indexed by a type \(t\), put

\[
\tau(\ell,p)=\begin{cases}
 s,&\ell=1,\\
 e_\ell,&\ell\text{ even},\\
 o_{\ell,p},&\ell\ge3\text{ odd}.
\end{cases}
\]

Form a matrix of formal power series \(T(z,\mathbf X)=(T_{pq})_{p,q\in\{0,1\}}\) with

\[
T_{pq}=\sum_{\ell\ge1}\sum_{g\ge1}
 {\bf1}_{\{q\equiv p+\ell+g\pmod2\}}
 z^{\ell+g}X_{\tau(\ell,p)}.
\]

Only terms of degree at most \(N\) are retained, so every expression is finite; in particular, \(\ell<N\). Define

\[
P_N(\mathbf X)=\frac N2\sum_{r=1}^{\lfloor N/2\rfloor}
 \frac1r[z^N]\operatorname{tr}\big(T(z,\mathbf X)^r\big),
\quad
A_N(\mathbf c)=[\mathbf X^{\mathbf c}]P_N(\mathbf X).
\]

Every \(A_N(\mathbf c)\) is a nonnegative integer. With \(\mathbf c=(c_t)_{t\in\mathcal T_N}\), the promised exact rank polynomial is

\[
\boxed{
R_N(u)=1+Nu^N+
\sum_{\mathbf c} A_N(\mathbf c)^2
\left(\prod_{t\in\mathcal T_N}c_t!h_t^{c_t}\right)
 u^{\sum_t|t|c_t}.
}
\]

The sum has finite support, namely the coefficient support of \(P_N\). In particular,

\[
r_{N,0}=1,\qquad r_{N,1}=N^2,\qquad
r_{N,2}=N^2+\frac{N^2(N-3)^2}{2},\qquad
r_{N,N-1}=N^2,\qquad r_{N,N}=N.
\]

For every even \(N\ge6\), there is also the explicit near-full-rank formula

\[
\boxed{r_{N,N-2}=\frac{N^2(3N-8)}4.}
\]

The first total cardinalities, for \(N=4,6,8,10,12,14,16\), are respectively

\[
61,\quad571,\quad6889,\quad101041,\quad1723621,\quad33233943,\quad711242001.
\]

The exact leading logarithmic growth and the rarity of globally extendible maps are

\[
\boxed{\lim_{N\to\infty,\,2\mid N}\frac{\log|\mathcal I_N|}{N\log N}=\frac12.}
\]

If \(E_N\) is the number of restrictions of full crown automorphisms, then

\[
\boxed{\lim_{N\to\infty,\,2\mid N}
\frac{\log(E_N/|\mathcal I_N|)}{N\log N}=-\frac12.}
\]

## Assumptions and scope

The ground poset is the labeled, even crown with \(N\ge4\); \(N\) denotes its number of vertices, not its minimum generator count. A partial automorphism must preserve and reflect all strict comparabilities; mere one-way order-preserving injections form a different semigroup. The rank \(k\) is the size of the domain of a partial map. All enumerations are of distinct embedded partial maps, not abstract isomorphism classes or maps modulo dihedral symmetry. Throughout, \(\log\) is natural logarithm.

## Proof

**1. Component-type classification.** Every proper nonempty vertex subset has induced comparability graph a disjoint union of paths. Paths consisting of a single vertex are all mutually isomorphic as induced posets, regardless of the original vertex's parity; this is the type \(s\). For a path of even length \(\ell\ge2\), clockwise-starting with an even or odd vertex yields isomorphic ordered paths by reversal, but the path has no nonidentity order automorphism; this gives one type \(e_\ell\). For odd \(\ell\ge3\), both endpoints are minimal or both are maximal. These two possibilities are nonisomorphic, recorded by the parity \(p\) of the clockwise initial vertex, and each path admits the reversal involution, giving \(h=2\). Thus a proper nonempty subset \(S\) has a unique multiset of types \(\mathbf c(S)\). Two such induced posets are isomorphic precisely when their multisets agree.

For a fixed multiset \(\mathbf c\), an isomorphism permutes components of each type and independently uses automorphisms of those components. Hence the number of isomorphisms between any two subsets of that type equals

\[
a(\mathbf c)=\prod_{t\in\mathcal T_N}c_t!h_t^{c_t}.
\]

**2. Counting subsets by types.** A proper nonempty subset uniquely has \(r\ge1\) clockwise runs of selected vertices, each of length \(\ell_i\ge1\), separated by clockwise gaps \(g_i\ge1\), with \(\sum_i(\ell_i+g_i)=N\). Consequently \(r\le N/2\). Choose one of the \(r\) runs as the marked first run. There are \(N/2\) possible starting vertices of each parity \(p\). The next run starts with parity \(q\equiv p+\ell_i+g_i\pmod2\). The type contribution of that run is \(X_{\tau(\ell_i,p)}\). Therefore the coefficient \([z^N]\operatorname{tr}(T^r)\) sums exactly the allowed clockwise run/gap arrangements with the starting parity restored. The prefactor \(N/2\) selects the actual starting vertex, and division by \(r\) erases the marked run. This proves that \(P_N\) is exactly the multivariate generating polynomial of proper nonempty subsets by type, so \(A_N(\mathbf c)\) is their count.

For each type there are \(A_N(\mathbf c)^2\) ordered domain-image pairs and \(a(\mathbf c)\) isomorphisms per pair. Their rank is \(\sum_t|t|c_t\). The empty map contributes \(1\). The full crown has exactly \(N\) automorphisms (color-preserving dihedral symmetries: \(N/2\) rotations and \(N/2\) reflections), contributing \(Nu^N\). Summing yields the boxed polynomial, with no double counting.

**3. Boundary ranks.** Every singleton domain maps to any of \(N\) targets, so the rank-one coefficient is \(N^2\). An induced two-point subposet is either one of \(N\) oriented comparability edges, with one automorphism, or one of \(\binom N2-N=N(N-3)/2\) antichain pairs, with two automorphisms. Squaring class counts gives the rank-two coefficient. Omitting one vertex leaves a path of odd length \(N-1\). Its endpoints have the same order parity. The two missing-vertex parities give two classes of \(N/2\) subsets, and each path has two automorphisms, yielding \(N^2\) at rank \(N-1\).

For rank \(N-2\), delete an unordered pair of vertices. Let \(d\) be their smaller cyclic separation, \(1\le d\le N/2\). For \(d<N/2\), the two-hole subset count is \(N\); for \(d=N/2\), it is \(N/2\). Applying the component classification to the two remaining paths, the resulting **contribution divided by \(N^2\)** is \(1\) for \(d=1,2\), also \(1\) for odd \(3\le d<N/2\), and \(2\) for even \(4\le d<N/2\). At antipodal separation it is \(1/2\) if \(N/2\) is odd, and \(1\) if \(N/2\) is even. In the latter case the two equal-length odd paths have a component-swap symmetry as well as two reversals, which is essential for the final factor. Summing the weights gives \((3N-8)/4\) for every even \(N\ge6\), proving the stated near-full-rank formula. The smallest crown \(N=4\) is excluded from this formula because its two-hole subposets coincide with the rank-two boundary case.

**4. Logarithmic asymptotics.** The \(N/2\) even vertices form an antichain. All their \((N/2)!\) bijections belong to \(\mathcal I_N\), giving the lower bound. For any proper nonempty subset, there are at most \(N/2\) connected components: each selected run requires an omitted vertex. Every isomorphism between two such induced subposets is determined by a permutation of components and at most one reversal decision for each, so their number is at most \(2^{N/2}(N/2)!\). There are at most \(4^N\) ordered subset pairs. Including the empty and full cases,

\[
(N/2)!\ \le\ |\mathcal I_N|\ \le\ 1+N+4^N2^{N/2}(N/2)!.
\]

Stirling's formula proves the first logarithmic limit. The automorphism group of the entire crown has order \(N\). Each automorphism has at most \(2^N\) distinct restrictions, and all \(N\) full automorphisms occur, so \(N\le E_N\le N2^N\). Thus \(\log E_N=o(N\log N)\), proving the second limit.

## Verification

The standalone `verify.py` (Python standard library only) implements an exact positive-composition expansion of the run/gap transfer formula and checks its multivariate coefficients against an independent enumeration of all vertex subsets for \(N=4,6,8,10,12,14\). It checks the rank polynomial through \(N=16\), verifies the stated low- and high-rank coefficients, and separately enumerates **actual partial injections and both directions of the strict comparability relation** for \(N=4,6,8\) without using the component-type classification. It terminates with `VERIFY_OK`. These finite checks are corroborative; the proof of the formula for arbitrary even \(N\) is the component and marked-run argument above, while the asymptotics follow from factorial bounds.

## Relationship to prior work

Dimitrova and Koppitz (arXiv:2204.13961, first public April 29, 2022) defined and characterized the same crown partial-automorphism inverse monoid and determined its minimum generating-set rank. Their Proposition 2.1 and Theorem 2.18 concern admissibility and generators, not the number of elements of each domain rank. The word *rank* in the title of their paper denotes the size of a smallest generating set, whereas the present rank polynomial grades by domain size.

Dimitrova, Fernandes, Koppitz, and Quinteiro (arXiv:2101.12468) gave cardinality formulas for partial automorphisms of **undirected paths**, using intervals. This supplies a relevant enumerative precedent but neither the cyclic wraparound nor the order orientation of crowns; the odd-length endpoint parities and circular run/gap trace in the present formula are absent there. Jajcay and collaborators (arXiv:1809.04422) established general structural facts about inverse monoids of partial graph and digraph automorphisms, without a crown-specific rank enumeration. Counts for undirected cycle graph partial automorphisms likewise do not determine the directed, parity-sensitive crown counts merely from their unrefined domain-rank totals: the types of odd path components must additionally be distinguished and isolated vertices handled separately.

## Limitations

The result applies to even crowns of at least four vertices, not arbitrary finite posets, fences, or undirected cycle-graph automorphisms. The growth estimates determine sharp logarithmic exponents but not multiplicative asymptotic constants. The transfer formula is a finite coefficient algorithm, not a claim of a rational univariate generating function across different crown sizes. The priority assessment is limited to the compared sources and searchable records; it is not an exhaustive guarantee against equivalent earlier enumerations. No independent mathematical validation is asserted.

## References

1. I. Dimitrova and J. Koppitz, *The rank of the inverse semigroup of all partial automorphisms on a finite crown*, arXiv:2204.13961 (first posted April 29, 2022), https://arxiv.org/abs/2204.13961.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468 (first posted January 29, 2021), https://arxiv.org/abs/2101.12468.
3. R. Jajcay, T. Jajcayová, N. Szakács, and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (first posted September 12, 2018), https://arxiv.org/abs/1809.04422.
