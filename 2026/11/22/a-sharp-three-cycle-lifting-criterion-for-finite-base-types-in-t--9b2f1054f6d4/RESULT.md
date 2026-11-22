# A sharp three-cycle lifting criterion for finite-base types in the dense local order

## Finding

Let \(D\) be the countable dense local order tournament. For every integer \(n\ge1\), let \(A\subseteq D\) be any finite, individually named, induced \(n\)-vertex parameter subtournament. Write \(\mathcal{T}_A\) for its complete nonalgebraic one-point types. Define
\[
\mathcal C_A=\{(p,q,r)\in\mathcal T_A^3:\exists x,y,z\text{ distinct realizing }p,q,r\text{ with }x\to y,\ y\to z,\ z\to x\}.
\]
There are exactly \(2n\) types; write their indices in cyclic order modulo \(2n\). Then
\[
(p,q,r)\in\mathcal C_A\iff \neg(p=q=r)\ \land\ (q-p)_{2n},(r-q)_{2n},(p-r)_{2n}\in\{0,\ldots,n\},
\]
where \((a)_{2n}\) is the residue in \(\{0,\ldots,2n-1\}\). In particular,
\[
\boxed{|\mathcal C_A|=n(n+1)(n+2).}
\]
The displayed test is a sharp local-to-global criterion: simultaneous realization of the three edges of a directed triangle follows from their separate pairwise feasibility, with the sole exception of three coincident unary types.

## Assumptions and scope

Represent \(D\) by a countable dense subset of the oriented unit circle containing no antipodal pair. The edge \(u\to v\) means clockwise angular displacement strictly between zero and a half-turn. Every finite induced tournament in this model is a permissible named parameter base. All realizations are new vertices distinct from one another and from the named base. A type is a complete one-point type in the pure tournament language with each base vertex named; homogeneity identifies these with the orientation vectors to the base. No uniform measure on the countable circle is involved.

## Proof

**One-point types.** Mark the \(n\) named points and their \(n\) antipodes. These \(2n\) distinct boundary points divide the circle into \(2n\) nonempty open arcs, each of length at most a half-turn. A new point's edge directions to the named base are constant on an arc. They are distinct on different arcs: the directions can agree after traversing a proper nonempty arc interval only if, for every named point, both of its antipodal boundaries or neither occur in that interval. If the interval contains both boundaries for one named point it has length exceeding a half-turn, so it contains at least one boundary for every named point; hence it must contain both for every point, impossible for a proper interval. Thus the \(2n\) arcs give exactly the complete nonalgebraic types. Antipodal rotation shifts arc index by \(n\).

**Binary feasibility.** Number arcs \(I_0,\ldots,I_{2n-1}\) clockwise. The edge \(u\to v\) with \(u\in I_p,v\in I_q\) is possible exactly for \((q-p)_{2n}\in\{0,\ldots,n\}\). For offset zero, choose two points in increasing clockwise order inside the same arc. For offset between one and \(n-1\), the chosen gap is strictly below a half-turn. At offset \(n\), antipodal arcs have equal angular widths, and choosing the source nearer its clockwise endpoint than the target's relative position makes the displacement below a half-turn. For offsets larger than \(n\) the displacement is strictly greater than a half-turn, so the edge is impossible.

**Simultaneous three-cycle.** Necessity of the three pairwise tests is immediate. If \(p=q=r\), all three realizing points lie in one open arc of angular length at most a half-turn, which induces a transitive tournament and cannot contain a directed triangle. If all three indices are different, list the arcs clockwise. Their three positive cyclic index gaps sum to \(2n\). The pairwise tests exactly say each gap is at most \(n\). At most one gap equals \(n\), because the others are positive. Choose representatives inside the arcs so that all three angular gaps are less than a half-turn. This is automatic when every index gap is smaller than \(n\); if one equals \(n\), the corresponding endpoint choices can make that angular gap strictly smaller than a half-turn, without changing the strict inequalities for the other two. Orienting the representatives cyclically then gives the required three-cycle. If exactly two indices agree, the pairwise tests force the remaining index to be the antipodal index, at offset \(n\). Choose the two representatives in the repeated arc in clockwise order, and the third in the opposite arc with its relative position between those of the repeated representatives; all three cyclic angular gaps are then less than a half-turn. This proves sufficiency in every case.

**Enumeration.** For three distinct indices the number of positive triples of cyclic index gaps \((a,b,c)\) with \(a+b+c=2n\) and all three at most \(n\) is
\[
\binom{2n-1}{2}-3\binom{n-1}{2}=\frac{(n-1)(n+4)}2,
\]
with the binomial coefficient interpreted as zero when its upper argument is below two. Choosing the starting arc gives \(2n\) choices, so the number of *ordered* three-cycle-feasible profiles with distinct indices is \(n(n-1)(n+4)\). With exactly two equal indices, there are \(2n\) choices for that repeated index, three positions for the exceptional index, and only its antipodal type is permitted. This gives \(6n\) profiles. All-three-equal contributes zero. Their sum is \(n(n-1)(n+4)+6n=n(n+1)(n+2)\).

## Verification

The included standalone `verify.py` uses exact rational angular coordinates, constructs non-antipodal named circles, recovers distinct one-type orientation signatures, and explicitly tests all ordered triples of arc types against the criterion. It samples eight strictly interior representatives in each arc; cases \(1\le n\le8\) agreed with the formula and with the geometric predicate. Finite sampling is a check only; the preceding argument supplies the all-\(n\) proof.

## Relationship to prior work

Coregliano's 2015 preprint studies locally transitive and carousel tournaments and provides the relevant cyclic tournament framework, but not the above finite-base three-cycle feasibility law. Williams (2014, Corollary 3.3) already determines the integral Smith factors of arbitrary consecutive-ones circulants; therefore no new Smith-matrix theorem is asserted here. The result is instead the sharp **three-variable simultaneous-realization criterion** and exact labelled type-profile count. The existing published finite-base one-type score classification in the dense local order concerns different invariants; its available summary does not establish this three-cycle law. The mathematical derivation above, not the failure of a database search, supports the claimed distinction.

## Limitations

The theorem concerns directed three-cycles of three distinct new points over a finite named base. It does not enumerate all complete ordered triple types, transitive triples, longer directed cycles, or cyclic triangles over reducts with fewer named relations. The geometric proof presumes the dense-circle model, including the absence of antipodal vertices. Historical priority of this specific three-cycle profile theorem remains provisional; a broader orbit-enumeration theorem not found in the inspected sources could subsume it. No independent mathematical audit has been performed.

## References

1. L. N. Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124, first posted 13 March 2015, https://arxiv.org/abs/1503.04124.
2. G. Williams, *Smith forms for adjacency matrices of circulant graphs*, Linear Algebra and its Applications 443 (2014), 21–33; freely available preprint https://repository.essex.ac.uk/8578/1/SNRcirculantgraphs.pdf (specifically Corollary 3.3, which covers a different, purely binary matrix invariant).
3. *Set-homogeneous hypergraphs*, Journal of the London Mathematical Society (2023), https://doi.org/10.1112/jlms.12796 (explicit countable dense-local-order circle model, background only).
