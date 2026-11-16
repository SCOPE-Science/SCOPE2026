# A sharp finite-degree gap-entry threshold and Robin edge crossover for two-periodic orthogonal polynomials

## Finding

Let \(a\in\mathbb R\) and \(b,c>0\), and define monic real orthogonal polynomials by \(P_{-1}=0\), \(P_0=1\) and, for \(n\ge0\),
\[
P_{n+1}(x)=(x-(-1)^n a)P_n(x)-d_nP_{n-1}(x),\qquad d_{2j+1}=b,\quad d_{2j}=c\ (j\ge1).
\]
The value of \(d_0\) is immaterial. Put
\[
r=\sqrt{a^2+(\sqrt b-\sqrt c)^2},\quad R=\sqrt{a^2+(\sqrt b+\sqrt c)^2},\quad q=\sqrt{c/b}.
\]
For **every** integer \(k\ge1\), the degree-\(2k\) polynomial has exactly two zeros in the central open periodic-bulk gap \((-r,r)\) **if and only if**
\[
\boxed{q>1+1/k.}
\]
The two gap zeros have opposite signs and equal nonzero absolute values. At equality, \(P_{2k}\) instead has exactly the two band-edge zeros \(\pm r\); below the threshold it has no gap or edge zeros. All its other zeros are in the interiors of the two bulk bands \([-R,-r]\cup[r,R]\), and no zero lies outside \([-R,R]\). The statement includes the closed-gap case \(r=0\), for which the strict threshold is impossible.

**Exact transition profile.** Fix \(a\in\mathbb R\), \(b>0\), and \(\gamma\in\mathbb R\). For each sufficiently large integer \(k\), set \(q_k=1+\gamma/k>0\) and \(c_k=bq_k^2\). Let \(\zeta_k>0\) be the smallest *positive* root of \(P_{2k}\) for these parameters. Then
\[
\boxed{\lim_{k\to\infty}\frac{k^2(\zeta_k^2-a^2)}b=\mathcal H(\gamma)},
\]
where the continuous crossover function is
\[
\mathcal H(\gamma)=\begin{cases}
\gamma^2+w_\gamma^2,&\gamma<1,\ \ w_\gamma\in(0,\pi),\quad w_\gamma\cot w_\gamma=\gamma,\\
1,&\gamma=1,\\
\gamma^2-z_\gamma^2,&\gamma>1,\ \ z_\gamma>0,\quad z_\gamma\coth z_\gamma=\gamma.
\end{cases}
\]
Both defining equations have exactly one solution in the specified range. In the subcritical branch the smallest root is in a band, in the supercritical branch it is in the gap, and at \(\gamma=1\) it is exactly at the inner band edge for **every** \(k\). In particular, the exact finite-size critical offset is \(q_k-1=1/k\).

## Assumptions and scope

The recurrence has strictly positive subdiagonal coefficients and hence defines a positive orthogonality functional and a half-line Jacobi operator. The two intervals above are the spectral bands of its periodic bulk; the half-line measure can additionally have an isolated gap atom, so the theorem makes no claim that the measure is supported *only* on the bands. The assertions concern the zeros of the monic polynomials and hold for every real \(a\), every positive \(b,c\), and all indicated degrees. The second assertion concerns a sequence of **different** positive-definite orthogonality functionals indexed by \(k\), not a fixed-measure degree limit.

## Proof

**1. Exact reduction.** Introduce the second-kind Chebyshev polynomials by \(U_{-1}=0\), \(U_0=1\), and \(U_{j+1}(t)=2tU_j(t)-U_{j-1}(t)\). Define \(t(x)=(x^2-a^2-b-c)/(2\sqrt{bc})\). Direct elimination of odd recurrence steps yields, for every \(k\ge1\),
\[
P_{2k+2}(x)=(x^2-a^2-b-c)P_{2k}(x)-bcP_{2k-2}(x).
\]
The initial values \(P_0=1\) and \(P_2=x^2-a^2-b\) therefore give
\[
\boxed{P_{2k}(x)=(bc)^{k/2}\bigl(U_k(t(x))+qU_{k-1}(t(x))\bigr).}
\]
For comparison, eliminating even steps gives \(P_{2k+1}(x)=(x-a)(bc)^{k/2}U_k(t(x))\), but the fixed Dirichlet zero of the odd degrees is not asserted to be new.

**2. One-dimensional outlier count.** Let \(F_k(t)=U_k(t)+qU_{k-1}(t)\). Its zeros \(2t\) are the eigenvalues of the real symmetric \(k\)-by-\(k\) tridiagonal matrix having off-diagonal entries one, first diagonal entry \(-q\), and all other diagonal entries zero. The unperturbed matrix has all its eigenvalues strictly between \(-2\) and \(2\). A negative rank-one perturbation moves no eigenvalue above \(2\) and permits at most one below \(-2\); irreducibility makes all eigenvalues simple. Finally,
\[
F_k(-1)=(-1)^k\bigl((k+1)-kq\bigr).
\]
The eigenvalues decrease strictly as \(q\) increases (their normalized eigenvectors have nonzero first component). Thus the smallest eigenvalue crosses \(-2\) exactly when \(q=(k+1)/k\); equality gives one simple edge root. All remaining \(t\)-roots lie in \((-1,1)\).

For a root \(t\ge-1\), the associated squared polynomial root is \(x^2=a^2+b+c+2\sqrt{bc}\,t\), in \([r^2,R^2)\). For \(t=-\cosh\eta<-1\), the Chebyshev formula gives
\[
\frac{\sinh((k+1)\eta)}{\sinh(k\eta)}=q.
\]
The left-hand ratio is strictly increasing for \(\eta>0\), with limit \((k+1)/k\) at zero and infinity as \(\eta\to\infty\). Moreover it is strictly greater than \(e^\eta\), so \(\eta<\log q\). Consequently
\[
a^2< x^2=a^2+b+c-2\sqrt{bc}\cosh\eta<r^2.
\]
This proves the exact gap pair, positivity of its squared radius, boundary cases, and absence of other exterior zeros.

**3. Critical profile from the exact root equations.** Let \(q_k=1+\gamma/k\). If \(\gamma>1\), write the unique outlier root as \(t_k=-\cosh\eta_k\). With \(z=k\eta\),
\[
k\left(\frac{\sinh((k+1)z/k)}{\sinh z}-1\right)\longrightarrow z\coth z
\]
locally uniformly for \(z>0\). The left-hand side increases strictly in \(z\), and \(z\coth z\) increases strictly from \(1\) to infinity. Bracketing around its unique solution gives \(k\eta_k\to z_\gamma\). Using
\[
\zeta_k^2-a^2=b\Bigl((q_k-1)^2-2q_k(\cosh\eta_k-1)\Bigr)
\]
proves the supercritical limit. The equation \(z_\gamma\coth z_\gamma=\gamma\) also gives \(0<z_\gamma<\gamma\), so the limit is positive.

If \(\gamma<1\), the smallest \(t\)-root belongs to \((-1,1)\). Write it as \(t_k=-\cos\theta_k\). It is characterized by the unique \(\theta_k\in(0,\pi/(k+1))\) with
\[
\frac{\sin((k+1)\theta_k)}{\sin(k\theta_k)}=1+\frac\gamma k.
\]
Uniqueness follows because \(u\cot u\) strictly decreases on \((0,\pi)\), making the ratio strictly decreasing from \((k+1)/k\) to zero on this interval. Uniformly on compact subintervals of \((0,\pi)\),
\[
k\left(\frac{\sin((k+1)w/k)}{\sin w}-1\right)\longrightarrow w\cot w.
\]
The limiting function decreases continuously from \(1\) to minus infinity, hence \(k\theta_k\to w_\gamma\). Now
\[
\zeta_k^2-a^2=b\Bigl((q_k-1)^2+2q_k(1-\cos\theta_k)\Bigr)
\]
gives the subcritical limit. For \(\gamma=1\), the exact finite-degree threshold yields \(t_k=-1\) and \(\zeta_k^2-a^2=b/k^2\). The branch formulas both tend to \(1\) as \(\gamma\to1\), proving continuity.

## Verification

The supplied standalone script `CHECK.py` verifies recurrence-to-Chebyshev identities by exact rational polynomial arithmetic for several parameter families and degrees, checks the exact finite-degree threshold in numerical tridiagonal examples, and compares the scaled smallest squared roots with the analytic crossover. These finite reproducibility checks do not replace the general rank-one, hyperbolic monotonicity, and compact-convergence arguments above. Run `python3 CHECK.py` with the Python standard library.

## Relationship to prior work

Paul Barry, *Orthogonal polynomials on two or more intervals: the Sprugnoli context* (arXiv:2611.05673, first posted 2026-11-03), Proposition 15, gives precisely the underlying two-periodic Jacobi matrix, coefficient structures and periodic-band formulas. The recurrence, its orthogonality and its bulk bands are **prior** results; what is established here is the degree-by-degree *exact threshold* for even-polynomial gap pairs and the parameter-varying sharp crossover.

Barry Simon, *Fine Structure of the Zeros of Orthogonal Polynomials, III. Periodic Recursion Coefficients* (arXiv:math/0412336, Theorems 2.1 and 2.3), develops general periodic-Jacobi band and Dirichlet-zero counting. In particular, the odd-degree fixed Dirichlet zero is covered by that framework. These theorems do not state the particular \(1+1/k\) boundary for even degrees or the \(k^{-2}\) cosine/hyperbolic Robin crossover as the recurrence coefficients change with degree. Peherstorfer's *Zeros of polynomials orthogonal on several intervals* (arXiv:math-ph/0203058) treats gap-zero representations and asymptotics on multiple intervals. These general tools supply important conceptual context rather than being claimed as new.

## Limitations

The criterion applies to this explicit period-two recurrence and does not classify all periodic Jacobi matrices. The crossover concerns the *smallest squared root* as the ratio \(c/b\) varies with degree; no assertions are made about eigenvector scaling or all zeros in the critical window. The same elementary Chebyshev combination can appear in older finite Jacobi boundary-defect or Bernstein–Szegő literature under alternate notation. Peherstorfer's 1991 study specifically addresses periodic recurrence coefficients but its complete text was unavailable. Full verification of these historical equivalences is not available, so publication priority remains provisional. No independent mathematical audit has been performed.

## References

1. P. Barry, *Orthogonal polynomials on two or more intervals: the Sprugnoli context*, arXiv:2611.05673, submitted 2026-11-03, https://arxiv.org/abs/2611.05673.
2. B. Simon, *Fine Structure of the Zeros of Orthogonal Polynomials, III. Periodic Recursion Coefficients*, arXiv:math/0412336, https://arxiv.org/abs/math/0412336.
3. F. Peherstorfer, *Zeros of polynomials orthogonal on several intervals*, arXiv:math-ph/0203058, https://arxiv.org/abs/math-ph/0203058.
4. F. Peherstorfer, *On Bernstein–Szegö orthogonal polynomials on several intervals. II. Orthogonal polynomials with periodic recurrence coefficients*, J. Approx. Theory 64 (1991), 123–161, doi:10.1016/0021-9045(91)90071-H (bibliographic information only; complete text not obtained).
5. F. Peherstorfer, *On the Zeros of Orthogonal Polynomials: The Elliptic Case*, Constructive Approximation 20 (2004), 377–397, doi:10.1007/s00365-004-0566-5 (abstract inspected; complete text not obtained).
