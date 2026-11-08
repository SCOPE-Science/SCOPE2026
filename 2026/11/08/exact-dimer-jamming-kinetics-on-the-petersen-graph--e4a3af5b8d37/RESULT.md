# Exact dimer-jamming kinetics on the Petersen graph

## Finding
On the ten-vertex Petersen graph, irreversible rate-one edge-dimer adsorption has the following **exact distribution of its terminal number \(X\) of accepted dimers**:
\[
\Pr(X=3)=\frac1{25},\qquad
\Pr(X=4)=\frac{52}{75},\qquad
\Pr(X=5)=\frac4{15}.
\]
No other terminal size is possible. In particular, \(\mathbb E X=317/75\), and the probability of reaching a perfect matching is exactly \(4/15\), despite perfect matchings being available initially. The 71 distinct terminal labeled matchings comprise five of size three, sixty of size four and six of size five; the probability of **each** matching in these respective classes is \(1/125\), \(13/1125\), and \(2/45\).

The **complete continuous-time mean number of accepted dimers** is the seven-relaxation-rate expression
\[
\begin{aligned}
\mathbb E X(t)={}&\frac{317}{75}-\frac47e^{-t}-\frac{25}{26}e^{-2t}
-\frac{10}{7}e^{-3t}-\frac7{25}e^{-5t}\\
&-\frac79e^{-6t}-\frac{67}{350}e^{-10t}
-\frac{326}{20475}e^{-15t},\qquad t\ge0.
\end{aligned}
\]
Thus the mean occupied-vertex fraction is \(\mathbb E X(t)/5\), the initial deposition rate is \(\frac{d}{dt}\mathbb E X(t)|_{t=0}=15\), and the long-time mean deficit is \((4/7)e^{-t}+O(e^{-2t})\).

## Assumptions and scope
Define the Petersen graph on vertices \(\{0,\ldots,9\}\) by the fifteen undirected edges \(\{i,i+1\pmod{5}\}\) for \(0\le i<5\), \(\{i,i+5\}\) for \(0\le i<5\), and \(\{i+5,5+(i+2\pmod{5})\}\) for \(0\le i<5\). Every edge has independent unit-rate Poisson deposition attempts. An attempt succeeds precisely when both endpoints are unoccupied; successful edges permanently occupy their endpoints. The system starts vacant at \(t=0\), with no desorption or rearrangement, and \(X(t)\) counts accepted edges up to time \(t\), with \(X=\lim_{t\to\infty}X(t)\). Continuous clocks ensure no simultaneous successful attempts. Time has units of inverse per-edge attempt rate; for common edge rate \(\lambda>0\), replace \(t\) by \(\lambda t\).

## Proof
Let \(S\) be a set of occupied vertices and write \(E(S)=\{\{u,v\}\in E:u,v\notin S\}\) and \(r(S)=|E(S)|\). From every nonterminal state \(S\) the next successful event waits an exponential time of rate \(r(S)\) and adds \(\{u,v\}\) with conditional probability \(1/r(S)\) for each \(\{u,v\}\in E(S)\). Rejected attempts do not affect this statement. This specifies a finite acyclic transition system and is exact, including boundary states with \(r(S)=0\).

For a terminal state \(S\), set \(L_S(S)=1\); for nonterminal states use the rational recurrence
\[
L_S(S')=\frac1{r(S')}\sum_{\{u,v\}\in E(S')}L_S(S'\cup\{u,v\}),
\]
with the terminal boundary \(L_S(T)=\mathbf1_{T=S}\). Enumerating every reachable occupied-vertex mask gives 272 masks and 36 terminal masks. Their occupancy-class multiplicities and individual probabilities are: five masks with six occupied vertices and probability \(1/125\) each, thirty masks with eight occupied vertices and probability \(26/1125\) each, and one mask with ten occupied vertices and probability \(4/15\). These sum to the displayed terminal distribution.

For an independent certificate that also resolves matching identities, use the isomorphic Kneser realization with the ten two-element subsets of \(\{0,1,2,3,4\}\) as vertices and edges between disjoint subsets. There are exactly 2,190 ordered sequences of *successful* deposited edges. Every such sequence has probability \(\prod_{j=0}^{k-1}r_j^{-1}\), where \(r_j\) is the number of available edges before its \((j+1)\)-st success. Exhausting these sequences yields exactly five, sixty and six maximal matching edge sets of sizes three, four and five, with the per-matching probabilities stated above. All sums are exact rational arithmetic, and the supplied independent enumeration evaluates every branch, not a sample.

For the time-dependent claim, conditional on any complete success sequence with success rates \(r_0>r_1>\cdots>r_{k-1}>0\), its inter-success waiting times are independent exponentials with those rates. The \(j\)-th success time has the hypoexponential cumulative law
\[
\Pr(T_j\le t\mid\text{sequence})=1-\sum_{i=0}^{j-1}
\left(\prod_{\substack{0\le\ell<j\\\ell\ne i}}
\frac{r_\ell}{r_\ell-r_i}\right)e^{-r_it}.
\]
Multiplying by the rational probability of each of the 2,190 complete sequences, summing \(j=1,\ldots,k\), and collecting identical exponentials gives the displayed \(\mathbb E X(t)\). Distinct rates follow because each accepted dimer removes at least its own edge from availability. A second derivation solves the forward Kolmogorov equations \(\dot p_S=-r(S)p_S+\sum_{T\to S}p_T\), successively by occupied-mask size, with \(p_{\varnothing}(0)=1\). It produces exactly the same eight nonzero coefficients, including the constant term. Both computations are independently reproducible in the appended source files.

## Verification
Run `python3 verify_mask.py` and `python3 verify_paths.py` with Python 3 standard library only. The first independently constructs the outer-cycle/inner-star graph, solves the exact rational backward terminal law and forward time-evolution equations over 272 states, and checks all coefficients. The second constructs \(\mathrm{KG}(5,2)\), enumerates all 2,190 successful-edge histories and their individual probabilities, and independently derives the complete time-dependent formula using hypoexponential convolutions. Both assert the exact terminal distribution and eight nonzero coefficients. The derivations use symbolic rationals, not floating-point fits, sampling or extrapolation.

## Relationship to prior work
The model is a finite-graph realization of random sequential adsorption and random greedy matching. Cadilhe–Araújo–Privman (2006/2007) review the irreversible lattice-adsorption setting and jamming kinetics; Gamarnik–Goldberg (2008/2009) study randomized greedy matchings and finite-girth bounds. Neither inspected full text reports the displayed exact Petersen terminal law or its complete eight-term transient mean. Pippenger (1989) treats edge adsorption on regular graphs and is an important earlier predecessor, but its full text was not accessible for a decisive entire-paper comparison. Known Petersen graph perfect-matching counts (six) and graph structure are background, not claimed discoveries.

## Limitations
The result is an exact finite ten-site benchmark, not a thermodynamic limit, a statement about other cubic cages, or a measurement on a physical material. A generic state-space recursion exists on any finite graph; the contribution is the explicitly evaluated, fully reproducible all-time kinetic law and its nontrivial labeled-terminal probabilities for this canonical graph. Unindexed historical tables and inaccessible early full text create a residual priority risk. The claim has not undergone independent expert audit.

## References
1. A. Cadilhe, N. A. M. Araújo and V. Privman, *Random Sequential Adsorption: From Continuum to Lattice and Pre-Patterned Substrates*, arXiv:cond-mat/0611413 (first publicly posted 2006-11-15), https://arxiv.org/abs/cond-mat/0611413.
2. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277 (first publicly posted 2008-07-08), https://arxiv.org/abs/0807.1277.
3. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401, https://doi.org/10.1137/0402034 (full text not inspected).
4. A. E. Brouwer, *Petersen graph*, https://aeb.win.tue.nl/graphs/Petersen.html (structural reference).
