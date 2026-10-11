# Exact descent filtration in the Zhang cocycle span
## Finding
Let \(\alpha=\alpha_3^1\), and let \(\beta_1,\beta_2,\beta_3\) be the new knot-space \(1\)-cocycles studied by Zhang.

Define the integral submodule
\[
L_{\mathbb Z}
=
\operatorname{span}_{\mathbb Z}
\{[\alpha],[\beta_1],[\beta_2]\}
\subset H^1(\mathcal K_{3,1};\mathbb Z).
\]
Then the submodule of \(L_{\mathbb Z}\) that descends to the space of parametrized closed knots is exactly
\[
\mathbb Z[\beta_1],
\]
and the submodule that descends further to the space of unparametrized oriented closed knots is
\[
0.
\]

Define
\[
L_2
=
\operatorname{span}_{\mathbb F_2}
\{[\bar\alpha],[\bar\beta_1],[\bar\beta_2],[\beta_3]\}
\subset H^1(\mathcal K_{3,1};\mathbb F_2).
\]
Zhang proves that these four classes are linearly independent, so \(L_2\) has dimension \(4\). Every class in \(L_2\) descends to parametrized closed knots. The subspace that descends to unparametrized oriented closed knots is exactly
\[
\operatorname{span}_{\mathbb F_2}\{[\bar\beta_1],[\beta_3]\},
\]
which has dimension \(2\).

Thus the source's positive descent statements are exhaustive inside these natural low-order spans: integrally, only the \(\beta_1\)-axis survives the first quotient and nothing in the three-generator span survives the second; modulo \(2\), the first quotient imposes no restriction and the second leaves precisely the \(\bar\beta_1,\beta_3\) plane.

## Assumptions and scope
Here \(\mathcal K_{3,1}\) is the long-knot space used by the source. “Parametrized closed knots” means \(\operatorname{Emb}(S^1,S^3)\). “Unparametrized oriented closed knots” means
\[
\operatorname{Emb}(S^1,S^3)/\operatorname{Diff}^+(S^1).
\]
The result classifies descent only inside the displayed source-generated submodules; it does not determine the full first cohomology of any of these knot spaces.

The bars denote reduction modulo \(2\). The source proves that
\[
[\bar\alpha],\ [\bar\beta_1],\ [\bar\beta_2],\ [\beta_3]
\]
are linearly independent over \(\mathbb F_2\).

## Proof
Zhang's descending criterion says that a class \(\xi\in H^1(\mathcal K_{3,1};R)\), for a commutative ring \(R\), descends to parametrized closed knots exactly when
\[
2\,\xi(\operatorname{Rot}(f))=0
\]
for every long knot \(f\). It descends further to unparametrized oriented closed knots exactly when, in addition,
\[
\xi(\operatorname{Roll}_0(f))+\xi(\operatorname{Rot}(f))=0
\]
for every \(f\).

For the three integral classes, the source gives
\[
\alpha(\operatorname{Rot}(f))=v_2(f),\qquad
\beta_1(\operatorname{Rot}(f))=0,\qquad
\beta_2(\operatorname{Rot}(f))=-v_3(f).
\]
Take
\[
\xi=a[\alpha]+b[\beta_1]+c[\beta_2]\in L_{\mathbb Z}.
\]
The first descent condition becomes
\[
2\bigl(a\,v_2(f)-c\,v_3(f)\bigr)=0
\]
for every \(f\). The source's table gives
\[
(v_2(4_1),v_3(4_1))=(-1,0)
\]
for the figure-eight knot. Hence \(a=0\). It also gives
\[
(v_2(3_1^+),v_3(3_1^+))=(1,1)
\]
for the right trefoil, so then \(c=0\). Conversely, \(\beta_1(\operatorname{Rot})=0\), so every integer multiple of \([\beta_1]\) satisfies the first condition. This proves that the parametrized-descending submodule is exactly \(\mathbb Z[\beta_1]\).

For the second quotient, it remains to test \(b[\beta_1]\). The source formula is
\[
\beta_1(\operatorname{Roll}_0(f))
=
2\left(\binom{v_2(f)}2-v_{4,2}(f)\right).
\]
For \(4_1\), the source gives \(v_2=-1\) and \(v_{4,2}=0\), so
\[
\beta_1(\operatorname{Roll}_0(4_1))
=
2\binom{-1}2
=
2.
\]
Since \(\beta_1(\operatorname{Rot})=0\), the second descent condition forces \(2b=0\) in \(\mathbb Z\), hence \(b=0\). Therefore no nonzero class in \(L_{\mathbb Z}\) descends to the unparametrized oriented closed-knot space.

Now work over \(\mathbb F_2\). The first descent condition is automatic because \(2=0\). For
\[
\eta
=
c_0[\bar\alpha]+c_1[\bar\beta_1]+c_2[\bar\beta_2]+c_3[\beta_3],
\]
the source formulas reduce the second obstruction to
\[
c_0\,v_2(f)+c_2\,v_3(f).
\]
Indeed, \(\alpha(\operatorname{Roll}_0)=6v_3\) vanishes modulo \(2\), both displayed rolling formulas for \(\beta_1,\beta_2\) have an overall factor \(2\), and \(\beta_3\) vanishes on both rotation and rolling loops.

Evaluating on \(4_1\) gives \(c_0=0\). Evaluating next on \(3_1^+\) gives \(c_2=0\). There is no condition on \(c_1,c_3\). Thus the unparametrized-descending subspace is exactly
\[
\operatorname{span}_{\mathbb F_2}\{[\bar\beta_1],[\beta_3]\}.
\]

The same witness pairings also show directly that \([\alpha],[\beta_1],[\beta_2]\) are \(\mathbb Z\)-linearly independent: rotation on \(4_1\) kills the \(\alpha\)-coefficient, rotation on \(3_1^+\) then kills the \(\beta_2\)-coefficient, and rolling on \(4_1\) kills the \(\beta_1\)-coefficient.

## Verification
The proof is symbolic and uses only the source's exact descending criterion, exact pairing formulae, and the invariant values of \(3_1^+\) and \(4_1\) tabulated in the source.

The bundled standalone verifier encodes the corresponding obstruction rows. Over \(\mathbb Z\), the two parametrized-descent witness rows are
\[
(-2,0,0),\qquad(2,0,-2)
\]
in coefficient order \((\alpha,\beta_1,\beta_2)\), whose simultaneous kernel is the \(\beta_1\)-axis. The figure-eight second-quotient row is
\[
(-1,2,2),
\]
which kills that remaining axis over \(\mathbb Z\).

Over \(\mathbb F_2\), the two second-quotient rows are
\[
(1,0,0,0),\qquad(1,0,1,0)
\]
in coefficient order \((\bar\alpha,\bar\beta_1,\bar\beta_2,\beta_3)\). Their common kernel is exactly the plane with basis \(\bar\beta_1,\beta_3\).

Running `artifacts/verify_descent_filtration.py` from the packaged path returns:

`VERIFY_OK integral_param=span(beta1) integral_unparam=zero mod2_param_dim=4 mod2_unparam_dim=2 mod2_unparam_basis=beta1,beta3`

The verifier is a replay of the finite-dimensional coefficient reduction; the infinite quantifier over knots is discharged by the source's necessary-and-sufficient criterion together with the two explicit witness knots, not by enumeration.

## Relationship to prior work
Zhang constructs \(\beta_1,\beta_2,\beta_3\), computes their canonical-loop pairings, proves the four mod-\(2\) classes \(\bar\alpha,\bar\beta_1,\bar\beta_2,\beta_3\) independent, and proves the general necessary-and-sufficient descending criterion. The paper's stated corollary records three positive facts: integral \(\beta_1\) descends to parametrized closed knots, while \(\bar\beta_1\) and \(\beta_3\) descend independently to unparametrized oriented closed knots. It does not state the exact descending submodule in the three-generator integral span or the exact descending subspace in the four-generator mod-\(2\) span.

The present result closes that local classification using the same source data: \(\alpha\) and \(\beta_2\) are excluded integrally already at the parametrized quotient; the surviving integral \(\beta_1\) is excluded at the unparametrized quotient; modulo \(2\), all four pass the first quotient but exactly \(\bar\beta_1,\beta_3\) pass the second.

Earlier work of Mortier constructs combinatorial and finite-type \(1\)-cocycles on long-knot spaces, including \(\alpha_3^1\), but predates Zhang's \(\beta_1,\beta_2,\beta_3\). Targeted searches using “descent”, “unparametrized”, the three \(\beta\)-labels, and the exact two-stage quotient did not identify a prior statement of this exhaustive span classification.

## Limitations
This is a classification within the natural spans generated by the named classes, not a computation of the complete groups \(H^1\) of the closed-knot spaces. In particular, it does not prove Zhang's conjecture that the displayed low-order classes form bases of all degree-one cohomology up to combinatorial order \(4\).

The result is an exact corollary of a very recent preprint. A later revision could add the same span classification or alter a source pairing formula; the statement here is tied to arXiv:2609.29946v1.

## References
1. Butian Zhang, *Pairings of combinatorial 1-cocycles with loops in knot spaces*, arXiv:2609.29946v1, first posted 2026-09-24. Theorem B, Theorem C, the canonical-loop pairing tables, and Corollary 7.8 are the primary inputs.
2. Arnaud Mortier, *Combinatorial cohomology of the space of long knots*, Algebraic & Geometric Topology 15 (2015), 3435--3465, DOI 10.2140/agt.2015.15.3435.
3. Arnaud Mortier, *Finite-type 1-cocycles of knots and virtual knots given by Polyak--Viro formulas*, Journal of Knot Theory and Its Ramifications 24 (2015), 1540004, DOI 10.1142/S0218216515400040.
