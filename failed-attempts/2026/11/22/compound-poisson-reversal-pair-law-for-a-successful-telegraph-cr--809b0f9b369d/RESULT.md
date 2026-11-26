# Compound-Poisson reversal-pair law for a successful telegraph crossing

## Finding
Consider a one-dimensional persistent particle moving at constant velocity \(+v\) or \(-v\), with velocity reversals at rate \(\gamma>0\). It is killed upon outward contact with either endpoint of \([0,L]\), \(L>0\), and starts at the left endpoint with **inward** orientation \(+v\). Let \(S\) be the event of absorption at the right endpoint, \(N\) the number of velocity reversals before absorption, and \(c=\gamma L/v>0\). Then \(\Pr(S)=(1+c)^{-1}\), and \(N\) is even on \(S\). For \(M=N/2\) conditioned on \(S\), the probability-generating function is, for \(0\le q\le1\),

\[
H_c(q)=\mathbb E[q^M\mid S]=\frac{1+c}{\cosh(c\sqrt{1-q})+\sinh(c\sqrt{1-q})/\sqrt{1-q}},
\]

with the continuous value \(H_c(1)=1\). If \(\xi_n(c)\), \(n\ge1\), is the unique root of
\[
\xi\cos\xi+c\sin\xi=0,\qquad (n-\tfrac12)\pi<\xi<n\pi,
\]
then \(M\) is equal in distribution to an almost surely finite sum of independent geometric variables \(G_n\), with
\[
\Pr(G_n=j)=p_n(1-p_n)^j,\quad j\in\{0,1,\ldots\},\qquad p_n=\frac{\xi_n^2}{\xi_n^2+c^2}.
\]
In particular, \(M\) is compound Poisson. Its jump intensity and positive-integer jump Lévy measure are exactly
\[
\Lambda_c=c-\log(1+c),\qquad
\nu_c(k)=\frac1k\sum_{n\ge1}\left(\frac{c^2}{c^2+\xi_n(c)^2}\right)^k\quad (k=1,2,\ldots),
\]
where \(\sum_{k\ge1}\nu_c(k)=\Lambda_c\). Its first two moments and zero probability are
\[
\mathbb EM=\frac{c^2(c+3)}{6(c+1)},\qquad
\operatorname{Var}(M)=\frac{c^2(c^4+6c^3+30c^2+60c+45)}{90(c+1)^2},\qquad
\Pr(M=0)=(1+c)e^{-c}.
\]
In the long-interval/short-persistence limit \(c\to\infty\),
\[
\frac{M}{c^2}\Rightarrow Z,\qquad
\mathbb E[e^{-sZ}]=\frac{\sqrt{s}}{\sinh\sqrt{s}}\quad(s\ge0),
\]
where the limit is the convergent sum of independent exponential variables with rates \((n\pi)^2\), \(n\ge1\). Thus \(\mathbb EZ=1/6\), \(\operatorname{Var}(Z)=1/90\). This is a distributional limit, not a Gaussian approximation.

## Assumptions and scope
Velocity is piecewise constant, switching instantly between exactly two signs with homogeneous independent exponential holding times of rate \(\gamma\). There is no translational Brownian noise, no reflection, no wall residence, and no additional event counted as a reversal. Outward contacts \((0,-v)\) and \((L,+v)\) are absorbing. The inward initial state \((0,+v)\) is *not* absorbed at time zero. The crossing event \(S\) has positive probability for every \(c>0\). The count \(N\) excludes absorption itself and includes every interior sign switch. The result concerns the law of reversals conditioned on right absorption and does not give a full joint law with the physical crossing time.

## Proof
Rescale position to \(y=\gamma x/v\in[0,c]\). For \(0\le z\le1\), define \(f_\pm(y;z)=\mathbb E_{(y,\pm)}[z^N\mathbf1_S]\). The backward equations and kinetic absorbing boundary conditions are
\[
\partial_y\begin{pmatrix}f_+\\f_-\end{pmatrix}=A_z\begin{pmatrix}f_+\\f_-\end{pmatrix},\qquad
A_z=\begin{pmatrix}1&-z\\z&-1\end{pmatrix},\qquad f_-(0;z)=0,\quad f_+(c;z)=1.
\]
These equations follow from the first-event expansion: at each interior point the hazard of reversal per unit distance is \(\gamma/v\), and a reversal earns a factor \(z\). Since \(A_z^2=(1-z^2)I\), the matrix exponential gives
\[
f_+(0;z)=\left[\cosh(c\sqrt{1-z^2})+\frac{\sinh(c\sqrt{1-z^2})}{\sqrt{1-z^2}}\right]^{-1}.
\]
At \(z=1\), this equals \(1/(1+c)\). On a successful exit, the initial and final velocities are both positive, so exactly an even number of sign changes occurred. Put \(q=z^2\); dividing by \(\Pr(S)\) yields the asserted \(H_c\), including the two boundary values by continuity.

For the product formula, define the entire function
\[
F_c(s)=\cosh(c\sqrt s)+\frac{\sinh(c\sqrt s)}{\sqrt s},\qquad F_c(0)=1+c.
\]
It is the value at \(c\) of the unique solution to \(u''=su\), \(u(0)=u'(0)=1\). Its zeros are \(-r_n^2\), the eigenvalues of the regular self-adjoint Robin–Dirichlet problem \(-u''=r^2u\), \(u'(0)=u(0)\), \(u(c)=0\). The quadratic form \(\int_0^c|u'|^2dy+|u(0)|^2\) is strictly positive, so all spectral parameters \(r_n^2\) are positive. Separation of solutions shows that \(\xi_n=cr_n\) is the unique root in \(((n-1/2)\pi,n\pi)\); these eigenvalues are simple. Because \(F_c\) is entire of order at most \(1/2\) and \(r_n\asymp n\), its genus-zero Hadamard factorization (with the normalization at zero) is
\[
F_c(s)=(1+c)\prod_{n=1}^{\infty}\left(1+\frac{s}{r_n^2}\right).
\]
Therefore
\[
H_c(q)=\prod_{n=1}^{\infty}\frac{r_n^2}{r_n^2+1-q}
=\prod_{n=1}^{\infty}\frac{p_n}{1-(1-p_n)q},\qquad p_n=\frac{r_n^2}{1+r_n^2}.
\]
Each factor is the generating function of a nonnegative geometric variable. Moreover \(\sum_n\mathbb EG_n=\sum_n r_n^{-2}<\infty\), so their independent sum is finite almost surely and has the displayed law.

Write \(a_n=1-p_n\). Expansion of the logarithm, absolutely convergent for \(|q|\le1\) after grouping at \(q=1\), yields
\[
\log H_c(q)=\sum_{k\ge1}(q^k-1)\frac1k\sum_{n\ge1}a_n^k.
\]
This is the probability-generating exponent of a compound-Poisson integer-valued law with Lévy mass \(\nu_c(k)\). Its total mass is \(-\log H_c(0)=c-\log(1+c)\), because \(F_c(1)=\cosh c+\sinh c=e^c\). Expanding \(F_c(s)\) near \(s=0\) gives
\[
F_c(s)=1+c+\left(\frac{c^2}{2}+\frac{c^3}{6}\right)s+\left(\frac{c^4}{24}+\frac{c^5}{120}\right)s^2+O(s^3).
\]
Differentiating \(H_c(q)=F_c(0)/F_c(1-q)\) once and twice at \(q=1\) gives the stated mean and variance, while \(H_c(0)=(1+c)e^{-c}\).

Finally, for fixed \(s\ge0\), put \(q=e^{-s/c^2}\). Then \(c\sqrt{1-q}\to\sqrt s\), while \(\sqrt{1-q}\sim\sqrt s/c\). Thus
\[
H_c(e^{-s/c^2})\longrightarrow\frac{\sqrt s}{\sinh\sqrt s}.
\]
The continuous limit is a valid Laplace transform: Euler's product for \(\sinh\) writes it as \(\prod_{n\ge1}(1+s/(n\pi)^2)^{-1}\), the transform of the independent exponential sum. The continuity theorem for Laplace transforms establishes weak convergence. Summing \(\sum(n\pi)^{-2}=1/6\) and \(\sum(n\pi)^{-4}=1/90\) proves the two limit moments independently; the exact finite-\(c\) moment expressions have the same scaled limits.

## Verification
The standalone file `check_reversal_pairs.py` tests the finite-interval backward formula against the geometric spectral product and the small-parameter derivative formulas, verifies root intervals and the continuous scaling limit, and independently samples spatial flights to check success and reversal-count moments. The random checks have specified tolerances and are corroborative, not the proof. The analytic proof above covers all real \(c>0\) and every nonnegative integer reversal-pair count.

## Relationship to prior work
Monthus (arXiv:2611.18270, 13 November 2026) developed exact spatial run-and-tumble extrema kernels and their invariance under fixed switching-rate-to-speed ratios; it includes zero-scale ballistic bond distributions and physical-time extensions but does not state the conditioned two-trap reversal-pair compound-Poisson or Robin-spectrum law. Masoliver, Porrà and Weiss (1992) studied propagation and absorption between two traps, but their position/time propagator does not identify this count decomposition. Cinque and Orsingher (2020) derived distributions of the telegraph maximum conditioned on a fixed total number of reversals by observation time, which is a different conditioning. Foong and Kanno (1994) obtained first-passage distributions resolved by reversal number, a closely related general technique and a significant possible implicit source of the present generating function; their complete original text was not available for direct comparison. The product, compound-Poisson representation and its explicit \(c^2\)-scaling law are the specific contribution claimed here, not first-passage or switching-count methodology in general.

## Limitations
The result does not cover asymmetric speeds or switching rates, diffusive positional noise, sticky walls, partial absorption, or a process launched at the boundary with outward velocity. It does not determine physical crossing-time statistics, which depend separately on \(v\) and \(\gamma\). At finite large \(c\) the success event has probability \((1+c)^{-1}\), so direct rare-event sampling can be costly. Although an independently derived structural identity is given, complete publication-priority verification against some older restricted-access full texts remains unresolved.

## References
1. C. Monthus, *Real-Space-RG for the drawups and drawdowns of run-and-tumble trajectories: universality classes for models with space-dependent velocities and switching rates*, arXiv:2611.18270v1, first submitted 13 November 2026. https://arxiv.org/html/2611.18270v1
2. J. Masoliver, J. M. Porrà, and G. H. Weiss, *Solutions of the telegrapher's equation in the presence of traps*, Physical Review A 45, 2222–2227 (1992), with published erratum. https://doi.org/10.1103/PhysRevA.45.2222
3. S. K. Foong and S. Kanno, *Properties of the telegrapher's random process with or without a trap*, Stochastic Processes and their Applications 53, 147–173 (1994). https://doi.org/10.1016/0304-4149(94)90061-2
4. F. Cinque and E. Orsingher, *On the distribution of the maximum of the telegraph process*, arXiv:2003.04044 (2020). https://arxiv.org/html/2003.04044v1
5. B. Martinucci, P. Paraggio, and S. Zacks, *Some results on the supremum and on the first passage time of the generalized telegraph process*, Advances in Applied Probability 57, 453–491 (2025). https://doi.org/10.1017/apr.2024.49
