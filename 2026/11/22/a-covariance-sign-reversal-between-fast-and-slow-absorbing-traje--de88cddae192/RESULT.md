# A covariance sign reversal between fast and slow absorbing-trajectory counts

## Finding

For independent absorbing runs, a fast outcome and a slow outcome are mutually exclusive within a single trial. Nevertheless, the counts of the two outcomes can switch from negative to positive covariance as a finite simulation budget increases. In the marked exponential-renewal model described below, this sign reversal is guaranteed on the sharp open region where the two endpoint-asymptotic signs are opposite:
\[
\frac12<b<\frac{\lambda_1}{\lambda_0+\lambda_1}.
\]
The initial and final signs are established by exact covariance coefficients, not by simulations.

## Assumptions and scope

At time zero, one worker starts a trajectory. Each completed trajectory is independently assigned an unobserved eventual mark \(X\in\{0,1\}\), with \(\Pr(X=1)=b\) and \(\Pr(X=0)=a=1-b\), where \(0<b<1\). Conditional on \(X=i\), its duration is exponential with rate \(\lambda_i>0\). Assume \(\lambda_1>\lambda_0\), so mark 1 completes faster on average. Every completed trajectory is recorded and the worker immediately starts an independent next trajectory. At budget time \(t\ge0\), the final unfinished trajectory, if any, is censored. Let \(R(t)\) and \(F(t)\) denote the numbers of fully completed trajectories with marks 1 and 0, respectively. There is no reset delay or queueing cost. Independent workers follow independent instances of this model.

Put \(c=b\lambda_0+a\lambda_1>0\). The theorem concerns the **unconditional joint count covariance** for a fixed worker at a fixed budget, not the covariance of the proportions conditional on the number of completed trajectories.

## Proof

Define \(f_i(s)=p_i\lambda_i/(s+\lambda_i)\) for \(s>0\), where \(p_1=b\), \(p_0=a\), and \(f(s)=f_0(s)+f_1(s)\). These are the joint Laplace transforms of a trajectory's completion time and outcome. The marked renewal equation yields the exact bivariate probability-generating-function transform
\[
\int_0^\infty e^{-st}\,\mathbb E[z_0^{F(t)}z_1^{R(t)}]dt
=\frac{1-f(s)}{s[1-z_0f_0(s)-z_1f_1(s)]}.
\]
This follows by conditioning on whether the first trajectory is incomplete at \(t\); its survival transform is \((1-f(s))/s\), while a completed first trajectory contributes \(z_i f_i(s)\) and initiates an independent renewed process. Taking the two first derivatives and the mixed derivative at \(z_0=z_1=1\) gives
\[
\mathcal L\{\mathbb EF(t)\}=\frac{f_0}{s(1-f)},\qquad
\mathcal L\{\mathbb ER(t)\}=\frac{f_1}{s(1-f)},\qquad
\mathcal L\{\mathbb E[F(t)R(t)]\}=\frac{2f_0f_1}{s(1-f)^2}.
\]
The rational transforms have poles only at \(s=0\) and \(s=-c\) because
\[
1-f(s)=\frac{s(s+c)}{(s+\lambda_0)(s+\lambda_1)}.
\]
Therefore their inverse transforms are finite linear combinations of polynomials and exponentially decaying terms, and the following expansions are rigorous. Expansion at \(s=\infty\), inversion term by term, and subtraction of the product of the first moments gives
\[
\operatorname{Cov}(F(t),R(t))
=\frac{ab\lambda_0\lambda_1(2b-1)(\lambda_0-\lambda_1)}6t^3+O(t^4)
\quad(t\downarrow0).
\]
The terms of orders zero, one and two cancel. Independently, extract the coefficients of the poles at \(s=0\). The first moments grow linearly, with rates \(a\lambda_0\lambda_1/c\) and \(b\lambda_0\lambda_1/c\). The quadratic terms in the mixed moment and the product of the means cancel. The remaining coefficient is
\[
\operatorname{Cov}(F(t),R(t))
=\frac{ab\lambda_0\lambda_1(\lambda_1-\lambda_0)(a\lambda_1-b\lambda_0)}{c^3}t+O(1)
\quad(t\to\infty).
\]
All omitted terms are bounded at infinity because the only other pole is strictly negative; in fact the remaining nonconstant transients are combinations of \(e^{-ct}\), \(te^{-ct}\) and \(e^{-2ct}\).

Because \(\lambda_1>\lambda_0\), the first nonzero short-time coefficient is negative exactly when \(b>1/2\). The large-time slope is positive exactly when \(a\lambda_1>b\lambda_0\), equivalently \(b<\lambda_1/(\lambda_0+\lambda_1)\). Both occur exactly on the asserted open interval. Covariance is a continuous function of budget because the generating-function transforms invert to continuous exponential-polynomial expressions, so at least one sign change follows by the intermediate-value theorem. Finally, the covariance of sums of independent worker counts is the sum of individual covariances, equal to \(M\) times the expression above.

## Verification

The included \(verify.py\) independently checks the rational transforms, algebraic cubic and linear asymptotic coefficients, and a strict finite-budget sign reversal at \(b=7/10\), \(\lambda_0=1\), \(\lambda_1=5\). At these parameters the covariance is negative at \(t=1/20\) and positive at \(t=1\). This numerical check is auxiliary: the assertion for the entire continuum of admissible parameters rests on the exact rational-transform proof.

## Relationship to prior work

Reia and Fontanari (2026) formulate the same heterogeneous exponential two-outcome renewal model, derive separate mean completion counts and describe the importance of their joint fluctuations for statistical precision. The present claim takes a mixed derivative of the marked renewal transform to find a previously unreported *opposite-sign endpoint regime* for the covariance of fast and slow counts. General marked-renewal transforms and renewal-reward asymptotics are classical mathematical tools, not themselves claimed as new. Earlier non-Poisson resetting and alternating-renewal literature establishes related counting methodology but does not, in inspected material, supply this specific parameter-window sign-reversal statement.

## Limitations

The proof concerns exponential conditional durations with iid marks and durations across trials. It neither classifies all finite-budget sign changes, nor proves that the crossing is unique. The result is not a theorem for arbitrary interacting microscopic absorbing systems or for first-trajectory-only filtering. More general marked-renewal theory could imply the coefficients through known machinery; an unindexed explicit equivalent remains a publication-priority risk. A finite simulation cannot establish the asymptotic continuum statement.

## References

- S. M. Reia and J. F. Fontanari, *Renewal Bias in Parallel Simulations of Absorbing Processes*, arXiv:2611.12692v1 (first submitted 9 November 2026), https://arxiv.org/abs/2611.12692.
- M. R. Evans, S. N. Majumdar and G. Schehr, *Stochastic Resetting and Applications*, Journal of Physics A (2020), https://arxiv.org/abs/1910.07993.
- T. Akimoto, *Statistics of the number of renewals, occupation times, and correlation in ordinary, equilibrium, and aging alternating renewal processes*, Physical Review E **108**, 054113 (2023), https://doi.org/10.1103/PhysRevE.108.054113.
