# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit simulation-certified Chernoff and Stein–Chen bounds for the n=m=500 balls-in-bins maximum

## 1. Model and notation

Throw $m=500$ balls independently and uniformly into $n=500$ bins.
Let $L_i$ be the load of bin $i$, $M=\max_{i\le n}L_i$,
$I_i(k)=\mathbf 1\{L_i\ge k\}$, $W_k=\sum_{i=1}^n I_i(k)$.
Each $L_i\sim\mathrm{Bin}(n,1/n)$ marginally; the $L_i$ are negatively
associated across bins. Note $\{M\le k\}=\{W_{k+1}=0\}$ and
$\{M\ge k\}=\bigcup_i\{L_i\ge k\}$.

## 2. Certified results

**Theorem (finite-$n$ certificate at $n=m=500$, machine-checked).**
Let $p_k=P(\mathrm{Bin}(500,1/500)\ge k)$,
$\lambda_6=n p_6$, $j_k=P(L_1\ge k,L_2\ge k)$. Then:

(a) **Exact-binomial union tails** (proved by exact integer arithmetic):
$$P(M\ge 8)\le 0.00491,\quad P(M\ge 9)\le 0.00060,\quad
  P(M\ge 10)\le 0.00006,\quad P(M\ge 6)\le 0.30.$$
  Checked values: $n p_8=0.00490891$, $n p_9=0.00053135$,
  $n p_{10}=0.00005177$, $n p_6=0.29099431$.

(b) **Textbook comparison** (Mitzenmacher–Upfal union–Chernoff
  $P(M\ge k)\le n(e m/(nk))^k=n(e/k)^k$): at $k=8,9,10$ it gives
  $0.08883947$, $0.01045774$, $0.00110132$ — looser than (a) by
  $18.1\times$, $19.7\times$, $21.3\times$ respectively.

(c) **Stein–Chen middle certificate.** With $B_i=\{\text{all bins}\}$
  ($b_3=0$), Arratia–Goldstein–Gordon Theorem 1 gives
  $d_{TV}(\mathcal L(W_6),\mathrm{Po}(\lambda_6))
   \le \frac{1-e^{-\lambda_6}}{\lambda_6}(b_1+b_2+b_3)
   \le b_1+b_2$ where, exactly,
  $$b_1=n^2p_6^2=0.084677,\qquad
    b_2=n(n-1)j_6=0.080067,\qquad b_1+b_2=0.164744\le 0.165\le 0.20.$$
  Hence, with $e^{-\lambda_6}=0.7475\pm 0.0002$ (rational Taylor bounds, §4),
  $$|P(M\le 5)-e^{-\lambda_6}|\le 0.20.$$
  (Excluding the diagonal, $n(n-1)p_6^2=0.084508$, sum $0.164575$.)

(d) **Lower tail and coverage.** $E[W_4]=n p_4=9.43274489$.
  Pairwise negative correlation $j_4\le p_4^2$ (ratio $0.97917014$)
  and $j_6\le p_6^2$ (ratio $0.947442$) are proved by exact integer
  inequalities $J_k\cdot 500^{500}\le S_k^2$ (§3), so
  $\mathrm{Var}(W_4)\le E[W_4](1-p_4)$ and with the exact covariance
  $$\frac{\mathrm{Var}(W_4)}{E[W_4]^2}=0.08322548\le 0.084.$$
  By Chebyshev, $\{W_4=0\}\subset\{|W_4-E|\ge E\}$,
  $$P(M\le 3)=P(W_4=0)\le 0.084.$$
  Consequently
  $$P(4\le M\le 7)=1-P(M\le 3)-P(M\ge 8)\ge 1-0.084-0.00491\ge 0.89$$
  (indeed $\ge 0.911$).

(e) **Simulation benchmark** (evidence, not proof): 20000 trials,
  `numpy.random.default_rng(1)`, per-trial max load:

| $M$ | count | freq | Clopper–Pearson 95% |
|---|---|---|---|
| 4 | 3214 | 0.1607 | [0.1556, 0.1659] |
| 5 | 11716 | 0.5858 | [0.5789, 0.5926] |
| 6 | 4317 | 0.2159 | [0.2102, 0.2216] |
| 7 | 677 | 0.0339 | [0.0314, 0.0365] |
| 8 | 61 | 0.00305 | [0.00233, 0.00392] |
| 9 | 15 | 0.00075 | [0.00042, 0.00124] |

  $P(M\le 5)=0.7465$ (vs $e^{-\lambda_6}=0.7475$, diff $0.001$);
  $P(4\le M\le 7)=0.9962$ (vs analytic $\ge 0.89$). No trial had
  $M\le 3$ or $M\ge 10$, consistent with (a) and (d).

**Correction to the proposal.** The assigned target stated
$P(M\le 3)\le 0.104$ via the crude bound $(1-p_4)/E[W_4]$.
The exact value of that crude ratio is $0.10401368>0.104$, so $0.104$
is **false by $1.4\times 10^{-5}$** for that proof route
(integer check fails). We instead certify the corrected crude bound
$\le 0.105$ and the stronger exact-covariance bound $\le 0.084$ above;
all coverage claims use $\le 0.084$. The proposed $17.5\times$ at $k=9$
is conservative: the true tightening is $19.7\times$.

## 3. Proofs

**Union tails.** By the union bound and symmetry,
$P(M\ge k)\le\sum_i P(L_i\ge k)=n\,p_k$.
With $p_k=S_k/500^{500}$,
$S_k=\sum_{j\ge k}\binom{500}{j}499^{500-j}$,
$U_k:=n p_k=S_k/500^{499}$. Each $S_k$ is an explicit integer
($\sim$4470 bits, 500 terms) computed by `math.comb`; the claim
$U_k\le t$ is the integer inequality $S_k\cdot t_{den}\le t_{num}\cdot
500^{499}$, verified in `check_exact.py` for the thresholds in (a).

**Textbook bound.** Standard Chernoff
$P(\mathrm{Bin}(n,p)\ge k)\le (enp/k)^k$ (Mitzenmacher–Upfal,
Theorem 4.4/4.6 line) plus union gives $500(e/k)^k$; evaluated in
floating point for display (proof of the formula cited, numbers
reproducible by one line).

**Stein–Chen.** Apply Arratia–Goldstein–Gordon (1990), Theorem 1
(also Barbour–Holst–Janson §2): for indicators $I_i$ with
$B_\alpha\ni\alpha$,
$d_{TV}\le \frac{1-e^{-\lambda}}{\lambda}(b_1+b_2+b_3)$ with
$b_1=\sum_\alpha\sum_{\beta\in B_\alpha}p_\alpha p_\beta$,
$b_2=\sum_\alpha\sum_{\beta\in B_\alpha,\beta\ne\alpha}
E[I_\alpha I_\beta]$,
$b_3=\sum_\alpha E|E[I_\alpha-p_\alpha\mid\sigma(I_\beta,
\beta\notin B_\alpha)]|$.
Take $B_i=\{1,\dots,n\}$: the conditioning set outside is empty so
$b_3=0$; $b_1=n^2p_6^2$, $b_2=n(n-1)j_6$.
The joint law: for $a+b\le 500$,
$P(L_1=a,L_2=b)=\frac{500!}{a!\,b!\,(500-a-b)!}\frac{498^{500-a-b}}{500^{500}}$,
so $j_6=J_6/500^{500}$ with
$J_6=\sum_{a,b\ge 6}500!/(a!b!c!)\,498^{c}$ an explicit integer
($\sim$4462 bits; full double sum, no truncation, $\approx$1 s).
Then $b_1+b_2\le 0.17$ is
$(n^2S_6^2+n(n-1)J_6500^{500})\cdot 100\le 17\cdot 500^{1000}$,
checked with big ints (holds with $3.2\%$ margin; $\le 0.165$ also holds).
Since $(1-e^{-\lambda})/\lambda\le 1$ ($e^{-x}\ge 1-x$),
$d_{TV}\le b_1+b_2\le 0.20$. The event $\{M\le 5\}=\{W_6=0\}$
transfers the TV bound to $|P(M\le 5)-e^{-\lambda_6}|$.

**Lower tail.** $E[W_4]=S_4/500^{499}=9.43274489$ (integer-bounded).
For the covariance sign we prove $j_4\le p_4^2$ directly:
$J_4\cdot 500^{500}\le S_4^2$ with
$J_4=\sum_{a,b\ge 4}500!/(a!b!c!)498^c$ (exact, $\approx$1 s);
ratio $0.97917014<1$. Hence all $\binom{n}{2}$ off-diagonal
covariances are $\le 0$ and
$\mathrm{Var}(W_4)=\sum_i p(1-p)+\sum_{i\ne j}(j-p^2)\le E(1-p)$.
Chebyshev: $P(W_4=0)\le P(|W_4-E|\ge E)\le \mathrm{Var}/E^2$.
The crude ratio $(500^{500}-S_4)/(500S_4)=0.10401368$ (so $\le 0.105$,
not $\le 0.104$). Keeping the exact covariance,
$\mathrm{Var}/E^2=[S_4(D-S_4)+(n-1)(J_4D-S_4^2)]/(nS_4^2)$
with $D=500^{500}$ equals $0.08322548\le 0.084$ (integer-checked
$\times 1000\le 84$). Coverage follows by union of the two tails.

## 4. Rigorous value of $e^{-\lambda_6}$

Integer checks give $\lambda_6\in[0.2909,0.2911]$.
For $x\in(0,1)$ the Taylor polynomials of $e^{-x}$ alternate around the
limit with $|\text{error}_N|\le x^{N+1}/(N+1)!$; even degrees bound above,
odd below. With $x_\ell=2909/10000$, $x_u=2911/10000$ as exact
`Fraction`s, $N=10/11$:
$e^{-x_u}\ge S_{11}(-x_u)=0.74744093$,
$e^{-x_\ell}\le S_{10}(-x_\ell)=0.74759044$
(remainder $<4\times 10^{-14}$), so
$e^{-\lambda_6}\in[0.74744,0.74760]\ni 0.7475$.

## 5. Simulation method

`output/artifacts/simulate.py`: `rng=np.random.default_rng(1)`;
10 batches of 2000 trials; each trial `rng.integers(0,500,size=500)`,
max load via `bincount`; deterministic (batching preserves draw order).
Clopper–Pearson intervals from a self-contained regularized incomplete
beta (continued fraction) plus bisection — no scipy needed.
CSV: `output/artifacts/sim_summary.csv`. Rerun: seconds.

## 6. What is proved vs computed vs open

- **Proved** (exact integer certificates + cited theorems): (a), (c), (d),
  the $18$–$21\times$ arithmetic comparison given the textbook formula.
- **Computed evidence** (not a theorem): (e) histogram and CP intervals;
  agreement $0.7465\approx 0.7475$ supports but does not prove the model.
- **Uncertainty / limits**: bounds are $n=m=500$-specific; no new asymptotics;
  TV bound $0.165$ is sufficient but not sharp (true $d_{TV}$ is smaller;
  refined factor $(1-e^{-\lambda})/\lambda=0.868$ alone gives $\le 0.143$);
  lower-tail Chebyshev is loose vs the true $P(M\le 3)\sim 10^{-4}$
  (Poisson heuristic $e^{-9.43}$); simulation CIs assume correct PRNG.

## 7. Reproducibility

- `output/artifacts/check_exact.py` — stdlib only; `python3 check_exact.py` → ALL-OK (~2 s).
- `output/artifacts/simulate.py` — needs numpy only; `python3 simulate.py` (~seconds).
- `output/artifacts/sim_summary.csv` — reference output.

## References

- Raab & Steger, Balls into Bins — A Simple and Tight Analysis, RANDOM 1998.
- Mitzenmacher & Upfal, Probability and Computing, Ch. Balls/Bins/Random Graphs.
- Barbour, Holst & Janson, Poisson Approximation, Oxford 1992.
- Arratia, Goldstein & Gordon, Poisson approximation and the Chen–Stein method,
  Statist. Sci. 5 (1990) — Theorem 1.
- Gonnet, Expected length of the longest probe sequence, JACM 1981 (context).
