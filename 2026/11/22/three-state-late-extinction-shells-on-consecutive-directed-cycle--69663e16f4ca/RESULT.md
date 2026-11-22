# Three-state late extinction shells on consecutive directed cycle bouquets

## Finding

Let \(a\ge2\) be an integer. Take two consistently oriented directed cycles of lengths \(a\) and \(a+1\), identify precisely one hub vertex, and otherwise retain disjoint vertices. Under simultaneous binary AND updates from all incoming neighbors, let \(E=a(a+1)\) and let \(\tau(x)\) be the first update at which the trajectory from \(x\) is identically zero, with \(\tau(\mathbf1)=\infty\). Every non-all-one configuration reaches the zero fixed point by update \(E\).

For every integer \(k\) with \(1\le k\le a\), the generating polynomial for configurations that are **not** all ones and remain nonzero at time \(E-k\), weighted by the *number of zeros in the initial configuration*, is exactly

\[
L_{E-k}(z)=(2k-1)z+(k-1)z^2.
\]

In particular, there are exactly \(3k-2\) such initial configurations; exactly \(2k-1\) have a single initial zero and exactly \(k-1\) have two initial zeros. There are no others. Hence exactly **three** configurations first reach zero at each of the times \(E-a+1,E-a+2,\ldots,E-1\): two with one initial zero and one with two. Exactly **one** configuration first reaches zero at time \(E\), having exactly one initial zero. The final \(a\) extinction shells are therefore size \(3,3,\ldots,3,1\).

## Assumptions and scope

The graph is the **directed** one-hub bouquet, not the undirected figure-eight graph. Every edge around each of the two cycles is directed consistently, with no additional edges or self-loops; there are \(2a\) labelled vertices. Each vertex other than the hub has exactly one incoming edge and copies its input. The hub receives one incoming edge from each cycle and takes their Boolean AND. All vertices update at the same discrete time. The polynomial counts labelled **initial** configurations, rather than orbits or patterns modulo graph automorphisms. The all-one configuration is excluded from survival counts because it is fixed and never extinguishes. The all-zero configuration has \(\tau=0\).

For any vertex \(u\), write \(\alpha(u)\) for the distance from \(u\) forward to the hub along its unique cycle; for the hub take distance zero. Similarly, write \(\beta(v)\) for the distance forward from the hub to \(v\). Every integer value \(1,\ldots,a-1\) occurs twice among the \(\alpha\) values, while \(a\) occurs once and \(0\) occurs once. The same statement holds for \(\beta\).

## Proof

**1. Exact predecessor propagation.** By induction on time, the value at vertex \(v\) at time \(t\) is the AND of the initial bits at all vertices from which there is a directed walk of exactly \(t\) edges to \(v\). Denote this predecessor set by \(R_t(v)\), and write \(M_t(v)=V\setminus R_t(v)\). For an initial zero set \(Z\ne\varnothing\), the state at time \(t\) has a nonzero bit if and only if \(Z\subseteq M_t(v)\) for at least one \(v\). This statement is an exact equivalence, not a probability approximation.

**2. The two-cycle length semigroup.** Every walk from \(u\) to \(v\) of length at least \(a^2\) must pass through the hub. Every such walk has length

\[
\alpha(u)+ma+n(a+1)+\beta(v),\qquad m,n\in\mathbb Z_{\ge0}.
\]

Conversely, every such length is realizable: follow \(u\) to the hub, traverse the two hub-return cycles \(m\) and \(n\) times in any order, then proceed to \(v\). Put \(S=\langle a,a+1\rangle\). Its Frobenius conductor is \(c=a(a-1)\): every integer at least \(c\) belongs to \(S\), but \(c-1\) does not. More specifically,

\[
[c-a,c-2]\cap\mathbb Z\subseteq S,
\]

since \(c-a+r=(a-2-r)a+r(a+1)\) for \(0\le r\le a-2\). Thus among integers at least \(c-a\), the **only** gap is \(c-1\).

**3. Geometry of the missing predecessor sets.** Take \(t=E-k\) with \(1\le k\le a\); then \(t\ge a^2\), and for all \(u,v\),

\[
t-\alpha(u)-\beta(v)\ge a^2-2a=c-a.
\]

By the preceding semigroup fact, the exact-length walk \(u\to v\) is missing precisely when

\[
\alpha(u)+\beta(v)=t-(c-1)=2a+1-k.
\]

For a given target \(v\), this describes the initial sources that are absent from \(R_t(v)\). Nonempty missing sets have either the unique source at distance \(\alpha=a\), or the two distinct sources sharing some distance \(\alpha\in\{a+1-k,\ldots,a-1\}\). Conversely, each such singleton or pair is attained for a suitable target distance \(\beta=2a+1-k-\alpha\); that distance lies in \(\{1,\ldots,a\}\). Missing sets with the same distance can be duplicated at two targets, which does not affect the count of distinct zero subsets.

**4. Enumerating surviving zero sets.** The condition \(Z\ne\varnothing\) and \(Z\subseteq M_t(v)\) allows precisely: one zero at any of the \(2(k-1)+1\) vertices with \(\alpha\ge a+1-k\); or both zeros at one of the \(k-1\) distance-pairs with \(\alpha\in\{a+1-k,\ldots,a-1\}\). No zero set of size at least three is possible. These classes are disjoint and exhaustive, proving

\[
L_{E-k}(z)=(2k-1)z+(k-1)z^2.
\]

**5. First-entry shells and the terminal cutoff.** The zero state is absorbing, so subtraction of consecutive survival polynomials counts first extinction. For \(1\le k\le a-1\),

\[
L_{E-(k+1)}(z)-L_{E-k}(z)=2z+z^2.
\]

This is the shell at time \(E-k\). At time \(E\), every difference \(E-\alpha(u)-\beta(v)\) is at least \(c\), so every source reaches every target in exactly \(E\) steps. Consequently \(F^E(x)=\mathbf0\) for every \(x\ne\mathbf1\); \(\mathbf1\) remains fixed. Since \(L_{E-1}(z)=z\), the final shell at time \(E\) is exactly one singleton-zero state. The two constants are the only recurrent states. This proves every assertion, including the case \(a=2\).

## Verification

Two independent executable checks accompany this result. `check_direct.py` enumerates all \(2^{2a}\) labelled initial states for every \(2\le a\le7\), applies the Boolean coordinate rules directly and checks the terminal first-entry counts and initial zero weights. `check_walk.py` instead propagates exact-length directed predecessor bitsets and enumerates allowable missing-source subsets for every \(2\le a\le40\). Both scripts passed when run from their packaged contents. The finite tests confirm boundary conventions but are not substitutes for the preceding all-size proof.

For example, with \(a=4\), the directed graph has eight vertices and \(E=20\); the exact numbers of configurations first reaching zero at times \(17,18,19,20\) are \(3,3,3,1\). With \(a=7\), the terminal times are \(50,51,52,53,54,55,56\), with first-entry counts \(3,3,3,3,3,3,1\).

## Relationship to prior work

The general connection between finite conjunctive Boolean network height and the exponent of its Boolean adjacency matrix, and the fact that the cyclic index controls limit-cycle periods, are established in Jarrah, Laubenbacher and Veliz-Cuba (2008). The present statement does **not** claim those structural facts or the classical two-generator Frobenius conductor as new. Its distinction is an exact late-time **labelled initial-state and zero-weight profile**, including constant size-three extinction shells, for an infinite family of consecutive directed double circuits.

Noual (2010) studies synchronous double Boolean automata circuits with the identical two-cycle-one-hub geometry; its positive-positive case is treated via earlier periodic-attractor results, while its developed formulas count periodic configurations and attractors with negative side circuits. The inspected text does not give the stated late-time transient zero-weight population formula. Demongeot, Noual and Sené (2012) describe doubly positive double circuits and their attractors; accessible indexed excerpts concern recurrent configurations, not the terminal extinction shells. Melliti et al. (2013) analyze **asynchronous** intersected circuits; their update model is different. A mathematically equivalent treatment of the explicit terminal defect sets in older, incompletely inspected sources cannot be excluded.

## Limitations

The theorem concerns only two **consecutive** cycle lengths and simultaneous binary AND dynamics. The first \(E-a\) extinction-time shells are not classified here. It does not assert that the absolute graph exponent or periodic attractor count is previously unknown. Some historical literature was accessible only in indexed excerpts rather than complete full text, so publication priority beyond the compared material remains uncertain. The proof and finite checks have not undergone independent external mathematical validation.

## References

- Abdul Salam Jarrah, Reinhard Laubenbacher and Alan Veliz-Cuba. *The Dynamics of Conjunctive and Disjunctive Boolean Networks*. arXiv:0805.0275, first version 2 May 2008. https://arxiv.org/abs/0805.0275
- Mathilde Noual. *Dynamics in parallel of double Boolean automata circuits*. arXiv:1011.3930, first version 17 November 2010. https://arxiv.org/abs/1011.3930
- Jacques Demongeot, Mathilde Noual and Sylvain Sené. *Combinatorics of Boolean automata circuits dynamics*. Discrete Applied Mathematics 160 (2012), 398–415. https://doi.org/10.1016/j.dam.2011.11.005
- Tarek Melliti, Mathilde Noual, Damien Regnault, Sylvain Sené and Jérémy Sobieraj. *Full characterisation of attractors of two intersected asynchronous Boolean automata cycles*. arXiv:1310.5747, first version 21 October 2013. https://arxiv.org/abs/1310.5747
