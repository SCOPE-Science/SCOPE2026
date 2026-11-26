# Critical-window crossover for a one-defect cyclic weighted shift

## Finding

Let \(n\ge3\), \(r\ge0\), and let \(T_n(r)\) be the complex \(n\)-dimensional cyclic weighted shift with all forward weights equal to \(1\), except the wraparound weight \(r\). Write
\[
 w_n(r)=\sup_{\|z\|_2=1}|\langle T_n(r)z,z\rangle|.
\]
Its **sharp defect crossover** occurs on the scale \(r=1+a/n\). For every fixed real \(a\), with \(r>0\) when necessary,
\[
 \lim_{n\to\infty}n^2\bigl(w_n(1+a/n)-1\bigr)=F(a),
\]
where
\[
 F(a)=\begin{cases}
 -z_a^2/2,&a<0,\quad z_a\in(0,\pi),\ z_a\tan(z_a/2)=-a,\\
 0,&a=0,\\
 y_a^2/2,&a>0,\quad y_a>0,\ y_a\tanh(y_a/2)=a.
 \end{cases}
\]
Each displayed scalar equation has exactly one root in the stated interval. Thus the limit is explicit and nontrivial on both sides of the bond-strength threshold; there is no discontinuity at \(a=0\).

The same theorem gives exact finite-size normalization and the two fixed-strength limits. For \(0\le r<1\), let \(\theta_n(r)\in(0,\pi/(n+1)]\) be the unique solution of
\[
 \cos\!\left(\frac{n+1}{2}\theta\right)=r\cos\!\left(\frac{n-1}{2}\theta\right).
\]
Then \(w_n(r)=\cos\theta_n(r)<1\) and, for fixed \(r<1\),
\[
 w_n(r)=1-\frac{\pi^2}{2\bigl(n+(1+r)/(1-r)\bigr)^2}+O_r(n^{-4}).
\]
For \(r=1\), \(w_n(1)=1\) exactly. For \(r>1\), let \(\eta_n(r)>0\) be the unique solution of
\[
 \cosh\!\left(\frac{n+1}{2}\eta\right)=r\cosh\!\left(\frac{n-1}{2}\eta\right).
\]
Then \(w_n(r)=\cosh\eta_n(r)>1\), and for every fixed \(r>1\),
\[
 w_n(r)=\frac{r+r^{-1}}2+\frac{(r^2-1)^2}{2r^{n+2}}+O_r(nr^{-2n}).
\]
For each fixed \(r<1\), \(w_n(r)\) increases strictly with \(n\); for each \(r>1\), it decreases strictly. The unperturbed value is independent of \(n\).

## Assumptions and scope

The Hilbert-space numerical radius uses the standard complex inner product and unit \(\ell_2\) norm. The shift is a directed single cycle of length \(n\ge3\), with nonnegative real weights \(1,\ldots,1,r\). Changing the position of the exceptional edge is a unitary permutation; the result makes no claim about arbitrary sign phases in general multisite perturbations. The notation \(O_r\) means the implicit constant may depend on the fixed positive parameter \(r\); the critical-window formula is a separate limit with \(a\) fixed. The only role of sequences of orders is the ordinary limit through all positive integers.

## Proof

**1. Perron reduction.** For a unit vector \(z\in\mathbb C^n\) set \(u_j=|z_j|\). The triangle inequality gives
\[
 |\langle T_n(r)z,z\rangle|\le\sum_{j=0}^{n-2}u_ju_{j+1}+ru_0u_{n-1}=\frac12 u^\mathsf{T}B_n(r)u,
\]
where \(B_n(r)\) is the real symmetric cycle adjacency matrix with the one exceptional edge of weight \(r\). Taking a nonnegative Perron eigenvector gives equality. Hence \(w_n(r)=\lambda_{\max}(B_n(r))/2\). This also holds at \(r=0\), because the remaining path is connected.

**2. Exact Perron eigenvalues.** Reflection across the distinguished bond preserves \(B_n(r)\), and its strictly positive Perron eigenvector is reflection-symmetric. The interior eigenvalue recurrence is
\[
 x_{j-1}+x_{j+1}=2\omega x_j \quad(1\le j\le n-2),
\]
with \(x_0=x_{n-1}>0\) and \(2\omega x_0=rx_{n-1}+x_1\). For \(r<1\), entrywise Perron monotonicity relative to the ordinary cycle gives \(\omega<1\), so write \(\omega=\cos\theta\). A positive reflection-symmetric solution is
\[
 x_j=\cos\!\left((n-1-2j)\theta/2\right).
\]
The boundary equation reduces to the displayed cosine equation. On \((0,\pi/(n+1)]\), its ratio of left- to right-hand cosine is strictly decreasing from \(1\) to \(0\), so the solution is unique and every component is positive. This proves the exact formula, including \(r=0\). For \(r>1\), Perron monotonicity instead gives \(\omega>1\); writing \(\omega=\cosh\eta\) gives a positive solution
\[
 x_j=\cosh\!\left((n-1-2j)\eta/2\right),
\]
with the displayed hyperbolic equation. Its cosine-hyperbolic ratio increases strictly from \(1\) to infinity, so the solution is unique. The case \(r=1\) is the ordinary cycle with Perron eigenvalue \(2\).

**3. Fixed strengths and strict finite-size monotonicity.** For \(0\le r<1\), put \(\alpha=(1+r)/(1-r)\). The trigonometric boundary equation is equivalent to
\[
 n\theta+2\arctan\bigl(\alpha\tan(\theta/2)\bigr)=\pi.
\]
For fixed \(r\), \(\theta=O(n^{-1})\), and expansion gives \(\theta=\pi/(n+\alpha)+O_r(n^{-4})\). Expanding the cosine yields the claimed \(O_r(n^{-4})\) approximation. The left-hand side is strictly increasing in both \(n\) and \(\theta\), so \(\theta\) strictly decreases with \(n\) and \(w_n(r)\) strictly increases.

For \(r>1\) put \(q_n=e^{\eta_n}>1\). The hyperbolic boundary equation is exactly
\[
 q_n-r=(rq_n-1)q_n^{-n}.
\]
It follows that \(q_n>r\) and \(q_n\to r\). The implicit equation, uniformly near fixed \(r>1\), gives
\[
 q_n-r=(r^2-1)r^{-n}+O_r(nr^{-2n}).
\]
Using \(w_n=(q_n+q_n^{-1})/2\) proves the exponential correction. At fixed \(\eta>0\), the ratio \(\cosh((n+1)\eta/2)/\cosh((n-1)\eta/2)\) strictly increases with \(n\); since it increases with \(\eta\), the solution \(\eta_n\) strictly decreases, as does \(w_n\).

**4. The critical window.** Fix \(a<0\), set \(r_n=1+a/n\) for sufficiently large \(n\), and put \(z_n=n\theta_n(r_n)\in(0,\pi)\). The exact boundary equation becomes
\[
 1+\frac an=\frac{\cos((1+1/n)z_n/2)}{\cos((1-1/n)z_n/2)}.
\]
The right-hand ratio is monotone in \(z_n\), and its scaled difference from \(1\) tends uniformly on compact subsets of \((0,\pi)\) to \(-z\tan(z/2)\). Because this continuous function strictly decreases from \(0\) to \(-\infty\), monotone root convergence yields \(z_n\to z_a\). Therefore
\[
 n^2(\cos(z_n/n)-1)\to-z_a^2/2.
\]
For \(a>0\), put \(y_n=n\eta_n(r_n)\). The corresponding equation is
\[
 1+\frac an=\frac{\cosh((1+1/n)y_n/2)}{\cosh((1-1/n)y_n/2)}.
\]
Its scaled difference from \(1\) tends uniformly on compact sets to \(y\tanh(y/2)\), a continuous strictly increasing map of \([0,\infty)\) onto itself. Monotone root convergence gives \(y_n\to y_a\) and \(n^2(\cosh(y_n/n)-1)\to y_a^2/2\). At \(a=0\), the numerical radius equals one for every \(n\). This completes all cases and quantifiers.

## Verification

The standalone script `check_cyclic_shift.py` checks the symbolic characteristic-polynomial identity for small sizes, compares the claimed finite-root formulas against independently diagonalized matrices, and evaluates the signed critical-window limits at two substantial dimensions using high-precision arithmetic. Run `python check_cyclic_shift.py` with NumPy, SciPy, SymPy and mpmath available. The script's finite checks are not used to justify infinite convergence or novelty.

## Relationship to prior work

Chien, Kirkland, Li, and Nakazato (arXiv:2304.06050, first version April 12, 2023) treat numerical ranges of general weighted cyclic shifts, including their determinant characterization and permutation comparisons. These methods cover the Perron reduction and can recover a finite-dimensional characteristic polynomial; those elementary ingredients are *not* claimed as independently new. The result here is the three-sided, sharp \(1/n\) defect-strength crossover for the numerical radius, together with the different fixed-strength finite-size laws and their leading corrections. Chang and Wang (2012) likewise analyze permutations of cyclic weights, not a stated defect critical-window limit. Grudsky, Maximenko, and Soto-González (arXiv:2308.07514, 2023) analyze eigenvalues of **weighted cycle Laplacians**, whose defect also changes the diagonal entries, unlike the Hermitian part of the cyclic shift here. Their spectral asymptotics do not by themselves give this numerical-radius crossover. The comparison is qualified: an equivalent earlier spectral-edge scaling may exist under periodic-Jacobi or defect-state terminology.

## Limitations

There is no claim about arbitrary multiple defects, the full numerical-range boundary, nonlinear \(\ell_p\) numerical radii, or uniform error bounds as the fixed strength approaches \(1\) faster than the investigated scaling. The finite-size characteristic equation is elementary and was accessible in the earlier general determinant framework; scientific novelty is restricted to the sharp critical crossover and its coordinated asymptotic regimes. No independent mathematical audit has been performed.

## References

1. M.-T. Chien, S. Kirkland, C.-K. Li and H. Nakazato, *Numerical ranges of cyclic shift matrices*, arXiv:2304.06050 (first submitted 2023-04-12), https://arxiv.org/abs/2304.06050.
2. C.-T. Chang and K.-Z. Wang, *Maximizing numerical radii of weighted shifts under weight permutations*, J. Math. Anal. Appl. **394** (2012), 592–602, doi:10.1016/j.jmaa.2012.04.039.
3. S. M. Grudsky, E. A. Maximenko and A. Soto-González, *Eigenvalues of laplacian matrices of the cycles with one negative-weighted edge*, arXiv:2308.07514 (first submitted 2023-08-15), https://arxiv.org/abs/2308.07514.
4. P. Gorkin and J. R. Partington, *Norms of truncated Toeplitz operators and numerical radii of restricted shifts*, Comput. Methods Funct. Theory **19** (2019), 487–508, doi:10.1007/s40315-019-00282-z.
