# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A verified augmentation-variety and torus-obstruction fragment for twist knots,
  with delimited non-transfer to max-tb 8_1

## 0. What is proved here vs cited vs open

- **Verified by machine in-lane** (script
  `output/artifacts/verify_aug_twist.py`, ALL_PASS): the symbolic reduction of the
  twist-knot DGA equations to the single relation $(ab+1)c=1$ (including the $n=3$
  extra term); the separability/Bezout identities and Laurent-unit facts used inside
  the torus non-embedding argument; brute-force point counts $|V(\mathbf F_q)|=q^2-q+1$
  for $q=2,3,5,7$; augmentation-point membership; Sabloff/Euler dimension arithmetic.
- **Cited human-checked proof** (Gao–Rutherford arXiv:2103.03951, Props 4.1/4.3,
  Cor 4.4): the geometric assembly — the projection is an algebraic isomorphism, and
  the UFD/finiteness completion of the non-embedding proof. Not re-proved by machine.
- **Not proved (open)**: the admitted target — a graded cluster-chart distinction of
  two orientable fillings of max-tb $8_1$ — and its transfer from the odd-twist family
  $\Lambda_n$ to the even-twist knot $8_1$. No front/DGA/pinch computation for $8_1$
  is offered. No cluster seed/mutation log is offered.

## 1. Setup (cited)

Let $\Lambda_n$, $n=2k+1\ge 3$ odd, be the max-tb Legendrian twist knots of Figure 1 in
Gao–Rutherford. Degree-0 chords: $a,b,c_1,\dots,c_n$; degree-1 chords: $e_0,\dots,e_n$.
With the sign convention of [34, §2.1] the differentials are (GR (4.1)–(4.5)):

$$\partial e_0 = t^{-1}+c_n(1+ab),$$
$$\partial e_1 = 1+(1+ba)(-c_1)+\begin{cases}(-b)(1+c_2c_3) & n=3\\ 0 & n>3\end{cases}$$
$$\partial e_j = 1+c_{j-1}c_j\ (2\le j\le k+1),\qquad
  \partial e_j = 1+c_jc_{j-1}\ (k+2\le j\le n).$$

All chords have degree 0 or 1, so every even-graded augmentation is 0-graded; the
$m$-graded and ungraded varieties coincide. $tb(\Lambda_n)=1$.

## 2. Verified proposition A — the augmentation variety

**Proposition A (replay of GR Prop 4.1, machine-checked reduction).**
For odd $n\ge 3$ and any field $\mathbf F$,
$$\mathrm{Aug}(\Lambda_n,\mathbf F)\cong V:=\{(a,b)\in\mathbf F^2\mid ab\ne-1\}
  \cong \{(a,b,c)\in\mathbf F^3\mid (ab+1)c=1\}$$
via $(a,b,c_1,\dots,c_n,t)\mapsto(a,b,c_1)$ with inverse
$c_j=c$ ($j$ odd), $c_j=-(ab+1)$ ($j$ even), $t=-1$.

*Proof status.* The map and inverse are due to GR. The in-lane contribution is the
symbolic verification: substituting the $c_j$ pattern, each $\partial e_j$ ($2\le j\le 8$
checked explicitly, pattern general) equals $1-(ab+1)c$; $\partial e_0|_{t=-1}=-1+(ab+1)c$;
$\partial e_1$ ($n>3$) equals $1-(ab+1)c$; the $n=3$ factor $1+c_2c_3$ likewise equals
$1-(ab+1)c$; spot evaluation at $(a,b,c)=(2,3,1/7)$ kills all equations. Script §A. ∎

Consequences checked in-lane: $\varepsilon_1=(0,1)$, $\varepsilon_2=(1,0)$,
$\varepsilon_3=(0,0)$ all lie in $V$ (so $\varepsilon_3$'s non-fillability is a toric
neighbourhood phenomenon, not absence from $V$); $|V(\mathbf F_q)|=q^2-q+1$ verified for
$q=2,3,5,7$ (3, 7, 21, 43); Euler arithmetic $\dim LCH_1=1$, $\dim LCH_0=2$,
$\chi=2-1=1=tb$; $H^*\mathrm{Hom}_+(\varepsilon,\varepsilon)$ has dimensions $(1,2)$,
matching a punctured torus. Script §C–D.

## 3. Verified proposition B — torus-obstruction computations

**Proposition B (computational core of GR Prop 4.3, machine-checked).**
Let $k=\bar{\mathbf F}$ and $V=\{(a,b,c):(ab+1)c=1\}$. If
$\phi:(k^*)^2\to V$ is algebraic with $\phi(s_0,t_0)=(0,0)$, write
$A=\phi^*a$, $B=\phi^*b$. Then:
(i) $AB+1=\alpha s^mt^n$ for some $\alpha\in k^*$, $m,n\in\mathbf Z$;
(ii) in characteristic 0, $(\alpha t_0^n)s^m-1$ is separable for every $m\ge 1$
($\gcd=1$ with explicit Bezout identity $-g+(s/m)g'=1$);
(iii) the $m=n=0$ case forces a non-injective map (demo $\phi(s,t)=(0,s)$ collides on
$\mathbf F_5^*$);
(iv) worked char-3 example $\gcd(2s^2-1,s)=1$ in $\mathbf F_3[s]$.

*Proof status.* (i) is the standard Laurent-unit description, cited. (ii)–(iv) are
verified symbolically in-lane (script §B: char-0 gcd+Bezout for $m=1,2,3,5$; GF(3)
example; unit demo $(s-1)\cdot1+1=s$; $\mathbf F_5$ collision). The remaining assembly
(clearing denominators to $\tilde A\tilde B=\alpha s^mt^n-1$ in $k[s,t]$, UFD
factorisation, common-zero finiteness forcing a contradiction) is the cited
human-checked argument of GR Prop 4.3 and is NOT machine-proved here. ∎

**Corollary (cited, GR Cor 4.4).** No orientable Lagrangian filling (with any rank-1
local system) induces the augmentation with $\varepsilon(a)=\varepsilon(b)=0$ on
$\Lambda_n$. Follows from Prop B's completion plus Prop 2.6 (filling induces an
injective torus $(k^*)^2\hookrightarrow V$ through $(0,0)$ since $tb=1$ forces genus 1).

## 4. Relation to the $8_1$ target (honest gap)

The admitted target concerns the **even**-twist knot $8_1$: two orientable fillings
$L,L'$ with identical classical invariants separated by a graded cluster-chart
function $X(\varepsilon_L)\ne X(\varepsilon_{L'})$. This report does **not** achieve it:
- no max-tb front, grading, or DGA for $8_1$ is computed;
- no two pinch-move fillings or induced augmentations for $8_1$ are constructed;
- no cluster seed, mutation log, or separating function $X$ is produced;
- the $c_j$-pattern/$\partial e_1$ computation above is specific to the odd family
  $\Lambda_n$ and does not transfer without the Etnyre–Ng–Vértesi classification
  analysis for the even case (cf. GR §4.3, which treats only odd-crossing negatives).

Hence the $8_1$ pair-separation remains open. What survives as fallback value (per the
admission fallback axis): a replayable graded-variety equation set plus the verified
computational core of a certified torus obstruction, packaged as a reusable template
for the neighbouring even-twist computation, with the transfer point precisely marked.

## 5. Reproduction

Run `python3 output/artifacts/verify_aug_twist.py` (requires only sympy; tested with
sympy 1.12). Expected: every line PASS, final ALL_PASS, exit 0.

## References

- H. Gao, D. Rutherford, Non-fillable augmentations of twist knots, arXiv:2103.03951.
- O. Capovilla-Searle, J. Hughes, D. Weng, Augmentations, Fillings, and Clusters for
  2-Bridge Links, arXiv:2308.11858 (ungraded/non-orientable context; why the graded
  orientable $8_1$ distinction is not implied).
- H. Gao, L. Shen, D. Weng, Augmentations, Fillings, and Clusters, arXiv:2008.10793.
- R. Casals et al., A Lagrangian filling for every cluster seed, arXiv:2308.00043.
- J. Etnyre, L. Ng, V. Vértesi, Legendrian and transverse twist knots, JEMS 15 (2013).
