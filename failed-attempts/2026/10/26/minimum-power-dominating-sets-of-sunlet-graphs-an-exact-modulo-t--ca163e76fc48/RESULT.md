# Minimum power dominating sets of sunlet graphs: an exact modulo-three census

## Finding
For each integer \(n\ge3\), form the labeled sunlet \(S_n=C_n\circ K_1\) by adjoining a pendant leaf \(v_i\) to each vertex \(u_i\) of the cycle \(C_n\), with subscripts modulo \(n\). A power dominating set first observes the selected vertices and all their neighbours. Thereafter any observed vertex with exactly one unobserved neighbour forces that neighbour. Let \(M_n\) be the number of power dominating vertex subsets of minimum possible cardinality. Then
\[
\gamma_P(S_n)=\left\lceil\frac n3\right\rceil,\qquad
M_n=\begin{cases}
3,&n\equiv0\pmod3,\\
3n,&n\equiv2\pmod3,\\
22,&n=4,\\
\frac{n(3n+1)}2,&n\equiv1\pmod3,\ n\ge7.
\end{cases}
\]
Moreover all minimum sets have an explicit classification by cyclic gaps described below. Counts distinguish each labeled vertex subset, not orbits under rotations, reflections, or graph isomorphisms.

## Assumptions and scope
The graph is finite, simple, and undirected, with \(n\ge3\). A set is *minimum* if it power dominates and has cardinality \(\gamma_P(S_n)\); this differs from being merely inclusion-minimal. If \(P\subseteq V(S_n)\), write its projection to the core cycle as \(T(P)=\{i:u_i\in P\text{ or }v_i\in P\}\). A cyclic gap of \(T=\{i_1,\ldots,i_k\}\), listed in cyclic order, is the number \(d_j\) of cycle edges from \(i_j\) to \(i_{j+1}\), with \(i_{k+1}=i_1\) cyclically. Thus \(\sum_jd_j=n\).

## Proof
**Projection lemma.** If \(P\) power dominates \(S_n\), then \(T(P)\) dominates \(C_n\). Indeed, suppose \(u_i\) is not in the closed cycle-neighbourhood of \(T(P)\). The indices \(i-1,i,i+1\) have neither core nor leaf initially selected. The vertex \(u_i\) is unobserved after the first step. To observe it later one of \(u_{i-1}\) or \(u_{i+1}\) must force it. But the private leaf of either such neighbour is initially unobserved and can itself be observed only after that core vertex forces it; forcing its leaf requires \(u_i\) already to be observed. Taking the first time \(u_i\) would be observed gives a contradiction. Hence \(|P|\ge|T(P)|\ge\gamma(C_n)=\lceil n/3\rceil\). Selecting the core vertices at any minimum dominating set of \(C_n\) observes the whole core immediately, after which each remaining leaf is forced. Therefore \(\gamma_P(S_n)=\lceil n/3\rceil\). Every minimum \(P\) chooses exactly one of \(u_i,v_i\) at each index of a minimum dominating set \(T\), and no vertices outside these pairs.

**Gap analysis.** Write \(k=\lceil n/3\rceil\). The cyclic gaps of any such \(T\) are in \(\{1,2,3\}\), since an unselected core vertex must be adjacent to \(T\). Their *deficit* is \(\sum_j(3-d_j)=3k-n\in\{0,1,2\}\). Mark a selected core vertex by \(A\), or its selected leaf by \(B\). For a gap of length three from one selected index to another, the core vertex immediately next to the first index is initially unobserved if that endpoint is marked \(B\). Its only possible forcing neighbour is that selected core vertex: the other core neighbour has an unobserved private leaf and cannot force towards the endpoint before the target is observed. Consequently any \(B\) with length-three gaps on **both** sides leaves two core neighbours mutually blocked forever. Conversely the classifications that follow guarantee forcing: all marked \(A\) vertices immediately see their two core neighbours; a \(B\) with one already observed core neighbour forces its other core neighbour if needed; after the complete core is observed, every unselected private leaf is forced by its core vertex.

If the deficit is zero, every gap has length three. All selected indices have length-three gaps on both sides, so all are marked \(A\). There are exactly three choices of \(T\), corresponding to cyclic phases. Hence \(M_n=3\) for \(3\mid n\).

If the deficit is one, exactly one gap has length two and all others have length three. Only its two endpoints may be marked \(B\). Both cannot be marked \(B\), since their common intervening core vertex is unobserved and each \(B\) has another unobserved neighbour across a length-three gap; neither can start forcing. Each of the other three choices (both \(A\), or one \(B\)) succeeds by the stated forcing rule. The single short gap has \(n\) labeled locations, so \(M_n=3n\) for \(n\equiv2\pmod3\).

If the deficit is two, the cyclic gaps consist either of (I) one gap of length one and the remaining gaps of length three, or (II) two gaps of length two and the remaining gaps of length three. In case (I), only the two adjacent selected endpoints of the length-one gap can be \(B\); both remain observed, so their independent replacements give **four** feasible markings. The length-one gap has \(n\) labeled locations, contributing \(4n\).

In case (II), a \(B\) can occur only at a selected endpoint incident with a length-two gap. For \(k\ge3\), if the short gaps are adjacent, they involve three distinct selected indices. Their three selected leaves may be substituted in any of the \(2^3-1=7\) ways except replacing all three: if all are \(B\), both intermediate core vertices are unobserved and every \(B\) sees two unobserved core neighbours. If at least one index remains \(A\), its adjacent gap intermediates are observed, and propagation proceeds successively toward any other selected \(B\) and its remaining unobserved core neighbour. If the two short gaps are disjoint, they involve four selected indices. Each short gap allows exactly the three patterns \(AA,AB,BA\), independently, hence \(3^2=9\) choices. The forbidden \(BB\) pattern leaves each endpoint unable to force its unknown neighbour in its other, length-three gap. With \(k\ge3\), there are \(n\) labeled minimum core dominating sets with adjacent short gaps and \(n(k-3)/2\) with disjoint short gaps: mark an ordered selected index and choose two of \(k\) gap positions, then divide the resulting \(n\binom{k}{2}\) marked structures by their \(k\) selected indices. Thus their count is \(4n+7n+9n(k-3)/2=n(3n+1)/2\), because \(k=(n+2)/3\).

The remaining deficit-two boundary case is \(k=2\), necessarily \(n=4\). Type (I) gives \(n=4\) core patterns, each with four markings. In type (II), both length-two gaps have the **same** two endpoints; there are two opposite pairs, each allowing exactly three markings, since replacing both endpoints blocks all ring forcing. Thus \(M_4=4\cdot4+2\cdot3=22\). These are all possible cases and complete the proof.

## Verification
The included standalone program `VERIFY.py` constructs the actual \(2n\)-vertex graph and iteratively applies the observation and forcing rules. It exhaustively checks all subsets of size \(\lceil n/3\rceil\) for \(3\le n\le15\) against the formula. Independently, it enumerates each minimum dominating core set and its binary core-versus-leaf lifts for \(3\le n\le13\), comparing graph propagation with the cyclic-gap classification. Both checks passed. They are finite checks of a separate argument, not the proof of the unbounded statement.

The counts at \(n=3,4,5,6,7,8,9,10,11,12,13,14,15\) are respectively \(3,22,15,3,77,24,3,155,33,3,260,42,3\).

## Relationship to prior work
Saibavani and Parvathi (2019), Theorem 3.1, determine the sunlet power domination number \(\lceil n/3\rceil\), but do not enumerate the optimal vertex sets or permit a core-versus-leaf census. Brimkov, Patel, Suriyanarayana and Teich (2018), Proposition 20 and Question 3, obtain power domination polynomials for coronas with attached cliques of size greater than one and explicitly single out the one-leaf corona as a more difficult case. The present result determines one natural coefficient—the coefficient at the minimum degree—for the cycle one-leaf corona, rather than the full polynomial. Bläsius, Göttlicher and Schirneck (2026) study enumeration of inclusion-minimal power dominating sets through an implicit hitting-set method. Their accessible abstract provides an algorithmic context, not a closed formula for labeled minimum sets of sunlets; the full text was not accessible for a conclusive whole-document comparison.

## Limitations
The formula counts **minimum** power dominating sets, not all inclusion-minimal sets and not the full power domination polynomial. It is for the one-leaf cycle corona, not arbitrary coronas. This proof is self-contained but has not undergone independent mathematical review. Historical-priority uncertainty remains, particularly because the full text of the 2026 algorithmic study was unavailable; absence in indexed searches is not a proof of novelty.

## References
1. T. N. Saibavani and N. Parvathi, *Power domination number of sunlet graph and other graphs*, Journal of Discrete Mathematical Sciences and Cryptography 22(6) (2019), 1121–1127. DOI: 10.1080/09720529.2019.1689610.
2. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984 (2018), especially Proposition 20 and Question 3. https://arxiv.org/abs/1805.10984
3. T. Bläsius, M. Göttlicher, M. Schirneck, *Implicit Hitting Set Enumeration for Power Dominating Sets*, arXiv:2610.24214v1 (first submitted 2026-10-16). https://arxiv.org/abs/2610.24214
