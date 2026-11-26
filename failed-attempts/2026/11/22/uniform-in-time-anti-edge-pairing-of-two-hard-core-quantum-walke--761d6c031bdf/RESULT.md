# Uniform-in-time anti-edge pairing of two hard-core quantum walkers on cocktail-party networks

## Finding
Let \(m\ge3\), and let \(G_m=K_{2m}\setminus M\), where \(M\) is a perfect matching. The \(m\) two-vertex parts of this cocktail-party graph are denoted \(P_i=\{i^+,i^-\}\). Put two identical hard-core bosons on distinct vertices, with unit hopping on each edge of \(G_m\) and zero on-site potentials. The orthonormal occupation basis is \(\lvert\{u,v\}\rangle\), \(u\ne v\), and the Hamiltonian moves one occupant along an edge to a vacant site with matrix element \(+1\). Initially occupy the nonadjacent pair \(P_1\).

Let \(Q_m(t)\) be the probability that both particles still occupy *one of the same two-vertex parts* at time \(t\ge0\) (not necessarily \(P_1\)). Set \(q_-=m-2\), \(q_+=2m-2\), and
\[
F_q(t)=\frac{4q}{q^2+4}\sin^2\bigl(t\sqrt{q^2+4}\bigr).
\]
The **exact** quantum pairing probability is
\[
\boxed{Q_m(t)=1-\frac1m F_{q_+}(t)-\frac{m-1}{m}F_{q_-}(t).}
\]
In particular, the quantum *unpairing* probability is uniformly small, at arbitrary observation times:
\[
\boxed{\lim_{m\to\infty}m\sup_{t\ge0}(1-Q_m(t))=4.}
\]
The upper bound is asymptotically sharp already at the explicit time
\[
\tau_m=\frac{\pi}{2\sqrt{(m-2)^2+4}}\sim\frac{\pi}{2m}.
\]

For the continuous-time classical two-particle symmetric exclusion process on the **identical** configuration graph, in which each permitted particle hop has rate one, let \(C_m(t)\) be the probability that the two particles occupy a common part when started from \(P_1\). Then
\[
\boxed{C_m(t)=\frac1{2m-1}+\frac{2m-2}{2m-1}e^{-(4m-2)t},\qquad
\lim_{m\to\infty}C_m(\tau_m)=e^{-2\pi}.}
\]
Thus the same natural observation time gives \(Q_m(\tau_m)\to1\), while \(C_m(\tau_m)\to e^{-2\pi}\). This is dynamical confinement to nonedges rather than an attraction-induced, nearest-neighbor dimer: there is no added interaction energy favoring a pair.

## Assumptions and scope
Every integer \(m\ge3\) is permitted; all hopping amplitudes are exactly one and all graph vertices have zero site energy. There are precisely two identical hard-core bosons (no double occupancy). Time is dimensionless in inverse hopping units, with \(\hbar=1\). Probability is measured in the orthonormal two-element-subset basis. The classical comparison is not a discrete-time walk or a degree-normalized walk: it assigns independent unit-rate moves to each allowed occupied-to-empty graph edge. Both dynamics start at \(\lvert\{1^+,1^-\}\rangle\) or the corresponding classical configuration. No claims of bound pairs on an underlying geometric lattice, of actual attractive interactions, or of noise robustness are made.

## Proof
Write \(a_i=\lvert\{i^+,i^-\}\rangle\), and for \(i<j\) write \(b_{ij}^{\epsilon\delta}=\lvert\{i^\epsilon,j^\delta\}\rangle\). Define normalized sign-even configurations \(c_{ij}=\tfrac12\sum_{\epsilon,\delta\in\{+,-\}} b_{ij}^{\epsilon\delta}\). The subspace \(\mathcal U=\operatorname{span}\{a_i,c_{ij}\}\) is invariant under the hopping Hamiltonian: interpart hopping is insensitive to the signs, and all amplitudes starting from \(a_1\) are sign-even. (The sign-odd sectors are consequently irrelevant to the measured evolution.)

Let \(R\) be the \(m\)-by-\(\binom m2\) unsigned incidence matrix of the complete graph \(K_m\): \(R_{i,\{j,k\}}=1\) if and only if \(i\in\{j,k\}\). Directly counting the allowed moves gives the restricted **symmetric** matrix
\[
H\big|_{\mathcal U}=\begin{pmatrix}0&2R\\2R^{\mathsf T}&2(R^{\mathsf T}R-2I)\end{pmatrix}.
\]
Indeed, \(a_i\) couples with amplitude \(2\) to each \(c_{ij}\); two different \(c\)-states share an amplitude \(2\) precisely when their index-pairs intersect, and the diagonal is zero. The identities \(R^{\mathsf T}R-2I=A(L(K_m))\) and \(RR^{\mathsf T}=(m-2)I+\mathbf1\mathbf1^{\mathsf T}\) follow entrywise. The latter has squared singular values \(q_+=2m-2\) (once, on constants) and \(q_-=m-2\) (\(m-1\) times, orthogonal to constants). As \(m\ge3\), both are positive.

For each left singular unit vector of \(R\) with squared singular value \(q\), its paired normalized right singular vector gives a two-dimensional invariant block
\[
H_q=\begin{pmatrix}0&2\sqrt q\\2\sqrt q&2(q-2)\end{pmatrix}
=(q-2)I+\begin{pmatrix}-(q-2)&2\sqrt q\\2\sqrt q&q-2\end{pmatrix}.
\]
The traceless summand squares to \((q^2+4)I\); therefore, evolution from the left-singular basis state into its right-singular partner has probability \(F_q(t)\). The initial vector \(a_1\) has squared projections \(1/m\) on the constant left-singular channel and \((m-1)/m\) on the orthogonal channels. These channels remain orthogonal during evolution. Summing their right-sector probabilities proves the displayed formula for \(1-Q_m(t)\).

Using \(\sin^2\le1\), for every \(t\ge0\),
\[
0\le1-Q_m(t)\le \frac{4q_+}{m(q_+^2+4)}+\frac{4(m-1)q_-}{m(q_-^2+4)}.
\]
Multiplying the right side by \(m\) and taking \(m\to\infty\) gives \(4\). At \(t=\tau_m\), the \(q_-\) sine equals one, while the other term contributes only \(O(m^{-2})\) by its prefactor, so \(m[1-Q_m(\tau_m)]\to4\). The matching upper and lower bounds prove the all-time supremum limit without requiring that a supremum be attained at a finite time.

For the classical chain, each paired configuration \(a_i\) has exactly \(4(m-1)\) outgoing moves, all to unpaired configurations. Every unpaired configuration \(b_{ij}^{\epsilon\delta}\) has exactly two moves to paired configurations (the two complementary vertices in the two occupied parts). Consequently, the indicator of being paired is an exactly lumpable two-state continuous-time Markov chain with transition rates \(4(m-1)\) from paired to unpaired and \(2\) in the opposite direction. Its forward equation is \(C_m'(t)=2-(4m-2)C_m(t)\), \(C_m(0)=1\), giving the stated finite-size formula. Since \((4m-2)\tau_m\to2\pi\), the classical limit follows.

## Verification
The standalone program \(\texttt{verify.py}\) constructs the full unordered two-boson configuration Hamiltonian from first principles and independently exponentiates it at multiple observation times, comparing the total paired probability to the displayed two-frequency formula. It also directly constructs and exponentiates the full continuous-time classical exclusion generator, independently comparing with the exact lumped-chain formula. Numerical high-size tests evaluate the sharp upper and lower asymptotic expressions without exponentiating large matrices. The program checks normalization, finite-size comparisons, and the claimed limits. These finite computations corroborate the all-parameter algebraic proof; they do not establish it in place of that proof.

## Relationship to prior work
Audenaert, Godsil, Royle, and Rudolph, *Symmetric Squares of Graphs* (arXiv:math/0507251, first public 2005-07-12), introduced and analyzed the relevant two-token symmetric-square adjacency Hamiltonian and spectral methods for strongly regular graphs. In particular, their equitable-partition and symmetric-square framework already applies to cocktail-party graphs, so neither that framework nor generic spectral reduction is claimed as new. Their paper does not give the present time-dependent paired-sector probability, its sharp uniform-in-time leakage coefficient, or the classical exclusion comparison.

The published result *The integral Laplacian spectrum of two-token cocktail-party graphs* (2026) treats precisely the same two-token configuration **graph**, but studies its degree-minus-adjacency spectrum and spanning-tree counts. Its signed-pair decomposition is closely related to the sign-even sector here. The exact unitary survival probability and the classical-versus-quantum time-scale separation are distinct dynamical observables; they do not follow from the listed Laplacian eigenvalues alone because the configuration graph is biregular. The published result *Three spectral protection channels and exact collision capture on balanced multipartite quantum networks* (2026) studies **noninteracting bosons with double occupancy permitted** and dissipative collision loss, not the hard-core hopping dynamics or this pairing event.

Gamble and collaborators (arXiv:1002.3003, first public 2010-02-16) analyze two-particle quantum walks on strongly regular graphs, especially their use in graph isomorphism. Their general hard-core Hamiltonian construction covers this model's definition, but the examined derivations concern walk matrix elements, graph distinctions, and short-time series rather than this observable's exact two-frequency law. Qin and collaborators (arXiv:1402.3349, first public 2014-02-14) examine interaction-driven co-walking on one-dimensional lattices; their bound-pair mechanism requires a distinct nearest-neighbor interaction rather than the connectivity-only suppression shown here. These differences limit the novelty assessment to the specific pairing-and-separation law, not the broader phenomena of two-body localization or quantum-classical differences.

## Limitations
The result is for exactly two hard-core bosons on equal two-vertex complete-multipartite parts, unit undirected hopping, no onsite potentials, and a specially prepared initially paired occupation. It establishes confinement to *some* deleted-matching pair, not necessarily to the initial pair. It is not a statement about finite-temperature interactions, disorder, loss, noisy networks, nonuniform rates, many-particle sectors, or spatially local physical dimers. The older general spectral framework and the published token-Laplacian calculation are substantial prior art; an unindexed earlier explicit pairing formula remains a priority risk. No independent audit has been performed.

## References
1. K. Audenaert, C. Godsil, G. Royle, and T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251, first posted 2005-07-12. https://arxiv.org/abs/math/0507251
2. J. K. Gamble, M. Friesen, D. Zhou, R. Joynt, and S. N. Coppersmith, *Two-particle quantum walks applied to the graph isomorphism problem*, arXiv:1002.3003, first posted 2010-02-16. https://arxiv.org/abs/1002.3003
3. X. Qin, Y. Ke, X. Guan, Z. Li, N. Andrei, and C. Lee, *Quantum Walks of Two Interacting Particles in One Dimension*, arXiv:1402.3349, first posted 2014-02-14. https://arxiv.org/abs/1402.3349
4. S. J. Large, M. S. Underwood, and D. L. Feder, *Perfect quantum state transfer of hard-core bosons on weighted path graphs*, arXiv:1412.1022, first posted 2014-12-02. https://arxiv.org/abs/1412.1022
5. *The integral Laplacian spectrum of two-token cocktail-party graphs*, published mathematical research record, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-integral-laplacian-spectrum-of-two-token-cocktail-party-grap--037630a5dd6a
6. *Three spectral protection channels and exact collision capture on balanced multipartite quantum networks*, published mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-spectral-protection-channels-and-exact-collision-capture-o--b8133a80f978
