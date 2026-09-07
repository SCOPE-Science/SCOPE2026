# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A checkable correction: the rational-Dulac margin fails, the zero-cycle
conclusion holds by elementary energy — cubic Liénard box
[1.1,1.2]×[1.9,2.0]

## Abstract

For the cubic Liénard family

$$x'=y-F(x;a,b),\qquad y'=-x,\qquad
  F(x;a,b)=x^{3}+bx^{2}+ax\tag{1}$$

on the parameter box $A=[1.1,1.2]\times[1.9,2.0]$ we prove two things.
First, the proposed Dulac certificate with weight $B(x)=(1+2x^{2})^{-2}$
and uniform margin $\operatorname{div}(BX)/B\le -1/20$ on $\mathbb R^{2}$
is **false**: the true divergence is affine in $y$ and unbounded above
below on every vertical line $x\ne0$ with $B'(x)\ne0$; e.g. at
$(a,b,x,y)=(1.1,2.0,1,-10)$ it equals $59/2>0$. The audit formula drops
the $y$-term and flips the sign of the $F$-term. More generally no
$C^{1}$ weight $B(x)>0$ with $B'\not\equiv0$ can have fixed-sign
divergence on all of $\mathbb R^{2}$ for this family. Second, we rescue
the nonexistence corollary by a classical energy function:
$V=(x^{2}+y^{2})/2$ satisfies $\dot V=-xF(x)\le -\tfrac1{10}x^{2}\le0$
uniformly over $A$, so (1) has no closed orbit in $\mathbb R^{2}$ for any
$(a,b)\in A$, the origin is the unique equilibrium (a locally
asymptotically stable focus), and it is in fact globally asymptotically
stable. All identities are exact-rational and replayed by the accompanying
stdlib+sympy script.

*Status of novelty.* The energy argument is classical, not original; the
contribution is a checkable correction: an explicit refutation of the
stated Dulac margin plus a certified replacement proof over the same box,
with machine-replayable exact arithmetic.

## 1. Setup, equilibrium, classical-test blindness

Equilibria of (1) satisfy $-x=0$ then $y=F(0)=0$; hence $(0,0)$ is the
unique equilibrium for every $(a,b)$. The Jacobian there is

$$J=\begin{pmatrix}-F'(0)&1\\-1&0\end{pmatrix}
   =\begin{pmatrix}-a&1\\-1&0\end{pmatrix},$$

with $\operatorname{tr}J=-a<0$, $\det J=1>0$, discriminant
$a^{2}-4\in[1.21-4,1.44-4]<0$ on $A$. Hence a locally asymptotically
stable focus. (Exact interval arithmetic; replayed in script, part A
context.)

With $B\equiv1$, $\operatorname{div}X=-F'(x)$,
$F'(x)=3x^{2}+2bx+a$, discriminant

$$\Delta=4b^{2}-12a=4(b^{2}-3a).$$

Since $b^{2}-3a$ is increasing in $b$ and decreasing in $a$,
over $A=[1.1,1.2]\times[1.9,2.0]$,

$$b^{2}-3a\in[1.9^{2}-3(1.2),\,2.0^{2}-3(1.1)]=[0.01,0.7],$$

so $\Delta\in[0.04,2.8]>0$ throughout (exact `Fraction` check in
script, part C). Thus $F'$ has two distinct real roots and $-F'$
changes sign; the $B\equiv1$ Bendixson test is inconclusive on every
$(a,b)\in A$. This part of the audit plan is correct.

## 2. Refutation of the stated Dulac margin

Let $B(x)=(1+2x^{2})^{-2}>0$, smooth on $\mathbb R^{2}$, and
$X=(y-F,-x)$. Since $B$ depends only on $x$,

$$\operatorname{div}(BX)
   =\partial_{x}[B(y-F)]+\partial_{y}[-Bx]
   =B'(x)(y-F(x))-B(x)F'(x).\tag{2}$$

Hence, with $B'/B=\frac{d}{dx}\log B=-8x/(1+2x^{2})$,

$$\boxed{\frac{\operatorname{div}(BX)}{B}
   =-F'(x)-\frac{8x}{1+2x^{2}}\,(y-F(x))}\tag{3}$$

symbolically re-derived in sympy (script, part A: the difference of the
two sides simplifies to $0$). In particular the criterion function is
affine in $y$ with slope $-8x/(1+2x^{2})$.

The audit plan instead defines
$M(x;a,b)=-(a+2bx+3x^{2})-8x(ax+bx^{2}+x^{3})/(1+2x^{2})$, i.e.
$-F'-8xF/(1+2x^{2})$. This is doubly wrong: it omits the term
$-8xy/(1+2x^{2})$ (no "cancellation" occurs — (2) is already complete),
and even on the slice $y=0$ it has the wrong sign: the true slice is
$-F'+8xF/(1+2x^{2})$. The four vertex quartics therefore audit an
incorrect function.

**Theorem 1 (explicit counterexample).** At
$(a,b,x,y)=(1.1,2.0,1,-10)$,

$$F=4.1=\tfrac{41}{10},\quad F'=8.1=\tfrac{81}{10},\quad
  \frac{\operatorname{div}(BX)}{B}
  =-\tfrac{81}{10}-\tfrac{8}{3}(-10-\tfrac{41}{10})
  =\tfrac{59}{2}=29.5>0>-\tfrac1{20}.$$

So $\operatorname{div}(BX)/B\le-1/20$ uniformly on $\mathbb R^{2}$
fails; indeed $\operatorname{div}(BX)/B$ takes positive values. All
fractions are exact (`Fraction` check, script part B).

**Lemma (no $x$-only weight works on $\mathbb R^{2}$).**
Let $B=B(x)>0$ be $C^{1}$ with $B'(x_{0})\ne0$ at some $x_{0}$. Then for
(1), $\operatorname{div}(BX)/B=(B'/B)(x_{0})(y-F(x_{0}))-F'(x_{0})$
is non-constant affine in $y$ hence takes both arbitrarily large
positive and negative values as $y$ varies at fixed $x=x_{0}$. In
particular no such $B$ can satisfy $\operatorname{div}(BX)/B<0$
everywhere on $\mathbb R^{2}$. The only way to avoid this is
$B'\equiv0$, i.e. constant $B$, which reduces to the $B=1$ case already
shown inconclusive. *Proof.* Immediate from (2). ∎

Consequence: fallback (i) of the topic (a certified sub-box of $A$) can
never rescue an $x$-only weight on $\mathbb R^{2}$, since the
$y$-unboundedness argument uses no property of $(a,b)$. Any Dulac
region excluding large $|y|$ would additionally need a proof that every
closed orbit lies inside it — which the energy argument below renders
moot.

## 3. Rescue: energy proof of no closed orbits (uniform over $A$)

**Theorem 2.** For every $(a,b)\in A$, system (1) has no periodic
(closed) orbit in $\mathbb R^{2}$. The origin is globally asymptotically
stable.

*Proof.* Take $V(x,y)=(x^{2}+y^{2})/2$, radially unbounded, positive
definite. Along (1),

$$\dot V=x(y-F)+y(-x)=-xF(x)=-x^{2}(x^{2}+bx+a).\tag{4}$$

Complete the square:
$x^{2}+bx+a=(x+b/2)^{2}+(a-b^{2}/4)\ge a-b^{2}/4$.
Since $a-b^{2}/4$ increases in $a$ and decreases in $b>0$, its minimum
over $A$ is at $(1.1,2.0)$:

$$\min_{A}(a-b^{2}/4)=1.1-1.0=0.1=\tfrac1{10}\quad\text{(exact)},$$

so uniformly over $A$ and all $x$,

$$x^{2}+bx+a\ge\tfrac1{10},\qquad
  \boxed{\dot V\le -\tfrac1{10}x^{2}\le0.}\tag{5}$$

*No closed orbits (elementary).* Suppose $\gamma(t)$, period $T>0$,
is a closed trajectory, not the equilibrium. Then
$\frac{d}{dt}V(\gamma(t))=-x(t)F(x(t))\le0$ with equality iff $x(t)=0$.
$\gamma$ cannot satisfy $x\equiv0$: then $y'=-x\equiv0$ gives constant
$y$, and $x'=y-F(0)=y$ forces $y\equiv0$, i.e. the equilibrium. Hence
$x(t_{0})\ne0$ for some $t_{0}$, and by continuity $\dot V<0$ on a
nontrivial interval, so $\oint_{\gamma}dV=V(\gamma(T))-V(\gamma(0))<0$,
contradicting periodicity ($=0$). Thus no closed orbit exists. Note this
uses only $xF(x)>0$ for $x\ne0$, which (5) implies.

*Global asymptotic stability.* $V$ gives Lyapunov stability and all
sublevel sets are compact; trajectories are bounded. By LaSalle's
invariance principle (cited textbook theorem, e.g. Khalil Thm 4.4),
every trajectory approaches the largest invariant set in
$\{\dot V=0\}=\{x=0\}$. On $x=0$, (1) gives $x'=y$, so invariance forces
$y=0$. Hence every trajectory tends to the origin, which is therefore
globally asymptotically stable (local stability from $V$, global
attractivity from LaSalle). ∎

*Remark.* Theorem 2 implies in particular the topic's nonexistence
corollary over the whole box, with the stronger uniform decrement (5)
and a one-line classical proof. The discriminant condition
$b^{2}-4a<0$ (equivalently $a-b^{2}/4>0$) is exactly what makes the box
"easy" for energy and "hard" for $B=1$ ($b^{2}-3a>0$): both hold here.

## 4. Reproducibility

`output/artifacts/verify_lane85.py` (stdlib + sympy 1.12 only) checks:

- (A) symbolic identity (3) via `sp.simplify` ($=0$ asserted);
- (B) exact-`Fraction` counterexample $59/2$;
- (C) exact discriminants $[0.04,2.8]$;
- (D) exact Lyapunov margin $\min(a-b^{2}/4)=1/10$;
- (E) reproduction of the audit vertex polynomial
  $-14x^{4}-24x^{3}-14x^{2}-4x-1.1$ at $(1.1,2.0)$, flagged as auditing
  the wrong (sign-flipped, $y$-dropped) function.

Run: `python3 output/artifacts/verify_lane85.py` (seconds; log in
`verify_output.txt`).

## 5. Limitations and conjecture/uncertainty separation

- **Proved:** Theorem 1 (Dulac margin false), Lemma ($x$-only weights
  impossible on $\mathbb R^{2}$), Theorem 2 (zero closed orbits + GAS
  via (5) + LaSalle-cited step). Provenance of each equation is shown
  above; no step relies on numerics.
- **Cited, not re-proved:** LaSalle's invariance principle (standard).
  The no-cycle claim itself needs no citation (elementary integral
  argument given in full).
- **Computed evidence:** the script's exact-rational/symbolic checks.
- **Not claimed:** any new Dulac weight, any limit-cycle upper bound
  beyond zero on this box, any statement outside $A$ (though (4) plainly
  generalizes wherever $xF(x)>0$), and no global-stability claim beyond
  what LaSalle + (5) give.
- **Originality:** the correction (Theorem 1 + Lemma) is the checkable
  new record for this lane's box; the rescue proof is classical energy
  and claimed only as a corrected certificate, not as a novel method.
