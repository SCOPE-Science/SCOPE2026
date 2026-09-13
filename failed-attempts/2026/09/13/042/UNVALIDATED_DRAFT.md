# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the critical N^{4/5} Painlevé-I scaling claim at g_c = −1/12

## 1. Theorem (target resolved in the negative)

Let, for $N\ge 1$ and $g\in\mathbb R$,

$$d\mu_{N,g}(M) = Z_{N,g}^{-1}\exp\!\big(-N\,\mathrm{Tr}(M^2/2+gM^4/4)\big)\,dM,$$

where $dM$ is Lebesgue measure on $N\times N$ Hermitian matrices and

$$Z_{N,g}=\int \exp\!\big(-N\,\mathrm{Tr}(M^2/2+gM^4/4)\big)\,dM\in(0,+\infty].$$

Let $g_c=-1/12$. Then:

**(a)** For every $N\ge 1$ and every $g<0$ (in particular $g=g_c$),
$Z_{N,g}=+\infty$. Hence the probability measure $\mu_{N,g_c}$ does not
exist and the expectation $\mathbb E_{\mu_{N,g_c}}[N^{-1}\mathrm{Tr}\,M^2]$
is undefined for every $N$.

**(b)** Consequently the claimed limit

$$L=\lim_{N\to\infty}N^{4/5}\big(\mathbb E_{\mu_{N,g_c}}[N^{-1}\mathrm{Tr}\,M^2]
-m_2^{(0)}(g_c)\big)$$

with $L$ finite and nonzero (equal to any explicit Painlevé-I constant
$c_*$) does not exist. The target claim, as stated for the fixed-coupling
Lebesgue Gibbs measure, is **false**.

**(c)** The number $m_2^{(0)}(g_c)=4/3$ is well defined only as a formal
analytic continuation of the genus-zero solution from $g>g_c$; it is not a
limit of expectations, since the expectations do not exist.

A formal supplementary calculation (§4) shows the claimed exponent $4/5$
is additionally wrong at the level of power counting even for a regularized
model: the averaged-moment double-scaling correction scales as $N^{-6/5}$,
and the genus-one coefficient is non-integrable, so no point-evaluation
constant $u(0)$ can give the averaged moment.

## 2. Proof that $Z_{N,g}=+\infty$ for $g<0$

Write $|g|=-g>0$. The log-density (unnormalized) is

$$E(M) := -N\,\mathrm{Tr}\,V_g(M),\qquad
V_g(M)=M^2/2+gM^4/4,$$

i.e. with eigenvalues $\lambda_i(M)$,

$$E(M) = -N\sum_{i=1}^N\frac{\lambda_i^2}{2}
+N|g|\sum_{i=1}^N\frac{\lambda_i^4}{4}.$$

Decompose $M=xI+Y$ with $x\in\mathbb R$ and $Y$ in a fixed transverse
hyperplane (e.g. $Y\perp I$ in Hilbert–Schmidt inner product). The map
$(x,Y)\mapsto M$ is a linear isomorphism, so $dM=J\,dx\,dY$ with a constant
Jacobian $J>0$. Eigenvalues of $M$ are $x+\lambda_i(Y)$.

Let $B=\{Y:\|Y\|_{HS}\le 1\}$ be the transverse unit ball; $0<\mathrm{vol}(B)<\infty$.
For $Y\in B$, each eigenvalue satisfies $|\lambda_i(Y)|\le\|Y\|_{HS}\le 1$.
Hence for $|x|\ge 1$ and $Y\in B$:

- $\sum_i (x+\lambda_i(Y))^2 \le N(|x|+1)^2$,
- $\sum_i (x+\lambda_i(Y))^4 \ge N(|x|-1)^4$
  (each $|x+\lambda_i|\ge |x|-1$).

Therefore uniformly for $Y\in B$,

$$E(xI+Y)\ge m(x):=N^2\Big[-\frac{(|x|+1)^2}{2}
+|g|\frac{(|x|-1)^4}{4}\Big].$$

Since the quartic dominates, $m(x)\to+\infty$ as $|x|\to\infty$; in
particular there is $X_0$ (e.g. $X_0=12$ at $|g|=1/12$, verifiable by direct
substitution and monotonicity of $u^4/48-(u+2)^2/2$ for $u=|x|-1\ge 11$)
with $m(x)\ge 0$ for all $|x|\ge X_0$. Then

$$Z_{N,g}\ge J\int_{|x|\ge X_0}\int_B e^{E(xI+Y)}\,dY\,dx
\ge J\,\mathrm{vol}(B)\int_{|x|\ge X_0} e^{m(x)}\,dx
\ge J\,\mathrm{vol}(B)\int_{|x|\ge X_0}1\,dx = +\infty.$$

This uses only Fubini–Tonelli for the nonnegative integrand. The argument
works for every $N\ge 1$ and every $g<0$. For $N=1$ it is the elementary
divergence $\int_{\mathbb R}\exp(-x^2/2+|g|x^4/4)\,dx=+\infty$.
∎

Hence $\mu_{N,g_c}$ cannot be normalized, no expectation exists at any $N$,
and the limit $L$ in the target is meaningless. A conjunction asserting its
existence, finiteness, nonvanishing, and explicit value is false. This is a
complete TARGET refutation via non-existence, one of the verdicts explicitly
licensed by the topic ("non-existence of the limit").

## 3. Status of the planar value and the genus expansion

The planar string equation $R(1+3gR)=t$ gives
$R(t,g)=[-1+\sqrt{1+12gt}]/(6g)$. At $g_c=-1/12$,
$R(t)=2-2\sqrt{1-t}$, $R(1)=2$, and formally

$$m_2^{(0)}(g_c)=2\int_0^1 R(t)\,dt = 2\cdot\frac23=\frac43,$$

verified numerically in `artifacts/verify_disproof.py`
($1.33333334\approx 4/3$). This is analytic continuation, not a limit of
expectations.

The $N^{-2}$ genus-one correction from
$R_n[1+g(R_{n-1}+R_n+R_{n+1})]=n/N$ with
$R_n=R(t)+N^{-2}R_1(t)+\cdots$ is

$$R_1(t)=-\frac{gRR''}{1+6gR},\qquad 1+6gR=\sqrt{1+12gt}.$$

At $g_c$, $R''(t)=\tfrac12(1-t)^{-3/2}$ and

$$R_1(t)=\frac{1}{12}\frac{R(t)R''(t)}{\sqrt{1-t}}
\sim\frac{1}{12}(1-t)^{-2},\qquad t\to1^-,$$

confirmed numerically ($(1-t)^2R_1\to 1/12$). It is non-integrable at
$t=1$, so the fixed-$g$ genus-one formula indeed breaks down at $g_c$ —
the only correct fragment of the target's "in particular" clause — but
this does not rescue the main $N^{4/5}$ claim, whose objects do not exist.

## 4. Formal exponent mismatch (supplementary, heuristic level)

Even setting aside §2 (e.g. under a cutoff regularization, which is a
different problem), the number $4/5$ cannot be the averaged-moment
correction exponent. Standard $m=2$ double scaling has boundary-layer width
$N^{-4/5}$ and amplitude $N^{-2/5}$ for $R_n$ near $n\approx N$. The
averaged moment $N^{-1}\sum_{n<N}(R_{n+1}+R_n)$ therefore receives

$$N^{-1}\times \underbrace{N^{1/5}}_{\text{\# terms}}
\times \underbrace{N^{-2/5}}_{\text{amplitude}}
= N^{-6/5},$$

not $N^{-4/5}$; $4/5$ is the scaling-variable exponent, not the observable
exponent. The formal $N^{-2}\sum R_1$ tail itself is $O(1/N)$
($N\times\text{tail}\to\pi^2/72$, $N^{4/5}\times\text{tail}\to 0$ in the
script). Moreover an averaged correction needs $\int u(s)\,ds$ of the
Painlevé-I transcendent, not the point value $u(0)$. So the "explicit
constant $c_*$ determined by Painlevé I at zero deformation parameter" is
dimensionally wrong for the second moment. This is recorded as supporting
evidence; the rigorous disproof is §2.

## 5. What was checked

- Planar integral $=4/3$, $(1-t)^2R_1(t)\to 1/12$, formal tail $O(1/N)$ with
  $N^{4/5}\times\text{tail}\to 0$, log-density $\to+\infty$ along the
  identity ray with explicit thresholds, and the $N^{-6/5}$ power count —
  all reproduced by `output/artifacts/verify_disproof.py`, results in
  `output/artifacts/verify_results.json`.
- No literature search was used; the disproof is elementary and self-contained.
- No cutoff or analytic-continuation reinterpretation was smuggled in: the
  topic defines the fixed-$g$ Lebesgue Gibbs measure, which is the object
  shown not to exist.

## 6. Conclusion

The target is disproved: at fixed $g_c=-1/12$ the stated $N^{4/5}$ scaling
limit with finite nonzero Painlevé-I constant cannot hold because the
finite-$N$ Gibbs measure and its mean do not exist at any $N$, and
independently the exponent $4/5$ and point-evaluation constant are
inconsistent with double-scaling power counting for the averaged moment.
