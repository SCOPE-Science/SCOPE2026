# An exact budget staircase for Poisson alarm detectors with false positives

## Finding

Consider any finite family of monitoring modalities, with positive extra genuine-call intensities \(a_i>0\) and background false-call intensities \(b_i>0\) per unit effort. Divide a fixed positive effort budget \(B\) among modalities. Declare a target present if and only if at least one counted call is obtained, and maximize the Youden criterion (sensitivity plus specificity minus one). Then the unique optimal *effective rate pair* follows the efficient lower convex boundary of the points \((a_i,b_i)\), moving in one direction as \(B\) increases. Every optimum can be implemented using at most two modalities, and two need be used only when their points are adjacent on that boundary.

More precisely, remove rate-duplicate and dominated points and discard interior points of collinear efficient faces. Let the remaining efficient boundary vertices be \((a_1,b_1),\ldots,(a_r,b_r)\), ordered so that \(a_1<\cdots<a_r\) and \(b_1<\cdots<b_r\). For \(r>1\), write
\[
s_j=\frac{b_{j+1}-b_j}{a_{j+1}-a_j},\qquad
c_j=\log\!\left(1+\frac{1}{s_j}\right),\qquad 1\le j<r.
\]
Here \(0<s_1<\cdots<s_{r-1}\), hence \(c_1>\cdots>c_{r-1}>0\).

The optimal effective pair lies strictly between vertices \(j\) and \(j+1\) precisely for
\[
\frac{c_j}{a_{j+1}}<B<\frac{c_j}{a_j}.
\]
On that interval, use only modalities \(j,j+1\), with the fraction assigned to \(j+1\) equal to
\[
\theta_j(B)=\frac{c_j/B-a_j}{a_{j+1}-a_j}.
\]
At \(B\le c_{r-1}/a_r\), use the highest-signal vertex \(r\); at \(B\ge c_1/a_1\), use the lowest-background vertex \(1\). For each interior vertex \(2\le j\le r-1\), use vertex \(j\) alone exactly when
\[
\frac{c_j}{a_j}\le B\le\frac{c_{j-1}}{a_j}.
\]
Each strict edge interval and each pure-vertex interval has nonempty interior. There are therefore exactly \(2r-1\) successive nonempty pure/mixed regimes along any nondegenerate strictly convex efficient boundary. If \(r=1\), its one effective pair is optimal at every positive budget. Mixtures using redundant collinear modalities may have the same optimal effective rates; the uniqueness claim refers to those rates and to the two-vertex implementation, not to all representations by effort vectors.

For a concrete three-modality configuration, take \((a,b)=(1,1/5),(2,1/2),(4,2)\). Define \(c_1=\log(13/3)\) and \(c_2=\log(7/3)\). The exact successive optimal regimes, with growing budget, are: high-rate modality only for \(B\le c_2/4\); a high–middle mixture for \(c_2/4<B<c_2/2\); middle alone for \(c_2/2\le B\le c_1/2\); a middle–low mixture for \(c_1/2<B<c_1\); and low-background modality alone for \(B\ge c_1\).

## Assumptions and scope

There is one binary true target state \(H\in\{0,1\}\) and \(m\ge1\) available sampling modalities. For each \(i\), allocate deterministic divisible effort \(t_i\ge0\), with \(\sum_i t_i=B>0\). Conditional on \(H=0\), its calls have a homogeneous Poisson count of mean \(b_it_i\). Conditional on \(H=1\), its calls have a homogeneous Poisson count of mean \((a_i+b_i)t_i\). Count processes for distinct modalities are conditionally independent and have nonnegative stationary rates \(a_i,b_i>0\); the state remains constant during sampling. For any zero allocation, its count is zero. The rule is a fixed pooled OR rule: a positive alarm occurs if any total count is nonzero. Costs per effort are incorporated into the rates, so one unit of effort has the same budget cost for every modality. The criterion is the population Youden score, not a sample-estimated or weighted diagnostic score.

The *efficient lower convex boundary* means the subset of the lower boundary of \(\operatorname{conv}\{(a_i,b_i)\}\) on which increasing \(a\) necessarily increases \(b\), after deleting any segment with nonpositive slope. Its first point has the smallest available \(b\) (choosing the largest \(a\) in case of a tie); its final point has the largest available \(a\) (choosing the smallest \(b\) in case of a tie). The vertices are the endpoints of maximal straight boundary segments. The description allows redundant input points and duplicated rates; for a strictly positive-slope efficient edge the endpoints are input modalities.

## Proof

**Step 1 (exact criterion).** By Poisson superposition and conditional independence, the no-call probabilities under absence and presence are respectively \(e^{-\sum_i b_it_i}\) and \(e^{-\sum_i(a_i+b_i)t_i}\). Therefore specificity is the first probability, sensitivity is one minus the second, and the Youden score is
\[
J(t)=e^{-\sum_i b_it_i}\big(1-e^{-\sum_i a_it_i}\big).
\]
Put \(a=\sum_i a_it_i/B\) and \(b=\sum_i b_it_i/B\). The feasible effective-rate pairs are exactly the convex hull of the input points, and
\[
J_B(a,b)=e^{-Bb}(1-e^{-Ba}).
\]
For every \(B>0\), this is strictly increasing in \(a>0\) and strictly decreasing in \(b>0\). Consequently its maximizer lies on the efficient lower boundary, and any boundary point can be represented by at most two adjacent boundary vertices. No discarded, strictly dominated mode can improve the score.

**Step 2 (uniqueness and edge stationary point).** Write the efficient boundary as \(b=f(a)\), where \(f\) is convex piecewise affine and strictly increasing, over \([a_1,a_r]\). On that interval
\[
L_B(a)=\log J_B(a,f(a))=-Bf(a)+\log(1-e^{-Ba}).
\]
The last term has strictly negative second derivative
\[
-\frac{B^2e^{Ba}}{(e^{Ba}-1)^2}<0.
\]
Thus \(L_B\) is strictly concave, so it has one and only one maximizer. On the interior of edge \(j\), with slope \(s_j\), the derivative equals
\[
L_B'(a)=B\left(\frac{1}{e^{Ba}-1}-s_j\right).
\]
It vanishes exactly at \(Ba=c_j=\log(1+1/s_j)\). The zero lies strictly inside \((a_j,a_{j+1})\) if and only if \(c_j/a_{j+1}<B<c_j/a_j\). The affine coordinate of this point is \(\theta_j(B)\) as stated. By strict concavity, this stationary point is the global maximum.

**Step 3 (vertex regimes and their ordering).** At interior vertex \(j\), the left derivative is nonnegative exactly when \(B\le c_{j-1}/a_j\); the right derivative is nonpositive exactly when \(B\ge c_j/a_j\). This proves the stated *closed* pure-vertex interval. Strict convexity of the lower hull makes its edge slopes strictly increase and therefore its \(c_j\) strictly decrease, so this interval has positive length. At the two endpoints of the full efficient boundary the one-sided derivative criterion gives the stated terminal regimes. Every strict edge interval also has positive length since \(a_{j+1}>a_j\). Since \(c_j/a_j<c_{j-1}/a_j\), the intervals meet in order without missing budgets or backtracking. Every regime occurs and the total count is \(r+(r-1)=2r-1\). The unique effective point at a boundary budget is the corresponding vertex, not an additional mixed optimum.

**Step 4 (sharp example).** For the three listed rate pairs, the slopes are \(s_1=3/10\) and \(s_2=3/4\). Both are positive and increase strictly, so all three points are efficient boundary vertices. Their constants are \(\log(1+10/3)=\log(13/3)\) and \(\log(1+4/3)=\log(7/3)\). Substituting into Steps 2 and 3 gives the five strict regimes. Since the rate points are distinct and noncollinear, their efficient mixtures have unique support among the three modes. The general upper bound \(2r-1\) is therefore attained already for \(r=3\); choosing the explicit positive rates \(a_j=j\), \(b_j=j^2\) for integers \(1\le j\le r\) gives strictly increasing slopes \(2j+1\), placing all \(r\) points on a strictly convex efficient chain and attaining the same sharp count for any larger \(r\).

## Verification

The self-contained standard-library script `CHECK.py` reconstructs the efficient lower hull, uses the analytic stationary point formula on each edge, and compares its value against direct pairwise optimization independent of the hull extraction. It checks 400 logarithmically spaced budgets for the three-modality example, four exact switching budgets, five explicitly selected phase regimes, and 9,000 random multi-modality/budget cases. Its reported result is `PASS 9409 independently checked optima/phase constraints`. These floating-point checks support implementation and the example; the proof of the arbitrary finite-family theorem is analytic and does not depend on finite tests. Run with `python3 CHECK.py`.

## Relationship to prior work

Udell et al. (2024) motivate the false-positive/false-negative issue in acoustic bat monitoring, but their full-text model estimates bat abundance and trends from counts, rather than allocating fixed effort among alternative Poisson alarm modalities to maximize a pooled binary Youden score. Clement (2016) treats false-positive occupancy survey design and allocation between survey types, targeting mean squared error of an estimated occupancy probability and using numerical optimization rather than the present explicit fixed-state alarm criterion. Fahad and Fuhrmann (2022) study sensing-time allocation in a vector Poisson model, but retain three count channels and optimize mutual information or a four-state Bayes correct-decision probability; their result does not imply this particular pooled OR rule's convex-frontier budget phase thresholds. Established Youden-index and generic convex-hull calculus are explicitly background mathematics, not newly claimed. A separate published result on convex-hull selective testing and previously studied first-alarm stopped ecological surveys likewise do not give the phase schedule for the objective here. Literature and mathematical-index searches are evidence of best-knowledge distinction, not a proof of global historical priority.

## Limitations

The model uses known fixed rates, ideal conditional Poisson independence, divisible common-price effort, a constant target state, and one pooled threshold of at least one count. Correlated detectors, nonstationary rates, fixed startup costs, rate uncertainty, fitted decision thresholds, prevalence-dependent Bayes losses, or retention of the full count vector change the optimization problem and are not addressed. This is a mathematical design benchmark, not a calibrated prescription for real bat surveys. Priority relative to all possible diagnostic-design and sensor-allocation literature is not independently established. Independent external validation has not been performed.

## References

1. Udell, B. J., et al. (2024), *Using mobile acoustic monitoring and false-positive N-mixture models to estimate bat abundance and population trends*, Ecological Monographs 94(4), e1617. First public release 2024-07-19. https://doi.org/10.1002/ecm.1617
2. Clement, M. J. (2016), *Designing occupancy studies when false-positive detections occur*, Methods in Ecology and Evolution 7(12), 1538–1547. https://doi.org/10.1111/2041-210X.12617
3. Fahad, M., and Fuhrmann, D. R. (2022), *Sensing Method for Two-Target Detection in Time-Constrained Vector Poisson Channel*, arXiv:2201.07915, version 1 dated 2022-01-19. https://arxiv.org/html/2201.07915v1
4. Stone, L. D., Stanshine, J. A., and Persinger, C. A. (1972), *Optimal Search in the Presence of Poisson-Distributed False Targets*, SIAM Journal on Applied Mathematics 23(1), 6–27. https://doi.org/10.1137/0123002 (abstract compared; full text not accessed).
