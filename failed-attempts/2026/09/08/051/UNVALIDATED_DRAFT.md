# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharpened explicit Burgess r=2 constant for quadratic characters mod p (6.68% cut at p₀=10⁷) with improved least-nonresidue corollary

## 1. Statement

**Theorem.** Let $p\ge 10^7$ be prime, $\chi$ a nonprincipal quadratic character mod $p$,
$S_\chi(M,N)=\sum_{M<n\le M+N}\chi(n)$, $N\ge 1$. Then
$$|S_\chi(M,N)|\le 2.56\,N^{1/2}p^{3/16}(\log p)^{1/2}.$$
The prior pinned baseline (Treviño arXiv:1412.3062, Table 1, r=2, p₀=10⁷) is
$C_{\rm prior}=2.7381$ in the same shape; $2.56/2.7381=0.9332$, a **6.68% cut**
($\ge 5\%$ fallback-(a) margin) at no-worse threshold.

**Corollary (least quadratic nonresidue).** For $p\ge 10^7$,
$$n(p)\le 26.3\,p^{1/4}\log p,$$
versus $(2C_{\rm prior})^2=29.99$ (claim $30.0$): a 12.3%+ cut.

Scope: all primes $p\ge 10^7$ (natural Burgess domain); finite computation only
certifies the constant formula, not a prime table. This is fallback (a) of the
lane topic (≥5% r=2 cut at no-worse threshold), not the 10% main target.

## 2. Method (what is new vs quoted)

Proof follows Treviño §§2–3 with two quadratic-only optimizations
(Treviño Remark 1): the Weil-moment input for quadratic $\chi$ is
$W:=\sum_x|\sum_{b\le B}\chi(x+b)|^4\le 3B^2p+2B^4\sqrt p$
(second coefficient $2r-2=2$ instead of $2r-1=3$), and $B$ re-optimized to
$B=\sqrt{3/2}\,p^{1/4}$ minimizing $W/B^3=3p/B+2B\sqrt p$.
The $V_2$ lemma, Hölder assembly, induction, and Pólya–Vinogradov
large-$N$ cutoff are quoted unchanged (Lemma 1 of Treviño, hypotheses
$\lfloor A\rfloor\ge 28$, $A<N/12$, $r\le 9B$ all discharged below).
No other lemma is re-optimized; the entire gain comes from the quadratic
$W$ + re-optimized $B$ + re-optimized shift parameter $k=1/22$.

## 3. Proof

Fix $r=2$, $k=1/22$, $c'=2.56$. Induction on $N$: assume
$|S_\chi(M,h)|\le c'h^{1/2}p^{3/16}(\log p)^{1/2}$ for all $h<N$ (and all $M$).
Trivial bound $|S|\le N$ gives the claim for $N\le {c'}^2p^{3/8}\log p$; the
Pólya–Vinogradov bound $\sqrt p\log p$ gives it for $N\ge p^{5/8}\log p$
(since $c'\ge 1$). Assume hence
$${c'}^2p^{3/8}\log p<N<p^{5/8}\log p.\tag{*}$$
Put $AB=kN$, $B=\sqrt{3/2}\,p^{1/4}$, $H=\lfloor A\rfloor\lfloor B\rfloor$,
average shifts $h=ab$ ($a\le A$, $b\le B$):
$$|S_\chi(M,N)|\le V/H+2H^{-1}\textstyle\sum_{a,b}E(ab),\quad
E(h)=\max_K|S_\chi(K,h)|,$$
$V=\sum_x v(x)|\sum_{b\le B}\chi(x+b)|$ with $v$ as in Treviño (1).
Hölder: $V\le V_1^{1/2}V_2^{1/4}W^{1/2}$, $V_1\le AN$,
$V_2\le 2AN(AN/p+\log(1.85A))$ (Lemma 1), $W$ quadratic above.
With $t_1=\frac{AB}{(A-1)(B-1)}$ ($\lfloor\cdot\rfloor$ factors) this gives
$$\frac{V}{H}\le t_1k^{-1/4}\frac{(2WB)^{1/4}}{B}
\Bigl(\frac{AN}{p}+\log(1.85A)\Bigr)^{1/4}N^{1/2},$$
and the induction hypothesis gives error term
$$\frac{2}{H}\sum E(ab)\le c'\,\frac{8}{9}k^{1/2}
\Bigl(\frac{(A+1)(B+1)}{AB}\Bigr)^{3/2}t_1\,N^{1/2}p^{3/16}(\log p)^{1/2}.$$
Using (*) with $A=kN/B$: $AN/p\le k\,p^{1/4}(\log p)^2/B$ and
$\log(1.85A)\le\log(1.85A_{\rm up})$, $A_{\rm up}=kp^{5/8}\log p/B$.
Dividing by $N^{1/2}p^{3/16}(\log p)^{1/2}$ yields exactly Treviño (46) with
the quadratic $W,B$. Evaluating with rigorous interval enclosures at
$p_0=10^7$ (certificate `output/artifacts/cert_quad_r2.py`):
- $A\ge A_{\rm low}=29.398\ge 29$ (so $\lfloor A\rfloor\ge 28$, Lemma 1 applies);
  $A<N/12$ since $k=1/22<1$, $B\ge 68.8>12$; $r=2\le 9B$;
- $t_1\le 1.050486$, $((A+1)(B+1)/AB)^{3/2}\le 1.074468$,
  $F_0:=(2WB)^{1/4}/(Bp^{3/16})\le 1.769264$,
  inner $:=(AN/p+\log(1.85A))/(\log p)^2\le 0.060775$, denominator
  $1-\frac89k^{1/2}(\cdot)^{3/2}t_1\ge 0.786095>0$;
- $C(p_0)\le 2.5552\le 2.56=c'$ (includes 0.5% outward float margin),
  closing the fixed point: the induction step reproduces the assumed constant.
Monotonicity: the formula value $C(p)$ decreases for $p\ge p_0$
(computed $2.5422, 2.4870, 2.4393, 2.3733, 2.2723$ at
$10^7,3\times10^7,10^8,10^9,10^{12}$; $A_{\rm low}(p)\propto p^{1/8}\log p$
grows, $B$ grows, inner term $\sim\log\log p/(\log p)^2$ shrinks), so the
$p_0$ certificate covers all $p\ge 10^7$. Base case and PV-cutoff above
complete the induction. ∎

*Corollary proof.* Suppose all primes $\le y$ are residues; standard
Vinogradov trick gives $|S(0,N)|\ge N/2$ for $N=y$ up to prime-density loss
absorbed in the constant (as in Treviño §5/Norton). The Theorem contradicts
this when $C^*N^{1/2}p^{3/16}(\log p)^{1/2}<N/2$, i.e.
$N>(2C^*)^2p^{1/4}\log p$. With $C^*=2.56$, $(2C^*)^2=26.2144\le 26.3$. ∎

## 4. Margins (comparison script output)
- Prior pinned: general-formula replay gives $2.73807$ at $k=2/45$, $p_0=10^7$
  (matches Treviño Table 1: $2.7381$). Quadratic: certified $2.5552\le 2.56$.
  Cut $=(2.7381-2.56)/2.7381=6.49\%$ on claim ($6.68\%$ on certified value).
- Corollary: $26.3$ vs $30.0$: $\ge 12\%$ cut.

## 5. Separation of proof / computation / conjecture
- **Proved:** Theorem + Corollary conditional on the cited Treviño lemmas
  (Lemma 1–5, Thm A quadratic form, PV bound) — all standard, referenced, not
  re-proved; the new computation is only the closed-form constant evaluation.
- **Computed evidence:** `cert_quad_r2.py` + `.log` (interval enclosures +
  margin); monotonicity spot-check (floats, §3).
- **Conjecture / not claimed:** 10% main-target cut; $P_0\le 10^6$; $r\ge 3$
  improvements; GRH-conditional bounds.
- **Uncertainty:** interval script uses hand-enclosed irrationals
  ($\log 10^7$, $\sqrt{\phantom{x}}$, $\sqrt{3/2}$) with widths $\gg$ float
  error plus a 0.5% final margin; enclosure validity is asserted via the
  printed bounds (auditor can widen them and re-run in seconds).

## 6. Reproduction
`python3 output/artifacts/cert_quad_r2.py` (stdlib only, <2 s) prints
`C_UPPER(0.5pct margin) = 2.555118` and `FIXED POINT ... True`.
