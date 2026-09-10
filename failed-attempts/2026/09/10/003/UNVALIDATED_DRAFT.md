# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Weak-glueing PASS verdict for the symmetric rank-1 degree-4 pre-limit series
on the 3-edge genus-6 metrized complex (binary verdict + slope-weight log; no smoothing claim)

## 1. Committed objects

**Complex M*.** Base field $\kappa$ algebraically closed. Two vertices
$\{a,b\}$, vertex curves $C_a=C_b=\mathbf P^1$ with affine coordinate $t$.
Joint: exactly $3$ parallel edges $e_1,e_2,e_3$ of unit length,
chain structure $\mathbf n=(1,1,1)$. Loops: $2$ loop edges at each vertex,
with $\mu=0$ chips (no joint twisting contribution); they are recorded as
vertex genus $\mathfrak g(a)=\mathfrak g(b)=2$, so total genus
$g=b_1(\theta_3)+4=2+4=6$.
Joint marked points $P_1=0$, $P_2=1$, $P_3=\infty$ on each $\mathbf P^1$;
loop half-edge marked points are chosen general and disjoint from
$\{0,1,2,\infty\}$; base point $R=\infty$.

**Series S*.** Line bundles $L_a=L_b=\mathcal O(2R)$ (degree $2$ each,
total $d=4$). Spaces $V_a=V_b=\mathrm{span}\{f_0,f_1\}$,
$f_0=1$, $f_1=1-t/2$ (dimension $2$, so $r=1$).
Both are regular sections of $\mathcal O(2R)$:
$(f_0)+2R=2R\ge 0$; $(f_1)=(2)-(\infty)$ as a rational function, so
$\mathrm{div}^0(f_1)=(f_1)+2(\infty)=(2)+(\infty)\ge 0$.
In the fixed trivialization the section evaluations at
$(P_1,P_2,P_3)=(0,1,\infty)$ are $f_0\mapsto(1,1,1)$,
$f_1\mapsto(1,1/2,0)$; the support of $f_1$ is $\{0,1\}$ ($f_1$ has a
simple zero at $P_3$). This is the symmetric $\{0,1\}$
displacement-tableau profile.
$\Gamma$-divisor $D_\Gamma=2(a)+2(b)$.

**Multidegree.** $w_0=(w_G=\{a{:}2,b{:}2\},\mu=0$ on joint edges and loops$)$;
tight tuple = the reduced pair $(w_a^{\mathrm{red}},w_b^{\mathrm{red}})$.
References: He arXiv:1707.04624 (weak glueing, Sec 3; Thms 4.3/4.7/4.8,
Lemma 4.9, Cor 4.10); Amini–Gierczak–Richman arXiv:2303.07729 (slope sets,
weight formula $d-r+rg$, positivity).

## 2. Twisting divisors and multivanishing (He Sec 2)

Single $\bar G$-edge $e$ with $3$ parallel graph edges over it.
$w_a$ is $a$-reduced, and one twist at $(e,a)$ sends
$w_G(a)=2\mapsto 2-3=-1<0$ (each of the $3$ edges has $\mu=0$, each
decrements by $1$). Hence $b_{a,b}=0$: the maximal number of nonneg twists
is $0$. Twisting divisors:
$D_0^{e,a}=0$, $D_1^{e,a}=P_1+P_2+P_3$ of degree $3>2=\deg L_a$;
same on side $b$. Single critical index $j=0$ per side.
$V_a(-D_1)=0$: a combination $c_0f_0+c_1f_1=c_0+c_1(1-t/2)$ vanishing at
$P_1=0$ and $P_2=1$ forces $c_0+c_1=0$ and $c_0+c_1/2=0$, hence
$c_0=c_1=0$. Both sections lie in $V_a(-D_0)=V_a$.
Multivanishing sequences $a^{e,a}=a^{e,b}=(0,0)$.
Pre-limit condition (I) (He Def 2.15(I)) holds, with equalities throughout
(refined case). Machine check: §(A)–(A2) of the replay log.

## 3. Weak-glueing check: PASS (He Def 3.3 / Remark 3.4)

Here $g_0=\#\{l:a_l^{e,a}=\deg D_0,\ a_{r-l}^{e,b}=\deg D_{b-0}\}=2$,
the full dimension of each quotient $V(-D_0)/V(-D_1)=V$.
Take $W_a=W_b=$ the whole $2$-plane. In the common trivialization the
evaluation matrix is $B=[(1,1,1),(1,1/2,0)]$ on each side.
Exact rational enumeration (replay §(B)) gives attained torus-orbit
supports on **each** side
$\{\{0,1\},\{0,2\},\{1,2\},\{0,1,2\}\}$ (plus $\{\}$ for the zero vector):
$\{0,1\}$ is $f_1$ itself; $\{1,2\}$ is $\mathrm{row}_0-\mathrm{row}_1$;
$\{0,2\}$ is $\mathrm{row}_0-2\,\mathrm{row}_1$; $\{0,1,2\}$ is
$\mathrm{row}_0$; no singleton supports exist in this $2$-plane in
$\kappa^3$. Both sides are identical, so for every torus
orbit $T_a$ (resp. $T_b=\varphi(T_a)$), $T_a\cap W_a\ne\varnothing\iff
T_b\cap W_b\ne\varnothing$, and by He Remark 3.4 the dimension equality
$\dim(T_a\cap W_a)=\dim(T_b\cap W_b)$ follows. **Verdict: PASS.**
Per-joint-edge reading: on $e_1$ ($P_1=0$) both basis sections are nonzero
($1,1$) and $\mathrm{row}_0-\mathrm{row}_1$ vanishes there; on $e_2$
($P_2=1$) both are nonzero ($1,1/2$) and $\mathrm{row}_0-2\,\mathrm{row}_1$
vanishes there; on $e_3$ ($P_3=\infty$) $f_1$ has a simple zero and the
vanishing pattern is matched symmetrically. No violating edge exists.

**Explicit Osserman data (He Def 2.15(II)).** With $\varphi=\mathrm{id}$
take $s_0=f_0,s_1=f_1$ and $s'_0=f_1,s'_1=f_0$; then
$\varphi(s_0)=s'_1$, $\varphi(s_1)=s'_0$. Condition (II) holds as a
glueing-datum record. Codimension datum recorded only: the jump
$\deg(D_1-D_0)=3$ with $g_0=2$ against $c=3-1=2$ glueing parameters;
sufficiency via Lemma 4.9 / Thm 4.8 is NOT invoked (see §4).

## 4. Smoothing limitation (no algebraic-gonality claim)

He Thm 4.3(II) with $\mathbf n=(1,1,1)$: the integer vector
$x=(1,-1,0)$ satisfies $\sum x_i\mathbf n(e_i)=0$ with a unique positive
entry, giving $\sum_i\lfloor x_j\mathbf n(e_j)/\mathbf n(e_i)\rfloor
=1+1+1=3$, so $d'<3$, i.e. $d'\le 2$. With $d=4$, the hypothesis
$d\le d'$ FAILS. Hence He Thm 4.8 and Cor 4.10 cannot be invoked for this
$(M^*,S^*)$ pair, and **no smoothing or algebraic-gonality ($\le 4$)
claim is made**. The headline result is strictly the preset-fallback
binary weak-glueing PASS verdict with its slope-weight log.

## 5. Slope-weight log (AGR)

$D_\Gamma=2(a)+2(b)$ is $a$- and $b$-reduced (Dhar burning, replay §(C)).
Exact Dhar reduction: every $D-(x)$ ($x\in\{a,b,m_1,m_2,m_3\}$, $m_i$ =
subdivided joint-edge midpoints) has effective $x$-reduced representative;
$D-(a)-(m_1)$ has $a$-reduced representative $(1,2,-1,0,0)$, hence is
unwinnable (reduced representatives are unique). So the tropical
Baker–Norine rank of $D_\Gamma$ is **exactly $1$**.
Vertex reduced coefficients $D_a(a)=D_b(b)=2$ give local Weierstrass
weights $\mu(a)=\mu(b)=2-1=1$ (AGR Remark 3.3 form $\mu(x)=D_x(x)-r$).
Joint-midpoint reduced coefficients are $3$–$4$, i.e. interior
Weierstrass points of weights $2$–$3$ (consistent with AGR Thm 1.8:
every cycle meets the Weierstrass locus). Global identity
$d-r+rg=4-1+6=9$ is the AGR theorem arithmetic; machine-certified local
contributions are $1+1$ at the vertices with the balance on
loop/joint interiors.

## 6. Replay

`python3 output/artifacts/verify_target.py` prints `VERIFY_TARGET_OK`
(committed inputs, twisting table, regular-section check, torus-pattern
match with per-edge PASS lines, explicit Osserman data, Dhar rank
letters, vertex weights, smoothing-limitation block). All claims above
are logged there with exact values.

## 7. Limitations / honest scope

(i) Loops are treated as vertex-genus augmentation ($\mathfrak g=2$ each)
with general loop marked points; the joint twisting/glueing computation
uses the loopless $3$-edge core, which is exactly the He-relevant datum.
(ii) The strongly Brill–Noether general hypothesis on the rational
components is admitted/assumed, not proved. (iii) Only vertex weights
$(1,1)$ are machine-certified pointwise; the total $9$ is the cited AGR
sum identity. (iv) No smoothing, lifting, or gonality transfer is claimed
(§4). (v) Originality: the test gives the verdict, prior papers give the
framework; no prior source logs this M*/S* cell (admission review).
