# Arf-parity shattering of binary quadratic refinements: an exact Lagrangian defect

## Finding
Fix an integer \(m\ge1\). In the binary symplectic vector space \(V=\mathbb F_2^{2m}\), use coordinates \(x=(u,v)\) with \(u,v\in\mathbb F_2^m\), the quadratic form \(Q_0(u,v)=\sum_{i=1}^m u_i v_i\), and its nondegenerate alternating polar form \(B(x,y)=Q_0(x+y)+Q_0(x)+Q_0(y)\). For \(a\in V\), define the quadratic refinement \(Q_a(x)=Q_0(x)+B(a,x)\). Its Arf invariant is \(\operatorname{Arf}(Q_a)=Q_0(a)\). For \(\epsilon\in\{0,1\}\), consider the concept class of zero sets
\[
\mathcal C_{m,\epsilon}=\bigl\{\{x\in V\setminus\{0\}:Q_a(x)=0\}:a\in V,\ Q_0(a)=\epsilon\bigr\}.
\]

**Complete support characterization.** A finite support \(S\subseteq V\setminus\{0\}\) is VC-shattered by \(\mathcal C_{m,\epsilon}\) if and only if \(S\) is linearly independent and at least one of the following holds:

1. \(B\) is nonzero on \(K=\operatorname{span}(S)^{\perp_B}\), equivalently \(K\) is not totally isotropic;
2. \(\epsilon=0\) and \(K\) is Lagrangian (a totally isotropic subspace of dimension \(m\)).

For \(0\le k\le2m\), let \(G_{n,k}=\genfrac{[}{]}{0pt}{}{n}{k}_2\) denote the binary Gaussian coefficient and let \(A_{m,r}\) be the number of totally isotropic \(r\)-subspaces of \(V\), defined by
\[
A_{m,r}=\begin{cases}
\displaystyle\prod_{i=0}^{r-1}\frac{2^{2m-i}-2^i}{2^r-2^i},&0\le r\le m,\\
0,&r>m.
\end{cases}
\qquad
b_k=\frac1{k!}\prod_{i=0}^{k-1}(2^k-2^i).
\]
Empty products are one. Then the **entire shattered-support polynomial** is
\[
\boxed{\Phi_{m,\epsilon}(z)=\sum_{k=0}^{2m}b_k\left(G_{2m,k}-A_{m,2m-k}+\mathbf1_{\{\epsilon=0,\ k=m\}}A_{m,m}\right)z^k.}
\]

In particular, the two parity classes differ in **only one coefficient**:
\[
\boxed{\Phi_{m,0}(z)-\Phi_{m,1}(z)=\frac{\lvert\mathrm{GL}(m,2)\rvert}{m!}\prod_{i=1}^m(2^i+1)\,z^m.}
\]
For every \(m\ge2\), both classes have VC dimension exactly \(2m-2\). At the exceptional boundary \(m=1\), the even class has VC dimension one and the odd class zero.

For example, at \(m=3\), the even/odd polynomials respectively are
\[
\begin{aligned}
\Phi_{3,0}(z)&=1+63z+1953z^2+39060z^3+282240z^4,\\
\Phi_{3,1}(z)&=1+63z+1953z^2+35280z^3+282240z^4.
\end{aligned}
\]

## Assumptions and scope
All vector spaces, vector-space dimensions, quadratic forms, alternating forms, and Arf invariants are over \(\mathbb F_2\). The concepts are exactly the zero loci of all nonsingular quadratic refinements of **one fixed polar form**, filtered by Arf invariant; they are not all quadratic forms, nor all affine quadrics. The query domain excludes zero, since every quadratic form vanishes there. A support is shattered when all \(2^{\lvert S\rvert}\) Boolean membership traces occur. The coefficient of \(z^k\) counts **unordered distinct** query supports, not ordered tuples, concepts, or affine subspaces.

## Proof
**1. Arf parameterization.** Every quadratic refinement of \(B\) differs from \(Q_0\) by a linear functional. Nondegeneracy of \(B\) identifies these functionals uniquely as \(B(a,-)\), giving all \(Q_a\). The Gauss sum of \(Q_0\) is \(2^m\), one factor of two from each coordinate pair. The change of variable \(x\mapsto x+a\) gives
\[
\sum_{x\in V}(-1)^{Q_a(x)}=(-1)^{Q_0(a)}2^m,
\]
so the Arf invariant of \(Q_a\) is \(Q_0(a)\). Thus fixing Arf parity is exactly the constraint \(Q_0(a)=\epsilon\).

**2. Linear independence is necessary.** On a support \(S=\{s_1,\ldots,s_k\}\), the vector of query bits for \(Q_a\) is the fixed vector \((Q_0(s_i))_i\) plus the linear evaluation map \(a\mapsto(B(a,s_i))_i\). If the \(s_i\) are dependent, this image is a proper affine subspace of \(\mathbb F_2^k\); therefore not all \(2^k\) traces occur, regardless of parity.

**3. Every trace becomes one coset.** Suppose \(S\) is independent and put \(W=\operatorname{span}(S)\). Nondegeneracy makes the evaluation map of Step 2 surjective, with kernel \(K=W^{\perp_B}\). Hence each prescribed trace corresponds to exactly one affine coset \(a+K\). It is realized by the parity-restricted concept class if and only if \(Q_0\) takes the specified value \(\epsilon\) on that coset. We must classify precisely when every coset intersects the parity level set.

**4. Nonisotropic kernels.** If \(B|_{K\times K}\ne0\), no restriction of \(Q_0\) to an affine coset of \(K\) can be constant: the polar form of such a constant quadratic function would vanish, contrary to the assumption. Because the codomain is binary, each coset contains both values zero and one. Thus both parity classes shatter \(S\).

**5. Totally isotropic kernels and the sharp defect.** Suppose \(K\) is totally isotropic and let \(r=\dim K\le m\). The map \(k\mapsto Q_0(k)\) is linear on \(K\), so choose \(a_0\in V\) satisfying \(B(a_0,k)=Q_0(k)\) for all \(k\in K\). Then \(Q_{a_0}|_K=0\). For \(w\in V\), the function \(Q_0\) is constant on \(a_0+w+K\) precisely when \(w\in K^{\perp_B}\), and its constant value is \(Q_0(a_0+w)\).

The form \(Q_{a_0}\) descends to a nondegenerate quadratic form on the quotient \(K^{\perp_B}/K\) of dimension \(2(m-r)\). If \(r<m\), this quotient has positive even dimension and its quadratic form represents **both** binary values: zero occurs at the zero class, and value one occurs because a nondegenerate quadratic form cannot be identically zero. Therefore there is a constant-even coset and a constant-odd coset. The constant-even coset excludes the odd parity class from shattering, while the constant-odd coset excludes the even class. Neither shatters.

If \(r=m\), then \(K=K^{\perp_B}\), so the only constant coset is \(a_0+K\). Because \(Q_{a_0}\) vanishes identically on the Lagrangian \(K\), its Arf invariant is zero: choose a symplectic basis starting with a basis of \(K\), and in these coordinates the Arf invariant, the sum of paired basis values, is zero. Step 1 gives \(Q_0(a_0)=0\). Thus this unique constant coset contains only even parameters, while every other coset has both parities. The even class shatters, whereas the odd class does not. These alternatives exhaust all kernels and prove the characterization.

**6. Exact support counts.** Each independent \(k\)-element support spans a unique \(k\)-subspace \(W\). Such a subspace has \(\lvert\mathrm{GL}(k,2)\rvert/k!=b_k\) unordered bases. The symplectic orthogonal-complement operation is a bijection from \(k\)-subspaces \(W\) to \((2m-k)\)-subspaces \(K\), giving \(G_{2m,k}\) possibilities. Of these, \(A_{m,2m-k}\) are totally isotropic, and the even class retains the Lagrangians when \(k=m\).

To count isotropic \(r\)-subspaces, construct an ordered independent isotropic basis. After \(i\) vectors have been chosen, their isotropic span has dimension \(i\). Its polar orthogonal has \(2^{2m-i}\) vectors, of which exactly \(2^i\) lie in the current span. Hence there are \(\prod_{i=0}^{r-1}(2^{2m-i}-2^i)\) ordered isotropic bases, and dividing by \(\lvert\mathrm{GL}(r,2)\rvert\) yields \(A_{m,r}\). At \(r=m\), this simplifies to \(A_{m,m}=\prod_{i=1}^m(2^i+1)\). This proves the polynomial and its single-degree parity difference.

**7. Dimension bounds.** The orthogonal complement of an independent \((2m-1)\)-support is one-dimensional and hence totally isotropic; it is not Lagrangian for \(m\ge2\). An independent \(2m\)-support has zero-dimensional kernel and similarly fails the criterion. For \(m\ge2\), take a nondegenerate binary two-plane \(K\) inside \(V\), and let \(S\) be any basis of \(K^{\perp_B}\), of dimension \(2m-2\). This \(S\) is shattered in both classes. The dimension therefore equals \(2m-2\). The boundary \(m=1\) follows from the criterion: all independent singletons qualify for the even class but none for the odd class.

## Verification
The standalone scripts `verify_quadratic_shattering.py` and `verify_dim6.cpp` construct the classes directly, evaluate the Boolean traces, and compare them to the structural theorem and exact enumerator. Run `python3 verify_quadratic_shattering.py` using the Python 3 standard library; compile `verify_dim6.cpp` with a C++17 compiler using `c++ -O2 -std=c++17 verify_dim6.cpp -o verify_dim6`, then execute `./verify_dim6`. Python exhaustively tests all supports of sizes zero through three in the four- and six-dimensional cases, plus higher-support samples in dimension six. The independently written C++ program exhaustively checks **all** six-dimensional supports of sizes zero through four, for both parity classes, including all 282,240 shattered four-supports. Both terminate with explicit PASS markers; their finite checks corroborate, but do not replace, the all-dimensional proof.

## Relationship to prior work
Schmidt (2018) develops association schemes, ranks, and code bounds for quadratic forms, including even characteristic and Reed–Muller connections. Its full text studies ranks, spectra, inner distributions and codes, not the present Arf-restricted Boolean trace system. Fitzpatrick–Iosevich–McDonald–Wyman (2021) analyze VC dimension of finite-field norm-sphere incidence, not parity-filtered fixed-polar quadratic refinements over the binary field. McDonald–Sahay–Wyman (2022) examine additive translates of multiplicative quadratic residues, not quadratic refinements of a symplectic polar form.

Related published classifications of affine-flat shattering concern flat indicators rather than Arf-level families; published studies of binary quadric Walsh sampling concern linear algebraic interpolation and Gram spectra, not combinatorial shattering on all query supports. A first-order classification of orthogonal polar point graphs concerns graph-theoretic logical equivalence, not the Boolean incidence concept system here. None of those inspected statements implies the Lagrangian exception or the coefficientwise parity difference. Classical Arf and symplectic-subspace counting facts are used as background, not claimed as new. Priority among older or unindexed incidence and theta-characteristic literature is not certified.

## Limitations
The result covers binary nonsingular quadratic refinements of a **fixed** symplectic polar form on the full nonzero-vector query domain. It does not address arbitrary quadratic forms with varying polar forms, other finite fields, restricted query subsets, Littlestone dimension or asymptotic sample complexity. Its infinite-family proof is mathematical, not the result of extrapolating finite computations. The novelty assessment is limited to the inspected literature and repository records; independent audit has not yet occurred.

## References
1. K.-U. Schmidt, *Quadratic and symmetric bilinear forms over finite fields and their association schemes*, first public arXiv:1803.04274v1 on 2018-03-12, https://arxiv.org/html/1803.04274v1 .
2. D. Fitzpatrick, A. Iosevich, B. McDonald and E. Wyman, *The VC-dimension and point configurations in finite-field planes*, first public arXiv:2108.13231v1 on 2021-08-30, https://arxiv.org/html/2108.13231v1 .
3. B. McDonald, A. Sahay and E. Wyman, *The VC-dimension of quadratic residues in finite fields*, first public arXiv:2210.03789v1 on 2022-10-07; revised version inspected, https://arxiv.org/html/2210.03789v2 .
4. *Complete quadratic Walsh sampling spectrum on a split binary quadric*, 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-quadratic-walsh-sampling-spectrum-on-a-split-binary-qua--477aab4e3535 .
5. *Fixed-rank affine-flat shattering complexes over finite fields*, 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-rank-affine-flat-shattering-complexes-over-finite-fields--6e9f3ce9d85a .
6. *Four rank-four theories of binary orthogonal polar point graphs*, 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-rank-four-theories-of-binary-orthogonal-polar-point-graphs--aadf485bbc13 .
