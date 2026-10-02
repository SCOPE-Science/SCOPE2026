# Homotopy invariance beyond row-finite higher-rank graphs: KK-equivalence for twisted relative algebras

## Context

Homotopy invariance for cocycle twists is known in several operator-algebraic settings. Gillaspy proved K-theory invariance for row-finite source-free higher-rank graphs, while Bönicke proved K-theory invariance for homotopies of twists on suitable ample groupoids. Finitely aligned higher-rank graphs require the boundary-path groupoid and relative Cuntz--Krieger relations.

## Statement

Let \(\Lambda\) be a countable finitely aligned \(k\)-graph, let
\(\mathcal E\subset FE(\Lambda)\) be satiated, and let
\(\{c_t\}_{t\in[0,1]}\) be a pointwise-continuous family of normalized
categorical \(2\)-cocycles:
\(t\mapsto c_t(\lambda,\mu)\) is continuous for every composable pair.

Then the pooled cocycle
\[
\widetilde c(\lambda,\mu)(t)=c_t(\lambda,\mu)
\]
defines a separable nuclear \(C([0,1])\)-algebra
\(C(\Lambda,\mathcal E,c_\bullet)\) whose fiber at \(t\) is canonically
\[
C(\Lambda,\mathcal E,c_\bullet)_t
\cong C^*(\Lambda,c_t;\mathcal E).
\]
Every evaluation
\[
\operatorname{ev}_t:
C(\Lambda,\mathcal E,c_\bullet)
\longrightarrow C^*(\Lambda,c_t;\mathcal E)
\]
is a KK-equivalence. Consequently
\[
[\operatorname{ev}_0]^{-1}\otimes
[\operatorname{ev}_t]
\]
is a KK-equivalence between the endpoint twisted relative algebras and carries the
vertex class \([s_v^{c_0,\mathcal E}]\) to
\([s_v^{c_t,\mathcal E}]\) in \(K_0\).

This is a KK-equivalence statement; no stable-isomorphism conclusion is asserted.

## Proof architecture

### 1. Pooled relative algebra and fibers

The pointwise-continuous cocycle family is a normalized
\(C([0,1],\mathbb T)\)-valued categorical cocycle. The universal
\(C([0,1])\)-linear twisted relative Cuntz--Krieger family gives the total
algebra. Quotienting by \(C_0([0,1]\setminus\{t\})\) produces a
\((\Lambda,c_t;\mathcal E)\)-family. The twisted relative gauge-invariant
uniqueness theorem identifies this quotient with
\(C^*(\Lambda,c_t;\mathcal E)\).

### 2. Boundary-groupoid realization

Let \(G_{\mathcal E}\) be the relative boundary-path groupoid. The categorical
cocycle construction yields a groupoid cocycle \(\sigma_{c_t}\). On every
basic groupoid chart, the formula for \(\sigma_{c_t}\) is a finite product of
finitely many categorical cocycle values, so pointwise continuity in \(t\)
gives joint continuity of
\[
((g,t),(h,t))\mapsto \sigma_{c_t}(g,h)
\]
on \(G_{\mathcal E}\times[0,1]\). Hence the total algebra agrees fiberwise, and
therefore as a \(C([0,1])\)-algebra, with the twisted groupoid algebra of this
homotopy.

### 3. K-theory and KK

The relative boundary groupoid is second countable, ample and amenable in the
standard finitely aligned setting. Bönicke's homotopy theorem for twists on
ample groupoids satisfying Baum--Connes with coefficients gives that each
evaluation induces an isomorphism on K-theory. Amenability gives the required
Baum--Connes/UCT input in this setting.

The fiber algebras are nuclear UCT algebras by the finitely aligned twisted
relative theory, and the total amenable groupoid algebra is likewise in the
bootstrap/UCT class. The mapping cone of an evaluation therefore lies in the
bootstrap class. Since the evaluation is a K-isomorphism, its mapping cone has
zero K-theory; the UCT then makes the cone KK-contractible. Thus the evaluation
class is invertible in KK.

Vertex preservation follows from the common vertex projection in the total
\(C([0,1])\)-algebra: both evaluations are images of the same K-theory class.

## Originality and value

The individual ingredients are established results: relative finitely aligned
twisted algebras, groupoid realization, Bönicke's homotopy K-theory theorem,
and the UCT mapping-cone criterion. The contribution is therefore an
incremental synthesis rather than a new operator-algebraic mechanism. Its useful
content is that pointwise categorical cocycle homotopies in the finitely aligned
satiated-relative setting fit the groupoid homotopy theorem and that the
resulting K-isomorphism upgrades canonically to KK-equivalence with vertex-class
tracking.

## Reproducibility

`python3 artifacts/pooled_cocycle_check.py` checks a concrete single-vertex
2-graph cocycle family and writes
`artifacts/pooled_cocycle_check_results.json`. This computation only illustrates
the pooled cocycle identity and continuity; it does not verify the cited
operator-algebraic theorems.

## Limitations

The proof depends on the published twisted relative uniqueness/UCT theory,
the categorical-to-groupoid cocycle construction, amenability of the relative
boundary groupoid, Bönicke's homotopy theorem, and the Rosenberg--Schochet UCT.
The scope is countable finitely aligned \(\Lambda\) and satiated
\(\mathcal E\). No claim is made for non-satiated relations, arbitrary
non-ample groupoids, or stable isomorphism of the fibers.

## References

- E. Gillaspy, *K-theory and homotopies of 2-cocycles on higher-rank graphs*, Pacific J. Math. 278 (2015), arXiv:1403.3799.
- C. Bönicke, *K-theory and homotopies of twists on ample groupoids*, J. Noncommut. Geom. 15 (2021), arXiv:1901.09441.
- A. Sims, B. Whitehead, M. Whittaker, *Twisted C*-algebras associated to finitely aligned higher-rank graphs*, arXiv:1310.7656.
