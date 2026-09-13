# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the torsion-arc Kakeya 5/2 lower bound (as stated)

## 1. Statement

Let $e_1=(1,0,0)$ and let $\mathcal F_{\rm tor}$ be the family of $C^3$
arclength-parametrized arcs $\gamma:[0,1]\to\mathbb R^3$ with curvature
$\kappa(t)\ge 1/2$ and torsion $|\tau(t)|\ge 1/2$ for all $t$.
A compact set $E\subset\mathbb R^3$ is called a *torsion Kakeya set* if,
in the literal wording of the topic, for every direction $u\in S^2$ there
exist a rotation $R$ with $R(e_1)=u$ and a translation $x$ with

$$x+R(\gamma([0,1]))\subset E\quad\text{for some }\gamma\in\mathcal F_{\rm tor}.$$

**Claim (disproved).** Every torsion Kakeya set $E$ satisfies
$\dim_H(E)\ge 5/2$.

We disprove this by exhibiting an explicit compact torsion Kakeya set
$E_0$ with $\dim_H(E_0)=1<5/2$.

## 2. The direction constraint is vacuous

$\mathcal F_{\rm tor}$ is rotation-invariant: if $\gamma\in\mathcal F_{\rm tor}$
and $Q\in SO(3)$ (indeed any $Q\in O(3)$), then $Q\circ\gamma$ is still
$C^3$, unit-speed, with the same curvature and $|\tau|$ preserved
($\tau$ preserved exactly for $SO(3)$, up to sign for reflections).
Hence $Q\circ\gamma\in\mathcal F_{\rm tor}$.

Fix any $\tilde\gamma\in\mathcal F_{\rm tor}$ and any $u\in S^2$.
Choose any rotation $R_0$ with $R_0(e_1)=u$ (exists by transitivity of
$SO(3)$ on $S^2$). Set $\gamma:=R_0^{-1}\circ\tilde\gamma$.
Then $\gamma\in\mathcal F_{\rm tor}$ by rotation-invariance and
$R_0(\gamma([0,1]))=\tilde\gamma([0,1])$.
Consequently, *any* compact set containing a single translate of a single
$\mathcal F_{\rm tor}$ arc automatically satisfies the torsion-Kakeya
property for every $u$ simultaneously (with $x$ fixed and $\gamma$
depending on $u$ via $R^{-1}$). In particular a single unit arc suffices.

## 3. Explicit admissible arc

Define for $s\in[0,1]$

$$\gamma_0(s)=\Bigl(\cos\frac{s}{\sqrt2},\ \sin\frac{s}{\sqrt2},\
\frac{s}{\sqrt2}\Bigr).$$

$\gamma_0$ is $C^\infty$. Its derivatives are

$$\gamma_0'(s)=\Bigl(-\tfrac1{\sqrt2}\sin\tfrac{s}{\sqrt2},\
\tfrac1{\sqrt2}\cos\tfrac{s}{\sqrt2},\ \tfrac1{\sqrt2}\Bigr),\qquad
  |\gamma_0'(s)|^2=\tfrac12\sin^2+\tfrac12\cos^2+\tfrac12=1,$$

so $\gamma_0$ is arclength-parametrized. Moreover

$$\gamma_0''(s)=\Bigl(-\tfrac12\cos\tfrac{s}{\sqrt2},\
  -\tfrac12\sin\tfrac{s}{\sqrt2},\ 0\Bigr),\qquad
  \kappa(s)=|\gamma_0''(s)|=\tfrac12,$$

and with
$\gamma_0'''(s)=(\tfrac1{2\sqrt2}\sin\frac{s}{\sqrt2},\
-\tfrac1{2\sqrt2}\cos\frac{s}{\sqrt2},0)$,

$$\gamma_0'\times\gamma_0''=
  \Bigl(\tfrac{\sin(s/\sqrt2)}{2\sqrt2},\
  -\tfrac{\cos(s/\sqrt2)}{2\sqrt2},\ \tfrac1{2\sqrt2}\Bigr),$$
$$\langle\gamma_0'\times\gamma_0'',\gamma_0'''\rangle
  =\tfrac{\sin^2+\cos^2}{8}=\tfrac18.$$

For a unit-speed curve $\tau=\langle\gamma'\times\gamma'',\gamma'''\rangle/
|\gamma''|^2$, so

$$\tau(s)=\frac{1/8}{1/4}=\frac12\qquad\forall s.$$

Hence $\kappa\equiv 1/2\ge 1/2$ and $|\tau|\equiv 1/2\ge 1/2$;
$\gamma_0\in\mathcal F_{\rm tor}$.
Since $z(s)=s/\sqrt2$ is strictly increasing, $\gamma_0$ is injective on
$[0,1]$. This is verified symbolically in
`output/artifacts/verify_helix.py` (speed$^2=1$, $\kappa=1/2$, $\tau=1/2$).

## 4. Counterexample set and its dimension

Put $E_0:=\gamma_0([0,1])$. As a continuous image of $[0,1]$, $E_0$ is
compact.

*Upper bound.* By $|\gamma_0'|\equiv1$,
$|\gamma_0(s)-\gamma_0(t)|\le|s-t|$; $\gamma_0$ is $1$-Lipschitz.
Lipschitz maps do not increase Hausdorff dimension, so
$\dim_H(E_0)\le\dim_H([0,1])=1$.

*Lower bound.* The orthogonal projection $\pi_z(x,y,z)=z$ is
$1$-Lipschitz and $\pi_z(E_0)=[0,1/\sqrt2]$, an interval of Hausdorff
dimension $1$. Hence $\dim_H(E_0)\ge 1$.

Therefore $\dim_H(E_0)=1<5/2$ (indeed $\mathcal H^1(E_0)>0$ since
$\mathcal H^1(\pi_z(E_0))=1/\sqrt2\le\mathcal H^1(E_0)$).

## 5. $E_0$ is a torsion Kakeya set

Let $u\in S^2$ be arbitrary. Pick $R\in SO(3)$ with $R(e_1)=u$
(complete $u$ to an oriented orthonormal basis). Define
$\gamma_u:=R^{-1}\circ\gamma_0$. By Section 2,
$\gamma_u\in\mathcal F_{\rm tor}$ (unit speed, $C^\infty$, same
$\kappa,|\tau|$ since derivatives are multiplied by the fixed orthogonal
matrix $R^{-1}$). With translation $x=0$,

$$x+R(\gamma_u([0,1]))=R(R^{-1}(\gamma_0([0,1])))=E_0\subset E_0.$$

Thus the required $R,x,\gamma$ exist for every $u$. So $E_0$ is a
torsion Kakeya set in the exact sense stated.

## 6. Conclusion

$E_0$ is compact, contains (indeed equals, up to the vacuous
rotation/translation) a torsion-nondegenerate arc in every direction in
the literal sense of the definition, and has
$\dim_H(E_0)=1<5/2$. Hence it is false that every torsion Kakeya set
satisfies $\dim_H\ge 5/2$.

*Remark on formulation.* The falsity is structural to the quantifier
order as written: because $\gamma$ is existentially quantified after
$R$, the condition $R(e_1)=u$ imposes no constraint on the placed arc.
A reformulation fixing the arc's initial tangent (e.g.\ requiring
$\gamma'(0)=e_1$) would be a genuinely different, non-vacuous problem
not addressed here.
