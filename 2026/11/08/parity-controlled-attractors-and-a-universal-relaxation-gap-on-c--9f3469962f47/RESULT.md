# Parity-controlled attractors and a universal relaxation gap on complete split graphs

## Finding
For integers \(a\ge2\) and \(b\ge1\), consider the labelled complete split graph \(G_{a,b}=K_a\vee\overline{K_b}\). There are \(a\) mutually adjacent core vertices, \(b\) mutually nonadjacent peripheral vertices, and every core-peripheral edge. Write \(N=a+b\). At each discrete time, one vertex chosen uniformly adopts the minority bit in its closed neighborhood, retaining its bit in case of a tie.

Every initial binary configuration reaches the maximum-cut configurations almost surely. **The recurrent configurations are exactly the maximum cuts.** The complete recurrent-class classification is:

1. If \(b\ge a\), there are exactly two recurrent classes, each a singleton absorbing configuration.
2. If \(1\le b<a\) and \(N\) is even, there are exactly \(2\binom{a}{(a-b)/2}\) singleton absorbing classes.
3. If \(2\le b<a\) and \(N\) is odd, there are exactly two nonabsorbing recurrent classes, each with \(\binom{a+1}{(a-b+1)/2}\) configurations.
4. If \(b=1\) and \(a\) is even, the graph is an odd complete graph and has exactly one nonabsorbing recurrent class of \(2\binom{a+1}{a/2}\) configurations.

In both nonabsorbing cases, the stationary law is uniform on each class, the chain is aperiodic, and the **exact discrete-time spectral gap** \(1-\lambda_2(P)\), where \(\lambda_2(P)\) is the second-largest eigenvalue of the restricted transition matrix, is
\[
\boxed{\gamma_{a,b}=\frac1{a+b}.}
\]
The result refers to the spectral gap of each recurrent-class chain, not a global spectral gap across multiple classes. For \(b\ge2\) in case 3, a recurrent transition graph is the inclusion graph between adjacent ranks \(k=(N-1)/2\) and \(k+1\) of the Boolean lattice on the \(a\) core vertices. For case 4, it is the corresponding middle-rank inclusion graph on all \(N=a+1\) vertices.

For example, \((a,b)=(5,2)\) has two recurrent classes of fifteen states each and gap \(1/7\); \((a,b)=(6,2)\) has thirty isolated absorbing states; \((a,b)=(4,1)\) has one recurrent class of twenty states and gap \(1/5\).

## Assumptions and scope
Graphs are finite, undirected, simple, and labelled. A configuration assigns a bit in \(\{0,1\}\) to each vertex. Its cut size is the number of edges with unequal endpoint bits. The minority update includes the selected vertex itself when tallying the closed neighborhood. Tied tallies cause **retention**, not a random choice. One vertex is selected independently and uniformly at each step, so a prescribed finite update sequence has positive probability. A recurrent class means a closed strongly connected component of the finite-state transition graph. A spectral gap is asserted only when its class has more than one state.

## Proof
**1. Exact update inequalities and the cut Lyapunov function.** If a selected vertex has \(s\) same-bit and \(o\) opposite-bit neighbors (excluding itself), then it changes bit precisely when \(s\ge o\); the cut increases by \(s-o\ge0\). Thus cut size never decreases, and any maximum-cut configuration can only move to another maximum-cut configuration. A neutral flip is reversible by immediately selecting the same vertex again.

Fix a configuration with \(i\) core ones and \(j\) peripheral ones. Its cut size is exactly
\[
Q(i,j)=i(a-i)+i(b-j)+(a-i)j=i(N-i)+j(a-2i).
\]
For a core one, the change to zero is allowed precisely when \(2(i+j)\ge N+1\); for a core zero, the change to one is allowed precisely when \(2(i+j)\le N-1\). A peripheral one can become zero when \(2i\ge a\), while a peripheral zero can become one when \(2i\le a\). These equivalences include all equality and boundary cases.

**2. Reachability of a maximum cut.** Suppose first that \(i\ge a/2\). Keeping the core fixed, update every peripheral one to zero. These updates are all allowed because \(2i\ge a\). Now \(j=0\), and \(Q(i,0)=i(N-i)\). If \(i<(N-1)/2\) and \(i<a\), successively update core zeros to ones; if \(i>(N+1)/2\), update core ones to zeros. At an integer boundary where equality holds, one more neutral update may be taken or omitted. This procedure reaches a maximizing value of \(i(N-i)\) on \(\lceil a/2\rceil\le i\le a\): if \(b<a\), it reaches an allowed integer nearest \(N/2\); if \(b\ge a\), it reaches \(i=a\). No peripheral update is needed after the initial phase. If initially \(i<a/2\), exchange the two colors and use the same construction. Thus *from every configuration* there is a finite path of permitted updates to a maximum cut.

Because every maximum-cut state is closed under the dynamics and is accessible from every other state through some finite path, no recurrent communicating class can lie outside the maximum-cut set. Conversely, the maximum-cut set is closed, and its connected components under reversible neutral flips are exactly its recurrent classes. Finiteness and the positive probabilities of prescribed vertex selections imply almost-sure entrance into that set from every initial configuration.

**3. Count and classify the maximizing configurations.** The coefficient of \(j\) in \(Q(i,j)\) is \(a-2i\). If \(i>a/2\), a maximizing configuration must have \(j=0\); if \(i<a/2\), it must have \(j=b\). When \(a\) is even and \(i=a/2\), \(Q\) is independent of \(j\), but this balanced-core slice attains the maximum only in the special case \(b=1\), which is the complete graph \(K_{a+1}\). Indeed, when \(b\ge2\), this slice is strictly worse than a neighboring attainable core count. Maximization of \(i(N-i)\) on the upper half \(a/2<i\le a\), together with color complement, now gives the four cases.

For \(b\ge a\), only the two fully polarized cuts of size \(ab\) are optimal. For \(b<a\), the optimum cut size is \(\lfloor N^2/4\rfloor\). If \(N\) is even, the maximizing core-one count on the peripheral-zero side is \(N/2\), giving \(2\binom a{(a-b)/2}\) states after complement, each absorbing because all single flips strictly reduce the cut. If \(N\) is odd and \(b\ge2\), the peripheral-zero side has the two adjacent core levels \(k=(N-1)/2\) and \(k+1\), giving \(\binom a k+\binom a{k+1}=\binom{a+1}{(a-b+1)/2}\) states; complement supplies a second disjoint side. Their neutral-flip graph is the connected incidence graph between those two ranks. All peripheral vertices are fixed within each class. If \(b=1\), the graph is exactly \(K_{a+1}\), and the usual middle-two-level incidence graph on all its vertices is connected when \(a\) is even; when \(a\) is odd, the balanced states are all absorbing.

**4. Exact spectrum.** In either nonabsorbing case let \(d\) be the number of freely changing vertices and \(k\) the smaller of the two allowed ranks. Specifically, use \(d=a\), \(k=(N-1)/2\) when \(b\ge2\), or \(d=N\), \(k=(N-1)/2\) when \(b=1\). In both cases \(k\ge(d-1)/2\) and \(k<d\). Write \(q=d-k\), \(m_r=\binom dr-\binom d{r-1}\), with \(\binom d{-1}=0\). Let \(L\) be the unweighted combinatorial Laplacian of the two-rank inclusion graph. Its complete eigenvalue multiset is
\[
\boxed{\operatorname{spec}(L)=\biguplus_{r=0}^{q-1}\bigl(\{r\}^{m_r}\uplus\{d+1-r\}^{m_r}\bigr)\uplus\{q\}^{m_q},}
\]
where an eigenvalue with zero multiplicity is omitted. In the odd-\(d\), middle-rank case \(m_q=0\). To see this directly, let \(B\) be the incidence matrix from \(k\)-subsets to \((k+1)\)-subsets. The vertex degrees on those two ranks are \(d-k\) and \(k+1\), so
\[
L=\begin{pmatrix}(d-k)I&-B\\-B^{\mathsf T}&(k+1)I\end{pmatrix}.
\]
The classical Boolean-lattice up/down commutator \(D_{r+1}U_r-U_{r-1}D_r=(d-2r)I\) decomposes each rank into harmonic modules of dimensions \(m_r\). It gives squared singular values \((k+1-r)(d-k-r)\), with multiplicity \(m_r\), for \(0\le r<q\); any unmatched lower-rank space has dimension \(m_q\). On each paired singular space the Laplacian has characteristic polynomial
\[
t^2-(d+1)t+r(d+1-r)=(t-r)(t-(d+1-r));
\]
the unmatched space has eigenvalue \(q\). This proves the full multiset above. Its least positive eigenvalue is exactly \(1\): if \(q\ge2\), the \(r=1\) harmonic appears, and if \(q=1\), the unmatched \(q\)-eigenvalue appears. Each allowed neutral flip is chosen with probability \(1/N\), hence \(P=I-L/N\). It follows that \(1-\lambda_2(P)=1/N\) in every nonabsorbing recurrent class. Symmetry of \(P\) gives a uniform stationary distribution; the inactive vertices ensure positive holding probabilities and aperiodicity.

## Verification
The standalone script `artifacts/check_attractors.py` constructs the complete labelled transition digraphs for 46 parameter pairs \(2\le a\le8\), \(1\le b\le8\) with \(a+b\le12\). Its Tarjan analysis independently determines all closed strongly connected components and compares their exact sizes and vertices against the predicted maximum-cut sets. It examines 46,088 configurations. The separate script `artifacts/check_spectrum.py` constructs rank-inclusion graph Laplacians from scratch and compares every numerically computed eigenvalue against the integral eigenvalue multiset above across 13 nonabsorbing parameter pairs; the summed matrix dimensions are 574. It uses NumPy. The saved outputs `artifacts/attractor_output.txt` and `artifacts/spectrum_output.txt` were generated by these scripts. These bounded checks support debugging and reproducibility but do not replace the all-parameter proof.

## Relationship to prior work
Rouquier, Regnault, and Thierry, *Stochastic Minority on Graphs* (first arXiv submission 2010-11-23), defines the identical closed-neighborhood asynchronous rule and proves the cut-energy principle; its Section 4.1 classifies ordinary cliques and Section 3.2 treats bipartite duals. The complete split graphs here are generally nonbipartite and noncomplete: those theorems do not supply their full attractor classification, parity transition, or recurrent-class gap.

Kun, Powers, and Reyzin, *Anti-Coordination Games and Stable Graph Colorings* (2013), treats equilibrium existence, stability, and complexity in anti-coordination games. Such static equilibrium conditions are relevant but do not by themselves determine the communicating classes produced by neutral minority updates. Papp and Wattenhofer, *Stabilization Time in Minority Processes* (2019), studies stabilization under conflict-reducing processes rather than the exact neutral recurrent-class spectrum here. Standard Boolean-lattice and Johnson-scheme spectral identities are used as established tools, not claimed as new. A published all-rank spectral factorization for consecutive-layer hypersimplex **polytope one-skeleta** includes additional same-rank Johnson exchange edges; the two-rank *inclusion graph alone* used here is not that one-skeleton.

## Limitations
The result is restricted to two-color uniform-vertex asynchronous minority with closed-neighborhood tie retention and fully joined clique/independent-set graphs. It does not give exact absorption-time distributions, absorption probabilities of individual classes, or a tight total-variation mixing-time formula. The spectral computation concerns recurrent classes only. The count and gap formulas are mathematical proofs, not independent certification of historical novelty; potentially unindexed anti-coordination or zero-temperature spin literature remains a priority risk.

## References
1. J.-B. Rouquier, D. Regnault, É. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119v1, submitted 2010-11-23; extended journal article, *Theoretical Computer Science* 412 (2011), 3947–3963. https://arxiv.org/abs/1011.5119
2. J. Kun, B. Powers, L. Reyzin, *Anti-Coordination Games and Stable Graph Colorings*, arXiv:1308.3258v1, 2013-08-14. https://arxiv.org/abs/1308.3258
3. P. A. Papp, R. Wattenhofer, *Stabilization Time in Minority Processes*, LIPIcs ISAAC 2019, Article 43, DOI:10.4230/LIPIcs.ISAAC.2019.43. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2019.43
4. L. Qiu, J. Qiu, Z. Jiang, C. Shen, *On the Spectrum of Middle-Cubes*, arXiv:0911.0126 (2009); standard two-rank Boolean-lattice incidence spectra. https://arxiv.org/abs/0911.0126
5. *Exact Laplacian factorization and paired harmonics of consecutive-layer hypersimplex graphs*, published mathematical record 2026-10-11. Its polytope-graph edge criterion includes boundary Johnson edges absent from the current dynamics graph.
