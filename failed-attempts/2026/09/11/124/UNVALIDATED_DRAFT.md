# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the quarter-arc root-endpoint Widom expansion (lane-1009)

## Target claim (to be refuted)

Let $A=\{e^{i\theta}:|\theta|\le\pi/2\}$, $f=1_A\,|e^{i\theta}-i|^{1/2}|e^{i\theta}+i|^{1/2}$,
$D_n(f)$ its Toeplitz determinant. The target asserts

$$\log D_n(f) = n^2\log(\sqrt2/2) - \tfrac18\log n + e_4^\star + O(n^{-1/2}),$$

with $e_4^\star=\tfrac14\log2-\tfrac12\log\pi+2\log[G(5/4)/\Gamma(3/4)]
+\tfrac18\log(2+\sqrt2)\approx-0.52611$.
Put $L=\log(\sqrt2/2)=-\tfrac12\log2\approx-0.34657$ and
$Y_n=\log D_n(f)-n^2L$. The target implies $Y_n=O(\log n)$, in particular
$Y_n/n\to0$ and $Y_n+\tfrac18\log n\to e_4^\star$ (finite).

## Theorem (negative resolution)

The expansion is false. In fact $\limsup_{n\to\infty}Y_n/n\le L<0$,
so $Y_n\to-\infty$ linearly. Hence there is a missing $O(n)$ term
($nL$), and no finite $O(1)$ constant of the claimed form exists with the
claimed remainder. The log coefficient $-1/8$ is moot once the $O(n)$
term is missing.

## Proof

### 1. Transplant data (exact, self-contained)

On $A$, $|e^{i\theta}-i|^2=2-2\sin\theta$,
$|e^{i\theta}+i|^2=2+2\sin\theta$, so

$$f(e^{i\theta}) = 1_A(\theta)\,\sqrt{2\cos\theta},\qquad
W(\theta):=\tfrac12\log(2\cos\theta)$$

is the arc weight ($W$ is singular at $\theta=\pm\pi/2$, hence NOT analytic:
Widom's arc formula (1.3) of Charlier–Claeys does not apply directly).

Widom transplant for $\theta_0=\pi/2$ ($s=\sin(\theta_0/2)=\sqrt2/2$):
$\theta(\phi)=2\arcsin(s\sin(\phi/2))$,
$\tilde V(\phi)=W(\theta(\phi))$. Exact trig computation:
$\cos\theta(\phi)=1-2s^2\sin^2(\phi/2)=1-\sin^2(\phi/2)=\cos^2(\phi/2)$, so

$$2\cos\theta(\phi)=1+\cos\phi,\qquad
\tilde V(\phi)=\tfrac12\log(1+\cos\phi)=\log|1+e^{i\phi}|-\tfrac12\log2.$$

Mean (classical $\int_0^{\pi/2}\log\cos u\,du=-\frac\pi2\log2$, by
$\int\log\sin=\int\log\cos$ symmetry): with $u=\phi/2$,

$$\tilde V_0=\frac1{2\pi}\int_{-\pi}^{\pi}\tilde V
=\frac1{2\pi}\big[\pi\log2+2(-\pi\log2)\big]=-\tfrac12\log2=L.$$

Fourier tail ($k\ne0$): for $r<1$,
$\log|1+re^{i\phi}|=\Re\sum_{k\ge1}(-1)^{k+1}r^ke^{ik\phi}/k$,
and $\log|1+re^{i\phi}|\to\log|1+e^{i\phi}|$ in $L^1$ as $r\to1^-$
(dominated log majorant $C+|\log|\cos(\phi/2)||\in L^1$), so

$$c_k(\tilde V)=\frac{(-1)^{k+1}}{2|k|},\qquad k\ne0.$$

Hence the transplanted Szeg\H{o} series diverges:
$\sum_{k\le M}k|c_k|^2=\frac14H_M\sim\frac14\log M\to\infty$.
So the $O(1)$ Szeg\H{o} term of any naive Widom application is $+\infty$:
the analytic-$W$ route is structurally obstructed.

### 2. Pushforward identity (Lemma)

For continuous symmetric $W$ on $A$,
$\tilde W_0=\int_A W\,d\mu_{\rm eq}$, where
$d\mu_{\rm eq}=u(\theta)d\theta$,
$u(\theta)=\frac1{2\pi}\sqrt{(1+\cos\theta)/\cos\theta}$ is the
arc equilibrium measure (Charlier–Claeys Prop. 3.1(a)).
Proof: $d\theta/d\phi=s\cos(\phi/2)/\cos(\theta/2)$ gives pushforward
density $\frac1{2\pi}\cos(\theta/2)/(s\sqrt{\cos\theta})
=\frac1{2\pi}\sqrt2\cos(\theta/2)/\sqrt{\cos\theta}=u(\theta)$,
using $\sin^2(\phi/2)=1-\cos\theta$. In particular, with $w=\sqrt{2\cos}$,

$$\int_A \log w\,d\mu_{\rm eq} = \tilde V_0 = L<0,$$

by direct substitution (no numerics needed; the quadrature value
$-0.34657359027997\ldots$ in §4 merely confirms it).

### 3. Analytic majorants + monotonicity (killing blow)

$\log w$ is usc on closed $A$ ($-\infty$ at endpoints, integrable:
$|\theta\mp\pi/2|^{-1/2}\log|\theta\mp\pi/2|\in L^1$).
$h_k=\max(\log w,-k)$ is continuous symmetric, $h_k\downarrow\log w$;
extend by $-k$ off $A$; Weierstrass gives symmetric trig polynomials
$T_k\ge h_k\ge\log w$ on $A$ with $\int_A T_k\,d\mu_{\rm eq}\to L$.

For $g_k=1_Ae^{T_k}$ ($T_k$ analytic, positive symmetric symbol),
Widom's arc formula (Charlier–Claeys (1.3), $\theta_0=\pi/2$ fixed) gives

$$\log D_n(g_k)=n^2L+n\tilde T_{k,0}+O(\log n),\qquad
\tilde T_{k,0}=\int_A T_k\,d\mu_{\rm eq}\ (\text{Lemma}).$$

Toeplitz monotonicity ($0\le f\le g_k\Rightarrow0<T_n(f)\le T_n(g_k)
\Rightarrow\det$ monotone; $T_n(f)\succ0$ since $f>0$ on open $A$):
$Y_n\le Y_n^{(k)}:= \log D_n(g_k)-n^2L$. Dividing by $n$,

$$\limsup_{n\to\infty}\frac{Y_n}{n}\le\int_A T_k\,d\mu_{\rm eq}
\quad\forall k\ \Longrightarrow\ 
\limsup_{n\to\infty}\frac{Y_n}{n}\le L\approx-0.34657<0.$$

Thus $Y_n\le(L/2)n$ eventually: $Y_n\to-\infty$ linearly.
This contradicts $Y_n=-\frac18\log n+e_4^\star+O(n^{-1/2})$
(which forces $Y_n/n\to0$ and $Y_n+\frac18\log n$ bounded). ∎

## Corroboration (computation, not proof)

- High-precision moments + Cholesky (mpmath, dps=100, $n\le20$;
  float64 valid only $n\lesssim15$ since min eigenvalue $\sim C^{-n}$):
  least squares $Y_n=an+b\log n+c$ gives $a=-0.34678\approx L$,
  $b=+0.002\approx0$ (target: $a=0$, $b=-1/8$); full-model residuals
  $\sim10^{-4}$ vs target-model residuals $O(1)$.
- `output/artifacts/verify.py` (stdlib only) replays: transplant mean
  $=L$ to $9\times10^{-6}$, tail $c_k=(-1)^{k+1}/2k$ for
  $k\in\{1,2,3,4,8,16\}$, Szeg\H{o} partial $S(2000)=2.0446=\frac14H_{2000}$,
  and $O(n)$ fit $a\approx L$, $b\approx0$: prints `VERIFY_OK`.

## What is NOT claimed

The true next-order asymptotics (exact log coefficient, $O(1)$) are not
established here; the fit suggests $\approx nL+0.087+o(1)$ (log coeff
$\approx0$) but that is conjecture. This report is a disproof only:
it certifies the stated expansion—including its missing $O(n)$ term,
its $-1/8$, its $e_4^\star$, and its $O(n^{-1/2})$ remainder—is false.
The obstruction (singular transplant, divergent Szeg\H{o} ledger
$\frac14\log M$, inapplicability of analytic Widom+Bessel matching) is
the mechanism and redirects endpoint-parametrix work.
