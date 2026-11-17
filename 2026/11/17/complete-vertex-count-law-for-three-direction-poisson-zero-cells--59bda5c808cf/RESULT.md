# Complete vertex-count law for three-direction Poisson zero cells

## Finding
Consider three independent stationary Poisson families of lines in the Euclidean plane. Their unit normals are
\[
n_1=(1,0),\qquad n_2=(-1/2,\sqrt3/2),\qquad n_3=(-1/2,-\sqrt3/2),
\]
so that \(n_1+n_2+n_3=0\). In family \(i\), the signed offsets \(t\) in the equations \(n_i\cdot x=t\) form a rate-\(\lambda_i\) Poisson process on \(\mathbb R\); assume \(\lambda_i>0\) independently for \(i=1,2,3\). Let \(C\) be the almost surely bounded zero cell containing the origin, and let \(N\) be its number of sides.

For each nonempty subset \(I\subseteq\{1,2,3\}\), define
\[
L_I=\sum_{i\in I}\lambda_i,\qquad
b_I=\left(\prod_{j\in I}\frac{\lambda_j}{L_I}\right)
     \left(\prod_{j\notin I}\frac{\lambda_j}{\lambda_j+L_I}\right).
\]
Put \(u_k=\sum_{|I|=k}b_I\) for \(k=1,2,3\), and \(s=\sum_{i=1}^3 b_{\{i\}}^2\). Then the complete side-count law is
\[
\begin{aligned}
\Pr(N=3)&=2u_3,\\
\Pr(N=4)&=2u_2-6u_3+s,\\
\Pr(N=5)&=2u_1-4u_2+6u_3-2s,\\
\Pr(N=6)&=1-2u_1+2u_2-2u_3+s.
\end{aligned}
\]
No other side count has positive probability, and \(\mathbb E N=6-2u_1\). All these expressions are independent of a common rescaling of the three rates.

For equal rates, the distribution simplifies to
\[
\boxed{\Pr(N=3)=\frac2{27},\quad
\Pr(N=4)=\frac{67}{144},\quad
\Pr(N=5)=\frac{25}{72},\quad
\Pr(N=6)=\frac{49}{432}}.
\]
In particular \(\mathbb EN=9/2\). This is the **zero-cell**, or area-weighted, law and must not be confused with the distribution of a uniformly selected **typical** cell.

## Assumptions and scope
The three line families have exactly the stated directions and independent positive offset intensities. The zero cell is the cell containing the deterministic origin; the origin almost surely lies on no line. Counts refer to facets of the bounded convex polygon; intersections in which three supporting lines meet have probability zero. The statement applies to arbitrary positive \(\lambda_1,\lambda_2,\lambda_3\), including strongly unequal rates, but not to additional line directions, non-Poisson offsets, or unbounded zero cells.

## Proof
**Reduction to six independent exponential gaps.** For each \(i\), let \(A_i\) be the smallest positive offset and \(-B_i\) the largest negative offset of the corresponding Poisson process. By disjoint-increment independence, the six variables \(A_1,B_1,A_2,B_2,A_3,B_3\) are independent, and \(A_i,B_i\) each have exponential rate \(\lambda_i\). Every other line in family \(i\) lies farther from the origin on the same side, hence is redundant. Thus
\[
C=\{x\in\mathbb R^2:-B_i\le n_i\cdot x\le A_i\ \text{for }i=1,2,3\}.
\]
Its boundedness follows because the six inequalities bound the two-dimensional plane and all gaps are finite and positive.

**Exact facet criteria.** Set \(y_i=n_i\cdot x\). As the normals add to zero, \(y_1+y_2+y_3=0\), and any triple satisfying this identity comes from exactly one planar \(x\). For distinct \(i,j,k\), the upper bound \(y_i\le A_i\) is redundant precisely when
\[
E_i=\{A_i>B_j+B_k\},
\]
and the lower bound \(y_i\ge-B_i\) is redundant precisely when
\[
F_i=\{B_i>A_j+A_k\}.
\]
For example, the other two lower bounds imply \(y_i=-y_j-y_k\le B_j+B_k\); if \(A_i<B_j+B_k\), the upper bound is attained by a feasible point and supports a genuine nonzero-length facet except on a null equality event. The lower criterion is symmetric. Consequently
\[
N=6-\sum_{i=1}^3(\mathbf1_{E_i}+\mathbf1_{F_i})
\]
almost surely.

**Joint redundancy probabilities.** For any nonempty \(I\), conditional on \(B_1,B_2,B_3\), independence of the \(A_i\) gives
\[
\Pr\left(\bigcap_{i\in I}E_i\mid B_1,B_2,B_3\right)
=\exp\left[-\sum_{j=1}^3\Big(\sum_{i\in I,\ i\ne j}\lambda_i\Big)B_j\right].
\]
Integrating the three exponential Laplace transforms yields
\[
\Pr\left(\bigcap_{i\in I}E_i\right)
=\prod_{j=1}^3\frac{\lambda_j}{\lambda_j+L_I-\lambda_j\mathbf1_{\{j\in I\}}}=b_I.
\]
Interchanging \(A\) and \(B\) proves the identical formula for the \(F\)-events.

**Separation of upper and lower mechanisms.** For \(i\ne j\), events \(E_i\) and \(F_j\) cannot coexist: the first implies \(A_i>B_j\), whereas the second implies \(B_j>A_i\). For a fixed \(i\), \(E_i\) involves exactly the variables \(A_i,B_j,B_k\), while \(F_i\) involves \(B_i,A_j,A_k\), so these two events are independent, with
\[
\Pr(E_i\cap F_i)=b_{\{i\}}^2.
\]
Such a matched mixed event cannot coexist with any further redundancy. Hence the total probability of mixed events is \(s\), all of which remove exactly two facets.

For the upper events alone, inclusion-exclusion gives probability \(u_3\) of exactly three redundant facets, \(u_2-3u_3\) of exactly two, and \(u_1-2u_2+3u_3\) of exactly one. The lower events have the same distribution. Their nonempty pure configurations are disjoint from each other, except for the separate matched-mixed events already counted. Thus the total redundant-facet count \(K=6-N\) obeys
\[
\begin{aligned}
\Pr(K=3)&=2u_3,\\
\Pr(K=2)&=2(u_2-3u_3)+s,\\
\Pr(K=1)&=2(u_1-2u_2+3u_3)-2s,\\
\Pr(K=0)&=1-2u_1+2u_2-2u_3+s.
\end{aligned}
\]
The third displayed expression simplifies to the asserted formula. Taking expectations of the six redundancy indicators gives \(\mathbb EN=6-2u_1\), without needing any cancellations among the cases.

**Equal intensities.** With \(\lambda_1=\lambda_2=\lambda_3\), the formula for \(b_I\) yields \(b_{\{i\}}=1/4\), \(b_{\{i,j\}}=1/12\), and \(b_{\{1,2,3\}}=1/27\). Hence \(u_1=3/4\), \(u_2=1/4\), \(u_3=1/27\), and \(s=3/16\). Exact rational substitution proves the four stated values and the mean \(9/2\).

## Verification
The reproducible checker in `checks/verify.py` validates the exact rational values, samples one million independent six-gap configurations for multiple unequal-intensity choices, and independently reconstructs polygon vertices by intersecting supporting lines for 15,000 configurations. No generic high-dimensional or continuous-angle approximation is involved. The analytic theorem rests on the foregoing exact probabilities, not on finite simulation.

## Relationship to prior work
Hilhorst and Calka (2008) examine many-sided **Crofton zero cells** in the isotropic continuous-direction Poisson line process, including large-side-count asymptotics, rather than the finite four-type law here. Hug and Schneider (2010) study large-volume limit shapes of Poisson hyperplane cells, not this polygonal facet-count distribution. Heerten, Krecklenberg and Thäle (2022) derive triangle probabilities for the **typical cell** of selected directional processes; Heerten, Hübner and Thäle (2023) determine its complete three-direction typical-cell sidedness law. These results are not automatically zero-cell laws. A zero cell is area-weighted: for every side count \(k\),
\[
\Pr(N_{\mathrm{zero}}=k)
=\frac{\Pr(N_{\mathrm{typ}}=k)\,\mathbb E[\operatorname{area}(C_{\mathrm{typ}})\mid N_{\mathrm{typ}}=k]}{\mathbb E\operatorname{area}(C_{\mathrm{typ}})}.
\]
Knowledge of the typical-cell probabilities alone does not specify the conditional areas. For equal directional rates, the 2023 typical-cell law is \((2/9,7/12,1/6,1/36)\), whereas the zero-cell probabilities proved here are \((2/27,67/144,25/72,49/432)\).

## Limitations
The result assumes independent stationary Poisson offset processes, three orientations separated by \(60\) degrees as unoriented lines, and positive rates. Historical priority beyond the cited and searched sources is not independently certified. The theorem does not give the conditional area distribution for each side count or extend to four or more line directions. The numerical checker does not replace proof, and no independent mathematical audit has been performed.

## References
1. H. J. Hilhorst and P. Calka, *Random line tessellations of the plane: statistical properties of many-sided cells*, arXiv:0802.1869, first public February 13, 2008. https://arxiv.org/abs/0802.1869
2. D. Hug and R. Schneider, *Large faces in Poisson hyperplane mosaics*, arXiv:1010.2333, first public October 12, 2010. https://arxiv.org/abs/1010.2333
3. N. Heerten, J. Krecklenberg and C. Thäle, *The proportion of triangles in a class of anisotropic Poisson line tessellations*, arXiv:2209.14121, first public September 28, 2022. https://arxiv.org/abs/2209.14121
4. N. Heerten, J. Hübner and C. Thäle, *Vertex number of the typical cell in a tri-directional Poisson line tessellation*, arXiv:2309.12771, first public September 22, 2023. https://arxiv.org/abs/2309.12771
