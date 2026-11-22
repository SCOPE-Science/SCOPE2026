# Sharp finite-size norm deficit for the dyadic Walsh compression

## Finding
For each integer \(N\ge2\), put \(d_0=1\), \(d_j=2^{j-1}\) for \(1\le j\le N\), and define the symmetric \((N+1)\)-by-\((N+1)\) matrix
\[
C_N(i,j)=2^{-N/2}\sqrt{d_i d_j}\,\mathbf1_{\{i+j\le N\}},\qquad 0\le i,j\le N.
\]
Its operator norm is determined **exactly at every finite index** by a tridiagonal characteristic polynomial. Define polynomials in a real variable \(t\) by
\[
\begin{split}
p_0(t)&=1,\qquad p_1(t)=2-t,\\
p_2(t)&=(6-t)(2-t)-4,\\
p_k(t)&=(6-t)p_{k-1}(t)-8p_{k-2}(t)\quad(3\le k\le N),\\
p_{N+1}(t)&=(4-t)p_N(t)-8p_{N-1}(t).
\end{split}
\]
Let \(\lambda_N\) be the smallest real zero of \(p_{N+1}\). Then \(\lambda_N>0\), all its zeros are positive and simple, and
\[
\boxed{\|C_N\|_{2\to2}=\lambda_N^{-1/2}.}
\]
More sharply, with \(L_\infty=1+1/\sqrt2\) and \(c=5+3\sqrt2\),
\[
\boxed{
L_\infty-\|C_N\|_{2\to2}
=\frac{\sqrt2\,\pi^2 L_\infty^3}{(N+c)^2}+O(N^{-4})
\qquad(N\to\infty).}
\]
In particular the norm deficit has the exact positive limit
\[
\lim_{N\to\infty}N^2\big(L_\infty-\|C_N\|_{2\to2}\big)
=\sqrt2\,\pi^2\left(1+\frac1{\sqrt2}\right)^3.
\]
These are assertions for the specified Walsh compression, not an assertion that it maximizes the norm among *all* dyadic column truncations.

## Assumptions and scope
All norms on finite-dimensional spaces are Euclidean operator norms. Indices start at zero. The constant in the \(O(N^{-4})\) term is absolute. No assertion is made about arbitrary non-dyadic truncations or the global Walsh maximal operator. The matrix above is the standard dyadic Walsh–Hadamard compression studied by Hogan and Lakey and also represented (with swapped letters for the auxiliary matrices) by Lakey.

## Proof
**1. Exact inverse and Jacobi reduction.** Let \(D=\operatorname{diag}(d_0,\dots,d_N)\), \(M_{ij}=\mathbf1_{\{i+j\le N\}}\), and \(R\) reverse coordinates. Writing \(M=UR\), where \(U\) is the upper triangular matrix of ones, gives \(U^{-1}=I-S\), where \(S\) has ones on its first superdiagonal. Consequently
\[
C_N^{-1}=2^{N/2}D^{-1/2}R(I-S)D^{-1/2}=:B_N.
\]
All nonzero entries of the symmetric \(B_N\) occur on two antidiagonals: \(B_N(i,j)=\sqrt2\) for \(i+j=N\) at an endpoint, \(B_N(i,j)=2\) for \(i+j=N\) away from endpoints, and \(B_N(i,j)=-\sqrt2\) for \(i+j=N+1\). Thus direct multiplication gives
\[
J_N:=B_N^2=\begin{pmatrix}
2&-2&&&\\
-2&6&-2\sqrt2&&\\
&-2\sqrt2&6&\ddots&\\
&&\ddots&6&-2\sqrt2\\
&&&-2\sqrt2&4
\end{pmatrix},
\]
where the middle \(6\) values occupy indices \(1,\dots,N-1\). The standard leading-minor determinant recurrence for \(J_N-tI\) is precisely the displayed recursion for \(p_{N+1}\). Because \(J_N\) is a positive definite irreducible real symmetric tridiagonal matrix, its eigenvalues are positive and simple. Since \(J_N=C_N^{-2}\), the operator norm of the symmetric \(C_N\) is the reciprocal square root of the least eigenvalue of \(J_N\). This proves the exact finite-index formula.

**2. Localization at the spectral edge.** Put \(t_*=6-4\sqrt2=L_\infty^{-2}\) and \(s=3+2\sqrt2\). The vector
\[
h=(\sqrt2 s,\,1+s,\,2+s,\,\dots,\,N+s)^T
\]
has all positive coordinates. A direct substitution into the Jacobi matrix shows \((J_N-t_*I)h\) vanishes at indices \(0,\dots,N-1\), while its last entry is
\[
(2\sqrt2-2)(N+s)+2\sqrt2>0.
\]
The ground-state transform for a tridiagonal matrix with negative offdiagonal entries now gives, for every real vector \(u\),
\[
\langle u,(J_N-t_*I)u\rangle
=\sum_{i=0}^{N-1}(-J_N(i,i+1))h_i h_{i+1}
\left(\frac{u_i}{h_i}-\frac{u_{i+1}}{h_{i+1}}\right)^2
+\frac{[(J_N-t_*I)h]_N}{h_N}u_N^2.
\]
The right side is strictly positive for nonzero \(u\). Hence \(\lambda_N>t_*\). On the other hand, the principal submatrix indexed by \(1,\dots,N-1\) is a constant-coefficient Jacobi matrix whose least eigenvalue is \(6-4\sqrt2\cos(\pi/N)\). The Rayleigh principle yields
\[
t_*<\lambda_N\le6-4\sqrt2\cos(\pi/N).
\]
Thus \(\lambda_N\to t_*\) and, writing
\[
\lambda_N=6-4\sqrt2\cos\theta_N,\qquad \theta_N>0,
\]
we have \(0<\theta_N\le\pi/N\) and \(\theta_N\to0\).

**3. Exact boundary phases.** For all sufficiently large \(N\), the Jacobi matrix's lowest eigenvector has strictly positive entries \(u_i\), by irreducibility and the variational principle. Its interior recurrence for \(i\ge2\) is
\[
u_{i+1}-2\cos\theta_N\,u_i+u_{i-1}=0.
\]
The first two Jacobi equations impose the effective left boundary \(u'_0=a(\theta_N)u_1\), where \(u'_0\) is the value obtained by extending the constant-coefficient recurrence from indices \(1,2\) and
\[
a(\theta)=\frac{\sqrt2}{2-(6-4\sqrt2\cos\theta)}.
\]
The last Jacobi equation imposes the right boundary \(u_{N+1}=bu_N\) with \(b=1/\sqrt2\). The positive eigenvector must therefore be proportional, for \(1\le i\le N\), to
\[
u_i=\sin((i-1)\theta_N+\phi(\theta_N)),
\]
where, for small positive \(\theta\), the boundary phases are
\[
\phi(\theta)=\arctan\frac{\sin\theta}{\cos\theta-a(\theta)},\qquad
\eta(\theta)=\arctan\frac{\sin\theta}{\cos\theta-b}.
\]
Both denominators are positive near zero. Positivity of the principal eigenvector fixes the first phase branch, so the right boundary identity is
\[
(N-1)\theta_N+\phi(\theta_N)+\eta(\theta_N)=\pi.
\]
In particular this is not merely an approximate boundary condition.

**4. Sharp expansion.** At zero, \(a(0)=(2+\sqrt2)/4\). Taylor expansion gives
\[
\phi(\theta)=\frac{\theta}{1-a(0)}+O(\theta^3),\qquad
\eta(\theta)=\frac{\theta}{1-b}+O(\theta^3).
\]
The boundary equation becomes
\[
(N+c)\theta_N=\pi+O(\theta_N^3),\qquad
c=-1+\frac1{1-a(0)}+\frac1{1-b}=5+3\sqrt2.
\]
Using \(\theta_N\le\pi/N\) gives
\[
\theta_N=\frac\pi{N+c}+O(N^{-4}).
\]
Finally, Taylor expansion of the cosine and the inverse square root yields
\[
\lambda_N=t_*+\frac{2\sqrt2\,\pi^2}{(N+c)^2}+O(N^{-4})
\]
and hence the asserted \(L_\infty-\lambda_N^{-1/2}\) expansion, including its coefficient and error term.

## Verification
The exact identities \(C_NB_N=I\), \(B_N^2=J_N\) and the characteristic-polynomial recurrence have been independently checked in exact algebra for \(2\le N\le12\), with the positive test vector and its boundary residual. Direct Jacobi eigenvalue computations at indices \(4,6,10,20,40,80,200,500,1000\) agree with the shifted asymptotic; see `checks/check.py`. These finite checks supplement but do not replace the proof for all \(N\).

## Relationship to prior work
Lakey's February 19, 2026 arXiv preprint introduces the standard dyadic Walsh truncation and its compressed matrix, alongside conjectural extremality among dyadic truncations. Hogan and Lakey's February 28, 2026 paper studies the same compression, obtains an approximate eigenvector at the limiting norm, and explicitly reports only *numerical evidence* that the norm deficit is of order \(N^{-2}\) (Remark 2). The present result proves that sharp rate, identifies its leading coefficient and finite-size phase shift, and supplies an exact finite characteristic-polynomial method. It neither proves nor assumes the conjecture comparing all dyadic truncations.

## Limitations
The exact norm is given as the smallest zero of an explicit recurrence, not in radicals for arbitrary \(N\). The correction formula is asymptotic with an absolute (not evaluated) \(O(N^{-4})\) constant. Classical Jacobi recurrence and ground-state-transform methods are standard; the claim is the specialized exact reduction and quantitative spectral-edge expansion for this Fourier compression. An equivalent calculation in unindexed literature cannot be excluded. No independent review is represented here.

## References
1. J. D. Lakey, *Towards direct \(L^2\)-bounds for maximal partial sums of Walsh–Fourier series: The case of dyadic partial sums*, arXiv:2602.17627v1, first posted February 19, 2026. https://arxiv.org/abs/2602.17627
2. J. A. Hogan and J. D. Lakey, *An Eigenvector Problem Arising in the Study of Convergence of Walsh–Fourier Series*, Mathematics **14** (2026), 829, first published February 28, 2026. https://doi.org/10.3390/math14050829
