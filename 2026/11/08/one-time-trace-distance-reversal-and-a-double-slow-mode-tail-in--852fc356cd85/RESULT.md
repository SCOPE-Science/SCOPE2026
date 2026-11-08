# One-time trace-distance reversal and a double-slow-mode tail in a Dicke population cascade

## Finding

For every integer \(N\geq3\), decay rate \(\Gamma>0\), intermediate Dicke excitation \(1\leq m<N\), and mixture weight \(0<b<1\), consider the zero-temperature collective-emission population cascade with rates \(\lambda_k=\Gamma k(N-k+1)\). Compare the diagonal initial states \(\rho_A=|m\rangle\langle m|\) and \(\rho_B=(1-b)|0\rangle\langle0|+b|N\rangle\langle N|\).

Write \(\Delta_j(t)\) for trace distance from the stationary ground state when starting at level \(j\), and \(Q_j(t)\) for the expected number of excitations. Then **there is exactly one positive time \(t_\Delta\)** such that \(\Delta_m(t_\Delta)=b\Delta_N(t_\Delta)\). The strict ordering is \(\Delta_m>b\Delta_N\) before this time, and \(\Delta_m<b\Delta_N\) afterwards. For any fixed \(N,m,b,\Gamma\), both the trace-distance ratio and the mean-excitation ratio satisfy

\[
\frac{\Delta_m(t)}{b\Delta_N(t)}\sim
\frac{Q_m(t)}{bQ_N(t)}\sim
\frac{m}{b\Gamma N(N-1)(N-m)}\,\frac1t
\quad(t\to\infty).
\]

If additionally \(m>bN\), the mean-excitation ordering also reverses at least once, though uniqueness of an energy crossing is not established here. In particular the preparation \(m=\lceil2N/3\rceil\), \(b=1/2\) has one and only one trace-distance crossing and at least one energy crossing for **every** \(N\geq3\), extending the published finite-size observations for \(6\leq N\leq60\).

## Assumptions and scope

The Hilbert-space dynamics is restricted to the symmetric Dicke excitation ladder \(k=0,1,\dots,N\) and to density matrices diagonal in this basis. There is one collective, zero-temperature jump channel: the population moves \(k\to k-1\) at rate \(\lambda_k=\Gamma k(N-k+1)\). The ground level \(0\) is absorbing. There are no individual emission channels, pumping, dephasing, coherent drives, dark-state occupations or other decoherence mechanisms. The trace distance is \(\frac12\|\rho(t)-|0\rangle\langle0|\|_1\), and the mean-excitation observable is \(\sum_k k\langle k|\rho(t)|k\rangle\); a constant transition energy multiplies the latter without changing comparisons.

Let \(T_j\) be the time to reach level \(0\) from \(j\), and set \(S_j(t)=\Pr\{T_j>t\}\). For these diagonal states \(\Delta_j(t)=S_j(t)\) exactly. For \(t\geq0\), \(Q_j(t)=\mathbb E[X_t\mid X_0=j]\). The mixture \(\rho_B\) has observables \(bS_N(t)\) and \(bQ_N(t)\) because its ground-state component is stationary. All asymptotics are for fixed \(N\) and \(\Gamma\) as \(t\to\infty\), not uniform in joint limits \(N,t\to\infty\).

## Proof

**1. Independent holding times and the repeated endpoint rate.** The successive holding times \(E_k\) in levels \(k=j,j-1,\ldots,1\) are independent exponentials with rates \(\lambda_k\), so \(T_j\) has the law of \(\sum_{k=1}^jE_k\). Put \(a=\Gamma N\). Then \(\lambda_1=\lambda_N=a\), whereas for \(2\leq k\leq N-1\),

\[
\lambda_k-a=\Gamma(k-1)(N-k)>0.
\]

Thus an initial level below \(N\) sees just one slow exponential; an initially fully excited state encounters two equally slow exponentials separated by faster levels.

**2. Strict monotonicity and uniqueness.** The density of each \(E_k\) is log-concave on \(\mathbb R\) (zero off the nonnegative axis). Closure under convolution, or equivalently the Prékopa integral theorem, makes the density of \(T_m\) log-concave. Integrating this density over \([t,\infty)\) shows that its survival \(S_m\) is log-concave; hence its hazard \(h_m(t)=-\frac{d}{dt}\log S_m(t)\) is nondecreasing for \(t>0\). The density is positive for \(t>0\), so \(h_m(t)>0\).

Write \(V=\sum_{k=m+1}^{N}E_k\), independent of \(T_m\), and extend \(S_m(u)=1\) for \(u\leq0\). For each fixed \(v>0\), the function \(R_v(t)=S_m(t-v)/S_m(t)\) is nondecreasing in \(t>0\). For \(0<t<v\), its logarithmic derivative is \(h_m(t)>0\); for \(t>v\), it is \(h_m(t)-h_m(t-v)\geq0\). Therefore

\[
\frac{S_N(t)}{S_m(t)}=\mathbb E[R_V(t)]
\]

is **strictly** increasing: for every finite \(t>0\), \(\Pr(V>t)>0\), and the integrand is strictly increasing on that positive-probability set. The ratio begins at \(1\) when \(t=0\). Step 3 shows that it tends to infinity, so there is precisely one solution of \(S_N(t)/S_m(t)=1/b>1\), with the claimed signs on either side. (The use of log-concavity and its marginalization is a standard mathematical tool, not a newly claimed theorem.)

**3. Exact leading tails.** For \(j<N\), let \(W_j=\sum_{k=2}^{j}E_k\), empty when \(j=1\). The exponential moment at \(a\) is finite and telescopes:

\[
C_j=\mathbb E[e^{aW_j}]
=\prod_{k=2}^{j}\frac{\lambda_k}{\lambda_k-a}
=\prod_{k=2}^{j}\frac{k(N-k+1)}{(k-1)(N-k)}
=\frac{j(N-1)}{N-j}.
\]

Convolving \(W_j\) with the remaining \(E_1\sim\mathrm{Exp}(a)\) gives \(S_j(t)=C_j e^{-at}(1+o(1))\). For \(j=N\), the two independent endpoint holding times \(E_1,E_N\) sum to an Erlang shape-two variable, independent of \(W_{N-1}\). Its survival is \(e^{-at}(1+at)\), so

\[
S_N(t)=\bigl[a C_{N-1}\,t+O(1)\bigr]e^{-at}
=\bigl[\Gamma N(N-1)^2t+O(1)\bigr]e^{-\Gamma Nt}.
\]

For \(j<N\), the probability of still occupying a level \(\geq2\) is the tail of \(\sum_{k=2}^jE_k\), which decays strictly faster than \(e^{-at}\). For \(j=N\), the same probability is \(O(e^{-at})\), due to the single slow level \(N\). Consequently \(Q_j(t)\sim S_j(t)\) for both \(j=m\) and \(j=N\), proving the two stated ratio limits. The spectral double-root factor is precisely the source of the \(t^{-1}\) reversal ratio.

**4. Energy reversal and an independent-decay control.** At time zero, \(Q_m(0)=m\) while the mixed state's energy is \(bQ_N(0)=bN\). If \(m>bN\), this first difference is positive, while the proven ratio tends to zero. Continuity supplies at least one finite energy crossing. By contrast, for independent spontaneous emission, \(Q_j(t)=j e^{-\Gamma t}\) and \(S_j(t)=1-(1-e^{-\Gamma t})^j\). Concavity of \(j\mapsto1-u^j\) for \(0<u<1\) yields \(S_m(t)\geq(m/N)S_N(t)>bS_N(t)\) if \(m>bN\). Independent decay therefore has neither reversal for such preparations.

## Verification

The standalone `verify.py` program evaluates exact rational telescoping identities for \(3\leq N\leq50\), integrates the finite-state Markov generator for selected sizes, tests the strict decrease and numerical crossing on finite time grids, checks the leading tail coefficient within finite-time tolerances, and compares independent-emitter dynamics. Run from the extracted package with `python verify.py` (requires NumPy and SciPy). Its finite checks are consistency tests; the preceding analytic argument proves all positive-time and all-integer-size statements.

## Relationship to prior work

Santos and collaborators, *Superradiant Mpemba Relaxation in a Dicke Ladder* (arXiv:2609.25359, first public September 21, 2026), establish the Dicke rates and motivating mixed-versus-intermediate preparations, reporting crossed diagnostics for examined \(6\leq N\leq60\). Those rates, preparations, the existence of superradiant Mpemba behavior for those sizes, and general pure-death holding-time methods are **not** claimed as new. The contribution here is a sharp all-\(N\) comparative theorem, unique crossing for the trace-distance diagnostic, a full family \((m,b)\), and an explicit polynomial-over-exponential late-time coefficient.

Exact Dicke-population solution methods were already developed by Holzinger and Genes, *An exact analytical solution for Dicke superradiance* (arXiv:2409.19040, first released 2024), and later work of Poddar and collaborators, *Exact Analytical Treatment of Collectively Pumped Dicke Superradiance* (arXiv:2610.37665, October 27, 2026), treats a pumped ladder with general symmetric initial states. The present theorem compares two specific state preparations under zero pumping and classifies their crossing, rather than claiming a new general population propagator.

## Limitations

The idealized one-channel Dicke ladder assumption is essential; additional decay pathways, dephasing, pumping or symmetry-breaking can destroy the endpoint eigenvalue degeneracy. Uniqueness is proved for **trace distance**, not for energy crossings. Late-time asymptotics are for fixed size and need not describe a finite observation interval at very large \(N\). The asymptotic coefficient and general structural argument derive from standard exponential-sum and log-concavity facts. A direct independent publication-priority audit has not been carried out: complete text of the motivating short preprint was inaccessible in the available sources, so closely related uninspected statements remain a substantive priority risk. No experiments on an actual emitter ensemble are claimed.

## References

1. M. G. H. Santos, H. Sanchez, I. M. de Araújo, L. F. A. da Silva, M. H. Y. Moussa, and N. G. de Almeida, *Superradiant Mpemba Relaxation in a Dicke Ladder*, arXiv:2609.25359 (2026), https://arxiv.org/abs/2609.25359 .
2. R. Holzinger and C. Genes, *An exact analytical solution for Dicke superradiance*, arXiv:2409.19040 (2024), https://arxiv.org/abs/2409.19040 .
3. A. Poddar et al., *Exact Analytical Treatment of Collectively Pumped Dicke Superradiance*, arXiv:2610.37665 (2026), https://arxiv.org/abs/2610.37665 .
4. A. Prékopa, *Logarithmic concave measures with applications to stochastic programming*, Acta Sci. Math. 32 (1971), 301–316 (standard marginal log-concavity theorem).
