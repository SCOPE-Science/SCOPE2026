# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the literal holomorphic-witness blowup claim on a bounded domain

## 1. Statement proved

Let $\Omega\subset \mathbb{C}^n$ be bounded (in particular the named
bounded smoothly truncated worm $W^{\mathrm{tr}}_{2\pi}$).
For integer $s\ge 0$ let $H^s(\Omega)$ be the standard Sobolev space with norm

$$\|f\|_{H^s}^2 = \sum_{|\alpha|\le s}\|D^\alpha f\|_{L^2(\Omega)}^2$$

on smooth functions, completed (equivalently by restriction; both admit
the same continuous inclusion into $L^2$ below).
Let $A^2(\Omega)=L^2(\Omega)\cap\mathrm{Hol}(\Omega)$ and
$P:L^2(\Omega)\to A^2(\Omega)$ be the Bergman (orthogonal) projection.

**Theorem.** For every integer $s\ge 0$ and every nonzero holomorphic
$f\in H^s(\Omega)$ one has $Pf=f$ (as $L^2$, hence as $H^s$ functions) and

$$\frac{\|Pf\|_{H^s(\Omega)}}{\|f\|_{H^s(\Omega)}}=1.$$

In particular there do **not** exist holomorphic data $f_j\in H^s(\Omega)$,
constants $C>0$, $\lambda>1$, and any $s\ge 0$ with

$$\frac{\|Pf_j\|_{H^s}}{\|f_j\|_{H^s}}\ge C\lambda^j\to\infty.$$

Hence the target claim, whose witness clause asserts exactly such a
holomorphic family with divergent ratios for all integers $s\ge S_0$,
is **false as stated**, on any bounded domain and a fortiori on
$W^{\mathrm{tr}}_{2\pi}$.

This does not decide Barrett-type irregularity witnessed by
*non-holomorphic* data; that is a different claim.

## 2. Proof

**Step 1 ($H^s\hookrightarrow L^2$).**
For integer $s\ge 0$ the term $\alpha=0$ belongs to the sum defining
$\|\cdot\|_{H^s}$, so for smooth $f$,

$$\|f\|_{L^2(\Omega)}\le \|f\|_{H^s(\Omega)}.$$

By density/completion (or restriction of an $H^s(\mathbb{R}^{2n})$
extension, whose $L^2(\mathbb{R}^{2n})$ norm dominates the $L^2(\Omega)$
norm) the inclusion $H^s(\Omega)\hookrightarrow L^2(\Omega)$ is continuous
with norm $\le 1$. Boundedness of $\Omega$ is used only to ensure the
standard Sobolev space has this property with Lebesgue measure finite;
no worm geometry is used. For $s=0$, $H^0=L^2$ with equality.

**Step 2 (Reproduction on holomorphic $L^2$ functions).**
By definition $P$ is the Hilbert-space orthogonal projection of
$L^2(\Omega)$ onto the closed subspace $A^2(\Omega)$. Hence

$$Pf = f\qquad\forall\,f\in A^2(\Omega),$$

with convergence in $L^2$. A function holomorphic in $\Omega$ in the
classical sense and belonging to $H^s\subset L^2$ lies in $A^2$
($L^2$ holomorphic functions are automatically smooth by elliptic
regularity of $\bar\partial$ / mean-value estimates; we only need that
a classically holomorphic $H^s$ function is an $L^2$ holomorphic
function).

**Step 3 (Ratio is identically one).**
Let $0\ne f\in H^s(\Omega)$ be holomorphic. By Step 1, $f\in A^2$;
by Step 2, $Pf=f$ in $L^2$. Since $f\in H^s$ by hypothesis, $Pf$
(viewed as the $L^2$ function $f$) lies in $H^s$ with identical
$H^s$ norm:

$$\|Pf\|_{H^s(\Omega)}=\|f\|_{H^s(\Omega)}\in(0,\infty),$$

the finiteness and nonvanishing following from $f$ being a nonzero
$H^s$ element. Therefore

$$\frac{\|Pf\|_{H^s}}{\|f\|_{H^s}} = 1.$$

If $f=0$ the quotient is undefined ($0/0$), so zero data cannot serve
as blowup witnesses either.

**Step 4 (No divergent holomorphic sequence).**
Taking suprema over nonzero holomorphic $H^s$ data,

$$\sup_{0\ne f\in H^s\cap\mathrm{Hol}}\frac{\|Pf\|_{H^s}}{\|f\|_{H^s}} = 1,$$

with the convention the set is nonempty (it contains e.g. constants,
since $\Omega$ is bounded so $1\in H^s\cap\mathrm{Hol}$; even if it were
empty there would still be no witness sequence). In particular no
sequence satisfies $\ge C\lambda^j\to\infty$ for any $C>0$, $\lambda>1$.
This holds for every integer $s\ge 0$, every $S_0$, and every bounded
$\Omega$, including $W^{\mathrm{tr}}_{2\pi}$.

**Remark on extensions.** If $\tilde P:H^s\to H^s$ is any bounded
extension agreeing with $P$ on a dense set of $H^s$ consisting of
$L^2$ functions (e.g. $C^\infty(\overline\Omega)$), continuity plus
$H^s\hookrightarrow L^2$ forces $\tilde Pf=f$ on holomorphic $H^s$
data as well, so the ratio remains $1$. There is no ambiguity in
$Pf_j$ for $f_j\in H^s\subset L^2$: the $L^2$ projection already
defines it.

## 3. Why the target fails and what it conflates

The classical Barrett/Krantz–Peloso mechanism proves $H^s$
unboundedness via **non-holomorphic** test functions $\varphi$
(e.g. compactly supported cutoffs representing the kernel,
$P\varphi = K_w\notin H^s$). On holomorphic inputs $P$ is the
identity, so it can never exhibit norm blowup. The target's phrase
"holomorphic data $f_j$ with ratios $\ge C\lambda^j$" asks the
identity map to be unbounded, which is impossible. Replacing
"holomorphic" by "smooth" yields a different, Barrett-type claim
not proved or disproved here.

## 4. Self-checks

- [x] $H^s\hookrightarrow L^2$ verified from the norm definition
  ($\alpha=0$ term); no hidden regularity of the worm boundary used.
- [x] Reproduction $Pf=f$ on $A^2$ is the definition of the Bergman
  projection; no kernel asymptotics needed.
- [x] Zero data excluded as undefined witnesses.
- [x] Constants belong to $H^s\cap\mathrm{Hol}$ on a bounded domain,
  so the supremum statement is non-vacuous.
- [x] No claim made about (non-holomorphic) Sobolev unboundedness
  of $P$; Barrett/Christ literature untouched.
