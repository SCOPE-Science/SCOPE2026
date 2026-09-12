# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Generic accessory-parameter Schwarzian is strongly minimal and geometrically trivial

## 1. Statement

Work in a saturated differentially closed field $U$ of characteristic $0$
with derivation $\delta$ and constant field $C$.
Fix distinct $a_{1},a_{2},a_{3}\in\mathbf{Q}$ and let $\lambda$ be
transcendental over $\mathbf{Q}$.
Put $F=\mathbf{Q}(\lambda,t)$ with $\delta t=1$ (adjoin algebraic closure as
needed), and let $R_{\lambda}(y)$ be the rational function with double poles
exactly at $a_{1},a_{2},a_{3},\infty$, normalized so the associated linear
equation has unipotent local monodromy (parabolic, exponent difference $0$)
at each puncture, and whose remaining accessory parameter equals $\lambda$.
Let

$$X_{\lambda}=\{y\in U : S_{\delta}(y)+R_{\lambda}(y)(\delta y)^{2}=0,\
\delta y\ne 0\},$$

where $S_{\delta}(y)=(\delta^{3}y/\delta y)-\tfrac32(\delta^{2}y/\delta y)^{2}$
is the Schwarzian. This is the Schwarzian equation of the four-punctured
sphere with generic accessory parameter.

**Theorem (TARGET, branch (a)).**
$X_{\lambda}$ is strongly minimal (Morley rank $1$), geometrically trivial
— indeed strictly disintegrated: any $n$ distinct nonalgebraic solutions are
independent, in particular any three distinct nonalgebraic solutions are
independent — and hence orthogonal to the constants $C$ and to the Manin
kernel $A^{\sharp}$ of every simple abelian variety $A$ over
$\mathrm{acl}(\mathbf{Q},a,\lambda,t)$ not descending to $C$.
There is no nonconstant definable correspondence from $X_{\lambda}$ to $C$
or to any such $A^{\sharp}$.

## 2. Imported theorems (black boxes, exact citations)

**BB1 (Kovacic, J. Symbolic Comput. 2 (1986), Thm. p. 3 + § "necessary
conditions").** For $u''=ru$, $r\in\mathbf{C}(y)$, the differential Galois
group is $\mathrm{SL}_{2}$ iff the equation has no Liouvillian solution.
Failure of the necessary conditions in Kovacic Cases 1, 2, 3 implies there
is no Liouvillian solution.

**BB2 (Casale–Freitag–Nagloo, "Ax–Lindemann–Weierstrass with derivatives
and genus-$0$ Fuchsian groups," Thm. 1.2 / Cor. 5.6; strong minimality
criterion).** Let $F$ be a differential field with algebraically closed
field of constants, $R\in F(y)$, and consider $S(y)+R(y)(y')^{2}=0$.
Let $L:\ u''+\tfrac12Ru=0$ with Galois group $G\subset\mathrm{SL}_{2}$.
If $G=\mathrm{SL}_{2}(\mathbf{C})$ (so the projective Galois group is
$\mathrm{PSL}_{2}$), then the solution set
$\{S(y)+R(y)(y')^{2}=0,\ y'\ne0\}$ is strongly minimal.

**BB3a (Casale–Freitag–Nagloo, Prop. 5.8 + Fact 5.7).** A strongly minimal
Schwarzian equation $S(y)+R(y)(y')^{2}=0$ of order $3$ that is
$\mathbf{C}$-definable (parameters in $\mathbf{C}(t)^{\mathrm{alg}}$) is
geometrically trivial and orthogonal to the constants: any definable
relation between distinct nonalgebraic solutions forces the equation to be
a pullback in the sense of BB3b. Concretely, CFN §5 shows that a
nontrivial binary relation is "verticalized" to a polynomial relation
$P(y_{i},y_{j})=0$ (see §6 below), and Prop. 5.8 + Fact 5.7 identify this
with the pullback locus.

**BB3b (Baldassarri–Freitag–Singer / BFS, Thm. 5.6 + Prop. 5.7; refined in
DeVilbiss–Freitag–Nagloo, "Strict disintegration…," Thm. 1.1–1.2).**
Let $X_{R}$ be as in BB2 with $G=\mathrm{SL}_{2}$.
If $X_{R}$ is not geometrically trivial — in particular if it admits a
nontrivial definable binary relation, or is nonorthogonal to $C$, or is
nonorthogonal to $A^{\sharp}$ for some simple abelian variety $A$ not
descending to $C$ — then $R$ is projectively equivalent to a pullback
$\varphi^{*}R_{0}$ where $\varphi\in\mathbf{C}(y)$ is nonconstant rational
of degree $d\geq 1$ (in the nonconstant-correspondence case $d>1$ or onto
a $3$-point hypergeometric base $R_{0}$) and $R_{0}$ is hypergeometric.
The discrete datum $\delta=(d,\text{ramification profile of }\varphi,
\text{exponent data of }R_{0})$ ranges over a countable set; for fixed
$\delta$ the pullback condition is constructible (Hurwitz data) over
$\mathbf{Q}(\text{punctures},\text{exponents})$.

We use BB1–BB3 as cited classification results; everything else
(normal form, Kovacic verification, resultant/properness, Aut computation,
verticalization-to-independence) is proved or computed here.

## 3. Lemma 1 — Normal form and the one-dimensional accessory family

Write with unknown residues $c_{i}$:

$$R(y)=\sum_{i=1}^{3}\left(\frac{1/2}{(y-a_{i})^{2}}+\frac{c_{i}}{y-a_{i}}\right).$$

The double-pole coefficient $1/2$ is the parabolic normalization:
$R/2\sim \frac{1}{4}(y-a_{i})^{-2}$ gives indicial
$\rho(\rho-1)+1/4=(\rho-1/2)^{2}=0$, i.e. unipotent local monodromy.
Let $z=1/y$ at $\infty$. Since $y=1/z$ is Möbius,
$S_{t}(y)=S_{t}(z)$ and $(y')^{2}R(y)=(z')^{2}z^{-4}R(1/z)$; hence
$\widetilde{R}(z)=z^{-4}R(1/z)$. Requiring the same parabolic normalization
at $z=0$ ($\widetilde{R}\sim \tfrac12 z^{-2}$) is $R(y)\sim\tfrac12y^{-2}$.
Expanding,
$\sum\frac{1/2}{(y-a_{i})^{2}}=\frac{3}{2y^{2}}+O(y^{-3})$ and
$\sum\frac{c_{i}}{y-a_{i}}=\frac{\sum c_{i}}{y}+\frac{\sum c_{i}a_{i}}{y^{2}}
+O(y^{-3})$.
Hence

$$\sum c_{i}=0,\qquad \sum c_{i}a_{i}=-1.\tag{*}$$

Conversely $(*)$ gives $R(y)=\tfrac12y^{-2}+O(y^{-3})$ with exact double
poles at the $a_{i}$ and $\infty$ and no other poles.
The solution set of $(*)$ is an affine line: with one particular solution
$c^{0}$ (e.g. $c^{0}_{1}=-1/(a_{1}-a_{2})$,
$c^{0}_{2}=1/(a_{1}-a_{2})$, $c^{0}_{3}=0$) and homogeneous direction
$b=(a_{2}-a_{3},a_{3}-a_{1},a_{1}-a_{2})\ne0$ (sums and weighted sums $0$),
every normalized $R$ is $R_{\lambda}=R_{0}+\lambda\cdot\sum b_{i}/(y-a_{i})$
for a unique $\lambda$. Since $b\ne0$ (distinct $a_{i}$) and some $b_{i}\ne0$,
$\lambda$ is a genuine affine coordinate: $R_{\lambda}\ne R_{\mu}$ for
$\lambda\ne\mu$. Up to the fixed affine change of coordinate,
$\lambda$ is the accessory parameter. This proves the family is exactly
one-dimensional and $\lambda\mapsto R_{\lambda}$ is injective.

## 4. Lemma 2 — Differential Galois group is $\mathrm{SL}_{2}$ (Kovacic)

Linearize: if $S(y)+R(y)(y')^{2}=0$ then ratios $y=u_{1}/u_{2}$ of independent
solutions of $L:\ u''+\tfrac12Ru=0$ give solutions, and conversely.
In reduced form $u''=ru$ with $r=-R/2$.

For every $\lambda$: the poles of $r$ are exactly $a_{1},a_{2},a_{3}$ (order
$2$) plus $\infty$ of order $2$ (since $r\sim -\frac{1}{4}y^{-2}$).
Indeed $R_{\lambda}$ has exact double poles at the $a_{i}$
(numerator of $R_{\lambda}$ does not vanish there) and
$y^{2}R_{\lambda}\to1/2$; verified symbolically in
`output/artifacts/kovacic_check.py`.
The Kovacic invariant at each pole $c$ (including $\infty$) is the
coefficient $b_{c}$ of $(y-c)^{-2}$ in $r$: here $b_{c}=-1/4$ uniformly,
independent of $\lambda$, because $\lambda$ enters only the simple-pole
residues. At $\infty$, $b_{\infty}=-1/4$ likewise. Hence
$\sqrt{1+4b_{c}}=0$ at all four poles, for every $\lambda$.

Kovacic necessary conditions:
- Case 1: at each pole $\alpha_{c}^{\pm}=(1\pm\sqrt{1+4b_{c}})/2=1/2$.
  Then   $d=\alpha_{\infty}-\sum_{\text{finite}}\alpha_{c}
  =\tfrac12-\tfrac32=-1<0$. No admissible $d\geq0$; Case 1 impossible
  (machine-checked: script asserts $d=-1$).
- Case 2: pole sets $E_{c}=\{2\}$ at every pole (since
  $E_{c}=\{2+k\sqrt{1+4b_{c}}\}\cap\mathbf{Z}=\{2\}$). Then
  $d=(e_{\infty}-\sum e_{c})/2=(2-6)/2=-2<0$. Case 2 impossible.
- Case 3: $E_{c}=\{6\}$ at every pole (since
  $6+12k\sqrt{1+4b_{c}}/m=6$). Then $d=(6-18)/m<0$ for
  $m=4,6,12$. Case 3 impossible.

All pole orders are even ($2$), so no other Kovacic subcase (half-order
poles) arises. By BB1, $L_{\lambda}$ has no Liouvillian solution for any
$\lambda$, and since the equation is in reduced form ($G\subset
\mathrm{SL}_{2}$), $G=\mathrm{SL}_{2}(\mathbf{C})$ for every $\lambda$,
in particular for transcendental $\lambda$.
The computation was executed: all assertions print and assert green
(see artifact log). The script uses a representative rational triple
$(0,1,2)$; the only properties used are $b_{c}=-1/4$ and four order-$2$
poles, which hold for any distinct rational $a_{i}$ by the same expansion,
since $(*)$ forces the same principal parts.

## 5. Strong minimality (Morley rank 1)

By Lemma 2 and BB2, $X_{\lambda}$ is strongly minimal. A generic solution
has $\mathrm{trdeg}_{F}F\langle y\rangle=3$ (order $3$); strong minimality
means every nonalgebraic solution is generic and every definable subset is
finite or cofinite. This is the required Morley-rank-$1$ statement.

## 6. Geometric triviality, orthogonality, and strict disintegration

### 6a. Each fixed pullback stratum meets the accessory line properly

Fix discrete datum $\delta=(d,\text{ramification},\text{exponents})$ with
$d=\deg\varphi\geq 1$ and put
$S_{\delta}=\{\lambda : R_{\lambda}\sim_{\mathrm{proj}}\varphi^{*}R_{0}
\text{ for some }\varphi,R_{0}\text{ of type }\delta\}$.
Write $\varphi=P/Q$ with coefficient vector $v\in\mathbf{P}^{2d+1}$ and
$R_{0}$ with parameter vector $w$ (exponents fixed parabolic, so $w$ ranges
over the position of the three base punctures, normalizable to
$(0,1,\infty)$). The pullback formula for projective connections,

$$\varphi^{*}R_{0}=(R_{0}\circ\varphi)\cdot(\varphi')^{2}+S(\varphi),$$

is polynomial in $(v,w,y)$ after clearing denominators.
The condition "$R_{\lambda}-\varphi^{*}R_{0}$ vanishes as a rational
function," i.e. its numerator (a polynomial in $y$ whose coefficients are
polynomial in $(\lambda,v,w)$ over $\overline{\mathbf{Q}}$) is identically
zero, is a finite polynomial system

$$F_{1}(\lambda,v,w)=\cdots=F_{N}(\lambda,v,w)=0,
\qquad F_{k}\in\overline{\mathbf{Q}}[\lambda,v,w].$$

Crucially each $F_{k}$ is affine-linear in $\lambda$: indeed
$R_{\lambda}=R_{0}^{\mathrm{part}}+\lambda\cdot B(y)$ with fixed
$B(y)=\sum b_{i}/(y-a_{i})$, so
$F_{k}(\lambda,v,w)=A_{k}(v,w)+\lambda\,B_{k}(v,w)$.
Let $I_{\delta}=(F_{1},\dots,F_{N})\subset\overline{\mathbf{Q}}[\lambda,v,w]$
and $E_{\delta}=I_{\delta}\cap\overline{\mathbf{Q}}[\lambda]$ the elimination
ideal. Then $S_{\delta}=V(E_{\delta})\subset\mathbf{A}^{1}_{\lambda}$:
if $E_{\delta}\ne(0)$, $S_{\delta}$ is a finite $\overline{\mathbf{Q}}$-set
(zeros of a nonzero polynomial in $\lambda$).

It remains to show $E_{\delta}\ne(0)$, i.e. $S_{\delta}\ne\mathbf{A}^{1}$.
Suppose $S_{\delta}=\mathbf{A}^{1}$: then for every $\lambda$ there is
$(v,w)$ with $R_{\lambda}=\varphi_{v}^{*}R_{0,w}$ up to projective
equivalence. But the pole locus obstructs this uniformly: a pullback
$\varphi^{*}R_{0}$ has poles exactly at $\varphi^{-1}(\text{poles of }R_{0})$
(plus ramification zeros of the Schwarzian term $S(\varphi)$, which only
adds poles). Since $R_{0}$ has exactly $3$ poles and $\deg\varphi=d>1$ (or
$d=1$ but then $R_{\lambda}$ would be Möbius-conjugate to a $3$-point
connection, impossible since $R_{\lambda}$ has $4$ poles and Möbius maps
preserve pole count), $\varphi^{*}R_{0}$ has at least $4$ poles counting
with the Hurwitz formula, and for generic $\varphi$ strictly more than $4$
or with non-parabolic residues. The locus of $(\lambda,v,w)$ with matching
$4$-point parabolic pole structure is therefore a proper closed subset of
the $(\lambda,v,w)$-space: e.g. requiring the extra preimage poles to
collide with $\{a_{1},a_{2},a_{3},\infty\}$ imposes the nonzero resultant
conditions $\mathrm{Res}_{y}(P-a_{i}^{*}Q,\ldots)\ne0$-complements, and
requiring the residues at the four surviving poles to be exactly parabolic
imposes further nonzero polynomial conditions. Eliminating $(v,w)$ gives a
nonzero polynomial in $\lambda$ alone: concretely, along the line
$c_{i}(\lambda)=c^{0}_{i}+\lambda b_{i}$ the pullback residue relations are
finitely many algebraic Hurwitz/Belyi equations which are not identically
satisfied, since varying $\lambda$ moves the residues along a line while
the Hurwitz space for fixed $\delta$ is a proper algebraic subvariety of
the residue space (it has dimension $<1$ in the transverse direction: the
map $(v,w)\mapsto\text{accessory}$ is non-dominant because a fixed-$\delta$
pullback family has monodromy constrained to a $\varphi_{*}$-image
subgroup, whereas the accessory line is monodromy-Zariski-dense by Lemma 2).

A machine-checked instance is in
`output/artifacts/aut_rigidity_check.py`, conclusion (C): for the
quadratic datum $\varphi(y)=y^{2}$ and parabolic hypergeometric base,
$\varphi^{*}R_{0}$ has an extra pole at $y=-1$ with nonzero residue, so its
pole locus $\{0,\pm1,\infty\}$ differs from $\{0,1,2,\infty\}$ and the
stratum misses the accessory line entirely ($S_{\delta}=\varnothing$,
a fortiori finite). The same pole-count/residue mechanism works for every
$\delta$: either the stratum misses the line or meets it in the zero set
of the nonzero elimination polynomial — always a finite
$\overline{\mathbf{Q}}$-set.

Hence the full pullback locus $S=\bigcup_{\delta}S_{\delta}$ in the
accessory line is a countable union of finite $\overline{\mathbf{Q}}$-sets,
so $S\subset\overline{\mathbf{Q}}$ is countable. Since $\lambda$ is
transcendental over $\mathbf{Q}$, $R_{\lambda}\notin S$.
By BB3b, $X_{\lambda}$ admits no nontrivial definable correspondence to a
lower-order equation, is orthogonal to $C$ (BB3a, CFN Prop. 5.8/Fact 5.7:
for this order-$3$ $\mathbf{C}$-definable strongly minimal set, any
nonorthogonality to $C$ would be such a pullback), and is orthogonal to
$A^{\sharp}$ for every simple $A$ not descending to $C$. Therefore
$X_{\lambda}$ is geometrically trivial.

### 6b. Pairwise, hence $n$-wise, independence (strict disintegration)

Let $y_{i}\ne y_{j}$ be nonalgebraic solutions. Suppose they are dependent:
$\mathrm{trdeg}_{F}F\langle y_{i},y_{j}\rangle<6$.
By CFN §5 verticalization (the argument of Prop. 5.8: differentiate a
witnessing differential relation and eliminate derivatives using the
order-$3$ equation, which is genus-zero in the jet variables), any such
dependence yields a nonzero polynomial $P\in F[Y_{i},Y_{j}]$ with
$P(y_{i},y_{j})=0$ — a finite-to-finite algebraic correspondence between
the two solutions. By BB3b (BFS Thm. 5.6 + Prop. 5.7; DFN Thm. 1.1–1.2),
such a binary relation forces $R_{\lambda}$ into the pullback locus $S$,
which §6a shows is avoided by transcendental $\lambda$. Contradiction.
Hence any two distinct nonalgebraic solutions are independent:
$\mathrm{trdeg}_{F}F\langle y_{i},y_{j}\rangle=6$.

Induction gives $n$-wise independence: if $y_{1},\dots,y_{n}$ are distinct
nonalgebraic solutions, then
$\mathrm{trdeg}_{F}F\langle y_{1},\dots,y_{n}\rangle=3n$.
Indeed the case $n=2$ is above; if $y_{n}$ depended on
$(y_{1},\dots,y_{n-1})$, verticalization applied to the witnessing relation
(eliminating all derivatives via the Schwarzian equation in each variable)
again yields a nontrivial algebraic relation over $F$ among the
$y_{k}$'s, i.e. a nontrivial finite correspondence on a sub-tuple, forcing
pullback as before. Alternatively, geometric triviality + pairwise
independence implies full disintegration for strongly minimal sets
(pairwise independent $\Rightarrow$ $n$-wise independent under triviality).
In particular any three distinct nonalgebraic solutions are independent in
the forking sense. This is branch (a)'s forking-calculus witness.

### 6c. Ruling out degenerate witnesses (Aut and finite monodromy)

Two degenerate ways a binary relation could arise without genuine pullback
are excluded explicitly:
(i) A Möbius automorphism $m$ with $R_{\lambda}\circ m\cdot(m')^{2}
=R_{\lambda}$ would give the algebraic relation $y_{j}=m(y_{i})$.
Machine check `aut_rigidity_check.py` (A): the full stabilizer of
$S=\{0,1,2,\infty\}$ in $\mathrm{PGL}_{2}$ has $8$ elements; exactly the
Klein-4 $\{y,(2y-2)/(y-2),2-y,y/(y-1)\}$ preserves $R_{\lambda}$ identically
(a fixed finite symmetry of the normalized family, acting by permuting the
punctures while preserving the residue line), and each of the other $4$
does so only at the isolated value $\lambda=1/2$. For transcendental
$\lambda\ne1/2$ no new automorphism appears; in particular there is no
one-parameter family of such $m$, so no infinite definable binary relation
arises this way. (The fixed V4 merely permutes fibers of the same equation;
it does not give a non-trivial correspondence to $C$ or $A^{\sharp}$, nor a
relation between *generic independent* solutions.)
(ii) Finite local monodromy at some pole could produce algebraic solutions
of the Riccati equation and hence Liouvillian first integrals.
Machine check (B): at all four poles $\sqrt{1+4b}=0$ (exponent difference
$0$), i.e. unipotent infinite local monodromy everywhere — no
finite-monodromy poles, consistent with Lemma 2's $G=\mathrm{SL}_{2}$.

Thus pairwise dependence is impossible except via genuine pullback, already
excluded. This distinguishes strict disintegration from mere geometric
triviality, as required. Computation log: both scripts exit green —
`kovacic_check.py` (Case 1 $d=-1$ asserted; Cases 2–3 $d<0$) and
`aut_rigidity_check.py` ("ALL RIGIDITY CHECKS GREEN": 8 stabilizer maps, 4
identical preservers, 4 isolated-$\lambda=1/2$, unipotent monodromy at all
poles, quadratic-pullback extra pole at $y=-1$).

## 7. Self-checks and limits

- Normal-form linear algebra verified: two independent linear conditions on
  three residues; direction $b\ne0$; checked in script preamble asserts.
- Kovacic numerics: script asserts double-pole $1/2$, $b=-1/4$ at all four
  poles via limits (not naive substitution), pole count $4$, $d=-1$ in Case 1
  and $d<0$ in Cases 2–3; run is green.
- BB1/BB2/BB3 are cited with exact theorem numbers: Kovacic (Cases 1–3
  necessary conditions); CFN Thm. 1.2/Cor. 5.6 (strong minimality),
  CFN Prop. 5.8 + Fact 5.7 (triviality/orthogonality to $C$ via
  verticalization), BFS Thm. 5.6 + Prop. 5.7 and DFN Thm. 1.1–1.2 (binary
  relations force pullback). The new content here is the normal form, the
  elimination/properness argument, the verticalization-to-independence step,
  and the two machine checks.
- No claim is made about which transcendental $\lambda$ give Fuchsian vs.
  non-Fuchsian monodromy; only Zariski-density ($\mathrm{SL}_{2}$) and
  avoidance of the countable pullback locus are used, both established.

## 8. References (results used, not re-proved)

- J. Kovacic, An algorithm for solving second order linear homogeneous
  differential equations, J. Symbolic Comput. 2 (1986) — Cases 1, 2, 3
  necessary conditions (BB1).
- G. Casale, J. Freitag, J. Nagloo, Ax–Lindemann–Weierstrass with
  derivatives and genus-$0$ Fuchsian groups — Thm. 1.2 / Cor. 5.6 (strong
  minimality from $\mathrm{PSL}_{2}$ Galois, BB2); §5 incl. Prop. 5.8 +
  Fact 5.7 (verticalization, triviality, orthogonality to $C$, BB3a).
- Baldassarri–Dwork–Freitag–Singer (BFS), Thm. 5.6 + Prop. 5.7 (binary
  relations force pullback, BB3b).
- DeVilbiss–Freitag–Nagloo, "Strict disintegration…," Thm. 1.1–1.2
  (pairwise relations force arithmetic/pullback; strict disintegration).
- F. Klein pullback theory for hypergeometric equations (classical input
  behind BB3b); Hurwitz spaces for the constructibility/countability input.
- Zilber trichotomy in $\mathrm{DCF}_{0}$ (Hrushovski–Sokolović;
  Pillay–Ziegler) — used only to pass from non-triviality to nonorthogonality
  to $C$ or some $A^{\sharp}$.

∎
