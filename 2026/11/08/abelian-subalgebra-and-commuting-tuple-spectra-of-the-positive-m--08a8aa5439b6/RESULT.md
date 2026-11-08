# Abelian-subalgebra and commuting-tuple spectra of the positive modular Witt nilradical

## Finding
Let \(p>3\) be prime, let \(k=\mathbb F_q\) with \(q\) any power of \(p\), and put \(m=(p-1)/2\). In the modular Witt algebra \(W=\operatorname{Der}_k(k[x]/(x^p))\), let
\[
\mathfrak n=\left\{f(x)\partial_x:f\in x^2k[x]/(x^p)\right\},\qquad
L_j=x^jk[x]/(x^p)\,\partial_x.
\]
Define \(A_d(p,q)\) to be the number of *individual* \(d\)-dimensional abelian Lie subalgebras (not conjugacy classes) of \(\mathfrak n\). Then \(A_0=1\), \(A_d=0\) for \(d>m\), and for \(1\le d\le m\),
\[
\boxed{A_d(p,q)={m\brack d}_q+\sum_{s=\max(2,d)}^m q^{p-s-d}{s-1\brack d-1}_q,}
\]
where \({n\brack d}_q\) is the Gaussian binomial coefficient. In particular, there are exactly \(q+1\) maximal-dimensional abelian subalgebras, each of dimension \(m\); they are naturally indexed by \(\mathbb P^1(k)\).

For any integer \(r\ge1\), let \(T_r(p,q)\) count all **ordered, pairwise commuting** \(r\)-tuples of elements of \(\mathfrak n\), allowing repeats and zeros. Then
\[
\boxed{T_r(p,q)=q^{mr}+(q^r-1)\sum_{s=2}^m q^{p-r+s(r-2)}.}
\]
Consequently, for fixed \(p,q\), \(\lim_{r\to\infty}T_r(p,q)/q^{mr}=q+1\). The tuple count is related to the abelian-subalgebra spectrum by
\[
T_r(p,q)=\sum_{d=0}^m A_d(p,q)\prod_{j=0}^{d-1}(q^r-q^j),
\]
with an empty product equal to one. These identities hold for every finite extension of the prime field, not only for prime fields.

## Assumptions and scope
Throughout, \(p\) is prime and strictly larger than three. The Lie bracket in \(\mathfrak n\) is \([f\partial_x,g\partial_x]=(fg'-gf')\partial_x\bmod x^p\). The vector-space dimension is \(p-2=2m-1\). An abelian subalgebra is any \(k\)-linear subspace closed under the zero bracket; no ideals, restricted-subalgebra conditions, or conjugacy identifications are imposed. For the geometric classification of maximal-dimensional abelian subalgebras, \(k\) may be any field of characteristic \(p\). The numerical formulas require finite \(k=\mathbb F_q\).

## Proof
**Centralizer lemma.** Suppose \(0\ne f\partial_x\in\mathfrak n\) has lowest nonzero monomial degree \(s\), where \(2\le s\le m\). Then
\[
C_{\mathfrak n}(f\partial_x)=k(f\partial_x)\oplus L_{p-s+1},\qquad\dim C_{\mathfrak n}(f\partial_x)=s,
\]
and this centralizer is abelian. To prove it without invoking any classification theorem, write \(f=x^su\) with \(u\in k[[x]]^\times\). For \(g\in x^2k[x]/(x^p)\), express \(g/f=h\in k((x))\). The equation \(fg'-gf'=0\bmod x^p\) is \(f^2h'=0\bmod x^p\). Coefficients of \(h\) relevant to \(g\bmod x^p\) have exponents \(j\) in the interval \(2-s\le j\le p-1-s\), entirely inside \((-p,p)\). Since \(f^2=x^{2s}u^2\), the commutator vanishes exactly when the coefficient of every \(x^j\), with \(j\ne0\) and \(j\le p-2s\), is zero. The only exponent divisible by \(p\) in this interval is zero, so \(h=c+x^{p-2s+1}h_1\) for the relevant terms. Therefore \(g=cf+v\) with \(v\in x^{p-s+1}k[x]/(x^p)\). Conversely every such element commutes with \(f\), because the bracket starts in degree at least \(p\). As \(2(p-s+1)-1\ge p\) for \(s\le m\), the tail \(L_{p-s+1}\) is abelian, completing the lemma.

**Classification and count of abelian subalgebras.** The tail \(H=L_{m+1}\) is an abelian subalgebra of dimension \(m\). Any abelian subalgebra \(U\) not contained in \(H\) has a minimal nonzero monomial degree \(s\in\{2,\ldots,m\}\). Choose \(f\in U\) with leading coefficient one in degree \(s\). The lemma implies \(U\subset kf\oplus L_{p-s+1}\), and \(U=kf\oplus V\), where \(V=U\cap L_{p-s+1}\) is an arbitrary subspace of dimension \(d-1\) in the \((s-1)\)-dimensional tail. There are \({s-1\brack d-1}_q\) choices for \(V\). For fixed \(V\), the normalized cosets of \(f\) modulo \(V\) have \(p-1-s-(d-1)=p-s-d\) free coefficients, hence \(q^{p-s-d}\) choices. Their uniqueness follows by using the normalized leading coefficient and quotienting by \(V\). Subalgebras contained in \(H\) contribute \({m\brack d}_q\), proving \(A_d\). The centralizer bound implies \(d\le m\). Equality occurs either for \(U=H\), or \(s=m\) and
\[
U=k(x^m+a x^{m+1})\partial_x\oplus L_{m+2},\quad a\in k.
\]
These are distinct and exhaust the maximum-dimensional case, giving the natural \(k\cup\{\infty\}=\mathbb P^1(k)\) parametrization.

**Ordered commuting tuples.** Every tuple entirely in \(H\) commutes, giving \(q^{mr}\) tuples. Otherwise its smallest nonzero monomial degree is \(s\in\{2,\ldots,m\}\). Let the first coordinate attaining degree \(s\) have position \(i\). This coordinate can be chosen in \((q-1)q^{p-1-s}\) ways. Every earlier coordinate lies in the \((s-1)\)-dimensional abelian tail \(L_{p-s+1}\) (the intersection of the centralizer with elements of degree greater than \(s\)); every later coordinate is arbitrary in the abelian centralizer of dimension \(s\). Thus the contribution for this \(s,i\) equals
\[
(q-1)q^{p-1-s}q^{(s-1)(i-1)+s(r-i)}.
\]
Summing over \(i=1,\ldots,r\) yields \((q^r-1)q^{p-r+s(r-2)}\). Summing over \(s\) proves \(T_r\). Alternatively, each tuple spans a unique abelian subalgebra; for a fixed \(d\)-space the number of ordered \(r\)-tuples spanning it is \(\prod_{j=0}^{d-1}(q^r-q^j)\), proving the displayed identity between both spectra. In the asymptotic formula the \(s=m\) summand contributes \(q\) after division by \(q^{mr}\); the other summands tend to zero, giving \(q+1\).

## Verification
The supplied dependency-free checker independently constructs the Witt bracket on the original coefficient basis. For \(p=q=5\), it exhaustively tests all ordered pairs of 125 elements, then all commuting triples and quadruples through adjacency intersections. The observed counts are \(3625\), \(93125\), and \(2340625\), respectively. It independently constructs all 31 two-dimensional subspaces of the three-dimensional algebra in reduced-row-echelon form, obtaining exactly six abelian planes and 31 abelian lines. For \(p=q=7\), it independently computes the commutator-map rank of each of the 16,807 elements, yielding \(1,731,121\) ordered commuting pairs. Finally it checks the Gaussian spanning identity over \(p\in\{5,7,11\}\), \(r\in\{2,3,4\}\). All these checks passed. They are finite corroborations; the proof above establishes the unrestricted conclusions.

## Relationship to prior work
Yao and Chang's 2013 preprint *Nilpotent commuting varieties of the Witt algebra* (arXiv:1301.5667v1), particularly Lemma 2.3 and Section 4, supplies an earlier centralizer classification and the irreducible-component geometry for commuting pairs in this nilradical. The centralizer lemma is therefore not claimed as new. The present mathematical assertion is the **dimension-refined finite-field count of every abelian subalgebra** and its coherent all-arity commuting-tuple count. It uses the centralizer structure to derive arithmetic subspace enumerators, rather than merely restating pair-component geometry. Yao's 2015 paper on nilpotent commuting \(r\)-tuple varieties is a closely related priority risk: its accessible abstract describes irreducible components and dimensions, but its full text was unavailable for comparison. Yao and Zhang's 2021 paper on full-Witt commuting \(r\)-tuples is also relevant; accessible material is restricted to the published abstract. The present claims should not be interpreted as independent historical-priority certification.

## Limitations
The count concerns the positive nilradical \(\mathfrak n\), not the full Witt algebra or all Borel subalgebras. It counts actual subspaces and labeled ordered tuples over \(\mathbb F_q\), not orbits under automorphisms. No assertion about irreducible components or nonreduced scheme structures of higher tuple varieties is made. The finite-field proof covers all extensions \(q=p^e\), but machine checks were performed only at the prime-field examples stated above. A complete full-text comparison with Yao (2015) remains an originality risk. Independent mathematical audit has not been performed.

## References
1. Y.-F. Yao and H. Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1, first posted 2013-01-23; especially Lemma 2.3 and Section 4. https://arxiv.org/abs/1301.5667
2. Y.-F. Yao, *On nilpotent commuting varieties of \(r\)-tuples in the Witt algebra*, Journal of Pure and Applied Algebra 219 (2015), 4042–4054. https://doi.org/10.1016/j.jpaa.2015.02.005 (abstract only inspected).
3. Y.-F. Yao and Y. Zhang, *Commuting variety of \(r\)-tuples over the Witt algebra*, Journal of East China Normal University (Natural Science) 2021 (3), 1–7. https://doi.org/10.3969/j.issn.1000-5641.2021.03.001 (abstract only inspected).
4. N. V. Ngo, *Commuting varieties of \(r\)-tuples over Lie algebras*, arXiv:1209.1659v1 (2012), for broader context in classical Lie algebras. https://arxiv.org/abs/1209.1659
