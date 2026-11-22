# A sharp reset-clock envelope for orthogonal extreme fronts in a planar Brownian gas

## Finding

Consider \(N\ge 2\) planar Brownian particles, each with diffusivity \(D>0\), driven by independent Brownian noises but reset *simultaneously* to the origin at the events of one stationary renewal clock. Let the independent, identically distributed strictly positive inter-reset durations be \(S\) with \(0<\mathbb E S<\infty\) and \(\mathbb E S^2<\infty\). At a stationary observation time, write \(F_N^x=\max_{1\le i\le N}X_i\) and \(F_N^y=\max_{1\le i\le N}Y_i\), and let \(\rho_N=\operatorname{Corr}(F_N^x,F_N^y)\).

**Theorem (one coupled size-and-shape law).** For every such clock and every \(N\ge2\), \(0<\rho_N<1\). There is a clock-specific constant \(K(S)\) such that

\[
\lim_{N\to\infty}(\log N)^2(1-\rho_N)=K(S)
=\frac{\pi^2}{24\left[1-\frac89\frac{(\mathbb E S^{3/2})^2}{(\mathbb ES)(\mathbb ES^2)}\right]}.
\]

Its **complete sharp attainable interval**, over all admissible renewal clocks, is

\[
\boxed{\frac{\pi^2}{24}<K(S)\le\frac{3\pi^2}{8}.}
\]

The upper endpoint is attained **only** by deterministic inter-reset durations; the lower endpoint is not attained but is approached by explicit two-point clock distributions. Every intermediate value is attained. A Poisson clock with any rate has \(K=\pi^2/[6(4-\pi)]\).

Simultaneously, the *scale-free angular asymmetry* has a protocol-independent limit:

\[
\boxed{\log N\left(\frac{F_N^x}{F_N^y}-1\right)\ \Longrightarrow\ L/2,\qquad
\Pr(L\le t)=\frac1{1+e^{-t}}.}
\]

For every finite \(N\), the ratio \(F_N^x/F_N^y\) is itself independent in distribution of the reset clock and \(D\), and is independent of the stationary reset age. These assertions concern coordinatewise **extrema over the same planar particle cloud**, not independent particle clouds in different experiments.

## Assumptions and scope

The renewal clock is independent of all particle noises. A stationary observation time samples the equilibrium backward recurrence age \(A\), whose density is \(\Pr(S>t)/(\mathbb ES)\) for \(t>0\). The reset is instantaneous and sets **both coordinates of all particles** to zero; there are no interactions, forces or additional individual reset clocks. Finite second interarrival moment ensures \(\mathbb EA<\infty\), making all Pearson correlations well defined. \(F_N^y=0\) has probability zero, so the ratio is defined almost surely. The theorem does not assert properties of spatially radial maxima, convex-hull perimeter or successive-particle gaps.

Write \(M_N=\max(Z_1,\ldots,Z_N)\) for independent standard normals, \(m_N=\mathbb EM_N>0\), and \(v_N=\operatorname{Var}(M_N)>0\). The finite-\(N\) exact identity is

\[
\rho_N=\frac{\Delta m_N^2}{\Delta m_N^2+(\mathbb EA)v_N},\qquad
\Delta=\mathbb EA-(\mathbb E\sqrt A)^2>0.
\]

For reference, \(\rho_2=(4-\pi)/(3\pi)\) for Poisson resetting; \(\rho_1=0\) is outside the theorem's strict-positivity range. The joint macroscopic limit is \((F_N^x,F_N^y)/\sqrt{4D\log N}\Rightarrow(\sqrt A,\sqrt A)\).

## Proof

**1. Stationary Gaussian scale mixture.** Conditional on the elapsed age \(A=t\), every particle is a centered isotropic Gaussian vector with independent coordinate variance \(2Dt\), and vectors from different particles are conditionally independent. Consequently, on one probability space,

\[
(F_N^x,F_N^y)\overset d=\sqrt{2DA}\,(M_N^{(x)},M_N^{(y)}),
\]

where the maxima on the right are independent copies of \(M_N\), independent of \(A\). The age identity follows directly by averaging the time spent at each age in a renewal interval. Its moment identity is

\[
\mathbb EA^p=\frac{\mathbb ES^{p+1}}{(p+1)\mathbb ES}\quad(p>-1\text{ for which the right-hand side is finite}).
\]

**2. Exact covariance.** Independence conditional on \(A\) gives

\[
\operatorname{Cov}(F_N^x,F_N^y)=2D\,[\mathbb EA-(\mathbb E\sqrt A)^2]m_N^2
\]

and \(\operatorname{Var}(F_N^x)=2D[(\mathbb EA)v_N+\Delta m_N^2]\). Since \(A\) is nondegenerate, \(\Delta>0\). For \(N\ge2\), \(m_N>0\) because the maximum strictly exceeds the sample average with positive probability (and has nonnegative expected sample average). This proves the finite-\(N\) formula and strict bounds. For \(N=2\), symmetry of two normal samples gives \(m_2=1/\sqrt\pi\) and \(v_2=1-1/\pi\), yielding the stated Poisson anchor.

**3. Sharp logarithmic approach.** Let \(b_N=\Phi^{-1}(1-1/N)\) for \(N\ge3\). The standard Gaussian Mills-ratio estimates imply \(b_N\sim\sqrt{2\log N}\) and

\[
\Pr\{b_N(M_N-b_N)\le z\}=\Phi(b_N+z/b_N)^N\longrightarrow e^{-e^{-z}}.
\]

For completeness, the normal upper-tail hazard is increasing, which bounds the positive normalized tail by \(e^{-z}\). For the negative normalized tail, split at \(z=b_N^2/2\): Mills-ratio bounds give a double-exponential estimate before this point, while beyond it \(\Phi(b_N-z/b_N)^N\) gives an integrable Gaussian-power bound. This establishes uniform integrability of squared normalized fluctuations and hence the classical moment limits

\[
\mathbb EM_N=b_N+\frac{\gamma}{b_N}+o(b_N^{-1}),\qquad
v_N=\frac{\pi^2}{6b_N^2}+o(b_N^{-2}).
\]

Here \(\gamma\) is Euler's constant. Thus \((\log N)^2v_N/m_N^2\to\pi^2/24\). Substituting in the exact covariance identity gives

\[
\lim_{N\to\infty}(\log N)^2(1-\rho_N)=\frac{\pi^2}{24}\frac{\mathbb EA}{\Delta}.
\]

**4. Optimal clock envelope.** With \(u=\mathbb ES\), \(w=\mathbb ES^{3/2}\) and \(z=\mathbb ES^2\), the age moment identity yields

\[
\frac{(\mathbb E\sqrt A)^2}{\mathbb EA}=
\frac89\frac{w^2}{uz}.
\]

Cauchy–Schwarz gives \(0<w^2\le uz\), and equality occurs exactly when \(S\) is constant almost surely. It follows that \(\pi^2/24<K(S)\le3\pi^2/8\), with equality at the upper endpoint only for periodic resets sampled at stationary phase. For \(L>1\), choose \(S_L=L\) with probability \(L^{-7/4}\) and \(S_L=1\) otherwise. As \(L\to\infty\), \(\mathbb ES_L\to1\), \(\mathbb ES_L^{3/2}\to1\), but \(\mathbb ES_L^2\sim L^{1/4}\to\infty\); thus \(K(S_L)\to\pi^2/24\) in the limit. To attain any intermediate value, continuously vary the two-point mixing probability from zero (deterministic \(S=1\)) to \(L^{-7/4}\), choosing \(L\) large enough that the endpoint coefficient is below the target. Continuity and the intermediate-value theorem complete sharp attainability. For exponential interarrivals, substitution of gamma moments gives the Poisson constant.

**5. Clock-free ratio law.** The common positive Gaussian multiplier cancels exactly in \(F_N^x/F_N^y=M_N^{(x)}/M_N^{(y)}\). Joint Gaussian-maximum convergence gives independent standard Gumbels \(G_x,G_y\) as the limits of \(b_N(M_N^{(x)}-b_N)\) and \(b_N(M_N^{(y)}-b_N)\). Therefore

\[
\log N\left(\frac{M_N^{(x)}}{M_N^{(y)}}-1\right)
=\frac{\log N}{b_N^2}\frac{b_N(M_N^{(x)}-M_N^{(y)})}{M_N^{(y)}/b_N}
\ \Longrightarrow\ \frac{G_x-G_y}{2}.
\]

For independent standard Gumbels, \(G_x-G_y\) is standard logistic (e.g. write \(e^{-G_x},e^{-G_y}\) as independent mean-one exponentials). This completes the theorem. Gaussian extreme concentration also gives the stated diagonal joint limit.

## Verification

Run \(\texttt{python verify.py}\) with Python 3, NumPy and SciPy. The checker evaluated 83 deterministic assertions, including the exact \(N=2\) identity; Gaussian-max density normalization and variance; large-\(N\) approach to the exact logarithmic coefficient; the Cauchy–Schwarz envelope; a two-point clock sequence approaching the unattained endpoint; scale cancellation; and the half-logistic limit. Its fixed-seed Gumbel sampling tests only the predicted distribution numerically, and is **not** used in the proof of the infinite-population limit.

## Relationship to prior work

Biroli, Larralde, Majumdar and Schehr, arXiv:2211.00563 (first made public 2022-11-01), derive the common-reset Gaussian scale mixture for a **one-dimensional** Brownian gas, including single-axis extreme and gap statistics. De Mauro, Biroli, Majumdar and Schehr, arXiv:2509.06658 (first made public 2025-09-08), extend one-dimensional conditional-independence and extremal results to renewal reset protocols. Those forward results are used as premises, not represented as new. The present theorem concerns a different joint observable—**the correlation and ratio of orthogonal extrema of the same planar configuration**—and proves a sharp functional envelope over the reset interarrival law. Standard Gaussian Gumbel asymptotics are also used and are not claimed as new.

Search comparisons with indexed results on stationary edge-gap covariance under common renewal resets and on logarithmic imbalance of one-dimensional spatial extremes identified different observables and no implication that supplies this two-axis correlation envelope. The comparison does not establish exhaustive publication priority; see limitations.

## Limitations

The theorem is for planar **free**, isotropic Brownian particles under **whole-system**, instantaneous resetting. In the correlation statement it requires an equilibrium renewal age with finite mean, equivalently a finite second moment of \(S\), and a stationary random observation phase. It does not cover independently reset coordinates, direction-dependent diffusion, finite sampling error, or finite-population optimization of the coefficient. Gaussian maxima and renewal-age identities are standard prerequisites. No independent mathematical audit has been performed. An unindexed or inaccessible equivalent treatment of the two-axis extreme statistics remains a possible priority risk.

## References

1. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first public 2022-11-01), https://arxiv.org/abs/2211.00563 .
2. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first public 2025-09-08), https://arxiv.org/abs/2509.06658 .
3. E. J. Gumbel, *Statistics of Extremes*, Columbia University Press, 1958 (classical maximum asymptotics).
