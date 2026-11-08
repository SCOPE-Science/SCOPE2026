# Weak convergence of root-doubling tree size through a logarithmic-time jump process

## Finding

In the root-doubling random recursive tree of Björnberg and Mailler, let \(B_n\) be the number of non-root vertices after \(n\) updates. Then the scaled size, whose moments were previously shown to converge without a proof of weak convergence, **does converge in law**:

\[
\frac{B_n}{n}\ \Longrightarrow\ \pi\qquad (n\to\infty).
\]

Here \(\pi\) is the **unique invariant probability distribution** on \([1,\infty)\) for the piecewise-deterministic Markov process \(Z_t\) with deterministic flow \(\dot Z_t=1-Z_t\), jumps \(z\mapsto 2z\), and state-dependent jump intensity \(1/z\). Equivalently, its generator on smooth compactly supported test functions is

\[
\mathcal Lf(z)=(1-z)f'(z)+\frac{f(2z)-f(z)}{z},\qquad z\ge1.
\]

The invariant law is nondegenerate: \(\int z\,\pi(dz)=2\) and \(\int z^2\,\pi(dz)=5\), so its variance equals \(1\). More generally, for every integer \(r\ge1\), its moments are

\[
\int z^r\,\pi(dz)=\prod_{j=1}^{r}\frac{j-1+2^j}{j}.
\]

No uniqueness claim is made from the moment sequence alone. The weak limit is instead selected by the uniquely ergodic jump process.

## Assumptions and scope

Start at the one-vertex rooted tree \(\tau_0\). At every discrete time, choose a vertex uniformly. If it is not the root, attach a new leaf there. If it is the root, replace the tree by one root with two entire copies of the preceding tree as its two rooted subtrees. Thus \(B_0=0\) and, conditioned on \(B_k=b\),

\[
B_{k+1}=\begin{cases}
 b+1,&\text{with probability }b/(b+1),\\
 2(b+1),&\text{with probability }1/(b+1).
\end{cases}
\]

All probabilities refer to this model, without changing its root-selection rule. The weak convergence concerns the real variables \(B_n/n\) as integer \(n\to\infty\); it does not assert almost-sure convergence, total-variation convergence, or a rate uniform over \(n\). The process \(Z\) starts from any \(z\ge1\), flows as \(\Phi_t(z)=1+(z-1)e^{-t}\) between jumps, and jumps to twice its pre-jump state. Because \(1/Z_t\le1\), it is nonexplosive.

## Proof

**1. The exact logarithmic-time one-step match.** For each integer \(k\ge1\), set \(Y_k=B_k/k\). Induction gives \(B_k\ge k\), hence \(Y_k\ge1\). With \(\Delta_k=\log((k+1)/k)\), an ordinary discrete update gives exactly \(Y_{k+1}=\Phi_{\Delta_k}(Y_k)\), whereas a root-doubling update gives exactly \(Y_{k+1}=2\Phi_{\Delta_k}(Y_k)\). Its conditional doubling probability is

\[
p_k(y)=\frac1{ky+1}.
\]

For the continuous process started at \(z\ge1\), the cumulative hazard of its **first** jump in a time interval of length \(\Delta_k\) is

\[
\int_0^{\Delta_k}\frac{ds}{\Phi_s(z)}
=\log\left(\frac{e^{\Delta_k}+z-1}{z}\right)
=\log\left(1+\frac1{kz}\right).
\]

Therefore the probability of at least one continuous jump is **exactly** \(p_k(z)\). This equality is specific to the reciprocal jump rate and the logarithmic time grid; no general approximation principle is needed for it.

**2. A controlled one-interval coupling.** Let \(z\ge1\). Denote by \(I_z\) the event of at least one jump of \(Z\) during the next interval. Let \(b=\Phi_{\Delta_k}(z)\). On \(I_z^c\), the continuous endpoint equals \(b\). If exactly one jump occurs at time \(s\in(0,\Delta_k]\), its endpoint is

\[
\Phi_{\Delta_k-s}(2\Phi_s(z))
=2b-\bigl(1-e^{-(\Delta_k-s)}\bigr),
\]

which differs from \(2b\) by at most \(\Delta_k\). Further jumps contribute positive increments to the linear flow representation. Since their compensator has conditional instantaneous **expected size** \((1/Z_t)Z_t=1\), the expected sum of their sizes after the first jump, conditional on that first jump, is at most \(\Delta_k\). Thus, on the first-jump Bernoulli coupling, the absolute endpoint discrepancy has expectation bounded by

\[
\mathbb E\big|Z_{\Delta_k}-(1+I_z)b\big|
\le2p_k(z)\Delta_k\le\frac2{k^2}.
\]

For arbitrary \(y,z\ge1\), couple the Bernoulli indicators with probabilities \(p_k(y)\) and \(p_k(z)\) by a common uniform variable. Their mismatch probability is \(|p_k(y)-p_k(z)|\). Writing \(a=\Phi_{\Delta_k}(y)\) and \(b=\Phi_{\Delta_k}(z)\), using \(b\le z\),

\[
b|p_k(y)-p_k(z)|
=\frac{bk|y-z|}{(ky+1)(kz+1)}\le\frac{|y-z|}{k}.
\]

Also \(|a-b|=e^{-\Delta_k}|y-z|\) and \(p_k(y)\le1/k\). Consequently one can couple the discrete transition from \(y\) and the continuous interval from \(z\) so that

\[
\mathbb E|Y_{k+1}-Z_{\Delta_k}|
\le\left(1+\frac2k\right)|y-z|+\frac2{k^2}.
\tag{1}
\]

Here \(Y_{k+1}\) denotes a single discrete step from \(y\); no assumption that \(y=z\) is used.

**3. Uniform finite-logarithmic-horizon approximation.** Couple an actual discrete trajectory from time \(m\ge2\) with a continuous trajectory initially set equal to \(Y_m\), using (1) successively. At the grid time \(t_k=\log(k/m)\), let \(e_k=\mathbb E|Y_k-Z_{t_k}|\). Then \(e_m=0\) and

\[
e_{k+1}\le(1+2/k)e_k+2/k^2.
\]

Because \(\prod_{j=m}^{n-1}(1+2/j)=n(n+1)/(m(m+1))\), this yields the explicit bound

\[
\boxed{\ \mathbb E\left|\frac{B_n}{n}-Z_{\log(n/m)}\right|
\le\frac{2n(n+1)}{m(m+1)(m-1)}\ },\qquad n\ge m\ge2,
\]

where the continuous process is started at \(Z_0=Y_m\) under this coupling. In particular, for each fixed \(T>0\) and \(m=\lfloor ne^{-T}\rfloor\), this error tends to zero as \(n\to\infty\).

**4. The continuous process has one attracting invariant law.** For \(V(z)=1+z\), the generator satisfies \(\mathcal LV(z)=2-z=3-V(z)\), and Dynkin's formula gives

\[
\mathbb E_z Z_t=2+(z-2)e^{-t}.
\]

For completeness, the needed irreducibility and small-set properties can be checked from the one-jump event. If the process starts at \(z\in[1,R]\) and has exactly one jump at time \(s\in(0,T)\), then

\[
Z_T=1+e^{-(T-s)}+2(z-1)e^{-T}.
\]

For any sufficiently large integer \(T\) satisfying \((2R-1)e^{-T}<1\), the one-jump distribution has a density bounded below uniformly over \(z\in[1,R]\) on a common nonempty subinterval of \((1+(2R-1)e^{-T},2)\). The first-jump density and subsequent no-jump probability have positive continuous lower bounds there. Every compact subset of \([1,\infty)\) is therefore a small set for a suitable power of the unit-time skeleton. Repeating this argument for consecutive sufficiently large integers establishes aperiodicity; every starting state can reach intervals of positive Lebesgue measure in \((1,2)\), establishing irreducibility. The exact drift \(P_1V(z)=3+(z-2)e^{-1}\) is geometrically contractive outside a compact set. The standard irreducible, aperiodic small-set Foster–Lyapunov theorem consequently supplies a unique invariant probability \(\pi\) and constants \(C,\gamma>0\) such that

\[
\|P_t(z,\cdot)-\pi\|_{\mathrm{TV}}
\le C(1+z)e^{-\gamma t},\qquad z\ge1,\quad t\ge0.
\tag{2}
\]

The construction also verifies all conditions to which this standard theorem is applied, instead of assuming positive recurrence from the formal drift alone.

**5. Passage to the discrete weak limit.** The original transition law gives \(\mathbb E(B_{k+1}\mid B_k)=B_k+2\); hence \(\mathbb EY_m=2\) for every \(m\ge1\). Fix \(T>0\), take \(m=\lfloor ne^{-T}\rfloor\), and let \(F\) be bounded and 1-Lipschitz. The coupling bound in Step 3 and (2) give

\[
\left|\mathbb EF(Y_n)-\pi F\right|
\le\frac{2n(n+1)}{m(m+1)(m-1)}
+3C'\|F\|_\infty\left(\frac mn\right)^\gamma,
\]

with \(C'\) an absolute constant associated with (2). Taking \(n\to\infty\) at fixed \(T\), and then \(T\to\infty\), proves \(Y_n\Rightarrow\pi\).

Finally, the published moment asymptotics give \(\mathbb EY_n^r\to m_r\) for every integer \(r\ge1\). The bounded \((r+1)\)-st moments imply uniform integrability of \(Y_n^r\); weak convergence therefore transfers those moment limits to \(\pi\). In particular \(m_1=2\), \(m_2=5\) and \(\operatorname{Var}_\pi Z=1\). This completes the proof.

## Verification

The standalone `verify.py` performs exact rational transitions of the original chain, checks its conditional drift and normalized first two moments, verifies the generator polynomial identities and the first-jump hazard identity on independent parameter grids, checks the one-jump minorization geometry, and simulates both the finite chain and the continuous process using exact event-time inversion. The recorded run passed 2,952 finite assertions. Its simulated stationary mean and second moment were approximately \(1.99322\) and \(4.98830\), compared with the analytic values \(2\) and \(5\). Its independent discrete simulation gave mean \(2.00432\) for \(B_{100000}/100000\).

The proof is analytic: finite enumeration and simulations are diagnostics, not proof of weak convergence, Harris recurrence, or absence of earlier literature.

## Relationship to prior work

Björnberg and Mailler (arXiv:2501.18466, initially public January 30, 2025) introduce this precise root-doubling model, derive the size recursion and the full limiting moment sequence, and state explicitly in Remark 1.2 that their results do **not** establish weak convergence of \(B_n/n\). Their obstruction is the failure of the available moment-uniqueness criterion. Here the exact first-jump coupling and the uniquely ergodic logarithmic-time process establish convergence without requiring moment determinacy.

Davis (1984) provides general piecewise-deterministic Markov process theory; Meyn and Tweedie (1993) provide the Foster–Lyapunov ergodicity framework. The model-specific hazard equality, coupling bound and weak convergence of this particular tree-size statistic are the new claim. The present argument does not claim novelty of the general PDMP or Harris machinery.

## Limitations

The result concerns only the number of vertices of the **root-only** doubling model, not the variant doubling at arbitrary vertices, whose expected growth is also studied in the source paper. It does not resolve the source paper's separate open problem on the height constant. Weak convergence is not strengthened to almost-sure convergence, and this work does not provide a closed-form density, distribution function, or convergence rate independent of the unknown Harris mixing constants. Standard Harris ergodicity is invoked after model-specific verification of the drift and minorization hypotheses; its full historical theory is credited. Independent mathematical validation and exhaustive historical-priority verification have not been performed.

## References

1. J. E. Björnberg and C. Mailler, *A random recursive tree model with doubling events*, arXiv:2501.18466 (first posted 2025-01-30), revised 2026; *Stochastic Processes and their Applications* 192 (2026), 104790. https://arxiv.org/html/2501.18466 ; https://doi.org/10.1016/j.spa.2025.104790 .
2. M. H. A. Davis, *Piecewise-Deterministic Markov Processes: A General Class of Non-Diffusion Stochastic Models*, *J. Roy. Statist. Soc. B* 46 (1984), 353–376. https://doi.org/10.1111/j.2517-6161.1984.tb01308.x .
3. S. P. Meyn and R. L. Tweedie, *Stability of Markovian processes III: Foster–Lyapunov criteria for continuous-time processes*, *Adv. Appl. Probab.* 25 (1993), 518–548. https://doi.org/10.1017/S0001867800025532 .
