# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Auditable partial portrait census for monic centered cubics with critical periods ≤ 4

## 1. Setting
$f(z)=z^3+az+b$ with critical points $c^2=-a/3$ (distinct iff $a\ne 0$).
For a critical point $c$ write $f(c)=c(2a/3)+b$. All claims replay from
committed integer data via `artifacts/audit_portraits.py` (sympy exact arithmetic).

## 2. Theorem (partial census)
The following fibers and portrait classes are certified exactly.

**(a) Bicritical symmetric fibers (uniqueness + realization).**
- Doubly-fixed portrait: unique fiber $(a,b)=(3/2,0)$.
  Indeed $f(c)-c=c(2a/3-1)+b$ must vanish at both $c=\pm c_0\ne0$,
  whence $2b=0$ and $2a/3-1=0$.
- Swap portrait ($c\leftrightarrow -c$): unique fiber $(a,b)=(-3/2,0)$.
  Indeed $f(c)+c$ vanishes mod $c^2+a/3$ there, while the remainder of
  $f(c)-c$ is $-2c\ne 0$, so the cycle is exactly period 2.

**(b) Bicritical tail portrait (realized).** At $(a,b)=(-3,0)$:
$+1\mapsto -2\mapsto -2$ and $-1\mapsto +2\mapsto +2$ (exact integer orbit logs),
so both critical points are strictly preperiodic tails onto distinct fixed points.

**(c) Unicritical exact-period census, $n=1,\dots,4$ ($a=0$).**
With $P_1=B$, $P_{n+1}=P_n^3+B$ (so $f_B^n(0)=P_n(B)$), exact division gives
$\deg P_n=3^{n-1}$; $P_1\mid P_3$ with quotient $Q_3$ of degree $8$;
$P_2\mid P_4$ with quotient $Q_4$ of degree $24$;
$Q_3(0)=Q_4(0)=1$ (hence coprime to all earlier $P_d$),
$\gcd(Q_3,P_2)=\gcd(Q_4,P_2)=1$, discriminants nonzero, both even polynomials.
Hence, counting $b\sim -b$ affine conjugacy ($z\mapsto -z$), there are exactly
$1,1,4,12$ unicritical classes of exact periods $1,2,3,4$; $n=1,2$ are realized by
$b=0$ ($0\mapsto 0$) and $b=i$ ($0\mapsto i\mapsto 0$); $n=3,4$ exist by degree
($Q_3,Q_4$ nonconstant, separable). Supplementary numeric witnesses:
$b_3\approx 0.55757+0.54035i$ ($|f^3(0)|\sim 10^{-15}$),
$b_4\approx 0.58384+0.27022i$ ($|f^4(0)|\sim 10^{-15}$).

**(d) Unrealizable portrait (empty fiber).** The abstract portrait
"$c$ fixed and $-c\mapsto c$ in one step" is realized by no $f$ with distinct
critical points: with $e_1=Cc(2A/3)+Bb-Cc$, $e_2=-Cc(2A/3)+Bb-Cc$,
$e_1-e_2=4ACc/3$, so $e_1=e_2=0$ forces $A=0$ or $Cc=0$; $A=0$ gives colliding
critical points, contradicting distinctness. Paired with (a), this is an
obstructed-vs-realized gap at the fiber level.

## 3. Limitations (explicit)
- This is a **partial** census: no complete list $L$ of all period-$\le 4$ portraits
  (mixed periods, longer tails, general $a\ne 0$ dynatomic resultants) is claimed.
- The obstruction in (d) is proved by elementary fiber emptiness, **not** by a
  Levy-cycle/Thurston-matrix certificate as originally targeted.
- Periods 3 and 4 unicritical existence uses FTA + exact separability/coprimality;
  no certified isolating boxes or minimal polynomials for $b_3,b_4$ are given.
- The gap pair is algebraic-combinatorial, not an adjacent Thurston-obstructed pair.

## 4. Verification
Run `python3 artifacts/audit_portraits.py`; every check prints PASS (`ALL: OK`).
No dynamics archive is trusted: all divisions, remainders, gcds, discriminants, and
orbit logs are recomputed from the committed integers above.
