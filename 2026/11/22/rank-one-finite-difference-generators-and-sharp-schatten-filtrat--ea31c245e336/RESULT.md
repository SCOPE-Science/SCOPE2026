# Rank-one finite-difference generators and sharp Schatten filtration for critical Fock integral jets

## Finding

On the standard one-variable Gaussian Bargmann–Fock space, fix an integer \(h\ge1\). For each integer \(j\ge0\) let
\[
A_{h,j}=I^{h+j}M_{z^h}D^j,
\qquad (If)(z)=\int_0^z f(w)\,dw,\quad Df=f',
\]
initially on polynomials and then extended boundedly. Write \(\Delta_j A_{h,j}=A_{h,j+1}-A_{h,j}\), and let \(S\) be the forward shift of the orthonormal monomial basis \(e_k(z)=z^k/\sqrt{k!}\). The family has the following exact structural and spectral properties.

**(a) Rank-one termination.** For every \(j\ge0\),
\[
\boxed{\displaystyle
\Delta_j^{h+1}A_{h,j}
=(-1)^{h+1}h!\sqrt{\frac{j!}{(j+2h)!}}\,
|e_{j+2h}\rangle\langle e_j|.}
\]
Thus the \((h+1)\)-st finite difference is nonzero rank one for *every* \(j\), rather than merely compact.

**(b) Sharp nonterminating hierarchy.** For every integer \(1\le r\le h\), the singular values of \(\Delta_j^r A_{h,j}\), in nonincreasing order and counting multiplicity, satisfy
\[
\boxed{\displaystyle s_N(\Delta_j^r A_{h,j})\sim
\frac{h!}{(h-r)!}\,N^{-r}\qquad(N\to\infty).}
\]
Consequently, for every real \(p>0\),
\[
\Delta_j^r A_{h,j}\in\mathcal S_p\quad\Longleftrightarrow\quad p>1/r,
\]
and the operator belongs to \(\mathcal S_{1/r,\infty}\setminus\mathcal S_{1/r}\) at the critical endpoint. Its critical logarithmic spectral sum has coefficient
\[
\lim_{N\to\infty}\frac{1}{\log N}
\sum_{n=1}^{N}s_n(\Delta_j^r A_{h,j})^{1/r}
=\left(\frac{h!}{(h-r)!}\right)^{1/r}.
\]
These constants do not depend on \(j\).

**(c) Exact closed-span and minimality statements.** Let \(\mathcal K_{2h}\) be the norm-closed space of compact weighted shifts supported on the single matrix diagonal \(\{(k+2h,k):k\ge0\}\), equivalently operators \(e_k\mapsto a_k e_{k+2h}\) with \((a_k)\in c_0\). Then
\[
\boxed{\displaystyle
\overline{\operatorname{span}}\{A_{h,j}:j\ge0\}^{\|\cdot\|}
=\mathbb C S^{2h}+\mathcal K_{2h}.}
\]
Every nontrivial finite linear combination of \(h+1\) or fewer distinct \(A_{h,j}\)'s is **not** finite rank. The \(h+2\) consecutive operators appearing in (a) therefore give a minimal-cardinality nonzero finite-rank linear relation.

## Assumptions and scope

The Hilbert norm is \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). All operators are complex-linear, \(h,j,r,k\) are integers in the ranges stated, and integration starts at \(0\). We use \(|e_m\rangle\langle e_n|\) for the rank-one map \(f\mapsto\langle f,e_n\rangle e_m\), with inner product linear in the first argument. The Schatten quasi-ideals are interpreted for every positive real exponent. The shift \(S^{2h}\) is the forward shift by \(2h\), not a multiplication operator on the entire-function realization. No positive-Sobolev-order or multivariable assertion is made.

## Proof

**1. Exact monomial action.** For \(k\ge j\), differentiation, multiplication, and repeated integration give
\[
A_{h,j}e_k=w_{h,j}(k)e_{k+2h},\qquad
w_{h,j}(k)=\frac{\prod_{a=1}^{h}(k-j+a)}{\sqrt{\prod_{a=1}^{2h}(k+a)}}.
\]
For \(k<j\), this weight is defined to be zero (the derivative vanishes). The denominator is independent of \(j\). For fixed \(h,j\), the positive weights eventually tend to \(1\); hence \(A_{h,j}\) is bounded, and \(A_{h,j}-S^{2h}\) is compact because its diagonal weights tend to zero. For all \(k\), different basis vectors have orthogonal output images.

**2. Polynomial finite differences and the rank-one boundary.** Put \(P_h(k,t)=\prod_{a=1}^{h}(k-t+a)\), a polynomial of degree \(h\) in each of \(k\) and \(t\). As a polynomial in \(t\), its \((h+1)\)-st forward difference vanishes identically. To apply this to operators one must also account for derivative truncation. If \(k<j\), every member of the finite difference annihilates \(e_k\). If \(k\ge j+1\), then for each term indexed by \(0\le s\le h+1\) with \(j+s>k\), the *untruncated* polynomial \(P_h(k,j+s)\) already vanishes: the integer \(j+s-k\) lies in \(\{1,\ldots,h\}\). Thus the whole operator difference vanishes on every such basis vector. At \(k=j\), the only truncated polynomial term not automatically zero is \(s=h+1\), with \(P_h(j,j+h+1)=(-1)^h h!\). Since the complete polynomial difference is zero, removing that term leaves \((-1)^{h+1}h!\). Division by \(\sqrt{\prod_{a=1}^{2h}(j+a)}=\sqrt{(j+2h)!/j!}\) proves (a), including its sign, exact support, and nonzero rank.

**3. Every lower difference has a sharp nonzero asymptotic.** For \(1\le r\le h\), take \(k\ge j+r\), so all differentiated terms are active. Regard \(P_h(k,t)\) as a polynomial in \(k\): its coefficient of \(k^{h-s}\) is a polynomial in \(t\) of degree \(s\), with leading term \((-1)^s\binom hs t^s\). The \(r\)-fold forward difference with respect to \(t\) annihilates coefficients for \(s<r\) and transforms the leading degree-\(r\) term into
\[
(-1)^r\binom hr r!=(-1)^r\frac{h!}{(h-r)!}.
\]
Therefore the numerator of the \(r\)-th operator difference is a polynomial in \(k\) of exact degree \(h-r\) and leading coefficient as displayed. Its denominator is \(k^h(1+O_h(k^{-1}))\); hence the resulting single-diagonal weights obey
\[
\Delta_j^r w_{h,j}(k)=(-1)^r\frac{h!}{(h-r)!}k^{-r}+O_{h,j,r}(k^{-r-1}).
\]
There are only finitely many exceptional low-index weights. The singular values are exactly the decreasing rearrangement of the absolute values of the diagonal weights, since the outputs of different basis vectors are orthogonal. Any sequence of the form \(Ck^{-r}(1+o(1))\), \(C>0\), has decreasing rearrangement asymptotic to \(CN^{-r}\), by sandwiching its distribution function between constant multiples of the pure power tail. This yields (b). The \(p\)-summability cutoff and critical logarithmic formula then follow by comparison with \(\sum n^{-rp}\) and \(\sum_{n\le N}1/n\).

**4. Closed-span determination.** Every generator belongs to \(\mathbb C S^{2h}+\mathcal K_{2h}\), which is norm closed: quotienting the single-band \(\ell^\infty\) model by its \(c_0\) subspace identifies the scalar constant-tail subspace as closed. Formula (a) puts the matrix unit \(|e_{j+2h}\rangle\langle e_j|\) in the linear span for every \(j\ge0\). Finite linear combinations of these matrix units are dense in \(\mathcal K_{2h}\). Since \(A_{h,0}-S^{2h}\in\mathcal K_{2h}\), the closure also contains \(S^{2h}\). Both containments in (c) follow.

**5. Minimum number of generators for a finite-rank combination.** Suppose \(t\le h+1\) distinct nonnegative indices \(j_1,\ldots,j_t\) and coefficients \(c_1,\ldots,c_t\) give a finite-rank sum. Its one-diagonal weight must vanish for all sufficiently large \(k\), because a finite-rank operator with mutually orthogonal columns cannot have infinitely many nonzero columns. Consequently the polynomial \(\sum_{v=1}^t c_v P_h(k,j_v)\) vanishes identically in \(k\). Comparing its coefficients from degree \(h\) downward, using the triangular leading-term structure of step 3, gives \(\sum_v c_v j_v^s=0\) for \(s=0,\ldots,h\). In particular, the first \(t\) moment equations form an invertible Vandermonde matrix because the indices are distinct. All \(c_v\) vanish. The nonzero \((h+2)\)-term relation in (a) shows the bound is sharp.

## Verification

The standalone standard-library program `CHECK.py` runs `python3 CHECK.py` and prints `JET_DIFFERENCE_VERIFY_OK 9008`. It verifies the exact finite-difference numerator and support formula over \(1\le h\le9\), \(0\le j\le9\), \(0\le k<70\); checks coefficient-degree annihilation and sharp leading coefficients for \(1\le r\le h\); and checks nondegenerate example Vandermonde determinants. These finite checks corroborate the exact algebra but are not substituted for the arbitrary-parameter proof above. All asymptotic and infinite-dimensional claims are deduced analytically.

## Relationship to prior work

Dong and Hu, arXiv:2611.01959v1, give the underlying critical integral-operator setup, compact-modulo-Laurent-Toeplitz representation, and general monomial coefficient formula (50). In the present equal-band family the common Calkin image \(S^{2h}\) is already implicit in their theory; it is **not** claimed as new. Formula (50) supplies a starting point, but the exact rank-one high finite difference, minimum-cardinality finite-rank identity, generated closed linear space and all-level sharp Schatten filtration of cross-order differences are additional claims not stated or classified there.

The accessible published result *Resonant cubic singular-value decay for critical Fock integral commutators* (2026) uses the identical operators and derives the exact weight formula; it concerns products' commutators, including a different quadratic/cubic resonance, not their **linear finite-difference** family. Mengestie (2017) treats Schatten properties of first-order Volterra operators, and Mengestie and Worku (2018) study differences of another fixed-order generalized Volterra family. Their frameworks do not directly identify the cross-order jet finite-difference identity proved here. Finite-difference polynomial calculus is standard; the novelty asserted is the operator-family structural realization and the sharp spectral classification, not the abstract finite-difference rule itself.

## Limitations

The classification is confined to the one-variable Gaussian Fock Hilbert space and a fixed positive integer monomial power \(h\), allowing variation of the derivative and matching integration orders. It concerns the norm-closed **linear space**, not an algebra under operator multiplication. The single-diagonal compact-operator space is much smaller than all compact operators on Fock space. Arbitrary polynomial-symbol families, higher-dimensional Fock spaces and different Hilbert/Sobolev normalizations are not covered. An unindexed equivalent identity or a broader symbolic-calculus result may predate this account; the available searches cannot prove absolute historical priority.

## References

1. J. Dong and S. Hu, *Carleson Measures and Integral Operators on Fock–Sobolev Spaces*, arXiv:2611.01959v1, posted 2026-11-01, especially Theorems 1.5–1.6 and formula (50), https://arxiv.org/html/2611.01959v1 .
2. *Resonant cubic singular-value decay for critical Fock integral commutators*, published-finding corpus published record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-resonant-cubic-singular-value-decay-for-critical-fock-integral-c--576b27bca5ec .
3. T. Mengestie, *Spectral properties of Volterra-type integral operators on Fock–Sobolev spaces*, arXiv:1702.08157v1, 2017, https://arxiv.org/html/1702.08157v1 .
4. T. Mengestie and M. Worku, *Topological structures of generalized Volterra-type integral operators*, arXiv:1802.08414v1, 2018, https://arxiv.org/abs/1802.08414 .
5. D. Alpay, P. Cerejeiras, U. Kähler and T. Kling, *Commutators on Fock spaces*, arXiv:2208.03394v1, 2022, https://arxiv.org/abs/2208.03394 .
