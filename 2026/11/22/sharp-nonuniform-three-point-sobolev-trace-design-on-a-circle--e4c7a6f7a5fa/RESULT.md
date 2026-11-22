# Sharp nonuniform three-point Sobolev trace design on a circle

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\). For real, periodic, mean-zero \(f\in H^1(\mathbb T)\), and any three distinct sites \(X=\{x_1,x_2,x_3\}\subset\mathbb T\), define
\[
C(X)^2=\sup_{\int_0^1|f'|^2>0}\frac{\sum_{j=1}^3|f(x_j)|^2}{\int_0^1|f'(x)|^2\,dx}.
\]
Then the exact global optimum is
\[
\boxed{\min_{|X|=3}C(X)^2=\frac{11+\sqrt{21}}{150}.}
\]
Every minimizing configuration, and no other, is a rotation or reflection of
\[
X_*=\{0,t_*,2t_*\},\qquad t_*=\frac{9-\sqrt{21}}{30}.
\]
Equivalently, its three positive cyclic gaps are the permutations of \((t_*,t_*,1-2t_*)\). By contrast, equally spaced sites have \(C(X)^2=1/9\), strictly larger than the optimum. At the optimal configuration the top singular value has multiplicity two, and the corresponding sharp trace inequality has a two-dimensional linear space of norming functions.

## Assumptions and scope
The circle has total arclength one. The space is the real Hilbert space \(H=\{f\in H^1(\mathbb T):\int_{\mathbb T}f=0\}\), equipped with the derivative-energy inner product \(\langle f,g\rangle_H=\int_{\mathbb T}f'g'\). Every member has a continuous periodic representative, so all evaluations are well-defined. The sampled output carries the unweighted Euclidean \(\ell^2\) norm. Sites must be distinct, without any separation or uniformity constraint. No reconstruction algorithm or observation-noise model enters the theorem.

## Proof
**1. Reproducing kernel and Gram reduction.** Let \(B_2(u)=u^2-u+1/6\) for \(0\le u\le1\), extended periodically, and set
\[
G(u)=\frac12B_2(\{u\})=\frac12\left(\{u\}^2-\{u\}+\frac16\right),\qquad d=G(0)=\frac1{12}.
\]
The distributional identity \(G''=1-\delta_0\) and the zero-mean hypothesis imply
\(\int_0^1 f'(x)G'(x-y)\,dx=f(y)\). Therefore the evaluation map \(E_Xf=(f(x_1),f(x_2),f(x_3))\) has
\[
E_XE_X^*=K_X=(G(x_i-x_j))_{1\le i,j\le3},\qquad C(X)^2=\lambda_{\max}(K_X).
\]
Write the three positive consecutive circular gaps as \(a,b,c\), with \(a+b+c=1\). Since \(G(1-u)=G(u)\), the three off-diagonal entries, up to permutation, are \(G(a),G(b),G(c)\). A principal two-by-two submatrix with off-diagonal entry \(r\) has top eigenvalue \(d+|r|\). Thus
\[
C(X)^2\ge d+\max\{|G(a)|,|G(b)|,|G(c)|\}. \tag{1}
\]

**2. A sharp three-gap obstruction.** Define
\[
t=\frac{9-\sqrt{21}}{30},\qquad s=G(t)=\frac{2\sqrt{21}-3}{300}.
\]
Direct expansion of \(5t^2-3t+1/3=0\) gives \(G(2t)=-s\). Moreover \(0<t<1/4\), \(6t<1\), and \(0<s<1/24\). For any \(0\le r<s\), define the two roots in \((0,1/2)\):
\[
\alpha_r=\frac12-\sqrt{\frac1{12}+2r},\qquad
\beta_r=\frac12-\sqrt{\frac1{12}-2r}.
\]
The monotonic decrease of \(G\) on \([0,1/2]\) and symmetry around \(1/2\) imply
\[
|G(u)|\le r\quad\Longleftrightarrow\quad
u\in[\alpha_r,\beta_r]\cup[1-\beta_r,1-\alpha_r]
\quad(0<u<1). \tag{2}
\]
Since \(G(t)=s\) and \(G(2t)=-s\), for \(r<s\) one has \(\alpha_r>t\) and \(\beta_r<2t\). If all three positive gaps obeyed (2), at most one could lie in the upper interval (each such gap exceeds \(1/2\)). If all three lay in the lower interval, their sum would be at most \(3\beta_r<6t<1\). If exactly one lay in the upper interval, their sum would be at least \((1-\beta_r)+2\alpha_r>1-2t+2t=1\). Both contradict \(a+b+c=1\). Consequently
\[
\max\{|G(a)|,|G(b)|,|G(c)|\}\ge s. \tag{3}
\]
At equality in (3), the same argument at \(r=s\) forces exactly one gap in the upper interval and two in the lower interval, with their sum attaining its minimum. Hence the gaps must be \((t,t,1-2t)\) up to permutation. This proves both the universal lower bound and the uniqueness of its equality geometry.

**3. Exact attainment.** For sites \((0,t,2t)\) in that cyclic order, the Gram matrix is
\[
K_*=\begin{pmatrix}d&s&-s\\s&d&s\\-s&s&d\end{pmatrix}.
\]
Its eigenvalues are \(d+s\) (twice) and \(d-2s\) (once), so \(\lambda_{\max}(K_*)=d+s=(11+\sqrt{21})/150\). This attains the lower bound (1)--(3), and the equality geometry from step 2 proves that no other configuration minimizes the norm. The top eigenspace is \(\{v\in\mathbb R^3:v_1-v_2+v_3=0\}\); the corresponding nonzero norming functions are precisely scalar multiples of functions \(\sum_j v_jG(\cdot-x_j)\) for nonzero vectors in this plane. Translation and reflection preserve the result.

**4. Uniform comparison.** For equal gaps \(1/3\), all off-diagonal Gram entries equal \(G(1/3)=-1/36\). The eigenvalues are \(1/36\) and \(1/9\) (twice), giving \(C(X)^2=1/9>(11+\sqrt{21})/150\).

## Verification
The analytic argument covers every real mean-zero periodic \(H^1\) input and every triple of distinct sampling sites; it does not extrapolate from a mesh search. Run `python checker.py` with Python 3, SymPy, and NumPy. The script checks the algebraic identities and Gram eigenstructure symbolically, the strict endpoint inequalities, all \(551300\) positive rational three-gap configurations with grid denominators \(3\) through \(150\) against the necessary pair-correlation bound, and \(19600\) smaller-grid configurations by a symmetric-matrix eigenvalue computation. A separate quadrature of the representer derivative inner products reproduces the optimal Gram matrix to numerical precision. These finite computations are corroboration, not a proof of the global inequality.

## Relationship to prior work
The periodic Bernoulli reproducing kernel is classical, and periodic Sobolev interpolation with equally spaced nodes is treated by Shadimetov, Hayotov and Mamatova (2010) [1]. Wang and Zhang (2012) [2] study **optimal reconstruction** from RKHS samples, with a different loss involving the residual kernel after interpolation; their general Karhunen–Loève methods do not by themselves give the minimum **raw, simultaneous evaluation norm** proved here. Related point-mass placement results treat a mean constraint modified by atoms and an \(H^1\)-to-supremum embedding rather than the present fixed arclength mean and three-output trace norm [3]. The exact three-gap coherence obstruction and its fully classified nonuniform equality case are the claim here. These comparisons do not prove absence of an unindexed equivalent in earlier optimal-design or kernel-matrix literature.

## Limitations
The result is for exactly three unweighted real sample outputs and the homogeneous derivative norm with an arclength-zero-mean constraint. It does not establish the minimizing design for four or more samples, the optimum under heteroscedastic noise, minimum-eigenvalue conditioning, or the optimal recovery error from samples. A historically unindexed equivalent in kernel-matrix spectral optimization remains possible; the known nearby interpolation and reconstruction formulations use different objectives.

## References
1. Kh. M. Shadimetov, A. R. Hayotov and N. H. Mamatova, *Optimal interpolation formulas in the periodic function space of S. L. Sobolev*, arXiv:1012.1953v1 (first public version 2010-12-09), https://arxiv.org/abs/1012.1953 .
2. Rui Wang and Haizhang Zhang, *Optimal Sampling Points in Reproducing Kernel Hilbert Spaces*, arXiv:1207.5871v1 (2012-07-25), https://arxiv.org/abs/1207.5871 .
3. *Sharp cubic-gap stability for optimally placed Sobolev mean constraints on a circle* (published 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-cubic-gap-stability-for-optimally-placed-sobolev-mean-cons--ed3ad9071b26 .
