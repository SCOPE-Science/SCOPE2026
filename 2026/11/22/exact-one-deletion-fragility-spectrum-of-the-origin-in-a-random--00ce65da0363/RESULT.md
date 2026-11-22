# Exact one-deletion fragility spectrum of the origin in a random inscribed polygon

## Finding

For every integer \(n\ge4\), sample \(n\) independent uniform directions in the plane. For a configuration whose convex hull contains the origin, call a vertex *pivotal* when removing that vertex destroys containment; for a configuration not containing the origin, define the pivotal count to be zero. Write this count \(K_n\). Its complete, finite-sample distribution is

\[
\begin{aligned}
\Pr(K_n=0)&=1-\frac{n(n-3)}{2^{n-1}},\\
\Pr(K_n=1)&=\frac{n(n-4)}{2^{n-1}},\\
\Pr(K_n=2)&=\frac{n}{2^{n-1}}.
\end{aligned}
\]

In particular \(K_n\le2\) almost surely, independently of sample size. Conditional on the hull containing the origin, its probability of surviving **every** single-vertex removal is
\[
\Pr(\text{one-deletion robust}\mid 0\in\operatorname{conv}\{X_1,\ldots,X_n\})
=\frac{2^{n-1}-n(n-2)}{2^{n-1}-n}.
\]
For \(n=4\), every origin-containing configuration has two pivotal vertices; for \(n=5\), the conditional probability of full single-deletion robustness is \(1/11\).

## Assumptions and scope

Let \(X_1,\ldots,X_n\) be iid uniform on the unit circle, with \(n\ge4\). Probabilities are unchanged when the \(X_i\) are replaced by independent nonzero planar vectors with iid uniform directions and any almost surely positive radii (possibly dependent on the directions): origin containment depends only on the rays. The event that the origin lies on a hull boundary has probability zero; all statements concern the ordinary convex hull. Let \(K_n\) count indices \(i\) for which origin containment holds for all \(n\) vectors but fails after omission of \(i\), and set \(K_n=0\) on the complement of original containment.

## Proof

Order the direction angles cyclically and write their normalized successive gaps as \(G_1,\ldots,G_n\), with \(\sum_iG_i=1\). Their joint distribution is the uniform Dirichlet law \(\operatorname{Dirichlet}(1,\ldots,1)\). The origin lies strictly inside the hull exactly when each \(G_i<1/2\), since otherwise all directions fit in an open semicircle. Deleting the direction between gaps \(G_{i-1}\) and \(G_i\) replaces those two gaps by their sum. Thus pivotality for that vertex is the event
\[
E_i=\left\{\max_jG_j<\frac12,\quad G_{i-1}+G_i>\frac12\right\}.
\]
The strict inequalities can be used because all boundaries have probability zero.

Any two events \(E_i,E_j\) whose pairs of adjacent gap coordinates are disjoint cannot both occur: their sums would exceed one. Among any three distinct edges of the cyclic gap graph with \(n\ge4\), two have disjoint endpoint sets. It follows that at most two of the events can occur, and whenever two occur, their corresponding cyclic edges must be adjacent.

A distinguished sum \(S=G_{i-1}+G_i\) has \(\operatorname{Beta}(2,n-2)\) distribution. Direct integration of its density \((n-1)(n-2)s(1-s)^{n-3}\) gives
\[
\Pr(S>1/2)=\frac{n}{2^{n-1}}.
\]
The portion of this event violating original containment consists, disjointly, of \(G_{i-1}>1/2\) and \(G_i>1/2\). Each has probability \(2^{-(n-1)}\). Therefore
\[
\Pr(E_i)=\frac{n-2}{2^{n-1}},\qquad
\mathbb E K_n=\frac{n(n-2)}{2^{n-1}}.
\]

For two adjacent pivotality events, put \(x\) equal to their shared gap. The conditions are \(0<x<1/2\), and each of its two neighboring gaps must exceed \(1/2-x\). After subtracting these two lower bounds, the total slack across all other gap coordinates is exactly \(x\). The Dirichlet density is \((n-1)!\) on the simplex; integrating the \((n-2)\)-dimensional residual simplex gives
\[
\Pr(E_i\cap E_{i+1})=(n-1)\int_0^{1/2}x^{n-2}\,dx=\frac1{2^{n-1}}.
\]
There are \(n\) unordered adjacent pairs of gap-edges. Since no configuration supports three pivotal events, their intersection events are pairwise disjoint, yielding
\[
\Pr(K_n=2)=\sum_{i=1}^n\Pr(E_i\cap E_{i+1})=\frac{n}{2^{n-1}}.
\]
The equation \(\mathbb E K_n=\Pr(K_n=1)+2\Pr(K_n=2)\) gives the probability for one pivotal vertex, and normalization gives the probability for zero.

Finally, Wendel's planar semicircle probability is \(\Pr(0\notin\operatorname{conv}\{X_1,\ldots,X_n\})=n/2^{n-1}\). Configurations with no pivotal vertices comprise both initially failing configurations and robust configurations. Subtracting the former from \(\Pr(K_n=0)\), and dividing by \(1-n/2^{n-1}\), gives the conditional robustness formula. This completes the proof.

## Verification

The accompanying Python program `verify.py` checks the equivalence of cyclic-gap and direct-deletion definitions on exhaustive positive and nonnegative integer-gap grids for four through seven points, checks \(K_n\le2\) on those grids, verifies the exact rational identities for \(4\le n\le200\), and performs independently seeded auxiliary simulations for \(4\le n\le10\). It is executable with Python standard library as `python verify.py`. The calculations support but are not required for the continuous proof. The half-gap boundary case is excluded mathematically by absolute continuity.

## Relationship to prior work

Wendel's classical theorem supplies the one-time probability of containing the origin, not the distribution of how many deletions destroy that event. Kabluchko, Vysotsky and Zaporozhets study absorption probabilities for random walks and Weyl chambers and recover Wendel's identity; their framework does not assert the cyclic deletion spectrum above. Fodor, Montenegro Pinzón and Vígh study Wendel-type probabilities for spindle-convex hulls, a different containment model. The new content is the exact three-point deletion-fragility law and the deterministic two-pivotal bound. These comparisons are not a guarantee of historical priority against unidentified equivalent semicircle-coverage formulations.

## Limitations

The law is for iid uniform directions and a single deletion. It is not asserted for angularly biased distributions, multiple deletions, higher-dimensional spheres, or nonuniform direction dependence. An exhaustive search of all historical semicircle-coverage formulations was not possible; priority remains subject to expert literature confirmation. No independent mathematical audit has been performed.

## References

1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–111. DOI: https://doi.org/10.7146/math.scand.a-10655. Original full text: https://scispace.com/pdf/a-problem-in-geometric-probability-4dxha13um7.pdf.
2. Z. Kabluchko, V. Vysotsky and D. Zaporozhets, *Convex hulls of random walks, hyperplane arrangements, and Weyl chambers*, preprint (2015), https://arxiv.org/abs/1510.04073.
3. F. Fodor, N. A. Montenegro Pinzón and V. Vígh, *On Wendel’s equality for intersections of balls*, Aequationes Mathematicae 97 (2023), 439–451; online 2022. https://doi.org/10.1007/s00010-022-00912-3.
