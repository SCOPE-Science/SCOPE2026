# Endpoint Schatten convergence for generalized Aluthge iterates via a Carleman envelope

## Finding
Let \(0<p<\infty\) and \(0<t<1\). For every Schatten-class operator \(T\in\mathcal S_p\) on a complex separable Hilbert space, the generalized Aluthge iterates satisfy
\[
\lim_{n\to\infty}\|\Delta_t^n(T)\|_{\mathcal S_p}^{p}=\sum_{j\ge1}|\lambda_j(T)|^p.
\]
In fact, their ordered singular-value lists converge in \(\ell^p\):
\[
\lim_{n\to\infty}\sum_{j\ge1}\big|s_j(\Delta_t^n(T))-|\lambda_j(T)|\big|^p=0.
\]
A quantitative, iterate-independent tail certificate is available directly from the original singular values: putting
\[
a_j=s_j(T)^p,\qquad G_k=\left(\prod_{j=1}^{k}a_j\right)^{1/k},
\]
with the convention that a product containing zero is zero, one has for every \(n\ge0\) and integer \(K\ge0\),
\[
\sum_{j>K}s_j(\Delta_t^n(T))^p\le\sum_{j>K}G_j,
\qquad\sum_{j\ge1}G_j\le e\|T\|_{\mathcal S_p}^{p}.
\]
The same tail bound holds with \(s_j(\Delta_t^n(T))\) replaced by \(|\lambda_j(T)|\). Thus the diagonal Schatten endpoint, including trace class \(p=1\), requires no membership in a strictly smaller ideal.

## Assumptions and scope
The Hilbert space is complex and separable, finite- or infinite-dimensional. For finite dimension, all sequences are padded with zeros. \(T\in\mathcal S_p\) means \(T\) is compact and \(\sum_j s_j(T)^p<\infty\); this is a quasi-ideal when \(0<p<1\). Its eigenvalues \(\lambda_j(T)\) are ordered by nonincreasing modulus, counted with algebraic multiplicity, and padded with zeros. Write the canonical polar decomposition \(T=U|T|\) and
\[
\Delta_t(T)=|T|^tU|T|^{1-t},\qquad
\Delta_t^0(T)=T,\qquad\Delta_t^{n+1}(T)=\Delta_t(\Delta_t^n(T)).
\]
The parameter is fixed in \((0,1)\). The conclusion is convergence of singular-value **lists**, not convergence in Schatten norm of the operators to a specific normal operator.

## Proof
**1. Two established operator inequalities.** Stanković, arXiv:2611.07728v1, Theorem 1.1, proves for compact \(T\) and every fixed \(j\) that
\[
 s_j(\Delta_t^n(T))\longrightarrow |\lambda_j(T)|.
\]
The same work, using exterior powers and the weak logarithmic-majorization inequality of Antezana, Massey and Stojanoff (2005, Remark 3.12), establishes for every \(n\ge0\) and \(k\ge1\)
\[
 \prod_{j=1}^{k}s_j(\Delta_t^n(T))\le\prod_{j=1}^{k}s_j(T).
\]
The successive iterates are compact: a product of a compact positive power and bounded factors remains compact; the first iterate is compact and so are the rest. All lists are arranged in nonincreasing order.

**2. A uniform geometric-mean envelope.** Fix \(p>0\) and define \(a_j=s_j(T)^p\), \(b_j^{(n)}=s_j(\Delta_t^n(T))^p\). The sequence \(b_j^{(n)}\) is nonincreasing. Hence for every \(k\ge1\),
\[
 (b_k^{(n)})^k\le\prod_{j=1}^{k}b_j^{(n)}\le\prod_{j=1}^{k}a_j.
\]
Taking \(k\)-th roots gives the pointwise domination \(0\le b_k^{(n)}\le G_k\) for every \(k,n\). If an original singular value vanishes, all ensuing products are zero and the same inequality holds without logarithms or division.

**3. Carleman's summable envelope, proved here.** For any nonnegative summable sequence \((a_j)\), the arithmetic–geometric mean inequality applied to \(a_1,2a_2,\ldots,ka_k\) yields
\[
 G_k\le\frac{\sum_{j=1}^{k}j a_j}{k(k!)^{1/k}}
 \le\frac{e}{k(k+1)}\sum_{j=1}^{k}j a_j.
\]
The last inequality uses \((k!)^{1/k}\ge(k+1)/e\), which follows inductively from \((1+1/k)^k<e\) (the base case \(k=1\) is immediate). Sum over \(k\ge1\), interchange nonnegative sums, and telescope:
\[
\sum_{k\ge1}G_k\le e\sum_{j\ge1}j a_j\sum_{k\ge j}\frac1{k(k+1)}
=e\sum_{j\ge1}a_j<\infty.
\]
The calculation proves the needed Carleman inequality directly, including zeros and infinite series. In particular \(\sum_{k>K}G_k\to0\). It also proves \(\Delta_t^n(T)\in\mathcal S_p\) for all \(n\).

**4. Passing to the limit at the same Schatten exponent.** For each \(j\), the nonnegative terms \(b_j^{(n)}\) tend to \(c_j=|\lambda_j(T)|^p\). Since \(b_j^{(n)}\le G_j\), also \(c_j\le G_j\). Dominated convergence for counting measure gives
\[
\sum_j b_j^{(n)}\longrightarrow\sum_j c_j,
\]
which is the first assertion. For the stronger list convergence, for every \(x,y\ge0\),
\[
|x-y|^p\le C_p(x^p+y^p),\qquad C_p=\max\{1,2^{p-1}\}.
\]
Each \(\big|s_j(\Delta_t^n(T))-|\lambda_j(T)|\big|^p\) converges to zero and is at most \(2C_pG_j\). Applying dominated convergence again proves the \(\ell^p\) assertion. The stated tail estimates follow from the same envelope, and the explicit error separation for every \(K\) is
\[
\left|\|\Delta_t^n(T)\|_{\mathcal S_p}^{p}-\sum_j|\lambda_j(T)|^p\right|
\le\sum_{j\le K}\left|s_j(\Delta_t^n(T))^p-|\lambda_j(T)|^p\right|+2\sum_{j>K}G_j.
\]
All limits and bounds hold for every fixed \(p>0\) and \(0<t<1\). \(\square\)

## Verification
The universal claim is a deduction from precisely identified published singular-value convergence and weak product-majorization statements, combined with the self-contained scalar Carleman proof above. No finite computation is used to deduce a statement about infinitely many singular values. A standalone standard-library checker (`CHECK.py`) separately tests finite geometric-mean envelopes and generalized Aluthge iterations of cyclic and nilpotent weighted shifts for several Schatten exponents, including \(p<1\). Such tests check normalization and implementation only, not the infinite theorem.

## Relationship to prior work
Stanković, *Singular values of iterated Aluthge transforms of compact operators* (first public 2026-11-05, arXiv:2611.07728v1), gives coordinatewise singular-value convergence and weak logarithmic majorization, and identifies the \(\mathcal S_p\)-norm limit under the stronger hypothesis \(T\in\mathcal S_q\) for \(q<p\) (Theorem 5.5). Remark 5.7 explicitly leaves the equal-exponent case open, particularly the trace norm for operators belonging to no \(\mathcal S_q\) with \(q<1\). The present argument supplies the missing uniform summability by a geometric-mean envelope and answers that stated question, extending the conclusion to every \(p>0\) without stronger ideal membership.

Antezana, Massey and Stojanoff (2005, Remark 3.12) already prove the weak product-majorization inequality; its novelty is not claimed here. Carleman's summability inequality is classical and is rederived above, not claimed as a new scalar inequality. Their combination with the new 2026 coordinatewise limit yields the presently stated operator conclusion. The broader measurable-operator framework of Dodds, Dodds, Sukochev and Zanin (2019) treats logarithmic submajorization and Hölder inequalities, not this dynamical Schatten endpoint. The earlier matrix convergence work of Antezana, Pujals and Stojanoff is finite-dimensional, where no infinite-tail obstruction arises.

## Limitations
This proof uses Stanković's fixed-index convergence theorem rather than reproving that deep operator-theoretic input. It does not assert convergence of the operators themselves, a convergence rate in the iteration index, an endpoint result for \(t=0\) or \(t=1\), or convergence in arbitrary symmetric operator ideals. The envelope gives an effective **tail** in terms of the singular values of \(T\), but the finite-head convergence has no universal rate in \(n\). Publication priority for a possible earlier equivalent formulation of the combined Carleman and log-majorization argument remains to be independently checked.

## References
1. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1 (first public November 5, 2026), Theorem 1.1, Theorem 4.1, Theorem 5.5 and Remark 5.7. https://arxiv.org/html/2611.07728v1
2. J. Antezana, P. Massey, D. Stojanoff, *\(\lambda\)-Aluthge transforms and Schatten ideals*, Linear Algebra Appl. 405 (2005), 177–199, especially Remark 3.12. https://doi.org/10.1016/j.laa.2005.03.016
3. P. Dodds, T. Dodds, F. Sukochev, D. Zanin, *Logarithmic submajorization, uniform majorization and Hölder type inequalities for \(\tau\)-measurable operators*, arXiv:1910.10874 (2019). https://arxiv.org/abs/1910.10874
4. J. Antezana, E. Pujals, D. Stojanoff, *Convergence of iterated Aluthge transform sequence for diagonalizable matrices II: \(\lambda\)-Aluthge transform*, arXiv:0706.1234 (2007). https://arxiv.org/abs/0706.1234
5. T. Carleman, classical geometric-mean summability inequality (1923); a complete elementary proof of the precise form used appears in Section 'Proof' above.
