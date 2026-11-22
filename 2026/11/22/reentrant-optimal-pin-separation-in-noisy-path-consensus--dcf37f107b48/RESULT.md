# Reentrant optimal pin separation in noisy path consensus

## Finding

Let \(P_n\) be the unit-conductance path with vertices \(1,\ldots,n\), \(n\ge2\). Place exactly two equal positive-feedback pins at distinct vertices \(i<j\), with feedback gain \(\kappa>0\), and write
\[
K_{i,j}(\kappa)=L(P_n)+\kappa(e_ie_i^{\mathsf T}+e_je_j^{\mathsf T}),\qquad
T_n(i,j;\kappa)=\operatorname{tr}\!\left(K_{i,j}(\kappa)^{-1}\right).
\]
For every \(n\) and \(\kappa\), all globally optimal pairs have *balanced exterior tails*: if \(d=j-i\), then \(|(i-1)-(n-j)|\le1\). For each integer \(1\le d\le n-1\), put \(q_d\in\{0,1\}\) for the parity of \(n-d-1\). The exact minimum at fixed gap is
\[
F_n(d;\kappa)=\frac{n}{2\kappa}
+\frac{(n-d)^2-1+q_d}{4}
+\frac{d^2-1}{6}
+\frac{3dn-2d^2+2}{6(2+\kappa d)}.
\tag{1}
\]
Consequently, the complete finite-path optimizer set is obtained by minimizing this explicit rational expression over \(1\le d\le n-1\), then placing the two pins so that the two tails differ by at most one. This is an exact one-dimensional reduction, not a claim of a closed radical formula for every finite size.

For any fixed scaled gain \(c>0\), set \(\kappa=c/n\). As \(n\to\infty\), the gap \(d_n\) of **every** globally optimal pair satisfies
\[
\frac{d_n}{n}\longrightarrow r(c),
\]
where \(r(c)\) is the unique root in \((1/2,2/3)\) of
\[
5c^2r^3-3c^2r^2+18cr^2-12cr+12r-6=0.
\tag{2}
\]
The limiting pin coordinates are \((1-r(c))/2\) and \((1+r(c))/2\). The gap crosses \(3/5\) exactly at \(c=5/3\), attains its **unique global maximum** at
\[
c_*=\frac{7+4\sqrt7}{3},\qquad
r(c_*)=1-\frac1{\sqrt7}=0.62203552699\ldots,
\tag{3}
\]
and decreases strictly thereafter to \(3/5\) as \(c\to\infty\). Before \(c_*\) the gap increases strictly; its weak-gain limit is \(1/2\). Thus optimal pin separation is genuinely *nonmonotone* in the gain, and temporarily exceeds even its infinite-gain limit.

The effect occurs at a finite natural size, not just in a limiting relaxation. On \(P_{21}\), the exact full optimizer sets at \(\kappa=1/21,\,2/7,\,100/21\), respectively, are
\[
\{\{5,17\}\},\qquad \{\{4,17\},\{5,18\}\},\qquad \{\{5,17\}\}.
\tag{4}
\]
These correspond to unique optimal gaps \(12,13,12\) as pin strength increases.

## Assumptions and scope

The path Laplacian is the symmetric unnormalized combinatorial Laplacian with every edge conductance exactly one. Both pins have the same gain \(\kappa\); all other vertices have zero direct feedback. A unit-intensity independent white-noise input at every vertex gives the linear stochastic model \(dX=-K_{i,j}(\kappa)X\,dt+dW\). Its stationary total variance equals \(T_n(i,j;\kappa)/2\); the constant factor does not change optimizers. The noise acts on pinned as well as unpinned vertices. The theorem concerns two distinct pins and the full-state integrated steady-state variance, not the noise-free leader model or the spectral-gap objective. In the scaling result \(c\) is held fixed and strictly positive as \(n\to\infty\).

## Proof

**Exact finite trace.** Connect each pinned vertex to a common grounded node through an edge of conductance \(\kappa\). The diagonal entries of \(K_{i,j}^{-1}\) are effective resistances from vertices to ground. Write \(d=j-i\), \(\ell=i-1\), and \(h=n-j\). Eliminating the ungrounded exterior tails and the \(d-1\) unpinned interior vertices yields the pinned-endpoint precision matrix
\[
\begin{pmatrix}\kappa+1/d&-1/d\\-1/d&\kappa+1/d\end{pmatrix},
\]
whose inverse has diagonal and off-diagonal entries
\[
V=\frac{\kappa d+1}{\kappa(\kappa d+2)},\qquad
C=\frac{1}{\kappa(\kappa d+2)}.
\]
An exterior vertex at graph distance \(s\) from its adjacent pin contributes variance \(V+s\). For the interior vertex at distance \(t\in\{0,\ldots,d\}\) from the left pin, the conditional bridge decomposition gives variance
\[
\frac{t(d-t)}d+\left(\frac{d-t}{d}\right)^2 V
+\left(\frac{t}{d}\right)^2V
+\frac{2t(d-t)}{d^2}C.
\]
The interior segment includes both pinned vertices exactly once, while the exterior sums exclude them. Evaluating the three elementary sums gives
\[
T_n(i,j;\kappa)=\frac{\ell(\ell+1)+h(h+1)}2+\frac{d^2-1}{6}
+V\left(\ell+h+\frac{(d+1)(2d+1)}{3d}\right)
+C\frac{d^2-1}{3d}.
\tag{5}
\]
At fixed \(d\), the gain-dependent terms depend on \(\ell,h\) only through their fixed sum \(\ell+h=n-d-1\). Strict convexity of \(\ell(\ell+1)+h(h+1)\) under that fixed integer sum shows that exactly the balanced tails minimize the trace. Using \((\ell-h)^2=q_d\), \(\ell+h=n-d-1\), and simplifying (5) yields (1).

**Scaling limit.** Put \(r=d/n\) and \(\kappa=c/n\). Uniformly over the entire discrete gap range,
\[
\frac{F_n(d;c/n)}{n^2}
=\frac1{2c}+J_c(r)+O_c(n^{-1}),\quad
J_c(r)=\frac{(1-r)^2}{4}+\frac{r^2}{6}
+\frac{r(3-2r)}{6(2+cr)}.
\tag{6}
\]
For \(0<r\le1/2\), the derivative of \(J_c\) is negative; for \(2/3\le r<1\), it is positive. Indeed, its derivative has the sign of
\[
N_c(r)=c^2r^2(5r-3)+6cr(3r-2)+12r-6.
\]
For \(r\in[1/2,2/3]\), a direct calculation gives
\[
J_c''(r)=\frac{5c^3r^3+30c^2r^2+60cr-12c+24}{6(2+cr)^3}>0,
\]
since \(60cr-12c\ge18c\). Moreover \(N_c(1/2)<0\) and \(N_c(2/3)>0\). Thus \(J_c\) has exactly one global minimizer \(r(c)\), satisfying (2). The uniform approximation and compactness imply convergence of every discrete optimum, including when there are finite-size ties. Balancing the tails then gives the asserted pin-coordinate limits.

**Sharp reentrance.** Implicit differentiation is valid because \(J_c''(r(c))>0\). Its gain-location mixed derivative is
\[
\partial_c\partial_r J_c(r)
=\frac{r(cr^2+6r-6)}{3(2+cr)^3}.
\]
Any stationary point of \(r(c)\) must satisfy \(c=6(1-r)/r^2\) together with \(N_c(r)=0\). Substitution factors the latter as
\[
\frac{6(2r-3)(7r^2-14r+6)}{r^2}=0.
\]
The unique admissible root in \((1/2,2/3)\) is \(r=1-1/\sqrt7\), giving exactly (3). As \(c\downarrow0\), the unique root tends to \(1/2\), and \(r'(c)>0\) for small positive \(c\). As \(c\to\infty\), the leading cubic terms yield \(r(c)=3/5+2/(5c)+O(c^{-2})\), hence \(r'(c)<0\) for all sufficiently large \(c\). Since there is exactly one possible stationary point, strict increase before it and strict decrease afterward follow. At \(r=3/5\), \(N_c(r)=-6(3c-5)/25\), proving the unique crossing at \(c=5/3\).

**A finite reentrance certificate.** At \(n=21\), evaluate (1) over each of the 20 admissible integer gaps using rational arithmetic. For \(c=n\kappa=1,6,100\), respectively, the only minimizing gaps are \(12,13,12\). The positive difference from the best to the next-best *distinct gap value* is, respectively, \(1307/2970\), \(19/240\), and \(169805/1666764\). Balancing the tails gives exactly the three optimizer sets in (4). The attached standalone checker carries out these exhaustive finite rational comparisons.

## Verification

The standalone `verify.py` reconstructs the rational trace identity symbolically, checks every pinned pair of paths with \(2\le n\le9\) by exact matrix inversion at rational gain, verifies the cubic derivative and maximum identities, certifies all 20 gap comparisons for each of three gains on \(P_{21}\), and compares five large finite paths with the unique continuum root. Execute `python verify.py` with SymPy and NumPy installed. Exact algebra and a complete finite comparison support their stated scope; the all-size and all-gain conclusions rely on the analytic proof, not on numerical experiments.

## Relationship to prior work

Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* (first publicly posted July 7, 2014, arXiv:1407.1569), formulate precisely the finite-gain, full-state noisy leader problem and derive general two-leader performance formulas. Their path discussion reports numerical optimum pairs for \(n=51,101\) at extreme gains; it does not establish the critical \(\kappa\asymp1/n\) continuum function, the analytic overshoot and unique maximum, or the finite 21-vertex reentrance certificate. Those are the claims here, not priority for the general inverse-trace criterion.

Fitch's November 2016 dissertation, Chapter 4, section 4.2.2, likewise reports the finite-gain path examples without the scaled-gain reentrant theorem. Patterson, McGlohon and Dyagilev (first posted December 20, 2014, and expanded in 2016) develop exact polynomial-time selection for one-dimensional *perfect-leader* coherence using the follower-grounded Laplacian, which differs from the full-state, finite-gain inverse considered here. Patterson, Yi and Zhang (2017) derive resistance-distance expressions for general finite-gain leaders, but their listed closed-form two-noisy-leader optimizer is for cycles, not the critical path scaling and reentrance proved here.

## Limitations

The scaling limit applies to equal gains \(\kappa=c/n\), not arbitrary separately varying gains; it does not assert a simple monotonic or analytic dependence for the exact integer-valued gap at every fixed \(n\). The finite-pair optimizer formula is exact but retains a one-dimensional integer minimization. No robustness claim is made for heterogeneous graph conductances, correlated disturbances or other objectives. Publication priority is judged only against sources actually inspected; undiscovered equivalent formulations remain possible. No independent mathematical audit has been performed.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (initial posting 2014-07-07), later IEEE Transactions on Control of Network Systems 3 (2016), 366–378. https://arxiv.org/abs/1407.1569 ; https://doi.org/10.1109/TCNS.2015.2481138
2. K. Fitch, *Optimal Leader Selection in Multi-agent Networks: Joint Centrality, Robustness and Controllability*, Princeton University dissertation (November 2016), Chapter 4, section 4.2.2. https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/Fitch_thesis_final2.pdf
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first posted 2014-12-20); expanded as *Optimal \(k\)-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094 (2016). https://arxiv.org/abs/1412.6595 ; https://arxiv.org/abs/1604.07094
4. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017). https://arxiv.org/abs/1708.06873
