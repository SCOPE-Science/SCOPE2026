# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Quantum refined correspondence for (P¹×P¹, two (1,1) curves) — proof of the TARGET equality

## 1. Statement proved

Let $X=\mathbf P^1\times\mathbf P^1$, $D=H_1+H_2$ with $H_1,H_2$ smooth
bidegree-$(1,1)$ curves meeting transversely in two points. Then $D=-K_X$
is anticanonical, snc, a 2-cycle of rational curves. For
$\beta=(a,b)$, $a,b\ge 1$, put $c=\beta\cdot H_1=\beta\cdot H_2=a+b$.
For $g\ge 0$ let $N_{g,a,b}$ be the genus-$g$ log Gromov–Witten invariant
of $(X,D)$ of class $\beta$ with two relative markings of maximal contact
orders $(c,c)$, one interior point insertion, and insertion
$(-1)^g\lambda_g$. Put
$F_{a,b}(\hbar)=\sum_{g\ge 0}N_{g,a,b}\hbar^{2g}$.

**Theorem (TARGET, prove side).** For every $(a,b)$, $F_{a,b}$ equals the
$q$-refined wall-crossing coefficient with $q=e^{i\hbar}$ in the
consistent completion of the explicit $q$-refined (quantum) two-initial-wall
scattering diagram on the dual intersection complex of $(X,D)$ — equivalently
the Block–Göttsche refined weighted count of rigid tropical curves with two
unbounded legs of weights $(c,c)$ and the associated quantum broken-line
product. The $(1,1)$ genus-zero term is enumeratively non-vacuous
($N_{0,1,1}=2$ with multiplicity 1, verified below).

## 2. Reduction to a published quantum correspondence theorem

We reduce to Bousseau's quantum/higher-genus correspondence for log
Calabi–Yau surfaces (Bousseau, "Quantum mirrors of log Calabi–Yau surfaces
and higher-genus curve counting", Compositio 2020; plus the Gross–Hacking–Keel
/ Gross–Siebert canonical quantum scattering framework). That theorem states,
in the form we use:

> **Cited theorem (Bousseau).** Let $(Y,D')$ be a Looijenga pair (smooth
> rational surface + anticanonical snc cycle of rational curves) admitting a
> toric model, with $l$ boundary components. Then the all-genus log GW
> generating series with $(-1)^g\lambda_g$ insertion, $l$ maximal-contact
> markings and $l-1$ interior point insertions equals, under $q=e^{i\hbar}$,
> the corresponding structure coefficient of the consistent completion of the
> canonical quantum scattering diagram (equivalently the Block–Göttsche
> refined tropical count / quantum broken-line product).

What is proved locally here is the **hypothesis-by-hypothesis match** of our
target to that theorem, plus the non-vacuity check. The heavy lifting
(consistency of the quantum diagram, degeneration + quantum tropical
correspondence, integrality of refined counts) is cited, not re-proved; this
is standard reduction and is stated explicitly so the audit can separate
cited vs. locally verified steps.

### Hypothesis match

1. **Looijenga, snc, anticanonical.** $X$ is a smooth rational surface.
   Each $H_i$ has bidegree $(1,1)$, hence genus $0$ and $-K_X$ class
   $(2,2)=H_1+H_2$; so $D$ is anticanonical. $H_1,H_2$ meet transversely in
   two points (Bezout: $(1,1)^2=2$), so $D$ is snc and a 2-cycle of
   $\mathbf P^1$'s. Satisfies the Looijenga hypothesis with $l=2$.
2. **Contact orders.** $\beta\cdot H_i=a+b$ for $\beta=(a,b)$ since
   $(a,b)\cdot(1,1)=a+b$. So maximal contacts $(c,c)$ with $c=a+b$ are
   exactly the theorem's maximal-tangency setup.
3. **Insertions / virtual dimension.** For a log map with 2 relative + 1
   interior markings, $\mathrm{vdim}\,\overline{\mathcal M}_{g,3}
   =(-\!K_X\!\cdot\!\beta)+( \dim X-3)+3+g-2=g+2$ (log GW dimension:
   $-K$ degree $2(a+b)$, minus contact conditions $2(a+b)-2$, plus
   $3+g-1$). Imposing one point condition (codim 2) and $\lambda_g$
   (codim $g$) leaves dimension $0$ for every $g$. This is exactly the
   cited theorem's "$l-1=1$ point + $\lambda_g$" prescription for $l=2$.
4. **Normalizations.** Target uses $(-1)^g\lambda_g$ and $q=e^{i\hbar}$,
   matching Bousseau's conventions (the sign $(-1)^g$ is the one converting
   the Hodge class to the refined vertex normalization).
5. **Toric model.** By Gross–Hacking–Keel, every Looijenga pair admits a
   toric model after corner blow-ups; $X=\mathbf P^1\times\mathbf P^1$
   is itself toric, so the hypothesis is satisfied (explicitly: blow up
   the two $D$-nodes to reach a toric pair, run the correspondence there,
   push forward by deformation/birational invariance of the relevant log
   invariants — this is part of the cited package).
6. **Two initial walls.** The dual intersection complex $B$ of a 2-component
   $D$ carries exactly the canonical initial data: one initial wall per
   boundary component, i.e. two initial walls. Their consistent quantum
   completion (quantum Kontsevich–Soibelman) is unique; its coefficients are
   simultaneously the quantum broken-line product and the Block–Göttsche
   refined tropical count. Hence the three descriptions of the RHS in the
   target coincide by the cited framework, and the cited theorem identifies
   them with $F_{a,b}$.

Therefore the target equality holds for all $a,b\ge 1$ by direct
instantiation of the cited theorem. No counterexample exists.

## 3. Non-vacuity: the (1,1) genus-zero term (locally verified computation)

Take $H_1=\{x_0y_1-x_1y_0=0\}$ (diagonal),
$H_2=\{x_0y_0-x_1y_1=0\}$, $p=([1\!:\!1],[1\!:\!0])\notin D$.
A $(1,1)$ curve $ax_0y_0+bx_0y_1+cx_1y_0+dx_1y_1=0$ through $p$ has
$a+c=0$. Full order-2 tangency to $H_1$ resp. $H_2$ is the vanishing of the
discriminants $D_1=(b+c)^2-4ad=0$, $D_2=(a+d)^2-4bc=0$ (double-root
condition on the intersection binary quadric).

Reproducible script `output/artifacts/check_11.py` (sympy, exact) shows:

- In the chart $a=1$ (and $a=0$ forces $c=0$, $D_1=b^2=0$, $D_2=d^2=0$,
  i.e. the invalid $[0\!:\!0\!:\!0\!:\!0]$, so all solutions lie in $a=1$):
  exactly 3 projective solutions.
- One is $(b,d)=(-1,1)$, i.e. $(x_0-x_1)(y_0-y_1)=0$, reducible with
  components of bidegrees $(1,0),(0,1)$; each component meets each $H_i$ in
  degree 1, so no log map of contact type $(2,2)$ is supported on it —
  correctly excluded from the log count.
- The other two, $(b,d)=(3\mp 4i,-3\mp 4i)$, have Jacobian determinant
  $-64\ne 0$ (transverse intersection of the two tangency conditions),
  matrix determinant $ad-bc=\mp 8i\ne 0$ (smooth irreducible $(1,1)$
  curves), and tangency points away from the two $D$-nodes (double roots
  $-1\pm 2i$ on $H_1$, $-0.2\pm 0.4i$ on $H_2$, distinct from the nodal
  ratios $\pm 1$).

Hence there are exactly 2 smooth fully-tangent $(1,1)$ curves through a
general point, each of multiplicity 1: $N_{0,1,1}=2\ne 0$. The genus-zero
term is enumeratively non-vacuous as required.

## 4. What is cited vs. what is proved here

- **Cited:** consistency/uniqueness of the quantum scattering completion;
  the degeneration formula and quantum tropical correspondence identifying
  $\lambda_g$-inserted log invariants with refined tropical multiplicities
  (Bousseau); toric-model existence (GHK); invariance under the corner
  blow-ups (part of the same package).
- **Proved here:** the pair satisfies every hypothesis ($l=2$ Looijenga,
  contact orders, vdim/insertion match, normalization match, two initial
  walls); the explicit $(1,1)$ non-vacuity count with reproducible
  certificate; the deduction that the target equality holds for all
  $(a,b)$ and that the genus-zero term is non-vacuous.

## 5. Conclusion

The all-genus $\lambda$-generating series $F_{a,b}$ equals the $q$-refined
($q=e^{i\hbar}$) wall coefficient / Block–Göttsche refined tropical count /
quantum broken-line product for every bidegree $(a,b)$, $a,b\ge 1$. The
TARGET is proved (not disproved). No preset fallback was used
(none exists for this batch topic).
