# A gcd-sensitive transfer law for recurrent spectra and attraction basins of two-bridge conjunctive cycles

## Finding
Consider two directed cycles of lengths \(a\ge2\) and \(b\ge2\) with two feed-forward arcs into the same downstream vertex, from upstream vertices separated by \(1\le s<a\). Under synchronous binary conjunction, define \(g=\gcd(a,b)\), \(\alpha=a/g\), \(\beta=b/g\), \(h=\gcd(g,s)\), \(m=g/h\), \(w=2^\alpha-1\), and
\[
T_z=\begin{pmatrix}w&w\\1&z\end{pmatrix},\qquad
Q_{a,b,s}(z)=\bigl(\operatorname{tr}(T_z^m)\bigr)^h.
\]
The exact number of recurrent states is \(Q_{a,b,s}(2^\beta)\). If \(q_k=[z^k]Q_{a,b,s}(z)\), there are exactly \(q_k2^{\beta k}\) recurrent *phases* having an \(F^{\operatorname{lcm}(a,b)}\)-preimage fiber of size \(2^{\beta(g-k)}\). Each temporal orbit of length \(d\) within this class attracts exactly \(d2^{\beta(g-k)}\) initial states.

The primitive-period census is also explicit. For every positive integer \(t\), let \(a_t=\gcd(a,t)\), \(b_t=\gcd(b,t)\), \(g_t=\gcd(a,b,t)\), \(h_t=\gcd(g_t,s)\), and \(m_t=g_t/h_t\). Then
\[
\left|\operatorname{Fix}(F^t)\right|
=\left[\operatorname{tr}\left(\begin{pmatrix}
2^{a_t/g_t}-1&2^{a_t/g_t}-1\\1&2^{b_t/g_t}
\end{pmatrix}^{m_t}\right)\right]^{h_t}.
\]
For each \(d\mid\operatorname{lcm}(a,b)\), the number of primitive period-\(d\) orbits is
\[
\frac1d\sum_{e\mid d}\mu(d/e)\left|\operatorname{Fix}(F^e)\right|.
\]
Hence both the primitive-period counts and the recurrent-phase basin-size spectrum depend on the bridge separation \(s\) **only through** \(\gcd(\gcd(a,b),s)\), although labelled orbit membership need not.

For example, when \(a=b=8\), the recurrent-state counts for \(s=1,2,4\) are respectively \(2207,2209,2401\). In a uniformly random initial state, the probability of eventual nonzero downstream activity is exactly
\[
1-2^{-a}Q_{a,b,s}(2^{-\beta}).
\]
For \(a=b=n\) and \(s=1\), this probability tends to \(1\); changing only the downstream length to \(b=n+1\) makes it equal to \(2^{-n}(1-2^{-(n+1)})\), tending to \(0\). These last statements hold for integers \(n\ge2\).

## Assumptions and scope
Let \(U_0,\ldots,U_{a-1}\) and \(V_0,\ldots,V_{b-1}\) be labelled vertices, with edges \(U_{i-1\bmod a}\to U_i\) and \(V_{j-1\bmod b}\to V_j\), and additionally \(U_0\to V_0\) and \(U_s\to V_0\). A state \((u,v)\in\{0,1\}^{a+b}\) evolves synchronously under
\[
(F(u,v))_{U_i}=u_{i-1\bmod a},\quad
(F(u,v))_{V_0}=v_{b-1}u_0u_s,\quad
(F(u,v))_{V_j}=v_{j-1}\ (1\le j<b),
\]
where multiplication is Boolean AND. A recurrent phase is a point on any periodic orbit. Its *phase fiber* is the inverse image of that phase under \(F^L\), \(L=\operatorname{lcm}(a,b)\). The attraction basin of a temporal orbit is the union of its phase fibers. The term \(\operatorname{Fix}(F^t)\) denotes points fixed after exactly \(t\) applications, including points with periods properly dividing \(t\).

## Proof
Set \(L=\operatorname{lcm}(a,b)\), and define \(A(u)\subseteq\mathbb Z/g\mathbb Z\) by placing \(r\) in \(A(u)\) exactly when \(u_i=1\) for *all* \(i\equiv r\pmod g\). Let
\[
K(u)=\#\{r\in\mathbb Z/g\mathbb Z:r\in A(u),\ r+s\in A(u)\}.
\]
Backtracking all length-\(L\) walks ending at \(V_j\), the only upstream ancestors are exactly those \(U_i\) with \(i\equiv j+1\) or \(i\equiv j+1+s\pmod g\): every crossing of the gate occurs after \(j+1+kb\) steps, and these predecessors sweep both residue classes. Because conjunction over repeated ancestors is idempotent, this proves the explicit projection
\[
F^L(u,v)=(u,v^*),\quad
v^*_j=v_j\prod_{i\equiv j+1\,(\mathrm{mod}\,g)}u_i
\prod_{i\equiv j+1+s\,(\mathrm{mod}\,g)}u_i.
\]
An empty product does not occur here. Applying the projection twice leaves its output unchanged. Moreover, whenever \(v^*_{b-1}=1\), all upstream bits needed by the gate are one; hence on the projection image, \(F\) simply rotates the upstream and downstream words independently. The projection image is therefore exactly the recurrent set, and all trajectories are periodic by update \(L\).

For a fixed upstream word, its \(g\) residue classes each contain \(\alpha\) bits. A class is active in one way (all ones) and inactive in \(w=2^\alpha-1\) ways. If the pattern of active classes is \((x_r)\), then \(K=\sum_r x_rx_{r+s}\). Thus
\[
\sum_{u\in\{0,1\}^a}z^{K(u)}
=\sum_{x\in\{0,1\}^g}\prod_{r}(w^{1-x_r}z^{x_rx_{r+s}}).
\]
The permutation \(r\mapsto r+s\pmod g\) consists of \(h\) disjoint directed cycles of length \(m\), so each partition function is \(\operatorname{tr}(T_z^m)\). This proves \(Q\), including when \(m=1\). For each upstream word with \(K=k\), exactly \(\beta k\) downstream coordinates may retain arbitrary binary values in the recurrent projection. Therefore there are \(2^{\beta k}\) recurrent phases over that word, and each has exactly \(2^{\beta(g-k)}\) original downstream preimages (the suppressed bits can be chosen freely). The upstream coordinates are fixed by the projection. The statistic \(K\) is unchanged by rotating the upstream word, so all phases on one temporal orbit have equal-size fibers. Their disjoint union is the orbit basin, giving the stated orbit basin formula.

To count points fixed by \(F^t\), a periodic phase must be invariant under rotation by \(t\) on each ring. The upstream and downstream words are therefore repetitions of words of lengths \(a_t\) and \(b_t\). The downstream support condition, applied simultaneously to all repeats, reduces exactly to the same two-bridge conjunction constraints on the reduced words, with common residue modulus \(g_t=\gcd(a_t,b_t)\) and offset \(s\pmod{g_t}\). Applying the preceding transfer count with reduced lengths proves the displayed fixed-iterate formula. Möbius inversion on divisors gives exact primitive orbit counts. Since \(\gcd(g_t,s)=\gcd(g_t,\gcd(g,s))\), the polynomial and every fixed-iterate count are invariant under replacing \(s\) by any \(s'\) with \(\gcd(g,s)=\gcd(g,s')\).

For the survival probability, for a given \(u\) with \(K(u)=k\), precisely \(2^{b-\beta k}\) of the \(2^b\) initial downstream words have all \(\beta k\) permitted sites zero. Averaging gives \(1-2^{-a}Q(2^{-\beta})\). If \(a=b=n\), \(s=1\), then \(Q(z)=\operatorname{tr}(\begin{psmallmatrix}1&1\\1&z\end{psmallmatrix}^n)\). Its evaluation at \(z=1/2\) grows at rate \(\lambda^n\), where \(\lambda=(3+\sqrt{17})/4<2\), proving convergence of survival to one. If \(b=n+1\), then \(g=1\) and \(Q(z)=(2^n-1)+z\), giving the exact displayed probability and its zero limit.

## Verification
The standalone scripts `check_two_bridges.py` and `check_two_bridge_walks.py` can be executed with Python 3 and no external dependencies. The first independently enumerates all initial states for \(115\) small parameter triples, totaling \(76{,}280\) states, compares direct iteration with the projection, checks individual phase-fiber sizes, exact coefficient populations, fixed-iterate formulas and temporal orbit partitions. It additionally checks the three \(16\)-vertex examples at \(a=b=8\) using all \(65{,}536\) initial states per offset. The second independently backtracks predecessor sets symbolically across \(8{,}450\) triples, with \(2\le a\le26\), \(1\le b\le26\), and \(1\le s<a\); it checks the exact walks asserted in the projection proof. All checks passed. The infinite-family theorem follows from the written proof, not from finite computation.

## Relationship to prior work
Jarrah, Laubenbacher and Veliz-Cuba (2008), especially Example 2.9 and Section 7.1, established fundamental cycle-structure bounds and studied a pair of directed cycles linked by one arc. Chen, Gao and Başar (first publicly posted 2017), Section IV-B, **already establish the two-bridge projection as a Hadamard product of elementary projections**, and their Lemma 9 and Theorem 2 cover eventual projection and rotation. Those statements and the generic projection step are **not claimed as new**. The contribution here is an exact closed weighted transfer polynomial for the recurrent-phase basin spectrum, all fixed-iterate and primitive-period populations, the divisor-class invariance under moving the second bridge, and the abrupt downstream survival comparison. The published texts inspected do not supply these numerical classifications. They can be derived using the known projection as a starting point, so unindexed enumerative precedents remain a limitation.

## Limitations
The graph class consists only of two directed cycle components with two arcs entering the same downstream vertex. The phase-fiber sizes are not the same as full temporal-orbit basins; the latter require multiplying by the orbit length. Divisor-class invariance concerns population statistics, not the identity of labelled trajectories. No claim is made about arbitrary linked strongly connected components or additional arcs. The numerical checks are finite and do not establish the all-size theorem without its proof. Independent external verification and exhaustive historical-priority confirmation have not been performed.

## References
- A. S. Jarrah, R. Laubenbacher, and A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, arXiv:0805.0275, first posted 2008-05-02. https://arxiv.org/abs/0805.0275
- X. Chen, Z. Gao, and T. Başar, *Asymptotic Behavior of Conjunctive Boolean Networks Over Weakly Connected Digraphs*, arXiv:1708.01975, first posted 2017-08-07. https://arxiv.org/abs/1708.01975
