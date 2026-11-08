# Sharp first-passage criterion and correlation-invariant tails for Markov-modulated heavy-tailed Poisson clocks

## Finding

Consider a simple symmetric walk on the positive integers, killed on its first visit to zero, whose nearest-neighbor jumps occur at a stochastic Poisson rate that is refreshed at unit times. Conditional on an irreducible aperiodic finite-state Markov environment, the refreshed rates are independent, with a potentially different positive distribution in each environment state. No finite moment of a rate is required.

Let \(f_i(s)\) denote the conditional rate Laplace transform in state \(i\), \(\pi\) the environment's stationary distribution, and
\[
h(s)=\sum_i\pi_i(1-f_i(s)).
\]
Then, for **every fixed starting site** \(x\ge1\), the first-passage time \(T_x\) has finite mean if and only if
\[
\boxed{\int_0^1\frac{ds}{\sqrt{s}\,h(s)}<\infty.}
\]
Moreover, if \(h\) is regularly varying at zero with index \(\alpha\in(0,1)\), let \(\vartheta_n\in(0,\pi)\) be the unique solution of
\[
n h(1-\cos\vartheta_n)=1.
\]
Then the **sharp survival equivalent** is
\[
\boxed{\Pr(T_x>t)\sim\frac{2x}{\pi}\Gamma\!\left(1+\frac1{2\alpha}\right)\vartheta_{\lfloor t\rfloor}.}
\]
The leading term depends only on the stationary mixture of conditional rate laws and is unchanged by replacing the temporally correlated Markov environment with independent stationary-mixture draws. This is an asymptotic statement: the finite-time survival laws generally differ.

For a natural tail family
\[
\Pr(\Lambda>u\mid J=i)\sim c_i u^{-\alpha_i}(\log u)^{\beta_i},
\qquad c_i>0,\ 0<\alpha_i<1,\ \beta_i\in\mathbb R,
\]
write \(\alpha_* = \min_i\alpha_i\), \(\beta_* = \max\{\beta_i:\alpha_i=\alpha_*\}\), and \(C_* =\Gamma(1-\alpha_*)\sum_{i:\alpha_i=\alpha_*,\,\beta_i=\beta_*}\pi_i c_i\). Then
\[
h(s)\sim C_*s^{\alpha_*}(\log(1/s))^{\beta_*},
\]
and the criterion becomes
\[
\boxed{\mathbb E T_x<\infty\iff \alpha_*<\tfrac12\quad\text{or}\quad (\alpha_*=\tfrac12\text{ and }\beta_*>1).}
\]
For these tails, the asymptotic scale is explicit:
\[
\vartheta_n\sim\sqrt2\left(\frac{\alpha_*^{\beta_*}}{C_*}\right)^{1/(2\alpha_*)}
 n^{-1/(2\alpha_*)}(\log n)^{-\beta_*/(2\alpha_*)}.
\]

## Assumptions and scope

Fix an integer \(r\ge1\), a row-stochastic \(r\times r\) matrix \(P\) that is irreducible and aperiodic, and its unique stationary probability row vector \(\pi\), so \(\pi P=\pi\) and \(\pi_i>0\). Start the environment \((J_m)_{m\ge0}\) with distribution \(\pi\), and let it evolve with transition matrix \(P\). Conditional on the *entire* environment path, the rates \((\Lambda_m)_{m\ge0}\) are independent with \(\Lambda_m\) drawn from distribution \(F_{J_m}\). Assume \(0<\Lambda_m<\infty\) almost surely. Conditional on the rates, jumps are an inhomogeneous Poisson process with constant intensity \(\Lambda_m\) during \([m,m+1)\); jump directions are independent fair signs. The clock, environment, and directions are independent except for the stated emission dependence. The walker begins at a fixed positive integer \(x\), and \(T_x\) is its first physical hitting time of zero. The one-state case is permitted, with the obvious primitive matrix.

No independence of consecutive rates is imposed, and the theorem permits state-dependent distributions with infinite mean. The general integral criterion requires no regular variation. The survival equivalent requires regular variation with exponent strictly between zero and one; the power-log corollary assumes the displayed conditional tails in every state.

## Proof

**1. Exact subordination and matrix transform.** Let \(A_n=\sum_{m=0}^{n-1}\Lambda_m\), the cumulative Poisson intensity through physical time \(n\). Let \(D(s)=\operatorname{diag}(f_1(s),\ldots,f_r(s))\), and \(Q(s)=D(s)P\). Conditioning successively on emissions and the environment gives the exact identity, for \(s>0\) and all integers \(n\ge0\),
\[
\mathbb E[e^{-sA_n}]=\pi Q(s)^n\mathbf1.
\]
Since every \(\Lambda_m\) is strictly positive, \(0<f_i(s)<1\) for positive \(s\), whence \(Q(s)\) has spectral radius strictly below one. The continuous-time unit-rate symmetric random walk killed at zero has spectral survival formula
\[
g_x(u):=\Pr(H_x>u)=\frac1\pi\int_0^\pi
\frac{\sin(x\theta)\sin\theta}{1-\cos\theta}
 e^{-u(1-\cos\theta)}\,d\theta,
\]
where \(H_x\) denotes its first hitting time of zero. Subordination gives \(\Pr(T_x>n)=\mathbb E[g_x(A_n)]\). For \(x=1\), the spectral weight is the strictly positive \(1+\cos\theta\), hence
\[
\boxed{S_1(n)=\frac1\pi\int_0^\pi(1+\cos\theta)
\pi Q(1-\cos\theta)^n\mathbf1\,d\theta.}\tag{1}
\]
Tonelli's theorem and the convergent matrix geometric series give the **exact** summed survival identity
\[
\sum_{n=0}^\infty S_1(n)=\frac1\pi\int_0^\pi(1+\cos\theta)
\pi[I-Q(1-\cos\theta)]^{-1}\mathbf1\,d\theta.\tag{2}
\]

**2. Uniform first-order Markov perturbation.** Define \(d_i(s)=1-f_i(s)\) and \(d(s)=\max_i d_i(s)\). As \(s\downarrow0\), all \(d_i(s)\downarrow0\). Because \(\pi_i>0\), \(d(s)\le h(s)/\min_i\pi_i\). At \(s=0\), \(Q(0)=P\), with simple Perron eigenvalue one, right eigenvector \(\mathbf1\), left eigenvector \(\pi\), and all other eigenvalues of modulus strictly below one. Finite-dimensional analytic (indeed, smooth-in-matrix-entries) perturbation of this isolated eigenvalue shows
\[
1-\rho(Q(s))=h(s)+O(h(s)^2),
\quad \pi \mathcal P(s)\mathbf1=1+O(h(s)),\tag{3}
\]
where \(\mathcal P(s)\) denotes its Perron spectral projector. More precisely, the first variation of eigenvalue \(1\) for perturbation \(-\operatorname{diag}(d_i)P\) is \(-\sum_i\pi_i d_i=-h(s)\), while the remaining terms are bounded by a constant times \(d(s)^2\). This estimate does not require differentiating the transforms with respect to \(s\). Decomposing the resolvent into the Perron projector and a uniformly bounded complementary inverse yields
\[
\pi[I-Q(s)]^{-1}\mathbf1\sim\frac1{h(s)}\qquad(s\downarrow0).\tag{4}
\]
The integrand of (2) is bounded on any fixed interval \(\theta\ge\epsilon>0\), by continuity and spectral radius below one. Near zero, \(1-\cos\theta\sim\theta^2/2\) and \(1+\cos\theta\to2\). Thus (2)--(4) prove
\[
\sum_{n\ge0}S_1(n)<\infty\iff\int_0^1\frac{ds}{\sqrt s\,h(s)}<\infty.\tag{5}
\]
The sum is finite exactly when \(\mathbb E T_1\) is finite, since \(T_1\ge0\) and the survival function is nonincreasing on every interval between integers.

**3. General fixed starting sites.** By the strong Markov property in *operational* time, \(H_x\) is the sum of \(x\) independent copies of \(H_1\). Therefore, for every \(u>0\),
\[
g_1(u)\le g_x(u)\le xg_1(u/x).
\]
The elementary continuous-time symmetric-walk hitting-time asymptotic \(g_1(u)\sim\sqrt{2/(\pi u)}\) implies \(\sup_{u\ge0}g_1(u/x)/g_1(u)<\infty\). Thus \(S_1(n)\le S_x(n)\le C_x S_1(n)\) for all \(n\), proving the same integrability criterion for any fixed \(x\). Moreover \(g_x(u)/g_1(u)\to x\) as \(u\to\infty\). For fixed \(K\), the inequality \(\Pr(A_n\le K)\le e^K\,\mathbb E e^{-A_n}\) gives exponential decay in \(n\), since \(\rho(Q(1))<1\). When \(S_1(n)\) is polynomially decaying, the part of the expected survival from \(A_n\le K\) is negligible; letting \(K\to\infty\) establishes \(S_x(n)\sim xS_1(n)\).

**4. Sharp survival under regular variation.** Suppose \(h\) is regularly varying at zero with exponent \(\alpha\in(0,1)\), and choose \(\vartheta_n\) as in the finding. Then \(\vartheta_n\downarrow0\). The Perron contribution in (1), after the change of variables \(\theta=\vartheta_n v\), satisfies
\[
\rho(Q(1-\cos(\vartheta_n v)))^n
\longrightarrow e^{-v^{2\alpha}}
\quad(v>0),\tag{6}
\]
by (3), regular variation, and \(n h(1-\cos\vartheta_n)=1\). The spectral-projector coefficient tends to one. For each sufficiently small fixed angle, the complementary spectral terms are bounded by a geometric factor \(\kappa^n\) with \(\kappa<1\); for angles away from zero, the full matrix powers similarly decay uniformly geometrically. Potter bounds for \(h\), combined with (3), dominate the rescaled Perron integral by an integrable function of \(v\). Therefore,
\[
S_1(n)\sim\frac{2\vartheta_n}{\pi}\int_0^\infty e^{-v^{2\alpha}}\,dv
=\frac{2\vartheta_n}{\pi}\Gamma\!\left(1+\frac1{2\alpha}\right).\tag{7}
\]
The fixed-\(x\) argument in Step 3 gives the factor \(x\). Because \(\vartheta_n\) is regularly varying with negative index \(-1/(2\alpha)\), replacing integer \(n\) by real \(t\) through the monotonic bounds \(S_x(\lfloor t\rfloor+1)\le\Pr(T_x>t)\le S_x(\lfloor t\rfloor)\) does not change the equivalent.

**5. Power-log tail mixture and the border.** Conditional tail integration gives \(1-f_i(s)=s\int_0^\infty e^{-su}\Pr(\Lambda>u\mid J=i)\,du\). Karamata's Abelian theorem yields
\[
1-f_i(s)\sim c_i\Gamma(1-\alpha_i)s^{\alpha_i}
(\log(1/s))^{\beta_i}.
\]
In the finite stationary mixture, terms with the smallest power \(\alpha_i\), followed by the largest logarithmic exponent \(\beta_i\), dominate. This gives \(h(s)\sim C_*s^{\alpha_*}(\log(1/s))^{\beta_*}\), and (5) becomes convergence at zero of
\[
\int_0^1 s^{-\alpha_*-1/2}(\log(1/s))^{-\beta_*}\,ds.
\]
Elementary integration gives the stated strict threshold and its logarithmic equality case. Solving the defining equation for \(\vartheta_n\) gives its displayed asymptotic with the factor \(\alpha_*^{\beta_*}\). This completes the argument.

## Verification

The included Python 3 standard-library script `verify.py` exercises (i) the exact Markov-emission matrix transform by independent path enumeration with rational arithmetic in two- and three-state examples, (ii) finite matrix-resolvent identities and positive remainders, (iii) Poissonized absorbed-walk survival against independent spectral integration for five starting sites, and (iv) the predicted Perron-eigenvalue slope for heavy-tailed transform examples. A recorded replay passed **116 assertions**. These finite checks test formulas but do not prove the limiting statements; the proof above supplies the mathematical argument. Reproduce using `python3 verify.py`.

## Relationship to prior work

Levit and Reuveni [1], first publicly posted 2026-09-22, give the general random-clock spectral survival identity (their Eq. (2)) and identify the infinite-to-finite mean transition for **independently refreshed** Mittag-Leffler rates; these formulas and the independent model are not new here. The present result substitutes the exact hidden-Markov matrix Laplace transform, proves a sharp criterion for arbitrary positive state-dependent emission laws, shows **leading survival invariance under finite-memory correlations**, and determines the log-corrected critical boundary for heterogeneous heavy tails.

Grebenkov [2] formulates first passage via integrated diffusivity and finite-state switching diffusion with fixed state diffusivities; that broad subordination framework and matrix approach are relevant antecedents. The present claim is specifically for discrete-time-refreshed hidden-Markov rate emissions with unbounded heavy tails and includes explicit Perron/regular-variation asymptotics and a necessary-and-sufficient borderline moment criterion. Angstmann et al. [3] analyze compounded random walks with independently sampled step counts, a distinct temporal mechanism. Neither [2] nor [3] is asserted to be new or absent from general first-passage theory.

## Limitations

The correlation-invariance is **only** the leading tail equivalent, not a finite-time identity, and relies on a fixed primitive finite-state environment and conditionally independent rate emissions. This work does not treat nonprimitive, long-range-dependent, or growing-state environments; rates can be heavy-tailed but must be finite and strictly positive almost surely. No universal tail equivalent is asserted when \(h\) fails regular variation. Strict novelty beyond the searched corpus has not been independently established; other Markov-additive renewal or switching-process results may subsume part of the argument. The checker is finite and does not certify an infinite asymptotic theorem.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1 (first posted 2026-09-22), https://arxiv.org/abs/2609.26925.
2. D. S. Grebenkov, *A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models*, arXiv:1812.07249v1 (2018), https://arxiv.org/abs/1812.07249.
3. C. N. Angstmann, J. Han, B. I. Henry, C. Huang, *First-Passage Times for the Space-Fractional Spectral Fokker-Planck Equation*, arXiv:2511.18256v1 (2025), https://arxiv.org/abs/2511.18256.
