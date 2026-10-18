# Roman-domination polynomial and minimum-labeling classification of triangular graphs

## Finding

For every integer \(n\ge3\), the triangular graph \(T_n=J(n,2)=L(K_n)\) has one vertex for each unordered pair of elements of \([n]\), with adjacency when the two pairs intersect. Its Roman-domination polynomial is
\[
R_n(z)=\sum_{f}z^{\sum_{e\in E(K_n)}f(e)},
\]
where the sum ranges over all functions \(f:E(K_n)\to\{0,1,2\}\) such that every edge assigned zero intersects an edge assigned two. Set \(N=\binom n2\). For integers \(s\ge0\) and \(m\ge0\), define
\[
A_s(m)=\sum_{j=0}^{s}(-1)^j\binom{s}{j}\binom{\binom{s-j}{2}}{m},
\]
where binomial coefficients with an inadmissible lower index vanish. Then **every coefficient** is given by the finite closed expression
\[
\boxed{R_n(z)=\sum_{w=0}^{n}\binom nw\sum_{m=0}^{\binom{n-w}{2}} A_{n-w}(m)\,z^{2m+\binom w2}(1+z)^{N-m-\binom w2}.}
\]
In addition, every function attaining the minimum weight \(n-1\) is uniquely of the following form: if \(n\) is odd, precisely the edges of a perfect matching on \(n-1\) ground vertices have label two, and all other edges have label zero; if \(n\) is even, the label-two edges constitute a perfect matching on \(n-2\) ground vertices, the edge joining the two omitted ground vertices has label one, and all remaining edges have label zero. Consequently, the **numbers** of minimum functions are
\[
\boxed{[z^{n-1}]R_n(z)=\begin{cases}
n(n-2)!!,&n\text{ odd},\\[2pt]
\binom n2(n-3)!!,&n\text{ even}.
\end{cases}}
\]
Here \((2r-1)!!=1\cdot3\cdots(2r-1)\) and \((-1)!!=1\). The minimum-weight value \(\gamma_R(T_n)=n-1\) was already proved by Zec (2023); the statement here is the complete weight enumerator and exhaustive minimum-function classification.

## Assumptions and scope

Graphs are finite, simple, and labeled; distinct functions on the fixed \(\binom n2\) vertices are counted distinctly. The result holds for **every** integer \(n\ge3\), with no asymptotic, parity, or generic-position assumption. Polynomial coefficients count functions, not orbits under graph automorphisms. No assertion is made about Roman-domination polynomials of \(J(n,k)\) for \(k\ge3\).

## Proof

**Forced-label lemma.** Fix the set \(F\subseteq E(K_n)\) of edges carrying label two. Write \(m=|F|\), let \(U\) be the union of the endpoints of \(F\), and let \(W=[n]\setminus U\), with \(w=|W|\). An edge of \(K_n\) is nonadjacent to every edge of \(F\) precisely when both its endpoints lie in \(W\). Therefore every one of the \(\binom w2\) edges within \(W\) must carry label one, while every other edge outside \(F\) may independently carry zero or one. For this fixed \(F\), the entire generating contribution is
\[
z^{2m+\binom w2}(1+z)^{N-m-\binom w2}.
\]
This characterization is necessary and sufficient, including the case \(F=\varnothing\).

**Counting the label-two sets.** Fix \(W\), so that \(s=n-w\) ground vertices remain. The graph \(([n]\setminus W,F)\) has exactly \(s\) vertices, \(m\) edges, and no isolated vertices; conversely every such graph gives an eligible \(F\) with precisely this set \(W\) of unused ground vertices. By inclusion-exclusion on the vertices required not to be isolated, the count is exactly \(A_s(m)\). There are \(\binom nw\) choices of \(W\). Multiplying by the forced-label contribution and summing over \(w,m\) proves the polynomial formula. In particular \(A_0(0)=1\) and \(A_1(0)=0\), so both boundary cases are included without a separate convention beyond the stated binomial rule.

**Minimum configurations.** If \(s=n-w\ge2\), absence of isolated vertices implies \(m\ge\lceil s/2\rceil\). Every function corresponding to \(F\) therefore has weight at least
\[
2\left\lceil\frac{s}{2}\right\rceil+\binom w2
=n-1+\frac{(w-1)(w-2)}{2}+\mathbf1_{s\text{ odd}}.
\]
For nonnegative integer \(w\), the last two terms are nonnegative. Equality is possible only for \(w\in\{1,2\}\) and even \(s\); equivalently, \(w=1\) for odd \(n\), or \(w=2\) for even \(n\). If \(s=1\), no nonempty simple graph on these vertices has no isolated vertices, so this case is impossible. If \(s=0\), all edges are forced to label one and the weight is \(N>n-1\) for \(n\ge3\).

For equality with even \(s\), one must have \(m=s/2\) and no optional label-one edges. A simple graph on \(s\) vertices with \(s/2\) edges and no isolates is necessarily a perfect matching. These choices indeed attain weight \(n-1\), proving the stated structural classification. The numbers of labeled perfect matchings on the remaining even vertex sets are \((n-2)!!\) in the odd case and \((n-3)!!\) in the even case; choose the omitted vertices in \(n\) and \(\binom n2\) ways respectively. This gives the exact multiplicities, and recovers the previously known minimum weight.

## Verification

The accompanying standalone standard-library program `verify.py` computes the polynomial by the inclusion-exclusion formula and checks it in two separate ways. First, it enumerates all \(3^{\binom n2}\) labelings directly for \(3\le n\le5\), testing the Roman condition on the actual triangular graph. Second, it independently enumerates every subset of possible label-two edges for \(3\le n\le6\), determines the forced labels directly, and expands the remaining independent zero/one choices. All polynomial coefficients agree. The program also verifies the minimum weight and exact multiplicity for \(3\le n\le18\). These finite checks test the algebra and implementation; the preceding unrestricted proof establishes the result for all \(n\ge3\).

For example, the low-weight portions are \(R_3(z)=3z^2+7z^3+6z^4+3z^5+z^6\), \([z^3]R_4(z)=6\), \([z^4]R_5(z)=15\), and \([z^5]R_6(z)=45\).

## Relationship to prior work

Chambers, Kinnersley, Prince, and West (2009) develop general extremal Roman domination theory. Gangabylaiah, Indiramma, Soner, and Alwardi (2021) introduce the Roman-domination polynomial and give formulas for several graph families and operations, but their examined results do not give the triangular-graph polynomial. Zec (2023), Theorem 2.1, proves \(\gamma_R(J(n,2))=n-1\) and exhibits one minimum function for each parity; this minimum **value and those examples are prior work**, not claimed as original here. The formula above counts every weight, classifies *all* minimum functions, and yields their exact multiplicities. Roman domination of \(L(K_n)\) is equivalently edge Roman domination of \(K_n\), which is included in the comparison terminology.

## Limitations

This is an exact enumeration of labeled functions, not an enumeration up to symmetry. The result does not settle Roman domination on higher Johnson graphs. No independent mathematical audit has been performed. An older equivalent enumeration under the terms *edge Roman domination of complete graphs* or *triangular-graph Roman domination polynomial* remains a possible priority risk, despite the literature comparisons described in the accompanying scientific review.

## References

1. E. W. Chambers, B. Kinnersley, N. Prince, D. B. West, “Extremal Problems for Roman Domination,” *SIAM J. Discrete Math.* **23** (2009), 1575–1586, DOI: 10.1137/070699688. Public online date: 2009-10-29.
2. Deepak Gangabylaiah, Indiramma M. H., Nandappa D. Soner, Anwar Alwardi, “On the Roman Domination Polynomial of Graphs,” *Bull. Int. Math. Virtual Inst.* **11** (2021), 355–365, DOI: 10.7251/BIMVI2102355G; open text: https://www.imvibl.org/buletin/bulletin_imvi_11_2_2021/bulletin_imvi_11_2_2021_355_365.pdf.
3. Tatjana Zec, “On the Roman Domination Problem of Some Johnson Graphs,” *Filomat* **37** (2023), 2067–2075, DOI: 10.2298/FIL2307067Z; open text: https://www.pmf.ni.ac.rs/filomat-content/2023/37-7/37-7-6-18102.pdf.
4. A. Mahmoodi, A. Behmaram, T. Došlić, N. Asadi, “Dominating Induced Matchings and Other Graph Parameters,” *AKCE Int. J. Graphs Combin.* **21** (2024), 261–267, DOI: 10.1080/09728600.2024.2342310 (edge Roman domination discussed in Section 3).
