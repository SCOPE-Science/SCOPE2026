# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — The l^{1/2} translation equivalence is not Borel reducible to E1

## 1. Statement

Let $X=\mathbf R^{\mathbf N}$ with product Polish topology and
$G=\ell^{1/2}=\{g\in\mathbf R^{\mathbf N}:\|g\|:=\sum_n|g_n|^{1/2}<\infty\}$,
acting by translation. Let $E_{1/2}$ be the orbit equivalence:
$x\,E_{1/2}\,y\iff x-y\in G\iff\sum_n|x_n-y_n|^{1/2}<\infty$.
Let $E_1$ on $(2^{\mathbf N})^{\mathbf N}$ be eventual equality.

**Theorem (TARGET).** $E_{1/2}\not\le_B E_1$: there is no Borel map
$f:\mathbf R^{\mathbf N}\to(2^{\mathbf N})^{\mathbf N}$ with
$x\,E_{1/2}\,y\iff f(x)\,E_1\,f(y)$.
In particular no Borel reduction exists.

Proof is via turbulence verification (Lemmas 1–3) plus the Kanovei generic-turbulence vs $E_1$ black box.

## 2. Polish setup

**Lemma 1.** $G$ with $d(g,h)=\sum_n|g_n-h_n|^{1/2}$ is a Polish abelian group;
translation on $X$ is a continuous Polish $G$-space.

*Proof.* $d$ is a finite translation-invariant metric on $G$ (finite since
$g,h\in G$ implies $|g_n-h_n|^{1/2}\le |g_n|^{1/2}+|h_n|^{1/2}$ summable).
Separability via rational finitely supported sequences. Completeness:
$d$-Cauchy implies coordinatewise Cauchy; let $g^{(j)}\to g$ coordinatewise;
for fixed $N$, $\sum_{n\le N}|g_n|^{1/2}\le\liminf_j\|g^{(j)}\|<\infty$,
so $g\in G$, and $d(g^{(j)},g)\to0$ by splitting finite head plus uniform
small tail of Cauchy sequence (standard $\ell^p$, $p<1$ argument).
Addition continuous. Action $(g,x)\mapsto g+x$ continuous from
$G\times X\to X$ since coordinatewise continuous. ∎

**Lemma 2.** Every $E_{1/2}$-class is dense and meagre in $X$.

*Proof.* $c_{00}\subset G$, so $x+G\supset x+c_{00}$ dense in product topology.
$G=\bigcup_{k}F_k$, $F_k=\{g:\|g\|\le k\}$. Each $F_k$ is closed in $X$:
coordinatewise limit preserves $\sum_{n\le N}|\cdot|^{1/2}\le k$ for all $N$.
Each $F_k$ nowhere dense: any basic cylinder constraining finitely many
coordinates is escaped by a large spike in a free coordinate. So $G$ meagre
$F_\sigma$; translates (orbits) meagre. ∎

## 3. Turbulence

Recall: for $x\in X$, open $U\ni x$, neighbourhood $V$ of $0$,
$O(x,U,V)=\{y:\exists m, x=x_0,\dots,x_m=y\in U,
x_{i+1}-x_i\in V\cap G\}$.
$x$ is turbulent if $O(x,U,V)$ is somewhere dense (closure has nonempty
interior) for all such $U,V$.

**Lemma 3.** Every $x\in X$ is turbulent.

*Proof.* Let $U$ basic: $|y_i-x_i|<\varepsilon$, $i<N$; $V=\{g:\|g\|<\delta\}$.
Shrink to convex $U_0=\{y\in U:|y_i-x_i|<\varepsilon/2,i<N\}\ni x$.
We show $O(x,U_0,V)\supset U_0\cap(x+c_{00})$, dense in $U_0$.
Let $z\in U_0\cap(x+c_{00})$, $d=z-x$ finitely supported with
$\|d\|<\infty$. Segment $x+td$, $t\in[0,1]$, lies in convex $U_0$.
Steps $d/m$ satisfy $\|d/m\|=m^{-1/2}\|d\|\to0$ (key $p=1/2$ scaling),
so for large $m$, $\|d/m\|<\delta$ and chain
$x,x+d/m,\dots,x+d=z$ stays in $U_0$. Hence $z\in O(x,U_0,V)$.
Since $U_0\cap(x+c_{00})$ dense in $U_0$, closure of $O(x,U,V)\supset O(x,U_0,V)$
contains $U_0$. ∎

Hence with Lemma 2 the action is turbulent (dense meagre orbits, every point
turbulent).

## 4. Kanovei–Reeken black box and conclusion

**Black box (Kanovei–Reeken 2003).** Let Class 1 be orbit equivalence
relations of generically turbulent Polish actions, and Class 4 the least
class containing equalities $D(S)$ on Polish spaces and closed under
countable union/intersection/disjoint union on a fixed space, product,
Fubini product $\prod_k F_k/\mathrm{Fin}$ modulo finite sets, and countable
power $F^\infty$ (definitions in Kanovei–Reeken §1.2). Then no ER in
Class 1 is Borel reducible — indeed, not reducible even by a
Baire-measurable map — to any ER in Class 4.
Reference: V. Kanovei, M. Reeken, "Some new results on Borel irreducibility
of equivalence relations", *Izvestiya: Mathematics* 67(1):55–76 (2003),
arXiv:math/0203102 — Theorem 1 stated in the Introduction and proved as
Theorem 6 (§2.1) via hereditary generic $F$-ergodicity for every
$F$ in Class 4.

*Background only.* Hjorth's earlier turbulence theorem (generically
turbulent ERs are not classifiable by countable structures, i.e. not Borel
reducible to orbit ERs of Polish $S_\infty$-actions; see Hjorth,
*Classification and Orbit Equivalence Relations*, AMS 2000, and exposition
in Gao, *Invariant Descriptive Set Theory*, CRC 2009, Ch. 8) is the
$S_\infty$ precursor that Kanovei–Reeken §3 derives from the above box;
it is not used as the operative black box here.

**$E_1$ lies in Class 4.** $E_1$ on $(2^{\mathbf N})^{\mathbf N}$ is exactly
the Fubini product $\prod_k D(2^{\mathbf N})/\mathrm{Fin}$:
$(a_k)\,E_1\,(b_k)\iff\{k:a_k\ne b_k\}$ is finite. Each $D(2^{\mathbf N})$
is an equality on a Polish space, and the Fubini product mod Fin is one
of the defining closure operations of Class 4, so $E_1\in$ Class 4
(cf. Kanovei–Reeken §1.2–1.3, where $E_0$ and $E_3$ are noted as Class 4
members by the same construction).

**Application.** By Lemma 2 every $E_{1/2}$-orbit is dense and meagre, and
by Lemma 3 every point is turbulent; hence the action is generically
turbulent (indeed everywhere turbulent with dense orbits), so $E_{1/2}$
is in Class 1. Since $E_1$ is in Class 4, the black box gives directly
that $E_{1/2}$ is not Borel reducible (indeed, not Baire-measurably
reducible) to $E_1$. No comeagre-collapse claim for arbitrary homomorphisms
is made or needed; non-reducibility follows from turbulence plus the absence
of a comeagre class (Lemma 2) through the cited theorem. ∎

## 5. Separation of proof / citation / uncertainty

- Proved self-contained: Lemmas 1–3 (Polish setup, dense meagre orbits,
turbulence at every point) and the verification $E_1\in$ Class 4.
- Cited black box: Kanovei–Reeken 2003 irreducibility theorem stated above
(Izvestiya 67:55–76, arXiv:math/0203102, Thm 1/Thm 6), not reproved here.
Hjorth/Gao cited only for $S_\infty$ background, not as the operative box.
- No computation; no conjecture. Negative resolution is complete modulo the
cited theorem whose reference is given exactly.
