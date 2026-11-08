# Exact arithmetic saturation of quartic-phase masked Fourier tomography

## Finding
Fix a prime \(p\ge5\) and \(1\le r\le p\). Write \(\zeta=e^{2\pi i/p}\) and define the normalized vectors
\[
 v_{s,k}(j)=p^{-1/2}\zeta^{s j^4+k j},\qquad 0\le s<r,\quad j,k\in\mathbb F_p.
\]
For the real vector space \(\operatorname{Herm}_p\) of Hermitian matrices, let
\[
 \mathcal L_{p,r}(H)=\bigl(v_{s,k}^*H v_{s,k}\bigr)_{0\le s<r,\ k\in\mathbb F_p}.
\]
Let \(\chi_p\) be the quadratic character on \(\mathbb F_p\), put \(\epsilon=\chi_p(-3)\in\{-1,1\}\), and set \(m_p=(2p+\epsilon)/3\). The exact real rank and nullity are
\[
 \boxed{\operatorname{rank}_{\mathbb R}\mathcal L_{p,r}=1+(p-1)\min\{r,m_p\}},
 \qquad
 \boxed{\dim_{\mathbb R}\ker\mathcal L_{p,r}=p^2-1-(p-1)\min\{r,m_p\}}.
\]
In particular, the sharp saturation index is \(m_p\): a new mask increases the real matrix-recovery rank by exactly \(p-1\) before saturation and increases it by zero afterward. The maximum never reaches \(p^2\), even when all \(p\) slopes are used.

For \(F(u)=4u^3+u\) on \(\mathbb F_p\), define \(n_a=|\{t\in\mathbb F_p:|F^{-1}(t)|=a\}|\). Then
\[
 \boxed{n_1=\frac{p-1}2,\quad n_2=1+\epsilon,\quad n_3=\frac{p-3-4\epsilon}6}.
\]
Every nonempty fiber has cardinality one, two, or three. The complete kernel is described below in terms of these fibers, not just its dimension.

## Assumptions and scope
All indices and divisions involving \(2,3,4,d\) are in \(\mathbb F_p\). The slopes are exactly the consecutive residues \(0,1,\ldots,r-1\), interpreted as distinct elements of \(\mathbb F_p\); the result does not assert the same rank for an arbitrary nonconsecutive selection. The entries of \(H\) are complex but \(H=H^*\); the output is real, so all ranks and dimensions above are real. There is no positivity or rank-one restriction on \(H\). The Fourier measurement vectors are normalized to unit Euclidean norm.

For every \(d\in\mathbb F_p^\times\), define the oriented cyclic diagonal and its cubic-fiber sums:
\[
 h_d(j)=H_{j,j-d},\quad
 a_{d,t}=\sum_{j:\ F(j/d-1/2)=t} h_d(j),
 \qquad t\in F(\mathbb F_p).
\]
The exact kernel criterion at every \(r\) is
\[
 \operatorname{tr}H=0,\qquad
 \sum_{t\in F(\mathbb F_p)} \zeta^{-s d^4t}a_{d,t}=0
 \quad \text{for every } d\ne0,\;s=0,\ldots,r-1.
\]
For \(r\ge m_p\), the last constraints are equivalent to \(a_{d,t}=0\) for every \(d\ne0\) and every attained value \(t\). For \(r<m_p\), they are exactly \(r\) independent complex constraints on the \(m_p\) fiber sums of each oriented diagonal.

## Proof
**1. Fourier separation into cyclic diagonals.** Expanding the intensity gives
\[
 v_{s,k}^*Hv_{s,k}=\frac1p\sum_{j,\ell\in\mathbb F_p}
 H_{j,\ell}\zeta^{s(\ell^4-j^4)+k(\ell-j)}.
\]
Taking the discrete Fourier transform in \(k\) (an invertible real transformation after pairing conjugate frequencies) isolates each diagonal offset \(d=j-\ell\). Its nonzero component, up to a nonzero common normalization, equals
\[
 T_{d,s}(H)=\sum_{j\in\mathbb F_p}H_{j,j-d}
 \zeta^{-s[j^4-(j-d)^4]}.
\]
When \(d=0\), all observations reduce to \(\operatorname{tr}H\); the entire traceless diagonal subspace is invisible. For \(d\ne0\), put \(u=j/d-1/2\). Direct binomial expansion yields the exact identity
\[
 j^4-(j-d)^4=d^4\left[\left(u+\tfrac12\right)^4-\left(u-\tfrac12\right)^4\right]
 =d^4(4u^3+u)=d^4F(u).
\]
Thus \(T_{d,s}(H)=\sum_t (\zeta^{-d^4t})^s a_{d,t}\), where the sum runs over the image of \(F\).

**2. Exact cubic image size and fiber profile.** Distinct \(x,y\) have \(F(x)=F(y)\) precisely when
\[
 4(x^2+xy+y^2)+1=0.
\]
For each fixed \(x\), the quadratic equation in \(y\) has discriminant \(-3x^2-1\). The standard elementary character identity \(\sum_{x\in\mathbb F_p}\chi_p(ax^2+b)=-\chi_p(a)\) for \(ab\ne0\) gives exactly \(p-\epsilon\) ordered solutions including those with \(x=y\). Such diagonal solutions obey \(12x^2+1=0\), so their number is \(1+\chi_p(-1/12)=1+\epsilon\). The number of ordered off-diagonal pairs is therefore \(p-1-2\epsilon\).

Any image value with a repeated root of \(F(u)-t\) has a root of \(F'(u)=12u^2+1\). There are \(1+\epsilon\) critical points. If two exist, they are \(\pm a\), and \(F(a)=2a/3\ne0\) while \(F(-a)=-2a/3\); hence they give distinct image values, each with exactly two distinct preimages. Thus \(n_2=1+\epsilon\). Every other nonempty fiber has size one or three. Counting ordered unequal pairs and then input points yields
\[
 2n_2+6n_3=p-1-2\epsilon,\qquad
 n_1+2n_2+3n_3=p.
\]
Solving gives the three boxed formulas, and in particular
\[
 |F(\mathbb F_p)|=n_1+n_2+n_3=(2p+\epsilon)/3=m_p.
\]
This arithmetic sublemma may be considered independently classical; novelty is not asserted for the character identity or generic cubic-value-set methods.

**3. Mask-wise Vandermonde rank.** For fixed \(d\ne0\), the columns of the matrix taking the \(m_p\) fiber sums \(a_{d,t}\) to \(T_{d,s}\) are \((1,z_t,\ldots,z_t^{r-1})^\top\), with distinct nodes \(z_t=\zeta^{-d^4t}\). Every leading square Vandermonde minor is nonzero. Therefore each nonzero cyclic diagonal has complex rank \(\min\{r,m_p\}\). Hermiticity pairs opposite offsets \(d\) and \(-d\); within each pair one may specify the \(p\) complex diagonal entries freely and their conjugates are forced, so its real contribution is twice this complex rank. There are \((p-1)/2\) pairs. Adding the one trace dimension proves the real-rank formula, then the rank-nullity theorem gives the nullity.

**4. Constructive kernel description.** For each nonzero offset, every difference supported within a single \(F\)-fiber has zero fiber sum and belongs to the kernel for all slopes. For \(r<m_p\), there are exactly \(m_p-r\) more independent relations among fiber sums. To exhibit them, define \(Q_d(z)=\prod_{t\in F(\mathbb F_p)}(z-z_t)\). For every polynomial \(P\) of degree less than \(m_p-r\), set
\[
 a_{d,t}=\frac{P(z_t)}{Q_d'(z_t)}.
\]
The Lagrange interpolation identity \(\sum_t z_t^j/Q_d'(z_t)=0\) for \(0\le j\le m_p-2\) implies \(\sum_t z_t^s a_{d,t}=0\) whenever \(0\le s<r\). These form all the missing \(m_p-r\) complex dimensions by polynomial evaluation injectivity; one may realize each prescribed fiber sum at any chosen representative and enforce Hermitian symmetry on the opposite diagonal. Traceless diagonal matrices and one representative from each opposite-offset pair complete the full real kernel.

## Verification
`CHECK.py` independently implements prime-field cubic fiber counting, constructs the complete real measurement matrix from an orthogonal Hermitian basis for small primes, tests the predicted rank at and beyond saturation, and verifies explicit fiber-based invisible matrices and Lagrange-kernel relations. Run with `python CHECK.py` after installing the package in `requirements.txt`. The general proof is algebraic; floating-point experiments are corroboration only.

## Relationship to prior work
Coded diffraction and lifted phase-retrieval methods, including Candès–Li–Soltanolkotabi [1], Huang–Li [2] and Huang–Wang [3], motivate an analysis of deterministic phase-mask families. Their main quantitative guarantees concern random masks and nonlinear signal reconstruction, not exact Hermitian-operator ranks for consecutive quartic phases. Li–Zhang [4] analyze finite-field polynomial value sets, placing the cubic image-counting mechanism in its established algebraic context, but do not give these quartic-mask tomography ranks. A quadratic-mask family, a cubic-plus-quadratic-offset family, and quartic-chirp Gabor tomography address different phase laws or measurement orbits; their respective statements do not directly cover the present result. The discrete Fourier decomposition and Vandermonde principle are standard; the combined quartic-phase rank, exact saturation index and explicit kernel are the specific result presented here.

## Limitations
The claim is restricted to prime cyclic lengths at least five, exact phase masks with consecutive slopes, and full noiseless Fourier-intensity profiles. It does not assert nonlinear phase-retrieval failure, rank-one ambiguities, quantitative noise robustness, generic rank for arbitrary slope sets, or extensions to prime powers/composite lengths. Publication priority is not independently certified; equivalences in older polynomial-phase tomography and cubic-value-set literature remain possible.

## References
1. E. J. Candès, X. Li, M. Soltanolkotabi, *Phase Retrieval from Coded Diffraction Patterns*, arXiv:1310.3240, first public 2013-10-11. https://arxiv.org/abs/1310.3240
2. G. Huang and S. Li, *PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate*, arXiv:2608.02450, first public 2026-08-03. https://arxiv.org/abs/2608.02450
3. M. Huang and T. Wang, *The Gauss–Newton Method for Phase Retrieval from Coded Diffraction Patterns*, arXiv:2610.18021, first public 2026-10-13. https://arxiv.org/abs/2610.18021
4. J. Li and Z. Zhang, *Improving bounds for value sets of polynomials over finite fields*, arXiv:2601.03548, first public 2026-01-07. https://arxiv.org/abs/2601.03548
