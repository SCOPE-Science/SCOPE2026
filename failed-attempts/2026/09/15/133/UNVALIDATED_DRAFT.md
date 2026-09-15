# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Quantitative nonvanishing percentage in large weight via optimized mollifiers

## 1. Statement

Let $2k$ be the weight, $k\to\infty$ through even integers, $H_{2k}$ the
orthogonal Hecke eigenbasis of $S_{2k}(SL_2(\mathbf Z))$,
$\lambda_f(n)$ the Hecke eigenvalues ($\lambda_f(1)=1$),
$L(s,f)$ the associated $GL(2)$ $L$-function, and
$$
\omega_f=\frac1{L(1,\mathrm{sym}^2 f)},\qquad
W_{2k}=\sum_{f\in H_{2k}}\omega_f,\qquad
\mathbf E^h[A]=\frac1{W_{2k}}\sum_{f}\omega_f A_f .
$$
Put $N_{2k}=\dim S_{2k}=k/6+O(1)$.
For $k$ even the Fricke sign is $+1$, so $L(1/2,f)$ is not forced to
vanish (for $k$ odd the sign is $-1$; hence the restriction to even $k$).

Fix a mollifier length $M=k^{\Delta}$ with $0<\Delta\le\Delta_{\max}$,
where $\Delta_{\max}>0$ is the fixed admissible exponent furnished by the
quoted twisted second-moment Lemma T2 below. Any such fixed $\Delta$
satisfies the target ("some fixed logarithmic length $\Delta>0$").
Consider mollifiers on squarefree integers,
$$
M_x(f)=\sum_{\substack{m\le M\\ m\ \mathrm{squarefree}}}
x_m\,\frac{\lambda_f(m)}{\sqrt m},\qquad x\in\mathbf R^{\mathcal M}.
$$
No Selberg shape is imposed: $x$ is chosen by quadratic-form
optimization. A Selberg-like vector is used only as a feasible comparison.

**Theorem (Target).** As $k\to\infty$ through even integers, let
$\Delta\in(0,\Delta_{\max}]$ be fixed. There exist coefficient vectors
$x^\star=x^\star(k)$ with $L(x^\star)=1$ (notation below) such that with
$S_1(x)=\mathbf E^h[L(1/2,\cdot)M_x]$,
$S_2(x)=\mathbf E^h[L(1/2,\cdot)^2M_x^2]$,
$$
S_1(x^\star)=1+o(1),\qquad
S_2(x^\star)\le 1+\frac1\Delta+o(1),
\tag{*}
$$
the second-moment upper bound matching the diagonal quadratic form at the
optimizer (sharp constant-matching). Consequently with harmonic weights,
$$
\sum_{\substack{f\in H_{2k}\\ L(1/2,f)\ne0}}\omega_f
\ge \Bigl(\frac{\Delta}{1+\Delta}-o(1)\Bigr)
\sum_{f\in H_{2k}}\omega_f,
\tag{W}
$$
i.e. weighted proportion at least $c-o(1)$ with explicit
$c(\Delta)=\Delta/(1+\Delta)>0$; e.g. $\Delta=1/4$ (if admissible) gives
$c=1/5$, $\Delta=1/12$ gives $c=1/13$. In all cases, with
$\Delta=\min(\Delta_{\max},1/4)$ fixed, $c=c(\Delta)>0$ is an explicit
absolute constant (effectively computable from the published
$\Delta_{\max}$). Using the known negative second moment for
$L(1,\mathrm{sym}^2)$ (Lemma NM),
$$
\#\{f\in H_{2k}:L(1/2,f)\ne0\}\ge (c'-o(1))\,N_{2k}
\tag{N}
$$
for explicit absolute $c'=c^2c_w^2/C_{\mathrm{neg}}>0$ with $c_w,
C_{\mathrm{neg}}$ from Lemma NM.

*What is proved vs quoted.* Petersson formula, AFE, Weil/Bessel bounds,
the twisted first-moment asymptotic, the deep twisted second-moment
asymptotic (Voronoi + shifted convolution), the Selberg test-vector
evaluations, and Lemma NM are quoted as black boxes (all standard
published theory; the last is the "known negative moment" named in the
target). The quadratic-form optimization, the comparison argument giving
$c(\Delta)$, the Cauchy deductions (W)–(N), and the harmonic-to-natural
conversion are proved here. No step assumes the conclusion. In particular
we do NOT claim the second mollified moment follows from trivial Bessel
decay alone; it uses Lemma T2.

## 2. Standard inputs (quoted)

**Lemma P (Petersson, normalized).** For $m,n\ge1$,
$\mathbf E^h[\lambda_f(m)\lambda_f(n)]=\delta_{m,n}+E(m,n)$ where $E$ is
the Kloosterman–Bessel sum with Weil bound. If
$\sqrt{mn}\ll k^{1-\delta}$ then $E=O_A(k^{-A})$ uniformly (Bessel decay
dominates); in general $E$ must be analyzed further. We use Lemma P
directly only where the effective length satisfies this (first moment);
for the second moment we quote Lemma T2 instead of asserting trivial
negligibility.

**Lemma AFE.** For even $k$ (sign $+1$),
$L(1/2,f)=2\sum_n\lambda_f(n)n^{-1/2}V_k(n)$ with $V_k$ localizing to
$n\ll k^{1+\varepsilon}$ (rapid decay beyond), $V_k(n)=1+o(1)$ for fixed
$n$; and $L(1/2,f)^2$ has the usual Rankin–Selberg AFE localizing to
conductor-square-root range (up to $k^{2+\varepsilon}$ before Hecke
reduction). Exact shapes are irrelevant beyond truncation and
$V_k=1+o(1)$ on fixed arguments.

**Lemma T1 (twisted first moment; quoted).** For fixed
$0<\Delta<1$ and $m\le k^{\Delta}$ squarefree,
$$
\mathbf E^h\!\left[L(\tfrac12,\cdot)\,
\frac{\lambda(m)}{\sqrt m}\right]=\frac{V_k(m)}{m}\cdot m^{1/2}
\text{-normalized }=b_m+o(1),
$$
uniformly, with $b_1=1+o(1)$, $b_m\ll1/m$. Off-diagonal is negligible by
Lemma P since $m\cdot k^{1+\varepsilon}\le k^{2-\delta}$ for
$\Delta<1$. By linearity, for $x$ with $\|x\|_1\ll k^{A_0}$,
$S_1(x)=L(x)+o(1)$, $L(x)=\sum b_mx_m$.

**Lemma T2 (twisted second moment, deep; quoted).** There exists a fixed
$\Delta_{\max}>0$ (furnished by the published mollified-moment theory:
Petersson + Voronoi + shifted-convolution / spectral analysis; see e.g.
Kowalski–Michel–VanderKam and weight-aspect extensions, Blomer et al.
second-moment theory and subsequent weight-aspect mollification works)
such that uniformly for squarefree $m_1,m_2\le k^{\Delta}$,
$0<\Delta\le\Delta_{\max}$,
$$
\mathbf E^h\!\left[L(\tfrac12,\cdot)^2\,
\frac{\lambda(m_1)\lambda(m_2)}{\sqrt{m_1m_2}}\right]
=A_{m_1,m_2}+o(A^{\mathrm{diag}}),
$$
where $A=(A_{m_1,m_2})$ is the explicit diagonal Rankin–Selberg Gram
matrix (symmetric positive-definite for large $k$), and the $o(1)$ is
uniform in the range with polynomial factors in $m_i$ absorbed by the
power saving in $k$. Consequently, uniformly for vectors with
$\|x\|_2\ll(\log k)^C$ (all vectors used below),
$$
S_2(x)\le Q(x)+o(1),\qquad Q(x)=x^TAx,
$$
with matching constant (upper bound with the diagonal main term; a
two-sided asymptotic for the Selberg test vector is also quoted as part
of the standard calculation). The proof of Lemma T2 requires Voronoi
summation and shifted-convolution bounds beyond trivial Bessel decay,
because the raw $L^2$ length is $\sim k^2$ so
$\sqrt{m_1m_2n}\sim k^{1+\Delta}>k$; we cite this analysis rather than
reproduce it. Only the existence of some $\Delta_{\max}>0$, the form
$Q$, $A\succ0$, and the test-vector values below are used.

**Selberg test-vector values (quoted standard calculation).** For
$x^0_m=\mu(m)\log(M/m)/\log M$ ($m\le M$ squarefree),
$$
L(x^0)=1+o(1),\qquad Q(x^0)=1+\frac1\Delta+o(1).
$$
The first is PNT/Mertens; the second is the classical Selberg-mollifier
diagonal computation (prime-sum variance), as evaluated in the
references underlying Lemma T2. We quote both for this single explicit
vector.

**Lemma NM (known negative moment; black box named by target).**
There exist absolute effectively computable $c_w>0$,
$C_{\mathrm{neg}}<\infty$ with for large even $k$,
$W_{2k}\ge c_wN_{2k}$ and
$\sum_f\omega_f^2=\sum_fL(1,\mathrm{sym}^2f)^{-2}\le C_{\mathrm{neg}}N_{2k}$.

## 3. Iwaniec–Sarnak optimization (proved here; not Selberg weights)

Fix $\Delta\in(0,\Delta_{\max}]$ and the constraint $L(x)=1$. Consider
$\min_{L=1}Q$. Since $A\succ0$, $b\ne0$, the unique minimizer is
$$
x^\star=\frac{A^{-1}b}{b^TA^{-1}b},\qquad
\min Q=\frac1{b^TA^{-1}b}.
\tag{OPT}
$$
This $x^\star$ is the IS optimized choice: it solves the quadratic-form
problem defined by the actual moment matrices. With
$\tilde x^0=x^0/L(x^0)$ ($L=1$ exactly),
$$
\min_{L=1}Q\le Q(\tilde x^0)
=\frac{Q(x^0)}{L(x^0)^2}=1+\frac1\Delta+o(1).
$$
Hence $Q(x^\star)\le1+1/\Delta+o(1)$, $L(x^\star)=1$.
Norm control: $\|x^0\|_2$, $\|x^\star\|_2\ll(\log k)^C$
($b_m\ll1/m$ so $\|b\|_2=O(1)$; $A\to A_\infty\succ0$ so
$\|A^{-1}\|=O(1)$), hence Lemmas T1–T2 errors $o(1)$ apply uniformly.
Therefore (*) holds:
$S_1(x^\star)=1+o(1)$, $S_2(x^\star)\le1+1/\Delta+o(1)$.

## 4. Cauchy deductions (proved here)

Harmonic proportion: $S_1(x)^2\le S_2(x)\,\mathbf E^h[{\bf1}_{L\ne0}]$,
since $L\cdot M_x$ vanishes when $L=0$. Hence
$\sum_{L\ne0}\omega_f/W_{2k}\ge S_1^2/S_2$. Insert $x^\star$ to get (W)
with $c(\Delta)=\Delta/(1+\Delta)$.

Natural proportion: with ${\cal N}=\{L\ne0\}$,
$(\sum_{\cal N}\omega_f)^2\le|{\cal N}|\sum_{\rm all}\omega_f^2$.
Using (W) and Lemma NM,
$|{\cal N}|\ge(c-o(1))^2W_{2k}^2/(C_{\mathrm{neg}}N_{2k})
\ge(c^2c_w^2/C_{\mathrm{neg}}-o(1))N_{2k}$, i.e. (N).

## 5. Limitations

- Admissible $\Delta_{\max}$ and $A\succ0$/main-term shape are imported
  from published twisted-moment theory; no numeric value for
  $\Delta_{\max}$ beyond existence/positivity (hence effective
  computability of $c$) is asserted beyond the illustrative pairs
  $(1/4,1/5)$, $(1/12,1/13)$ computed in artifacts as $c(\Delta)$.
- $c_w,C_{\mathrm{neg}}$ are imported; $c'$ is via the stated formula,
  not an invented numeral.
- Kloosterman–Bessel/Voronoi/shifted-convolution details are cited, not
  reproduced; the length obstruction ($\sqrt{m_1m_2n}>k$ for $L^2$) is
  explicitly flagged, correcting any trivial-decay claim.
- Even $k$ used for sign $+1$.

## References (standard tools)

Iwaniec–Sarnak; Kowalski–Michel–VanderKam; Blomer–Fouvry–Kowalski–Michel–
Milićević–Sawin second-moment theory; Petersson/Weil/Voronoi/AFE;
Hoffstein–Lockhart et al. for Lemma NM; Luo and weight-aspect
mollification works for Lemma T2 range.
