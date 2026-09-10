# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Klein invariant-series non-obstruction certificate (degree ≤ 2000)

## 1. Object and notation (after Bauer–Di Rocco–Harbourne–Huizenga–Seceleanu–Szemberg, arXiv:1609.08648)

Let $\mathcal{K}$ be the Klein configuration of $21$ lines in $\mathbf{P}^2$,
with $21$ quadruple points and $28$ triple points as its singular locus, and let
$X_{\mathcal{K}}$ be the blowup of $\mathbf{P}^2$ at these $49$ points.
Write $H$ for the pullback of a line and $E_4$, $E_3$ for the sums of the
exceptional divisors over the quadruple and triple points. The intersection form
satisfies $H^2=1$, $E_4^2=-21$, $E_3^2=-28$, pairwise orthogonal. The class of
the line configuration is $A_{\mathcal{K}}=21H-4E_4-3E_3$ with $A_{\mathcal{K}}^2=-147$.

The target divisor (Conjecture 5.8 of Bauer et al.) is

$$D = 28H - 2E_4 - 5E_3, \qquad D^2 = 0,\quad D\cdot A_{\mathcal{K}} = 0,$$

and $D$ nef implies the Waldschmidt constant $\widehat{\alpha}(I_{\mathcal{K}})=13/2$
(Lemma 3.3). For $B=dH-m_4E_4-m_3E_3$,

$$D\cdot B = 28d - 42m_4 - 140m_3.$$

Let $T=\mathbf{C}[\Phi_4,\Phi_6,\Phi_{14}]\subset S$ be the invariant subring and
$T_d(-\!m_4E_4-\!m_3E_3)$ the subspace of degree-$d$ invariant forms vanishing to
order $\ge m_4$ (resp.\ $\ge m_3$) at the quadruple (resp.\ triple) points.
Bauer et al.\ (Definition 4.10, Theorem 4.11) define

$$\mathrm{edim}\,T_d(-\!m_4E_4-\!m_3E_3)
  = \max\{\dim T_d - \mathrm{cond}_4(m_4) - \mathrm{cond}_3(m_3),\,0\},$$

where $\dim T_d = \#\{(a,b,c)\in\mathbf{N}^3 : 4a+6b+14c=d\}$ and
$\mathrm{cond}_n(m)=\#\{(i,j)\in\mathbf{N}^2 : 2i+nj\le m-1\}$ for $m\ge 1$,
$\mathrm{cond}_n(0)=0$, and prove actual dimension $\ge$ expected dimension.

## 2. Certified theorem

**Theorem.** Let $D=28H-2E_4-5E_3$ and $B=dH-m_4E_4-m_3E_3$ with integers
$d,m_4,m_3\ge 0$. If $D\cdot B = 28d-42m_4-140m_3 < 0$ and $d\le 2000$, then

$$\mathrm{edim}\,T_d(-m_4E_4-m_3E_3) = 0,$$

i.e.\ $\dim T_d - \mathrm{cond}_4(m_4) - \mathrm{cond}_3(m_3) \le 0$.
In particular, within degree $\le 2000$ the representation-theoretic
expected-dimension count **never** produces an invariant curve class meeting
$D$ negatively.

**Corollary (D-orthogonal census, same certificate).** There is no class
$B=dH-m_4E_4-m_3E_3$ with $d\le 2000$, $D\cdot B = 0$, $B^2<0$, and
$\mathrm{edim}>0$.

## 3. Proof (reduction verified by the replay script)

Fix $d$. By the general monotonicity lemma
($\mathrm{cond}_n(m+1)\ge\mathrm{cond}_n(m)$ for all $m\ge 0$ and every $n$,
since $\{(i,j):2i+nj\le m-1\}\subset\{(i,j):2i+nj\le m\}$), the raw expected
dimension $\dim T_d-\mathrm{cond}_4(m_4)-\mathrm{cond}_3(m_3)$
is nonincreasing in each of $m_4,m_3$, including the unbounded tails; the
script additionally checks monotonicity explicitly over the used ranges
($\mathrm{cond}_4$ on $0,\dots,500$, covering $\max M(d)=437$;
$\mathrm{cond}_3$ on $0,\dots,1200$).
Hence for fixed $(d,m_4)$ it suffices to test the *smallest* $m_3\ge 0$ with
$28d-42m_4-140m_3<0$ (this $m_{3,\min}$ is computed in closed form).
For the $m_4$-tail, let $M(d)$ be the least $M$ with $\mathrm{cond}_4(M)\ge\dim T_d$
(computed exactly); for every $m_4\ge M(d)$ and every $m_3$,
raw edim $\le \dim T_d-\mathrm{cond}_4(m_4)\le 0$. So looping
$m_4=0,\dots,M(d)$ with $m_3=m_{3,\min}(d,m_4)$ covers **all**
$(m_4,m_3)$ with $D\cdot B<0$. The script performs this finite exact-integer
check for every $d=0,\dots,2000$ ($221{,}019$ inner triples total;
$\max M(d)=437$) and finds zero counterexamples. The orthogonal census loops
$m_4=0,\dots,1334$, $m_3=0,\dots,400$: since $D\cdot B=0\iff 2d=3m_4+10m_3$,
$d\le 2000$ forces $3m_4+10m_3\le 4000$ (hence $m_4\le 1333$, $m_3\le 400$),
so this visits **every** $D$-orthogonal class with $d\le 2000$.

## 4. Replay

```
python3 output/artifacts/verify.py
```

Stdlib only, exact integer arithmetic (no floating point, no solvers).
Expected terminal output:

```
counterexamples (must be []): [] count = 0
cond monotonicity OK over used ranges
D-orthogonal negative edim>0 count: 0
VERIFY_EMERGENT_OK
```

## 5. Why this matters for the target

Lemma 4.1 of Bauer et al.\ reduces $D$-nefness to $G_{\mathcal{K}}$-irreducible
negative curves. The Theorem eliminates, in one stroke and up to degree $2000$,
every *expected* (edim $>0$) invariant obstruction to $D$-nefness. Consequently
any hypothetical counterexample to Conjecture 5.8 of degree $\le 2000$ must be a
Wiman-type *unexpected* curve (effective despite edim $0$, as the
$90H-4E_4-8E_3$ Wiman curve with edim $0$). This is a precise, citable
redirection of all future work on the Klein gap: the stabilizer
expected-dimension heuristic can never refute $D$; only global-dependence
phenomena can.

## 6. Supporting exact evidence (not part of the claimed theorem)

* `output/artifacts/exact_triple.py` (exact arithmetic over $\mathbf{Q}$ with
  $\Phi_4=x^3y+y^3z+z^3x$, $\Phi_6=xy^5+yz^5+zx^5-5x^2y^2z^2$,
  $\Phi_{14}=\mathrm{BH}(\Phi_4,\Phi_6)/9$): at $q=[1\!:\!1\!:\!1]$
  $(\Phi_4,\Phi_6,\Phi_{14})=(3,-2,-48)$; exact Taylor ranks give
  actual $=$ edim in all tested $m_4=0$ cases, e.g.\ $(42,(0,8))$ has
  $\dim T=9$, rank $8$, actual $1=$ edim $1$ (recovering the known
  $42H-8E_3$ curve at triple points). Shows the invariant-series machinery
  is tight on this slice.
* `output/artifacts/klein_cell.py` (numeric, NumPy): rebuilds the Klein cell
  from the $\mathrm{PSL}(2,7)$ representation (paper §2.2) — $21$ lines,
  $49$ singular points ($21$ quadruple $+$ $28$ triple), $4+4$ per line —
  and replays Proposition 3.1 ($\dim|D_k|=7k+6$, hence $\widehat\alpha\le 6.5$).
  Numerical evidence only, kept for object-fixing provenance.

## 7. Limitations (explicit)

* The Theorem constrains only the **expected** dimension. Since actual
  dimension $\ge$ edim (Theorem 4.11), it does **not** prove $D$ nef, does not
  bound $\widehat\alpha(I_{\mathcal{K}})$, and does not close wh $=13/2$.
* The certificate covers $d\le 2000$ only. Spot checks along the critical ray
  $(d,m_4,m_3)=(28t-2,2t,5t)$ (where $D\cdot B<0$ minimally) show the deficit
  $\dim T_d-\mathrm{cond}_4-\mathrm{cond}_3=-t/2$ grows linearly negative
  (checked to $t=5000$), suggesting an all-degree analytic extension, but that
  extension is **not** claimed here.
* Full $D$-nefness (target) and $D_{14}$-nefness (preset fallback) both remain
  open: they require classifying $G_{\mathcal{K}}$-irreducible negative curves
  (to degree $394$ for $D_{14}$), far beyond the paper's degree-$200$ list.

## 8. Originality

Bauer et al.\ supply the edim formula, verify an SHGH-type conjecture for
$d<144$, and classify negative curves to degree $200$, but never state or test
the $D\cdot B<0\Rightarrow\mathrm{edim}=0$ vanishing. No inspected source
(Bauer et al., Calvo–Huizenga–Szemberg July 2025, Nguyen, Szpond survey)
records it. It is a new, proved, machine-checkable structural fact about the
Klein invariant ring, discovered by exhaustively hunting for edim-level
obstructions to the target divisor.
