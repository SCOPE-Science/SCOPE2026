# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Strong honest definition for the translate cell in (R,<,+,e^Z) — TARGET certificate

## Setting
- $M=(\mathbb R,<,+,G)$, $G=e^{\mathbb Z}$, $e$ transcendental $>1$ (Hermite).
- $\varphi(x_1,x_2;y):=G(x_1-x_2+y)$, $|x|=2$, $|y|=1$.
- $\varphi_0(x;y):=G(x+y)$ is the one-variable fragment ($\varphi$ with $x_2=0$).

## Result
$\varphi$ is distal, via an explicit strong honest definition for
$\varphi^{\mathrm{opp}}(y;x_1,x_2)$ (hence $\varphi$ distal by $x/y$-symmetry
of distality), plus a uniform fiberwise cell family for $\varphi$ using at
most $N=2$ pairs from the finite set $A$. Corollary: $\varphi_0$ is distal
with the same engine, and $VC(\varphi_0)=2$ exactly. All verifications use
only $+$, $<$, $G$ (\S4 gives the $+$-only forms).

## Lemma U (difference uniqueness)
If $c\ne 0$ and $e^p-e^q=e^n-e^m=c$ with $p,q,n,m\in\mathbb Z$, then
$(p,q)=(n,m)$. If $e^p-e^q=0$ then $p=q$.
*Proof.* Clear denominators (multiply by $e^K$, $K$ large) to get
$P(e)=0$ for $P=X^{p+K}-X^{q+K}-X^{n+K}+X^{m+K}\in\mathbb Z[X]$.
By transcendence $P\equiv 0$. Coefficient comparison: the two $+1$ terms and
two $-1$ terms must cancel pairwise; for $c\ne 0$ this forces $p=n$, $q=m$
(the only other cancellation makes all four exponents equal, i.e.\ $c=0$). ∎

## Schema (finite cell family, $\le 2$ pairs from $A$)
Fix finite nonempty $A\subset\mathbb R^2$ and $b\in\mathbb R$.
Put $D_A=\{a_1-a_2:a\in A\}$, $T=\{d\in D_A:d+b\in G\}$ (hitting diffs).
- **Empty** ($T=\varnothing$): $\theta_\perp:=(x_1\ne x_1)$.
- **Single diff** ($T=\{d\}$, witnessed by $w\in A$ with $d=w_1-w_2$):
  $\theta_w(x):=(x_1-x_2=d)$, i.e.\ $x_1+w_2=x_2+w_1$ ($+$-only).
- **Two diffs** ($d_1\ne d_2$ in $T$, witnessed by $w^1,w^2\in A$):
  with $\delta=d_1-d_2$,
  $$\theta_{w^1,w^2}(x):=\exists u\,
    \bigl(G(u)\land G(u-\delta)\land G(x_1-x_2+u-d_1)\bigr),$$
  $+$-only form:
  $$\exists u\,\exists v\,\exists t\,
    \bigl(G(u)\land G(v)\land G(t)\land
    u+w^1_2+w^2_1=v+w^1_1+w^2_2\ \land\
    x_1+u+w^1_2=t+x_2+w^1_1\bigr).$$
  (First equality says $v=u-\delta$; second says $t=x_1-x_2+u-d_1$.)
- $A=\varnothing$: $\theta_\perp$ (degenerate, $0$ params).

## Correctness (honest definition for $\varphi^{\mathrm{opp}}$, uniform in $A$)
**Honest-definition schema with parameters from $A$.** Recall: $\psi(x;d)$
($d$ a tuple of $x$-sort) is an SHD for $\varphi$ if for every finite nonempty
$A\subset\mathbb R^2$ and $b\in\mathbb R$ there is $d\in A^{|z|}$ with
$\psi(A;d)=\varphi^b(A)$ and $\psi(M;d)\subseteq\varphi^b(M)$
($\forall x\,(\psi(x;d)\to\varphi(x;b))$); $A=\varnothing$ is degenerate.
Our three cells use exactly this parameter source:
- *Single diff.* $\theta_w\Rightarrow\varphi^b$: $x_1-x_2=d\Rightarrow
  x_1-x_2+b=d+b\in G$. Trace on $A$: $a\in A$ satisfies $\theta_w$ iff
  $a_1-a_2=d$ iff (as $T=\{d\}$) $a_1-a_2+b\in G$ iff $\varphi(a;b)$. Uses $1$ pair.
- *Two diffs.* Write $d_i+b=e^{n_i}$ ($n_1\ne n_2$ since $d_1\ne d_2$);
  $\delta=e^{n_1}-e^{n_2}$. By Lemma U the unique $u$ with
  $u,u-\delta\in G$ is $u=e^{n_1}$ (with $v=e^{n_2}$). Hence for
  $d=x_1-x_2$: $\theta$ holds iff $d+u-d_1\in G$ for $u=e^{n_1}$ iff
  $d+b\in G$ (as $e^{n_1}-d_1=b$): indeed $t=d+e^{n_1}-d_1=d+b$ up to the
  $+$-only rearrangement, and conversely. So $\theta_{w^1,w^2}$ is globally
  equivalent to $\varphi(x;b)$, hence honest with correct trace. Uses $2$ pairs.
- *Empty.* $\theta_\perp$ matches empty trace and entails vacuously.
Cases exhaust $T$; at most $2$ pairs used, all parameters $w,w^1,w^2\in A$.
- *Partition note.* The schema above is the honest definition for
  $\varphi^{\mathrm{opp}}$ ($y$ as the object variable): read with $b$ as the
  object point and $A$ as the finite parameter set, it gives the SHD cell for
  every $\varphi^{\mathrm{opp}}$-type over a finite set. Since a formula is
  distal iff its opposite is distal (distality is partition-symmetric), this
  proves $\varphi$ distal. Equivalently, read fiberwise: for fixed finite
  $A\subset\mathbb R^2$ and parameter $b$, the same case split yields the
  uniform cell $\theta$ (with data from $A$) trace-correct on $A$ and implying
  $\varphi^b$ — the distal cell decomposition of $\varphi$ with $N=2$ pairs.
Thus $\varphi$ has a strong honest definition (finite cell family, bound
$N=2$ pairs) — $\varphi$ is distal (hence NIP as a formula). No global NIP of
$M$ is assumed; it follows for $\varphi$ from distality.

## Corollary ($\varphi_0$, $K=2$, $VC=2$)
Same engine in one variable. For finite $A\subset\mathbb R$, $b$:
$S=\{s\in A:s+b\in G\}$. $|S|=0$: $\perp$. $|S|=1$, $S=\{s\}$: $x=s$
($\Rightarrow\varphi_0^b$; trace exact on $A$). $|S|\ge 2$ with $s_1\ne s_2$:
$\exists u\,(G(u)\land G(u-(s_1-s_2))\land G(x+u-s_1))$
($+$-only: $u+s_2=v+s_1$, $x+u=t+s_1$), globally equivalent to
$\varphi_0(x;b)$ by Lemma U. So $K=2$.
$VC(\varphi_0)=2$: $\{1,e\}$ is shattered ($a\in\{-10,e^2-1,e^2-e,0\}$ give
$\varnothing,\{1\},\{e\},\{1,e\}$; checks: $e^2+e-1\in(e^2,e^3)$,
$e^2-e+1\in(e,e^2)$, so the singletons miss the other point); no $3$-set
$\{b_1,b_2,b_3\}$ shatters: hitting $b_i\ne b_j$ pins $a$ uniquely (as
$b_i-b_j=e^n-e^m$ pins $(n,m)$ by Lemma U, so $a=e^n-b_i$), hence any
full-pattern witness (hitting all three) coincides with each pair's unique
double-hitter — contradicting the pair-only patterns, which require missing
the third point. So $VC=2$, and $VC(\varphi)\ge 2$ (set $x_2=0$).

## Machine replay
- `output/artifacts/verify.py` (`python3 output/artifacts/verify.py` → `VERIFY_OK`):
  exact Laurent-polynomial arithmetic (monomial $\Leftrightarrow$ in $G$; no floats).
  (U) $83\,521$ exponent-quadruples ($|{\cdot}|\le 8$): polynomial identity
  $\Leftrightarrow$ index equality (bounded window of Lemma U; general case by the
  transcendence proof above). (V) $2$-shattering table + pair-collision instance.
  (R) schema replay on representatives of all trace classes
  (empty/singleton/multi-same-diff/two-distinct-diff) checking trace equality on
  the test finite set and entailment over the test universe (existential $u$ over
  bounded exponents with canonical $u$ verified in range), plus the $\varphi_0$
  pair case. Generalization to all $(A,b)$ is the proof above.
- `output/artifacts/recovery_test.py` (→ `RECOVERY_OK`): bounded numeric +
  polynomial sanity checks (uniqueness window, shattering intervals, pair-forces-full).

## Limitations / scope notes
- Proves distality of the formula $\varphi$ (hence $\varphi_0$), not distality of
  the full theory $\mathrm{Th}(M)$ nor a classification of all
  $(\mathbb R,<,+,\alpha^{\mathbb Z})$.
- Uses Hermite's transcendence of $e$ as a cited theorem; everything else is
  elementary (ordered-group arithmetic + Lemma U).
- Certificate is a finite cell family ($\perp$ / line / pair-existential) with
  bound $N=2$ pairs; the $A=\varnothing$ case uses the $0$-parameter $\perp$ cell.
