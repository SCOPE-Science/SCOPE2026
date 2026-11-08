# Bessel–Dirichlet condensation on the critical constant-weight boundary

## Finding
Let \(w\) be any probability mass function on \(\mathbb N_0\) with a positive exponential moment, let \(\rho_c=\sum_{n\ge0}nw(n)\), and fix \(\theta>0\). Form the canonical product ensemble with stationary weights
\[
w_L(n)=w(n)+\frac{\theta}{L^2},\qquad n\in\mathbb N_0,
\]
conditioned on exactly \(N_L\) particles at \(L\) sites, where \(N_L/L\to\rho>\rho_c\). Put \(a=\rho-\rho_c\), let \(\eta_{(1)}\ge\cdots\ge\eta_{(L)}\) be the ranked occupations, and count sites above the mesoscopic cutoff by \(K_L=\#\{i:\eta_i>L^{2/3}\}\).

Then the full canonical partition function obeys
\[
L Z_{L,N_L}\longrightarrow F_\theta(a)
=\sum_{j=1}^\infty\frac{\theta^j a^{j-1}}{j!(j-1)!}
=\sqrt{\frac{\theta}{a}}I_1(2\sqrt{\theta a}),
\]
where \(I_1\) is the modified Bessel function of the first kind. The count converges to a finite positive random integer \(K\) with
\[
\Pr(K=j)=\frac{\theta^j a^{j-1}}{j!(j-1)!F_\theta(a)},\qquad j=1,2,\ldots.
\]
Conditionally on \(K=j\), let \((D_1,\dots,D_j)\) have the uniform Dirichlet law \(\operatorname{Dirichlet}(1,\ldots,1)\) (the unit point mass for \(j=1\)). In the sup-norm topology on sequences vanishing at infinity,
\[
\big(\eta_{(1)}/L,\eta_{(2)}/L,\ldots\big)
\ \Longrightarrow\
a\big(D_{(1)},\ldots,D_{(K)},0,0,\ldots\big).
\]
Thus this critical line has a *finite, nondegenerate random number* of macroscopic condensate sites with a uniform-simplex split of the excess mass; it is neither the single-site phase nor a Poisson–Dirichlet infinite-partition phase. In particular,
\[
\Pr(K=1)=\frac{\sqrt{\theta a}}{I_1(2\sqrt{\theta a})}\in(0,1),\qquad
\mathbb E K=\frac{\sqrt{\theta a}\,I_0(2\sqrt{\theta a})}{I_1(2\sqrt{\theta a})}.
\]

## Assumptions and scope
For each integer \(L\ge1\), take \(N_L\in\mathbb N_0\) with \(N_L/L\to\rho\). Assume \(w(n)\ge0\), \(\sum_n w(n)=1\) and \(\sum_n e^{\lambda n}w(n)<\infty\) for some \(\lambda>0\). There is no requirement that every \(w(n)\) be positive: the perturbation makes every \(w_L(n)\) strictly positive. The canonical probability of \(\eta\in\mathbb N_0^L\) with \(\sum_i\eta_i=N_L\) is \(Z_{L,N_L}^{-1}\prod_i w_L(\eta_i)\). Throughout \(\theta\) and \(a\) are fixed and positive. Occupations are sorted in descending order, padded with zeros, and viewed in \(c_0\) with the supremum norm. The cutoff \(L^{2/3}\) is a concrete separator between logarithmic bulk sites and order-\(L\) condensates; it is not a critical exponent of the model.

The result concerns static canonical equilibrium and does not assert any relaxation, coarsening, or condensate-hopping time. It applies to the line \(\gamma=\kappa+2=2\) with \(\kappa=0\), not to every point on the broader transition line. The proof also establishes that the number of sites exceeding the cutoff is tight and that their summed occupations divided by \(L\) converge in probability to \(a\).

## Proof
**1. Exact nonnegative expansion.** Write \(W(z)=\sum_{n\ge0}w(n)z^n\). The generating function of the constant perturbation is \((1-z)^{-1}\) as a formal power series. Therefore
\[
Z_{L,N}=[z^N]\left(W(z)+\frac{\theta}{L^2(1-z)}\right)^L
=\sum_{j=0}^L A_{L,N,j},
\]
where, with independent \(w\)-distributed variables \(G_1,G_2,\ldots\) and \(S_m=G_1+\cdots+G_m\) (including \(S_0=0\)),
\[
A_{L,N,0}=\Pr(S_L=N),\qquad
A_{L,N,j}=\binom Lj\frac{\theta^j}{L^{2j}}\,
\mathbb E\!\left[
\mathbf1_{\{S_{L-j}\le N\}}
\binom{N-S_{L-j}+j-1}{j-1}
\right]\quad(j\ge1).
\]
The combinatorial coefficient counts all weak compositions of the mass left after the \(L-j\) unmarked bulk occupations into the \(j\) sites carrying the perturbative summand. This is an exact identity, including \(j=L\); no large-volume approximation has yet been made.

**2. Each fixed number of marked sites.** Since \(S_{L-j}/L\to\rho_c\) in probability and \(N/L\to\rho\), for fixed \(j\ge1\) the leftover mass divided by \(L\) tends in probability to \(a>0\). On the event \(S_{L-j}\le N\),
\[
L^{1-j}\binom{N-S_{L-j}+j-1}{j-1}
\longrightarrow\frac{a^{j-1}}{(j-1)!}
\]
in probability. The left side is bounded uniformly in \(L\) for fixed \(j\), because \(N\le CL\) eventually. Dominated convergence and \(\binom Lj/L^j\to1/j!\) give
\[
L A_{L,N,j}\longrightarrow\frac{\theta^j a^{j-1}}{j!(j-1)!}.
\]
Meanwhile \(A_{L,N,0}=\Pr(S_L=N)\le\Pr(S_L\ge N)\le e^{-cL}\) for some \(c>0\), by exponential Markov inequality using the positive exponential moment of \(w\) and \(\rho>\rho_c\).

**3. Uniform control of arbitrarily many marked sites.** Choose \(C>0\) so that \(N\le CL\) for large \(L\). For \(1\le j\le L\), use \(\binom Lj\le L^j/j!\) and
\[
\mathbf1_{\{S_{L-j}\le N\}}\binom{N-S_{L-j}+j-1}{j-1}
\le \frac{((C+1)L)^{j-1}}{(j-1)!}.
\]
It follows that
\[
0\le L A_{L,N,j}\le \frac{\theta^j(C+1)^{j-1}}{j!(j-1)!}.
\]
The right side is summable over all \(j\ge1\), independently of \(L\). Combining this bound with the fixed-\(j\) limits proves \(LZ_{L,N}\to F_\theta(a)\) and yields convergence of the *latent* integer \(J_L\), defined by choosing the corresponding nonnegative binomial-expansion summand with probability \(A_{L,N,j}/Z_{L,N}\), to \(K\) with the displayed law. In particular \((J_L)\) is tight.

**4. Separation of marked and unmarked sites.** The latent expansion is an exact positive coupling of the canonical ensemble: conditional on \(J_L=j\), uniformly choose \(j\) marked sites. The unmarked site weights are \(w\); after summing over the marked occupations, the joint law of the unmarked sites is their independent \(w\) law tilted by
\[
H_{L,j}(S_{L-j})=\mathbf1_{\{S_{L-j}\le N\}}
\binom{N-S_{L-j}+j-1}{j-1}.
\]
For every fixed \(j\), its normalizing expectation is asymptotic to \(a^{j-1}L^{j-1}/(j-1)!\), while its maximum is at most \(((C+1)L)^{j-1}/(j-1)!\). Consequently the Radon–Nikodym density relative to the independent bulk law is bounded by a constant depending on \(j,a,C\), for all sufficiently large \(L\). The independent bulk exponential moment then implies
\[
\Pr\!\left(\max_{\mathrm{unmarked}}\eta_i>L^{2/3}\mid J_L=j\right)
\le C_j L e^{-\lambda L^{2/3}}\longrightarrow0
\]
(after replacing \(\lambda\) by any smaller positive moment parameter if necessary). Likewise \(S_{L-j}/L\to\rho_c\) conditionally, so the mass \(h_L=N-S_{L-j}\) assigned to marked sites satisfies \(h_L/L\to a\) conditionally.

**5. Uniform compositions and their limit.** Conditional on the unmarked occupations and \(J_L=j\), the \(j\) marked occupations are uniformly distributed among all \(\binom{h_L+j-1}{j-1}\) weak compositions of \(h_L\). For fixed \(j\ge2\), a Riemann-sum argument on the simplex proves that these occupations divided by \(h_L\) converge in distribution to \(\operatorname{Dirichlet}(1,\ldots,1)\); the \(j=1\) case is deterministic. In addition, for \(0\le T<h_L\), each marked coordinate \(U_i\) obeys the elementary bound
\[
\Pr(U_i\le T\mid h_L,j)\le\frac{(j-1)(T+1)}{h_L+j-1},\qquad j\ge2.
\]
For \(T=\lfloor L^{2/3}\rfloor\) and \(h_L/L\to a>0\), this bound tends to zero. Hence at fixed \(j\), with probability tending to one precisely the \(j\) marked sites exceed the cutoff, while all unmarked sites remain below it. Since \(J_L\) is tight, the union over all fixed \(j\) proves \(\Pr(K_L=J_L)\to1\).

**6. Ranked process and distribution.** Fixed-\(j\) conditional convergence, the smallness of all unmarked occupations divided by \(L\), and continuity of decreasing rearrangement in the sup norm show that the ranked occupations divided by \(L\) converge to the sorted Dirichlet vector with mass \(a\). Tightness of \(J_L\) allows mixture over \(j\), proving the asserted joint limiting description and convergence in \(c_0\). The sum of ranked bulk coordinates does not tend to zero, so an \(\ell^1\) convergence claim would be incorrect; the asserted sup-norm topology is deliberate. Finally the identity
\[
I_1(2\sqrt x)=\sum_{m=0}^\infty\frac{x^{m+1/2}}{m!(m+1)!}
\]
gives \(F_\theta(a)=\sqrt{\theta/a}\,I_1(2\sqrt{\theta a})\), and termwise summation gives the one-site probability and mean count as stated. This completes the proof.

## Verification
The standalone script `verify_critical.py` checks the exact binomial-expansion identity against independent direct coefficient convolution for geometric and Bernoulli bulk distributions, using rational arithmetic for small systems, and tests normalization of the candidate Bessel-series probabilities. The script reports 1,344 assertions passed. `finite_diagnostics.py` independently evaluates the finite-volume expansion for a geometric bulk with \(\rho_c=1\), \(\rho=2\), \(\theta=1\): the values of \(LZ_{L,N}\) at \(L=50,100,200,400,800\) approach the predicted \(I_1(2)\approx1.590636855\). Neither finite experiment proves the thermodynamic limit; the proof is in Steps 1–6.

Reproduce with `python verify_critical.py` and, with NumPy and SciPy installed, `python finite_diagnostics.py`. Only the standard Python library is needed for the exact checker.

## Relationship to prior work
Blank, Chleboun, Grosskinsky and Jatuviriyapornchai (arXiv:2603.00806v1, first publicly posted February 28, 2026) introduce the size-dependent canonical weights, prove general ensemble equivalence, and derive the mesoscopic and single-condensate sides of the \(\gamma=\kappa+2\) boundary. Their Section 2.2 and Figure 1 explicitly leave the boundary open except for a different inclusion-type endpoint, while Section 3 provides an expansion into perturbatively marked sites that motivates Step 1. Neither the expansion nor known bulk condensation is claimed as new. The present contribution is the full normalized partition coefficient, the finite Bessel count law, and the joint Dirichlet ranked-mass limit on the \(\kappa=0,\gamma=2\) boundary for any exponential-tail bulk.

Jatuviriyapornchai and Grosskinsky (2024) treat a related fast-rate zero-range model and explicitly identify the \(\gamma=2\) regime as analytically unresolved. Chleboun, Gabriel and Grosskinsky (2022) prove Poisson–Dirichlet limits under different, occupation-dependent stationary-weight scaling; their infinite-partition conclusion is not a theorem for the constant perturbation here. The present limit has only finitely many positive macroscopic parts almost surely, so it cannot equal that Poisson–Dirichlet law.

## Limitations
The result is restricted to canonical stationary measures with exactly constant perturbation \(\theta/L^2\), positive excess density, and exponentially light bulk. It does not cover general \(\kappa\ne0\), general perturbative error terms, the critical-density case \(\rho=\rho_c\), or finite-time dynamics. The latent marked-site count is a proof device, not a measurable physical label; Step 5 supplies its asymptotic equivalence to the observable cutoff count. Stronger unindexed condensation results could affect publication priority. The proof establishes convergence in the sup-norm topology, not in \(\ell^1\), because diffuse bulk mass persists.

## References
1. J. Blank, P. Chleboun, S. Grosskinsky and W. Jatuviriyapornchai, *Condensation in stochastic lattice gases with size-dependent stationary weights*, arXiv:2603.00806v1 (first posted 2026-02-28), https://arxiv.org/html/2603.00806 . In particular Sections 2.1–2.2, 3.2–3.4 and Figure 1.
2. W. Jatuviriyapornchai and S. Grosskinsky, *Condensation in Zero-Range Processes with a Fast Rate*, Journal of Statistical Physics 191, article 147 (2024), https://doi.org/10.1007/s10955-024-03362-0 . In particular the discussion of the borderline regime.
3. P. Chleboun, S. Gabriel and S. Grosskinsky, *Poisson-Dirichlet asymptotics in condensing particle systems*, Electronic Journal of Probability 27 (2022), https://arxiv.org/abs/2106.09625 . In particular the stationary-weight assumptions and condensation partition results.
