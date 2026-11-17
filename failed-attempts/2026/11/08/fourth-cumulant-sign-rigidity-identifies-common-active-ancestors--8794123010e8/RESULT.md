# Fourth-cumulant sign rigidity identifies common active ancestors in overdamped harmonic networks

## Finding
Consider a stable cooperative overdamped harmonic network driven by independent symmetric two-state active forces and arbitrary independent additive Gaussian noise. **For every four observed sites and every four observation times**, its connected fourth position correlation is nonpositive. It is *strictly negative exactly when the four observed sites have at least one common reachable active-force source*. This yields an exact graph-support classification, independent of all observation times and unaffected by independent Gaussian background noise. The same network, with each telegraph force replaced by a variance- and covariance-matched Gaussian Ornstein–Uhlenbeck force, has identical position covariances at all time lags but zero connected fourth correlations.

More precisely, let \(M\in\mathbb R^{n\times n}\) be Hurwitz and Metzler (every off-diagonal entry is nonnegative), let \(B\in[0,\infty)^{n\times m}\), and let \(G\) be any fixed real matrix. Let \(\sigma_1,\ldots,\sigma_m\) be independent stationary fair telegraph signs taking values \(\pm1\), each flipping at positive rate \(\gamma_\ell\), independently of a standard Brownian vector \(W\). The unique stationary solution of
\[
 dX_t=MX_t\,dt+B\sigma_t\,dt+G\,dW_t
\]
exists. Define the directed graph by \(j\to i\) whenever \(M_{ij}>0\) for distinct sites. Say source \(\ell\) *reaches* site \(i\) if some \(j\) with \(B_{j\ell}>0\) reaches \(i\) along a directed path, permitting a path of length zero. Write \(\mathcal S_i\) for the set of these sources.

For arbitrary \(i_1,\ldots,i_4\in\{1,\ldots,n\}\) and \(t_1,\ldots,t_4\in\mathbb R\), set
\[
 K=\operatorname{cum}\bigl(X_{i_1}(t_1),X_{i_2}(t_2),X_{i_3}(t_3),X_{i_4}(t_4)\bigr).
\]
Then the **complete strict-sign and support classification** is
\[
 \boxed{K<0\ \Longleftrightarrow\ \bigcap_{p=1}^4\mathcal S_{i_p}\ne\varnothing,\qquad K=0\ \Longleftrightarrow\ \bigcap_{p=1}^4\mathcal S_{i_p}=\varnothing.}
\]
In particular the sign cannot depend on lag or on the Gaussian-noise covariance, and four-point observations detect common active ancestry rather than merely two-point statistical correlation. The assertion does not claim reconstruction of individual graph edges or uniqueness of the hidden-source arrangement.

## Assumptions and scope
All dimensions \(n,m\) are finite and positive. The rate of each telegraph force is \(0<\gamma_\ell<\infty\); different forces are independent and have the symmetric stationary distribution. The linear drift is stable and cooperative: \(M\) has spectral abscissa strictly negative and nonnegative off-diagonal entries. The input matrix \(B\) is entrywise nonnegative, but is allowed to contain zero columns. The Gaussian noise covariance \(GG^{\mathsf T}\) is arbitrary, including degenerate or spatially correlated cases. The comparison Gaussian force \(Z_\ell\) is independently stationary and solves
\[
 dZ_\ell(t)=-2\gamma_\ell Z_\ell(t)\,dt+\sqrt{4\gamma_\ell}\,d\widetilde W_\ell(t),
\]
with \(\widetilde W\) independent of \(W\). Its variance is one and its covariance matches that of \(\sigma_\ell\). The theorem concerns stationary *positions* and their connected correlations, not displacements of the form \(X(t)-X(0)\), nor signed velocity filters of underdamped chains.

## Proof
**1. Stable causal representation.** Since \(M\) is Hurwitz, its semigroup is exponentially decaying and the unique stationary solution has the convergent representation
\[
 X_i(t)=\sum_{\ell=1}^m\int_0^\infty H_{i\ell}(s)\,\sigma_\ell(t-s)\,ds+Y_i(t),
 \quad H(s)=e^{Ms}B,
\]
where \(Y(t)=\int_0^\infty e^{Ms}G\,dW(t-s)\) is a centered stationary Gaussian process independent of all telegraph inputs. Integrability of every \(H_{i\ell}\) follows from exponential stability.

**2. An exact four-time telegraph cumulant.** For any four times \(u_1,\ldots,u_4\), rearrange them as \(u_{(1)}\le u_{(2)}\le u_{(3)}\le u_{(4)}\). The symmetric two-state Markov semigroup yields
\[
 \mathbb E[\sigma_\ell(u_{(1)})\sigma_\ell(u_{(2)})\sigma_\ell(u_{(3)})\sigma_\ell(u_{(4)})]
 =e^{-2\gamma_\ell[(u_{(2)}-u_{(1)})+(u_{(4)}-u_{(3)})]}.
\]
Each pair correlation is \(e^{-2\gamma_\ell|u-v|}\). Subtracting the three pair products, the first cancels the four-point moment and the other two are equal. Consequently
\[
 \operatorname{cum}_4\bigl(\sigma_\ell(u_1),\ldots,\sigma_\ell(u_4)\bigr)
 =-2e^{-2\gamma_\ell[(u_{(3)}-u_{(1)})+(u_{(4)}-u_{(2)})]}<0.
\]
The formula includes coincident times by continuity and the Markov property.

**3. Exact connected-correlator integral.** Let \(u_p=t_p-s_p\), and let \(u_{(1)},\ldots,u_{(4)}\) be their order statistics. Multilinearity of cumulants, independence of the telegraph sources, and vanishing of every fourth Gaussian joint cumulant give
\[
 \boxed{K=-2\sum_{\ell=1}^m\int_{[0,\infty)^4}
 \left(\prod_{p=1}^4H_{i_p\ell}(s_p)\right)
 e^{-2\gamma_\ell[(u_{(3)}-u_{(1)})+(u_{(4)}-u_{(2)})]}
 \,ds_1\cdots ds_4.}
\]
All terms are absolutely integrable: their absolute values are at most \(2\prod_p\|H_{i_p\ell}\|_{L^1}\). No independence between values of a given telegraph process at different times is assumed.

**4. Exact reachability criterion.** Put \(A=M+cI\) for sufficiently large \(c\) so that \(A\) is entrywise nonnegative. For \(s>0\),
\[
 (e^{Ms}B)_{i\ell}=e^{-cs}\sum_{q=0}^\infty\frac{s^q}{q!}(A^qB)_{i\ell}.
\]
Every summand is nonnegative. At least one summand is positive precisely when there is a directed path from a site with \(B_{j\ell}>0\) to \(i\); diagonal steps do not create new reachability. Thus \(H_{i\ell}(s)>0\) at *every* positive \(s\) if \(\ell\in\mathcal S_i\), and \(H_{i\ell}\equiv0\) otherwise. In the integral in Step 3, an active-source term is strictly negative if and only if that source reaches all four observed sites; the exponential factor is always strictly positive. All remaining source terms are zero. This proves both directions of the strict-sign and zero-support classification, at every choice of observation lags.

**5. Covariance-matched Gaussian control.** Independent stationary OU drivers \(Z_\ell\) above obey \(\mathbb E[Z_\ell(t)Z_k(u)]=\delta_{\ell k}e^{-2\gamma_\ell|t-u|}\), identical to the telegraph covariance. Linear filtering therefore makes all two-time position covariance matrices identical between the two models. But the OU-driven position process is jointly Gaussian, so its connected fourth correlations vanish identically. Thus covariance equality does not imply equality of the exact fourth-order common-ancestor signature.

**6. Boundary of the hypothesis.** Cooperativity cannot be dropped without changing the sign theorem. With \(M=\begin{pmatrix}-2&-1\\-1&-2\end{pmatrix}\) and a single source at site 1, \((e^{Ms}B)_1=e^{-2s}\cosh s>0\) while \((e^{Ms}B)_2=-e^{-2s}\sinh s<0\) for \(s>0\). The same formula from Step 3 gives \(\operatorname{cum}(X_1,X_1,X_1,X_2)>0\) at any observation times. Stability alone therefore does not suffice.

## Verification
The included standalone `verify.py` checks the four-time telegraph identity directly against two-state transition matrices for multiple rates and repeatedly ordered times, verifies one-body exact stationary cumulants, checks semigroup reachability signs in explicit finite graphs, and computes a negative mixed-site/mixed-time example using deterministic Sobol quadrature. It records 895 passing deterministic assertions. These finite checks are diagnostics; Steps 1–6 are the complete proof for all finite dimensions and all real observation times.

For the single-site comparison \(dX=-\mu X\,dt+a\sigma\,dt\), the known beta-law moment identities give the exact cross-check
\[
 \operatorname{Var}(X)=\frac{a^2}{\mu(\mu+2\gamma)},\quad
 \operatorname{cum}_4(X)=-\frac{6a^4}{\mu(\mu+2\gamma)^2(3\mu+2\gamma)},\quad
 \frac{\operatorname{cum}_4(X)}{\operatorname{Var}(X)^2}=-\frac6{3+2\gamma/\mu}.
\]
As a concrete support distinction, take \(M=\begin{pmatrix}-2&0&0\\1&-2&0\\0&0&-2\end{pmatrix}\), \(B=[e_1,e_3]\), and a common scalar Gaussian noise coupled through \(G=(1,1,1)^{\mathsf T}\). Then \(\operatorname{cum}(X_1,X_2,X_2,X_2)<0\), while \(\operatorname{cum}(X_1,X_1,X_3,X_3)=0\) even though \(\operatorname{Cov}(X_1,X_3)=1/4>0\) from the common Gaussian forcing.

## Relationship to prior work
Paul, Dhar and Chaudhuri (arXiv:2402.11358, originally public 17 February 2024) study the finite overdamped chain of independent run-and-tumble forces with harmonic interactions. Their stationary two-point position correlations and *time-displacement* kurtosis analysis motivate the distinction made here; their reported displacement kurtosis can be either sign, whereas our theorem proves an all-lag sign law for **connected position correlations**, a different observable. The inspected main sections and appendices do not provide the common-active-ancestor fourth-cumulant equivalence across arbitrary cooperative directed graphs. Their special finite-chain model is included as a strictly-negative case for stationary position-connected correlations under pinned boundaries, but not for all of their displacement observables.

Sarkar, Santra and Basu (arXiv:2210.09035, originally public 17 October 2022) compare Gaussian OU and telegraph active reservoirs in an **inertial** harmonic chain, noting identical second-order forcing but different higher-order fluctuation behavior. Its inertial Green functions can change sign; the present exact cooperative sign and topology criterion is not implied by that work. One-site harmonic RTP stationary distributions and their beta-law moments were known earlier and are used here only as a check, not as a novelty claim. Classical fourth-cumulant filtering identities for independent non-Gaussian inputs are also antecedents; the specific telegraph all-time strict sign combined with nonnegative semigroup reachability and the if-and-only-if support classification is the assessed contribution.

## Limitations
The reachability statement identifies **shared active-source ancestry**, not a unique underlying directed graph or the identity or number of individual sources. Rates must be positive, signs fair, and distinct sources independent; correlated or biased active inputs can invalidate the four-time sign formula. Input coefficients must be nonnegative, drift cooperative and stable, and additive noise Gaussian independent of the active signs. The time-integrated formula uses stationary positions: subtracting positions at two different times generally creates signed kernels and need not obey the same sign restriction. Inertial oscillatory networks also need not satisfy the criterion. Four-point zero measurements in finite noisy datasets require statistical inference; the mathematical result concerns population cumulants only. No result is claimed for infinite-dimensional graphs without additional summability and stability hypotheses. An unindexed antecedent on telegraph cumulants in positive linear systems remains a scientific priority risk.

## References
1. S. Paul, A. Dhar, D. Chaudhuri, *Dynamical crossovers and correlations in a harmonic chain of active particles*, arXiv:2402.11358 (first public 2024-02-17), https://arxiv.org/abs/2402.11358.
2. R. Sarkar, I. Santra, U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (first public 2022-10-17), https://arxiv.org/abs/2210.09035.
3. A. Dhar, A. Kundu, S. N. Majumdar, S. Sabhapandit, G. Schehr, *Run-and-tumble particle in one-dimensional confining potentials: Steady-state, relaxation, and first-passage properties*, Phys. Rev. E 99, 032132 (2019), https://doi.org/10.1103/PhysRevE.99.032132.
4. L. D. Lutes, *Cumulants of stochastic response for linear systems*, Journal of Engineering Mechanics 112, 1062 (1986), https://doi.org/10.1061/(ASCE)0733-9399(1986)112:10(1062).
