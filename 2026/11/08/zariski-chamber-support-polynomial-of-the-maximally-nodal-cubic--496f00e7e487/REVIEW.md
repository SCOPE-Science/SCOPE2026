# Independent mathematical audit

## correctness

PASS

The count is for the smooth complex resolution, not for the singular cubic. The four strict line transforms D_i give -K=H+(sum D_i)/2, which is nef with square three; adjunction forces negative curves to have (self-square, anticanonical degree) (-1,1) or (-2,0). For nonexceptional curves Cauchy forces plane degree at most two. In degree two the equations force five or six simple centers, hence three on one original line, impossible for an irreducible conic. In degree one a line through two incident edge centers is the original line attached to their common vertex. The resulting list is exactly six exceptional curves, three diagonal strict transforms, and four pairwise disjoint -2 curves. Diagonals are disjoint from all D_i and may be selected at most one, with the two matching edges forbidden. Eliminating the exceptional -I block leaves 2I minus the restricted incidence product as the positive matrix to test. This demands degree at most one at each selected vertex and forbids selecting both endpoints of an isolated edge; these conditions make the matrix strictly positive diagonal. This proves the three graph factors. A new exact determinant check of all 8192 principal subsets and a separate sum over all 64 labelled graphs both give (1,13,69,186,260,168,29), total 726, with 393 supports containing a diagonal and 333 not. Independent replay: /workspace/branches/9712fab3-7d95-4f4f-8469-c910499bdeb2/independent_check.py and independent_check_output.txt. The finite enumeration uses the geometrically proved exhaustive list. The frozen scripts were inspected, not executed; no formal verification or expert attestation is asserted.

## originality

PASS

The distinct contribution is the exact Cayley support-size and diagonal census with a K4 expansion. The geometry, nine-line count, Cox-ring data and general chamber algorithm are known. The exact catalogue entry later used as the identity case of an equivariant result explicitly cites this frozen finding; other relevant inspected sources do not cover the combined claim. Historical priority remains provisional.

## value

PASS

The maximally nodal cubic is a canonical singular case, and the distribution by support size is a natural resolution invariant. The optional-matching factor resolves the contribution of the three distinguished diagonals and the graph expression shows exactly which configurations of exceptional curves obstruct a support. This provides both a benchmark beyond a total and a combinatorial description useful for later symmetry-sensitive enumerations; it is not just a line count or an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
