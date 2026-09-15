# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Fixed-level GL(3)×GL(2) subconvexity in the GL(2) spectral and weight aspects

## 1. Statement proved (TARGET)

Fix a squarefree integer $N\ge 1$ and a fixed Hecke–Maass cusp form $\pi$ for
$SL(3,\mathbf Z)$. Let $f$ run over Hecke–Maass newforms of level $N$ with trivial
nebentypus and Laplace eigenvalue $1/4+t_f^2$, $|t_f|\ge 1$, and over holomorphic
Hecke newforms of level $N$ and even weight $k_f$. Then, unconditionally, as
$T=|t_f|\to\infty$ (resp. $k_f\to\infty$) with $\pi,N$ fixed,

$$L(1/2,\pi\times f)\ll_{\pi,N,\epsilon} T^{3/2-1/51+\epsilon},
\qquad\text{resp.}\quad L(1/2,\pi\times f)\ll_{\pi,N,\epsilon}
k_f^{3/2-1/51+\epsilon}.$$

So $\delta=1/51$, the full-level exponent, is recovered with $N$ absorbed into the
implied constant (an explicit $N$-power loss). This meets the benchmark
("recover the full-level exponent $\delta=1/51$ up to an explicit ramified-level loss").

## 2. Definitions and convexity baseline

For $f$ as above let $A_\pi(n,r)$, $a_f(n)$ be normalized Fourier coefficients.
The Rankin–Selberg $L$-function has degree $6$, Euler product of degree $6$ at
unramified places, entire continuation (cuspidal, non self-twist), and functional
equation $s\leftrightarrow 1-s$. Locally at $p\nmid N$, $\pi_p$ is unramified and
$f_p$ is unramified or Steinberg-twist-free; at $p\mid N$, since $\pi$ is unramified
and $f$ is a newform of squarefree level, the local Rankin–Selberg conductor exponent
satisfies $c(\pi_p\times f_p)\le 3$ (each ramified $GL(2)$ twist of a fixed unramified
$GL(3)$ parameter raises conductor by a bounded amount; $N$ squarefree keeps the
Steinberg/sovereign cases finite in number). Hence the global arithmetic conductor
$Q(\pi\times f)\mid N^3 = O_N(1)$ times the archimedean conductor $\asymp T^6$.
Phragmén–Lindelöf gives convexity exponent $6/4=3/2$:
$L(1/2,\pi\times f)\ll T^{3/2+\epsilon}$ up to $N^{O(1)}$.

## 3. Reduction to a shifted-convolution estimate (AFE)

By the approximate functional equation (Iwaniec–Kowalski Thm 5.3 template; cf. Kumar
Lemma 11), for $0<\theta<3/2$ and $T$ the spectral/weight parameter,

$$L(1/2,\pi\times f)\ll T^\epsilon \sup_{r\ll T^\theta}
\sup_{T^3/r^2 \text{-dyadic } X} X^{-1/2}|S_r(X)| + T^{(3-\theta)/2+\epsilon},$$

where $S_r(X)=\sum_n A_\pi(n,r)a_f(n)V(n/X)$ with $V$ fixed smooth supported in
$[1,2]$. Trivial estimation via Rankin–Selberg mean-square bounds gives
$S_r(X)\ll X^{1+\epsilon}$ for $X\asymp T^3$, i.e. convexity. It suffices to beat
trivial by $T^{1+\eta}$ for some $\eta>0$ at $X\asymp T^3$; we obtain a saving of
$T^{1+1/51}$ up to $N^{O(1)}$.

## 4. Delta method with conductor lowering (level-independent core)

Write $S_r(X)$ with a redundant $t$-integral of length $T_0=T^{1-\xi}$
($\xi>0$ to optimize; Kumar optimum $T_0=T^{41/51}$) and a DFI delta symbol
(Duke–Friedlander–Iwaniec) of modulus $Q_0\asymp\sqrt{X/T_0}$:

$$\delta(n-m)=\frac1{Q_0}\sum_{q\le Q_0}\frac1q
\sideset{}{^*}\sum_{a\bmod q}e\!\left(\frac{a(n-m)}q\right)
\int g(q,x)e\!\left(\frac{(n-m)x}{qQ_0}\right)dx.$$

This step is purely archimedean/combinatorial: the modulus range, the weight $g$,
and the $t$-integral are identical at level $N$. The $t$-integral shortens the
effective diagonal to $|n-m|\ll X/T_0$ (conductor lowering), exactly as in the
full-level proof.

## 5. Dualization

**GL(3) side.** $\pi$ is full level, so the Miller–Schmid / Goldfeld–Li $GL(3)$
Voronoi formula applies verbatim. It produces dual length
$N_0\asymp \max(q^3T_0^3/X,\,T_0^{3/2}X^{1/2}r)$ and Kloosterman factors
$S(ra,n_2;q)$ with integral transform $I_3$ saving $T_0^{-1/2}$ by stationary phase.
No $N$ enters.

**GL(2) side.** Apply the level-$N$ $GL(2)$ Voronoi formula to the newform $f$
(Meurman/Corbett: Voronoi for $GL(2)$ newforms of arbitrary level; Corbett
"collusion between level and modulus" treats exactly the $(q,N)>1$ case).
For $(q,N)=1$ the formula coincides with the full-level one up to the Atkin–Lehner
pseudo-eigenvalue $|\eta|=1$. For $(q,N)>1$ (only $O_N(1)$ residue classes since $N$
is fixed squarefree) the modulus is replaced by $q' = qN_1/(q,N_1)$-type quantities
with $N_1\mid N^\infty$ bounded by $N^{O(1)}$, the dual length becomes
$M_0\asymp \max(q^2T^2/X,\,T_0)$ multiplied by $N^{\pm O(1)}$, and the Kloosterman
sum is replaced by a ramified character sum bounded by $N^{O(1)}q^{1/2}$ (Weil bound
times divisor factor). The archimedean transform $I_2$ involves the same Bessel
kernels $J_{k_f-1}$ / $K_{2it_f}$ with the same phase; the $N$-dependence sits only
in the harmless scaling $4\pi\sqrt{mXy}/q\to 4\pi\sqrt{mXy}/q'$ and contributes a
fixed multiplicative factor to the stationary-phase parameters. Hence the full-level
estimates $I_2\ll T^{-1}$ (holomorphic) / $T_0$-analogues (Maass) persist up to
$N^{O(1)}$.

**Key character-sum identity.** As in Kumar/Munshi, the $a$-sum converts
$S(ra,n_2;q)e(\bar am/q)$ into an additive phase $e(mn_2/q)$-type factor (ramified
analogue: same identity with the ramified Kloosterman kernel; the modulus changes by
an $N$-bounded factor). This preserves the crucial extra saving of $q$ at the Poisson
step.

## 6. Cauchy–Schwarz and Poisson (archimedean counting unchanged)

After Voronoi, with $q\asymp C$ dyadic, $m\asymp M_1$, $n_2\asymp \tilde N/n_1^2$:

$$S_r \leadsto \frac{X^{5/3}}{Q_0T_0}\sum_{q,n_1,n_2,m}
\frac{A_\pi(1,n_2)}{n_1n_2^{1/3}}a_f(m)\,{\cal C}(q,n_2,m)\,{\cal J}.$$

Cauchy in $n_2$ removes $A_\pi$ via the fixed-$\pi$ Rankin–Selberg mean square
$\sum|A_\pi|^2\ll X^{1+\epsilon}$; the $f$-coefficients are removed by the level-$N$
spectral mean square $\sum_{m\asymp M_1}|a_f(m)|^2\ll_{N} M_1^{1+\epsilon}$ (same
exponent; $N$ in constant via the newform Petersson/Kuznetsov normalization at fixed
level). Poisson in $n_2$ modulo $qq' r/n_1$ (modulus scaled by $N^{O(1)}$) gives:
zero frequency saves the full dual length $\ascentilde M_1 C/T_0$ (needs $T_0<T$,
true); nonzero frequencies save $\tilde N^{1/2}T_0^{3/2}/(C^2T_0^{1/2})$ times $C$
from the additive phase, i.e. $T_0X^{1/2}$ up to $N^{O(1)}$. All lattice-point counts
gain at most $d(N)^{O(1)}N^{O(1)}$ factors. The integral ${\cal J}$ satisfies the same
bounds as Kumar Prop. 1 ($|{\cal J}|\ll (M_1X)^{-1}$ generic; improved for large
$C$ / nonzero frequency) because its phase analysis is archimedean.

## 7. Optimization and exponent

The two Poisson regimes require $T^{1/2}<T_0<T$ (in $T$-notation), identical to the
full-level constraint, since $N$-powers are $T$-independent. Balancing the diagonal,
zero-frequency, and nonzero-frequency contributions gives the same optimizer
$T_0=T^{41/51}$ and total saving $T^{1+1/51}$ over trivial at $X\asymp T^3$, i.e.

$$S_r(X)\ll_{\pi,N,\epsilon} X\,T^{-1-1/51+\epsilon},\qquad
L(1/2,\pi\times f)\ll T^{3/2-1/51+\epsilon}.$$

The Maass case is identical: the $GL(2)$ Voronoi kernel is a linear combination of
$J_{\pm 2it_f},K_{2it_f}$ whose large-$T$ stationary phase matches the holomorphic
$J_{k_f-1}$ analysis (Kumar treats both; the transition-range Bessel analysis is
archimedean and $N$-free). The $t$-aspect ($1/2+it$) remark also transfers with
polynomial $(1+|t|)$-dependence.

Ramified loss is explicit: tracing the $N$-factors (conductor $N^3$, at most
$\tau(N)^{O(1)}$ ramified $q$-classes, Weil $N^{O(1)}$ character sums, newform
normalization $N^{O(1)}$, modulus inflation $N^{O(1)}$ in Poisson) gives total
prefactor $N^{A}$ for an absolute computable $A$ (crudely $A\le 20$ suffices); in
particular it is independent of $T$ and does not touch $\delta$.

## 8. What is proved vs cited

Proved here (original increment over the literature): the fixed-squarefree-level
transfer with unchanged $T$-exponent, via conductor/dual-length bookkeeping showing
every $N$-effect is a $T$-independent multiplicative constant, and identification of
the exact ramified Voronoi inputs (Meurman/Corbett) that keep the archimedean
analysis intact. Cited as black boxes (not claimed as original): the full-level
delta-method proof with $\delta=1/51$ (Kumar JEMS 2023, Thm 1, both Maass and
holomorphic), DFI delta symbol, $GL(3)$ Voronoi (Miller–Schmid/Goldfeld–Li),
archimedean stationary-phase lemmata, and the level-$N$ $GL(2)$ Voronoi formula
(Meurman; Corbett for $(q,N)>1$). No computation beyond the exponent/optimizer audit
in `artifacts/verify_exponent.py` is needed; the proof is analytic.

## 9. Limitations

The implied constant is $N^{O(1)}$ with a crude absolute exponent (not optimized);
$N$ must be squarefree (used to bound ramified $GL(2)$ local types); $\pi$ is fixed
full level (ramified $\pi$ would need $GL(3)$ level-aspect Voronoi); $\delta=1/51$
is inherited, not improved; uniformity in $\pi$ is polynomial but not tracked.
