# A randomly clipped Poisson field of universal random intervals

## Finding

Let \(I_i=[L_i,R_i]\), \(1\le i\le n\), be \(n\) independent intervals obtained from two iid uniform endpoints on \([0,1]\), each pair sorted. Two vertices are adjacent precisely when their intervals intersect; a vertex is *universal* if it is adjacent to every other vertex. Define
\[
Q_n=\min_i R_i,\qquad P_n=\max_i L_i,\qquad A_n=\sqrt n Q_n,\qquad B_n=\sqrt n(1-P_n).
\]
For each universal interval record the point \((\sqrt n L_i,\sqrt n(1-R_i))\), and let \(\Xi_n\) denote the resulting finite point measure.

**Theorem.** As \(n\to\infty\), \((A_n,B_n,\Xi_n)\) converges jointly to \((A,B,\Xi)\), where \(A,B\) are independent Rayleigh-type variables with \(\Pr(A>t)=\Pr(B>t)=e^{-t^2}\) for \(t\ge0\). Given \(A=a,B=b\), the measure \(\Xi\) is a homogeneous Poisson point process of intensity \(2\,dx\,dy\) on the random rectangle \([0,a]\times[0,b]\), and is zero off that rectangle. In particular, given \(A,B\), the number of universal vertices converges to a Poisson law of mean \(2AB\), and, conditional on the two thresholds and the count, the scaled endpoint deficits are iid uniform over that rectangle.

The limiting count \(U=\Xi(\mathbb R_+^2)\) has
\[
\Pr(U=k)=\frac{2^{k+1}(k+1)((k+1)!)^2}{(2k+3)!},\qquad k=0,1,2,\ldots,
\]
so \(\Pr(U=0)=1/3\), \(\Pr(U=1)=4/15\), \(\mathbb EU=\pi/2\), and \(\operatorname{Var}U=\pi/2+4-\pi^2/4\). This theorem resolves the *locations* as well as the count. The classical finite-\(n\) probability \(\Pr(U_n>0)=2/3\) is previously known and is **not** claimed as new.

## Assumptions and scope

The conclusion holds for all independent identically distributed endpoint pairs from a common atomless distribution after applying its common cumulative distribution function to all endpoints. Thus the coordinates in the theorem are *quantile coordinates*; their Euclidean scaling need not hold in the original coordinate system if the endpoint density is irregular. Intervals are closed; with atomless endpoints, boundary equalities occur with probability zero. For every \(n\ge2\), the definition of universal includes all \(n-1\) other vertices. The limit is weak convergence of the two real scalars jointly with the finite point measure (vague convergence plus tightness of total mass).

## Proof

**Exact geometric identity.** Because intervals \([l,r]\) and \([l_j,r_j]\) intersect precisely when \(l\le r_j\) and \(r\ge l_j\), the universal-vertex condition is exactly
\[
L_i\le Q_n\quad\text{and}\quad R_i\ge P_n.
\]
The inequalities for \(j=i\) hold automatically. This identity justifies the random rectangle directly without a limiting approximation.

**Three independent corner clouds.** A sorted uniform endpoint pair has constant density \(2\) on the triangle \(0<l<r<1\). Consider the small-corner cloud with coordinates \((\sqrt n l,\sqrt n r)\) in the wedge \(0<x<y\), the large-corner cloud with coordinates \((\sqrt n(1-r),\sqrt n(1-l))\) in the same wedge, and the spanning cloud with coordinates \((\sqrt n l,\sqrt n(1-r))\) in the nonnegative quadrant. On every fixed compact set, the three preimage regions in the original triangle are disjoint once \(n\) is large. Each mapped region has area divided by \(n\) and hence expected local point intensity \(2\,dx\,dy\). For any compactly supported nonnegative continuous test functions on the three regions, independence over the \(n\) sampled intervals gives the joint Laplace functional
\[
\left(1-\frac2n\sum_{j=1}^3\int (1-e^{-f_j})\,dx\,dy\right)^n
\longrightarrow
\prod_{j=1}^3\exp\!\left[-2\int (1-e^{-f_j})\,dx\,dy\right].
\]
Consequently these three corner clouds jointly converge, on bounded windows, to independent homogeneous Poisson point processes of intensity \(2\), restricted to their respective wedges/quadrant.

**Extreme corners.** The minimum second coordinate of the small-corner limit is \(A\), and that of the large-corner limit is \(B\). Because the wedge below height \(t\) has area \(t^2/2\), \(\Pr(A>t)=\Pr(B>t)=e^{-t^2}\). These two variables are independent and independent of the limiting spanning cloud. Directly, for \(t,s\ge0\) fixed and sufficiently large \(n\),
\[
\Pr(A_n>t,B_n>s)=\left(1-\frac{t^2+s^2}n\right)^n\longrightarrow e^{-(t^2+s^2)},
\]
which also establishes tightness of the two thresholds.

**Clipping and total-mass convergence.** The geometric identity says exactly that \(\Xi_n\) is the spanning-corner cloud clipped to \([0,A_n]\times[0,B_n]\). The limiting independent Poisson cloud has almost surely no points on the rectangle boundary. On the event \(A_n,B_n\le T\), for any fixed \(T\), the operation of clipping is continuous at almost every limiting configuration on a compact window containing the rectangle. The complement has probability at most \(2(1-T^2/n)^n\), asymptotically at most \(2e^{-T^2}\). Taking \(T\to\infty\) yields joint weak convergence of \((A_n,B_n,\Xi_n)\) and of total masses. Given the thresholds, the limiting spanning cloud has Poisson intensity \(2\) in the clipped rectangle; this proves the claimed marked conditional law.

**Count distribution.** The joint density of \((A,B)\) is \(4ab e^{-a^2-b^2}\). Therefore
\[
\Pr(U=k)=\frac1{k!}\int_0^\infty\!\int_0^\infty
4ab e^{-(a+b)^2}(2ab)^k\,da\,db.
\]
With \(s=a+b\) and \(v=a/s\), this integral separates into a Gamma integral and a Beta integral, giving
\[
\Pr(U=k)=\frac{2^{k+1}(k+1)((k+1)!)^2}{(2k+3)!}.
\]
The first two moments follow from \(U\mid A,B\sim\operatorname{Poisson}(2AB)\), using \(\mathbb EA=\sqrt\pi/2\) and \(\mathbb EA^2=1\). In particular, \(\mathbb EU=\pi/2\), \(\operatorname{Var}U=\mathbb E(2AB)+\operatorname{Var}(2AB)=\pi/2+4-\pi^2/4\). This is a *genuinely mixed* Poisson law and not an ordinary Poisson law.

## Verification

The standalone `CHECK.py` exhaustively enumerates every perfect matching of the \(2n\) endpoint ranks for \(2\le n\le6\) (equivalent to the uniform endpoint law) and independently checks the geometric identity for every matching. For each \(n\) it reproduces the established finite probability \(\Pr(U_n>0)=2/3\). Exact-arithmetic checks verify the stated limiting probabilities at three low counts and their normalization to numerical precision. Separate seeded simulations at \(n=120\) and \(n=700\) check convergence toward the predicted absence probability and mean. These finite and numerical checks support, but do not substitute for, the point-process proof above. The verification does not assert novelty or independent certification.

## Relationship to prior work

The 1990 article by Justicz, Scheinerman and Winkler establishes the probability that some sampled interval meets all the others, and the 2015 preprint by Iliopoulos recounts its finite-sample \(2/3\) result and the random interval graph model. The latter's relevant full text (degree section and proof) was inspected. The contribution assessed here is the **joint extreme-boundary and marked-Poisson spatial limit in quantile endpoint coordinates**; the event probability, and any pre-existing unmarked count formulas, are excluded from novelty claims. A 2026 article by Sarkar focuses explicitly on how many intervals intersect all others; its full text could not be inspected, so any unmarked count formula must be treated as potentially covered. The marked conditional geometry is stronger than a marginal count law, but historical priority for that stronger claim remains subject to independent literature review.

## Limitations

The result is asymptotic and assumes independent endpoint pairs drawn from one common atomless distribution. It does not provide finite-sample error bounds for the marked-point-process approximation, and it does not claim a Euclidean-length limit for arbitrary nonuniform original endpoint distributions. The classical probability of at least one universal interval is not new. A plausible recent count-distribution treatment and the original 1990 full text were not accessible for complete comparison; no independence of scholarly verification is asserted.

## References

- J. Justicz, E. R. Scheinerman, P. M. Winkler, *Random Intervals*, American Mathematical Monthly **97** (1990), 881–889. DOI: `10.1080/00029890.1990.11995679`.
- V. Iliopoulos, *Random Interval Graphs*, arXiv:`1507.06275v1`, first posted 2015-07-22; Section 4.3 and bibliography.
- E. R. Scheinerman, *Random Interval Graphs*, Combinatorica **8** (1988), 357–371. DOI: `10.1007/BF02189092`.
- J. Sarkar, *How Many Random Intervals Intersect All Others?*, Resonance **31** (2026), 739–751. DOI: `10.1007/s12045-026-1997-0`. Cited for related count-distribution scope; full text not inspected.
