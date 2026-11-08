# Exact two-density thermodynamic current and square-root noise smoothing in a five-neighbor particle automaton

## Finding

For the stochastic five-neighbor lattice transport rule defined in [1], we give a closed form for its macroscopic *physical* stationary current, at fixed two independent conserved densities, and determine its singular zero-noise boundary layer. The established finite-volume stationary measure and double sum of [1] are premises, not new claims here.

For \(0<\beta\), \(2\beta<\rho<1-\beta\), \(0<\alpha<1\), put
\[
c=1-\rho,\qquad f=\rho-2\beta,\qquad
K=f+c\alpha+\beta(1-\alpha),\qquad
\Delta=K^2-4cf\alpha.
\]
The current and its deterministic reference are
\[
\boxed{Q_\infty(\rho,\beta,\alpha)=\rho-\frac{K-\sqrt\Delta}{2}},
\qquad Q_0(\rho,\beta)=\max\{2\rho-1,2\beta\}.
\]
Strictly, \(Q_0<Q_\infty<\rho\), and \(Q_\infty\) decreases as \(\alpha\) increases. Along \(\rho=(1+2\beta)/2\), \(0<\beta<1/4\),
\[
Q_\infty-Q_0\sim\sqrt{(1-\rho)\beta}\sqrt{1-\alpha}.
\]
For \(\varepsilon=1-\alpha\downarrow0\), assuming \(f-c=\lambda\sqrt\varepsilon+o(\sqrt\varepsilon)\), \(c\to c_0>\beta_0>0\), and \(\beta\to\beta_0>0\), the sharper crossover is
\[
\lim_{\varepsilon\downarrow0}\frac{Q_\infty-Q_0}{\sqrt\varepsilon}
=\frac{\sqrt{\lambda^2+4c_0\beta_0}-|\lambda|}{2}.
\]
In this final formula it is enough to require \(c_0>0\), \(\beta_0>0\) and approach through the strict feasible domain; the stronger displayed \(c_0>\beta_0\) follows on the critical line and is used only to emphasize feasibility.

## Assumptions and scope

We use [1, Section 2 and Corollary 4.3] verbatim for the dynamics, the stationary measure, and the definition of physical current \(Q_u\); in particular the stationary current of the transformed variable is \(Q\), whereas the physical current is \(Q_u=H/L-Q\). The ring has \(L\) sites, \(H\) particles, and \(B\) cyclic occurrences of the local word \(110\), with \(B\ge1\), \(F=H-2B\ge1\), and \(A=L-H-B\ge1\). Let \(C=L-H=A+B\). The noise variable \(\alpha\) obeys \(0<\alpha<1\).

The limit is for *any* integer sequences with \(H/L\to\rho\) and \(B/L\to\beta\) in the strict feasible interior; initial distributions may be arbitrary on the fixed-conservation sector because [1, Corollary 4.3] proves their stationary physical current is equal. The source's finite-volume distribution (not this work) supplies that premise. The limiting analysis concerns particle transport, rather than a classification of cellular automata.

## Proof

**1. Exact coefficient identity.** Let \(k_1=\#1110\) and \(k_2=\#010\). The universal finite-volume factor \(N(k_1,k_2)\) from [1, Eq. (18)] counts the allocations of \(F\) free particles among \(A\) minus-sites (at most one extra particle) and \(B\) plus-sites (arbitrarily many extras). The total stationary weight is proportional to \(\alpha^{k_2}(1-\alpha)^{-(k_1+k_2)}\). Setting \(v=\alpha/(1-\alpha)\), the one-site generating factors are
\[
g_-(z)=1+vz,\qquad
g_+(z)=1+\frac{z}{(1-\alpha)(1-z)}=\frac{1+vz}{1-z}.
\]
Consequently the normalized-relevant partition coefficient is exactly
\[
Z_L=[z^F](1+vz)^C(1-z)^{-B}.
\]
Here \([z^F]\) denotes coefficient extraction; the component-dependent multiplier from [1, Proposition 4.2] cancels in all expectations. In particular this is a re-expression of [1]'s proved finite-volume double sum, not a new stationary-measure formula.

For the transformed stationary flux numerator \(\alpha k_1+k_2\), differentiating the one-site weights with respect to its contribution yields \(vz\) on a minus-site and \(\alpha z/((1-\alpha)(1-z))=vz/(1-z)\) on a plus-site. In both cases the marked-to-unmarked factor is \(vz/(1+vz)\). Therefore
\[
\mathbb E(\alpha k_1+k_2)=
Cv\frac{[z^{F-1}](1+vz)^{C-1}(1-z)^{-B}}
{[z^F](1+vz)^C(1-z)^{-B}},
\]
and the finite physical current is \(H/L\) minus this expectation divided by \(L\).

**2. Conditional independent-occupation representation and thermodynamic limit.** Choose \(z\in(0,1)\), and write \(t=vz/(1+vz)\). The coefficient measure is the law of \(C\) independent Bernoulli variables with success probability \(t\), together with \(B\) independent geometric variables on nonnegative integers with success mass \((1-z)z^j\), all conditioned to have total sum \(F\). To see this, multiply the normalized Bernoulli and geometric probability generating functions: their product equals \((1+vzx)^C(1-zx)^{-B}\) times a factor independent of \(x\). The marking identity in step 1 identifies the flux expectation with the conditional mean number of Bernoulli successes.

For each sufficiently large \(L\), there is a unique \(z_L\in(0,1)\) for which the unconditioned expected total is \(F\). Its equation is
\[
\frac{F}{L}=\frac{C}{L}\frac{vz_L}{1+vz_L}
+\frac{B}{L}\frac{z_L}{1-z_L}.
\]
The left side is fixed and the right side increases strictly from zero to infinity, so uniqueness is exact. In the strict interior with \(\alpha\) fixed, \(z_L\to z_*\in(0,1)\), the unique root of
\[
f=c\frac{vz_*}{1+vz_*}+\beta\frac{z_*}{1-z_*}.
\]
The unconditioned sum is a lattice triangular array with variance proportional to \(L\), uniformly bounded exponential moments for sufficiently large \(L\), and lattice span one. Its local central limit theorem at its mean gives, for one tagged Bernoulli, the ratio of the probabilities of total \(F-1\) among the remaining summands and of total \(F\) among all summands tending to one. Thus, conditioned on the total \(F\), the tagged success probability tends to \(t_*=vz_* /(1+vz_*)\). Exchangeability among the \(C\) Bernoulli slots and step 1 yield
\[
\lim_{L\to\infty}Q_u=\rho-ct_*.
\]
This local-limit argument is valid for every integer approach to the same interior densities; it does not exchange the size and zero-noise limits.

**3. Explicit saddle solution.** Since \(z_*=t_*/(v(1-t_*))\),
\[
\frac{z_*}{1-z_*}=\frac{(1-\alpha)t_*}{\alpha-t_*},
\qquad 0<t_*<\alpha.
\]
Hence \(f=ct_*+\beta(1-\alpha)t_*/(\alpha-t_*)\). Multiplying by \(\alpha-t_*\) yields
\[
ct_*^2-Kt_*+f\alpha=0.
\]
The left side at zero is positive and at \(\alpha\) is \(-\alpha\beta(1-\alpha)<0\), so the physical solution is the *smaller*, strictly real root \(t_*=(K-\sqrt\Delta)/(2c)=2f\alpha/(K+\sqrt\Delta)\). Substitution proves the closed form.

**4. Monotonicity and deterministic boundary.** For fixed \(t\in(0,\alpha)\), the right side of the fugacity equation in step 3 decreases strictly as \(\alpha\) increases, while it increases strictly in \(t\). Consequently \(t_*\) increases strictly with \(\alpha\), so \(Q_\infty\) decreases. The equation gives \(t_*<f/c\) and also \(t_*<\alpha<1\); thus \(ct_*<\min(f,c)\), proving \(Q_\infty>\rho-\min(f,c)=Q_0\). The quadratic at \(\alpha\uparrow1\) has limiting roots \(f/c\) and \(1\), so \(t_*\to\min(f/c,1)\).

**5. Critical scaling.** Let \(\varepsilon=1-\alpha\) and \(\delta=f-c\). The discriminant identity is *exact*:
\[
\Delta=\delta^2+
\varepsilon\{2(f+c)(\beta-c)+4cf\}+
\varepsilon^2(\beta-c)^2.
\]
Subtracting \(Q_0=\rho-(f+c-|\delta|)/2\) from the proved closed form gives
\[
Q_\infty-Q_0=\tfrac12\left(\sqrt\Delta-|\delta|-(\beta-c)\varepsilon\right).
\]
If \(\delta=0\), the leading radicand term is exactly \(4c\beta\varepsilon\), proving the square-root cusp. If \(\delta/\sqrt\varepsilon\to\lambda\), \(c\to c_0\), and \(\beta\to\beta_0\), the radicand divided by \(\varepsilon\) tends to \(\lambda^2+4c_0\beta_0\), proving the full crossover function.

## Verification

The included `check.py` uses only the Python 3 standard library. It compares the original double sum of [1, Eq. (21)] with the coefficient and marked-coefficient identities using exact rational arithmetic on a broad exact finite grid, and checks finite grids of strict monotonicity and crossover examples. Run `python3 check.py` in the package directory. The exact finite checks and numerical limiting examples are supplementary; the infinite-volume assertion follows from the conditional local central limit theorem and subsequent algebra.

## Relationship to prior work

[1] establishes the stationary weights, universal combinatorial factor, finite canonical flux and the deterministic \(\alpha\uparrow1\) limit. This result does not re-claim them. Its further step is an explicit thermodynamic flux surface at positive noise, together with the strictly positive noise enhancement and a quantified two-density square-root crossover. [2], an older conjectural preprint of the *same* stochastic five-neighbor system, gives finite-size weighted flux and the deterministic limit but not the thermodynamic critical crossover; its speculative stationary assumption was subsequently proved by [1]. [3] proves the deterministic flux crease without positive noise. [4] and its earlier references derive square-root flux expressions for other, one-density stochastic automata; this shows that square roots themselves are not novel. No assertion of priority over an unindexed general equivalence or transport formula is made.

## Limitations

The result applies only to the strict interior domain and to the specified five-neighbor rule; it does not classify all interacting particle systems. The bulk size limit is taken at fixed nonzero noise, followed by the zero-noise limit; no uniform finite-size crossover is claimed. All finite stationary-measure input comes from [1]. The local central limit step requires positive limiting densities and a fixed \(0<\alpha<1\), and the proof does not supply finite-size error constants. The crossover concerns stationary *physical* current, not entropy production or fluctuation spectra. General earlier transport asymptotics may still imply the same specialization.

## References

1. K. Endo, S. Iwao, H. Nagai and Y. Nakano, *Stationary Measures and Mean Flux Depending on Multiple Conserved Quantities in a Stochastic Cellular Automaton*, arXiv:2605.28052v1 (first public 2026-05-27). https://arxiv.org/pdf/2605.28052
2. K. Endo, *Asymptotic behavior of a stochastic particle system of 5 neighbors*, arXiv:2202.02499v1 (2022-02-05). https://arxiv.org/pdf/2202.02499
3. K. Endo and D. Takahashi, *Three-dimensional fundamental diagram of particle system of 5 neighbors with two conserved densities*, arXiv:2112.12929v1 (2021-12-24). https://arxiv.org/pdf/2112.12929
4. K. Endo, D. Takahashi and J. Matsukidaira, *On fundamental diagram of stochastic cellular automata with a quadratic conserved quantity*, NOLTA 7 (2016), 313–323, doi:10.1587/nolta.7.313. https://www.jstage.jst.go.jp/article/nolta/7/3/7_313/_pdf
