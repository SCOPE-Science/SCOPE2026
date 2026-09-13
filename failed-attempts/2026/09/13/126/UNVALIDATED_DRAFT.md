# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — The stated P^1 family is empty: no weakly admissible member, hence no crystalline V_t

## Theorem (TARGET resolution by disproof)

Let $p=11$, $K=\mathbf{Q}_{11^2}$, $E=\overline{\mathbf{Q}}_{11}$, with embeddings
$\sigma_0,\sigma_1$. Let $\zeta_1\ne\zeta_2$ be Teichmüller units and
$D=E e_1\oplus E e_2$ per component with
$\varphi(e_i)=11^2\zeta_i e_i$ ($\sigma$-linear). Define filtrations as in the
target: $\mathrm{Fil}^2_0=\mathrm{span}(e_1)$,
$\mathrm{Fil}^1_0(t)=\mathrm{span}(e_1+t e_2)$ ($t\in\mathbf{A}^1$),
$\mathrm{Fil}^1_0(\infty)=\mathrm{span}(e_2)$, and
$\mathrm{Fil}^1_1=\mathrm{span}(e_1+3e_2)$, $\mathrm{Fil}^2_1=\mathrm{span}(e_1)$.

Then:

1. **(Filtration axiom.)** For every $t\in\mathbf{P}^1(E)$ the data do not
   define a filtered $\varphi$-module. At $\sigma_1$,
   $\mathrm{Fil}^2_1\not\subseteq\mathrm{Fil}^1_1$ for all $t$; at $\sigma_0$,
   $\mathrm{Fil}^2_0\subseteq\mathrm{Fil}^1_0(t)$ iff $t=0$. In particular there
   is no $t$ with valid filtrations at both embeddings, and the claimed
   labelled weights $\{0,2\}/\{0,2\}$ (which require
   $\mathrm{Fil}^1_\sigma=\mathrm{Fil}^2_\sigma$ a line) never occur except
   possibly at $(\sigma_0,t=0)$.
2. **(Weak admissibility.)** Even at the single partially nested point
   $t=0$ (and at any hypothetical correction of $\sigma_1$ keeping
   $e_1\in\mathrm{Fil}^2_\sigma$ both $\sigma$), the $\varphi$-stable rank-one
   sub-isocrystal $D'=\mathrm{span}(e_1)$ satisfies $t_H(D')=4>2=t_N(D')$,
   violating $t_H\le t_N$. Hence no $D_t$ is weakly admissible.
3. **(Consequence.)** By Colmez–Fontaine, no $D_t$ corresponds to a
   crystalline representation $V_t$. The objects $V_t$, $\mathrm{ad}^0(V_t)$,
   the Bloch–Kato groups $H^1_f(G_K,\mathrm{ad}^0(V_t))$, $H^2(G_K,
   \mathrm{ad}^0(V_t))$, the generic value $g$, and the jump locus $J$ in the
   target statement are undefined: the presupposition that the written
   $D_t$ form a $\mathbf{P}^1$ family of weakly admissible modules is false.
   No Euler-characteristic / exponential computation can be started because
   its input does not exist.

So the complete answer is: $g$ and $J$ do not exist; $H^2$-vanishing is moot;
the target family is empty. This is a rigorous TARGET disproof.

## Proof

### Filtrations must be nested

A filtered $\varphi$-module over $K$ (with coefficients in $E$) requires, for
each embedding $\sigma$, a decreasing, exhaustive, separated filtration
$\cdots\supseteq\mathrm{Fil}^i_\sigma\supseteq\mathrm{Fil}^{i+1}_\sigma
\supseteq\cdots$ by $E$-subspaces. In particular
$\mathrm{Fil}^2_\sigma\subseteq\mathrm{Fil}^1_\sigma$ always.

For lines in a plane, $L_2\subseteq L_1$ with $\dim L_i=1$ forces $L_2=L_1$.
Hence validity is equivalent to equality of the two named lines. Equality is
tested by the $2\times2$ determinant: $(a_1,a_2)\sim(b_1,b_2)$ span the same
line iff $a_1b_2-a_2b_1=0$.

At $\sigma_1$: vectors $(1,0)$ and $(1,3)$; determinant $1\cdot3-0\cdot1=3$.
In residue characteristic $11$, $3\ne0$; since $|3|_{11}=1$, $3\ne0$ in $E$
(char. $0$). Lines are distinct, never nested, for every $t$ (the $\sigma_1$
filtration is $t$-independent).

At $\sigma_0$, finite $t$: vectors $(1,0)$ and $(1,t)$; determinant $t$.
Zero iff $t=0$. So nested (indeed equal) iff $t=0$. At $t=\infty$:
$(1,0)$ vs $(0,1)$; determinant $1\ne0$, distinct.

Thus no $t\in\mathbf{P}^1(E)$ is nested at both embeddings. The $\sigma_1$
obstruction alone empties the family uniformly in $t,\zeta_1,\zeta_2$.

Remark on weights: labelled weights $\{0,2\}$ at $\sigma$ mean, for rank two,
$\dim\mathrm{gr}^0_\sigma=\dim\mathrm{gr}^2_\sigma=1$ and
$\mathrm{Fil}^1_\sigma=\mathrm{Fil}^2_\sigma$ is the weight-$2$ line. Two
distinct lines cannot give this graded pattern; without nesting, graded
pieces are not even defined. Verified computationally in
`output/artifacts/check_obstruction.py`.

### Weak admissibility fails via $\mathrm{span}(e_1)$

Recall $t_N(D)=v_p(\det\varphi^f)/f$ with $f=[K_0:\mathbf{Q}_p]=2$,
$t_H(D)=\sum_\sigma\sum_i i\dim\mathrm{gr}^i_\sigma$ (Fontaine). Whole-module
numbers match numerically: $v_p(11^2\zeta_i)=2$, $\varphi^2$ has eigenvalues
of valuation $4$ each, $\det\varphi^2$ valuation $8$, so $t_N(D)=8/2=4$;
$t_H(D)=(0+2)+(0+2)=4$.

Let $D'=(K_0\otimes E)e_1$, rank one. It is $\varphi$-stable:
$\varphi(e_1)=11^2\zeta_1e_1\in D'$ and
$\varphi(ce_1)=\sigma(c)11^2\zeta_1e_1\in D'$. So it is a sub-isocrystal
that must satisfy $t_H(D')\le t_N(D')$ for weak admissibility.

$t_N(D')=4/2=2$ (single $\varphi^2$-eigenvalue of valuation $4$ divided by
$f=2$). For Hodge: $e_1$ spans $\mathrm{Fil}^2_\sigma$ at both $\sigma$
(by definition $\mathrm{Fil}^2_0=\mathrm{Fil}^2_1=\mathrm{span}(e_1)$), so
wherever the filtration is nested (in particular at $(\sigma_0,t=0)$ and
everywhere if one counts membership), $e_1$ carries Hodge weight $2$ per
embedding: $t_H(D')=2+2=4$. Hence $t_H(D')=4>2=t_N(D')$, a uniform
violation, independent of $t$ and of distinctness of $\zeta_i$. Any other
$\varphi$-stable lines are irrelevant: one violator suffices. Computed in
`check_obstruction.py`.

Therefore even repairing the $\sigma_1$ nesting (e.g. resetting
$\mathrm{Fil}^1_1$ to $\mathrm{span}(e_1)$) would still leave $D_t$ never
weakly admissible with these $\varphi$-slopes and weight-$2$ lines.

### Crystalline representations do not exist

Colmez–Fontaine: crystalline $E$-representations of $G_K$ are equivalent to
weakly admissible filtered $\varphi$-modules. Since the empty set above
contains no weakly admissible object, there are no $V_t$, no
$\mathrm{ad}^0(V_t)$, and no Bloch–Kato Selmer groups to compute dimensions
or jump loci of. The requested $g$, $J$, bases of crystalline cocycles, and
$H^2$-obstruction classes do not exist for this data. This disposes of the
target: it is false as stated, proved directly from the explicit $D_t$-data
without needing the exponential or Euler characteristic.

## What was checked

- Determinants $3$ ($\sigma_1$), $t$ ($\sigma_0$ finite), $1$ ($\infty$);
  script `output/artifacts/check_obstruction.py` reproduces all numbers.
- Valuation computation $t_N(D)=4$, $t_N(D')=2$, $t_H(D')=4$.
- $\varphi$-stability of $\mathrm{span}(e_1)$ under $\sigma$-linear $\varphi$.
- No dependence on $\zeta_1\ne\zeta_2$ beyond diagonal stability of $e_1$.

## Limitations / non-claims

- This is a negative result: it does not produce a nearby valid family, a
  corrected jump locus, or generic $H^1_f$ dimension for modified data.
- It uses standard Fontaine definitions (decreasing filtrations,
  $t_H\le t_N$ for all subobjects, Colmez–Fontaine equivalence); under any
  nonstandard convention dropping nesting or subobject inequalities the
  statement would have to be reformulated, but under the stated
  weakly-admissible crystalline setting the family is empty.
