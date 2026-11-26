# Universal sharp entrywise sensitivity of Laplace-transform matrix filters

## Finding

Let \(n\ge1\), \(\mu\ge0\), and let \(\nu\) be a finite nonnegative Borel measure on \([0,\infty)\) for which
\[
m_\mu=\int_{[0,\infty)}t e^{-\mu t}\,d\nu(t)<\infty.
\]
Define the Laplace-transform spectral filter \(g(s)=\int e^{-st}\,d\nu(t)\), \(s\ge\mu\), and the symmetric-matrix map \(\Phi_g(A)=g(-A)=\int e^{tA}\,d\nu(t)\), on the cone \(\mathcal D_\mu=\{A=A^{\mathsf T}\in\mathbb R^{n\times n}:A\preceq-\mu I\}\). Let \(\|H\|_{\max}=\max_{i,j}|H_{ij}|\), with the **same** norm on inputs and outputs. Then the exact global two-input Lipschitz coefficient is
\[
\boxed{\sup_{\substack{A,B\in\mathcal D_\mu\\A\ne B}}
\frac{\|\Phi_g(A)-\Phi_g(B)\|_{\max}}{\|A-B\|_{\max}}
=\frac{(1+\sqrt n)^2}{4}\int_{[0,\infty)} t e^{-\mu t}\,d\nu(t).}
\]
The formula includes the constant-filter case \(m_\mu=0\), with sharp coefficient zero. It is a supremum; finite distinct matrices need not attain it.

For heat evolution \(\Phi(A)=e^{\tau A}\) at fixed \(\tau>0\), the coefficient is \(\tau e^{-\mu\tau}(1+\sqrt n)^2/4\). For shifted resolvents \(\Phi(A)=(\alpha I-A)^{-1}\), \(\alpha>0\), it is \((1+\sqrt n)^2/[4(\alpha+\mu)^2]\). For every \(p>0\), the filter \((\alpha I-A)^{-p}\) has coefficient \(p(1+\sqrt n)^2/[4(\alpha+\mu)^{p+1}]\). Thus, even though each \(e^{tA}\) is contractive in Euclidean norm, sensitivity to componentwise input errors has sharp dimension-growth \(n/4+\sqrt n/2+1/4\) relative to the scalar derivative.

## Assumptions and scope

Everything is real and finite-dimensional. Both input matrices are symmetric, with all eigenvalues at most \(-\mu\). The perturbation is allowed to be any symmetric matrix as long as both endpoints remain in the cone. No nonnegativity of the entries, graph-Laplacian structure, finite lower spectral bound, or commutativity between the two inputs is assumed. The measure \(\nu\) is finite and nonnegative, and the stated weighted first moment is finite. For \(n=1\), the dimensional factor is one. The result does not cover signed measures or arbitrary scalar functions without a positive Laplace representation.

## Proof

**Step 1: sharp row-sum norm of a positive contraction.** If \(0\preceq B\preceq I\) is real symmetric, put \(q=B_{ii}\in[0,1]\). Since \(B^2\preceq B\),
\[
\sum_{j\ne i}B_{ij}^2=(B^2)_{ii}-q^2\le q(1-q).
\]
Cauchy–Schwarz gives
\[
\sum_j|B_{ij}|\le q+\sqrt{n-1}\sqrt{q(1-q)}
\le C_n,\qquad C_n=\frac{1+\sqrt n}{2}.
\]
The last maximum follows by writing \(q=(1+\cos\theta)/2\): its right side is \(1/2+[\cos\theta+\sqrt{n-1}\sin\theta]/2\), maximized at \(q_*= (1+n^{-1/2})/2\). For \(n=1\) the same bound reads \(q\le1=C_1\). In particular, every positive contraction has induced vector \(\ell^\infty\) norm at most \(C_n\).

The estimate is **sharp**. For \(n\ge2\) set
\[
u_1=\sqrt{q_*},\qquad u_j=\sqrt{\frac{1-q_*}{n-1}}\quad(2\le j\le n),
\qquad P=uu^{\mathsf T}.
\]
Then \(\|u\|_2=1\), \(P\) is an orthogonal rank-one projection, and
\[
\sum_j P_{1j}=u_1\sum_j u_j=q_*+\sqrt{(n-1)q_*(1-q_*)}=C_n.
\]
For \(n=1\), use \(u=(1)\) and \(P=I\).

**Step 2: global upper estimate.** For any \(A\in\mathcal D_\mu\) and \(t\ge0\), the spectral theorem gives \(0\preceq e^{tA}\preceq e^{-\mu t}I\). Step 1 thus yields
\[\|e^{tA}\|_{\infty\to\infty}\le C_n e^{-\mu t}.\]
The standard Fréchet formula, for a symmetric direction \(H\), is
\[
D(e^{tA})[H]=t\int_0^1e^{(1-r)tA}H e^{rtA}\,dr.
\]
Using \(\|XYZ\|_{\max}\le\|X\|_{\infty\to\infty}\|Y\|_{\max}\|Z\|_{1\to1}\), and symmetry of the outer factors, gives
\[\|D(e^{tA})[H]\|_{\max}\le t e^{-\mu t} C_n^2\|H\|_{\max}.\]
The weighted moment condition allows differentiation under the \(\nu\)-integral for matrices strictly inside \(\mathcal D_\mu\), yielding \(\|D\Phi_g(A)[H]\|_{\max}\le m_\mu C_n^2\|H\|_{\max}\). Alternatively the two-input Duhamel formula gives the same bound on the entire closed cone directly: for \(A,B\in\mathcal D_\mu\),
\[
e^{tA}-e^{tB}=t\int_0^1 e^{(1-r)tA}(A-B)e^{rtB}\,dr,
\]
so integration against \(\nu\) establishes the claimed global upper estimate without requiring boundary differentiability.

**Step 3: exactness by a rank-one slow mode.** Let \(u,P\) be as in Step 1 and write \(J=\mathbf1\mathbf1^{\mathsf T}\). Fix \(\delta>0\) and \(M>0\), and set
\[
A_{\delta,M}=-(\mu+\delta)I-M(I-P).
\]
This matrix is in the strict interior of \(\mathcal D_\mu\); for \(|h|<\delta/n\), both \(A_{\delta,M}\) and \(A_{\delta,M}+hJ\) remain in the cone because \(\|J\|_2=n\). Also \(\|J\|_{\max}=1\). For every \(0<r<1\),
\[
\lim_{M\to\infty}e^{(1-r)tA_{\delta,M}}J e^{rtA_{\delta,M}}
=e^{-t(\mu+\delta)}PJP\qquad(t>0).
\]
The integrand norm is bounded by \(C_n^2e^{-t(\mu+\delta)}\) times the factor \(t\); the moment hypothesis permits dominated convergence first over \(r\) and then over \(\nu\). Hence
\[
\lim_{M\to\infty}D\Phi_g(A_{\delta,M})[J]
=\left(\int t e^{-(\mu+\delta)t}\,d\nu(t)\right)PJP.
\]
The first diagonal element satisfies \((PJP)_{11}=(u_1\sum_j u_j)^2=C_n^2\), including \(n=1\). Since the derivative at an interior point is a limit of admissible two-input difference quotients in direction \(J\), the global Lipschitz coefficient is at least \(C_n^2 m_{\mu+\delta}\). Let \(\delta\downarrow0\); monotone convergence gives \(m_{\mu+\delta}\uparrow m_\mu\), completing equality. No finite experiment or inaccessible lemma is needed.

## Verification

The proof reduces to the explicitly derived contraction row bound, the Fréchet/Duhamel integral identity and a rank-one limit; no computational certificate is needed for the universal quantifiers. `CHECK.py` is a standalone Python 3 standard-library supplementary checker. Running `python3 CHECK.py` produces `CHECK_OK 2100 supplementary assertions`, including the closed-form rank-one identities, 1,500 random positive-contraction row-sum tests, and convergence of the exact two-eigenvalue derivative toward the predicted constant for heat, resolvent, fractional-power and positive-mixture filters. These tests are not the proof of the infinite statement.

## Relationship to prior work

Fréchet derivatives of matrix functions and their condition estimates are standard; the present claim is not their discovery. Kandolf–Relton (2017) develops Krylov approximation for matrix-function derivatives. Crouzeix–Kressner (2020) establishes bivariate functional-calculus *spectral-norm* estimates, with a general upper constant \((1+\sqrt2)^2\) for the spectral norm, but not the dimension-dependent *entrywise maximum* sharp coefficient here. Kandolf–Koskela–Relton–Schweitzer (2020) studies low-rank approximations and Stieltjes functions, again in Euclidean norm. The additional result here is the exact all-dimensional maximum-entry coefficient for every nonnegative Laplace-transform filter and the universal slow-rank-one extremizing sequence. Searches of published mathematical records and accessible prior research claims did not identify a dominating statement; this is evidence-limited, not a proof of priority.

## Limitations

The theorem is finite-dimensional and its dimension-dependent factor generally grows. It does not imply bounds independent of \(n\), nor does it apply to arbitrary nonsymmetric dissipative generators, entrywise nonnegative Markov generators, signed Laplace mixtures, or finite lower spectral windows without further analysis. The supremum may only be approached by increasingly separated spectral scales. The priority assessment is conditional on the inspected indexed sources; unindexed equivalent results remain possible. Independent mathematical validation has not been performed.

## References

1. M. Crouzeix and D. Kressner, *A bivariate extension of the Crouzeix–Palencia result with an application to Fréchet derivatives of matrix functions*, arXiv:2007.09784, first publicly posted 2020-07-19, https://arxiv.org/abs/2007.09784.
2. P. Kandolf, A. Koskela, S. D. Relton, M. Schweitzer, *Computing low-rank approximations of the Fréchet derivative of a matrix function using Krylov subspace methods*, arXiv:2008.12926, first publicly posted 2020-08-29, https://arxiv.org/abs/2008.12926; journal full text https://doi.org/10.1002/nla.2401.
3. P. Kandolf and S. D. Relton, *A Block Krylov Method to Compute the Action of the Fréchet Derivative of a Matrix Function on a Vector with Applications to Condition Number Estimation*, SIAM J. Sci. Comput. 39 (2017), A1416–A1434, https://doi.org/10.1137/16M1077969.
4. N. J. Higham, *What Is a Matrix Norm?*, expository reference on induced matrix norms, https://nhigham.com/2021/.
