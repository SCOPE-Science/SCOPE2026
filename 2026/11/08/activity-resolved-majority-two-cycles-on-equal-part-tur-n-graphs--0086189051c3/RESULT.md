# Activity-resolved majority two-cycles on equal-part Turán graphs

## Finding
For integers \(r,q\geq 2\), let \(G_{r,q}=K_{q,\ldots,q}\) be the labelled complete \(r\)-partite graph with \(r\) independently labelled parts of size \(q\). At each discrete time every vertex takes the strict majority bit among its open neighbors, retaining its own bit on a tie. Let \(h_q=\binom{q}{q/2}\) when \(q\) is even, and \(h_q=0\) when \(q\) is odd.

Every trajectory eventually has least period one or two. There are exactly
\[
F_{r,q}=2+h_q^{r}
\]
fixed configurations. For \(1\leq a\leq\lfloor r/2\rfloor\), let \(N_{r,q}(a)\) be the number of **configurations**, not orbits, belonging to a primitive two-cycle and having exactly \(2aq\) vertices change bit at every step. If \(r=2k\) is even, then
\[
N_{r,q}(a)=\frac{r!}{a!^2(r-2a)!}\,h_q^{r-2a},\qquad 1\leq a\leq k.
\]
If \(r=2k+1\) is odd, then
\[
N_{r,q}(a)=
\begin{cases}
\dfrac{r!}{a!^2(r-2a)!}\,h_q^{r-2a},&1\leq a<k,\\[5pt]
r\binom{r-1}{k}(2^q-2),&a=k.
\end{cases}
\]
The conventional empty product is used: \(h_q^0=1\), including for odd \(q\). There are no other primitive two-cycle configurations or activity values. The number of primitive two-cycle **orbits** with this activity is exactly \(N_{r,q}(a)/2\). The total two-step-periodic population is \(F_{r,q}+\sum_a N_{r,q}(a)\).

In particular, when \(r\) and \(q\) are both odd, every primitive two-cycle has a *single* partially occupied part, all remaining parts change completely and exactly half of those full parts initially contain ones. When \(q\) is even, new activity strata occur, with multiple half-occupied parts remaining fixed during a two-cycle. This is a sharp parity distinction within the same natural graph family.

## Assumptions and scope
Each part contains \(q\) distinct labelled vertices, and two different parts are joined by all possible edges; no vertices inside one part are adjacent. The degree of every vertex is \(d=q(r-1)\). For a configuration \(x\in\{0,1\}^{rq}\), denote by \(s_i(x)\in\{0,\ldots,q\}\) the number of ones in part \(i\), and by \(K(x)=\sum_i s_i(x)\) the total number of ones. A part is *mixed* if its count lies strictly between zero and \(q\). An activity-\(2aq\) periodic configuration changes exactly \(2aq\) distinct vertex bits between consecutive states. Counts are for labelled configurations; temporal rotations are not quotiented until the orbit count is taken.

## Proof
**Local part rule.** Every vertex in part \(i\) sees exactly \(K-s_i\) neighboring ones, and has degree \(d=q(r-1)\). Thus, writing \(T=d/2\), the updated part is all one if \(K-s_i>T\), all zero if \(K-s_i<T\), and unchanged if \(K-s_i=T\). At equality \(T\) must be integral. This proves that every output part is uniform unless it was mixed and experienced a tie.

**Restriction to periods at most two.** Write vertex bits as signs \(z_v\in\{-1,+1\}\). Let \(A\) be the symmetric adjacency matrix of \(G_{r,q}\), with a diagonal one added at each vertex if \(d\) is even. The sign of \((Az)_v\) is the prescribed updated sign, and \((Az)_v\) is always a nonzero integer (the added diagonal resolves exactly the even-degree tie). For an orbit \(z(t)\), let \(E(t)=-z(t)^{\mathsf T}Az(t-1)\). By symmetry,
\[
E(t+1)-E(t)=-\sum_v\bigl(z_v(t+1)-z_v(t-1)\bigr)(Az(t))_v\leq0.
\]
Every nonzero summand is strictly negative, because \(z_v(t+1)\) is the sign of \((Az(t))_v\). Since \(E(t)\) is integral and bounded below, it eventually stops decreasing. Equality then forces \(z(t+1)=z(t-1)\), proving eventual period at most two without relying on finite enumeration.

**Uniform parts.** If a two-periodic configuration contains only uniform parts, let \(a\) parts be all one. A zero part sees \(aq\) ones and a one part sees \((a-1)q\) ones. If both types occur, all zero parts can switch to one while all one parts switch to zero simultaneously exactly when \(a=r/2\); this is possible only for even \(r\). Such states are primitive two-cycles, with \(r\) parts (all \(rq\) vertices) flipping. Otherwise the update becomes unanimous and cannot return to the mixed uniform-part state. A uniform-part fixed configuration must be unanimous: for both part types to stay put would require \(aq\leq T\leq(a-1)q\), which is impossible. When \(q\) is odd the even-\(r\) balanced count is \(\binom r{r/2}\), precisely the stated terminal activity term with \(h_q=0\).

**Mixed-part persistence.** Suppose \(x\) has a mixed part and \(M^2x=x\), where \(M\) is the update. No uniform part can become mixed under one update, so every mixed part of \(x\) must remain unchanged under both updates: it must tie both times. Thus its occupancy \(j\) satisfies \(1\leq j\leq q-1\), and every mixed part has the *same* occupancy \(j=K(x)-T\). The two successive configurations also have the same total \(K\). Because \(0<j<q\), all pure-zero parts switch to pure one and all pure-one parts switch to pure zero. If \(a\) parts are pure zero, \(b\) pure one, and \(c\geq1\) mixed, total preservation forces \(a=b\); hence \(r=2a+c\). In turn, the equation \(K=aq+cj=T+j\) becomes
\[
(c-1)\bigl(j-q/2\bigr)=0.
\]
This identity is necessary and sufficient: given these conditions, mixed parts tie and persist, and the other two groups exchange, so \(M^2x=x\).

If \(c=1\), then \(r=2a+1\), so \(r\) is odd and \(a=(r-1)/2\). The mixed part can contain *any nonempty proper subset* of its \(q\) vertices; the remaining parts split equally into pure zero and pure one. There are exactly \(r\binom{r-1}{a}(2^q-2)\) such configurations, all with activity \(2aq\).

If \(c>1\), the displayed identity forces \(q\) even and \(j=q/2\). Choose \(a\) pure-zero parts, \(a\) pure-one parts, and \(c=r-2a\) half-filled parts. For each half-filled part there are \(h_q\) choices. The count is exactly \(r!\,h_q^{r-2a}/(a!^2(r-2a)!)\). When \(a\geq1\), the pure parts flip and produce a primitive two-cycle. When \(a=0\), all \(r\) parts are half-filled and the configuration is fixed, giving \(h_q^r\) fixed states. The case \(c=1\) with \(j=q/2\) is already included in the preceding arbitrary-proper-subset formula, so it must not be counted twice. For even \(r\), \(c=1\) cannot occur; for odd \(r\), \(a=(r-1)/2\) gives the top activity formula, while smaller \(a\) gives the half-filled strata. The two unanimous configurations complete the fixed-point count.

These cases exhaust all fixed points and all two-cycles, and the earlier energy proof exhausts all possible eventual periods.

## Verification
Two distinct exact-integer implementations accompany this document. `check_bits.py` applies the rule directly to all \(2^{rq}\) labelled binary configurations in 21 cases with \(rq\leq18\), and checks fixed points and the full activity-resolved primitive-two-cycle profile. `check_profiles.py` uses a different state space: all part occupancies \((s_1,\ldots,s_r)\), weighted by \(\prod_i\binom q{s_i}\), and independently verifies 34 parameter pairs by exact two-step tests. Their captured outputs in `bits_output.txt` and `profiles_output.txt` end in `DIRECT_ALL_PASS` and `PROFILE_ALL_PASS`, respectively. All parameter claims are proved above; these finite tests are regression checks, not the all-parameter proof.

For example, \((r,q)=(5,4)\) gives \(F_{5,4}=7778\) fixed states, \(N_{5,4}(1)=4320\) states with eight vertices flipping, and \(N_{5,4}(2)=420\) with sixteen flipping, hence \(2370\) primitive two-cycle orbits. For \((r,q)=(3,3)\), there are exactly two fixed configurations and 18 primitive two-cycle orbits.

## Relationship to prior work
The generic period-at-most-two principle is classical (Goles–Olivos, 1980); it is not asserted as new. Kaaser, Mallmann-Trenn and Natale (2015), particularly their symmetry analysis and Turán-graph example, address voting-time upper bounds, not this complete activity-resolved periodic census. Adams, Brass, Stokes and Troxell (2011) study *irreversible* majority conversion on complete multipartite graphs; irreversible activation cannot yield the reversible two-cycles counted here. Aledo and collaborators (2020) count periodic states for Boolean maxterm/minterm (OR/AND) systems, a different local update. The specific result assessed here is the exact activity-by-activity enumeration under strict synchronous open-neighbor majority with tie retention.

## Limitations
The theorem does not count transient basins or their entrance-time distributions. It concerns equal-sized parts, not arbitrary multipartite block-size vectors, directed graphs, random updates or nonmajority Boolean rules. Direct enumeration covers finitely many parameter pairs; the proof, not those experiments, supports the unrestricted statement. An equivalent earlier classification in unindexed material remains possible; no claim of independent external audit is made.

## References
1. S. S. Adams, Z. Brass, C. Stokes, D. S. Troxell, *Irreversible k-threshold and majority conversion processes on complete multipartite graphs and graph products*, first public preprint February 25, 2011, https://arxiv.org/abs/1102.5361 (used for graph-family context, not as a reversible-cycle theorem).
2. D. Kaaser, F. Mallmann-Trenn, E. Natale, *On the Voting Time of the Deterministic Majority Process*, first public preprint August 14, 2015, https://arxiv.org/abs/1508.03519 (symmetric update rule, Turán graphs and timing bounds).
3. E. Goles, J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 (general two-period theorem).
4. J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), https://doi.org/10.1155/2020/9708347 (different Boolean maxterm/minterm rules).
