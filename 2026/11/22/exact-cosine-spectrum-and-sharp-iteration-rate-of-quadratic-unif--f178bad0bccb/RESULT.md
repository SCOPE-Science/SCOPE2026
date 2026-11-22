# Exact cosine spectrum and sharp iteration rate of quadratic uniform Schoenberg splines

## Finding
For each integer \(n\ge 2\), the classical *uniform clamped quadratic* Schoenberg–Greville operator \(S_n:C([0,1])\to C([0,1])\) has the **entire spectrum**
\[
\boxed{\sigma(S_n)=\{0,1\}\cup\left\{\frac{3+\cos(j\pi/n)}4:1\le j\le n\right\}.}
\]
The eigenvalue \(1\) has multiplicity two (the fixed affine functions), each of the \(n\) displayed nontrivial eigenvalues is simple, and \(0\) is an infinite-multiplicity eigenvalue. Explicit quadratic B-spline eigenfunctions are given below. Consequently the second-largest eigenvalue and the exact asymptotic rate of convergence of the iterates to endpoint interpolation \(L\) are
\[
\boxed{\gamma_n=\frac{3+\cos(\pi/n)}4,\qquad
\lim_{m\to\infty}\|S_n^m-L\|_{C\to C}^{1/m}=\gamma_n,\qquad
n^2(1-\gamma_n)\longrightarrow\frac{\pi^2}{8}.}
\]
This gives, for quadratic degree, an explicit affirmative and quantitatively sharp answer to the fixed-degree, fine-mesh half of Conjecture 1 posed by Nagler, Cerejeiras and Forster (2014). No assertion is made for any other fixed spline degree or for increasing spline degree.

## Assumptions and scope
Fix an integer \(n\ge2\). The knot vector of length \(n+5\) is
\[
t_0=t_1=t_2=0,\quad t_{i+2}=i/n\quad(1\le i\le n-1),\quad
t_{n+2}=t_{n+3}=t_{n+4}=1.
\]
Let \(B_0,\ldots,B_{n+1}\) be the normalized degree-two nonnegative B-splines associated to these knots, with the usual left-continuous endpoint convention at \(1\). Their Greville nodes are
\[
\xi_i=(t_{i+1}+t_{i+2})/2,
\quad \xi_0=0,\quad \xi_i=(i-\tfrac12)/n\ (1\le i\le n),\quad \xi_{n+1}=1.
\]
For each real-valued \(f\in C([0,1])\) define
\[
(S_nf)(x)=\sum_{i=0}^{n+1}f(\xi_i)B_i(x),
\quad (Lf)(x)=(1-x)f(0)+xf(1).
\]
Spectrum and operator norms refer to the complexification of \(C([0,1])\), with supremum norm, and the corresponding induced operator norm. Affine reproduction \(S_nL=L=LS_n\) follows from partition of unity and the Greville linear reproduction identity.

For \(1\le j\le n\), define \(\theta_j=j\pi/n\), \(v_i^{(j)}=\sin((i-\tfrac12)\theta_j)\) for \(1\le i\le n\), and
\[
\Phi_j(x)=\sum_{i=1}^{n}v_i^{(j)}B_i(x),\quad
q_j=\sum_{i=1}^{n}(v_i^{(j)})^2=
\begin{cases}n/2,&1\le j<n,\\n,&j=n.\end{cases}
\]
All the \(\Phi_j\) vanish at both endpoints. Their exact eigenvalues are \(\lambda_j=(3+\cos\theta_j)/4\).

## Proof
**1. Exact collocation block.** The Cox–de Boor recurrence at the Greville nodes gives the matrix \(M_{i\ell}=B_\ell(\xi_i)\), indexed by \(0\le i,\ell\le n+1\). Its first and last rows have only a single \(1\) at their corresponding endpoint columns. In the interior rows \(1\le i\le n\), the only nonzero entries are
\[
M_{i,i}=\begin{cases}5/8,&i=1\text{ or }i=n,\\3/4,&2\le i\le n-1,\end{cases}\qquad
M_{i,i-1}=\begin{cases}1/4,&i=1,\\1/8,&i\ge2,\end{cases}
\]
\[
M_{i,i+1}=\begin{cases}1/4,&i=n,\\1/8,&i\le n-1.\end{cases}
\]
For \(n=2\), both boundary formulas apply without any interior middle rows. Thus the middle \(n\times n\) block \(T=(M_{i\ell})_{1\le i,\ell\le n}\) is real symmetric, with diagonal \(5/8\) at both ends, \(3/4\) in the interior, and first off-diagonals equal to \(1/8\). The entries to the exterior columns supply the missing \(1/4\) mass in the first and last interior rows.

**2. Anti-reflecting boundary eigenvectors.** For an interior sequence \(v=(v_1,\ldots,v_n)\), extend the ghost values as \(v_0=-v_1\) and \(v_{n+1}=-v_n\). Then every row of \(T\) is
\[
(Tv)_i=\tfrac34v_i+\tfrac18(v_{i-1}+v_{i+1}).
\]
The sine choice \(v_i^{(j)}=\sin((i-\tfrac12)j\pi/n)\) obeys the ghost conditions, since \(\sin(-\theta_j/2)=-\sin(\theta_j/2)\) and \(\sin((n+\tfrac12)\theta_j)=-\sin((n-\tfrac12)\theta_j)\) for every integer \(j\). Using \(\sin(a-b)+\sin(a+b)=2\sin(a)\cos(b)\) therefore proves
\[
Tv^{(j)}=(\tfrac34+\tfrac14\cos\theta_j)v^{(j)}=\lambda_jv^{(j)}.
\]
Discrete sine orthogonality gives \(\sum_i v_i^{(j)}v_i^{(k)}=q_j\mathbf1_{j=k}\), with \(q_j=n/2\) for \(j<n\), \(q_n=n\). In particular these \(n\) vectors span the interior subspace, and \(1/2=\lambda_n<\cdots<\lambda_1<1\). The coefficient spline \(\Phi_j\) vanishes at both endpoints, and evaluation of it at the interior nodes equals \(Tv^{(j)}\); hence \(S_n\Phi_j=\lambda_j\Phi_j\).

**3. Completeness of the spectrum.** The operator has range in the \((n+2)\)-dimensional spline space, where the fixed affine functions form a two-dimensional eigenspace at \(1\), and the \(n\) independent \(\Phi_j\) supply all remaining directions. The spline coefficient-to-function map is injective by B-spline linear independence, so no nonzero spectral value is omitted. Since \(C([0,1])\) is infinite dimensional and \(S_n\) has finite rank, \(0\) is an eigenvalue of infinite multiplicity and there are no further spectral values. The distinct eigenvalues also show the finite-dimensional image operator is diagonalizable.

**4. Exact iterations and sharp rate.** Set \(d_i=f(\xi_i)-Lf(\xi_i)\) for \(1\le i\le n\). The first iterate of \(f-Lf\) has interior spline coefficients \(d\) and zero endpoint coefficients. Each subsequent iterate applies \(T\) to that coefficient vector. The discrete sine expansion therefore holds as a genuine finite identity for every \(m\ge1\):
\[
\boxed{S_n^m f-Lf=\sum_{j=1}^n\lambda_j^{m-1}
\frac{\sum_{i=1}^n d_i v_i^{(j)}}{q_j}\Phi_j.}
\]
All coefficient functionals are bounded. Since \(0<\lambda_j<\lambda_1\) for \(j\ge2\), the normalized operators satisfy
\[
\gamma_n^{1-m}(S_n^m-L)\longrightarrow P_{n,1},\quad
(P_{n,1}f)(x)=\frac{\sum_{i=1}^n d_i v_i^{(1)}}{q_1}\Phi_1(x)
\]
in operator norm, where \(P_{n,1}\ne0\) (test \(f=\Phi_1\)). This proves the sharp operator-norm \(m\)-th-root limit, without relying on a generic upper rate alone. Finally, \(1-\gamma_n=(1-\cos(\pi/n))/4\), and \(n^2(1-\cos(\pi/n))\to\pi^2/2\); thus the spectral gap has the stated \(\pi^2/(8n^2)\) law.

## Verification
The accompanying standalone `spectral_check.py` uses rational Cox–de Boor basis values and independently constructs all sampling matrices for \(2\le n\le48\). It verifies every matrix row and affine reproduction exactly; it then evaluates all \(1,175\) asserted interior eigenmode identities and \(1,316\) sampled power-expansion equalities in floating point. Replaying `python3 spectral_check.py` prints `PASS`. The finite experiments do not establish the all-\(n\) theorem; that follows from the preceding recurrence, trigonometric identities and spectral expansion. For example \(n=2\) yields nontrivial eigenvalues \(3/4,1/2\), and \(n=3\) yields \(7/8,5/8,1/2\).

## Relationship to prior work
Nagler, Cerejeiras and Forster (arXiv:1402.2403v1, February 11, 2014) proved general spectral containment and geometric convergence of Schoenberg iterates, but expressly stated on page 11 that the exact eigenvalues/eigenfunctions were unknown, and their Conjecture 1 included \(\gamma_{\Delta_n,k}\to1\) for fixed \(k\) as the mesh grows. This proof supplies **only the quadratic, uniform-knot case** with a sharp coefficient; the broad conjecture is not claimed solved. Nagler and Kähler (arXiv:1312.5546v1) also investigated uniform Schoenberg iteration but did not state this cosine spectrum. Moldovan (2017) instead studied how to modify quadratic knot positions to improve approximation order, and Moldovan and Păltănea (2020–2021) studied multidimensional approximation and shape preservation. The anti-reflecting tridiagonal sine diagonalization is elementary and is used as a tool, not claimed as a separate novel result. Targeted searches found no exact equivalent Schoenberg–Greville operator spectrum, but missing or unindexed historical spectral calculations remain a novelty risk.

## Limitations
The full spectrum and sharp iterated convergence are established only for degree-two splines on an exactly uniform, clamped finite interval, with the standard Greville nodes and unweighted supremum norm. They are not assertions about general knots, other spline degrees, joint large-degree limits or a uniform-in-\(n\) power-expansion remainder. The eigenvalues of the finite cosine tridiagonal block are classical; priority concerns the specific operator identification and its consequent exact approximation rate.

## References
1. J. Nagler, P. Cerejeiras, B. Forster, *Lower bounds for the approximation with variation-diminishing splines*, arXiv:1402.2403v1, first public 2014-02-11, https://arxiv.org/pdf/1402.2403 (full text, Sections 2–3 and page 11, Conjecture 1).
2. J. Nagler, U. Kähler, *A lower bound for the uniform Schoenberg operator*, arXiv:1312.5546v1, first public 2013-12-19, https://arxiv.org/pdf/1312.5546 (full text, operator and iteration sections).
3. C. L. Moldovan, *A choice of the knots in Schoenberg spline operator with an improvement of the order of approximation*, Bulletin of the Transilvania University of Brașov, Series III 10(59), 2017, 77–90, https://www.researchgate.net/publication/323238390_A_choice_of_the_knots_in_Schoenberg_spline_operator_with_an_improvement_of_the_order_of_approximation (visible article text).
4. C. L. Moldovan, R. Păltănea, *A Definition of Two-Dimensional Schoenberg Type Operators*, Symmetry 12(8), 1364 (2020), https://doi.org/10.3390/sym12081364 (open full text).
5. C. L. Moldovan, R. Păltănea, *Preserving the Shape of Functions by Applying Multidimensional Schoenberg-Type Operators*, Symmetry 13(6), 1016 (2021), https://doi.org/10.3390/sym13061016 (open full text).
