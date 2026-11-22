# Mixed Volterra-power commutators: exact rank and factorial spectral product

## Finding
Let \(V\) be the indefinite integration operator on complex \(L^2(0,1)\), \((Vf)(x)=\int_0^x f(t)\,dt\). For every pair of positive integers \(m,n\), the mixed adjoint-power commutator
\[
K_{m,n}=V^m(V^*)^n-(V^*)^n V^m
\]
has **exact rank**
\[
\operatorname{rank}K_{m,n}=2\min\{m,n\}.
\]
In the self-commutator case \(K_m=K_{m,m}\), exactly \(m\) nonzero eigenvalues are positive and exactly \(m\) are negative, counting multiplicity. They occur in opposite pairs \(\pm\lambda_{m,j}\), with \(\lambda_{m,j}>0\), and satisfy the exact all-order spectral product
\[
\boxed{\prod_{j=1}^m\lambda_{m,j}^{\,2}=
\frac{\left(\prod_{r=0}^{2m-1}r!\right)^2}{\prod_{r=0}^{4m-1}r!}.}
\]
In particular, every nonzero eigenvalue is determined as part of a finite, explicitly constructible rational matrix spectrum, and there is no hidden infinite-dimensional spectral tail.

## Assumptions and scope
All powers are positive **integer** powers of the bounded Volterra operator on \(L^2(0,1)\) with Lebesgue measure. The adjoint is \((V^*f)(x)=\int_x^1 f(t)\,dt\); the commutator convention is \([A,B]=AB-BA\). Set \(\mathcal P_d=\{\text{polynomials of degree at most }d\}\). The term rank refers to the Hilbert-space operator rank. The determinant below is taken on the invariant, finite-dimensional range and is not a Fredholm determinant on the whole Hilbert space.

## Proof
**1. A rank-two building block.** By Fubini, the integral kernel of \([V,(V^*)^n]\) is, for every \(x,y\in(0,1)\),
\[
B_n(x,y)=\frac{y^n-(1-x)^n}{n!}.
\]
For instance, on \(x<y\) its two constituent kernels are \([y^n-(y-x)^n]/n!\) and \([(1-x)^n-(y-x)^n]/n!\); on \(x>y\) the same difference results. The displayed kernel is a sum of two separable polynomial kernels, so \(\operatorname{rank}[V,(V^*)^n]\le2\). The standard commutator identity gives
\[
K_{m,n}=\sum_{j=0}^{m-1}V^j[V,(V^*)^n]V^{m-1-j},
\]
hence \(\operatorname{rank}K_{m,n}\le2m\). Since \(K_{m,n}^*=K_{n,m}\), this yields the upper bound \(2\min(m,n)\).

**2. Polynomiality and the exact lower bound.** Take \(m\le n\) and put \(L=m+n-1\). The building-block formula, together with integration of polynomials by \(V\) and \(V^*\), shows that \(K_{m,n}\) has a globally polynomial kernel \(k_{m,n}(x,y)\), of total degree at most \(L\). Directly, on \(0<x<y<1\), the kernel is
\[
\frac1{(m-1)!(n-1)!}
\left\{\int_0^x(x-t)^{m-1}(y-t)^{n-1}\,dt
-\int_y^1(t-x)^{n-1}(t-y)^{m-1}\,dt\right\}.
\]
Write \(k_{m,n}(x,y)=\sum_{i,j=0}^L a_{ij}x^iy^j\). Expanding these two integrals, using the beta integral and the upper-endpoint polynomial expansion, gives the entire highest total-degree diagonal:
\[
a_{i,L-i}=\begin{cases}
\dfrac{(-1)^{m-1-i}}{i!(L-i)!},&0\le i<m,\\[5pt]
0,&m\le i<n,\\[5pt]
\dfrac{(-1)^{i-m}}{i!(L-i)!},&n\le i\le L.
\end{cases}
\]
The middle cancellation is exact, not asymptotic. Let \(S=\{0,\ldots,m-1\}\cup\{n,\ldots,L\}\), of cardinality \(2m\). In the square coefficient submatrix \((a_{ij})_{i,j\in S}\), all entries with \(i+j>L\) vanish, while every anti-diagonal entry with \(i+j=L\) is nonzero. Thus this submatrix is invertible after reversing columns. The coefficient matrix has rank at least \(2m\). The integral operator rank equals this matrix rank because the monomials are linearly independent and their moment functionals are independent (their Gram matrix is positive definite). Together with Step 1, \(\operatorname{rank}K_{m,n}=2m\). Taking adjoints handles \(m>n\).

**3. Exact self-commutator determinant.** Put \(n=m\) and \(N=2m\). The rank result and polynomial degree bound imply \(\operatorname{ran}K_m=\mathcal P_{N-1}\). Its kernel coefficient matrix \(A=(a_{ij})_{0\le i,j<N}\) is anti-triangular, with \(a_{ij}=0\) for \(i+j>N-1\). The just-computed highest-degree coefficients yield
\[
\det A=\frac{(-1)^m}{\left(\prod_{r=0}^{N-1}r!\right)^2}.
\]
The monomial Gram matrix \(G=(1/(i+j+1))_{0\le i,j<N}\) is a Hilbert matrix. Its Cauchy determinant is
\[
\det G=\frac{\prod_{r=0}^{N-1}(r!)^4}{\prod_{r=0}^{2N-1}r!}.
\]
The matrix of \(K_m\) acting on its invariant range in the monomial basis is \(AG\). Consequently
\[
\det(K_m|_{\mathcal P_{N-1}})
=\frac{(-1)^m\left(\prod_{r=0}^{N-1}r!\right)^2}{\prod_{r=0}^{2N-1}r!}.
\]

**4. Inertia and pairing.** The operator \(K_m\) is self-adjoint. The reflection unitary \((Rf)(x)=f(1-x)\) obeys \(RVR=V^*\); hence \(RK_mR=-K_m\). Every nonzero eigenvalue therefore occurs with the same multiplicity as its negative. Rank \(2m\) gives exactly \(m\) positive and \(m\) negative eigenvalues, counting multiplicity. Their determinant is \((-1)^m\prod_{j=1}^m\lambda_{m,j}^2\). Equating this with Step 3 proves the stated factorial identity.

## Verification
The included `verify_volterra.py` independently expands both triangular Fubini kernel expressions and compares their exact rational polynomial coefficients for all \(1\le m,n\le5\). It checks the rank \(2\min(m,n)\), the leading homogeneous coefficient formula, the nonzero coefficient minor, and, for \(1\le m\le5\), the self-adjoint matrix determinant, reflection symmetry and even characteristic polynomial. Run `python verify_volterra.py` with Python 3 and SymPy. The replay output is `VOL_TERRA_MIXED_EXACT_OK 205 checks; 25 mixed pairs and five self-adjoint determinants`. The finite checks are corroborative; the statements for *all* positive integers rest on the proof above.

## Relationship to prior work
The 2022 study by Khadkhuu and Tsedenbayar evaluates self-commutator norms at integration orders one and two, not the mixed-power exact rank law or the factorial spectral product for every order. Ransford and Tsedenbayar (arXiv:2402.09287, first submitted 14 February 2024) study spectra and numerical ranges of the *linear* combinations \(V^m\pm(V^*)^m\), not the mixed *products* in \(K_{m,n}\). A separate all-order polynomial adjoint-power-pencil result supplies an exact rank and determinant for a linear combination \(V^m+(-1)^{m-1}(V^*)^m\). Its finite-rank kernel is relevant algebraic background, but its theorem does not give the rank of \([V^m,(V^*)^n]\) or the self-commutator eigenvalue product. The special cases \(m=1\) and \(m=2\), rank-two commutator identities and the Cauchy determinant are not asserted to be discoveries.

## Limitations
The classification applies to integer integration powers, not fractional orders, weighted Volterra kernels, or general polynomials in \(V\). The factorial product does not individually solve the algebraic characteristic equations for each fixed order. A standard abstract finite-rank commutator theory, or older literature not located by the searches, might cover aspects of the exact rank statement; this is a historical-priority risk. No independent mathematical audit has been performed.

## References
- T. Ransford and D. Tsedenbayar, *On the real and imaginary parts of powers of the Volterra operator*, arXiv:2402.09287, originally submitted 14 February 2024; https://arxiv.org/abs/2402.09287.
- L. Khadkhuu and D. Tsedenbayar, *A note on self-commutators of Volterra operator and its square*, Journal of Applied Science and Engineering A 3 (2022), 11–16, DOI:10.5564/jasea.v3i1.2455; https://doi.org/10.5564/jasea.v3i1.2455.
- *Exact rank, inertia, and Schatten cancellation for opposing Volterra powers* (2026), publicly indexed mathematical note on the linear adjoint-power pencil; https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-rank-inertia-and-schatten-cancellation-for-opposing-volter--498265e45420.
