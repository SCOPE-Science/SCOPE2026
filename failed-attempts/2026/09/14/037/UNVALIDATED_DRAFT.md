# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the total invariant-degree bound for quartic fields

## Claim (negation of the target bound)

Let

$$X = P(x,y)\,\partial_x + Q(x,y)\,\partial_y,\qquad
  P(x,y) = -2y,\;\; Q(x,y) = -5x^4,$$

over $\mathbb{C}$. Then $X$ satisfies every hypothesis of the target
($\max(\deg P,\deg Q)=4$, $\gcd(P,Q)=1$, finitely many affine singularities)
but possesses distinct irreducible invariant algebraic curves of total degree
$\ge 13$. In fact it possesses infinitely many. Hence the asserted bound
"sum of degrees $\le 12$" is **false**.

## Proof

**Step 1 — Hypotheses.** $\deg P = 1$, $\deg Q = 4$, so
$\max(\deg P,\deg Q)=4$. $P=-2y$ and $Q=-5x^4$ have no common nonconstant
factor, so $\gcd(P,Q)=1$ in $\mathbb{C}[x,y]$ (machine-checked: gcd is 1).
The affine singular locus $P=Q=0$ is $\{y=0,\ x^4=0\}=\{(0,0)\}$, a single
point, hence finite (machine-checked via Gr\"obner basis $\{x^4,y\}$).
So $X$ is an admissible quartic field. It is the Hamiltonian field of
$H(x,y)=y^2-x^5$, i.e. $X=(-H_y,H_x)$.

**Step 2 — Invariant curves with checked cofactors.**
For each $c\in\mathbb{C}$ put $f_c(x,y)=y^2-x^5-c$. Then

$$X(f_c) = P\,\partial_x f_c + Q\,\partial_y f_c
  = (-2y)(-5x^4) + (-5x^4)(2y) = 10x^4y - 10x^4y = 0 = 0\cdot f_c.$$

Thus each $f_c$ satisfies $X(f_c)=K_c f_c$ with cofactor $K_c\equiv 0$,
so (when irreducible) $\{f_c=0\}$ is an invariant algebraic curve.

**Step 3 — Irreducibility over $\mathbb{C}$ for every $c$.**
View $f_c = y^2 - g_c(x)$ with $g_c(x)=x^5+c$ as a monic quadratic in $y$
over the UFD $\mathbb{C}[x]$. It is reducible iff $g_c$ is a square in
$\mathbb{C}[x]$. Suppose $x^5+c = h(x)^2$ for some $h\in\mathbb{C}[x]$.
Comparing degrees: $5 = 2\deg h$, impossible since $5$ is odd. Hence no such
$h$ exists, for *every* $c\in\mathbb{C}$ (since $\deg(x^5+c)=5$ for all $c$).
By Gauss's lemma, $f_c$ is irreducible in $\mathbb{C}[x,y]$ for every $c$.

**Step 4 — Distinctness and degree count.**
$\deg f_c = 5$ for every $c$. For $c\ne c'$, $f_c - f_{c'} = c'-c$ is a
nonzero constant, so $f_c, f_{c'}$ are non-associate irreducibles defining
distinct (indeed disjoint) curves. Taking e.g. $c\in\{0,1,2\}$ gives three
pairwise distinct irreducible invariant curves of degrees $5+5+5=15\ge 13$.

Indeed *every* fiber $H-c$ is such a curve, so the total sum over all
distinct irreducible invariant curves is infinite, not $\le 12$.

**Step 5 — Conclusion.** The quartic field $X$ above satisfies all the
hypotheses and violates the claimed degree-sum bound. The "equality forces
a Darboux integral" clause is moot since the bound itself fails. This is the
second complete answer explicitly admitted by the target claim (an explicit
verified quartic counterexample with cofactors checked). ∎

## Computational verification

`output/artifacts/verify_counterexample.py` (SymPy) checks:
$\max\deg=4$; $\gcd(P,Q)=1$; singular locus Gr\"obner basis $\{x^4,y\}$
(single point $(0,0)$); $X(f_c)\equiv 0$ for $c=0,1,2$; $\deg f_c=5$ each
(total $15$); irreducibility over $\mathbb{Q}$ via `factor_list` (analytic
degree-parity argument above lifts this to $\mathbb{C}$ for all $c$);
pairwise differences nonzero constants. Output stored in
`output/artifacts/verify_counterexample_output.json`.
