# Parity-sharp covering threshold for simplex-normal planks

## Finding
Fix an integer \(d\ge 2\), and let \(u_0,\ldots,u_d\) be the unit vertex vectors of a regular simplex centered at the origin in \(\mathbb R^d\), so that \(\langle u_i,u_j\rangle=-1/d\) for distinct indices. For \(t\ge0\), put
\[
P_i(t)=\{x\in\mathbb R^d:|\langle u_i,x\rangle|\le t\},\qquad B_d=\{x:\|x\|_2\le1\}.
\]
The exact threshold for the \(d+1\) congruent, centrally positioned planks with these fixed normals to cover the unit ball is
\[
\boxed{\inf\{t\ge0:B_d\subseteq\bigcup_{i=0}^dP_i(t)\}=\tau_d=\begin{cases}d^{-1/2},&d\text{ odd},\\\frac{1}{\sqrt{d+2}},&d\text{ even}.\end{cases}}
\]
Equivalently, zones about the corresponding great subspheres cover the unit sphere precisely when their common *full spherical width* is at least \(2\arcsin\tau_d\). The maximal distance from a unit direction to the nearest great subsphere is \(\arcsin\tau_d\).

All extremal directions are explicit. Set \(m=d+1\), \(p=\lfloor m/2\rfloor\), and \(q=\lceil m/2\rceil\). For any subset \(I\subset\{0,\ldots,d\}\) with \(|I|=p\), let \(J\) be its complement and set
\[
y_i=\begin{cases}\tau_d q/p,&i\in I,\\-\tau_d,&i\in J,\end{cases}\qquad
x_I=\frac d{d+1}\sum_{i=0}^d y_i u_i.
\]
Then \(\|x_I\|_2=1\), and the complete set of unit maximizers of \(\min_i|\langle u_i,x\rangle|\) is \(\{\pm x_I:|I|=p\}\). There are exactly \(\tfrac12\binom{d+1}{(d+1)/2}\) unoriented maximizing lines when \(d\) is odd, and exactly \(\binom{d+1}{d/2}\) when \(d\) is even. In the odd-dimensional case all \(d+1\) absolute projections agree; in the even-dimensional case the minority and majority projection magnitudes have ratio \((d+2)/d\).

## Assumptions and scope
All bodies and planks are Euclidean and closed. The simplex is regular, has unit vertex vectors, and is centered at the origin; neither translations of the planks nor variations of their normals are optimized. Width \(2t\) is the Euclidean distance between the bounding hyperplanes of one plank. A spherical zone of full angular width \(2\alpha\) consists of unit vectors whose angular distance to a great subsphere is at most \(\alpha\). The theorem concerns **the fixed simplex-normal arrangement**, not the globally best arrangement of \(d+1\) planks or zones, and assumes \(d\ge2\).

## Proof
**1. Tight-frame reduction.** Regular-simplex identities imply
\[
\sum_{i=0}^d u_i=0,\qquad \sum_{i=0}^d u_iu_i^{\mathsf T}=\frac{d+1}{d}I_d.
\]
For any unit \(x\), write \(y_i=\langle u_i,x\rangle\). Thus \(\sum_i y_i=0\) and \(\sum_i y_i^2=(d+1)/d\). Conversely, every real zero-sum vector \((y_0,\ldots,y_d)\) with that squared norm corresponds to a unit \(x\), uniquely reconstructed by \(x=\frac d{d+1}\sum_i y_i u_i\). This follows because the analysis map of the tight frame has range exactly the \(d\)-dimensional zero-sum subspace.

**2. Exact max-min reduction.** Put
\[
F_d=\max_{\|x\|_2=1}\min_{0\le i\le d}|\langle u_i,x\rangle|.
\]
The maximum exists by compactness and is positive: a generic unit direction has no vanishing projection. For such a direction, set \(h=\min_i|y_i|>0\) and \(b_i=y_i/h\). Then \(\sum_i b_i=0\), every \(|b_i|\ge1\), and
\[
h^2=\frac{(d+1)/d}{\sum_i b_i^2}.
\]
There must be \(p'\ge1\) positive and \(q'\ge1\) negative entries, with \(p'+q'=m=d+1\). Let the sum of the positive entries be \(s\), also the sum of the magnitudes of negative entries. Since all magnitudes are at least one, \(s\ge\max\{p',q'\}\). Cauchy--Schwarz on the two groups gives
\[
\sum_i b_i^2\ \ge\ \frac{s^2}{p'}+\frac{s^2}{q'}
\ \ge\ \frac{m\max\{p',q'\}}{\min\{p',q'\}}.
\]
Equality in both steps is possible and has an exact characterization: each sign group is constant in magnitude, every entry in the larger group has magnitude \(1\), and every entry in the smaller group has magnitude equal to the ratio of their cardinalities. In particular, the bound is attained for every sign partition. Among positive integers \(p',q'\) with sum \(m\), the quotient \(\max\{p',q'\}/\min\{p',q'\}\) is minimized only by the most balanced split.

If \(m\) is even (\(d\) odd), the minimum squared norm of \(b\) is \(m\), giving \(F_d^2=(m/d)/m=1/d\). If \(m\) is odd (\(d\) even), the minimum is \(m(m+1)/(m-1)=m(d+2)/d\), giving \(F_d^2=1/(d+2)\). The equality conditions identify every maximizer and yield the displayed vectors \(x_I\). When \(m\) is even, complementary subsets give opposite vectors and halve the unoriented count; when \(m\) is odd, choosing the minority-sign subset identifies one representative from each antipodal pair. This proves the classification and counts.

**3. Covering equivalence and sharpness.** By definition of \(F_d\), every unit vector lies in at least one \(P_i(F_d)\). Every point of the unit ball is a nonnegative contraction of a unit vector, so the same covering holds throughout \(B_d\). For any \(t<F_d\), an equality direction \(x_I\) satisfies \(|\langle u_i,x_I\rangle|\ge F_d>t\) for every \(i\), hence is uncovered. Therefore the covering threshold is exactly \(F_d=\tau_d\). On the sphere, angular distance to \(u_i^\perp\) is \(\arcsin|\langle u_i,x\rangle|\), giving the spherical formulation.

## Verification
The standalone Python 3 standard-library program `verify.py` checks the exact rational squared thresholds and equality witnesses for every integer \(2\le d\le50\), exhausts every possible sign-group cardinality in those dimensions, and verifies the unoriented equality counts. It also performs a seeded numerical sampling check of the upper bound for \(2\le d\le15\). Run it with `python3 verify.py`; successful completion prints `SIMPLEX_PLANK_PARITY_CHECKS_OK`. These finite tests are diagnostic only. The proof for every integer \(d\ge2\) is the dimension-free Cauchy--Schwarz argument above.

## Relationship to prior work
The 2026 note of Akopyan and Polyanskii gives a short proof of Ball's general symmetric plank theorem, supplying current motivation for the fixed-normal covering question [1]. The theorem in [1] gives a bound on the **sum** of relative widths for arbitrary coverings; for this unit-ball family its necessary condition is \((d+1)2t\ge2\), or \(t\ge1/(d+1)\), and it does not determine the exact simplex-normal threshold or equality directions. The full manuscript [1] was not accessible for detailed comparison; this is retained as a literature risk.

Jiang and Polyanskii [2] prove that total spherical zone width must be at least \(\pi\), with equality only for essentially coplanar zone normals in the indicated cyclic arrangement. Their bound implies \(\arcsin t\ge\pi/(2(d+1))\) for \(d+1\) congruent zones. It is sharp for this configuration when \(d=2\), but strictly weaker for every \(d\ge3\); it does not yield the even-dimensional sharp values. The open-access survey [3], especially its sections on Ball's plank theorem and Fejes Tóth's zone theorem, discusses these general inequalities without an exact fixed regular-simplex-normal classification. Bezdek, Fodor, Vígh, and Zarnócz [4] address zone-covering **multiplicity**, a distinct optimization objective. An online 2024 discussion [5] asks for the reversed \(\min_{\|x\|=1}\max_i|\langle u_i,x\rangle|\), which controls a different geometric quantity and does not by itself imply the higher even-dimensional max-min theorem. A direct implication of the existing literature should be separated from the even-dimensional conclusion: when \(d\) is odd, the equimodular balanced-sign construction in [5] (given for the reversed min-max problem), together with the tight-frame second moment, already yields the odd-dimensional value and its equality configurations. For \(d=2\), the general zone lower bound of [2] is exact, and three equally spaced planar great subspheres attain it. Those cases are included for a uniform geometric classification, not asserted as independently novel. The new quantitative component is the higher even-dimensional formula, the unequal two-level equality classification for every even \(d\ge4\), and its exact extremal-line count.

Searches of mathematical records and published literature found no displayed higher even-dimensional fixed-normal threshold or line-count formula, but absence from the inspected sources is not a proof of novelty.

## Limitations
No statement is made about translating the planks, varying their orientations, or minimizing widths among all zone configurations. The original 2026 note [1] was verified at the abstract level but its complete text could not be inspected through the available sources; an unindexed source or older special-case argument might overlap. The result is a deterministic theorem, not a computational classification in unbounded dimension; the analytic proof supplies the unbounded quantifier. Independent external validation has not been performed.

## References
[1] Arseniy Akopyan and Alexander Polyanskii, *A short proof of Ball's plank theorem*, arXiv:2609.36163v1, first posted 2026-09-28. https://arxiv.org/abs/2609.36163

[2] Zilin Jiang and Alexandr Polyanskii, *Proof of László Fejes Tóth's zone conjecture*, Geometric and Functional Analysis 27 (2017), 1367–1377; arXiv:1703.10550. https://arxiv.org/pdf/1703.10550

[3] William Verreault, *Plank theorems and their applications: A survey*, Bulletin of the London Mathematical Society 58 (2026), e70230, first published 2025-11-09. https://doi.org/10.1112/blms.70230

[4] András Bezdek, Ferenc Fodor, Viktor Vígh, Tamás Zarnócz, *On the Multiplicity of Arrangements of Congruent Zones on the Sphere*, Studia Scientiarum Mathematicarum Hungarica 61 (2024), 262–273. https://doi.org/10.1556/012.2024.04319

[5] *Minimum of the dot product over the vertices of a regular n-simplex*, Mathematics Stack Exchange, posted 2024-04-06. https://math.stackexchange.com/questions/4894174/minimum-of-the-dot-product-over-the-vertices-of-a-regular-n-simplex
