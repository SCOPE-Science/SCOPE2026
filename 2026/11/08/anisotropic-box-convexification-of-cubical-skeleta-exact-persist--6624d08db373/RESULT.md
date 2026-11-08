# Anisotropic box convexification of cubical skeleta: exact persistence and void-loss exponents

## Finding
Let \(d\ge2\), \(0\le r<d\), and \(a_1,\ldots,a_d>0\). Write \(C=[0,1]^d\), let \(A_{d,r}=\operatorname{skel}_r(C)\) be the union of its closed faces of dimension at most \(r\), and let \(B_a=\prod_{i=1}^d[-a_i,a_i]\). For every real \(\lambda\ge0\), set \(X_\lambda=A_{d,r}+\lambda B_a\) and \(Q_\lambda=C+\lambda B_a\). Put
\[
N_\lambda=\{i:2\lambda a_i<1\},\qquad s_\lambda=|N_\lambda|,
\]
and for integers \(s\ge0\) define \(b_r(s)=0\) when \(s\le r\), and otherwise
\[
b_r(s)=\sum_{j=r+1}^{s}2^{j-r-1}\binom{j-1}{r}.
\]
The following statements hold **simultaneously**, including at all critical parameters and with equal box widths.

**(1) Exact shape and convexification.** A point \(x\in Q_\lambda\) belongs to \(X_\lambda\) if and only if at most \(r\) of its coordinates satisfy \(\lambda a_i<x_i<1-\lambda a_i\). Equivalently, \(X_\lambda\) consists of all points in \(Q_\lambda\) with at least \(d-r\) endpoint-admissible coordinates. Consequently
\[
X_\lambda\text{ is convex}\ \Longleftrightarrow\ s_\lambda\le r
\ \Longleftrightarrow\ \lambda\ge\frac1{2a_{(r+1)}},
\]
where \(a_{(1)}\le\cdots\le a_{(d)}\) are the increasing rearrangements. In the convex regime \(X_\lambda=Q_\lambda\).

**(2) Homotopy and the entire barcode.** If \(s_\lambda>r\), then \(X_\lambda\) strongly deformation retracts onto the \(r\)-skeleton of an \(s_\lambda\)-cube and hence has homotopy type
\[
X_\lambda\simeq\bigvee^{b_r(s_\lambda)}S^r.
\]
Here the wedge-of-zero-spheres convention means \(b_0(s)+1\) isolated points. If \(s_\lambda\le r\), the set is a convex box, hence contractible. Its only nonzero reduced integral homology is \(\widetilde H_r(X_\lambda;\mathbb Z)\cong\mathbb Z^{b_r(s_\lambda)}\) (when \(s_\lambda>r\)). For every \(0\le\lambda\le\mu\), inclusion \(X_\lambda\hookrightarrow X_\mu\) is surjective on this reduced homology. Thus, over **any field**, every finite persistence interval starts at \(0\); at a parameter where \(s\) drops from \(s_-\) to \(s_+\), precisely \(b_r(s_-)-b_r(s_+)\) intervals end. At one-coordinate crossings \(s\to s-1\), the death multiplicity is
\[
2^{s-r-1}\binom{s-1}{r}\quad(s\ge r+1).
\]
There is no reduced homology in other degrees, at any scale. In ordinary degree-zero persistence, one additional connected-component interval persists indefinitely.

**(3) Exact void volume and critical order.** Write \(g_i=1-2\lambda a_i\) and \(u_i=4\lambda a_i\) for \(i\in N_\lambda\). Then
\[
\operatorname{vol}_d(Q_\lambda\setminus X_\lambda)
=\left(\prod_{i\notin N_\lambda}(1+2\lambda a_i)\right)
\sum_{\substack{I\subseteq N_\lambda\\|I|>r}}
\left(\prod_{i\in I}g_i\right)
\left(\prod_{i\in N_\lambda\setminus I}u_i\right).
\]
This quantity is positive exactly in the nonconvex regime. At the final convexification threshold \(\lambda_*=1/(2a_{(r+1)})\), let \(a_*=a_{(r+1)}\), \(t=|\{i:a_i<a_*\}|\), \(m=|\{i:a_i=a_*\}|\), and \(h=r+1-t\). Then \(1\le h\le m\) and, as \(\lambda\uparrow\lambda_*\),
\[
\operatorname{vol}_d(Q_\lambda\setminus X_\lambda)
=K(\lambda_*-\lambda)^h+O((\lambda_*-\lambda)^{h+1}),
\]
where the **strictly positive** explicit coefficient is
\[
K=\binom mh(2a_*)^h2^{m-h}
\prod_{a_i<a_*}\left(1-\frac{a_i}{a_*}\right)
\prod_{a_i>a_*}\left(1+\frac{a_i}{a_*}\right).
\]
In particular, the isotropic case \(a_i=a\) has extinction exponent \(r+1\) and coefficient \(\binom d{r+1}(2a)^{r+1}2^{d-r-1}\). This exponent is not generally one: ties among box widths can create higher-order closing of the missing volume.

## Assumptions and scope
The skeleton is a geometric union of closed coordinate faces, **not** the set of their vertices unless \(r=0\). The ambient metric is the standard Euclidean one, but the dilation body is the specified axis-parallel box, not a Euclidean ball. Minkowski addition, Lebesgue volume, and ordinary/reduced homology have their usual meanings. The filtration contains \(X_0=A_{d,r}\). The first-public motivating literature date is October 19, 2026 (arXiv version 1); it is not the manuscript's printed date.

## Proof
**Coordinate reduction.** Every point of an \(r\)-face has at least \(d-r\) coordinates fixed to \(0\) or \(1\). If \(x\in Q_\lambda\), a fixed endpoint can be chosen for coordinate \(i\) precisely when \(x_i\in[-\lambda a_i,\lambda a_i]\cup[1-\lambda a_i,1+\lambda a_i]\). Every nonfixed coordinate can be realized with some value of \([0,1]\) because \(x_i\in[-\lambda a_i,1+\lambda a_i]\). This proves (1)'s membership criterion. A coordinate fails endpoint admissibility precisely on the open gap \((\lambda a_i,1-\lambda a_i)\), which exists only if \(2\lambda a_i<1\). Since \(\operatorname{conv}(A_{d,r})=C\), we have \(\operatorname{conv}(X_\lambda)=Q_\lambda\). If \(s_\lambda>r\), points with \(r+1\) gap coordinates lie in \(Q_\lambda\setminus X_\lambda\); otherwise no such point exists. Sorting the widths yields the convexification threshold, including equality.

**Strong deformation retract.** For each narrow coordinate let \(\delta_i=\lambda a_i<1/2\) and clamp the enclosing interval \([-\delta_i,1+\delta_i]\) onto \([\delta_i,1-\delta_i]\). For each nonnarrow coordinate clamp it to \(1/2\). Coordinatewise straight-line interpolation with the resulting map stays inside \(X_\lambda\): a narrow coordinate initially in either endpoint interval remains there, while a coordinate in the open gap remains fixed. Thus at most \(r\) gap coordinates appear throughout. The map fixes its image pointwise. The image is exactly the \(r\)-skeleton of the smaller \(s_\lambda\)-box, with a point in every other factor. When \(s_\lambda\le r\), this is the entire smaller box and all of \(X_\lambda=Q_\lambda\) is convex.

**Wedge and rank.** The cubical \(r\)-skeleton of an \(s\)-cube is \((r-1)\)-connected for \(r\ge1\): the full cube is obtained by attaching only cells of dimension at least \(r+1\), and is contractible. For \(r=1\) it is a connected graph; for \(r\ge2\) the Hurewicz and Whitehead theorems identify it up to homotopy with a wedge of \(r\)-spheres; \(r=0\) is a finite discrete set. Its \(j\)-cell count is \(2^{s-j}\binom sj\) for \(0\le j\le r\). The reduced Euler characteristic gives
\[
b_r(s)=(-1)^r\left[\sum_{j=0}^r(-1)^j2^{s-j}\binom sj-1\right].
\]
The Pascal identity yields \(b_r(s)-b_r(s-1)=2^{s-r-1}\binom{s-1}{r}\) for \(s\ge r+1\), with \(b_r(r)=0\), proving the stated formula.

**Persistence maps.** If \(\lambda\le\mu\), then \(N_\mu\subseteq N_\lambda\). Fix every dropped coordinate at the endpoint \(0\). A copy of the \(r\)-skeleton on the surviving coordinates is contained in \(X_\lambda\), and its image in \(X_\mu\) maps to the full set of degree-\(r\) generators under the above deformation retraction (the coordinatewise endpoint-and-gap rescaling is homotopic to the identity on the cubical skeleton). Thus all inclusion maps are surjective on reduced degree-\(r\) homology. The ranks and surjections determine the entire finite-type persistence barcode; equal critical scales are handled by taking their combined drop.

**Volume and vanishing order.** The enclosing box is partitioned, up to null boundaries, according to which narrow coordinates lie in their open gaps. A gap has length \(g_i\); its complementary two endpoint intervals have total length \(u_i\), and every nonnarrow coordinate has length \(1+2\lambda a_i\). A point is missing exactly when more than \(r\) gaps occur. Multiplying the corresponding lengths proves (3)'s finite sum. Near \(\lambda_*\), exactly \(t\) coordinates have gap lengths with positive limits, exactly \(m\) critical coordinates have gap lengths equal to \(2a_*(\lambda_*-\lambda)\), and the remaining coordinates are nonnarrow. At least \(h=r+1-t\) critical gaps are needed; the smallest possible power uses all \(t\) noncritical gaps and exactly \(h\) of the \(m\) critical gaps. Its coefficient is \(K\) as stated; all other contributions have higher order, and \(K>0\).

## Verification
Run `python check.py` with Python 3.10 or newer. The standalone program uses only standard-library integer arithmetic and exact rational numbers. It checked the cubical chain-boundary ranks for all skeletons through dimension six, the Euler/rank-jump formulas through dimension 79, and 50,114 combined exact assertions for rational offset membership, positive void volume, and threshold equivalence through dimension seven. The finite tests do not replace the all-dimensional proof. As a diagnostic, for \(d=4\), \(r=1\), \(a=(1,2,3,5)\), the first-Betti ranks are \(17\), \(5\), \(1\), and \(0\) across the successive scale changes \(1/10\), \(1/6\), and \(1/4\). The last transition is the exact convexification threshold.

## Relationship to prior work
Meyer, *Finite convexification by Minkowski summation* (arXiv:2610.26744v1, first public October 19, 2026), formulates general criteria for eventual convexification by a convex Minkowski summand. The present claim gives an **exact finite scale**, an **entire anisotropic topological persistence module**, and a **piecewise polynomial void-volume profile** for the geometrically canonical family of cubical skeleta; no assertion is made that the general finiteness criterion is new. The classical CW-cell structure and topology of cubical skeleta are used, not claimed as novel by themselves. Earlier convexification formulas for skeleta of products of simplices already cover the isotropic cubical-skeleton threshold after translating the symmetric dilating box, while earlier results on repeated averaging of orthotope face skeleta concern a different Minkowski operation; neither supplies this anisotropic persistence module and tied-width void-loss exponent. Rowlands, *Topology of complements of skeletons* (arXiv:2209.08434), studies complements of abstract polytopal skeleta, not the present anisotropic offset filtration. Computational cubical-persistence methods such as Hu, *MMPersistence* (arXiv:2602.15502), treat algorithms for general filtrations, not these explicit geometric formulas.

## Limitations
These formulas require an **axis-parallel convexifier**; rotating the box invalidates the coordinate factorization. They do not describe Euclidean-ball offsets, arbitrary polytopal skeleta, or non-box convexifiers. The homotopy statement is not a claim that the offsets are combinatorially cubical complexes; it is a deformation-retraction statement. Historical originality is based on accessible primary literature and mathematical-record comparison, not a proof that no unindexed equivalent theorem exists. No independent external audit was performed.

## References
1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, October 19, 2026, https://arxiv.org/abs/2610.26744.
2. Rowan Rowlands, *Topology of complements of skeletons*, arXiv:2209.08434, September 18, 2022, https://arxiv.org/abs/2209.08434.
3. Chuan-Shen Hu, *MMPersistence: A mathematical morphology-oriented software library for computing persistent homology on cubical complexes*, arXiv:2602.15502, February 17, 2026, https://arxiv.org/abs/2602.15502.
4. Kaczynski, Mischaikow and Mrozek, *Computational Homology*, Springer, 2004 (standard cubical-chain background).
