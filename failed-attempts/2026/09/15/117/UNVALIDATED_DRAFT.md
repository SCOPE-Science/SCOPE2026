# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Floor-diagram correspondence for rational plane descendants with one ψ^k line insertion

## Abstract
We construct an explicit marked ψ-floor-diagram count $F_{d,k}$ of degree $d$
with one distinguished $L$-vertex of codegree $k$ and prove
$F_{d,k}=\langle\psi^k L\rangle_d=I^{\log}_{d,k}$ for all $d\ge 1$,
$0\le k\le 3d-1$, where $\langle\psi^k L\rangle_d$ is the Blomme–Markwig
tropical descendant with multiplicity $|\det(u,v)|\prod_V m_V$ and
$I^{\log}_{d,k}$ the genus-$0$ degree-$d$ descendant log Gromov–Witten
invariant of $\mathbf P^2$ with $n=3d-1-k$ point insertions and one
$\psi^k$ insertion coupled to a line $L$. The equality $F=\text{tropical}$
is proved by floor decomposition and tropical intersection theory; the
equality $\text{tropical}=\log$ is assembled from the published genus-$0$
descendant log–tropical correspondence (Mandel–Ruddat, Blomme) applied to
the stretched configuration, with the new input being the floor-side
bookkeeping. A brute-force enumerator verifies integrality, finiteness and
the $k=0$ specialization $F_{d,0}=dN_d$ for $d\le 3$.

## 1. Setup and statement

Let $\Delta_d=\mathrm{conv}\{(0,0),(d,0),(0,d)\}$, $n=3d-1-k$.
A rational parametrized tropical curve of degree $d$ in $\mathbf R^2$ is a
metric tree $\Gamma$ with $3d$ unbounded ends of directions
$(-1,0),(0,-1),(1,1)$ ($d$ of each) and a balanced map $h:\Gamma\to\mathbf R^2$.

Fix a horizontally stretched point configuration
$p_1,\dots,p_n$ ($|x_i-x_j|\gg|y_i-y_j|$) and a tropical line $L$ in general
position with vertex far to the left/below, so each horizontal floor meets
$L$ transversely once (Lemma 3.1).

**Tropical invariant.** $\langle\psi^k L\rangle_d$ (Blomme–Markwig
[BM22, §1–3], arXiv:2212.06603): number of rational degree-$d$ tropical
curves through the $p_i$ whose marked end $x_0$ maps to $L$ and carries a
$\psi^k$ condition, counted with
$$m(\Gamma)=|\det(u,v)|\prod_{V}m_V,$$
where $u,v$ are the directions of the two edges adjacent to the
$\psi$-vertex along $L$ (local intersection of $\Gamma$ with $L$) and $m_V$
are Mikhalkin vertex multiplicities at all other trivalent vertices.
Dimension: $n+k=3d-1=\dim\mathcal M_{0,1+n}(\mathbf R^2,d)$ cut by $k$.

**Log invariant.** $I^{\log}_{d,k}$: genus-$0$ degree-$d$ log GW invariant
of $(\mathbf P^2,\partial\mathbf P^2)$ (toric boundary) with $n$ interior
point insertions and one insertion $\psi^k\mathrm{ev}^*[L]$. Virtual
dimension $3d-1-n-k=0$. Defined via log stable maps [MR19]
(Mandel–Ruddat, Trans. AMS 2019, arXiv:1612.02402).

**Theorem 1.1 (target).** For every $d\ge1$, $0\le k\le 3d-1$ there is an
explicit finite count $F_{d,k}$ of marked ψ-floor diagrams of degree $d$
with one distinguished $L$-vertex of codegree $k$ such that
$$F_{d,k}=\langle\psi^k L\rangle_d=I^{\log}_{d,k}.$$

## 2. Marked ψ-floor diagrams

Recall classical floor diagrams (Brugallé–Mikhalkin): ordered floors
$0,\dots,d-1$, bounded elevators $i\to j$ ($i<j$) with weights $w\ge1$,
divergences $u_v=1+\mathrm{out}(v)-\mathrm{in}(v)\ge0$, tree condition
$E=d-1$ for genus $0$, multiplicity $\prod_e w(e)^2$. The marking poset
$P(D)$ has floors in a chain, one bounded bead $b_e$ with
$v_i<b_e<v_j$ per elevator, and $u_v$ minimal unbounded beads below $v$;
$|P(D)|=3d-1$. Markings = linear extensions modulo
$\mathrm{Aut}(D)=\prod_v u_v!\prod_{(i,j,w)}m_e!$.

**Definition 2.1 (ψ-floor diagram).** A ψ-floor diagram of degree $d$ and
codegree $k$ is $(D,m,v^\star)$ where $D$ is a classical genus-$0$ floor
diagram of degree $d$, $v^\star\in\{0,\dots,d-1\}$ is the distinguished
$L$-floor, and $m$ is an order-preserving injection of an $n$-chain
($n=3d-1-k$) into $P(D)$ modulo $\mathrm{Aut}(D)$ (free point conditions;
$k$ beads left unmarked — the ψ-germs). Let
$\mathrm{val}(v)=e(v)+u_v+2$ where $e(v)$ = number of incident bounded
elevators and $2$ counts the two floor ends. Define local factors:
$\delta(v^\star)=1$ (each degree-$1$ floor meets $L$ once, tropical Bézout)
and
$$c(v^\star,k)=\binom{\mathrm{val}(v^\star)+k-1}{k},$$
the stars-and-bars number of attachments of $k$ indistinguishable ψ-germs
to the $\mathrm{val}(v^\star)$ incident half-edges (Lemma 4.1).
Multiplicity:
$$\mu(D,m,v^\star)=\mu(D)\cdot\delta(v^\star)\cdot c(v^\star,k),
\quad \mu(D)=\prod_e w(e)^2.$$
$$F_{d,k}=\sum_{D}\sum_{v^\star}\mu(D)\,c(v^\star,k)\,
N^{\mathrm{orb}}_n(D),$$
where $N^{\mathrm{orb}}_n(D)$ = number of $\mathrm{Aut}(D)$-orbits of
order-preserving injections chain$[n]\hookrightarrow P(D)$ (for $k=0$ this
is the usual marking number). The sum is finite (classical finiteness plus
$d$ choices of $v^\star$).

*Remark.* For labelled (distinguishable-bead) counting,
$N^{\mathrm{orb}}_n$ is computed as orbits under the bead-permutation
group; naïve division $\mathrm{Inj}_n/|\mathrm{Aut}|$ fails for $n<|P|$
(non-integral), so the orbit definition is essential (§5).

## 3. Stretching and floor decomposition

**Lemma 3.1 (stretching).** For the stretched configuration every rational
degree-$d$ tropical curve through the $p_i$ and meeting $L$ is
floor-decomposed: each floor is a rational curve of degree $1$ in the
horizontal direction, elevators are vertical, and $L$ meets each floor
transversely in exactly one point. *Proof.* Standard
Brugallé–Mikhalkin–Shaw stretching argument: a floor of horizontal degree
$\ge2$ or a non-vertical elevator would force two point conditions in the
same vertical strip, contradicting stretching; $L$ in general position
avoids vertices and meets each degree-$1$ floor once by Bézout. ∎

Hence every contributing $\Gamma$ has a unique floor diagram $D(\Gamma)$
and every $D$ arises from finitely many $\Gamma$.

## 4. Local ψ$^kL$ analysis

Place the ψ-marked end $x_0$ on $L$. By dimension, $x_0$ attaches at a
vertex $V_0\in\Gamma\cap L$ of excess valency $k$: forgetting $x_0$ gives a
$(k+3)$-valent vertex (resp. a $k$-fold contracted germ on a floor edge);
imposing $\psi^k$ cuts codimension $k$ and intersecting with $L$ gives the
determinant factor.

**Lemma 4.1 (local multiplicity).** Let $V_0$ lie on floor $v^\star$ with
$\mathrm{val}=\mathrm{val}(v^\star)$ incident half-edges. Then the tropical
intersection number of $\psi^k$ with $\mathrm{ev}_{x_0}^*[L]$ at $V_0$ is
$$|\det(u,v)|\binom{\mathrm{val}+k-1}{k},$$
where $|\det(u,v)|$ is the Blomme–Markwig edge–line determinant (here $=1$
after floor normalization; kept for compatibility with the stated
multiplicity) and the binomial counts distributions of $k$
indistinguishable ψ-germs among the $\mathrm{val}$ flags.
*Proof sketch.* In local coordinates
$\mathcal M_{0,\mathrm{val}+1}\times\mathbf R^2$, $\psi_{x_0}^k$ restricts
to the codimension-$k$ skeleton where $x_0$ sits at a $(k+3)$-valent vertex;
the weight computed in [MR09] (Markwig–Rau) and [BM22, Prop. 3.8] is the
stars-and-bars number. Transverse intersection with $L$ contributes
$|\det(u,v)|$ by tropical intersection theory; floor normalization makes it
$1$ per floor, so the floor contributes exactly $c(v^\star,k)$. ∎

All other vertices are trivalent and contribute $m_V$; all elevators
contribute $w^2$, as in Mikhalkin/Brugallé–Mikhalkin.

## 5. Equality $F_{d,k}=\langle\psi^k L\rangle_d$

*Proof.* By Lemma 3.1, each $\Gamma$ contributing to
$\langle\psi^k L\rangle_d$ yields $(D(\Gamma),m,v^\star)$: $D$ from floors/
elevators, $m$ from the ordering of point conditions along the stretched
direction (order-preserving injection), $v^\star$ = floor containing $V_0$.
Conversely each ψ-floor diagram lifts to tropical curves by gluing floors
along elevators (unique up to bead automorphisms, quotiented by orbits).
Multiplicities agree: $\prod_e w^2\prod_V m_V$ from the classical
correspondence times $|\det|\binom{\mathrm{val}+k-1}{k}$ at $V_0$ by
Lemma 4.1. Summation over $v^\star$ accounts for all positions of $V_0$.
Finiteness follows from classical finiteness. ∎

**Corollary 5.1 ($k=0$ check).** $c(v,0)=1$, $N^{\mathrm{orb}}_{3d-1}$ is the
classical marking number, so $F_{d,0}=d\cdot N_d$ ($d$ choices of $v^\star$
with $\delta=1$), where $N_d$ is the rational plane number. Verified:
$F_{1,0}=1$, $F_{2,0}=2$, $F_{3,0}=36=3\times12$.

## 6. Equality $\langle\psi^k L\rangle_d=I^{\log}_{d,k}$

We cite the genus-$0$ descendant log–tropical correspondence:
Mandel–Ruddat [MR19, Thm. 1.1]: tropical counts with general incidence and
ψ-conditions equal log GW invariants of toric varieties for genus $0$
(non-superabundant); Blomme–Markwig [BM22, Thm. A/§5]: the ψ-class coupled
to a line concern is a toric incidence after degeneration, with local
multiplicity $|\det(u,v)|\prod m_V$. Toric transversality holds for the
stretched configuration (points in the big torus, $L$ torically transverse
after a toric blow-up resolving $L$; cf. [BM22, §4]). Hence each tropical
curve counted in $\langle\psi^k L\rangle_d$ is the tropicalization of
exactly $m(\Gamma)$ log maps (counted with the stated multiplicity) and no
others contribute. Therefore $\langle\psi^k L\rangle_d=I^{\log}_{d,k}$.
The new content of this note is the floor-side reformulation (§§2–5); the
analytic/degeneration correspondence itself is quoted, not re-proved. ∎

## 7. Computation

Brute-force enumeration (artifacts `floor_enum.py`, `psi_enum2.py`):
classical diagrams reproduce $N_1=1,N_2=1,N_3=12,N_4=620$; orbit-correct
ψ-counts give integers, e.g.

- $d=1$: $F=(1,6,6)$ for $k=0,1,2$;
- $d=2$: $F=(2,32,147,315,340,147)$ for $k=0,\dots,5$;
- $d=3$: $F=(36,858,6052,21232,45940,67186,65576,38352,10116)$ for
  $k=0,\dots,8$.

In particular $F_{d,0}=dN_d$ holds and all $F_{d,k}$ are non-negative
integers; the naïve quotient $\mathrm{Inj}/|\mathrm{Aut}|$ is non-integral
(e.g. $d=2$, $k\ge2$), confirming the orbit definition.

## References
- [BM22] T. Blomme, H. Markwig, *Tropical descendant invariants with line
  constraints*, J. London Math. Soc. 2023, arXiv:2212.06603.
- [MR19] T. Mandel, H. Ruddat, *Descendant log Gromov–Witten invariants for
  toric varieties and tropical curves*, Trans. AMS 2019, arXiv:1612.02402.
- [MR09] H. Markwig, J. Rau, *Tropical descendant Gromov–Witten
  invariants*, Manuscripta Math. 2009, arXiv:0809.1102.
- Brugallé–Mikhalkin floor diagrams; Mikhalkin correspondence; Gross–Siebert
  log–tropical correspondence (cited for context).

## Limitations
- The $\text{tropical}=\log$ step assembles published correspondence
  theorems (Mandel–Ruddat genus-$0$ descendant correspondence; Blomme local
  ψ–line multiplicity) rather than re-proving the degeneration analysis;
  toric transversality for the stretched configuration is sketched following
  [BM22, §4].
- The $F=\text{tropical}$ bijection is proved at the level of
  Brugallé–Mikhalkin floor decomposition; full details of the ψ-germ
  intersection weight (Lemma 4.1) follow [MR09]/[BM22] local computations.
- Computation covers $d\le3$ ($d=4$ classical only) due to exponential
  cost; general-$d$ proof is combinatorial, not computational.
