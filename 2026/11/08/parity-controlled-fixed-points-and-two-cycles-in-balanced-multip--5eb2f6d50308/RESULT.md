# Parity-controlled fixed points and two-cycles in balanced multipartite majority dynamics

## Finding
For each integer \(r\ge4\) and each integer \(n\ge1\), take the labelled complete balanced multipartite graph \(G_{r,n}=K_{n,\ldots,n}\), with \(r\) independent parts of size \(n\). Apply synchronous binary strict open-neighbor majority, retaining the current bit on a tie. Let \(F_{r,n}\) and \(P_{r,n}\) be the numbers of labelled fixed and *initially primitive-two* configurations, respectively. These are initial configurations, not transient states which reach a two-cycle later.

If \(n\) is even, write \(B_n=\binom{n}{n/2}\). The exact formulas are
\[
F_{r,n}=2+\mathbf1_{2\mid n}B_n^r,
\]
\[
P_{r,n}=H_{r,n}+\mathbf1_{2\mid n}\sum_{\substack{2\le t\le r-2\\2\mid t}}\binom rt\binom t{t/2}B_n^{r-t},
\]
where \(H_{r,n}=\binom r{r/2}\) for even \(r\) and \(H_{r,n}=r\binom{r-1}{(r-1)/2}(2^n-2)\) for odd \(r\). When \(n\) is odd, all terms containing \(B_n\) are omitted. The sum is zero if its index set is empty. In all cases the number of distinct two-orbits is \(P_{r,n}/2\).

For even \(r\), period two exists at every \(n\ge1\). For odd \(r\ge5\), it exists precisely at \(n\ge2\). At even \(n\), the leading families contain **two reversing homogeneous parts** and \(r-2\) fixed balanced mixed parts:
\[
P_{r,n}\sim r(r-1)\binom{n}{n/2}^{r-2},\qquad
F_{r,n}\sim\binom{n}{n/2}^{r}
\]
for each fixed \(r\ge4\). At odd \(n\), \(P_{r,n}=\binom r{r/2}\) for even \(r\) and \(P_{r,n}\sim r\binom{r-1}{(r-1)/2}2^n\) for odd \(r\). This gives a sharp parity-dependent change from exponentially many mixed-part oscillations to either constant or singly mixed populations.

A few exact values, written as \((F_{r,n},P_{r,n})\):

| Parts \(r\) | Part size \(n\) | Fixed | Primitive-two configurations |
| ---: | ---: | ---: | ---: |
| 4 | 1 | 2 | 6 |
| 4 | 2 | 18 | 54 |
| 4 | 3 | 2 | 6 |
| 4 | 4 | 1298 | 438 |
| 5 | 1 | 2 | 0 |
| 5 | 2 | 34 | 220 |
| 5 | 3 | 2 | 180 |
| 5 | 4 | 7778 | 4740 |
| 6 | 2 | 66 | 860 |
| 6 | 4 | 46658 | 42140 |

## Assumptions and scope
A labelled part means its vertices are distinguished: each binary assignment contributes separately. The graph is simple, undirected, and has no edges within a part and all edges between distinct parts. A vertex has degree \((r-1)n\). The majority threshold is *strict* with tie retention, not random tie breaking and not majority including self as an extra vote except insofar as that reproduces tie retention. The map is denoted \(M\). A primitive-two configuration \(x\) obeys \(M^2x=x\ne Mx\), while a fixed configuration obeys \(Mx=x\). The theorem covers all integer \(r\ge4\), \(n\ge1\), including both parities and all finite sizes. No claim is made here for arbitrary unequal part sizes or transient entrance-time distributions.

## Proof
**1. Update of an entire part.** Let \(a_i\in\{0,\ldots,n\}\) be the number of ones in part \(i\), and put \(S=\sum_i a_i\) and \(T=(r-1)n/2\). Every vertex of part \(i\) has exactly \(S-a_i\) neighbors in state one. Consequently the whole part becomes all one when \(S-a_i>T\), becomes all zero when \(S-a_i<T\), and is unchanged when \(S-a_i=T\). In particular **a homogeneous part stays homogeneous after every subsequent update**. A mixed (nonconstant) part either remains identical at a tie or becomes homogeneous permanently.

**2. Fixed configurations.** A configuration with at least one mixed part can be fixed only if each mixed part has a tie, giving \(S-a_i=T\). If a uniform zero part were also present, it would see \(S=T+a_i>T\) ones (as \(0<a_i<n\)), and would flip. If a uniform one part were present, it would see \(S-n=T+a_i-n<T\) ones and would flip. Hence all parts must be mixed. Since their ties imply equal occupancies \(a_i=a\), the identity \((r-1)a=(r-1)n/2\) forces \(a=n/2\). Thus the mixed fixed states exist exactly for even \(n\), with \(B_n^r\) choices. If all parts are homogeneous, let \(q\) of the \(r\) parts be one. For a one-part to remain one requires \((q-1)n\ge T\), whereas a zero-part to remain zero requires \(qn\le T\). If both types are present, these inequalities are incompatible. Exactly two homogeneous fixed states remain, unanimity zero and unanimity one. This gives \(F_{r,n}\).

**3. Primitive-two classification with mixed parts.** Suppose \(M^2x=x\) and \(x\) has exactly \(s\ge1\) mixed parts and \(t=r-s\) uniform parts. Every mixed part must remain identical in each update, or it would become homogeneous forever and could not return at time two. It therefore has a tie at both phases. Write \(a_i\) for its one-count, and let \(q\) of the \(t\) uniform parts initially be one. For a tied mixed part \(i\), \(S=T+a_i\). Every uniform zero part sees \(S>T\) and flips to all one. Every uniform one part sees \(S-n<T\) and flips to all zero. Thus **all uniform parts reverse at each step**. If \(t=0\), the configuration is fixed by Step 2 rather than period two. Otherwise \(t\ge1\), and the second-phase tie condition subtracts from the first-phase one-count the amount \((2q-t)n\). Since the mixed counts remain fixed, it requires \(q=t-q\), hence \(t\) is even and \(q=t/2\). In particular \(t\ge2\).

If \(s\ge2\), the ties for any two mixed parts imply their one-counts are equal, say \(a\). Using \(q=t/2\), the tie identity becomes \((s-1)a+(t/2)n=((s+t-1)/2)n\). Since \(s-1>0\), \(a=n/2\). This requires even \(n\), and gives \(B_n^s\) independent choices of balanced bit patterns in the mixed parts, \(\binom rt\) choices of the positions of the uniform parts, and \(\binom t{t/2}\) choices of which uniform parts initially hold one. Conversely each such configuration indeed ties at every mixed part and flips every uniform part at every step, hence has least period two.

If \(s=1\), the equation reduces to \(q=t/2\) without constraining the count in the single mixed part. Now \(r=t+1\) must be odd, and every nonconstant assignment in the mixed part is permitted: \(2^n-2\) choices. Choosing its position and the initial homogeneous phases yields \(r\binom{r-1}{(r-1)/2}(2^n-2)\) labelled period-two states. Conversely each is a genuine two-cycle.

**4. Primitive-two configurations with no mixed part.** For an all-homogeneous state with \(q\) one-parts, the zero parts see \(qn\) ones and the one parts see \((q-1)n\). When \(q<r/2\), the map sends all ones to zero and keeps zeros zero; when \(q>r/2\), it sends all zeros to one and keeps ones one, apart from the relevant boundary ties, which also do not create reversals. The only nontrivial two-cycle consists of \(q=r/2\) for even \(r\), when both types reverse. It has \(\binom r{r/2}\) labelled initial states. For odd \(r\), the tie cases cannot reverse both classes, so there are no all-homogeneous period-two configurations. These observations also directly cover the cases with one of the two homogeneous types absent.

Summing the disjoint cases \(s=0\), \(s=1\), and \(s\ge2\) proves the formula. Every term counts all labelled configurations, including both temporal phases, so dividing by two counts orbits.

**5. Existence and asymptotics.** For even \(r\), the all-homogeneous half-one case always exists. For odd \(r\), the \(s=1\) class exists exactly for \(n\ge2\); all other terms vanish at \(n=1\). With fixed \(r\ge4\) and even \(n\), Stirling's formula gives \(B_n\sim2^n\sqrt{2/(\pi n)}\). The \(t=2\) term equals \(\binom r2\binom21 B_n^{r-2}=r(r-1)B_n^{r-2}\). Every larger even \(t\) contributes \(O(B_n^{r-4})\); the all-homogeneous even-\(r\) contribution is constant; the odd-\(r\) one-mixed contribution is \(O(2^n)\), negligible beside \(B_n^{r-2}\) since \(r-2\ge3\). The asserted even-\(n\) asymptotics follow. For odd \(n\) only the explicitly given \(H_{r,n}\) remains. This completes the proof for all stated parameters.

## Verification
Two standalone standard-library Python checkers accompany the result and require no external packages. `verify_balanced_multipartite_counts.py` enumerates all \((n+1)^r\) part-occupancy profiles and weights each profile by \(\prod_i\binom n{a_i}\), independently applying the part-count dynamics; it confirms the formulas for 19 parameter pairs with \(4\le r\le8\) and \(1\le n\le4\). `verify_balanced_multipartite_direct.py` constructs an explicit neighbor bitmask for every vertex and directly iterates all \(124400\) labelled states across 11 parameter pairs including \((r,n)=(4,4),(5,3),(6,2),(7,2)\). Its independent bit-level census agrees with the formulas exactly. Captured deterministic outputs are stored separately in the package. The general theorem follows from the proof, not from finite enumeration.

## Relationship to prior work
Goles and Olivos [1] establish eventual period at most two for finite symmetric threshold networks; this does not enumerate the *initial* fixed and primitive-two configurations. Benjamini, Chan, O'Donnell, Tamuz, and Tan [2] treat convergence and disagreement on infinite unimodular and random graphs and explicitly distinguish the finite period-two property; their results do not provide the present exact balanced multipartite census. Tosic and Agha [3] analyze threshold cellular automata chiefly over one-dimensional rings; their configuration-space framework does not furnish counts for arbitrary numbers of complete-multipartite parts.

The closest accessible related exact census considers strict majority on complete tripartite graphs: in its equal-size specialization the only two-cycle class has one nonconstant frozen part. The present theorem treats \(r\ge4\), including entirely new families with at least two independent balanced mixed parts; its even-part parity law and its asymptotics do not follow from a fixed three-part case. A published multipartite *parity automaton* result concerns a linear XOR update, not majority. A multipartite majority-coloring invariant concerns static colorings, not recurrence under a majority update. No stronger covering statement was identified in the literature and research-result searches performed, but historical priority beyond these comparisons is not certified.

## Limitations
The graph is balanced and complete multipartite, the bits are binary, and updates are simultaneous strict open-neighbor majority with retained ties. The counting result addresses initially recurrent configurations, not the basins or first entrance times of transient states. No claim is made for arbitrary unequal part sizes. Some historic literature is not available in full text: the complete 1980 three-page article [1] was inaccessible after open-access attempts, and an institutional copy could not be obtained. Its abstract proves the eventual-period restriction but not the present exact census; an unindexed equivalent enumeration remains a residual originality risk. No independent scientific audit has been performed.

## References
[1] E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189. DOI: `10.1016/0012-365X(80)90121-1`.

[2] I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1, publicly posted 2014-05-11. `https://arxiv.org/abs/1405.2486`.

[3] P. Tosic and G. Agha, “Characterizing Configuration Spaces of Simple Threshold Cellular Automata,” *Proceedings of ACRI* (2004), full manuscript: `https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf`.
