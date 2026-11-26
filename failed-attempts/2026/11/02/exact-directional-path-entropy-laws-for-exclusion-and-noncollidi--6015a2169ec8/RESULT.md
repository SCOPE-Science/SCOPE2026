# Exact directional path-entropy laws for exclusion and noncolliding walks on a ring

## Finding

For every integer \(n\ge4\) and \(2\le k\le n-2\), compare stationary clockwise simple exclusion on \(\mathbb Z/n\mathbb Z\) with the Doob-conditioned noncolliding version of \(k\) independent clockwise walkers. The relative entropies of their path laws on \([0,t]\) are **exactly affine in time**. Writing
\[
R_{n,k}=\frac{\sin(\pi k/n)}{\sin(\pi/n)},\qquad
\alpha_{n,k}=(k-R_{n,k})\left(1-\frac{k+R_{n,k}}n\right),\qquad
\beta_{n,k}=R_{n,k}-\frac{k(n-k)}{n-1},
\]
one has, for every real \(t\ge0\),
\[
D(\mathsf P_{\mathrm{NC}}^{[0,t]}\Vert\mathsf P_{\mathrm{Ex}}^{[0,t]})
=D(\pi_{\mathrm{NC}}\Vert\pi_{\mathrm{Ex}})+t\alpha_{n,k},
\]
\[
D(\mathsf P_{\mathrm{Ex}}^{[0,t]}\Vert\mathsf P_{\mathrm{NC}}^{[0,t]})
=D(\pi_{\mathrm{Ex}}\Vert\pi_{\mathrm{NC}})+t\beta_{n,k}.
\]
Both coefficients are strictly positive. In the sparse regime of fixed \(k\ge2\) and \(n\to\infty\),
\[
\alpha_{n,k}\sim\frac{\pi^2 k(k^2-1)}{6n^2},\quad
\beta_{n,k}\sim\frac{k(k-1)}n,\quad
\frac{\beta_{n,k}}{\alpha_{n,k}}\sim\frac{6n}{\pi^2(k+1)}.
\]
Thus the two directions have different mesoscopic information scales even though the processes share every permitted jump. For exactly two particles the complete critical-window limits are, for each fixed \(u\ge0\),
\[
\lim_{n\to\infty}D(\mathsf P_{\mathrm{NC},n,2}^{[0,un^2]}\Vert\mathsf P_{\mathrm{Ex},n,2}^{[0,un^2]})=1-\log2+\pi^2u,
\]
\[
\lim_{n\to\infty}\frac1nD(\mathsf P_{\mathrm{Ex},n,2}^{[0,un^2]}\Vert\mathsf P_{\mathrm{NC},n,2}^{[0,un^2]})=2u.
\]

## Assumptions and scope

A configuration \(S\) is an unordered \(k\)-subset of \(\mathbb Z/n\mathbb Z\). A legal directed move replaces an occupied site \(x\) by the unoccupied site \(x+1\pmod n\); each such move has rate one for exclusion (Ex). Define the circular chord Vandermonde and traffic count
\[
h(S)=\prod_{\substack{x,y\in S\\x<y}}|e^{2\pi ix/n}-e^{2\pi iy/n}|,\qquad
\kappa(S)=\sum_{x\in\mathbb Z/n\mathbb Z}\mathbf1_{\{x,x+1\}\subset S}.
\]
The noncolliding Doob chain (NC) assigns each legal move \(S\to S'\) rate \(h(S')/h(S)\). All rates are continuous-time rates per unit time. \(\pi_{\mathrm{Ex}}(S)=\binom nk^{-1}\) and \(\pi_{\mathrm{NC}}(S)=h(S)^2/n^k\) are their respective stationary laws. The path measures in the finding start from these respective stationary laws, with the same time interval \([0,t]\). Relative entropy uses natural logarithms, and the two path measures are mutually absolutely continuous on each finite time interval.

## Proof

**1. Constant noncolliding exit rate and stationary laws.** The discrete Fourier Vandermonde identity gives
\[
\sum_{S':\ S\to S'}h(S')=R_{n,k}h(S),\qquad
\sum_{S':\ S'\to S}h(S')=R_{n,k}h(S).
\]
One way to derive it is to expand the determinant of the \(k\) consecutive centered Fourier characters on \(S\), apply a clockwise shift to one coordinate in each determinant term, and sum. The character eigenvalues add to \(\sum_{j=0}^{k-1}\exp(2\pi i(j-(k-1)/2)/n)=R_{n,k}\); the Vandermonde orientation and cyclic permutation signs cancel on a wrap-around move, while collision contributions vanish. Reflecting the ring proves the incoming identity. In particular the NC total jump rate is \(R_{n,k}\), independent of state. The Ex exit rate is \(k-\kappa(S)\).

Let \(V\) be the \(k\times n\) Fourier matrix with entries \(V_{r,x}=e^{2\pi irx/n}\), for \(0\le r<k\). Cauchy--Binet gives
\[
\sum_{|S|=k}h(S)^2=\det(VV^*)=n^k.
\]
The incoming and outgoing eigenfunction identities show that \(h^2/n^k\) balances the stationary NC flow, while the number of legal clockwise and counterclockwise moves is equal at every exclusion configuration, proving uniform Ex stationarity. Both chains are irreducible on the finite configuration set.

**2. Exact stationary traffic expectations.** Under uniform Ex sampling the two sites \(x,x+1\) are jointly occupied with probability \(k(k-1)/(n(n-1))\), so \(\mathbb E_{\mathrm{Ex}}\kappa=k(k-1)/(n-1)\). Under NC the Fourier projection determinantal kernel is
\[
K(x,y)=\frac1n\sum_{r=0}^{k-1}e^{2\pi ir(x-y)/n}.
\]
The occupied-neighbor two-point probability is \(K(x,x)K(x+1,x+1)-|K(x,x+1)|^2=(k^2-R_{n,k}^2)/n^2\). Therefore
\[
\mathbb E_{\mathrm{NC}}\kappa=\frac{k^2-R_{n,k}^2}{n}.
\]

**3. Path likelihood and both entropy identities.** On any finite-time path, the standard continuous-time jump-process likelihood formula and the NC-to-Ex jump-rate ratio \(h(S')/h(S)\) give
\[
\log\frac{d\mathsf P_{\mathrm{NC}}^{[0,t]}}{d\mathsf P_{\mathrm{Ex}}^{[0,t]}}
=\log\frac{\pi_{\mathrm{NC}}(S_0)}{\pi_{\mathrm{Ex}}(S_0)}+
\log\frac{h(S_t)}{h(S_0)}+(k-R_{n,k})t-\int_0^t\kappa(S_s)\,ds.
\]
The sum of jump logarithms telescopes to the endpoint term. Stationarity makes the expected endpoint-log term zero under either law. Taking expectation first under NC and then of the negative likelihood under Ex yields the asserted two exact affine identities using Step 2. Strict positivity follows also from the strict path-law relative-entropy-rate inequality: at least one legal edge has rate \(h(S')/h(S)\ne1\) for \(2\le k\le n-2\): a contiguous block of particles has one legal clockwise move whereas a configuration split into two nonempty blocks has at least two, so the state-independent NC exit rate could not equal both Ex exit rates. By irreducibility and strict convexity of \(v\log v-v+1\), both directional entropy-rate sums are positive.

**4. Sparse and two-particle limits.** For fixed \(k\), Taylor expansion gives \(R_{n,k}=k-\pi^2 k(k^2-1)/(6n^2)+O_k(n^{-4})\). Substitution yields the three fixed-\(k\) asymptotics in the finding. For \(k=2\), the chord weight for a pair at separation \(d\) is \(2\sin(\pi d/n)\). The product identity \(\prod_{d=1}^{n-1}2\sin(\pi d/n)=n\) gives the exact initial reverse entropy
\[
D(\pi_{\mathrm{Ex},n,2}\Vert\pi_{\mathrm{NC},n,2})
=\log\frac{2n}{n-1}-\frac{2\log n}{n-1}\longrightarrow\log2.
\]
For the ordered gap \(d=b-a\), the NC gap distribution converges by Riemann sums to density \(4(1-x)\sin^2(\pi x)\) on \((0,1)\). Since the divergence integrand is invariant under \(x\mapsto1-x\), this is equivalent in the relevant integral to the symmetric weight \(2\sin^2(\pi x)\). Endpoint integrability of \(x^2|\log x|\) then gives
\[
D(\pi_{\mathrm{NC},n,2}\Vert\pi_{\mathrm{Ex},n,2})\longrightarrow
\int_0^1 2\sin^2(\pi x)\log(2\sin^2(\pi x))\,dx=1-\log2.
\]
The last integral follows by differentiating the beta integral for \(\int_0^\pi\sin^{2a}u\,du\) at \(a=1\). Finally \(n^2\alpha_{n,2}\to\pi^2\), \(n\beta_{n,2}\to2\), proving the critical-window limits.

For completeness, if \(k/n\to\rho\in(0,1)\), setting \(a=\sin(\pi\rho)/\pi\) gives the distinct extensive-rate limits \(\alpha_{n,k}/n\to(\rho-a)(1-\rho-a)\) and \(\beta_{n,k}/n\to a-\rho(1-\rho)\). No assertion about the corresponding initial-entropy constants in this dense regime is needed.

## Verification

Run `python3 verify.py` using Python's standard library. The script enumerates all unlabeled configurations for \(3\le n\le10\), independently computes legal edges, Vandermonde weights, incoming/outgoing stationary flows, both stationary traffic averages, both path-relative-entropy rates, and two-particle stationary intercepts. It checks fixed-particle and fixed-density scaling numerically at larger \(n\). The completed execution reported `PASS 8839 total deterministic assertions`. These finite checks detect normalization and factor errors but do not replace the all-\(n\) analytic argument.

## Relationship to prior work

The radial Vandermonde transform, noncolliding ring jump rates, determinantal stationary measure and TASEP traffic change of measure are established by Johnston (2022 preprint, later publication) and reviewed/generalized by Shiatis (2026). These are *inputs*, not newly claimed discoveries. General entropy identities for Doob-conditioned processes are also standard background (e.g. Chetrite--Touchette). The added conclusion is the explicit **paired** stationary path-divergence coefficients, their sharp sparse directional separation, and complete two-particle time-window constants. No claim is made that generic Girsanov likelihoods or the underlying exclusion/noncollision equivalence are new.

## Limitations

The formulas concern stationary initial distributions, unit-rate clockwise movement, finite rings and finite observation intervals. They do not assert corresponding formulae for arbitrary initial states, other jump asymmetries, or large-deviation or testing exponents. Asymptotics are for fixed \(k\) or specified particle density, and the initial-entropy critical-window constants are stated only for \(k=2\). Historical priority of these particular entropy coefficients has not been independently adjudicated; earlier Doob-transform and determinantal literature is a genuine source of possible implicit coverage.

## References

- Rohan Shiatis, *Exclusion vs Noncolliding Dynamics in Markov Processes*, arXiv:2610.00741v1, first public 2026-09-30, https://arxiv.org/abs/2610.00741 .
- Samuel G. G. Johnston, *Continuous Kasteleyn theory for the bead model*, arXiv:2207.13538, first public 2022-07-27, https://arxiv.org/abs/2207.13538 .
- Raphaël Chetrite and Hugo Touchette, *Variational and optimal control representations of conditioned and driven processes*, arXiv:1506.05291, https://arxiv.org/abs/1506.05291 .
