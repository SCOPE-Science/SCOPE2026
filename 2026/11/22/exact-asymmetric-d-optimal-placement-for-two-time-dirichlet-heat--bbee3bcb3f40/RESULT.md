# Exact asymmetric D-optimal placement for two-time Dirichlet heat measurements

## Finding
Consider the unit-diffusivity heat equation on the interval \((0,1)\), with homogeneous Dirichlet boundary conditions and initial state restricted to the first two unnormalized sine modes:
\[
 f_0(z)=c_1\sin(\pi z)+c_2\sin(2\pi z),\qquad (c_1,c_2)\in\mathbb R^2.
\]
At time \(0\), observe the scalar field at \(x\in[0,1]\), and at prescribed time \(T>0\) observe it at an independently chosen position \(y\in[0,1]\). Each observation has independent centered Gaussian noise with the same variance \(\sigma^2>0\). Define
\[
 q=e^{-\pi^2T},\qquad k=q^3=e^{-3\pi^2T},\qquad
 w(k)=\frac{4k^2}{1+7k^2+\sqrt{(1+7k^2)^2-48k^4}},
\]
and
\[
 s(k)=\sqrt{\frac{1-2w(k)}{2-3w(k)}},\qquad t(k)=\sqrt{w(k)}.
\]
**Theorem.** For every finite \(T>0\) and \(\sigma^2>0\), the only ordered location choices that maximize the determinant of the Fisher information for \((c_1,c_2)\) are
\[
 (x_*,y_*)=\left(\frac{\arccos s(k)}\pi,\frac{\arccos(-t(k))}\pi\right)
 \quad\text{and}\quad (1-x_*,1-y_*).
\]
In particular, \(0<x_*<1/2<y_*<1\), and \(x_*+y_*<1\) for finite \(T>0\). The maximum information determinant is
\[
 \boxed{\det\mathcal I_{\max}(T)=\frac{4q^2}{\sigma^4}\,
 \frac{(1-w(k))^4}{(1-2w(k))(2-3w(k))^2}.}
\]
As the time separation grows, the earlier site moves strictly from \(\arccos(1/\sqrt3)/\pi\) toward \(1/4\), and the later site moves strictly from \(1-\arccos(1/\sqrt3)/\pi\) toward \(1/2\). Their sharp large-time asymptotics are
\[
 x_*=\frac14+\frac{e^{-6\pi^2T}}{2\pi}+O(e^{-12\pi^2T}),\qquad
 y_*=\frac12+\frac{\sqrt2}{\pi}e^{-3\pi^2T}+O(e^{-9\pi^2T}).
\]
For small positive \(T\), the two sites initially translate in the same direction at equal first-order speed:
\[
 x_*(T)=x_*(0)-\frac{3\pi}{4\sqrt2}T+O(T^2),\qquad
 y_*(T)=y_*(0)-\frac{3\pi}{4\sqrt2}T+O(T^2),
\]
where \(x_*(0)\) and \(y_*(0)\) denote the limits just stated. If the equal-time limiting locations are retained at both observation times, their information determinant is asymptotically smaller than the optimum by the exact factor \(27/16\).

## Assumptions and scope
The parameter coordinates are coefficients of the explicitly given **unnormalized** sine functions. Using orthonormal sine modes rescales every design determinant by a common constant and does not change any location optimizer. The two scalar measurements have equal independent Gaussian noise, each at its stated time; there is one measurement at each time, no additional temporal or spatial observations, no speed or movement-cost constraint, and no prior on the unknown coefficients. Both spatial locations can independently vary throughout the closed unit interval. D-optimality means maximization of \(\det(\sigma^{-2}M^\mathsf TM)\), the determinant of the likelihood Fisher matrix; this is not the smallest-singular-value, condition-number, posterior-risk, or infinite-dimensional PDE optimality criterion.

## Proof
**1. Exact information determinant.** Heat evolution preserves the sine modes with respective decay factors \(q\) and \(q^4\), so the measurement matrix for the two coefficients is
\[
 M(x,y)=\begin{pmatrix}
 \sin(\pi x)&\sin(2\pi x)\\
 q\sin(\pi y)&q^4\sin(2\pi y)
 \end{pmatrix}.
\]
The Fisher matrix is \(\mathcal I=\sigma^{-2}M^\mathsf TM\). Elementary double-angle identities give
\[
 \det M=2q\sin(\pi x)\sin(\pi y)
       \bigl(k\cos(\pi y)-\cos(\pi x)\bigr).
\]
Since \(\det\mathcal I=\sigma^{-4}(\det M)^2\), this is the exact global objective, including singular endpoint and repeated-site designs.

**2. Reduction to one strictly concave maximization.** Set \(z=\cos(\pi x)\), \(v=\cos(\pi y)\), and let \(s=|z|\), \(t=|v|\). The inequality \(|z-kv|\le s+kt\) is an equality for nonzero \(s,t\) exactly when \(z,v\) have opposite signs. Therefore the global problem reduces, without loss or relaxation, to maximizing
\[
 F_k(s,t)=(1-s^2)(1-t^2)(s+kt)^2,
 \qquad 0\le s,t\le1.
\]
It is positive in the interior and vanishes if \(s=1\) or \(t=1\). At \(s=0<t<1\), increasing \(s\) increases the objective, and at \(t=0<s<1\), increasing \(t\) increases it because \(k>0\); the origin has objective zero. Thus any maximizer lies in \((0,1)^2\). On this square,
\[
 \log F_k=\log(1-s^2)+\log(1-t^2)+2\log(s+kt)
\]
is strictly concave: each of the first two summands has strictly negative second derivative in its own coordinate, while the last has negative semidefinite Hessian. Hence there is a unique interior global maximizing pair \((s,t)\).

**3. Closed solution and equality cases.** Vanishing of both derivatives of \(\log F_k\) is equivalent to
\[
 2s^2+kst=1,\qquad st+2kt^2=k.
\]
Write \(w=t^2\). The second equation gives \(st=k(1-2w)\); using this in the first and squaring yields
\[
 s^2=\frac{1-2w}{2-3w},\qquad
 k^2=\frac{w}{(1-2w)(2-3w)}.
\]
The second relation is strictly increasing in \(w\) on \((0,1/3]\), since its derivative is
\[
 \frac{2(1-3w^2)}{(1-2w)^2(2-3w)^2}>0.
\]
It maps \((0,1/3]\) onto \((0,1]\), and its smaller quadratic root is precisely the displayed stable formula for \(w(k)\). This is the unique stationarity solution. Because \(s,t>0\), the original triangle inequality has equality only for \((z,v)=(s,-t)\) or \((-s,t)\). The cosine map is bijective from \([0,1]\) to \([-1,1]\), yielding exactly the two claimed ordered physical designs. Furthermore \(s^2-w=(1-w)(1-3w)/(2-3w)>0\) for \(0<k<1\); hence \(s>t\), which implies \(x_*+y_*<1\).

**4. Sharp value and monotone migration.** Substitution gives \(1-s^2=(1-w)/(2-3w)\), while the stationarity equations give \(s+kt=(1-w)/\sqrt{(1-2w)(2-3w)}\). Thus
\[
 F_k(s,t)=\frac{(1-w)^4}{(1-2w)(2-3w)^2},
\]
which, multiplied by \(4q^2/\sigma^4\), proves the stated maximum. The strictly increasing map \(w\mapsto k\) makes \(t=\sqrt w\) strictly increasing with \(k\). As \(s^2=(1-2w)/(2-3w)\) has derivative \(-1/(2-3w)^2<0\) in \(w\), \(s\) strictly decreases with \(k\). Since \(k=e^{-3\pi^2T}\) decreases with \(T\), the indicated physical positions move monotonically as stated.

**5. Endpoint laws and information advantage.** The quadratic root gives \(w=2k^2-14k^4+O(k^6)\) as \(k\downarrow0\). Expanding the square roots and inverse cosines yields
\[
 s=\frac1{\sqrt2}-\frac{k^2}{2\sqrt2}+O(k^4),\quad
 t=\sqrt2 k+O(k^3),\quad
 x_*=\frac14+\frac{k^2}{2\pi}+O(k^4),\quad
 y_*=\frac12+\frac{\sqrt2k}{\pi}+O(k^3).
\]
For \(k\uparrow1\), \(w\to1/3\), \(s,t\to1/\sqrt3\). Implicit differentiation of the scalar equation at \(k=1\) gives \(w'(1)=1/6\), \(s'(1)=-\sqrt3/12\), and \(t'(1)=\sqrt3/12\). The inverse-cosine chain rule and \(k'(0)=-3\pi^2\) yield the short-time formulas.

Finally, fixed equal-time optimal locations use \(\cos(\pi x)=1/\sqrt3\), \(\cos(\pi y)=-1/\sqrt3\). Their determinant squared, as \(q\downarrow0\), is asymptotic to \(16q^2/27\), whereas the newly optimized determinant squared is asymptotic to \(q^2\). Their information-determinant ratio is consequently \(27/16\), independent of noise variance. All boundary cases were already covered by Step 2.

## Verification
`CHECK.py` is a Python-standard-library-only supplementary verifier. It directly assembles the two rows of the physical heat measurement matrix, checks the exact information determinant and both independent stationarity identities, exhaustively compares \(81^2\) location grid pairs for each of nine time-decay ratios, and additionally compares \(10^4\) random unrestricted location pairs for each ratio. It checks reflection, endpoint asymptotics and the static-design information ratio. Replaying it from the delivered package prints `HEAT_TWO_TIME_DESIGN_PASS 149121`. All numerical comparisons are finite supplementary checks. Global optimality, equality characterization, and asymptotic orders are proved analytically above, not inferred from the checks.

## Relationship to prior work
Aldroubi and collaborators (2020) establish stable space-time sampling and heat-flow reconstruction results on bandlimited function spaces, with Vandermonde and frame estimates, but do not determine this two-temporal-point Dirichlet Fisher determinant optimizer. Alexanderian and Saibaba (2017) develop scalable D-optimal experiment-design algorithms for general PDE inverse problems, rather than an explicit two-mode, two-time location classification. Cheng and Paley (2021) optimize mobile sensor paths for a diffusion-advection system with a Kalman covariance-plus-motion objective; that objective and its constraints differ from the present exact finite-dimensional likelihood determinant. Huang, Needell and Tang (2021) prove randomized graph dynamical-sampling stability bounds. Closely related public finite-cycle two-sensor heat results optimize the least singular value, not the Fisher determinant of two temporally staggered measurements with individually chosen locations. General D-optimality definitions and two-by-two determinant identities are background, not claimed as discoveries.

## Limitations
The theorem solves only the two-mode Dirichlet model with exactly two snapshots, fixed earlier and later observation times, freely chosen continuous positions, equal independent noise, and the Fisher determinant objective. A result for two retained heat modes need not transfer to the full heat equation or arbitrary sensor/parameter priors. If sensor movement must obey a speed bound, these optimizers might be infeasible. Maximizing determinant does not guarantee optimal worst-direction reconstruction error, trace posterior risk, or practical reconstruction performance. A historically equivalent special design in older thermal-sensing literature is possible; publication priority and the analytical proof have not received independent validation.

## References
- A. Alexanderian and A. K. Saibaba, *Efficient D-optimal design of experiments for infinite-dimensional Bayesian linear inverse problems*, first posted 2017-11-16, https://arxiv.org/abs/1711.05878.
- A. Aldroubi, K. Gröchenig, L. Huang, P. Jaming, I. Krishtal, and J. L. Romero, *Sampling the flow of a bandlimited function*, first posted 2020-04-29, https://arxiv.org/abs/2004.14032.
- L. Huang, D. Needell, and S. Tang, *Robust recovery of bandlimited graph signals via randomized dynamical sampling*, first posted 2021-09-28, https://arxiv.org/abs/2109.14079.
- S. Cheng and D. A. Paley, *Optimal guidance and estimation of a 2D diffusion-advection process by a team of mobile sensors*, first posted 2021-11-02, https://arxiv.org/abs/2111.01343.
