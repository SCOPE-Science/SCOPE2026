# Sharp mean-distance optimization for one-loop hub-and-spoke metric networks

## Finding
Fix an integer \(k\ge1\) and total arclength \(L>0\). A one-loop hub-and-spoke graph is formed by gluing the root of each of \(k\) intervals to a single marked point of one circular loop. The unique minimum of the average intrinsic geodesic distance over all positive allocations of its \(k+1\) edge lengths occurs at *equal* arm lengths and a particular strictly positive loop length. Writing \(t\) for the pendant fraction of the total length, the unique optimum is
\[
t_k=\frac{k(k-4+2\sqrt{k^2-2k+2})}{3k^2-8},\quad
C=L(1-t_k),\quad a_1=\cdots=a_k=\frac{Lt_k}{k}.
\]
The sharp minimum is \(L f_k(t_k)\), with
\[
f_k(t)=\frac{(1-t)^3}{4}+\frac{t(1-t)^2}{2}+\frac{t^2}{k}-\frac{2t^3}{3k^2}.
\]
For a single pendant, \(t_1=1/5\) and the minimum equals \(17L/75\). As the number of arms grows, the best loop share shrinks: \(1-t_k=2/k-3/k^2+O(k^{-3})\), and
\[
\frac{\min \mathbb E d(X,Y)}{L}=\frac1k-\frac{8}{3k^2}+O(k^{-3}).
\]
For every finite \(k\), a strictly positive loop improves on the pure star limit; a positive family with equal arms attains the bound without degeneracy.

## Assumptions and scope
All edge lengths are strictly positive. The loop is a genuine geodesic circle of length \(C\); all \(k\) pendant intervals meet it at *one and the same* root vertex and have no additional intersections. Their lengths are \(a_i>0\), and \(L=C+\sum_{i=1}^k a_i\). Points \(X,Y\) are independent and uniform with respect to normalized one-dimensional arclength measure on the full metric graph. Distances are shortest-path (intrinsic) distances. The theorem optimizes lengths only within this fixed topological class, not the location of several independent attachments or general unicyclic metric graphs. The number of pendant arms \(k\) is a fixed positive integer in every minimization.

## Proof
Write \(T=\sum_i a_i\), \(S_2=\sum_i a_i^2\), and \(S_3=\sum_i a_i^3\). The ordered-pair distance integral is calculated by partitioning the two chosen points by edges. For two loop points, the mean shorter-arc distance is \(C/4\), so their integral contribution is \(C^3/4\). For two points on the same arm of length \(a_i\), their contribution is \(a_i^3/3\). For two distinct arms \(i,j\), distance is the sum of the two distances from the hub, giving the *ordered* contribution \(a_i^2a_j+a_ia_j^2\). Finally, the ordered loop-arm contribution for arm \(i\) is \(Ca_i^2+C^2a_i/2\), since a loop point lies on average a distance \(C/4\) from the hub. Summing gives the exact identity
\[
L^2\mathbb E d(X,Y)=\frac{C^3}{4}+\frac{C^2 T}{2}+L S_2-\frac{2}{3}S_3.\tag{1}
\]
Here the identity \(\sum_{i<j}(a_i^2a_j+a_ia_j^2)=T S_2-S_3\) has been used.

Fix the loop length and total pendant length. For a chosen pair of arms \(x,y\) with sum \(s=x+y\), the variable portion of the right side of (1) is
\[
L(x^2+y^2)-\frac23(x^3+y^3)=Ls^2-\frac23s^3-2(L-s)xy.\tag{2}
\]
Because \(L-s\ge C>0\), replacing unequal lengths by their average strictly decreases the distance integral (it increases \(xy\)). By successive pairwise equalization, or compactness and a balancing argument, the unique minimizer at fixed \(C,T\) has \(a_i=T/k\) for all \(i\). This equality is strict up to permutations and does not require any differentiability assumption at the boundary.

Put \(t=T/L\in(0,1)\). Substituting \(C=L(1-t)\) and \(a_i=Lt/k\) into (1) gives \(\mathbb E d(X,Y)=L f_k(t)\) with the displayed cubic. Its derivative is
\[
f_k'(t)=\frac{(3k^2-8)t^2+(8k-2k^2)t-k^2}{4k^2}.\tag{3}
\]
When \(k=1\), \(f_1'(t)=-(t-1)(5t-1)/4\), so its unique minimum in \((0,1)\) is at \(1/5\); the boundary values are both larger. For \(k\ge2\), the quadratic numerator in (3) has positive leading coefficient, negative constant coefficient, and precisely one positive root; moreover \(f_k'(0)=-1/4\) and \(f_k'(1)=2(k-1)/k^2>0\). Hence its sole positive zero lies in \((0,1)\), where the derivative changes from negative to positive. Solving that quadratic yields the radical \(t_k\), proving unique global optimality and attainability for every fixed \(k\).

For monotonicity in \(k\), the first two explicit roots satisfy \(t_1=1/5<t_2=\sqrt2-1\); for real \(k\ge2\), \(\partial_k f_k'(t)=-2t(k-2t)/k^3<0\) on \((0,1)\). The unique positive derivative root thus increases strictly with \(k\). For \(k\ge2\), the minimum \(f_k(t_k)\) decreases strictly with \(k\) because \(\partial_k f_k(t)=-t^2(k-4t/3)/k^3<0\); the same strict comparison between \(k=1\) and \(k=2\) follows directly from \(f_2(t)-f_1(t)=-t^2(1-t)/2<0\). Expanding the displayed radical at \(1/k=0\) gives \(t_k=1-2/k+3/k^2+O(k^{-3})\) and substitution into \(f_k\) yields \(f_k(t_k)=1/k-8/(3k^2)+O(k^{-3})\).

## Verification
The standalone Python checker recomputes (1), tests the balancing inequality for random unequal arm configurations, samples independent arclength-uniform point pairs on different graph configurations with shortest-path distances evaluated independently of (1), and verifies the optimum algebraically and numerically for \(1\le k\le50\). Its passing output is `ONE_LOOP_BOUQUET_OPTIMAL_MEAN_DISTANCE_OK`. The proof of the theorem is analytical; random checks do not certify infinitely many arm counts.

## Relationship to prior work
The continuous network mean-distance concept goes back to Doyle and Graver (1982). Ruchansky and collaborators (2015) motivate Wiener-distance network design in the discrete setting. Garijo, Márquez, and Silveira (2021 preprint/2023 publication) give a general algorithm for continuous mean distance of weighted graphs, and Baptista, Kennedy, and Mugnolo (2023 preprint/2024 publication) establish universal metric-graph bounds and optimal equilateral flower graphs among *all* graphs with fixed edge count. Those broader graph-theoretic tools are not claimed as new. The present claim is the explicit strict one-loop-plus-star constrained optimizer, its universal arm equalization, and the all-\(k\) exact length and asymptotic laws. The general all-graph flower bound does not imply this constrained optimum; its extremizer has a different topology. Historical coverage by older specialized shape formulas is a residual risk.

## Limitations
The cycle and all pendants must meet at one common hub; arbitrary tree branches, multiple attachment locations, Euclidean straight-line network embeddings, and arbitrary unicyclic graphs are not covered. The old Doyle--Graver 1982 article could not be materially inspected in full, so historical priority is provisional. The exact formulas were derived and checked within the stated model; independent external mathematical review has not been performed.

## References
- J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B 9 (1982), 177–179, DOI: 10.1068/b090177 (month/year available, precise public day not independently verified).
- J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI: 10.1002/jgt.3190060410.
- N. Ruchansky et al., *The Minimum Wiener Connector*, arXiv:1504.00513, first posted 2015-04-02.
- D. Garijo, A. Márquez, R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676 (2021), and Results in Mathematics 78 (2023), 139.
- L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952 (2023), and Journal of Geometric Analysis 34 (2024), 137.
