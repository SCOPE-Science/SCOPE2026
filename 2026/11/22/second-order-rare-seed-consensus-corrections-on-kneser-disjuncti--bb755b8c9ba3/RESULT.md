# Second-order rare-seed consensus corrections on Kneser disjunctive networks

## Finding
Fix integers \(k\ge3\), \(n\ge3k\), a real \(\lambda>0\), and put \(N=\binom nk\), \(p=\lambda/N\), with \(n\) large enough that \(p\le1\). Independently activate each vertex of the Kneser graph \(KG(n,k)\) with probability \(p\), and apply synchronous open-neighborhood Boolean OR updates. Denote by \(T\) the first time at which all vertices are active, with \(T=\infty\) if this never occurs. Define
\[
J_1=\binom{k+1}{2},\qquad J_2=\frac{k(k+1)(2k+1)}6,
\]
\[
A=k^2J_1,\qquad B=\frac{k^2(k-1)}2J_1+\frac{k^3}2J_2-\frac{A^2}{2},
\qquad C=\binom{k+2}{3}k^3+3\binom{k+2}{4}k^4.
\]
For \(Z\sim\operatorname{Poisson}(\lambda)\), as \(n\to\infty\) through integers at fixed \(k,\lambda\),
\[
\boxed{\Pr(T=1)=\Pr(Z\ge k+1)-\frac{e^{-\lambda}\lambda^{k+1}}{(k+1)!}\frac A n
-\frac{e^{-\lambda}}{n^2}\left(\frac{\lambda^{k+1}}{(k+1)!}B+\frac{\lambda^{k+2}}{(k+2)!}C\right)+O_{k,\lambda}(n^{-3}).}
\]
Moreover \(\Pr(T=0)=p^N\), \(\Pr(T=\infty)=(1-p)^N\), and \(\Pr(T=2)=1-p^N-(1-p)^N-\Pr(T=1)\). Thus every nonzero initial configuration becomes all-one no later than time two. The second-order coefficient \(C\) records exactly two distinct minimal collision motifs: three initially active \(k\)-sets sharing a common ground point, and two disjoint pairs of initially active \(k\)-sets intersecting internally. It is *not* just the pair-collision correction from the minimal \(k+1\)-seed case.

## Assumptions and scope
The vertices of \(KG(n,k)\) are the \(k\)-element subsets of \([n]\), with an undirected edge exactly for disjoint subsets and with no loops. If \(X_t(S)\in\{0,1\}\) is the Boolean state of vertex \(S\), then
\[
X_{t+1}(S)=\bigvee_{R\cap S=\varnothing}X_t(R).
\]
All vertices independently have initial state one with probability \(p=\lambda/\binom nk\). The integer \(k\) and positive real \(\lambda\) are held fixed as \(n\to\infty\). No claim is made for growing \(k\), arbitrary correlated seeding, or finite-\(n\) signs of the asymptotic truncation.

## Proof
**Dynamics and transversals.** For any two \(k\)-sets \(R,S\), the union has at most \(2k\) elements, so \(n\ge3k\) provides a \(k\)-set \(H\) disjoint from both. Hence every ordered pair of vertices is connected by a walk of exact length two. A nonempty initial seed family therefore gives \(X_2\equiv1\); the empty seed family remains zero. At time one all vertices are active exactly when every \(k\)-set is disjoint from at least one seed. Equivalently, the selected family has transversal number at least \(k+1\), where a transversal is a set of ground elements meeting every selected \(k\)-set.

**Seed-family size.** Let \(M\) be the number of selected seeds. When \(M\le k\), choose one element from each selected set and extend to a \(k\)-set: a transversal exists, so time-one consensus fails. When \(M=k+1\), a transversal of size at most \(k\) exists if and only if two selected sets intersect. Indeed, one intersection point covers the intersecting pair and one point per remaining seed covers all \(k+1\) seeds using at most \(k\) points, while a family of \(k+1\) pairwise disjoint sets requires \(k+1\) transversal points.

Conditional on \(M=k+1\), the probability \(D_n\) of pairwise disjoint selected \(k\)-sets is exactly
\[
D_n=\prod_{j=0}^{k}\frac{\binom{n-jk}{k}}{\binom nk-j}.
\]
For fixed \(k\ge3\), replacing each denominator by \(\binom nk\) changes its logarithm only by \(O_k(n^{-3})\). Expanding \(\sum_{j=0}^{k}\sum_{i=0}^{k-1}\log(1-jk/(n-i))\), using \(\sum j=J_1\) and \(\sum j^2=J_2\), gives
\[
\log D_n=-\frac{A}{n}-\frac{1}{n^2}\left(\frac{k^2(k-1)}2J_1+\frac{k^3}{2}J_2\right)+O_k(n^{-3}),
\]
and therefore \(D_n=1-A/n-B/n^2+O_k(n^{-3})\).

**Exactly one extra seed.** Conditional on \(M=k+2\), sample \(k+2\) distinct uniform \(k\)-sets. A transversal of size at most \(k\) must save at least two points relative to selecting one point from each of the \(k+2\) sets. At the \(n^{-2}\) scale, exactly two identifications among independent ground-element draws can occur. They save two transversal points precisely in either of these cases: three of the chosen sets share one ground element (\(\binom{k+2}{3}\) choices of sets and \(k^3\) coordinate coincidences), or two disjoint pairs of chosen sets intersect internally at two distinct ground elements (\(3\binom{k+2}{4}\) pairings and \(k^4\) coordinate coincidences). Two distinct intersections involving a common chosen set save only one transversal point; two intersections between the same two sets also save only one. All configurations requiring three or more identifications, and all overlaps of two counted motifs, have probability \(O_k(n^{-3})\). Conditioning the sampled sets to be distinct changes estimates by \(O_k(\binom nk^{-1})=O_k(n^{-3})\). It follows that
\[
\Pr(\text{a transversal of size at most }k\mid M=k+2)=C/n^2+O_k(n^{-3}).
\]

**Larger seed families.** For any fixed ground \(k\)-set \(H\), the number of graph vertices whose corresponding sets intersect \(H\) is at most \(k\binom{n-1}{k-1}=O_k(n^{k-1})\). Its expected number of selected vertices is thus \(O_{k,\lambda}(n^{-1})\). A failure of time-one consensus with at least \(k+3\) seeds requires some \(H\) hitting every selected seed and hence at least \(k+3\) selected members of the collection meeting \(H\). By a union bound over \(\binom nk=O_k(n^k)\) possible \(H\), and the factorial-moment upper bound for a binomial count, the probability of this event is \(O_{k,\lambda}(n^k n^{-(k+3)})=O_{k,\lambda}(n^{-3})\).

**Poisson mixing and first-hitting normalization.** As \(M\sim\operatorname{Bin}(N,\lambda/N)\) and \(N=\Theta_k(n^k)\), its probabilities for fixed counts differ from those of \(Z\sim\operatorname{Poisson}(\lambda)\) by \(O_{k,\lambda}(n^{-k})=O_{k,\lambda}(n^{-3})\). Sum the cases \(M\le k\), \(M=k+1\), \(M=k+2\), and \(M\ge k+3\). This proves the displayed expansion for \(\Pr(X_1\equiv1)\). The initially all-one state contributes only \(p^N=o(n^{-3})\), so the same expansion holds for \(\Pr(T=1)\). The remaining first-hitting probabilities follow from two-step propagation and the absorbing zero initial state. This completes the proof.

## Verification
The self-contained `CHECK.py` recomputes \(A,B,C\), compares the exact disjoint-family probability with its second-order truncation, and uses a separate state-update implementation to check two-step consensus and the transversal criterion on finite Kneser graphs. It also samples the rare \(k+2\)-set transversal failures. Run `python CHECK.py`; its recorded output is `CHECK_OUTPUT.txt`. These finite checks support implementation consistency; the infinite statement follows from the proof above, not from finite sampling.

## Relationship to prior work
Jarrah, Laubenbacher and Veliz-Cuba (2008), *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, studies the structural periodic dynamics of such OR networks; it does not give the present sparse-seed second-order probability. Brešar, Cornet, Dravec and Henning (2023 preprint), *\(k\)-Domination invariants on Kneser graphs*, establishes minimum total-domination structure, including clique minimizers in sufficient order, which covers the basic \(k+1\)-disjoint-seed threshold but not the second-order collision motifs for \(k+2\) seeds. Cornet and Torres (2023), *\(k\)-tuple domination on Kneser graphs*, addresses minimum domination parameters rather than random temporal probabilities. Östergård, Shao and Xu (2015), *Bounds on the domination number of Kneser graphs*, concerns ordinary domination bounds, not the transversal probability expansion. The displayed second-order expansion is therefore presented as a quantitative refinement, not a new minimum domination number or a new general dynamical classification.

## Limitations
Historical priority cannot be proved by searches; an equivalent rare-hypergraph transversal expansion may exist under different terminology. The separate error coefficient is not uniform when \(k\) or \(\lambda\) grows. Sampled finite numerical tests cannot establish the infinite asymptotic statement and do not replace the structural collision proof. The relevant 2015 domination article and some later preprint sections were not fully inspectable in the available access route; an independently reviewed novelty determination remains outstanding.

## References
- Jarrah, A. S., Laubenbacher, R., Veliz-Cuba, A. (2008). *The Dynamics of Conjunctive and Disjunctive Boolean Networks*. arXiv:0805.0275. https://arxiv.org/abs/0805.0275
- Brešar, B., Cornet, M. G., Dravec, T., Henning, M. A. (2023). *\(k\)-Domination invariants on Kneser graphs*. arXiv:2312.15464. https://arxiv.org/abs/2312.15464
- Cornet, M. G., Torres, P. (2023). *\(k\)-tuple domination on Kneser graphs*. arXiv:2308.15603. https://arxiv.org/abs/2308.15603
- Östergård, P. R. J., Shao, Z., Xu, X. (2015). *Bounds on the domination number of Kneser graphs*. *Ars Mathematica Contemporanea* 9(2), 187–195. https://www.dlib.si/details/URN:NBN:SI:doc-G3YP01PE
