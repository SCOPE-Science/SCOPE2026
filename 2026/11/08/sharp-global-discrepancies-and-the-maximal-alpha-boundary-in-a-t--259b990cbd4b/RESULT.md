# Sharp global discrepancies and the maximal-alpha boundary in a toric Fano realization family

## Finding

For all integers \(n\ge2\) and positive coprime integers \(B\le A\le nB\), consider the toric \(\mathbf Q\)-Fano variety \(X_{n;A,B}\) constructed by Wu, with fan consisting of cones over the faces of
\[
Q_{n;A,B}=\left\{(d_0,\ldots,d_n)\in\mathbb R^{n+1}:\sum_i d_i=0,\quad -A\le d_i\le B\right\}.
\]
Coordinates are measured in the lattice \(N=\{d\in\mathbb Z^{n+1}:\sum_i d_i=0\}\). Its **global minimal log discrepancy**, defined as the infimum of log discrepancies of all divisorial valuations with centers anywhere on the variety, is exactly
\[
\operatorname{mld}_{\mathrm{glob}}(X_{n;A,B})=\frac1B.
\]
Furthermore, \(X_{n;A,B}\) is canonical exactly when \(B=1\), and terminal exactly when \((n,A,B)=(2,1,1)\).

Wu proves \(X_{n;A,B}\) is K-polystable and has ordinary alpha invariant \(\alpha(X_{n;A,B})=B/(A+B)\). Consequently, at fixed \(n\ge2\), the coprime sequence \((A,B)=(B+1,B)\), with \(B\ge2\), satisfies
\[
\alpha(X_{n;B+1,B})=\frac{B}{2B+1}\longrightarrow\frac12,
\qquad \operatorname{mld}_{\mathrm{glob}}(X_{n;B+1,B})=\frac1B\longrightarrow0.
\]
Thus even alpha values approaching the maximal toric K-polystable endpoint do not give a positive lower bound for global minimal log discrepancy within this family.

## Assumptions and scope

The ground field is \(\mathbb C\). The fan is Wu's **face fan**, not the normal fan of \(Q_{n;A,B}\). His Propositions 3.2–3.4 give the coordinate realization and show that its vertices are primitive lattice vectors, so \(Q_{n;A,B}\) is the Fano polytope consisting of the convex hull of primitive ray generators. The canonical and terminal claims concern singularities of the whole variety. The minimum permits centers of any codimension, including invariant boundary divisors; it is not the minimum restricted to closed points. The parameter domain ensures the full-dimensional Fano polytope is bounded with the origin in its interior.

## Proof

**Log discrepancy support function.** For a toric \(\mathbf Q\)-Gorenstein Fano variety with primitive-ray polytope \(Q\), the toric log discrepancy function on the complete lattice fan is the Minkowski gauge of \(Q\), because its restriction to each maximal cone is the linear functional taking value one on that facet. In the present coordinates, for any \(d\in N\setminus\{0\}\), it is therefore
\[
h(d)=\inf\{r>0:d\in rQ_{n;A,B}\}
=\max\left\{\frac{\max_i d_i}{B},\frac{-\min_i d_i}{A}\right\}.
\]
Standard toric discrepancy theory states that the global minimal log discrepancy equals the minimum of this function over nonzero lattice points; a primitive lattice point produces an associated divisorial toric valuation. The equality is valid for the possibly nonsimplicial face fan and can be proved by taking a toric log resolution and using the normal-crossings discrepancy formula.

**Exact minimum.** Since \(d\ne0\) has integer coordinates summing to zero, at least one coordinate is positive and hence \(\max_i d_i\ge1\). Thus \(h(d)\ge1/B\) for every nonzero lattice vector. The primitive vector \(w=(1,-1,0,\ldots,0)\) satisfies
\[
h(w)=\max\{1/B,1/A\}=1/B,
\]
using \(A\ge B\). This proves the exact global minimum, with attainment and no appeal to finite enumeration.

**Canonical classification.** The toric Fano polytope criterion says that the singularities are canonical precisely when the origin is the only interior lattice point of \(Q\). If \(B\ge2\), then \(w\) lies strictly in \(Q\): its positive coordinate satisfies \(1<B\), its negative coordinate satisfies \(-1>-A\), and zero lies strictly between the two bounds. Hence it is noncanonical. If \(B=1\), any nonzero integer zero-sum vector has a positive coordinate at least one and hence cannot lie in the interior of \(Q\). Thus all and only the \(B=1\) members are canonical.

**Terminal classification.** The toric Fano criterion is that the only lattice points of \(Q\) are the origin and its vertices. Noncanonical cases are already excluded. When \(B=1\) and either \(n\ge3\) or \(A\ge2\), the lattice point \(w\) lies on \(Q\), has gauge one, but is not a vertex: for \(n\ge3\), only two coordinate bounds can be active at \(w\), fewer than the \(n\) needed for a vertex; for \(n=2\) and \(A\ge2\), only the upper bound at coordinate one is active. Therefore such members are nonterminal. In the remaining case \((n,A,B)=(2,1,1)\), the integer points of the hexagonal polygon \(\{-1\le d_i\le1,\sum d_i=0\}\) are precisely the origin and the six permutations of \((-1,0,1)\), all vertices. Hence that member is terminal.

**Endpoint degeneration.** For \(B\ge2\), taking \(A=B+1\) is coprime and satisfies \(B\le A\le nB\) for every \(n\ge2\). The stated alpha and discrepancy limits follow from the exact formulas and Wu's previously proved alpha-invariant calculation.

## Verification

The standalone script `discrepancy_verify.py` enumerates all lattice points of the box section in 27 admissible small triples, using exact fractions. It compares the minimum gauge against \(1/B\) and tests interior-point and vertex criteria independently. It also checks seven terms of the endpoint family. All checks passed. These exhaustive finite checks corroborate the boundary cases, while the proof above covers every admissible integer triple without extrapolation.

## Relationship to prior work

Wu, *The alpha spectrum of K-polystable toric \(\mathbf Q\)-Fano varieties* (2026), proves the realization of every rational alpha value in the permitted interval and constructs the coordinate box sections used here. Liu and Zhu (2026) introduced the earlier special-width family. Standard toric discrepancy theory identifies log discrepancies with a piecewise-linear support function and gives canonical/terminal lattice-point criteria. The additional content here is the sharp optimization of that function, the complete singularity-threshold classification **for Wu's entire parameter family**, and the explicit contrasting boundary behavior of the alpha invariant and minimal log discrepancy. In particular, the formula concerns a different invariant from the alpha spectrum itself.

## Limitations

The theorem does not compute minimal log discrepancies at each individual closed point, the full exceptional divisor stratification, local class groups, or stringy invariants. It does not assert that no other K-polystable Fano family has the same degenerating behavior. The first-public-source date is Wu's initial 2026 preprint date, not the date of subsequent revisions. Historical priority and independent mathematical validation are not established.

## References

- Xian Wu, *The alpha spectrum of K-polystable toric \(\mathbf Q\)-Fano varieties*, arXiv:2608.14115 (first version 2026-08-14), Sections 2–4, especially Proposition 3.2 and Theorem 1.2. https://arxiv.org/abs/2608.14115
- Jihao Liu and Ziwen Zhu, *K-polystable toric Fano varieties with small alpha invariants*, arXiv:2607.04005 (2026), Sections 2–4. https://arxiv.org/abs/2607.04005
- *Minimal log discrepancies of hypersurface mirrors*, Forum of Mathematics, Sigma (2024), Section 2.1, Lemma 2.2 (toric lattice discrepancy description). https://doi.org/10.1017/fms.2024.10
- J. Hausen, C. Mauz and M. Wrobel, *The anticanonical complex for non-degenerate toric complete intersections*, manuscripta mathematica (2022), introductory toric Fano singularity criteria. https://doi.org/10.1007/s00229-022-01400-3
