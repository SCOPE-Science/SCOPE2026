# Exact phase-aliasing bounds for sampled analogue-neighbor saturation on periodic trajectories

## Finding

For an exactly periodic scalar time series with distinct values at the \(P\) phases, the **fraction of test histories having \(K\) exact training neighbors** is controlled by finite phase multiplicities. A uniformly spaced subset of test histories need not faithfully estimate that fraction. At a sharp one-phase saturation cutoff, it can report \(100\%\) exact-neighbor saturation even though only \(1/P\) of the full test collection is saturated. The overstatement \(1-1/P\) has no universal bound below one. A stride coprime to the period, sampled over full stride orbits, removes this arithmetic bias.

## Assumptions and scope

Fix positive integers \(K,Y,H\) and a period \(P\ge2\). Let \((x_j)_{j\ge0}\) be a scalar sequence satisfying \(x_{j+P}=x_j\) for all \(j\), with \(x_0,\ldots,x_{P-1}\) pairwise distinct. For a history start \(j\), define \(v_j=(x_j,\ldots,x_{j+Y-1})\). A stored record has indices \(0,\ldots,N-1\), with chronological training region \(0,\ldots,T-1\) and test region \(T,\ldots,N-1\); the usable starts are respectively \(0\le j\le T-Y-H\) and \(T\le j\le N-Y-H\). The margin \(H\) requires every future through horizon \(H\) to remain in its region. Assume both sets are nonempty. Neighbor distances are Euclidean in history space and include all training starts, without a Theiler exclusion. A test history is *exact-neighbor saturated* when its \(K\)-th nearest training-history distance is zero.

## Proof

Different starting residues modulo \(P\) have different first coordinates and hence different history vectors. Equal residues give identical histories and identical futures through every horizon. Therefore, counting exact matches is equivalent to counting training starts by residue. For \(p\in\{0,\ldots,P-1\}\), the number of integers \(j=p+mP\) with \(0\le j\le T-Y-H\) is exactly

\[
c_T(p)=\max\left\{0,1+\left\lfloor\frac{T-Y-H-p}{P}\right\rfloor\right\}.
\]

When \(T-Y-H=(K-1)P+r-1\) and \(1\le r\le P\), this count is \(K\) on residues \(0\le p<r\) and \(K-1\) on the remaining residues (including \(K=1\), when the latter count is zero). Thus the exact-neighbor indicator is the characteristic function of the first \(r\) residues. Any test interval comprising an integer number of full periods has saturation fraction \(r/P\).

For queries in the progression \(j_0+td\), let \(g=\gcd(P,d)\). Reduction modulo \(P\) traverses exactly the \(P/g\) residues congruent to \(j_0\) modulo \(g\), each once per stride orbit. Counting its intersections with the first \(r\) residues gives

\[
F_{\mathrm{stride}}=\frac{g}{P}\#\big\{p\in\{0,\ldots,r-1\}:p\equiv j_0\pmod g\big\}.
\]

When \(g=1\), this is \(r/P\). When \(g=P\), every sampled query has the same phase and its fraction is either zero or one. To achieve maximal overstatement, choose \(r=1\) and \(P>Y+H\), and put

\[
T=(K-1)P+Y+H,\qquad N=T+Y+H+MP-1.
\]

The test starts form exactly \(MP\) consecutive indices. The chosen stride-\(P\) queries are \(j_t=KP+tP\), \(0\le t<M\). They lie in the test range because \(KP-T=P-Y-H>0\) and the final index is no later than \(N-Y-H\). Each has phase zero, with exactly \(K\) training copies; all its averaged \(K\)-neighbor forecasts equal the true future through horizon \(H\). Exactly \(M\) of the \(MP\) test starts have this property. This proves the sharp gap. No claim is made that nonsaturated queries necessarily have nonzero forecast error: the conclusion concerns exact training-neighbor multiplicity, not a converse forecast-error criterion.

## Verification

The accompanying `verification.py` exhaustively reconstructs the training phase multiplicities for \(P=3,\ldots,41\), \(K=1,\ldots,5\), and \(Y,H=1,2,3\), including selected stride orbits. It additionally enumerates actual length-five history vectors for \(P=29\), \(K=3\), \(Y=H=5\), \(T=68\), \(M=31\), \(N=976\). Of the \(899\) admissible test starts, precisely \(31\) have three exact training copies, whereas all \(31\) stride-selected queries do. These finite checks corroborate the integer-count proof but do not replace its all-parameter argument. Run `python verification.py` using Python 3.

## Relationship to prior work

Velichko and Pham (2026) identify forecast-error Lyapunov collapse when a finite-precision digital orbit supplies repeated predictive histories. Their diagnostic \(F_{\mathrm{exact},K}\) measures zero \(K\)-th-neighbor distance, and their experiments sometimes evaluate evenly spaced subsets of test histories. They give a recurrence-occupancy scaling estimate rather than this exact phase-by-phase finite-cutoff and progression-residue formula. The present theorem isolates a separate *sampling-identifiability* issue: a sampled exact-neighbor diagnostic can attain one substantially before the full diagnostic does. Classical phase aliasing principles motivate this possibility; the claimed contribution is the exact multiplicity and sharp saturation discrepancy under the specified catalogue protocol.

## Limitations

The theorem assumes an exactly periodic record from its first sample and pairwise distinct scalar phase values; a preperiodic transient, observation collisions, noisy histories, alternative test margins, nonuniform query selection, or deliberate exclusion of temporally close neighbors require separate analysis. A coprime stride is unbiased only when an entire stride cycle (or an integer number of them) is sampled. The construction does not show that the specific numerical experiments of Velichko and Pham suffered bias. This is a finite deterministic sampling theorem, not a theorem about a positive underlying real-system Lyapunov exponent. Historical priority beyond inspected material remains unverified.

## References

Velichko, A., and Pham, V.-T. (2026). *When more data become less informative: Finite-precision periodicization and collapse of forecast-error Lyapunov estimates.* arXiv:2608.16120, version 1 first submitted August 17, 2026; full-text version 2 posted October 30, 2026. https://arxiv.org/abs/2608.16120 and https://arxiv.org/html/2608.16120v2.
