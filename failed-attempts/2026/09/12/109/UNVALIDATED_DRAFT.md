# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Orthogonal extra-twisted matching for the named involutive semi-Fano pair — impossibility proof

## 1. The named ordinary pair and its K3 lattices

Let $Y_+= {\mathbb P}^3$, $C_+\subset Y_+$ a smooth complete-intersection curve of
type $(2,3)$ (degree $6$, genus $4$), and $Z_+=Bl_{C_+}Y_+$.
Let $Y_-=Q^3\subset{\mathbb P}^4$ a smooth quadric, $C_-\subset Y_-$ a smooth conic
(degree $2$, genus $0$), and $Z_-=Bl_{C_-}Y_-$.
Both are semi-Fano; let $\Sigma_\pm\subset Z_\pm$ be smooth anticanonical K3 divisors.

Write $H$ for the hyperplane pullback and $E$ for the exceptional divisor.
$K_Z=\pi^*K_Y+E$, $-K_Z=-\pi^*K_Y-E$ up to sign conventions, and for a blow-up
along a curve $C$, $\deg N_{C/Y}=2g(C)-2-K_Y\!\cdot\! C$ and $E^3=-\deg N_{C/Y}$.

Plus side: $-K_{Y_+}\!\cdot\! C_+=4\cdot 6=24$, $2g-2=6$, so $\deg N=30$,
$E^3=-30$, $H^3=1$, $H\!\cdot\! E^2=-H\!\cdot\! C=-6$.
With $-K_{Z_+}=4H-E$, $(-K_{Z_+})^3=64-48+6=22$.
On $\Sigma_+\sim -K_{Z_+}$, with $h=H|_{\Sigma_+}$, $e=E|_{\Sigma_+}$:
$$h^2=H^2\!\cdot\!(-K_{Z_+})=4,\quad h\!\cdot\! e=H\!\cdot\! C_+=6,\quad
  e^2=E^2\!\cdot\!(-K_{Z_+})=4(H\!\cdot\! E^2)-E^3=-24+30=6.$$
Hence the (full) restriction lattice is
$$N_+=\begin{pmatrix}4&6\\6&6\end{pmatrix},\quad \det N_+=-12,\quad
  N_+^*/N_+\cong {\mathbb Z}_2\times{\mathbb Z}_6,$$
even, rank 2, signature $(1,1)$. The anticanonical sublattice
$\langle -K|_{\Sigma_+}\rangle=\langle 4\rangle$ has discriminant ${\mathbb Z}_4$.

Minus side: $H^3=2$ on $Q^3$, $-K_{Y_-}=3H$, $-K_{Y_-}\!\cdot\! C_-=6$,
$2g-2=-2$, so $\deg N=4$, $E^3=-4$, $H\!\cdot\! E^2=-2$.
With $-K_{Z_-}=3H-E$, $(-K_{Z_-})^3=54-12-2=40$.
On $\Sigma_-\sim -K_{Z_-}$:
$$h^2=3H^3=6,\quad h\!\cdot\! e=H\!\cdot\! C_-=2,\quad
  e^2=3(H\!\cdot\! E^2)-E^3=-6+4=-2.$$
Hence
$$N_-=\begin{pmatrix}6&2\\2&-2\end{pmatrix},\quad \det N_-=-16,\quad
  N_-^*/N_-\cong {\mathbb Z}_2\times{\mathbb Z}_8,$$
even, rank 2, signature $(1,1)$. The anticanonical sublattice is $\langle 6\rangle$
with discriminant ${\mathbb Z}_6$.

Both $N_\pm$ are even. The orthogonal pushout $W=N_+\perp N_-$ has rank 4,
signature $(2,2)$; $2\,\mathrm{rk}\,W=8\le 22$, so by Nikulin, Theorem 1.12.4
(cf. Nordstrom Theorem 6.6), $W$ admits a primitive embedding into the K3 lattice
$L=U^3\oplus E_8^2$, unique up to $O(L)$. Thus **ordinary** orthogonal
$\pi/2$ matching is lattice-unobstructed. The obstruction below is strictly
involutive/extra-twisted.

## 2. Fixed-locus lemma: mixed "points + curve" is impossible for a K3 involution

Lemma (holomorphic Lefschetz / local eigenvalues).
Let $\iota$ be a holomorphic involution of a K3 surface $\Sigma$.
At a fixed point, $d\iota$ has eigenvalues $(\pm1,\pm1)$.
$(-1,-1)$ gives $\det=+1$ on $T$ and hence acts trivially on $K_\Sigma$
(symplectic, isolated fixed point); $(+1,-1)$ gives $\det=-1$
(non-symplectic, fixed curve through the point). A connected component of
$\mathrm{Fix}(\iota)$ is therefore either an isolated point (symplectic type)
or a smooth curve (non-symplectic type). In particular:
symplectic $\Rightarrow$ $8$ isolated points only (Nikulin);
non-symplectic with nonempty fixed locus $\Rightarrow$ disjoint smooth curves
only, no isolated points. A "non-symplectic involution with isolated fixed
points plus a fixed curve" cannot exist on any K3.

## 3. Nordstrom involution-block structure never gives the required $\tau_\pm$

Nordstrom (arXiv:1809.09083) Definition 2.7, Sect.~1.1--2.2, Remark 2.12:
an involution block $(Z,f,\Sigma,\tau)$ has $\tau$ holomorphic with $\Sigma$ a
connected component of $\mathrm{Fix}(\tau)$; $\tau$ covers the base involution
$(z\!:\!w)\mapsto(z\!:\!-w)$, so $\mathrm{Fix}(\tau)\subseteq\Sigma\cup\Sigma'$
for the two preserved fibres. Hence $\tau|_{\Sigma}=\mathrm{id}$ (a fixed
surface, not a non-symplectic action), and $\mathrm{Fix}(\tau)\cap\Sigma'$ is
the fixed locus of a non-symplectic K3 involution: smooth curves only, no
isolated points. No Definition-2.7 block has isolated fixed points, and $\tau$
never acts non-symplectically on the asymptotic K3 $\Sigma$ itself.

Therefore the target's data — "Nordstrom extra-twisted involution $\tau_\pm$
acting non-symplectically on the (Picard-rank-2) K3 $\Sigma_\pm$ with isolated
fixed points plus a fixed curve as specified by the Brandhorst fixed-lattice
data" — is internally contradictory: no such $\tau_\pm$ exists on the named
$Z_\pm$ (indeed on any building block of this type).

## 4. Nikulin 2-elementary lattice obstruction

Nikulin's classification (Sect.~5.1 of Nordstrom): the fixed lattice $N$ of a
non-symplectic K3 involution is primitive 2-elementary, i.e.
$N^*/N\cong({\mathbb Z}_2)^a$, equivalently $2N^*\subseteq N$ and
$|\disc N|$ is a power of $2$.

Verification (script `output/artifacts/verify_lattices.py` reproduces this):
$2N_+^{-1}=\frac{2}{-12}\mathrm{adj}(N_+)$ and $2N_-^{-1}$ are non-integral,
so $2N_\pm^*\not\subseteq N_\pm$; $N_+^*/N_+\cong{\mathbb Z}_2\times{\mathbb Z}_6$
has 3-torsion; $N_-^*/N_-\cong{\mathbb Z}_2\times{\mathbb Z}_8$ has an element
of order 8. The rank-1 sublattices $\langle4\rangle$ (${\mathbb Z}_4$) and
$\langle6\rangle$ (${\mathbb Z}_6$) likewise fail $d\mid2$. Hence $N_\pm$
(and their anticanonical sublattices) cannot be fixed lattices of any
non-symplectic K3 involution. Additionally $N_+$ represents no $2$:
$2x^2+6xy+3y^2=1$ is impossible mod 3, excluding even the rank-1
$\langle2\rangle$ fixed sublattice there. This is the precise
Nikulin lattice-embedding obstruction.

## 5. Theorem (complete negative answer to the target)

There is no hyper-Kahler rotation $r:\Sigma_+\to\Sigma_-$ intertwining putative
$\tau_\pm$ as specified and realizing orthogonal ($\pi/2$) extra-twisted gluing
from this pair, because the required $\tau_\pm$ do not exist (Sections 3--4).
A fortiori there is no closed extra-twisted connected-sum $G_2$-manifold with
exponentially small torsion from these data. Secondary obstruction: square
$\pi/2$ gluing with $b_+=b_-=1$ on both sides has $\pi_1\cong{\mathbb Z}_2$
(Nordstrom Sect.~1.3), so it would not yield the claimed simply-connected
closed sum in any case.

## 6. Separation of proof, computation, and conjecture

Proved above: ordinary intersection numbers and discriminants; fixed-locus
dichotomy; Def-2.7 fixed-point structure; 2-elementary failure. Computed
evidence: Smith forms $(2,6)$, $(2,8)$ and non-integrality of $2N^{-1}$
(script output). Conjecture/uncertainty: none needed for the negative answer;
we make no claim about other (non-named, non-involutive, or different-angle)
matchings, and the ordinary (non-extra-twisted) rectangular TCS channel for
this pair remains lattice-unobstructed and is left open.
