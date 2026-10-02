# Nonexistence of D2-symmetric disk 4-vertex stationary planar 2-clusters

## Context

Planar isoperimetric clusters with two bounded chambers of prescribed areas are
studied through first-variation stationarity: boundaries are finite networks of
circular arcs meeting only at interior triple junctions at 120 degrees, with
curvatures given by pressure Lagrange multipliers. The admitted target asked
whether a highly symmetric candidate can exist: a bounded equal-area
(|E1| = |E2| = 1) stationary 2-cluster whose chambers are each connected and
simply connected (topological disks), exactly invariant under reflections across
two perpendicular lines (D2 symmetry), with exactly four triple junctions and
positive shared interface length.

## Definitions

- Chambers E1, E2: bounded disjoint nonempty open subsets of R^2 of finite
  perimeter; E0 denotes the exterior region.
- S = dE1 union dE2: finite union of C^1 circular arcs meeting only at interior
  triple junctions, each arc separating two distinct chambers of {E0, E1, E2}.
- D2 symmetry: |Rj(Ei)\/Ei| = 0 for i, j in {1, 2}, where R1, R2 are reflections
  across two perpendicular lines L1, L2; rho = R2 o R1 is rotation by pi about
  O = L1 cap L2 (taken as 0).
- Disk topology: each Ei is connected and simply connected as an open set (up to
  the usual finite-perimeter null-set identification, resolved in the proof).
- Reduced/essential boundary d*Ei: the measure-theoretic boundary used in
  finite-perimeter theory; isometry-covariant and stable under null-set changes.

## Result

Theorem. Let E1, E2 be bounded disjoint nonempty open sets of finite perimeter
with S a finite union of C^1 circular arcs meeting only at interior triple
junctions separating distinct chambers. If each Ei is connected and simply
connected and each Ei is D2-symmetric up to null sets, then this is impossible:
no such pair exists. In particular there is no cluster satisfying the full
admitted target hypotheses; the equal-area, four-vertex, positive-interface, and
pressure conditions are not even needed for the contradiction.

## Proof / evidence

Lemma 1 (chambers are faces). Each Ei equals exactly one connected component
(face) of R^2 \ S: Ei lies in a unique face Fi; Fi cap Ei is nonempty and
relatively clopen in Fi because its relative boundary in Fi lies in
(dEi) cap Fi subset S cap Fi = empty, so Fi subset Ei.

Lemma 2 (exact symmetry upgrade). R(S) = S and R(Ei) = Ei exactly for each
reflection. Every non-vertex arc point has density 1/2 on each adjacent chamber
side, so H^1(S \ (d*E1 union d*E2)) = 0. Null-set symmetry plus
isometry-covariance of d* gives H^1(S \/ R(S)) = 0; since S \ R(S) is relatively
open in the compact arc network S, it must be empty, and likewise for the
inverse. Hence R permutes faces, and |R(Ei) cap Ei| = |Ei| > 0 forces
R(Ei) = Ei exactly. Consequently rho(Ei) = Ei exactly with rho(z) = -z.

Lemma 3 (rotation obstruction). A nonempty open connected rho-invariant
U not containing 0 is not simply connected. Join x to -x by a path alpha in U
and close it with rho(alpha) to a symmetric loop beta with
beta(t + 1/2) = rho(beta(t)). The projected loop on S^1 has lift difference
constantly in pi + 2piZ, so total change 2(2k+1)pi: odd winding 2k+1 about 0.
Thus beta is essential in R^2 \ {0} and in U.

Conclusion. E1 cap E2 = empty, so at most one Ei contains 0; both are nonempty
connected exactly rho-invariant opens. The one missing 0 contradicts the disk
hypothesis by Lemma 3. The numeric artifact winding_check.py illustrates the
odd-winding mechanism on the exact circle (winding 1) and six random symmetric
polygonal loops (all winding 1, odd); the proof itself is self-contained and
does not depend on numerics.

## Limitations

The proof uses the stated topological reading of simple connectedness for the
open chambers together with the finite triple-junction arc-network structure to
upgrade null-set symmetry to exact symmetry. It does not classify stationary
2-clusters without the D2 disk-topology hypotheses, and says nothing about
minimizers, unequal areas, non-symmetric configurations, or clusters with
different vertex counts.

## Reproducibility

Translate L1 cap L2 to the origin; verify Lemmas 1-3 as above. Run
`python3 artifacts/winding_check.py` to reproduce the winding-number
illustration (expected: circle winding 1.000000; six seeds all odd winding;
final line confirming all symmetric-loop windings are odd and nonzero).

## References

- F. Morgan et al., double-bubble minimality in R^2 and R^d (standard double
  bubble theorem).
- W. Wichiramala, planar triple bubble theorem.
- E. Paolini, A. Tamagnini, Minimal clusters of four planar regions with the
  same area, arXiv:1612.00178.
- E. Paolini, V. M. Tortorelli, The quadruple planar bubble enclosing equal
  areas is symmetric.
- E. Milman, J. Neeman, multi-bubble isoperimetric results.
