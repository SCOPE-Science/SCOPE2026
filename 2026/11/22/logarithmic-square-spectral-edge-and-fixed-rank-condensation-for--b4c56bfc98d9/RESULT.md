# Logarithmic-square spectral edge and fixed-rank condensation for damped monomial cross-products

## Finding
On the complex Hardy space \(H^2(\mathbb D)\), let \(C_\varphi f=f\circ\varphi\), let \(H^2_0=zH^2\), and fix coprime integers \(2\le p<q\). For \(0<\rho<1\), put
\[
T_\rho=\left.C_{\rho z^p}^{*}C_{\rho z^q}\right|_{H^2_0},\qquad B_\rho=T_\rho+T_\rho^*.
\]
The operator \(B_\rho\) is compact self-adjoint and trace class, with infinitely many positive eigenvalues \(\lambda_1(\rho)\ge\lambda_2(\rho)\ge\cdots>0\), repeated according to multiplicity. For **every fixed positive integer** \(J\),
\[
\boxed{\lim_{\rho\uparrow1}\left(\log\frac1{1-\rho}\right)^2(2-\lambda_J(\rho))=\pi^2(\log q)^2.}
\]
In particular, the largest eigenvalue and all fixed positive spectral ranks share the same sharp logarithmic-square boundary rate. Its coefficient depends on the **larger** monomial degree \(q\) but not the smaller coprime degree \(p\). The statement includes the exact rate of the numerical-radius disk, since \(w(T_\rho)=\lambda_1(B_\rho)/2\) on \(H^2_0\):
\[
\lim_{\rho\uparrow1}\left(\log\frac1{1-\rho}\right)^2(1-w(T_\rho))
=\frac{\pi^2(\log q)^2}{2}.
\]
For example, the sharp constant in the first display for \((p,q)=(2,3)\) is \(\pi^2(\log3)^2\).

## Assumptions and scope
We use the standard orthonormal Hardy monomials \(e_k(z)=z^k\), \(k\ge0\). Constants form a reducing eigenvalue-one summand of each composition-adjoint product and are removed by restricting to \(H^2_0\); otherwise the boundary comparison can be masked by that irrelevant constant mode. The integers \(p,q\) are fixed and relatively prime, with both at least two. The asymptotic concerns each fixed \(J\), not a rank growing with \(\rho\). The logarithm is natural. For every \(0<\rho<1\), all statements use the ordinary compact self-adjoint eigenvalue enumeration, not spectra of finite sections.

## Proof
**1. Exact weighted path model and compactness.** For \(k\ge1\), the composition operator satisfies \(C_{\rho z^q}e_k=\rho^k e_{qk}\), while \(C_{\rho z^p}^*e_{pk}=\rho^ke_k\). Coprimality gives
\[
T_\rho e_{pk}=\rho^{(p+q)k}e_{qk},\qquad T_\rho e_j=0\quad(p\nmid j).
\]
Every nonzero arrow links \(pk\) to \(qk\), with weight \(\exp(-(p+q)\varepsilon k)\), where \(\varepsilon=-\log\rho\). These arrows have distinct initial and terminal basis vectors, so \(T_\rho\) is a trace-class weighted partial permutation, since \(\sum_{k\ge1}e^{-(p+q)\varepsilon k}<\infty\). As \(q>p\), indices strictly increase along oriented arrows. Any component is a finite path (or isolated vertex): a path with \(L\) consecutive arrows requires its initial index to contain a factor \(p^L\), and no fixed positive integer can contain arbitrarily high powers of \(p\). The Hermitian operator \(B_\rho\) is therefore a direct sum of weighted path adjacency matrices, all of degree at most two. Their bipartite sign symmetry ensures that \(\|B_\rho\|\) is its largest positive eigenvalue and that \(w(T_\rho)=\|B_\rho\|/2\) (rotating vertex phases also shows the numerical range of \(T_\rho\) is a disk centered at zero).

**2. Upper spectral-edge estimate.** Write \(\ell=\log(1/\varepsilon)\), so \(\ell\to\infty\). Remove all edges of weight at most \(\delta=\ell^{-4}\). The removed adjacency has maximum row-sum norm at most \(2\delta\). Each retained edge has source parameter
\[
k<K_\varepsilon:=\frac{4\log\ell}{(p+q)\varepsilon}.
\]
Consider any retained connected string of \(L\) consecutive edges, ordered from smaller to larger vertex index. Its edge-source parameters are \(k_0,(q/p)k_0,\ldots,(q/p)^{L-1}k_0\), each an integer. Because \(p,q\) are coprime, \(p^{L-1}\mid k_0\); hence the last source parameter is at least \(q^{L-1}\). Thus \(L\le1+\lfloor\log K_\varepsilon/\log q\rfloor=:M_\varepsilon\), up to the harmless strict-inequality endpoint. Every retained block, which has at most \(M_\varepsilon+1\) vertices, is entrywise dominated by the unit-weight path. The latter's largest adjacency eigenvalue is \(2\cos(\pi/(M_\varepsilon+2))\). Monotonicity for nonnegative matrices and the perturbation bound give
\[
\lambda_J(\rho)\le\lambda_1(\rho)
\le2\cos\frac{\pi}{M_\varepsilon+2}+2\ell^{-4}.
\]
As \(M_\varepsilon=\ell/\log q+O(\log\ell)\), this proves
\[
\liminf_{\rho\uparrow1}\ell^2(2-\lambda_J(\rho))\ge\pi^2(\log q)^2.
\]
The same upper bound remains valid even though the truncation may split formerly connected paths.

**3. Lower estimate for every fixed rank.** Choose \(J\) distinct positive integers \(m_1,\ldots,m_J\), each coprime to \(pq\), and set
\[
L_\varepsilon=\left\lfloor\frac{\ell-5\log\ell}{\log q}\right\rfloor.
\]
For each \(m\) among these integers, the vertices
\[
 m p^{L_\varepsilon},\;m p^{L_\varepsilon-1}q,\;\ldots,\;m q^{L_\varepsilon}
\]
form a weighted path of \(L_\varepsilon\) consecutive edges in the original graph. These \(J\) paths are in distinct components: the coprime cofactor \(m\) is invariant along an arrow and cannot change under exchanges of factors \(p,q\). Every edge-source parameter on the \(m\)-path is at most \(m q^{L_\varepsilon-1}\). Consequently, if \(m_*\) is the largest chosen cofactor, every path weight is at least
\[
\exp(-(p+q)m_*\varepsilon q^{L_\varepsilon-1})=1-O_J(\ell^{-5}),
\]
where the constant may depend on \(p,q,J\). The normalized positive sine vector for the unweighted \((L_\varepsilon+1)\)-vertex path has Rayleigh quotient at least
\[
2(1-O_J(\ell^{-5}))\cos\frac{\pi}{L_\varepsilon+2}.
\]
The \(J\) sine vectors live in mutually orthogonal reducing path components, so the min-max principle gives
\[
\lambda_J(\rho)\ge 2(1-O_J(\ell^{-5}))\cos\frac{\pi}{L_\varepsilon+2}.
\]
Since \(L_\varepsilon=\ell/\log q+O(\log\ell)\), this yields
\[
\limsup_{\rho\uparrow1}\ell^2(2-\lambda_J(\rho))\le\pi^2(\log q)^2.
\]
Together with Step 2, this proves the limit for every fixed rank. Finally \(\log(1/\varepsilon)=\log(1/(1-\rho))+o(1)\), so the stated form follows. Infinitely many coprime cofactors \(m\) give infinitely many positive modes at each fixed \(\rho\), as claimed.

## Verification
Run `python3 checker.py` using Python 3 standard library. Its executable finite test checks weighted directed edges, component dimensions, trace-square diagonal identities and exact unit-path sine eigenvectors for several coprime pairs; it also checks the displayed comparison scales at selected large logarithmic parameters. The expected terminal output is `MONOMIAL_LOG_EDGE_DIAGNOSTIC_OK 7818`. This is a diagnostic, not an infinite proof; the full asymptotic and every fixed-rank assertion are established in the preceding analytic argument.

## Relationship to prior work
Leng and Zhao (2026) investigate Schatten membership for products of composition operators and adjoints; the present compact products are a natural special family, but their membership results do not furnish this fixed-rank spectral-edge law. Clifford, Dabkowski and Wiggins (2021), especially their weighted-chain constructions and numerical-range analysis, study the **same damped monomial operator family**. The weighted path model, numerical-range disk and its qualitative approach to the unit-disk limit are **not** claimed here as original. Their available theorems give different regimes (including small damping), not the sharp logarithmic-square coefficient nor simultaneous fixed-eigenvalue-rank condensation. Previously published work on degree-truncated **undamped** monomial cross-composition sections proves a closely related \(\pi^2(\log q)^2/2\) numerical-radius edge constant. The present theorem quantifies a genuine compact radial boundary limit rather than polynomial cutoffs, and strengthens the bound to every fixed spectral rank. A published analysis of damped cross-product self-commutator Schatten invariants concerns \(T^*T-TT^*\), not \(T+T^*\). We claim no new weighted-path decomposition or novelty for the classical path cosine formula.

## Limitations
The result is restricted to fixed coprime positive integer degrees \(2\le p<q\), real common damping \(0<\rho<1\), and the constant-free Hardy subspace. It does not establish uniformity when the eigenvalue rank \(J\) grows with \(\rho\), a second-order correction, or full rescaled eigenvalue distributions. The rate is logarithmically slow, and finite numerical sections can converge poorly. The quantitative conclusion is closely related to known undamped finite-cutoff edge results; a more general earlier theorem may implicitly imply it. This is a mathematical proof accompanied by diagnostic tests, not independent certification or a claim of exhaustive historical priority.

## References
1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (first public 2026-10-11), https://arxiv.org/abs/2610.15472.
2. J. Clifford, M. Dabkowski and A. Wiggins, *The Numerical Range of \(C_\psi^*C_\varphi\) and \(C_\varphi C_\psi^*\)*, *Concrete Operators* **8** (2021), 13–23, https://doi.org/10.1515/conop-2020-0108.
3. *Arithmetic universality and pure-point spectral laws for monomial cross-composition sections*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-arithmetic-universality-and-pure-point-spectral-laws-for-monomia--ed43628bf3a8.
4. *Two-ideal spectral rigidity for damped monomial composition–adjoint products*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-ideal-spectral-rigidity-for-damped-monomial-composition-adjo--ba7c08a56403.
5. *Arithmetic spectral trichotomy for monomial composition–adjoint products*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-arithmetic-spectral-trichotomy-for-monomial-composition-adjoint--e66a895c9359.
