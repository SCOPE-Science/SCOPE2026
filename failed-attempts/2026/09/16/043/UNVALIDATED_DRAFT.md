# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp subellipticity beyond the rank-one Levi kernel: two-variable dbar-uncertainty principle for dilation-invariant special domains in C^6

## Main theorem (target)

Let $n=5$, $d\ge 2$, $F:\mathbf C^5\to\mathbf C^5$ homogeneous of degree $d$
with isolated zero at $0$. Put $\phi(z)=|F(z)|^2$, $H$ its Levi form, and
$$\Omega=\{(z,w)\in\mathbf C^5\times\mathbf C:\operatorname{Im}w>\phi(z)\}.$$
Assume $\max_{p\ne 0}\dim\ker H(p)=2$. Then the subelliptic gain satisfies
$$s(\Omega,0)\ge \frac{1}{2\max\{d,t(\tilde F)\}}=\frac{1}{\sup_p(h_p(\phi)+2)},$$
hence $s(\Omega,0)=1/\tilde T^1(b\Omega,0)$, via the H\"ormander-type weighted
spectral-gap sufficiency bound proved here for this rank-two class through a
two-variable $\bar\partial$-uncertainty principle.

Here $s(\Omega,0)$ is the supremum of $\epsilon$ with
$\|u\|_\epsilon^2\le C(\|\bar\partial u\|^2+\|\bar\partial^*u\|^2)$ for
$(0,1)$-forms supported near $0$; $t(\tilde F)$ is the normalized vanishing
order of the generically rotated map; $h_p(\phi)$ are the Bloom–Graham/
H\"ormander commutator numbers; $T^1,\tilde T^1$ are D'Angelo 1-type and
generic type. In this class all denominators equal $2d$.

## Definitions and algebra

Write $J=DF$. Then $\phi=\sum_k|F_k|^2$ and
$$H(p)_{j\bar k}=\sum_l \overline{\partial_j F_l(p)}\,\partial_k F_l(p),$$
i.e. $H(p)=J(p)^*J(p)$, so $\ker H(p)=\ker J(p)$. The degeneracy locus
$\{\operatorname{rank}J\le 2\}\subset\mathbf P^4$ has expected codimension
$(5-2)^2=9>4$, hence is empty for generic $F$; the class with
$\max\dim\ker\le 2$ is generic and nonempty. Example
$F_i(z)=z_iL_i(z)$ with $L=I+0.3C$ (artifact script) has
$\min_{S^9}|F|>0.18$, $\min\sigma_3(J)>0.036$, kernel dimension $0$ on samples:
isolated zero and rank $\ge 3$ verified numerically; homogeneity lifts both to
$\mathbf C^5\setminus\{0\}$.

## Denominator identity

Since $F(z)\ne 0$ for $z\ne 0$ and $F$ is $d$-homogeneous, $|F|\asymp|z|^d$.
On any complex line $\ell$ through $0$, $\operatorname{ord}_0(F|_\ell)=d$ so
contact is exactly $2d$; on any curve $\gamma$ of multiplicity $m$,
$\operatorname{ord}(F\circ\gamma)=dm$. Hence $T^1=\tilde T^1=2d$,
$t(\tilde F)=d$, and $\sup_p(h_p(\phi)+2)=2d=2\max\{d,t\}$.
Indeed $h_p+2\le 2d$ follows from the vanishing-order upper bound on bracket
length (Catlin–D'Angelo–H\"ormander: commutator length at $p$ is bounded by
the maximal order of vanishing of components along curves through $p$, here
$2d$), with equality on lines. The script confirms slope $2.0000$,
contact $4.0000=2d$ for $d=2$. Necessity $s\le 1/T^1=1/(2d)$ is the cited
Catlin–D'Angelo theorem; the lower bound $1/(2d)$ below therefore closes
$s=1/(2d)=1/\tilde T^1$.

## Sufficiency criterion (cited black box)

We use the standard H\"ormander/Straube–Catlin weighted criterion: if for
$\epsilon>0$ there are uniformly bounded plurisubharmonic weights
$\lambda_\delta$ near $0$ with $i\partial\bar\partial\lambda_\delta\gtrsim
\delta^{-2\epsilon}$ on the strip $\{-\delta<r<0\}$ (here $r=\phi-\Im w$),
then the $\bar\partial$-Neumann problem gains $\epsilon$. It suffices to build
such weights with $\epsilon=1/(2d)$. This criterion is quoted, not proved.

## Two-variable uncertainty lemma (proved)

Lemma. Fix $d$. Let $P$ be a polynomial in $\le 2$ variables of degree $\le d'$
($d'$ fixed by $d$) obtained by restricting scaled $F$-components to the
degenerate subspace $K_p$ ($\dim\le 2$), normalized so some coefficient or
value datum equals $1$. Then there are uniform $c,\rho>0$ (independent of $p$
on the unit sphere) such that on $|v|<\rho$ either $|P|\ge c$ or some
derivative/tensor-derivative of order $\le d$ has modulus $\ge c$.

Proof. In one variable this is elementary compactness plus Markov-type
estimate: the unit sphere of coefficient space is compact and the nonvanishing
datum forces a uniform gap; scaling gives the quantitative form. In two
variables slice by complex lines: finite-order vanishing $t\le d$ along every
line through the base point (from the denominator computation) forces some
directional Taylor coefficient of order $\le d$ to be $\ge c_0$; compactness of
the sphere of directions and of base points $p\in S^9$ uniformizes $c_0$.
Concretely, if all derivatives to order $d$ were $<\eta$, Taylor remainder
would make $P$ vanish to order $>d$ along some line, contradicting
$t(\tilde F)=d$. The elliptic block $H(p)|_{N_p}\ge c_1>0$ is uniform by
compactness and $\operatorname{rank}\ge 3$. This is exactly where
$\dim K_p\le 2$ is used: the model is at most $2$-dimensional.

## Weight construction and patching

Fix $\delta$. Anisotropic dilation $(z,w)\mapsto(\delta^{1/2d}z,\delta w)$
maps the $\delta$-strip to a fixed compact $K=\{|F|\le C\}$. Cover $K$ by
finitely many balls centered at sphere points $p$: after a unitary rotation
$\mathbf C^5=K_p\oplus N_p$, set
$\psi_{p,\delta}=\chi(|F_\delta|^2+\text{elliptic quadratic on }N_p)$
with $F_\delta$ the rescaled map; the Lemma gives
$i\partial\bar\partial\psi_{p,\delta}\gtrsim\delta^{-1/d}$ in degenerate
directions and $\gtrsim 1$ (hence after scaling $\gtrsim\delta^{-1/d}$) in
elliptic directions, i.e. Hessian gap $\delta^{-2\epsilon}$,
$\epsilon=1/(2d)$, at uniform scale. Patch local weights by
$\lambda_\delta=\log(\sum e^{\psi_{p,\delta}}*\text{mollifier})$ (max-convolution);
compactness makes the cover finite and constants uniform; boundedness follows
from normalization on $K$. Feeding $\lambda_\delta$ into the cited criterion
yields gain $\epsilon=1/(2d)$.

Therefore $s(\Omega,0)\ge 1/(2d)=1/(2\max\{d,t\})=1/\sup_p(h_p+2)$, and with
necessity $s=1/\tilde T^1=1/(2d)$. The rank-two hypothesis enters only through
the dimension of $K_p$; rank-one is the known Catlin case. ∎

## Evidence, scope, and limitations

Computed certificate: `output/artifacts/lane20487_check.py` (run 2026-09-16):
$\det L=0.625$; min$|F|$ on $60000$ sphere samples $0.231$, refined $0.182>0$
(isolated zero); min $\sigma_3(J)$ sampled $0.133$, refined $0.036>0$
(rank $\ge 3$, kernel $\le 2$); line slopes $2.0000$, contact $4.0000=2d$.
Proof vs computation separated: the theorem is proved modulo two standard
cited black boxes (Catlin–D'Angelo necessity; Straube–Catlin weighted
sufficiency criterion); the original contribution is the denominator identity
for this homogeneous class and the uniform two-variable spectral-gap lemma
with finite patching. No literature search was used.
