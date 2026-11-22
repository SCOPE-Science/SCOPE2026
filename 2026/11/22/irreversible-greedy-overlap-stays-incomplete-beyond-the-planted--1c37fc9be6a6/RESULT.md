# Irreversible greedy overlap stays incomplete beyond the planted-matching recovery threshold

## Finding
Consider the complete bipartite graph with two labelled vertex classes of size \(n\), and the distinguished perfect matching \(M_* = \{(i,i):1\le i\le n\}\). Independently assign exponential edge-arrival times of rate \(c>0\) to the \(n\) distinguished edges and rate \(1/n\) to every other edge. Process edges in arrival order, irrevocably accepting an edge exactly when neither endpoint has previously been matched. Let \(S_n(c)\) be the number of accepted distinguished edges.

For each **fixed** \(c>0\),
\[
\frac{S_n(c)}n\xrightarrow[n\to\infty]{\mathbb P}f(c)=c\int_0^\infty y_c(t)\,dt,
\]
where \((x_c,y_c)\) is the unique solution of
\[
\dot x_c=-x_c^2-cy_c,\qquad \dot y_c=-2x_cy_c-cy_c,\qquad (x_c(0),y_c(0))=(1,1).
\]
The asymptotic greedy loss is strictly positive for **every finite** rate \(c>0\):
\[
1-f(c)=\int_0^\infty x_c(t)^2\,dt\ge\frac1{2(1+c)}>0.
\]
In contrast, the minimum-total-arrival-time perfect matching for the *same exponential edge-weight distribution* has planted overlap tending to one for \(c\ge4\), by the theorem of Moharrami, Moore and Xu. Thus above their almost-perfect-recovery threshold, the irreversible greedy dynamics retains a macroscopic loss; at \(c=4\) its limiting loss is at least \(1/10\).

## Assumptions and scope
For each \(n\ge1\), each distinguished edge has an independent \(\operatorname{Exp}(c)\) clock; each other edge has an independent \(\operatorname{Exp}(1/n)\) clock. An accepted edge permanently occupies both endpoints. All edges are present, so the final matching is perfect almost surely; the variable \(S_n(c)\) measures its overlap with \(M_*\), not its size. The parameter \(c>0\) is fixed before taking the limit. The optimal matching used for comparison minimizes the **sum** of the original clock times, not the latest arrival time and not the number of unplanted edges.

## Proof
Let \(X_n(t)\) be the number of unmatched vertices in either vertex class, \(Y_n(t)\) the number of distinguished pairs both of whose endpoints are still free, and \(Z_n(t)\) the number of accepted distinguished edges. Initially \((X_n,Y_n,Z_n)=(n,n,0)\). Conditional on \(X_n=k\) and \(Y_n=j\), there are \(j\) available distinguished edges, \(j(j-1)\) available nondistinguished edges whose endpoints belong to two distinct intact distinguished pairs, \(2j(k-j)\) nondistinguished edges involving exactly one intact pair, and \((k-j)^2\) nondistinguished edges involving no intact pair. The corresponding changes in \((X_n,Y_n,Z_n)\) are respectively \((-1,-1,+1)\), \((-1,-2,0)\), \((-1,-1,0)\), \((-1,0,0)\). Their respective rates are \(cj\), \(j(j-1)/n\), \(2j(k-j)/n\), and \((k-j)^2/n\). These counts sum to the full available-edge rate and apply even at the boundary \(j=0\) or \(j=k\).

Write \((x_n,y_n,z_n)=(X_n/n,Y_n/n,Z_n/n)\). Their exact predictable drift is
\[
\left(-x_n^2-cy_n+\frac{y_n}{n},\quad -2x_ny_n-cy_n+\frac{2y_n}{n},\quad cy_n\right).
\]
Every jump of these normalized variables has magnitude at most \(2/n\), and the total rate is at most \((1+c)n\). Therefore for each fixed finite horizon \(T\), the martingale parts have \(L^2\) maximal norm \(O_{c,T}(n^{-1/2})\). The limiting drift is Lipschitz on the invariant cube \([0,1]^3\). The martingale decomposition and Gronwall's lemma imply uniform convergence in probability over \([0,T]\) to the solution \((x_c,y_c,z_c)\) of the displayed two-component system together with \(\dot z_c=cy_c\), \(z_c(0)=0\). No independent-particle or mean-field closure assumption is used: the three-dimensional Markov description is exact at every finite \(n\).

Because \(0\le y_c\le x_c\le1\) and \(\dot x_c\le -x_c^2\), comparison gives \(x_c(T)\le(1+T)^{-1}\). After time \(T\), at most \(X_n(T)\) additional distinguished edges can be accepted. Thus the absolute difference between final \(S_n(c)/n\) and \(z_c(T)\) is bounded by the finite-time approximation error plus \(x_n(T)\), and the deterministic tail \(z_c(\infty)-z_c(T)\le x_c(T)\). Taking \(n\to\infty\) and then \(T\to\infty\) proves convergence to \(f(c)=z_c(\infty)\).

Finally, \(\dot x_c+\dot z_c=-x_c^2\), \(x_c(0)=1\), and \(x_c(\infty)=0\). Hence \(1-f(c)=\int_0^\infty x_c^2\). The bound \(y_c\le x_c\le1\) gives \(\dot x_c\ge-(1+c)x_c\), so \(x_c(t)\ge e^{-(1+c)t}\) and therefore \(1-f(c)\ge1/[2(1+c)]\). Since \(\dot z_c(0)=c>0\), also \(f(c)>0\). The cited matching theorem applies to the identical independent \(\operatorname{Exp}(c)\) and \(\operatorname{Exp}(1/n)\) weights but minimizes the full total weight, proving the asserted contrast.

## Verification
The standalone \`verification.py\` has two finite-state implementations: a reduced exact-rational recursion indexed by remaining vertices and intact distinguished pairs, and an independent labelled-subset recursion. They agree in 24 tests with \(1\le n\le6\) and four rational rate ratios per size. The reduced recurrence is
\[
F_{k,j}=\frac{wj}{D}(1+F_{k-1,j-1})+\frac{j(j-1)}D F_{k-1,j-2}+\frac{2j(k-j)}D F_{k-1,j-1}+\frac{(k-j)^2}D F_{k-1,j},
\]
where \(D=k^2+(w-1)j\), \(F_{0,0}=0\), omitted zero-coefficient terms are excluded, and \(w=cn\). Numerically integrating the independent deterministic ODE gives \(f(1)\approx0.470697\) and \(f(4)\approx0.789943\). These decimals are orientation checks only; the theorem and the strict positive-loss bound do not depend on numerical integration. The verifier also compares exact finite \(n=20,50,100\) expectations against these asymptotic values.

## Relationship to prior work
Bennett and Bohman (2012) analyze **uniform-rate** random greedy hypergraph matching and near-perfect coverage via dynamic concentration, not the biased distinguished-edge overlap on \(K_{n,n}\). Arnosti (2021) compares edge-uniform random greedy matching to other greedy algorithms on random bipartite graphs, not a planted exponential priority class. Moharrami, Moore and Xu (2019 preprint; 2021 journal) use exactly the same planted exponential edge-weight model, but analyze the globally **minimum-total-weight** perfect matching and prove near-perfect planted recovery for \(c\ge4\); the present theorem quantifies the different outcome of irreversible first-feasible-edge selection. The underlying irreversible dimer-adsorption perspective is classical, as in Pippenger (1989). None of these identified statements implies the greedy two-component fluid limit or its all-finite-rate deficit.

## Limitations
The fluid theorem takes \(c>0\) fixed as \(n\to\infty\); no uniform result for a growing \(c=c_n\), central-limit theorem, convergence-rate estimate, or optimal greedy-policy guarantee is claimed. The optimal matching comparison is an attributed published theorem, not a new proof of that theorem. Historical priority remains subject to potentially unlocated results on weighted planted greedy matchings. All verification programs are finite tests and are not substitutes for the martingale argument.

## References
- P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581 (first public arXiv version 2012-10-12), https://arxiv.org/abs/1210.3581.
- M. Moharrami, C. Moore and J. Xu, *The Planted Matching Problem: Phase Transitions and Exact Results*, arXiv:1912.08880 (first public version 2019-12-18), https://arxiv.org/abs/1912.08880. See Theorem 1 on near-perfect recovery by minimum-total-weight matching.
- N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, *Stochastic Systems* 12 (2022), 133–150 (first published online 2021-11-02), https://doi.org/10.1287/stsy.2021.0082.
- N. Pippenger, *Random Sequential Adsorption on Graphs*, *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, https://doi.org/10.1137/0402034.
