# A sharp deadline-driven reversal of epidemic sentinel placement on \(K_{3,4}\)

## Finding
For an irreversible continuous-time susceptible–infected (SI) process on the complete bipartite graph \(K_{3,4}\), suppose the initial infection is uniform over its seven vertices and exactly three vertices are continuously observed. Every infected–susceptible edge transmits independently at rate \(\lambda>0\). Let \(T\) be the time at which a selected observer first becomes infected, with \(T=0\) when the initial case is observed. For \(a=0,1,2,3\), let \(S_a(t)=\Pr(T>t)\) when \(a\) observers belong to the part of size three (each degree four) and the remaining \(3-a\) belong to the part of size four (each degree three).

There exists a unique \(u_*>0\), specified below, such that **every** three-observer configuration minimizing the survival probability at the deadline \(t>0\) is of type \(a=3\) for \(0<\lambda t<u_*\), of type \(a=0\) for \(\lambda t>u_*\), and exactly types \(a=0,3\) at \(\lambda t=u_*\). The mixed allocations \(a=1,2\) are strictly suboptimal for every \(t>0\). The unique threshold is \(u_*=-\log x_*\), where \(x_*\in(0,1)\) is the unique root of
\[
R(x)=11x^5+11x^4-94x^3-94x^2+311x-25=0.
\]
Numerically, \(x_*=0.0826175756653503\ldots\) and \(u_*=2.49353284063757\ldots\). In contrast to this late-deadline reversal, minimizing the **mean** first-detection delay always selects all three higher-degree vertices: \(\mathbb E T_3=4/(21\lambda)<139/(630\lambda)=\mathbb E T_0\).

## Assumptions and scope
Write \(A\) for the three-vertex class and \(B\) for the four-vertex class. Every edge joins one vertex in \(A\) and one in \(B\); all twelve edges have the same transmission rate \(\lambda>0\). Transmission is irreversible and each susceptible vertex receives infection at the sum of rates from its already infected neighbors. The single seed is uniformly chosen among all seven vertices, including the monitored ones. Three permanent, perfectly observing sentinels trigger upon the first infection of any sentinel. All deadlines are deterministic and strictly positive. Placements are equivalent if they select the same number \(a\) of vertices in \(A\), since all vertices in each class are symmetric.

We optimize the probability of detection by a specified deadline, equivalently minimize \(S_a(t)\), rather than the probability of eventual detection (which is one for every allocation). The result is not claimed for networks other than \(K_{3,4}\), for heterogeneous edge rates, or for recovery before detection.

## Proof
Set \(u=\lambda t\) and \(x=e^{-u}\). Let \(i\) and \(j\) count infected **unmonitored** vertices in \(A\) and \(B\), respectively. Before detection, their admissible ranges are \(0\le i\le3-a\), \(0\le j\le1+a\), with \(i+j>0\). In dimensionless time, the transient generator \(Q_a\) has off-diagonal entries
\[
(Q_a)_{(i,j),(i+1,j)}=j(3-a-i),\quad
(Q_a)_{(i,j),(i,j+1)}=i(1+a-j),
\]
whenever the target count is admissible, and diagonal entries
\[
(Q_a)_{(i,j),(i,j)}=-\{j(3-i)+i(4-j)\}.
\]
The negative diagonal counts all transmissions, including those that cause absorption by infecting a sentinel. The initial row distribution assigns masses \((3-a)/7\) and \((1+a)/7\) to count states \((1,0)\) and \((0,1)\) when they exist; seeds on sentinels contribute to detection at time zero. Thus \(S_a(t)=\alpha_a e^{uQ_a}{\bf1}\). The generator is triangular by total infected count, so its finite linear differential system gives the following exact closed forms (including repeated-rate terms):
\[
\begin{aligned}
S_0(t)&=\frac{135x^3+336x^4-405x^5+105x^7-11x^9}{280},\\
S_1(t)&=\frac{107x^3+228x^4-594x^5+(352+120u)x^6-21x^7}{126},\\
S_2(t)&=\frac{23x^3+32x^4-72x^5+40x^6-7x^7}{28},\\
S_3(t)&=\frac{4x^3}{7}.
\end{aligned}
\]
These four expressions are also proved directly by the included checker: it builds the *independent full individual-level* transient generator on the fifteen nonempty subsets of the four unmonitored vertices; it matches the first fifteen Taylor derivatives exactly and verifies that every proposed exponential or exponential-times-linear term is annihilated by that generator's characteristic polynomial. By Cayley–Hamilton and uniqueness for constant-coefficient linear ODEs, this certifies the expressions for all \(t\ge0\), not only sampled times.

The differences factor as
\[
S_2-S_3=\frac{x^3(1-x)}{28}(7x^3-33x^2+39x+7)>0
\]
because \(39x-33x^2\ge6x\ge0\) for \(0<x<1\). Similarly,
\[
S_1-S_3=\frac{x^3}{126}\bigl(35+228x-594x^2+(352+120u)x^3-21x^4\bigr).
\]
Use \(u=-\log x\ge1-x\) to bound the last bracket below by
\[
(1-x)\left[35+x(141x^2-331x+263)\right]>0.
\]
Indeed the quadratic has positive leading coefficient and discriminant \(331^2-4\cdot141\cdot263=-38771<0\). Thus every mixed configuration is strictly worse than the all-\(A\) configuration, at every positive deadline.

Finally,
\[
S_0-S_3=\frac{x^3(1-x)}{280}R(x).
\]
One has \(R(0)=-25\), \(R(1)=120\), and on \([0,1]\),
\[
R''(x)=220x^3+132x^2-564x-188\le-212x-188<0.
\]
Strict concavity and the endpoint signs imply that \(R\) crosses zero exactly once in \((0,1)\): its nonnegative superlevel set is an interval containing \(1\), and it cannot have a separate positive component. Moreover, \(R(x)<0\) below that zero and \(R(x)>0\) above it. Since \(x=e^{-\lambda t}\) decreases strictly from one to zero, the claimed unique deadline reversal and equality case follow. Integrating the exponential survival laws gives \(\mathbb E T_3=4/(21\lambda)\) and \(\mathbb E T_0=139/(630\lambda)\), proving the different mean criterion.

## Verification
Run `python3 verify_k34.py` in a directory containing that standalone file. The verification uses only Python's standard library and exact rational arithmetic. It constructs the actual seven-vertex graph (rather than reusing the count-state generator in the proof); for each of the four allocation types it enumerates all fifteen transient infected subsets, computes the generator, confirms spectral multiplicities, and matches the first fifteen derivatives of the displayed survival formula. It also independently checks the factorization identities, the negative discriminant, endpoint signs, and exact mean-delay values. The included program produced: `PASS: full independent 15-state exact-generator derivative matching, term spectra, mean values, polynomial identities; checks= 89`. The checker supplies finite exact algebraic identities plus a characteristic-polynomial argument; it is not being used to infer universal inequalities from numerical samples. The polynomial sign and uniqueness arguments are supplied in the proof.

## Relationship to prior work
Goering, Sahneh, Albin, Scoglio and Poggi-Corradini (first arXiv version 2015-11-24) give the same continuous-time SI edge-hazard model and the first-passage interpretation, but optimize or measure epidemic hitting times between individual pairs; their result does not imply an exact three-sentinel deadline phase diagram on \(K_{3,4}\). Leskovec and collaborators (2007) formulate broad outbreak-detection sensor placement and give submodular approximation guarantees, but do not obtain this exact finite-graph phase transition. Batlle Franch (2020) gives a generic Markov-chain matrix expression for fixed-horizon optimal sentinel sets; specialization can compute the same surveillance probabilities, but does not itself establish the strict polynomial comparison, unique threshold, or exclusion of mixed placements here. Colman and collaborators (2019) use simulation-based SIR surveillance objectives on empirical and synthetic networks and discuss network topology, rather than this continuous-time SI exact theorem. Heavey and collaborators (2022) prove approximation-hardness and bicriteria methods for expected detection delay, rather than this deadline-probability reversal.

A related published mathematical result on discounted hitting domination for complete bipartite graphs analyzes simple random-walk hitting and *uniform per-source coverage thresholds*, not SI infection spread, deadline probability, or a fixed three-sentinel budget. Its complete-bipartite formulas therefore do not cover the present stochastic-epidemic claim. No matching closed-form phase diagram was located in the inspected evidence; this is not a proof of historical novelty.

## Limitations
The result assumes no recovery, one uniformly random initial infection, perfect permanent monitoring, equal memoryless edge-transmission hazards, a fixed three-observer budget, and exactly the seven-node graph \(K_{3,4}\). A different seed prior, recovery, changing observation frequency or edge heterogeneity may change the placement optimum. Numerical values of the critical time are approximations to a unique polynomial root, whereas the root characterization and strict comparisons are exact. Other finite-graph tables, theses, supplements and unindexed work may contain an equivalent result; independent historical priority assessment has not been performed.

## References
1. M. Goering, F. D. Sahneh, N. Albin, C. Scoglio, P. Poggi-Corradini, “Numerical Investigation of Metrics for Epidemic Processes on Graphs,” arXiv:1511.07893v1, first submitted 2015-11-24, https://arxiv.org/abs/1511.07893.
2. J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen, N. Glance, “Cost-effective Outbreak Detection in Networks,” CMU-ML-07-111, June 2007, https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf. The cover identifies the month only, not a verified day.
3. P. Batlle Franch, “Sensor placement for early detection in compartmental epidemic models on networks,” May 2020, https://upcommons.upc.edu/bitstream/handle/2117/332006/TFG_PauBatlle.pdf.
4. E. Colman, P. Holme, H. Sayama, C. Gershenson, “Efficient sentinel surveillance strategies for preventing epidemics on networks,” PLoS Computational Biology 15 (2019), e1007517, https://doi.org/10.1371/journal.pcbi.1007517.
5. J. Heavey, J. Cui, C. Chen, B. A. Prakash, A. Vullikanti, “Provable Sensor Sets for Epidemic Detection over Networks with Minimum Delay,” AAAI 36 (2022), 10202–10209, https://faculty.cc.gatech.edu/~badityap/papers/network-sensors-aaai22.pdf.
6. “Exact discounted hitting domination of complete bipartite graphs,” publicly available 2026 research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-discounted-hitting-domination-of-complete-bipartite-graphs--f5f86f5d861d. The note concerns random-walk hitting coverage, not epidemic first detection.
