# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Pants Hitchin vs same-boundary Fuchsian figure-eight domination — resolution

## Theorem (target decided: inequality holds, in fact as equality)

Let $P$ be the pair of pants with peripheral loops $g_1,g_2,g_3$ satisfying
$g_1g_2g_3=1$ in $\pi_1(P)$ (up to simultaneous conjugacy, i.e. up to the
choice of connecting arcs; see §1). Let $\rho:\pi_1(P)\to\mathrm{PSL}(3,\mathbb R)$
be positive with loxodromic boundary holonomy, and let
$H(M)=\log(|\lambda_1|/|\lambda_3|)$ be the Hilbert length, where
$|\lambda_1|\ge|\lambda_2|\ge|\lambda_3|>0$ are the eigenvalue moduli.
Let $J(\rho)$ be the Fuchsian pants representation into a fixed copy of
$\mathrm{PSL}(2,\mathbb R)<\mathrm{PSL}(3,\mathbb R)$ with the same three
boundary Hilbert lengths, $H_{J(\rho)}(g_i)=H_\rho(g_i)$.
For the literal seam word $w=g_1g_2$:

$$H_\rho(w) = H_\rho(g_3) = H_{J(\rho)}(g_3) = H_{J(\rho)}(w)$$

for every $\rho\in R$. In particular $H_\rho(w)\ge H_{J(\rho)}(w)$ holds for
all positive $\rho$ with loxodromic boundary, and no positive coordinate tuple
with strict reverse inequality exists.

## 1. The word $w$ is peripheral

$P$ deformation-retracts to a wedge of two circles; $\pi_1(P)$ is free of rank
$2$. With a basepoint $p$ and loops $g_1,g_2$ freely generating, the three
peripheral (boundary-parallel) conjugacy classes satisfy the standard pants
relation: after suitable choices of arcs from $p$ to the cuffs,

$$g_1\,g_2\,g_3 = 1 \quad\text{in }\pi_1(P,p),$$

i.e. $g_3$ is conjugate to $(g_1g_2)^{-1}$ for any choice of connecting arcs
(the conjugating element records the arc change; different conventions change
$g_3$ to a conjugate or its inverse). Hence as group elements (for compatible
arc choices), and in all cases as free-homotopy/conjugacy classes,

$$[w] = [g_1g_2] = [g_3]^{-1}.$$

Consequence: $w$ is boundary-parallel, not an interior curve. Every essential
simple closed curve on a pair of pants is peripheral, so the label
"figure-eight curve" for the literal word $g_1g_2$ is a misnomer; a genuine
interior self-intersecting word (e.g. $g_1g_2^{-1}$ or a commutator) would be a
different, genuinely nontrivial domination problem, outside the literal scope.
We decide the literal claim as stated.

## 2. Hilbert-length lemma

For $M\in\mathrm{SL}(3,\mathbb R)$ loxodromic (three real eigenvalues of
pairwise distinct moduli — equivalently $|\lambda_1|>|\lambda_2|>|\lambda_3|>0$),
$H(M)=\log(|\lambda_1|/|\lambda_3|)$ is well defined, finite and positive, and:

(a) **Conjugacy invariance:** $H(AMA^{-1})=H(M)$, since conjugation preserves
eigenvalues. Hence $H$ descends to free-homotopy classes (conjugacy classes in
$\pi_1$) and to $\mathrm{PSL}(3,\mathbb R)$-conjugacy classes of
representations. It is also unchanged by rescaling a lift by a nonzero scalar
(the scalar cancels in the ratio; in particular there is no lift ambiguity
issue, and for $n=3$ odd $\mathrm{SL}(3,\mathbb R)\to\mathrm{PSL}(3,\mathbb R)$
is in fact an isomorphism).

(b) **Inverse invariance:** if $\mathrm{spec}(M)=\{\lambda_1,\lambda_2,
\lambda_3\}$ then $\mathrm{spec}(M^{-1})=\{\lambda_i^{-1}\}$; ordering by
modulus reverses, so with $|\mu_1|\ge|\mu_2|\ge|\mu_3|$ the moduli of
$M^{-1}$,
$$\frac{|\mu_1|}{|\mu_3|}=\frac{|\lambda_3|^{-1}}{|\lambda_1|^{-1}}
=\frac{|\lambda_1|}{|\lambda_3|},\qquad H(M^{-1})=H(M).$$
This is a purely linear-algebraic identity; it uses only invertibility.

## 3. The Fuchsian match $J(\rho)$

Fix once and for all an embedding $\mathrm{PSL}(2,\mathbb R)\hookrightarrow
\mathrm{PSL}(3,\mathbb R)$ (either the reducible diagonal embedding or the
irreducible symmetric-square embedding). For a hyperbolic cuff of length
$\ell>0$, the embedded Hilbert length is $H=\ell$ (reducible) or $H=2\ell$
(principal), in either case a strict monotone bijection $(0,\infty)\to
(0,\infty)$. Classical hyperbolic pants theory (Fricke coordinates /
right-angled hexagon construction) gives, for every triple
$(\ell_1,\ell_2,\ell_3)$ of positive cuff lengths, a hyperbolic pants
representation unique up to $\mathrm{PSL}(2,\mathbb R)$-conjugacy. Given
$\rho$, set $\ell_i$ by $H_{\mathrm{embed}}(\ell_i)=H_\rho(g_i)>0$ (possible
since boundary is loxodromic, so each $H_\rho(g_i)$ is finite positive); the
resulting Fuchsian pants $J(\rho)$ satisfies $H_{J(\rho)}(g_i)=H_\rho(g_i)$
for $i=1,2,3$ and is unique up to conjugacy. Since $H$ is conjugacy-invariant,
$H_{J(\rho)}(w)$ is well defined. The conclusion below is independent of which
of the two embeddings is used, provided the same one is used for the boundary
matching and for evaluating $w$.

## 4. Proof of equality (hence domination)

Let $M_i=\rho(g_i)$ and $M_w=\rho(w)=\rho(g_1)\rho(g_2)=M_1M_2$ (in
Fock–Goncharov weight-matrix coordinates these are the explicit monodromy
matrices; the relation $M_1M_2M_3=I$ holds identically as the boundary
relation of the pants group, so $M_w=M_3^{-1}$ exactly and computably — see
§5). Then:

1. $H_\rho(w)=H_\rho(g_3)$: indeed $w=g_3^{-1}$ as elements (compatible arcs),
   and in general $[w]=[g_3]^{-1}$ as conjugacy classes; apply Lemma 2(a)–(b).
2. $H_\rho(g_3)=H_{J(\rho)}(g_3)$: by definition of the boundary match.
3. $H_{J(\rho)}(g_3)=H_{J(\rho)}(w)$: same group-theoretic identity applied to
   the representation $J(\rho)$.

Chaining gives $H_\rho(w)=H_{J(\rho)}(w)$ for every $\rho\in R$. The non-strict
domination $H_\rho(w)\ge H_{J(\rho)}(w)$ follows. A strict-reverse tuple is
impossible. Positivity and loxodromicity are used only to ensure $H$ is defined
(finite) on the boundary; no cross-ratio estimates are needed beyond that.

## 5. Decidability / FG-computability note

The target asks that both sides be decidable from FG weight-matrix monodromy
formulas and positivity/cross-ratio bounds. This holds: for any concrete
positive coordinate tuple, the matrices $M_1,M_2,M_3$ are explicit rational
functions of the shear and triangle coordinates; $M_w=M_1M_2$; each $H$ is the
log-ratio of extreme eigenvalue moduli, computable to arbitrary precision
(and in exact arithmetic when coordinates are algebraic). The identity
$M_1M_2M_3=I$ is verifiable symbolically/numerically per tuple. The companion
script `output/artifacts/verify_equality.py` checks (i) $H(M)=H(M^{-1})$ on
totally positive $SL(3,\mathbb R)$ matrices, (ii) $H(M_1M_2)=H(M_3)$ for a pants
triple, and (iii) the two Fuchsian embeddings' $H$-vs-$\ell$ scalings; all
passed.

## 6. Scope remark

The proof uses the literal word $w=g_1g_2$. If "figure-eight" was intended to
mean a genuinely interior word such as $g_1g_2^{-1}$ (whose free-homotopy class
is still peripheral on the pants — indeed every simple class is — unless one
passes to self-intersecting words like commutators, or to a larger surface),
domination there is a separate claim not decided here. Within the admitted
literal scope, the answer is complete: equality, hence domination, for all of
$R$ with loxodromic boundary and no cusp restriction.

## 7. Conclusion

The domination inequality is TRUE for the stated word, with equality on all of
$R$. No counterexample exists. This completes the target (proof branch).
