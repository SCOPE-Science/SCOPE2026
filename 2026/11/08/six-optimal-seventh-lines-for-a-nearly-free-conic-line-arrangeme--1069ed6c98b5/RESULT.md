# Six optimal seventh lines for a nearly free conic–line arrangement

## Finding
Let \(s=\sqrt5\), \(r=9+4s\), and put
\[
Q=(7-3s)x^2-4xy-2(3-s)xz+(7+3s)y^2-2(3+s)yz+2z^2.
\]
Over \(\mathbb C\), let \(C\) be the reduced degree-eight arrangement
\[
F=Q\,xyz(y-z)(x-z)(x-r y)=0.
\]
For every projective line \(L\) distinct from the six displayed line components, suppose the enlarged reduced degree-nine arrangement \(C\cup L\) has **only ordinary nodes, ordinary tacnodes and ordinary triple points**. Then its total Tjurina number satisfies the sharp inequality
\[
\boxed{\tau(C\cup L)\le46.}
\]
Equality holds for precisely **six** projective lines. Three join pairs among the original nodes \(A=[0:1:1]\), \(B=[1:0:1]\), \(D=[r:1:0]\):
\[
 x+y-z=0,\qquad x-r y+r z=0,\qquad x-r y-z=0.
\]
The other three are the unique noncomponent tangents from these nodes to the conic:
\[
\begin{aligned}
 x-(2+s)y+(2+s)z&=0,\\
 (s-2)x+y+(2-s)z&=0,\\
 (2-s)x+(2+s)y+z&=0.
\end{aligned}
\]
The joining-line extensions have singularity counts \((n_2,t,n_3)=(5,3,8)\), and the node-tangent extensions have \((n_2,t,n_3)=(6,4,7)\). Both profiles give \(\tau=46\). In particular **no such one-line extension of this explicit degree-eight arrangement is free or nearly free**. This is a boundary on the line-addition approach to the still-open degree-nine existence problem under the three specified singularity types, not a nonexistence theorem for all degree-nine conic–line arrangements.

## Assumptions and scope
All coefficients and tangencies are taken over \(\mathbb C\). The distinguished arrangement is defined over \(\mathbb Q(\sqrt5)\). A projective line is identified up to a nonzero complex scalar. An ordinary tacnode consists of two smooth branches tangent to order two and has local Tjurina number \(3\); an ordinary triple point has three distinct smooth tangent directions and local Tjurina number \(4\). The extra line must avoid generating higher-order or nonordinary singularities. The classification is of the admissible line additions maximizing total Tjurina number, not of all possible lines or all nearly free arrangements of degree nine.

## Proof
**1. The original singularities.** Intersecting the six constituent lines gives precisely three line-only triple points \([1:0:0]\), \([0:1:0]\), \([0:0:1]\), and six double points. The conic passes through three of these six double points, namely \([1:1:1]\), \([r:1:1]\), \([r:1:r]\), where it meets each pair of lines transversely. The other three double points are exactly \(A,B,D\) above and lie off \(Q\). The symmetric conic matrix has determinant \(-32\), so \(Q\) is smooth. Its restrictions to the coordinate lines are perfect squares, with tangency points \([0:1:v]\), \([1:0:u]\), \([v:u:0]\), where \(u=(3-s)/2\), \(v=(3+s)/2\); these are disjoint from all line–line singular points. The three remaining lines meet \(Q\) transversely in pairs drawn from the three named double points. Thus the initial arrangement has \((n_2,t,n_3)=(3,3,6)\) and \(\tau(C)=3+9+24=36\). Each assertion follows by direct substitution, including the avoidance statements, and is independently reconstructed by the attached exact-arithmetic program.

**2. Increment bound.** An admissible new line cannot pass through an old tacnode: the resulting point would have three branches with an already tangent pair. Nor can it pass through an old ordinary triple point, which would produce at least four local branches. Its only permissible old singular points are therefore among \(A,B,D\), where a new transverse branch converts a node of Tjurina number \(1\) into an ordinary triple point of Tjurina number \(4\).

Write \(h\) for the number of old nodes on \(L\), and let \(\epsilon\in\{0,1\}\) indicate whether \(L\) has a new simple tangency to the conic at an otherwise smooth point of \(C\). The new line meets the degree-eight divisor in total intersection multiplicity eight. At a converted old node, two intersection units replace two generic new nodes (Tjurina gain \(3\) instead of \(2\)). At an otherwise smooth conic tangency, two intersection units produce a tacnode (gain \(3\) instead of \(2\)). All remaining intersections are ordinary new nodes. Consequently
\[
\tau(C\cup L)-\tau(C)=8+h+\epsilon.
\]
The three old nodes are not collinear, hence \(h\le2\); a line is tangent to the smooth conic at at most one point, hence \(\epsilon\le1\). To reach \(\tau=47\), it would be necessary that \(h=2\) and \(\epsilon=1\).

**3. The three joins are not tangent.** The unique lines joining two of \(A,B,D\) are the three listed joining lines. Restricting \(Q\) to the span of each corresponding pair of point vectors, its quadratic discriminant equals, in that order,
\[
128,\qquad 3008+1344s,\qquad 448+192s.
\]
All three are nonzero. Thus none is tangent to \(Q\), so \(h=2\) forces \(\epsilon=0\). The sharp bound \(\tau\le36+10=46\) follows.

**4. Exhaustion and attainment.** Equality requires \((h,\epsilon)=(2,0)\) or \((1,1)\). The first case gives exactly the three joining lines. They avoid every other old singular point and intersect \(Q\) transversely, so each is admissible. The resulting singularities are \((5,3,8)\).

For the second case, each old node has exactly two tangents to the smooth conic. One is already a coordinate-line component of \(C\). The other is found by substituting a general line in the pencil through the node into the dual-conic equation. At \(A\) write \(x+w(y-z)=0\), at \(B\) write \(y+w(x-z)=0\), and at \(D\) write \(z+w(x-r y)=0\). The dual-conic quadratics factor, up to nonzero constants, respectively as
\[
 w(w+2+s),\quad w(w+2-s),\quad w(w-2+s).
\]
The nonzero roots yield the three stated new tangent lines. Each passes through its designated old node and no other old singularity. Its conic contact is a new point. Hence all three are admissible and have singularities \((6,4,7)\). These six lines are distinct. No seventh equality case exists.

**5. Freeness obstruction.** Gałecka's lower bound for an arrangement with these three allowed singularity types is \(\operatorname{mdr}\ge2m/3-2\). At degree \(m=9\), this gives \(\operatorname{mdr}\ge4\). For a free degree-nine curve, the smaller exponent cannot exceed \(4\), so both exponents would be \((4,4)\), forcing \(\tau=48\). For a nearly free degree-nine curve the exponents must be \((4,5)\), forcing \(\tau=47\). The proven sharp upper bound \(46\) rules out both possibilities.

## Verification
Run the standalone Python 3 verifier with SymPy installed:

```console
python verify_degree9_line_extension.py
```

Expected final marker:

```text
DEGREE9_SIX_OPTIMAL_ADDITIONS_PASS 9 3 3 3 46 47 48
```

The verifier reconstructs the complete pairwise line incidence structure, independently checks the conic matrix, conic incidence and tangent points, computes the three discriminants, solves all three node–tangent pencil equations over \(\mathbb Q(\sqrt5)\), excludes forbidden singular-point incidences and confirms the two singularity baskets. The general lower bound on the minimal Jacobian syzygy degree and free/nearly free Tjurina formulas are published theorems, not numerically inferred by the program.

## Relationship to prior work
Gałecka's 2022 study asks about existence of degree-nine nearly free conic–line arrangements with only nodes, tacnodes and ordinary triple points. An openly available 2026 construction supplies the explicit degree-eight nearly free one-conic/six-line arrangement used here, but explicitly leaves degree nine untreated. The present result does **not** claim that degree-eight example or Gałecka's numerical formulas as new. It classifies all optimal seventh-line additions to that example and proves this natural direct route cannot solve the degree-nine existence problem. Dimca, Ilardi, Pokora and Sticlaru's general line-addition constructions cover other free and nearly free arrangements, but their inspected sections do not identify the six-line optimum for this conic and its three remaining nodes.

## Limitations
The result concerns one particular degree-eight starting arrangement and only seventh lines preserving the three specified singularity types. Other degree-eight arrangements, changes to the conic or to several components at once, or degree-nine arrangements not obtained by a single line addition remain outside the theorem. The originality comparison is based on accessible published text and mathematical-record searches; unindexed calculations or a specialized addition–deletion corollary may already imply the conclusion. The computation is an exact symbolic check of critical finite algebraic identities, while the geometric upper bound and the published numerical criteria are justified separately in the proof.

## References
1. A. Gałecka, “On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points,” arXiv:2204.13969, first posted 29 April 2022; *Boletín de la Sociedad Matemática Mexicana* 28 (2022), article 67. DOI: 10.1007/s40590-022-00461-4.
2. “A degree-eight nearly free conic-line arrangement over a quadratic field,” publicly available mathematical note (2026), with explicit formula for the degree-eight curve and proof of its nearly freeness, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-degree-eight-nearly-free-conic-line-arrangement-over-a-quadrat--2edf9ed667f2.
3. A. Dimca, G. Ilardi, P. Pokora and G. Sticlaru, “Construction of Free Curves by Adding Lines to a Given Curve,” arXiv:2301.01117, first posted 3 January 2023; *Results in Mathematics* 79 (2024), article 11. DOI: 10.1007/s00025-023-02036-9.
4. A. Dimca, “On free and plus-one generated curves arising from free curves by addition-deletion of a line,” arXiv:2310.08972, first posted 13 October 2023 (abstract only inspected; not relied on in the proof).

5. P. Pokora, “On the Numerical Terao Conjecture,” arXiv:2608.05662, first posted 6 August 2026. Its degree-nine one-conic/seven-line examples have ordinary quadruple points and thus lie outside the singularity assumptions here.
