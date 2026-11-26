# Log-Pareto central concentration in a harmonically confined intermittent swimmer

## Finding

For a one-dimensional swimmer with deterministic propulsion episodes followed by independent Lomax-distributed inactive episodes, harmonic confinement converts a power-law *time* tail into an integrable, almost inverse-linear singularity of the stationary *position* density. Specifically, with the definitions below, the unique stationary position density satisfies

\[
p_*(x)\sim \frac{C_\alpha}{x[\log(L/x)]^\alpha},\qquad
\mathbb P_*(0<X\le x)\sim \frac{C_\alpha}{\alpha-1}[\log(L/x)]^{1-\alpha}
\quad(x\downarrow0),
\]

where

\[
C_\alpha=\frac{\mu^{\alpha-1}\theta^\alpha}{h+\theta/(\alpha-1)}.
\]

There is no stationary point mass at the trap center, even though the density diverges there. Moreover every inverse position moment diverges: \(\mathbb E_*[X^{-q}]=\infty\) for all \(q>0\). The leading coefficient is independent of propulsion speed; that speed only sets the logarithmic length scale \(L\). This is a logarithmic rather than the algebraic central singularity associated with exponentially distributed inactive periods.

## Assumptions and scope

Fix \(\mu,v,h,\theta>0\) and \(\alpha>1\). The position is a real variable with piecewise deterministic dynamics

\[
\dot X=-\mu X+v\quad\text{during each run of duration }h,\qquad
\dot X=-\mu X\quad\text{during each inactive period}.
\]

The inactive durations \(U_1,U_2,\ldots\) are independent with survival function

\[
\Pr(U_n>t)=(1+t/\theta)^{-\alpha},\quad t\ge0.
\]

Every run is followed by an inactive period and vice versa. The durations are independent of the previous state. Let \(L=v/\mu\), \(B=e^{-\mu h}\), \(a=L(1-B)>0\), and \(m=h+\theta/(\alpha-1)\). Observation is made in the stationary alternating-renewal regime, not at a freshly started episode. The phase process includes elapsed age as necessary; no thermal translational noise is assumed. We state asymptotics of the invariant continuous position law, not a convergence rate from an arbitrary synchronization.

## Proof

**Stationary entrance chain.** Let \(Z_n\) denote the position at the start of the \(n\)-th run, and \(Y_n\) the position immediately after it. The deterministic and inactive flows give

\[
Y_n=a+BZ_n,\qquad Z_{n+1}=e^{-\mu U_n}Y_n.
\]

On \([0,L]\) these maps are contractions in the starting position with Lipschitz factor at most \(B<1\). A two-sided independent sequence of inactive durations therefore produces a unique stationary entrance chain by backward iteration; every stationary \(Y_n\) lies in \([a,L]\) almost surely. In particular, the current \(U_n\) is independent of \(Y_n\). Since the mean cycle duration is finite, the renewal-reward construction yields a stationary continuous-time position law, and contraction gives its uniqueness.

**Occupation formula.** Write \(S(t)=(1+t/\theta)^{-\alpha}\). At an inactive episode entered at position \(Y\), the trajectory is \(Ye^{-\mu t}\). For any nonnegative test function \(g\), the stationary inactive contribution is exactly

\[
\frac1m\,\mathbb E\int_0^U g(Ye^{-\mu t})\,dt
=\frac1m\,\mathbb E\int_0^\infty S(t)g(Ye^{-\mu t})\,dt.
\]

Here the expectation on the right is taken over stationary \(Y\), independent of the upcoming \(U\). Changing variables gives, for \(0<x<a\), the exact inactive density

\[
p_{\mathrm{off}}(x)=\frac{1}{\mu m x}\,\mathbb E\left[S\left(\frac1\mu\log\frac{Y}{x}\right)\right].
\]

During the active episode entered at \(Z\), \(X(t)=L+(Z-L)e^{-\mu t}\) increases monotonically (except for a null boundary case), with instantaneous speed \(\mu(L-X)\). Thus the stationary active occupation density satisfies the explicit bound

\[
0\le p_{\mathrm{on}}(x)\le \frac{1}{m\mu(L-x)}\qquad(0<x<L).
\]

This bound follows because each active trajectory crosses a given position at most once, and its occupation density on a crossing is the reciprocal speed.

**Uniform asymptotics.** Since \(a\le Y\le L\), the logarithm obeys

\[
\log(L/x)+\log(a/L)\le \log(Y/x)\le\log(L/x).
\]

As \(x\downarrow0\), the ratio of the two extreme values of \(S\) in the preceding density formula tends to one. Hence, uniformly over the unknown entrance law,

\[
\mathbb E S\left(\mu^{-1}\log(Y/x)\right)
\sim (\mu\theta)^\alpha[\log(L/x)]^{-\alpha}.
\]

The inactive density is therefore asymptotic to \(C_\alpha/[x(\log(L/x))^\alpha]\), while the active density remains bounded at the origin. This proves the first asymptotic and shows explicitly that the entrance distribution does not appear in its leading constant.

**Small ball and moment limits.** Directly integrate the inactive occupation formula for \(0<x<a\):

\[
\Pr_*(X\le x,\mathrm{off})
=\frac{\theta}{(\alpha-1)m}\,\mathbb E\left[\left(1+\frac{\log(Y/x)}{\mu\theta}\right)^{1-\alpha}\right].
\]

The same uniform squeeze yields the stated small-ball asymptotic. The active-phase mass below \(x\) is at most \(x/[m\mu(L-x)]\), negligible compared with every negative power of \(\log(L/x)\). All trajectories at finite episode ages have strictly positive positions, so the stationary law has no atom at zero. Finally, the displayed density lower bound implies divergence of \(\int_0^a x^{-q}p_*(x)dx\) for every \(q>0\), completing the proof.

## Verification

The included standalone `check.py` uses the exact occupation identity, the contractive entrance recursion, and explicit analytic upper and lower bounds on the logarithmic asymptotic ratios. It tests nondegenerate parameter choices, checks the constants against both density and small-ball expressions at independently chosen logarithmic scales, and checks the residence-time normalizations used in the exact formulas. The script is a finite diagnostic, not the proof of the limits; those limits follow from the uniform squeeze and the finite mean of the Lomax law.

## Relationship to prior work

Basu, Majumdar, Rosso, Sabhapandit and Schehr (2019) exactly classify the central singularity of a Markovian three-state run-and-tumble particle in a harmonic trap, finding algebraic and critical logarithmic behaviors. Their switching is exponential, unlike the heavy-tailed inactivity here. Datta, Beta and Großmann (first publicly posted 2024) treat intermittent run/turn motion with general waiting-time laws, deriving free-space transport and anomalous diffusion, and identify external fields as a further direction; their model does not establish confined stationary small-position densities. Farago and Smith (2024) allow non-exponential switching in a confined *two-velocity* run-and-tumble model; their propulsion remains \(\pm v\), and their exact numerical steady-state framework does not include zero-velocity inactive sojourns or the claimed logarithmic singularity. Sun, Ye and Podgornik (2024) incorporate finite zero-velocity tumbles in harmonic confinement, but the switching is exponential in both states. Um, Song and Jeon (2019) study telegraphically driven Langevin motion and its time statistics, rather than this renewal-age central small-ball law. The renewal-reward identity and inspection-paradox residual lifetime are standard ingredients; the physical confinement transformation and sharp constants are the assessed contribution.

## Limitations

This is a one-sided directed run/zero-speed rest model with a fixed positive run duration and no thermal translational noise. The statement does not claim the same leading constant for sign-changing propulsion, run durations approaching zero, or thermal diffusion. A strictly stronger published result on this exact confined non-Markovian model would cover this claim; the literature and database comparisons listed in the accompanying review reduce but cannot eliminate that priority risk. The result is not a phase-transition claim for all three-state active particle models.

## References

- U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083v1, publicly posted 2019-10-22. https://arxiv.org/abs/1910.10083
- A. Datta, C. Beta and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277v1, publicly posted 2024-06-21; later revisions exist. https://arxiv.org/abs/2406.15277
- O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576v1, 2024-01-03. https://arxiv.org/abs/2401.01576
- A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1, 2024-09-01. https://arxiv.org/abs/2409.00578
- J. Um, T. Song and J.-H. Jeon, *Langevin Dynamics Driven by a Telegraphic Active Noise*, Frontiers in Physics 7, 143 (2019), 2019-10-18. https://doi.org/10.3389/fphy.2019.00143
