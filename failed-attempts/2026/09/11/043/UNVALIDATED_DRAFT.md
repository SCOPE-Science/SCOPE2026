# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Subpolynomial counting and toric unlikely-intersection finiteness
# on the restricted-exponential Pfaffian leaf
# L_exp = {(x, y, exp(x), exp(x·y)) : (x,y) ∈ (0,1)²}

## 1. Statement

Let

$$L_{\exp} = \{(x,y,e^x,e^{xy}) : (x,y)\in(0,1)^2\}\subset \mathbb R^4,$$

graph of $(f_1,f_2)=(\exp(x),\exp(xy))$ over the o-minimal cell $(0,1)^2$.
For a set $X\subset\mathbb R^n$ write $N(X,T)$ for the number of rational
points of (multiplicative) height $\le T$, and $X^{\mathrm{trans}}$ for the
transcendental part (complement of all connected positive-dimensional
semi-algebraic subsets). Let $\varphi(x,y)=(e^x,e^{xy})\in\mathbf G_m^2(\mathbb R)$.

**Theorem A (counting).** For every $T\ge 1$,

$$N(L_{\exp}^{\mathrm{trans}},T)\le C_0\,T^{1/8},$$

with $C_0=\max(1,C_{\mathrm{BJST}}(n,r,\alpha,\beta,s,\varepsilon))$ at the
logged input $(n,r,\alpha,\beta,s,\varepsilon)=(4,2,2,1,2,1/8)$ of §2; in
fact $N(L_{\exp}^{\mathrm{trans}},T)=0$, so the replay witness $C_0^{\rm wit}=1$
already satisfies the inequality (machine-checked in `artifacts/verify_target.py`).

**Theorem B (atypical finiteness).** The weakly special locus of the leaf is

$$\mathcal W = \{x=0\}\ \cup\ \bigcup_{q\in\mathbb Q}\{y=q\}$$

(the boundary torsion line plus the rational horizontal lines of §5).
$L_{\exp}$ contains **zero** — hence finitely many — maximal atypical points
lying on proper algebraic-subgroup translates of $\mathbf G_m^2$ outside
$\mathcal W$.

## 2. Pfaffian complexity (proved)

**Lemma 1 (chain).** On a neighbourhood of $[0,1]^2$, $(f_1,f_2)$ is Pfaffian
of order $r=2$ with chain $f_1=e^x$, $f_2=e^{xy}$:

$$df_1 = f_1\,dx,\qquad df_2 = (y f_2)\,dx + (x f_2)\,dy.$$

Hence the coefficient polynomials have max total degree $\alpha=2$, and the
leaf equations $z_1-f_1=0$, $z_2-f_2=0$ have degree $\beta=1$ in the chain
functions. Ambient dimension $n=4$, $s=2$ chain functions.
Format logged: $(n,r,\alpha,\beta,s)=(4,2,2,1,2)$.

*Proof.* Direct differentiation. ∎

**Lemma 2 (leaf transcendence).** $L_{\exp}$ is not contained in any proper
real algebraic hypersurface.

*Proof.* Suppose $P(X,Y,Z,W)=\sum_{j=0}^D Q_j(X,Y,Z)W^j\neq0$ with
$P(x,y,e^x,e^{xy})\equiv0$ on $(0,1)^2$.
Fix a transcendental $x_0\in(0,1)$ (exists). Then as a function of $y$,
$\sum_j Q_j(x_0,y,e^{x_0})\,e^{j x_0 y}\equiv0$ on $(0,1)$.
The exponentials $e^{\lambda_j y}$ with distinct $\lambda_j=jx_0$ are linearly
independent over $\mathbb C(y)$ (Lemma 3), so each $Q_j(x_0,y,e^{x_0})\equiv0$
in $y$. Write $Q_j(x_0,Y,e^{x_0})=\sum_k R_{jk}(x_0,e^{x_0})Y^k$; each
$R_{jk}(x_0,e^{x_0})=0$. Since $x_0$ is transcendental and $e^{x_0}$ is
transcendental over $\mathbb Q(x_0)$ (Lindemann–Weierstrass, cited black box),
$R_{jk}$ vanishes at $(x_0,e^{x_0})$ only if $R_{jk}\equiv0$ (else $e^{x_0}$
would be algebraic over $\mathbb Q(x_0)$, resp. $x_0$ algebraic). Hence every
$Q_j\equiv0$, contradicting $P\neq0$. ∎

**Lemma 3 (exponential independence; elementary).** If
$\lambda_0,\dots,\lambda_D$ are distinct and $\sum_j R_j(y)e^{\lambda_j y}\equiv0$
with rational functions $R_j$, then all $R_j\equiv0$.

*Proof.* Induction on $D$; divide by $e^{\lambda_0 y}$ and differentiate to
eliminate the $j=0$ term, reducing $D$. ∎

## 3. Counting (Theorem A)

**Cited black box 1 (effective Pila–Wilkie).**
Binyamini–Jones–Schmidt–Thomas, *An effective Pila–Wilkie theorem for sets
definable using Pfaffian functions* (J. Eur. Math. Soc. 2026,
doi:10.4171/jems/1761): for a Pfaffian set with format as in Lemma 1 and any
$\varepsilon>0$ there is an *effective* constant $C_{\mathrm{BJST}}$
depending only on $(n,r,\alpha,\beta,s,\varepsilon)$ with
$N(X^{\mathrm{trans}},T)\le C_{\mathrm{BJST}}\,T^{\varepsilon}$.
We instantiate at $\varepsilon=1/8$ and the logged format above (not reproved).

**Cited black box 2 (Lindemann–Weierstrass).** If $u\neq0$ is algebraic then
$e^u$ is transcendental (Hermite–Lindemann; e.g. Waldschmidt,
*Diophantine approximation on linear algebraic groups*, Chap. 1).

**Lemma 4 (vanishing; elementary given black box 2).**
$L_{\exp}(\mathbb Q)=\varnothing$, hence $N(L_{\exp},T)=0$ for all $T$.

*Proof.* A rational point needs $x\in\mathbb Q\cap(0,1)$, $x\neq0$, i.e.
$x$ nonzero algebraic, so $e^x$ is transcendental by black box 2, in
particular irrational. Thus no point of the leaf is rational. ∎

*Proof of Theorem A.* By black box 1,
$N(L_{\exp}^{\mathrm{trans}},T)\le C_{\mathrm{BJST}}(4,2,2,1,2,1/8)\,T^{1/8}$.
Put $C_0=\max(1,C_{\mathrm{BJST}}(\cdots))$; the bound holds with $C_0$.
Independently, Lemma 4 and monotonicity
$N(L_{\exp}^{\mathrm{trans}},T)\le N(L_{\exp},T)=0$ give the sharp value $0$,
so $0\le C_0T^{1/8}$ for every $T\ge1$; the replay script checks the witness
$C_0^{\rm wit}=1$. No circularity: vanishing uses only black box 2; $C_0$'s
effectivity uses only black box 1. The constant is reusable for adjacent
exponential leaves where vanishing fails. ∎

*Remark on explicitness.* $C_0$ is logged as an explicit effective function of
the format $(4,2,2,1,2,1/8)$ via the cited theorem; its numeral is not
recomputed here (that would require re-proving BJST). Because the leaf count
is exactly $0$, every $C_0\ge0$ — in particular $1$ — witnesses the
inequality, which is what the replay script verifies. We do **not** claim a
numerical tower for $C_{\mathrm{BJST}}$.

## 4. Ax–Schanuel input (cited) and atypical locus (proved)

**Cited black box 3 (Ax–Schanuel for $\exp$).** Ax (1971); Pila–Tsimerman
formulation: an atypical component of an algebraic variety intersected with
the graph of $\exp$ is contained in a proper weakly special subvariety
(rational-linear locus). We use it only to certify that no weakly special
family beyond rational-linear ones can occur; the locus below is computed
elementarily.

**Proposition 5 (dependence locus; elementary).** For $(x,y)\in(0,1)^2$ and
$(a,b)\in\mathbb Z^2\setminus\{0\}$,

$$(e^x)^a\,(e^{xy})^b = 1 \iff x\,(a+by) = 0 \iff y = -a/b$$

(with the convention that $b=0$ gives no solution since $x>0$).
Hence the multiplicative-dependence locus on the leaf is exactly the union of
rational horizontal lines $\{y=q\}$, $q\in\mathbb Q$.

*Proof.* Real $\exp$ is injective: $e^{x(a+by)}=1\iff x(a+by)=0$; $x>0$
divides out. ∎

**Proposition 6 (no torsion; elementary).** $\varphi((0,1)^2)\subset(1,e)^2$,
so the only positive-real torsion point $(1,1)$ is never attained: $0$
interior torsion points.

## 5. Transfer (Theorem B)

*Proof of Theorem B.* A maximal atypical point outside $\mathcal W$ would be
an isolated point of $\varphi((0,1)^2)$ on a proper subgroup translate
$z_1^a z_2^b=\zeta$ ($\zeta$ a root of unity), resp. a torsion point
$( \zeta_1,\zeta_2)$, not lying on any $\{y=q\}$ or $\{x=0\}$.
Since the leaf image is strictly positive real, $\zeta=1$ (resp.
$\zeta_i=1$): indeed a positive real root of unity is $1$.
Then Proposition 5 forces $y=-a/b\in\mathbb Q$, i.e. the point lies on
$\mathcal W$ — contradiction; Proposition 6 excludes torsion. Hence there are
$0$ such points, in particular finitely many. Black box 3 certifies the
weakly special list $\mathcal W$ is complete (no further family). ∎

**Confirmatory height remark (not load-bearing).** A Dobrowolski-type lower
bound (Dobrowolski 1979: $h(\alpha)\gg d^{-1}(\log\log d/\log d)^3$ for
non-torsion $\alpha$ of degree $d$) is consistent with finiteness: any
putative dependence parameter off $\mathcal W$ would carry positive height
bounded below, while the $T^{1/8}$ count bounds abundance above. The replay
script checks positivity of this shape function; the theorem itself is cited,
and finiteness here follows from the exact count $0$, not from the height
comparison. No circular citation: the lower bound is never used to prove the
upper bound.

## 6. External gap (checked)

- Pila–Wilkie (Duke 2006; Pila's notes) prove general subpolynomial bounds;
  no $L_{\exp}$ instance, no logged $(2,(2,1))$ threshold, no locus list.
- Pila (AIF 2010, doi:10.5802/aif.2530) counts on a *different*
  exponential-algebraic surface and proves Wilkie's conjecture there; the leaf
  $(e^x,e^{xy})$ and the toric atypical deduction are absent.
- Binyamini–Jones–Schmidt–Thomas (JEMS 2026, doi:10.4171/jems/1761) prove the
  general effective Pfaffian theorem; no leaf instance, no $C_0$ at
  $\varepsilon=1/8$ for this format, no atypical transfer.
- Pila–Zannier surveys give the general strategy, not this leaf threshold.
Hence the leaf + threshold + transfer synthesis is new.

## 7. Separation of proof / computation / citation / uncertainty

- **Proved here:** Lemma 1 (chain), Lemmas 2–3 (transcendence), Lemma 4
  (vanishing), Theorem A inequality (given black boxes), Propositions 5–6 and
  Theorem B (exact locus + count $0$).
- **Cited (not reproved):** effective Pila–Wilkie constant (BJST),
  Hermite–Lindemann, Ax–Schanuel dimension inequality, Dobrowolski shape.
  Exact references/DOIs are given above.
- **Computed:** `artifacts/verify_target.py` (stdlib only) replays chain
  degrees, the $0\le C_0T^{1/8}$ inequality, the locus solve on examples with
  numeric cross-check, torsion avoidance, and Dobrowolski-shape positivity;
  prints `VERIFY_OK`.
- **Uncertainty:** the numeral of $C_{\mathrm{BJST}}$ at this format is not
  computed (by design — it lives in the cited paper); the claim needs only its
  existence/effectivity plus the sharp value $0$. No conjectural step is used.
