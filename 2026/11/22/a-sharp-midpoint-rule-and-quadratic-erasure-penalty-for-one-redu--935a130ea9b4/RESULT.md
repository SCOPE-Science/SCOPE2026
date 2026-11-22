# A sharp midpoint rule and quadratic erasure penalty for one redundant Fourier sample

## Finding

Fix an integer \(N\ge2\). In the complex Fourier space of polynomials \(p(z)=\sum_{k=0}^{N-1}c_kz^k\), normalize each unit-circle sample to be the row
\[
v_N(t)=N^{-1/2}\bigl(e^{2\pi i kt/N}\bigr)_{k=0}^{N-1},\qquad t\in\mathbb R/N\mathbb Z.
\]
Keep all \(N\) critical samples at \(t=0,1,\ldots,N-1\), and add exactly one new sample at \(t\), distinct from the existing nodes. Let \(F_{N,t}^{(-j)}\) be the square matrix left after deleting any one of the \(N+1\) sample rows. Define the adversarial one-erasure lower squared singular value
\[
B_N(t)=\min_{0\le j\le N}\sigma_{\min}^2\bigl(F_{N,t}^{(-j)}\bigr),
\]
where \(j=N\) means deleting the extra row.

**Theorem.** Among all locations of the single additional sample, \(B_N(t)\) is maximized uniquely at the midpoint of any gap of the original grid (up to rotation by an integer). With
\[
\eta_N=\begin{cases}1,&N\text{ odd},\\
\cos\bigl(\pi/(2N)\bigr),&N\text{ even},\end{cases}
\qquad \gamma_N=\frac1{N\eta_N},
\]
the exact optimal guarantee and optimal worst-erasure spectral condition number are
\[
\boxed{\max_t B_N(t)=1-\sqrt{1-\gamma_N^2}},\qquad
\boxed{\kappa_N^*=\sqrt{\frac{1+\sqrt{1-\gamma_N^2}}{1-\sqrt{1-\gamma_N^2}}}}.
\]
Every non-grid extra position gives recovery after any single erasure; grid positions fail for at least one erasure. The sharp large-size laws are
\[
\max_t B_N(t)=\frac{1}{2N^2}+O(N^{-4}),\qquad \kappa_N^*=2N+O(N^{-1}).
\]
For comparison, if *all* sample locations may be changed, taking \(N+1\) equally spaced points yields a worst-erasure lower squared singular value exactly \(1/N\). Thus preserving the original critical grid imposes an asymptotic factor \(2N\) in the lower-bound comparison, despite adding the same single redundant sample.

## Assumptions and scope

All sample measurements are equally weighted and have row norm one. The Fourier frequencies are the \(N\) consecutive integers \(0,\ldots,N-1\), and the original \(N\) nodes are immovable. A single adversarial erasure may remove any original sample or the extra one; locations of the erasure are known when reconstructing. The optimization is over the one additional unit-circle point only. The Fourier coefficients and erasure noise may be arbitrary complex numbers. No claim about optimality over unequal weights, other frequency sets, or more than one redundant sample is made.

## Proof

**1. Rank-two spectrum after one erasure.** The rows \(u_j=v_N(j)\), \(0\le j<N\), form an orthonormal basis of \(\mathbb C^N\). Write the additional unit row \(w=v_N(t)\) and \(a_j=\langle w,u_j\rangle\), with the convention of row inner products. Deleting an original row \(u_j\) leaves the \(N-1\) other orthonormal rows and \(w\). Its row Gram matrix has eigenvalues
\[
1+\sqrt{1-|a_j|^2},\quad 1-\sqrt{1-|a_j|^2},
\quad\text{and }1\text{ with multiplicity }N-2.
\]
Indeed the off-diagonal correlation column has squared norm \(\sum_{\ell\ne j}|a_\ell|^2=1-|a_j|^2\), by Parseval. Deleting \(w\) leaves the unitary original Fourier matrix. Hence, putting \(g_N(t)=\min_{0\le j<N}|a_j|\),
\[
B_N(t)=1-\sqrt{1-g_N(t)^2}.
\]
The same formulas give the condition number, and show that every one-erasure square system is invertible exactly when every \(a_j\ne0\).

**2. Dirichlet coefficient and reduction to a gap.** The geometric sum gives
\[
|a_j|=\frac{\left|\sin\bigl(\pi(t-j)\bigr)\right|}{N\left|\sin\bigl(\pi(t-j)/N\bigr)\right|}.
\]
A shift by an integer permutes the original sample rows, and reflection preserves singular values. Therefore it is enough to take \(0<t\le1/2\). Here the numerator is \(\sin(\pi t)\), independent of \(j\). Maximizing the denominator over \(j=0,\ldots,N-1\) yields exactly
\[
g_N(t)=\begin{cases}
\displaystyle\frac{\sin(\pi t)}{N\cos(\pi t/N)},&N\text{ even},\\[6pt]
\displaystyle\frac{\sin(\pi t)}{N\cos\bigl(\pi(1/2-t)/N\bigr)},&N\text{ odd}.
\end{cases}
\]
For even \(N=2m\), the maximizing denominator occurs at \(j=m\). For odd \(N=2m+1\), it occurs at \(j=m+1\). This follows by choosing the available grid point with angular difference nearest a half-period, including the circular wrap-around.

**3. Unique geometric optimum.** In the even case, the logarithmic derivative of \(g_N(t)\) on \(0<t<1/2\) equals
\[
\pi\cot(\pi t)+\frac\pi N\tan(\pi t/N)>0.
\]
In the odd case, with \(x=1/2-t\), the quantity proportional to \(g_N\) is \(\cos(\pi x)/\cos(\pi x/N)\). Its logarithmic derivative in \(x\) is
\[
-\pi\tan(\pi x)+\frac\pi N\tan(\pi x/N)<0,
\]
for \(0<x<1/2\). Thus \(g_N(t)\) increases strictly up to \(t=1/2\) in each case. Reflection and rotation give the claimed unique optimizer in every original gap. Substitution gives \(g_N(1/2)=\gamma_N\). Since the map \(s\mapsto1-\sqrt{1-s^2}\) is strictly increasing on \([0,1]\), this proves the optimal lower bound and the condition-number formula.

**4. Erasure recovery and comparison.** In the original Fourier row basis, the new evaluation is \(y_t=\sum_{\ell=0}^{N-1}a_\ell y_\ell\). If the erased original datum is at \(j\), it is recovered explicitly by
\[
y_j=\frac{y_t-\sum_{\ell\ne j}a_\ell y_\ell}{a_j},
\]
and the inverse Fourier transform then recovers the coefficients. All \(a_j\) are nonzero for non-grid \(t\). At a grid location, the new sample duplicates an original one, so removing a different original point loses rank. The expansions of the sharp formulas follow from \(\gamma_N=N^{-1}+O(N^{-3})\) and \(1-\sqrt{1-x}=x/2+O(x^2)\). For \(N+1\) uniformly spaced rows \(\tilde v(j)=N^{-1/2}(e^{2\pi i kj/(N+1)})_{k=0}^{N-1}\), their complete Gram operator is \((N+1)I/N\); deleting any one row subtracts a unit-rank projector and leaves minimum eigenvalue \(1/N\). This completes the comparison.

## Verification

A standalone program, `check.py`, constructs the actual complex nonuniform Fourier matrices for \(2\le N\le34\), compares all one-erasure eigenvalues with the exact two-outlier formula at eight distinct fractional offsets, verifies the worst-erasure equality, and checks strict midpoint optimality against 49 offsets in each half-gap. It passed 6,930 independent numerical assertions. These checks are finite corroboration; the theorem for every integer \(N\ge2\) follows from the analytic proof above.

## Relationship to prior work

Yu and Townsend (2022, arXiv:2202.04722) analyze arbitrary perturbations of Fourier grids and the stability of an oversampled nonuniform discrete Fourier transform. Their full paper's Sections 2 and 6 give broad frame inequalities rather than an adversarial one-erasure optimum with exactly one additional point. Kunis, Nagel, and Strotmann (2021, arXiv:2103.08167) prove separation-based multivariate Vandermonde stability bounds, and Kunis and Nagel (2020) analyze conditions with nearly colliding node pairs; the latter's full article treats bounds, not the complete fixed-grid-plus-one sampling geometry. General erasure-robust-frame results provide conceptual context but do not yield the sharp midpoint rule or its odd/even constants in the inspected material.

## Limitations

The finding addresses one extra *equal-weight* point, one lost sample, consecutive frequencies, and a frozen Fourier grid. It does not assert an unrestricted optimal frame over all \(N+1\)-point designs; the equispaced regridding calculation is a comparison, not such a universal bound. Finite numerical replay is not a proof. The cited literature comparison supports best-knowledge distinctness only; an unindexed or inaccessible specialization of general frame theory could predate the result. No independent mathematical audit has been performed.

## References

1. A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722v1, first submitted 9 February 2022. https://arxiv.org/html/2202.04722v1
2. S. Kunis, D. Nagel, and A. Strotmann, *Multivariate Vandermonde matrices with separated nodes on the unit circle are stable*, arXiv:2103.08167, first submitted 15 March 2021. https://arxiv.org/abs/2103.08167
3. S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, *Numerical Algorithms* 87 (2021), 473–496, first online 21 July 2020. https://doi.org/10.1007/s11075-020-00974-x
4. A. P. Austin and L. N. Trefethen, *Trigonometric interpolation and quadrature in perturbed points*, arXiv:1612.04018, first submitted 13 December 2016. https://arxiv.org/abs/1612.04018
5. Y. Wang, *Random Matrices and Erasure Robust Frames*, *Journal of Fourier Analysis and Applications* 24 (2018), 1–16. https://doi.org/10.1007/s00041-016-9486-6
