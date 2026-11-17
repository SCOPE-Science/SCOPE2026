# Interval extremizers and a 29-rim Gini–Dobrushin crossover for lazy wheel walks

## Finding

For each integer \(m\ge3\), let \(W_m=K_1\vee C_m\) be the unweighted wheel with one hub and \(m\) rim vertices. Let \(P_m=(I+D^{-1}A)/2\) be the half-lazy simple random walk acting on **real column signals**. Write
\[
G_m(f)=\sum_{u<v}|f_u-f_v|,\qquad
L_m=\sup_{G_m(f)>0}\frac{G_m(P_m f)}{G_m(f)}.
\]
For each integer \(1\le k\le m\), define the cyclic binary word \(b^{(m,k)}\) with its first \(k\) rim entries equal to one and all remaining rim entries zero; set the hub value to zero. Define
\[
t_i^{(m,k)}=3b_i^{(m,k)}+b_{i-1}^{(m,k)}+b_{i+1}^{(m,k)},\qquad
t_h^{(m,k)}=\frac{3k}{m},
\]
with indices modulo \(m\), and
\[
R_m(k)=\frac{\sum_{i<j}|t_i^{(m,k)}-t_j^{(m,k)}|+\sum_i|t_i^{(m,k)}-3k/m|}{6k(m+1-k)}.
\]
**Exact finite-family formula and extremizer structure:**
\[
\boxed{L_m=\max_{1\le k\le m}R_m(k).}
\]
In particular, for every \(m\), at least one sharp nonconstant input is the indicator of a contiguous rim arc, with hub input zero. The formula evaluates using at most six rim-output levels, hence at most \(m\) constant-size rational comparisons, rather than examining exponentially many binary inputs or arbitrary real vectors.

**A sharp crossover against classical oscillation contraction:** For all \(m\ge6\), the Dobrushin/Hopf-oscillation coefficient of \(P_m\) is exactly \(5/6\), whereas
\[
\boxed{L_m\le 5/6\ \Longleftrightarrow\ 3\le m\le28,\qquad
L_m>5/6\ \Longleftrightarrow\ m\ge29.}
\]
At the first crossing, the six-consecutive-rim indicator gives the exact lower witness
\[
\frac{G_{29}(P_{29}b^{(29,6)})}{G_{29}(b^{(29,6)})}
=\frac{10441}{12528}>\frac56.
\]
Nevertheless \(L_m<1\) in **every** dimension. Furthermore,
\[
\boxed{\lim_{m\to\infty}L_m=\frac56.}
\]
Thus the Gini and oscillation coefficients cross at a definite finite rim size while having the same asymptotic limit. The exact norm above is for one half-lazy step, not arbitrary powers or continuous-time heat.

## Assumptions and scope

The rim is the simple cycle of length \(m\ge3\), all edges have unit conductance, the hub has degree \(m\), and each rim vertex has degree three. The matrix acts on real vertex values, with the row-stochastic convention \((Pf)_u=\sum_vP_{uv}f_v\). There are \(m+1\) output coordinates; the sum defining \(G_m\) covers all unordered pairs including hub–rim pairs. Constants are quotiented out by this seminorm. Neither the output norm nor the input norm is weighted by the stationary distribution.

## Proof

**1. Binary cut reduction.** For any real input, sort its distinct levels. It is a constant plus a nonnegative linear combination of indicators of upper level sets. Pairwise absolute differences obey the exact coarea identity \(G_m(f)=\sum_j a_jG_m(1_{S_j})\) with \(a_j\ge0\), and the triangle inequality gives \(G_m(P_mf)\le\sum_j a_jG_m(P_m1_{S_j})\). Therefore the sharp quotient is attained among binary cuts. Complementation preserves the quotient because \(P_m\mathbf1=\mathbf1\); complement when necessary so the hub value is zero. A nonzero such cut contains exactly \(k\in\{1,\dots,m\}\) rim vertices, with denominator \(k(m+1-k)\).

**2. Cyclic arc majorization.** Fix \(k\in\{2,\dots,m-2\}\) and a binary rim set \(S\) of size \(k\). Write \(r\) for its number of cyclic runs. On selected vertices, the sixfold rim output \(t_i=3\mathbf1_S(i)+\mathbf1_S(i-1)+\mathbf1_S(i+1)\) equals \(3+d_S(i)\), where \(d_S(i)\in\{0,1,2\}\) is the induced rim-neighbor degree. On unselected vertices, \(t_i\) equals the number of neighboring selected vertices and belongs to \(\{0,1,2\}\). Thus every selected output exceeds every unselected output.

For a single arc, the selected induced degrees sorted downward are \(2\) repeated \(k-2\) times and \(1\) twice, and the unselected outputs are \(1\) twice and \(0\) otherwise. For an arbitrary \(r\)-run set, the selected induced degrees sum to \(2(k-r)\) and are individually at most two. The sums of their largest \(p\) values do not exceed the single-arc sums: for \(p\le k-2\) use the bound \(2p\); for \(p=k-1\), if \(r\ge2\) use \(2k-4<2k-3\), while \(r=1\) is itself an arc; for \(p=k\) use \(2(k-r)\le2k-2\).

For a partial sum of the largest \(k+q\) rim outputs, \(q\ge1\), the arbitrary-set sum is at most \(5k-2r+\min(2q,2r)\), because the total unselected boundary degree is \(2r\). The single-arc sum equals \(5k-2+\min(q,2)\). For \(r=1\) equality holds; for \(r\ge2\) the desired inequality follows separately for \(q=1\) and \(q\ge2\). Total rim sums are equal to \(5k\). Hence the single-arc rim-output vector **majorizes** every other \(k\)-cut rim-output vector. For \(k=1\) and \(k=m-1\), all cuts are already arcs up to rotation; for \(k=m\) there is only one rim cut. Appending the identical hub output \(3k/m\) preserves majorization. The pairwise-difference sum is convex and permutation-invariant, hence Schur-convex. It is therefore maximal for an arc. The sixfold-output formula in the finding follows directly from \((P_mb)_i=t_i/6\) and \((P_mb)_h=k/(2m)\).

**3. Rational formula in the interior and the rim-29 crossing.** For \(3\le k\le m-2\), the arc rim-output values multiplied by six have multiplicities \(0\) repeated \(m-k-2\) times, \(1\) twice, \(4\) twice and \(5\) repeated \(k-2\) times. Their sum of pairwise absolute differences is \(5k(m-k)-8\). Comparing the hub output \(3k/m\) with the rim level one gives
\[
R_m(k)-\frac56=
\begin{cases}
\displaystyle\frac{3k-8-6k(k+2)/m}{6k(m+1-k)},&3k\le m,\\[5pt]
\displaystyle\frac{3k-12-6k^2/m}{6k(m+1-k)},&3k\ge m.
\end{cases}
\]
The two expressions agree at equality. If \(3k\le m\), strict exceedance of \(5/6\) requires \(m>6k(k+2)/(3k-8)\). For every integer \(k\ge3\), the latter threshold is at least \(144/5=28.8\), because \((k-6)(5k-32)\ge0\) for integer \(k\ge3\). If \(3k\ge m\), the concave expression \(3k-6k^2/m\) decreases on \([m/3,m]\) and is at most \(m/3\); hence the second numerator is negative whenever \(m\le28\). The boundary arc sizes are harmless: \(R_m(1)=5/6-1/(2m)-3/m^2\), \(R_m(m)=1/3\), and \(R_m(m-1)=(7m-11-6/m)/(12(m-1))<5/6\). For \(k=2\) and \(m\ge6\), \(R_m(2)=(10m-12-48/m)/(12(m-1))<5/6\); direct substitution treats \(m=4,5\), while \(m=3\) belongs to the \(k=m-1\) case. This proves \(L_m\le5/6\) for \(m\le28\). For every \(m\ge29\), \(k=6\) lies in the first interior branch and has numerator \(10-288/m>0\); the displayed first-crossing fraction follows by substitution.

**4. Strict Gini contraction and the asymptotic limit.** Form a column-centering rank-one correction \(B_m=P_m+\mathbf1v^\mathsf T\), with \(v_j=(1-\sum_i(P_m)_{ij})/(m+1)\). On rim columns \(v_j=(m-3)/(6m(m+1))\), while on the hub column \(v_h=(3-m)/(6(m+1))\). Direct substitution shows that \(B_m\) has strictly positive entries and all its row and column sums equal one. Because \(B_m f-P_mf\) is a constant vector, \(G_m(B_mf)=G_m(P_mf)\). A strictly positive doubly stochastic matrix is a strict contraction of every symmetric convex dispersion seminorm on vectors modulo constants; indeed subtract its smallest entry from each matrix entry to decompose it into a positive uniform-averaging part and a strictly subunit multiple of a doubly stochastic matrix. This proves \(L_m<1\). For \(m\ge4\), its smallest entry is \((m-3)/(6m(m+1))\), yielding the explicit upper bound \(L_m\le5/6+1/(2m)\). The singleton-arc expression in Step 3 gives \(L_m\ge5/6-1/(2m)-3/m^2\); the squeeze proves the stated limit. In the case \(m=3\), the exact formula gives \(L_3=1/3\).

**5. Oscillation coefficient.** The classical Dobrushin coefficient is \(\delta(P_m)=1-\min_{u\ne v}\sum_w\min(P_{uw},P_{vw})\). Every pair of rows overlaps in the hub column by at least \(1/6\), hence \(\delta(P_m)\le5/6\). If \(m\ge6\), choose rim vertices whose length-three rim neighborhoods are disjoint. Their rows overlap exactly in the hub column, giving \(\delta(P_m)=5/6\). Thus the 29-rim inequality is a genuine comparison of **two different induced seminorms for the same operator**, not a statement about probabilistic total variation of initial distributions.

## Verification

The standalone Python checker `verify_wheel_gini.py` uses only exact integer and rational arithmetic. It checks every nonempty hub-zero binary rim cut for wheel sizes \(3\) through \(11\), reproducing the interval extremizer maximum independently; checks all \(43{,}956\) interior formulas through size \(300\); computes every arc for sizes \(3\) through \(28\); verifies the first strict witness at size \(29\) and its persistence through size \(300\); constructs and checks the strictly positive doubly stochastic correction for sizes \(3\) through \(50\); and checks two-sided asymptotic bounds through size \(200\). Run with `python3 verify_wheel_gini.py`. These **finite** tests corroborate the algebra; the dimension-unrestricted conclusions follow from Steps 1–5 and not from an extrapolation.

## Relationship to prior work

Gaubert and Qu's 2013–2014 Dobrushin-operator work provides the general oscillation coefficient and its total-variation dual; neither seminorm is the complete-pair Gini variation used here. Their formula implies the benchmark \(5/6\) after evaluating the wheel's row overlaps, but not this wheel's Gini norm, interval extremizer reduction or 29-rim crossover. Separate published wheel-heat work studies **unnormalized continuous-time heat** with a **graph-edge Lipschitz** norm; its wheel thresholds cannot be transferred to the present normalized **discrete-time** operator with complete-pair Gini variation. Other published sharp variation computations on bipartite graphs use different topologies or edge seminorms. General majorization and bistochastic contraction explain the nonexpansivity part but do not supply the sharp arc reduction or crossover. Current novelty is a best-knowledge claim only, not an exhaustive priority certificate.

## Limitations

No exact norm of higher powers \(P_m^t\) or arbitrary laziness parameter is asserted. The sharp formula requires a simple unweighted wheel, uniform half-laziness, real signals and unweighted complete-pair Gini variation, and supplies an \(O(m)\) exact rational optimization rather than a single uniform closed rational expression in \(m\). No unique characterization of **all** maximizing signals is claimed. The argument does not cover weighted wheels or higher-dimensional coned graphs. Existing unindexed literature may contain equivalent formulas; no independent mathematical audit has been performed.

## References

1. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, first public arXiv submission 2013-02-21, arXiv:1302.5226. https://arxiv.org/abs/1302.5226
2. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, first arXiv submission 2013-07-17, arXiv:1307.4649; author-available full text at https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf
3. *Weighted wheel heat flow: a contractivity boundary and a sharp star-limit amplification envelope*, a published comparison involving unnormalized heat and graph-edge Lipschitz variation, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-weighted-wheel-heat-flow-a-contractivity-boundary-and-a-sharp-st--cec0303daea0
