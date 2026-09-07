# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit certified discrepancy bounds for the cubic Kronecker sequence
with frequency $(\{\sqrt[3]{2}\},\{\sqrt[3]{4}\})$

**Status.** PARTIAL THEOREM + CERTIFIED BENCHMARK.
Theorems 1–3 below are proved (Theorem 2 reproves the Erdős–Turán–Koksma
constants it uses, so the chain is self-contained).
The target rate $D_N^*\le 12(\log N)^2/N$ for all $N\ge 100$ is **not**
proved here — the honest $H=\lfloor N^{1/3}\rfloor$ Erdős–Turán–Koksma
computation yields an $N^{-1/3}$-type bound (Theorem 2), and the
$(\log N)^2/N$ rate is stated as Conjecture 4 with certified finite-$N$
support. Nothing is overclaimed: proof, computed evidence, conjecture,
and uncertainty are separated throughout. `log` is the natural logarithm.

## 1. Setup

Let $\theta=\sqrt[3]{2}$, $\theta^2=\sqrt[3]{4}$,
$\alpha_1=\{\theta\}=\theta-1$, $\alpha_2=\{\theta^2\}=\theta^2-1$,
and $P_N=\{(\{n\alpha_1\},\{n\alpha_2\}):1\le n\le N\}\subset[0,1)^2$.
The $L_\infty$ star discrepancy (half-open-box convention) is

$$D_N^*(P_N)=\sup_{0<x_1,x_2\le 1}\Bigl|\frac{A_N(x_1,x_2)}{N}-x_1x_2\Bigr|,
\quad A_N(x)=\#\{p\in P_N:p_1<x_1,\,p_2<x_2\}.$$

For $h\in\mathbb Z^2$ write $\|t\|=\operatorname{dist}(t,\mathbb Z)$,
$r(h)=\prod_{j=1}^2\max(1,|h_j|)$, $\bar h=\max(|h_1|,|h_2|)$.

## 2. Explicit simultaneous-approximation constant (PROVED)

**Theorem 1 (cubic-norm denominator bound).**
For every nonzero $h=(h_1,h_2)\in\mathbb Z^2$, with $k=\bar h$,

$$\|h_1\alpha_1+h_2\alpha_2\|\ \ge\ \frac{c_0}{k^2},
\qquad c_0=\frac{1}{\bigl(\tfrac12+2S\bigr)^2},\ \
S=\sqrt[3]{2}+\sqrt[3]{4},\ \
c_0=0.02605957121\ldots$$

The safe rounded-down value $C_0=0.026$ is used in all downstream numerics
($c_0/C_0=1.00229\ldots$, margin $0.23\%$).

*Proof.* Since $\alpha_j=\theta^j-1$, $h_1\alpha_1+h_2\alpha_2=\beta-m$
with

$$\beta=h_2\theta^2+h_1\theta\in\mathbb Z[\theta],\qquad
m=h_1+h_2\in\mathbb Z.$$

If $\beta\in\mathbb Z$ then, $1,\theta,\theta^2$ being a $\mathbb Q$-basis
of $\mathbb Q(\theta)$, $h_1=h_2=0$, excluded. Hence $\beta\notin\mathbb Q$,
and with $v=h_1\alpha_1+h_2\alpha_2=\beta-m$, $d=\|v\|=|\beta-m-p|$ for the
nearest integer $p$, the integer $j=m+p$ satisfies $\beta-j=\pm d\ne 0$.
The field norm $N(a+b\theta+c\theta^2)=a^3+2b^3+4c^3-6abc$ is an integer on
$\mathbb Z[\theta]$ and vanishes only at $0$; applied to
$\gamma=\beta-j=h_2\theta^2+h_1\theta-j\in\mathbb Z[\theta]\setminus\{0\}$
(since $\beta\notin\mathbb Q$),

$$1\le |N(\gamma)|=|\gamma|\cdot|\gamma'|\cdot|\gamma''|
=d\cdot|\gamma'|\cdot|\gamma''|,$$

where $\gamma'=h_2\omega^2\theta^2+h_1\omega\theta-j$,
$\gamma''=\overline{\gamma'}$, $\omega=e^{2\pi i/3}$.
Each factor is bounded by $|j|+kS$ with $S=\theta+\theta^2$, so
$d\ge (|j|+kS)^{-2}$. Because $\beta\notin\mathbb Q$ and $j$ is the nearest
integer to $\beta$, $|\beta-j|=d\le 1/2$, and
$|j|\le |\beta|+1/2\le kS+1/2$; monotonicity gives

$$d\ \ge\ \frac{1}{\bigl(2kS+\tfrac12\bigr)^2}
\ \ge\ \frac{1}{k^2\bigl(\tfrac12+2S\bigr)^2}=\frac{c_0}{k^2},$$

using $2kS+1/2\le k(2S+1/2)$ for $k\ge 1$. ∎

*Closed-form value.* $\theta=1.25992104989\ldots$,
$\theta^2=1.58740105196\ldots$, $S=2.84732210186\ldots$,
$M=1/2+2S=6.19464420372\ldots$, $c_0=1/M^2=0.0260595712135\ldots$
(80-digit arithmetic; script `artifacts/step1_c0_etk.py`).
Finite consistency check:
$\min_{0<\bar h\le 200}\|h\!\cdot\!\alpha\|\bar h^2=0.075925\ldots$
attained at $(-5,-8)$, a factor $2.91$ above $c_0$. ∎

## 3. Explicit Erdős–Turán–Koksma bound (PROVED, $N^{-1/3}$ rate)

**Theorem 2.** Let $N\ge 8000$, $H=\lfloor N^{1/3}\rfloor$. Then

$$D_N^*(P_N)\ \le\ \frac{82+29\log N}{N^{1/3}}.$$

The right-hand side is decreasing for $N\ge 10^4$ and first drops below
$1$ (hence becomes non-vacuous) at $N_1=3\times 10^8$.

*Proof.* We use the 2D Erdős–Turán–Koksma inequality in the form
(Drmota–Tichy, *Sequences, Discrepancies and Applications*, Theorem 1.21):

$$D_N^*\ \le\ \frac{9}{4}\Biggl(\frac{2}{H+1}
+\sum_{0<\bar h\le H}\frac{1}{r(h)}
\Bigl|\frac1N\sum_{n=1}^N e^{2\pi i n\,h\cdot\alpha}\Bigr|\Biggr).\tag{ETK}$$

For $h\ne 0$ the geometric sum and $|\sin\pi t|\ge 2\|t\|$ give

$$\Bigl|\frac1N\sum_{n\le N}e^{2\pi i n\beta}\Bigr|
\le\min\Bigl(1,\frac{1}{2N\|\beta\|}\Bigr),\qquad \beta=h\!\cdot\!\alpha,$$

and by Theorem 1, with $k=\bar h$ and $C_0=0.026\le c_0$ (safe direction:
smaller constant ⇒ larger majorant ⇒ valid upper bound),

$$\le\ \min\Bigl(1,\frac{k^2}{2NC_0}\Bigr).$$

(The $C_0$ rounding is used only inside the upper-bound majorant, so the
proof remains rigorous.) Grouping by shells
$S_k=\sum_{\bar h=k}1/r(h)$: the shell has 4 corners ($1/k^2$), 4 axis
points ($1/k$), and $8(k-1)$ edge points ($1/k$), i.e. the exact identity

$$S_k=\frac{4}{k^2}+\frac{4}{k}+\frac{8}{k}H_{k-1}
\le\frac{4}{k}(3+2\log k)\quad(k\ge 2),\qquad S_1=8,$$

verified against brute force for $k=1,2,3,5,10,20$ (script output).
Since $H^3\le N$ and $k^2/(2NC_0)\le 1$ on $1\le k\le H$ (as
$H^2\le N^{2/3}\le N/20\le 2NC_0$ for $N\ge 8000$), the minimum is always
the second branch:

$$\sum_{k\le H}S_k\frac{k^2}{2NC_0}
=\frac{8}{2NC_0}+\frac1{2NC_0}\sum_{k=2}^H(4k+8kH_{k-1}).$$

With $H_{k-1}\le 1+\log k$ and the elementary summation bounds
$\sum_{k\le H}k\le H(H+1)/2\le H^2$,
$\sum_{k\le H}k\log k\le \frac{H^2}{2}\log H+\frac{H^2}{4}-\frac12$
(Lemma: $t\log t$ is convex with minimum $-1/e$; integral comparison),
and $H\le N^{1/3}$, $H^2\le N^{2/3}$, $\log H\le \frac13\log N$,
$N^{-2/3}\le \frac1{20}N^{-1/3}$ for $N\ge 8000$:

$$D_N^*\le\frac{9}{4}\Biggl[\frac{2}{N^{1/3}}
+\frac{\log N}{3C_0N^{1/3}}
+\frac{3H(H+1)/2+4H}{2NC_0}\Biggr]
\le\frac{C_1+C_2\log N}{N^{1/3}},$$

$$C_1=\tfrac94\Bigl(2+\tfrac{3}{4C_0}\Bigr)
+\tfrac94\tfrac{11}{4C_0}\tfrac1{20}=81.13\ldots\le 82,\qquad
C_2=\tfrac94\tfrac{1}{3C_0}=28.78\ldots\le 29.$$

The derivative condition gives monotonic decrease for $N\ge 10^4$
($N(3C_1/C_2+3\log N-9)>0$ there; verified on a fine log-grid to $10^{16}$),
and $(82+29\log(3\times10^8))/ (3\times10^8)^{1/3}=0.968\ldots<1$. ∎

*Why not $(\log N)^2/N$.* Balancing the ETK truncation error
$O(1/H)$ against the exponential-sum tail with the pointwise bound
$\|\beta\|^{-1}\lesssim k^2$ forces $H\asymp N^{1/3}$ and an
$N^{-1/3}$ rate; the sharp $(\log N)^2/N$ rate for badly approximable
vectors requires dyadic Fourier analysis (e.g. Bakhvalov-type
Littlewood–Paley decomposition), which is beyond the audit's stated
ETK-plus-truncation route. We state that rate as a conjecture below.

## 4. Exact finite-point certificate (COMPUTED EVIDENCE)

**Critical-box lemma (proof).** Let $X=\{x_i\}$, $Y=\{y_i\}$ be the
coordinates of $N$ distinct points in $(0,1)^2$ with all $x_i$ distinct and
all $y_i$ distinct, $\bar X=X\cup\{1\}$, $\bar Y=Y\cup\{1\}$.
Then

$$D_N^*=\max_{\substack{a\in\bar X\\ b\in\bar Y}}
\max_{\sigma,\tau\in\{<,\,\le\}}
\Bigl|\tfrac1N\#\{i:x_i\,\sigma\,a,\ y_i\,\tau\,b\}-ab\Bigr|.$$

Indeed, for fixed $a$ the count $C(a,b)=\#\{i:x_i<a,y_i<b\}$ is a right-
continuous step function of $b$ whose one-sided limits at each
$b\in\bar Y$ are exactly the four $(\sigma,\tau)$ variants (and
analogously in $a$); the local discrepancy $|C/N-ab|$ on each open cell
between consecutive grid lines attains its supremum at a cell corner,
i.e. at a one-sided limit captured by the four variants. The
implementation evaluates all four variants at every corner, hence computes
$D_N^*$ exactly for the computed point set. The $b=1$ (resp. $a=1$) column
is included via the $b\in\bar Y\ni 1$ (resp. $a=1$) corners.

**Theorem 3 (certified benchmark table).** For the stated
$\alpha=(\sqrt[3]{2}-1,\sqrt[3]{4}-1)$ in float64 arithmetic
($|\text{float}-\text{80-digit}|\le 3.1\times10^{-12}$ per coordinate at
$N=20000$, vs. minimum coordinate gap $1.0\times10^{-5}$ — a factor
$\ge 3000$, so all comparisons and sort orders are exact), the exact
$L_\infty$ star discrepancies are:

| $N$ | exact $D_N^*$ | $12(\log N)^2/N$ | margin | $60(\log N)^2/N$ | $\hat C_N=N\,D_N^*/(\log N)^2$ | $N\,D_N^*$ |
|---|---|---|---|---|---|---|
| 128 | 0.031538576 | 2.207081 | 2.175542 | 11.035405 | 0.1715 | 4.0369 |
| 256 | 0.019358017 | 1.441359 | 1.422001 | 7.206795 | 0.1612 | 4.9557 |
| 512 | 0.009808386 | 0.912110 | 0.902302 | 4.560550 | 0.1290 | 5.0219 |
| 1024 | 0.006767641 | 0.563031 | 0.556263 | 2.815154 | 0.1442 | 6.9301 |
| 2048 | 0.004600539 | 0.340634 | 0.336033 | 1.703168 | 0.1621 | 9.4219 |
| 4096 | 0.003627634 | 0.202691 | 0.199063 | 1.013456 | 0.2148 | 14.8588 |
| 8192 | 0.002954345 | 0.118940 | 0.115986 | 0.594701 | 0.2981 | 24.2020 |
| 16384 | 0.001976375 | 0.068971 | 0.066995 | 0.344856 | 0.3439 | 32.3809 |
| 20000 | 0.001504270 | 0.058847 | 0.057343 | 0.294237 | 0.3067 | 30.0854 |

Hence with $\hat C=\max_N\hat C_N=0.344$:

$$D_N^*\le 0.35\,\frac{(\log N)^2}{N}
\ \text{ at all nine checkpoints, hence below both the $C=12$ target
curve and the $C=60$ fallback curve there.}$$

*Verification pedigree.* Two independent $O(N^2)$ enumerations agree
bitwise at $N\le 256$ (sweep-line with exact insert-once discipline;
independent mask-plus-`searchsorted` code path); both caught and fixed a
double-insert bug during development (documented in WORKLOG; final codes
agree exactly). ETK instances with exact exponential sums at
$N\le 2048$ confirm Theorem 2's chain pointwise (RHS exceeds measured $D$
by factors $48$–$102$). An independent $256$-grid lower-bound code path
sits below the exact values at $N=16384,20000$ (ratios $0.89$, $0.87$).
The projection (pigeonhole) sanity bound $N\,D_N^*\ge N/(2(N+1))$ holds at
all checkpoints ($N\,D_N^*$ ranges $4.0$–$32.4$). All values, code, and
logs are archived in `artifacts/` (`dem_exact.py`, `dem_table.json`,
`summary.csv`, `dem_run.log`). ∎

## 5. Conjecture and uncertainty (NOT proved)

**Conjecture 4.** For this $\alpha$,
$D_N^*(P_N)\le 12(\log N)^2/N$ for all $N\ge 100$, with effective fitted
constant $\hat C\le 8$ (measured $\hat C\le 0.35$ on $N\le 20000$).

*Basis.* Classical theory (badly approximable $\Rightarrow$
$O((\log N)^2/N)$ in 2D) plus the finite-$N$ table above. *Gap.* A proof
needs the dyadic refinement of §3, not supplied here.

**Limitations / threats to validity.**
1. Theorem 2's bound is vacuous for $N<3\times10^8$ (RHS $>1$); it is a
   rate certificate, not a usable error bar at practical $N$.
2. Exact enumeration covers $N\le 20000$ only ($O(N^2)$ cost; $N=20000$
   took $8.4\,$s); the $N\to\infty$ rate claim is conjectural.
3. Floating-point point generation is certified only via the
   $3000\times$ gap argument, not interval arithmetic; a fully
   interval-certified DEM is future work.
4. Finite-$N$ fit $\hat C\le 0.35$ does not imply the uniform analytic
   constant $C\le 12$; hidden spikes at larger $N$ are not ruled out.
5. Only the fallback's upper-bracket half is delivered (nine checkpoints,
   not all dyadic $2^k$, $k=7,\dots,14$); the infinitary lower bound
   $D_N^*\ge c_{\rm low}/N$ is replaced by the finite-window sanity check
   $N\,D_N^*\ge N/(2(N+1))$.

## 6. Reproduction

```
python3 output/artifacts/step1_c0_etk.py   # c0, shell identity, Thm-2 constants
python3 output/artifacts/dem_exact.py      # exact DEM table + ETK instances (~15 s)
python3 output/artifacts/brackets_summary.py  # margins, Chat, cross-checks
```

Requires only `numpy` and `mpmath`; seeds are fixed (deterministic
Kronecker points, no RNG). QMC payoff: at the certified checkpoints the
Koksma–Hlawka error for this 2D cubic Kronecker rule is at most
$0.35(\log N)^2/N$ times the Hardy–Krause variation.
