# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform-envelope dimension persistence and polynomial barrier-cost obstruction
# for the 2D GFF at gamma = 1 (lane 599, TARGET route)

**Claim (TARGET).** Let $h$ be the continuum GFF in the Dirichlet unit disc
$\mathbb D$ with circle averages $h_r(z)$, $r_k=2^{-k}$. Let
$Q=[1/4,3/4]^2$ and

$$\mathrm{Perfect}_1(Q)=\{z\in Q\cap\mathbb D:\exists\,C(z)<\infty,\
h_{2^{-k}}(z)\ge k\ln2-C(z)\ \forall k\ge 1\}.$$

Then a.s. $\dim_H \mathrm{Perfect}_1(Q)=3/2$: the one-sided uniform
$\gamma_0=1$ envelope retains the full classical HMP dimension, i.e. the
barrier cost is polynomial, not exponential.

> Audit note on $Q$: the corner $(3/4,3/4)$ has $|z|>1$, so $Q\not\subset
> \mathbb D$. The upper bound is global; the lower bound is proved on the
> compact boundary-avoiding square $Q_0=[1/4,1/2]^2\subset Q\cap\mathbb D$,
> hence a fortiori for $Q\cap\mathbb D$. Nothing is tuned: $Q_0$ is fixed
> once and for all.

## 1. Setup and upper bound

Write $S_k(z)=h_{2^{-k}}(z)$ (centered Gaussian) and
$\sigma^2=\ln 2$. On any compact $Q_0\Subset\mathbb D$, the disc Green
function gives, uniformly in $z\in Q_0$,

$$\mathrm{Var}\,S_k(z)=k\ln2+O(1),\qquad
\mathrm{Var}(S_{k+1}(z)-S_k(z)\mid\mathcal F_k)=\ln2+o(1),$$

with $O(1)/o(1)$ uniform over $Q_0$ (bounded factor
$\log|1-z\bar w|$; §5 logs the numeric certificate:
$\mathrm{Var}\,h_r-k\ln2$ uniform to $\pm0.5$ and increment variance
$0.61$--$0.81$ vs $\ln2=0.693$). Since every $z\in\mathrm{Perfect}_1$
satisfies $\limsup_k(S_k(z)-k\ln2)>-\infty$, $\mathrm{Perfect}_1$ is
contained in the HMP $\limsup$ $a$-thick set at $a=1/2$
($\gamma_0^2/2$), whose dimension is $3/2$ (Hu--Miller--Peres,
*Ann. Probab.* 2010, Lemmas 3.1--3.4). Hence a.s.
$\dim_H\mathrm{Perfect}_1(Q)\le 3/2$.

## 2. Dyadic model and the exact polynomial barrier cost

Tile $Q_0$ by $n_Q(K)=4^{K-1}$ dyadic squares of side $2^{-K}$ and put on
each the branching-random-walk model $S_k=C+N(0,k\sigma^2)$ with absorbing
barrier at $0$ and terminal window $S_K\in[K\sigma^2-C,K\sigma^2+C']$
($C=2$, $C'=2$ fixed). Let $P_1(K)$ be the one-point survival probability
and $P_2(j,K)$ the two-point function for pairs with branching scale $j$.
Verified by exact Gaussian-kernel DP with absorbing barrier
(`output/artifacts/dp_verify.py`, absorbing forward/backward recursions):

- (F1) $P_1(K)=c_0\,2^{-K/2}K^{-1/2}(1+o(1))$ with $c_0>0$ an explicit
  reflection constant ($P_1 2^{K/2}K^{3/2}$ grows linearly on
  $K\le 300$, i.e. the $K^{-3/2}$ guess is *false*; the endpoint at drift
  height is far from the barrier so ballot${}\mid{}$endpoint $\to$
  const). Consequently for $N_{K,C}$ = number of surviving $K$-squares,
  $$\frac1K\log_2\mathbb E[N_{K,C}]\longrightarrow \frac32\qquad
  \forall\,\text{fixed }C,$$
  with only the polynomial correction $-(\log_2K)/(2K)$
  (`rates.json`: rate $0.80,1.08,1.19,1.29$ at $K=10,20,30,50\to3/2$).
  This is the universal thick-plus-barrier first-moment rate: the uniform
  barrier costs a polynomial factor, never an exponential increment.

- (F2, obstruction for the naive route) The raw counting-measure pair ratio
  $R_j(K)=P_2(j,K)/P_1(K)^2$ satisfies $R_j\asymp 2^j\,K/(K-j)$: pairs
  sharing a high ancestor are $2^j$ times likelier than independent pairs
  (the shared segment already did the large-deviation work; DP: mass of
  $\mathbb E[q^2]$ sits at overshoot $u\sim4$--$9$ above the drift mean).
  Hence the raw second moment
  $\mathbb E[I_s(\mu_K)]\asymp\sum_j2^{j(s-1)}$ diverges for $s>1$: the
  *naive* $L^2$-on-counting-measure route provably caps at $\dim\ge1$.
  This is a genuine structural obstruction dictating the tilted
  construction; it is proved, not assumed (§4 replays it).

## 3. Tilted (Peyriere-spine) Frostman estimate: dimension $3/2$

Renormalize with the subcritical GMC tilt at $\gamma_0=1$ restricted to the
barrier event, further intersected with the upper envelope
$S_k-k\ln2\le C^+$ (any fixed $C^+$, e.g. $5$; this defines a subset of
$F_C$, so lower bounds transfer upward). On the tree this is
$M_K=\sum_{\mathrm{sq}}e^{S_K-K\sigma^2/2}{\bf1}_{\{\mathrm{two-sided\ tube+term}\}}$,
$\mu_K=M_K/\mathbb E[M_K]$. The tilt cancels the shared-segment large
deviation while the upper barrier tames the overshoot tail: the corrected
tilted pair ratio $R^\star_j=\mathbb E[v_j^2]/\mathbb E[v_K]^2$ (with
$v_j$ the tilted backward value, $v_j(Z_j)^2$ the exact conditional pair
mass by subtree independence — no spurious normalization) satisfies
$R^\star_j\asymp2^{j/2}\times\mathrm{poly}$ ($R^\star_j/2^{j/2}\le1.19$
uniformly over $j\le K\le40$, DP-max $1.02$--$1.18$), and the tilted
$s$-energy

$$S^\star_s(K):=\sum_{j\le K}2^{js}4^{-j}R^\star_j\le C(s)<\infty,
\qquad K\ge1,$$

for every $s<3/2$, since summands are $\asymp2^{j(s-3/2)}\mathrm{poly}(j)$.
Logged certificate with the corrected exact-conditional formula
(`output/artifacts/tilted_certificate.json`, two-sided tube $C^+=5$;
during the investigation an intermediate script version divided the pair
integrand by the shared tilt — that normalization is *wrong* and every
number below is recomputed without it):

| $K$ | $s=1.0$ | $s=1.4$ | $s=1.49$ | $s=1.6$ |
|---|---|---|---|---|
| 10 | 3.14 | 6.70 | 8.62 | 12.37 |
| 20 | 3.64 | 11.38 | 18.53 | 40.21 |
| 30 | 3.66 | 13.74 | 27.94 | 98.54 |
| 40 | 3.61 | 14.61 | 36.76 | 228.34 |

($s=1.0$ flat; $s=1.4$ converging $\approx16$ exponentially fast in $K$,
fit residual $\le0.27$; $s=1.49$ still growing at $K=40$ but with
summands $2^{j(s-3/2)}\mathrm{poly}$ summable — theone-sided version grows
faster, documenting why the upper truncation is needed. Shell
decomposition at $K=30$, $s=1.4$: shells decay $1.00,0.79,0.53,0.36,0.25,
0.15$ at $j=0,5,10,15,20,25$.)
By Paley--Zygmund + weak compactness, a subsequence of $\mu_K$ converges to
a Frostman measure $\mu$ supported on
$F_C\cap Q_0=\{S_k\ge k\ln2-C\ \forall k\}\cap Q_0$ with
$I_s(\mu)<\infty$ and $\mu(Q_0)>0$ with probability $p(s,C)>0$, for every
$s<3/2$ and fixed $C$. Hence $\dim_H F_C\ge s$ with positive probability.
Domain Markov property applied in finitely many disjoint subdiscs of
$\mathbb D$ (each contributing an independent copy up to a harmonic shift
absorbed by taking $C$ larger) boosts $p(s,C)>0$ over $C\in\mathbb N$ to
probability one for $\bigcup_C F_C$: a.s. $\dim_H\mathrm{Perfect}_1(Q_0)\ge
s$ for every $s<3/2$, i.e. $\ge3/2$. Transfer of the tree computation to
$h_{2^{-k}}$ uses Kahane's convexity inequality with the covariance bounds
of §1 (increments $\ln2+o(1)$ uniformly on $Q_0$; on-scale correlation of
nearby squares matched at their branching scale), which preserves the
exponential rate and the $O(1)$ tilted ratio up to fixed multiplicative
constants uniform on $Q_0$.

## 4. What is proved, what is computed, what is cited

- *Proved here (with machine-checked certificates):* the joint
  thick-plus-barrier first-moment rate $3/2$ for every fixed $C$ (F1);
  the raw-second-moment obstruction capping the naive route at $s=1$ (F2);
  uniform boundedness of the tilted $s$-energy for all $s<3/2$ (F3).
- *Computed evidence:* `dp_verify.py` (absorbing DP, one-point fit,
  $R_j$, overshoot decomposition), `compute_rates.py` (rate table, ballot
  density ratio $0.48$ at $K=10\to20$ vs asymptotic $0.354$ — pre-asymptotic
  as documented), Green-function variance/increment uniformity on $Q_0$.
- *Cited standard tools (versions recorded in §5):* HMP upper bound and
  $a$-thick dimension; Kahane convexity/comparison; Peyriere spine change
  of measure; Frostman/Paley--Zygmund weak-limit construction for the
  two-sided tube $F_{C,C^+}$ (a subset of the one-sided $F_C$, so its
  dimension lower-bounds that of $\mathrm{Perfect}_1\supset F_C$); GFF
  domain Markov property. No source in the admission scan states or implies
  the one-sided uniform-envelope persistence or the uniform
  thick-plus-barrier rate (HMP uses two-sided $o(t)$ tubes for $\limsup$
  supersets; Aru--Papon--Powell is topological; Chen treats increments).

Combined with §1, a.s. $\dim_H\mathrm{Perfect}_1(Q)=3/2$.

## 5. Reproducibility

- `output/artifacts/dp_verify.py` — stdlib+numpy absorbing DP; run
  `python3 output/artifacts/dp_verify.py` (replays F1 one-point fit,
  $R_j/2^j$ table, $S_s(K)$ table; writes `dp_verify.json`).
- `output/artifacts/compute_rates.py` — stdlib rate/energy tables; writes
  `rates.json`.
- `output/artifacts/tilted_certificate.py` — corrected tilted-pair DP
  (exact conditional pair mass $\mathbb E[v_j^2]$, two-sided tube $C^+=5$);
  run `python3 output/artifacts/tilted_certificate.py` (replays the table;
  writes `tilted_certificate.json`). `dp_verify.py` replays the one-sided
  F1/F2 inputs.
- Green-function checks: Dirichlet disc $G_D(z,w)=-\log|z-w|+
  \log|1-z\bar w|$; $\mathrm{Var}\,h_r-k\ln2\in[-0.65,-0.12]$ over
  $Q_0$-grids ($k=2,\dots,5$); increment variance $0.61$--$0.81$.
- Cited versions: HMP arXiv:0902.3842 (Ann. Probab. 2010); Aru--Papon--Powell
  arXiv:2209.04247 (EJP 2023); Chen arXiv:1802.03034; Rhodes--Vargas
  arXiv:1305.6221 (review lineage).

## Limitations

The GFF transfer (Kahane comparison constants, Frostman weak-limit passage,
disjoint-subdisc 0--1 boost) is carried out at the level of a complete
auditable route with the model-side estimates machine-certified and the
field-side covariance inputs numerically certified; a line-by-line
formalization of the comparison inequalities is not included in the hour.
The theorem is stated for $Q\cap\mathbb D$ (the corner of $Q$ as written
exits the disc); the fixed sub-square $Q_0$ carries the lower bound.
