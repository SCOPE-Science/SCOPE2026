# Boundary and branch strata in coordinate-involution quotients of polygonal real moment-angle surfaces

## Finding
Let \(C_n\) be the simplicial boundary cycle of a convex \(n\)-gon, where \(n\ge3\) (with \(C_3=\partial\Delta^2\)). In the real moment-angle surface
\[
M_n=(D^1,S^0)^{C_n}\subset[-1,1]^n,
\]
let \(\tau_S\) replace \(x_i\) by \(-x_i\) for all \(i\in S\), for any nonempty subset \(S\subseteq[n]\). Write \(Q_{n,S}=M_n/\langle\tau_S\rangle\). Its homeomorphism type and the branch structure of the quotient map are exactly:

| Coordinates reversed | Type of quotient | Genus/crosscaps | Fixed or branch locus |
|---|---|---|---|
| \(|S|=1\) | Connected orientable bordered surface | Genus \(1+(n-5)2^{n-4}\) | \(2^{n-3}\) boundary circles, each pointwise fixed |
| \(|S|=2\), cyclically adjacent | Connected closed orientable surface | Genus \(1+(n-5)2^{n-4}\) | \(2^{n-2}\) isolated order-two branch points |
| Even \(|S|\), not an adjacent pair | Connected closed orientable surface | Genus \(1+(n-4)2^{n-4}\) | Empty (free action) |
| Odd \(|S|\ge3\) | Connected closed nonorientable surface | \(2+(n-4)2^{n-3}\) crosscaps | Empty (free action) |

Thus the **two distinct forms of nonfree involution give the same genus**, although one produces a surface boundary and the other has isolated branching. For \(n=3\) the first type is a disk, the second is a sphere with two branch points, and the last is a real projective plane. For \(n=4\) the four types are an annulus, a sphere branched at four points, a torus, and a Klein bottle. The free-action cases are included for completeness; the new calculation focuses on the nonfree boundary and branched strata.

## Assumptions and scope
For each face \(\sigma\in C_n\), the polyhedral product cell is \(\prod_{i\in\sigma}D^1\times\prod_{i\notin\sigma}S^0\). Faces have at most two vertices, and a pair is a face exactly when the indices are consecutive around the cyclic polygon. The action is **coordinate sign reversal**, not permutation of coordinates under the polygon dihedral group. All surfaces and quotients are ordinary geometric orbit spaces. Every integer \(n\ge3\) and every nonidentity element of \((\mathbb Z/2)^n\) is included.

## Proof
**1. Surface and its orientation.** The cubical product has \(2^n\) vertices, \(n2^{n-1}\) edges and \(n2^{n-2}\) squares. These form a closed connected orientable surface: each edge belongs to two squares, each vertex has polygonal link \(C_n\), and the one-skeleton is the connected \(n\)-cube. Assign the copy of the base polygon labeled by a sign vector \(\varepsilon\in\{\pm1\}^n\) the orientation sign \(\prod_i\varepsilon_i\); this makes the orientations agree across glued edges. Consequently
\[
\chi(M_n)=(4-n)2^{n-2},\qquad g(M_n)=1+(n-4)2^{n-3}.
\]
The sign reversal \(\tau_S\) has orientation degree \((-1)^{|S|}\).

**2. Exact fixed set.** A point is fixed by \(\tau_S\) exactly when \(x_i=0\) for all \(i\in S\). Since the set of coordinates in \((-1,1)\) must be a face of \(C_n\), the fixed set can only be nonempty if \(S\) is a single vertex or an adjacent pair. For a singleton \(S=\{i\}\), every coordinate outside the two neighbors of \(i\) is forced to \(\pm1\), and the two neighboring coordinates vary in \((D^1,S^0)^{S^0}=\partial([-1,1]^2)\cong S^1\). Thus
\[
M_n^{\tau_{\{i\}}}\cong\bigsqcup_{2^{n-3}}S^1.
\]
For \(S=\{i,i+1\}\), all remaining coordinates are signs and
\[
|M_n^{\tau_S}|=2^{n-2}.
\]
For all other nonempty \(S\) the action is free.

**3. Local quotient types.** The one-coordinate reversal is an orientation-reversing reflection near each of its fixed circles, so its orbit space is a compact surface whose boundary is exactly the image of those circles. In fact the quotient is the half \(\{x_i\ge0\}\cap M_n\). Its connectedness follows because its vertices with \(x_i=1\) form a connected \((n-1)\)-cube. It is orientable as an open subsurface of \(M_n\), extended across the boundary. At an isolated fixed point of an adjacent-pair reversal, the two local coordinate directions are simultaneously negated: the local quotient is a disk under rotation by \(\pi\), with branching order two. Because this involution preserves orientation, the quotient is closed orientable. All remaining actions are free coverings; parity determines whether the quotient is orientable.

**4. Euler characteristic and surface classification.** A finite equivariant subdivision gives for every involution on a finite CW complex
\[
\chi(Q_{n,S})=\frac{\chi(M_n)+\chi(M_n^{\tau_S})}{2}.
\]
For a singleton the fixed Euler characteristic is zero, and the number of boundary components is \(b=2^{n-3}\). Solving \(2-2h-b=(4-n)2^{n-3}\) yields \(h=1+(n-5)2^{n-4}\). For an adjacent pair the fixed Euler characteristic is \(2^{n-2}\), so \(2-2h=(5-n)2^{n-3}\), yielding exactly the same genus. For free even cardinality, \(2-2h=(4-n)2^{n-3}\) yields \(h=1+(n-4)2^{n-4}\). For free odd cardinality, \(2-c=(4-n)2^{n-3}\) yields \(c=2+(n-4)2^{n-3}\). The classification theorem for connected compact surfaces completes every homeomorphism assertion.

## Verification
The included `verify_sign_quotients.py` enumerates a sign-equivariant cubical subdivision by splitting each coordinate interval at zero. It enumerates **all nonidentity coordinate flips for every \(3\le n\le7\)**, checks the quotient-cell Euler characteristic against the fixed-set Euler characteristic, checks the fixed-circle connected components and the isolated branch-point counts, and verifies all four genus/crosscap formulas. The exact recorded output is in `check_output.txt`; the final line is `POLYGON_MOMENT_ANGLE_ALL_SIGN_INVOLUTIONS_PASS cases=243`. Finite enumeration is a cross-check; the proof above establishes the unbounded theorem.

## Relationship to prior work
Buchstaber and Panov introduce the moment-angle cubical framework. Erokhovets (2022) gives the polygonal surface genus and sign-labelled polygon gluing, which are used rather than claimed new here. Known vector-colouring surface formulas also imply the **free** quotient cases once the action is shown free; those cases are included solely to make the four-case statement complete. Erokhovets (2024) studies general nonfree sign-subgroup quotients and broad manifold criteria, but does not state this four-case explicit polygonal *surface homeomorphism* classification or the equality of genera for singleton and adjacent-pair involutions in the parts inspected. Liu (2015) classifies polygonal moment-angle *partial quotient manifolds* in a paper whose exact relationship remains an unresolved priority comparison because its full text was inaccessible; the abstract's 4-dimensional quasitoric setting suggests a different dimension and action. The primary novel contribution here is the full nonfree boundary/branch calculation, not the established ambient genus or the free-action genus consequences.

## Limitations
This is a topological classification, not an equivariant classification of the quotient maps relative to all possible automorphisms. Branch-point locations within each orientable quotient surface are not marked up to mapping class group. The cohomology action, higher-dimensional moment-angle complexes, and quotients by subgroups of order more than two are outside scope. A plausible inaccessible 2015 publication may contain related polygonal partial quotient results, and unindexed equivalent 2-dimensional calculations cannot be ruled out without independent bibliography review. All mathematical review here is non-independent.

## References
- V. M. Buchstaber and T. E. Panov, *Torus actions, combinatorial topology and homological algebra*, arXiv:math/0010073v1, October 7, 2000. https://arxiv.org/abs/math/0010073
- N. Yu. Erokhovets, *Canonical geometrization of orientable 3-manifolds defined by vector colourings of 3-polytopes*, Sbornik: Mathematics 213 (2022), 752–793, §1 (polygonal gluing and genus formula). https://www.mathnet.ru/eng/sm9665
- N. Yu. Erokhovets, *Manifolds realized as orbit spaces of non-free Z2^k-actions on real moment-angle manifolds*, arXiv:2403.00492 (2024), §§1–6 (general quotient criteria). https://arxiv.org/abs/2403.00492
- D. P. Liu, *The partial quotients of Moment-angle manifolds over a polygon*, Acta Mathematica Sinica, English Series 31 (2015), 319–330, DOI:10.1007/s10114-015-3104-4 (abstract inspected; full text inaccessible). https://doi.org/10.1007/s10114-015-3104-4
