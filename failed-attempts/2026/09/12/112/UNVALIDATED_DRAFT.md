# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Rigid S¹×S² associative from the named mixed TCS gluing pair — impossibility via adjunction/intersection

## Abstract

We answer the stated question in the negative by proving the gluing data
cannot exist. A smooth rational curve with normal bundle
$\mathcal{O}(-1)\oplus\mathcal{O}(-1)$ in a smooth 3-fold satisfies
$-K\cdot C = 0$, hence has homological intersection $0$ with any
anticanonical divisor. It therefore cannot meet a (complex) anticanonical K3
divisor transversely in 2 points, where the local contributions are $+1$
each. Hence the curve $C_{+}$ in the hypothesis does not exist in any
semi-Fano building block, the glued class $A$ from such a pair is undefined,
and no closed embedded rigid associative $P \cong S^{1}\times S^{2}$ arises
by the stated Bera transverse-gluing route. This is an intersection-number
obstruction of exactly the kind the target allows.

## 1. Setup

Let $Y$ be a smooth complex 3-fold and $\Sigma \subset Y$ a smooth divisor
with $[\Sigma] = c_{1}(Y) = [-K_{Y}]$ in $H^{2}(Y;\mathbb{Z})$ (the
anticanonical/K3 setting of TCS building blocks; the same holds with
$\mathbb{Q}$-coefficients). Let $C \cong \mathbb{P}^{1} \subset Y$ be a smooth
rational curve with normal bundle $N_{C/Y} \cong
\mathcal{O}_{\mathbb{P}^{1}}(-1)\oplus\mathcal{O}_{\mathbb{P}^{1}}(-1)$.

## 2. Lemma 1 (adjunction degree)

$\deg N_{C/Y} = c_{1}(Y)\cdot C - 2$. In particular, if
$N_{C/Y} \cong \mathcal{O}(-1)\oplus\mathcal{O}(-1)$ then
$c_{1}(Y)\cdot C = 0$ and hence $\Sigma\cdot C = 0$ homologically for any
$\Sigma \in |-K_{Y}|$.

*Proof.* From $0 \to T_{C} \to T_{Y}|_{C} \to N_{C/Y} \to 0$ take degrees:
$\deg T_{Y}|_{C} = c_{1}(Y)\cdot C$, $\deg T_{C} = \deg T_{\mathbb{P}^{1}} =
2$. Hence $\deg N_{C/Y} = c_{1}(Y)\cdot C - 2$. For
$\mathcal{O}(-1)\oplus\mathcal{O}(-1)$, $\deg N = -2$, so
$c_{1}(Y)\cdot C = 0$. Since $[\Sigma]=c_{1}(Y)$, $\Sigma\cdot C = 0$. ∎

## 3. Lemma 2 (positivity of complex transverse intersections)

If a holomorphic curve $C$ meets a complex divisor $\Sigma$ transversely at
$p$, the local homological intersection multiplicity is $+1$. Hence two
distinct transverse intersection points contribute $+2$, and any further
(complex) intersections contribute nonnegatively, so $\Sigma\cdot C \ge 2$.

*Proof.* In holomorphic coordinates with $\Sigma = \{z_{1} = 0\}$ and $C$
the $z_{1}$-axis, both with complex orientations, the real oriented
intersection is $+1$ (complex subspaces intersect positively). Summing over
intersection points gives the homological pairing. ∎

## 4. Theorem (stated $C_{+}$ does not exist; target answered negatively)

There is no smooth rational curve $C_{+} \subset Y_{+}$ with
$N_{C_{+}/Y_{+}} \cong \mathcal{O}(-1)\oplus\mathcal{O}(-1)$ meeting the
anticanonical K3 divisor $\Sigma_{+}$ transversely in 2 points, in any smooth
building block $Y_{+}$ with $\Sigma_{+} \in |-K_{Y_{+}}|$. The same holds for
any blow-up model (e.g. the stated blow-up of $\mathbb{P}^{3}$) as long as
$\Sigma_{+}$ represents $c_{1}$.

*Proof.* Lemma 1 gives $\Sigma_{+}\cdot C_{+} = 0$. Lemma 2 gives
$\Sigma_{+}\cdot C_{+} \ge 2$ from the two transverse meetings. Contradiction.
∎

### Corollary (resolution of the target question)

The Bera transverse-gluing data $(C_{+}, C_{-}, r)$ posited in the target
cannot be formed: $C_{+}$ as specified does not exist. Consequently the glued
integral class $A \in H_{3}(M;\mathbb{Z})$ from such a pair is undefined, and
a fortiori no closed embedded rigid associative $3$-fold
$P \cong S^{1}\times S^{2}$ calibrated by the glued closed $G_{2}$-structure
(and its torsion-free perturbation) arises in the class $A$ by the stated
construction. The compound existence claim is therefore false. This
constitutes a complete negative answer via intersection-number obstruction,
as expressly permitted by the target ("a proof that no closed associative
represents $A$ via volume-bound, intersection-number, or deformation-index
obstruction").

## 5. Remarks and scope

- The argument is independent of the specific centres blown up, of the
  perpendicular Donaldson matching $r$, and of the analysis of $C_{-}$: the
  holomorphic piece alone is already impossible. We do not need to evaluate
  the special Lagrangian cylinder.
- ACyl rigid cylinders meeting $\Sigma$ twice do occur, but their compact
  normal degree is $0$ (e.g. $\mathcal{O}\oplus\mathcal{O}$), not $-2$; the
  obstruction is specific to the $(-1,-1)$ hypothesis.
- This does not prove the TCS manifold $M$ contains no associative at all,
  nor does it rule out associatives from different gluing data; it refutes
  exactly the stated configuration and class.
- No computation beyond integer arithmetic ($-2 + 2 = 0 \ne 2$) is required;
  the proof is self-contained deduction from the adjunction exact sequence
  and positivity of complex intersections.
