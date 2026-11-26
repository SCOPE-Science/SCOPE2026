# Exact deadline regimes for two sentinels on the five-vertex path

## Finding

On the path \(0-1-2-3-4\), start an irreversible susceptible–infected process from one uniformly chosen vertex. Transmission across each active infected–susceptible edge is independent and has a common rate \(\lambda>0\). Two distinct sentinel vertices \(S\) are observed continuously and perfectly. Let \(T_S\) be the time to first detection and \(Q_S(t)=\Pr(T_S>t)\).

Write \(x=\lambda t\). Let \(\xi\) and \(\eta\) be the unique strictly positive roots of
\[
 e^\xi=1+2\xi,\qquad e^\eta=1+2\eta+2\eta^2.
\]
They satisfy \(0<\xi<\eta\), with \(\xi\approx1.25643120862617\) and \(\eta\approx3.46288587294379\). The complete set of minimizers of \(Q_S(t)\) for \(t>0\) is

| Dimensionless deadline | All optimal pairs |
|---|---|
| \(0<x<\xi\) | \(\{1,3\}\) |
| \(x=\xi\) | \(\{1,3\},\{0,3\},\{1,4\}\) |
| \(\xi<x<\eta\) | \(\{0,3\},\{1,4\}\) |
| \(x=\eta\) | \(\{0,3\},\{1,4\},\{0,4\}\) |
| \(x>\eta\) | \(\{0,4\}\) |

The mean-optimal pairs are \(\{1,3\},\{0,3\},\{1,4\}\), with mean \(1/(2\lambda)\). The endpoint pair has mean \(3/(5\lambda)\), a 20% increase. Every deadline optimum is mean-optimal for \(0<x<\eta\); at \(x=\eta\) mean-optimal and mean-suboptimal pairs both minimize the deadline tail; for \(x>\eta\) the unique deadline optimum is mean-suboptimal.

## Assumptions and scope

The seed is uniform and independent of the transmission clocks. There is no recovery, importation or observation delay; a monitored seed is detected at time zero. The phase diagram is for a simple unweighted five-vertex path with exactly two sentinels. It is not a classification of intermediate deadline optima for longer paths or other graphs.

## Proof

Conditional on an unmonitored seed at \(i\), the nearest sentinels to the left and right, when present, are reached by sums of independent exponentials along disjoint paths. For a distance \(d\ge1\), the dimensionless survival function is \(U_d(x)=e^{-x}\sum_{j=0}^{d-1}x^j/j!\); put \(U_\infty(x)=1\) for a direction without a sentinel. The survival of the minimum is the product, since the two directional passages use disjoint independent clocks. Averaging over all seeds (the sentinel seeds contribute zero) yields
\[
Q_S(t)=\frac15\sum_{i\notin S}U_{d_L(i)}(\lambda t)U_{d_R(i)}(\lambda t).
\]
This all-placement identity is also given for general paths in [1, equation (1)]. Reflection reduces the five-vertex calculation to six pair types:

| Representative \(S\) | \(5e^{2x}Q_S(t)\) | \(\lambda\mathbb E[T_S]\) |
|---|---|---|
| \(\{1,3\}\) | \(2e^x+1\) | \(1/2\) |
| \(\{0,3\}\) | \(e^x+2x+2\) | \(1/2\) |
| \(\{0,4\}\) | \(2x^2+4x+3\) | \(3/5\) |
| \(\{0,2\}\) | \((x+2)e^x+1\) | \(7/10\) |
| \(\{1,2\}\) | \((x+3)e^x\) | \(4/5\) |
| \(\{0,1\}\) | \((x^2+4x+6)e^x/2\) | \(6/5\) |

The table follows by multiplying the directional tails at each unmonitored seed; the means follow by integrating the tails. For instance, for the endpoint pair the two endpoint-adjacent seeds each contribute \(e^{-2x}(1+x+x^2/2)\) to the sum, and the middle seed contributes \(e^{-2x}(1+x)^2\). For \(\{1,3\}\) the two outer seeds each contribute \(e^{-x}\) and the middle seed contributes \(e^{-2x}\).

For \(x>0\) the last three rows have strictly larger tails than the first, by the respective scaled differences \(xe^x\), \((x+1)e^x-1\), and \((1+2x+x^2/2)e^x-1\). Write \(B=\{1,3\}\), \(A=\{0,3\}\) or its reflection, and \(C=\{0,4\}\). The remaining comparisons are
\[
5e^{2x}(Q_A-Q_B)=1+2x-e^x,
\qquad
5e^{2x}(Q_A-Q_C)=e^x-1-2x-2x^2.
\]
The first comparison changes sign at \(\xi\): \(e^x-1-2x\) starts at zero with negative derivative, and its derivative strictly increases to infinity. For \(g(x)=e^x-1-2x-2x^2\), \(g(0)=0\) and \(g'(0)=-1\); \(g''(x)=e^x-4\) changes sign once from negative to positive. Thus \(g'\) first decreases, then increases through zero, and \(g\) decreases before increasing to infinity and crossing zero at \(\eta\). Since \(g(\xi)=-2\xi^2<0\), \(\xi<\eta\). For \(0<x<\xi\) we have \(Q_B<Q_A<Q_C\); for \(\xi<x<\eta\) we have \(Q_A<\min(Q_B,Q_C)\); for \(x>\eta\) we have \(Q_C<Q_A<Q_B\). The equalities give precisely the two reported ties. The mean-optimal set and loss follow from the mean column.

## Verification

The accompanying standard-library `verify.py` compares the exact Laplace transforms derived from a finite-state interval Markov recurrence with the directional-passage formula at four positive rational arguments for each two-sentinel placement on paths with two to five vertices. It also checks the tabulated means. The finite checks corroborate the formulas; the analytic comparisons above establish the conclusions for every positive deadline.

## Relationship to prior work

The companion calculation [1] already gives the gamma-tail formula on paths of any length, eventual endpoint optimality, and the complete four-vertex deadline switch at \(\xi\). In particular, [1] shows that on paths through four vertices every deadline optimum is mean-optimal: on four vertices both deadline-competing types have the same mean and strictly dominate the other types in the tail. On five vertices, eventual endpoint optimality from [1] together with the immediate mean comparison \(3/(5\lambda)>1/(2\lambda)\) suffices to deduce that this is the smallest path exhibiting disagreement. That cutoff is context, not the distinct contribution here. The five-vertex calculation resolves which pairs win at all intermediate deadlines, including the reflected pair type, the second crossing and both ties. In particular it locates precisely when the deadline and mean criteria stop agreeing.

General sensor-placement objectives and algorithms appear in [2,3]; they are not asserted to be new here. Holme [4] studies exact small-graph times to detection or extinction with recovery, a different time variable and objective. The full text of the related mobile-network placement paper [5] was not available for comparison, so this is not an exhaustive historical priority claim.

## References

1. *A universal deadline reversal for two sentinels on epidemic paths*, [Resultary record 1aae6884ac6b](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-a-universal-deadline-reversal-for-two-sentinels-on-epidemic-path--1aae6884ac6b/RESULT.md), equation (1) and the four-vertex analysis.
2. J. Leskovec et al., *Cost-effective outbreak detection in networks*, KDD 2007, [DOI:10.1145/1281192.1281239](https://doi.org/10.1145/1281192.1281239).
3. J. Heavey et al., *Provable Sensor Sets for Epidemic Detection over Networks with Minimum Delay*, AAAI 2022, [DOI:10.1609/aaai.v36i9.21260](https://doi.org/10.1609/aaai.v36i9.21260).
4. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, [arXiv:1708.06456v3](https://arxiv.org/abs/1708.06456v3).
5. C. Zhou et al., *Efficient Sensor Placement Optimization for Early Detection of Contagious Outbreaks in Mobile Social Networks*, IEEE Mobile Services 2015, [DOI:10.1109/MobServ.2015.45](https://doi.org/10.1109/MobServ.2015.45).
