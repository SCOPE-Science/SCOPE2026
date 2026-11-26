# Exact two-tag transient diffusivity on a finite heterogeneous exclusion ring

## Finding

Two distinguishable symmetric exclusion walkers on a finite ring have the same long-time diffusivity. Each tag's instantaneous diffusivity strictly decreases toward that common value and the finite-time diffusivities differ if and only if their microscopic hopping rates differ. At every finite time the ratio of their excess diffusivities above the common limit is the square of the microscopic rate ratio. Each mean-squared displacement is a linear term plus a positive sum of explicit odd reflecting-gap relaxation terms.

Let \(L\ge3\), \(n=L-1\), \(q=a+b\), \(r_1=a\), and \(r_2=b\). Define
\[
D_* = \frac{n-1}{n}\frac{ab}{q},\qquad
\theta_m=\frac{m\pi}{2n},\qquad
\lambda_m=4q\sin^2\theta_m.
\]
For every \(t\ge0\), \(\mathbb E[X_i(t)]=0\), and
\[
\boxed{\mathbb E[X_i(t)^2]=2D_*t+\left(\frac{r_i}{q}\right)^2
\sum_{\substack{1\le m<n\\m\ \mathrm{odd}}}
\frac{\cos^2\theta_m}{n^2\sin^4\theta_m}(1-e^{-\lambda_m t}).}
\]
Write \(K_i(t)=\tfrac12\tfrac{d}{dt}\mathbb E[X_i(t)^2]\). Then
\[
\boxed{\ K_i(t)>D_*,\qquad K_i'(t)<0,\qquad
\frac{K_1(t)-D_*}{K_2(t)-D_*}=\left(\frac ab\right)^2\ }
\qquad(0\le t<\infty).
\]
The derivatives at zero are right derivatives. The endpoints and finite-size intercept are
\[
K_i(0)=\frac{n-1}{n}r_i,\qquad
\lim_{t\to\infty}K_i(t)=D_*,\qquad
\lim_{t\to\infty}\bigl(\mathbb E[X_i(t)^2]-2D_*t\bigr)
=\left(\frac{r_i}{q}\right)^2\frac{n^2-1}{6}.
\]
For every strictly positive rate pair, the common slowest relaxation exponent is \(4q\sin^2(\pi/(2n))\).

## Assumptions and scope

The space is the cycle \(\mathbb Z/L\mathbb Z\), with integer \(L\ge3\). Exactly two distinguishable walkers occupy different sites. In continuous time, walker 1 independently attempts to hop one site clockwise and anticlockwise at rate \(a>0\) for each direction; walker 2 does likewise at rate \(b>0\) per direction. A jump into an occupied site is rejected. Initial labeled positions are uniform over the \(L(L-1)\) ordered distinct-site pairs, the reversible stationary measure. Each \(X_i(t)\) is the unwrapped clockwise-minus-anticlockwise successful hop count after time zero, not a position modulo \(L\).

## Proof

**Reflecting gap.** Let \(G_t\in\{1,\ldots,n\}\) be the clockwise gap from walker 1 to walker 2 modulo \(L\). Its generator is
\[
(Qf)(k)=q\mathbf 1_{k>1}(f(k-1)-f(k))
+q\mathbf 1_{k<n}(f(k+1)-f(k)).
\]
The invariant law \(\pi\) is uniform, and the initial gap has this law. The drift of tag \(i\) at gap \(k\) is \(g_i(k)=s_i r_i(\mathbf 1_{k=n}-\mathbf 1_{k=1})\), where \(s_1=1,s_2=-1\). The squared-jump activity has stationary mean \(2r_i(n-1)/n\). Since \(\langle g_i,1\rangle_\pi=0\), the mean displacement vanishes.

**Poisson corrector and second moment.** The function \(u_i(k)=s_i(r_i/q)(k-(n+1)/2)\) satisfies \(-Qu_i=g_i\), has zero mean, and gives \(\langle g_i,u_i\rangle_\pi=r_i^2(n-1)/(nq)\). Define \(M_i(k,t)=\mathbb E[X_i(t)\mathbf 1_{\{G_t=k\}}]\). Its forward equation is \(\dot M_i=QM_i-g_i/n\) with \(M_i(\cdot,0)=0\): the incoming signed jump current is the negative of the outgoing current under the uniform stationary gap law, by edge reversal of each allowed marked hop. Thus \(M_i=-(I-e^{tQ})u_i/n\). Expanding the square across each marked jump gives
\[
\begin{aligned}
K_i(t)&=\frac{r_i(n-1)}n+\sum_k M_i(k,t)g_i(k)\\
&=\frac{r_i(n-1)}n-\langle g_i,u_i\rangle_\pi+\langle g_i,e^{tQ}u_i\rangle_\pi\\
&=D_*+\langle g_i,e^{tQ}u_i\rangle_\pi.
\end{aligned}
\]

**Odd modes.** An orthonormal nonconstant eigenbasis of \(-Q\) in \(L^2(\pi)\) is
\[
\phi_m(k)=\sqrt2\cos\!\left(\frac{m\pi(k-1/2)}n\right),\quad
\lambda_m=4q\sin^2\theta_m,\quad 1\le m<n.
\]
The opposite endpoint values of \(g_i\) imply zero overlap with even modes, and \(|\langle g_i,\phi_m\rangle_\pi|^2=8r_i^2\cos^2\theta_m/n^2\) for odd \(m\). Expanding \(u_i=(-Q)^{-1}g_i\) on the mean-zero subspace and integrating the expression for \(K_i(t)\) gives the squared-displacement formula. Its coefficient of \(1-e^{-\lambda_m t}\) is \(2|\langle g_i,\phi_m\rangle_\pi|^2/\lambda_m^2\). Every odd-mode coefficient is positive and \(m=1\) exists, even for \(L=3\). Hence the excess is positive, strictly decreasing, and has the stated leading decay. The only tag-dependent factor in the excess is \(r_i^2\), giving equality of finite-time diffusivities precisely at \(a=b\). The initial value follows from the activity since \(M_i(k,0)=0\), and the limit follows from the positive eigenvalues. Finally the intercept equals \(2\langle u_i,u_i\rangle_\pi\), using the same eigenbasis. The variance of the uniform gap is \((n^2-1)/12\), yielding the stated intercept.

## Verification

The accompanying `checker.py` constructs the marked gap transition matrices from individual hopping events. Its independent block-matrix exponential gives the second moments without evaluating the spectral formula, and rational arithmetic checks the Poisson corrector. Run `python checker.py` with Python 3, NumPy and SciPy. It includes equal and unequal rates, ring lengths \(3\) through \(14\) in the floating-point comparisons, and lengths through \(17\) in the rational checks. These finite tests corroborate rather than replace the proof.

## Relationship to prior work

Mason, Jack and Bruna [1] study unequal-species exclusion at dilute/macroscopic scales in dimensions at least two, rather than the finite two-particle lattice spectrum. Ambjörnsson and coauthors [2] study two continuum hard-core particles on the infinite line, with simulations using a reflecting finite interval. Mallmin, du Buisson and Touchette [3] derive long-time currents for reflected Brownian particles on a continuum ring. Their harmonic-mean effective diffusivity matches the structural form of the long-time result, but not the finite-lattice occupancy factor or the tagged transient spectrum. Gupta and coauthors [4] address finite-size tagged correlations in asymmetric homogeneous exclusion. The two-particle activity spectrum in [5] uses the same reflecting gap at equal rates, but its observable counts all accepted hops without signs or labels, and its nonconstant modes are even. The assertion here is the exact stationary two-tag transient on a finite periodic lattice, not a priority claim for the reflecting-gap method or the long-time harmonic mean.

## Limitations

This result is for exactly two walkers, a finite periodic lattice, stationary start, continuous time, and symmetric hopping. It does not extend by this proof to additional particles, driven hopping, open boundaries, nonstationary gaps, or continuous Brownian motion. The constant ratio concerns the excesses, not the entire instantaneous diffusivities. The ratio is well-defined at all finite times, and its limit is \((a/b)^2\); substituting the limiting diffusivities into the ratio would instead give \(0/0\). Historical priority remains qualified by the scope of the literature comparison.

## References

1. J. Mason, R. L. Jack and M. Bruna, *Macroscopic behaviour in a two-species exclusion process via the method of matched asymptotics*, arXiv:2203.01038. https://arxiv.org/abs/2203.01038
2. T. Ambjörnsson, L. Lizana, M. A. Lomholt and R. J. Silbey, *Single-file dynamics with different diffusion constants*, arXiv:0803.2485. https://arxiv.org/abs/0803.2485
3. E. Mallmin, J. du Buisson and H. Touchette, *Large deviations of currents in diffusions with reflective boundaries*, arXiv:2102.04846. https://arxiv.org/abs/2102.04846
4. S. Gupta, S. N. Majumdar, C. Godrèche and M. Barma, *Tagged Particle Correlations in the Asymmetric Simple Exclusion Process: Finite Size Effects*, arXiv:cond-mat/0703464. https://arxiv.org/abs/cond-mat/0703464
5. *A diffusive-time theta crossover for two-particle exclusion activity on a ring*, Resultary, 2026-11-22. https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-diffusive-time-theta-crossover-for-two-particle-exclusion-acti--ef4ea58edfd5/RESULT.md
