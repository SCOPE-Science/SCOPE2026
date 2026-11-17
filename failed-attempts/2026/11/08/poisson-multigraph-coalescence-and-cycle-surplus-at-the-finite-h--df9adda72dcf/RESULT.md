# Poisson multigraph coalescence and cycle surplus at the finite-hub percolation threshold

## Finding

For each fixed integer \(m\ge2\) and real \(a>0\), independently retain the edges of \(K_{m,n}\) with probability \(p_n=a/\sqrt n\), where \(n>a^2\). Write the left vertex set as \([m]\); the right vertex set has \(n\) vertices. For each unordered pair \(e\) of left vertices, write \(N_{n,e}\) for the count of right vertices whose **entire** left neighborhood is precisely \(e\). Let \((P_e)_e\) be independent \(\operatorname{Pois}(a^2)\) variables. Then

\[
 d_{\rm TV}\bigl(\mathcal L((N_{n,e})_e),\mathcal L((P_e)_e)\bigr)=O_{m,a}(n^{-1/2}).
\]

With probability \(1-O_{m,a}(n^{-1/2})\) no right vertex has three or more left neighbors. On that event, the partition \(\Pi_n\) of left hubs by connectivity is exactly the component partition of the multigraph with \(N_{n,e}\) parallel edges on each left pair. Thus \(\Pi_n\Rightarrow\Pi\), where \(\Pi\) is the component partition of the independent-Poisson multigraph \((P_e)_e\). In particular, the underlying *simple* hub graph has the \(G(m,1-e^{-a^2})\) law, but the multigraph retains more information.

Let \(\beta_n=|E_n|-|V_n|+c_n\) be the total cyclomatic number of the complete percolated bipartite graph, including isolated vertices in the component count \(c_n\). Put \(\kappa=\sum_e P_e-m+|\Pi|\). Then \((\Pi_n,\beta_n)\Rightarrow(\Pi,\kappa)\). For every hub block \(C\in\Pi_n\), let \(S_n(C)\) be the number of original (left plus right) vertices in its component. Encode these masses by the vector \(W_{n,i}=S_n(C_i)/\sqrt n\), where \(C_i\) is the block of \(\Pi_n\) containing hub \(i\) (so the same block size is repeated on its member coordinates). Jointly,

\[
 (\Pi_n,\beta_n,(W_{n,i})_{i=1}^m)
 \ \Longrightarrow\ (\Pi,\kappa,(a|C_i|)_{i=1}^m).
\]

All right-side components containing no left vertex are isolated single vertices. Consequently the largest component \(L_n\) satisfies

\[
 \frac{L_n}{\sqrt n}\Longrightarrow a\max_{C\in\Pi}|C|,
 \qquad \frac{\mathbb E L_n}{\sqrt n}\longrightarrow a\,\mathbb E\max_{C\in\Pi}|C|.
\]

For the smallest nontrivial case \(m=2\), \(L_n/\sqrt n\) has the limiting two-point law \(a\) with probability \(e^{-a^2}\) and \(2a\) otherwise, while \(\beta_n\Rightarrow(P-1)_+\) for \(P\sim\operatorname{Pois}(a^2)\). This gives both macroscopic coalescence and cycle multiplicity in one critical window.

## Assumptions and scope

The integer \(m\) and the real number \(a\) are fixed while \(n\to\infty\). Edges are independently retained. A right-side degree is counted *only* toward the left-side neighbors. All formulas concern ordinary finite simple bipartite graphs before contraction, so parallel edges appear only in the auxiliary hub multigraph. The total cycle rank is \(|E|-|V|+c\) on all vertices, including isolates. No infinite-size interchange in \(m\) is asserted. The convergence of partitions means convergence in distribution on the finite set of partitions of \([m]\); the joint marked convergence uses the specified \(m\)-vector encoding.

## Proof

For a right vertex, the probability of having exact left neighborhood \(e\) of size two is \(r_n=p_n^2(1-p_n)^{m-2}\). Its probabilities for different pairs are disjoint. Thus \((N_{n,e})_e\) is part of a multinomial occupancy count over \(n\) independent categorical trials, with total marked probability \(R_n={m\choose2}r_n=O_{m,a}(n^{-1})\). Couple each categorical marked trial to a Poisson point process of the same total intensity \(R_n\), with independent category labels proportional to \(r_n\). The one-trial total-variation discrepancy is \(O(R_n^2)\) (compare a Bernoulli variable to a Poisson variable of equal mean). Summing over trials and superposing the Poisson processes yields

\[
 d_{\rm TV}\left(\mathcal L((N_{n,e})_e),\bigotimes_e\operatorname{Pois}(nr_n)\right)
 \le O(nR_n^2)=O_{m,a}(n^{-1}).
\]

Since \(nr_n=a^2(1-a/\sqrt n)^{m-2}=a^2+O_{m,a}(n^{-1/2})\), a further Poisson-mean coupling gives the claimed \(O(n^{-1/2})\) total-variation bound. A union bound on degree-three triples gives

\[
 \Pr(\exists\hbox{ right vertex with at least three left neighbors})
 \le n{m\choose3}p_n^3=O_{m,a}(n^{-1/2}).
\]

On the complementary event, every right vertex has degree zero, one or two. Degree-zero right vertices are isolated; degree-one vertices are pendant leaves; and every degree-two right vertex connects precisely its pair of left hubs. Therefore the hub connectivity partition depends only on which \(N_{n,e}\) are nonzero. Since degree-one vertices do not change the cycle rank, replacing each degree-two vertex and its two incident edges by one multigraph edge preserves both hub connectivity and the cyclomatic number. More explicitly, writing \(N_0\) for right isolates, \(N_1\) for the total degree-one right vertices and \(P_n=\sum_eN_{n,e}\), the original graph has \(m+N_0+N_1+P_n\) vertices, \(N_1+2P_n\) edges, and \(N_0+|\Pi_n|\) components. Hence

\[
 \beta_n=P_n-m+|\Pi_n|.
\]

Total-variation convergence of the pair-count vector, followed by a finite-state mapping and the preceding high-probability reduction, yields the joint limit of partition and cycle rank.

For each left hub \(i\), its number \(A_{n,i}\) of degree-one right neighbors is \(\operatorname{Bin}(n,p_n(1-p_n)^{m-1})\), regardless of dependence with other hubs. Its mean is \(a\sqrt n+O_{m,a}(1)\) and its variance is at most \(a\sqrt n\). Chebyshev's inequality and a union bound over fixed \(m\) therefore show

\[
 \max_{1\le i\le m}|A_{n,i}/\sqrt n-a|\longrightarrow0
 \quad\hbox{in probability}.
\]

On the degree-at-most-two event, the component associated with a hub block \(C\) has exactly \(|C|+\sum_{i\in C}A_{n,i}+\sum_{e\subseteq C}N_{n,e}\) vertices; the last sum is \(O_{\mathbb P}(1)\) uniformly across the finitely many possible blocks, by the Poisson coupling. Thus its mass divided by \(\sqrt n\) differs uniformly from \(a|C|\) by \(o_{\mathbb P}(1)\). This proves the claimed joint limit, including largest-component convergence, because right isolates have size one.

For convergence of means, \(L_n\le m+\sum_{i=1}^mD_{n,i}\), where \(D_{n,i}\sim\operatorname{Bin}(n,p_n)\) counts neighbors of hub \(i\). The quantities \(D_{n,i}/\sqrt n\) have uniformly bounded second moments. By Cauchy–Schwarz, \(L_n/\sqrt n\) is uniformly integrable, so its expectations converge. For \(m=2\), the only hub pair has limiting Poisson count \(P\), the hubs coalesce iff \(P\ge1\), and the cycle surplus is \((P-1)_+\), giving the explicit two-point law.

## Verification

The standalone `verify.py` checks the exact graph-theoretic cycle-rank identity for all degree-at-most-two right-neighborhood configurations on \(m=2,3,4\) hubs with up to three right vertices; checks the explicit \(m=2\) Poisson formulas at several parameters; and checks multinomial cell normalizations. These finite checks are regressions only. The infinite asymptotic statement follows from the coupling, union bounds, and moment arguments just proved, not from numerical sampling.

## Relationship to prior work

Christoph, Morawski and Wigderson (2026) establish general spectral percolation thresholds on finite graphs, with bounds rather than the present finite-hub joint limit. Federico (2019/2020) studies critical component sizes in random intersection and bipartite graphs when *both* sides grow as powers of a common parameter; his theorems do not state a fixed-hub Poisson-multigraph limit. Fill, Scheinerman and Singer-Cohen (2000), Rybarczyk (2011) and Kim, Lee and Na (2018) address approximation of the *simple projected random intersection graph* by an independent-edge graph. The ordinary projected-graph limit in the Finding is accordingly not claimed as new: a projected graph forgets multiple shared neighbors, so those equivalence results alone do not determine the bipartite cycle-surplus variable \(\kappa\) or the joint labeled right-neighbor marks. The proposed contribution is the combined finite-hub topology, macroscopic component masses and surviving cycle multiplicities at the spectral scale.

## Limitations

The theorem applies only to fixed \(m\), not a second limit with \(m\to\infty\). The classical projected-graph limit is already part of earlier random-intersection theory. The originality of the *joint marked* statement is a best-knowledge comparison, not independently certified; an older complete finite-hub bipartite percolation treatment could imply it. The 2026 source was checked in abstract form because its full text was inaccessible, and there is no claim to have read missing sections. The theorem does not address edge-dependent percolation.

## References

1. M. Christoph, P. Morawski and Y. Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145 (first publicly posted 2026-08-19), https://arxiv.org/abs/2608.19145.
2. L. Federico, *Critical scaling limits of the random intersection graph*, arXiv:1910.13227 (2019); see also the author's 2020 thesis *Phase transitions and connectivity in random graphs*, Chapter 1, Section 1.5 and Chapter 6, https://pure.tue.nl/ws/portalfiles/portal/147808971/20200309_Federico.pdf.
3. J. A. Fill, E. R. Scheinerman and K. B. Singer-Cohen, *Random intersection graphs when \(m=\omega(n)\): An equivalence theorem relating the evolution of the \(G(n,m,p)\) and \(G(n,p)\) models*, Random Structures & Algorithms 16 (2000), 156–176, doi:10.1002/(SICI)1098-2418(200003)16:2<156::AID-RSA3>3.0.CO;2-H.
4. K. Rybarczyk, *Equivalence of a random intersection graph and \(G(n,p)\)*, Random Structures & Algorithms 38 (2011), 205–234, doi:10.1002/rsa.20356.
5. J. H. Kim, S. J. Lee and J. Na, *On the total variation distance between the binomial random graph and the random intersection graph*, Random Structures & Algorithms 52 (2018), 662–679, doi:10.1002/rsa.20750.
