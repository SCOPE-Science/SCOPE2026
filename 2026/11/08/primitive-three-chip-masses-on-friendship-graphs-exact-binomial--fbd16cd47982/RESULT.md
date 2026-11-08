# Primitive-three chip masses on friendship graphs: exact binomial bands and a two-uniform limit

## Finding

For every integer \(k\ge2\), let \(F_k\) be the *friendship graph* formed from \(k\) edge-disjoint triangles by identifying one vertex from each into a common hub. The triangles have separately labelled peripheral pairs. In the synchronous parallel chip-firing system, a vertex holding at least its degree in nonnegative integer chips simultaneously sends one chip along every incident edge; otherwise it sends none. Write \(U\) for the deterministic update and \(|\sigma|\) for the conserved total of chips.

Define the *immediate primitive-three mass polynomial*
\[
H_k(z)=\sum_{\substack{\sigma\in\mathbb Z_{\ge0}^{V(F_k)}\\U^3\sigma=\sigma,\;U\sigma\ne\sigma}}z^{|\sigma|}.
\]
For \(0\le j\le k-1\), put
\[
c_{k,j}=3\sum_{a=0}^{j}\binom{k}{a}2^{k-a}.
\]
Then exactly
\[
\boxed{H_k(z)=\sum_{j=0}^{k-1}c_{k,j}\bigl(z^{3k+j}+z^{7k-1-j}\bigr).}
\]
In particular, the supported masses are precisely the disjoint intervals of integers \([3k,4k-1]\) and \([6k,7k-1]\). Both inner endpoints \(4k-1\) and \(6k\) have exactly \(3(3^k-1)\) immediate primitive-three states; there are \(12k\cdot3^{k-1}\) such labelled states in total and \(4k\cdot3^{k-1}\) distinct three-state orbits.

For an immediate primitive-three state selected uniformly among these \(12k\cdot3^{k-1}\) states, its normalized chip total converges weakly as \(k\to\infty\) to the equal-weight mixture of the continuous uniform laws on \([10/3,4]\) and \([6,20/3]\). This is a statement about already recurrent states, not eventual basins or all possible temporal periods.

## Assumptions and scope

The graph is finite, simple, connected and labelled: its vertices are \(h,a_1,b_1,\dots,a_k,b_k\), and its edges are \(ha_i,hb_i,a_ib_i\), for \(1\le i\le k\). Hence \(|V|=2k+1\), \(|E|=3k\), \(\deg(h)=2k\), and \(\deg(a_i)=\deg(b_i)=2\). Each state assigns a nonnegative integer to each vertex. At each discrete time the firing decisions are made from the old state simultaneously, and a firing vertex sends exactly one chip to each neighbor. Period-three means the least period of the state starting at time zero is three. No assumption is made about nonperiodic initial states; they are excluded from the enumerator.

## Proof

**Equal firing count.** Suppose \(U^3\sigma=\sigma\). Let \(n_v\) be the number of times vertex \(v\) fires in these three rounds. Net chip change at every vertex is \(\sum_{w\sim v}n_w-\deg(v)n_v=0\). The kernel of the graph Laplacian of a finite connected graph consists of constants, so all \(n_v\) are equal. If that common number is zero or three, every vertex always waits or always fires, and \(U\sigma=\sigma\). Consequently, in a primitive-three orbit each vertex fires either once or twice per three rounds.

**One-firing case.** Fix the hub's firing word to be \((1,0,0)\) at times \(0,1,2\). The other two choices of hub firing phase will multiply the count by three. For any peripheral pair \((a_i,b_i)\), enumerate the three cyclic shifts of \((1,0,0)\) for each vertex. Applying the degree-two firing inequalities at all three times, together with the chip increments, gives precisely the following feasible choices (time indices are the firing times):

| Firing times of \((a_i,b_i)\) | Initial chips \((\sigma(a_i),\sigma(b_i))\) | Peripheral firings at times \(0,1,2\) |
| --- | --- | --- |
| \((1,1)\) | \((1,1)\) | \((0,2,0)\) |
| \((1,2)\) | \((1,0)\) | \((0,1,1)\) |
| \((2,1)\) | \((0,1)\) | \((0,1,1)\) |

All six other ordered pairs of firing times have an empty feasible interval for at least one peripheral chip count. The claim can be checked directly: if a vertex has degree \(d\), prescribed firing word \(f_0,f_1,f_2\), and prescribed incoming counts \(g_0,g_1,g_2\), then its time-\(t\) chip count is \(x+\sum_{s<t}(g_s-df_s)\); require this to lie in \([d,\infty)\) when \(f_t=1\), and in \([0,d-1]\) otherwise. The table records the unique feasible peripheral initial count in each case.

Let \(a\) be the number of triangles of the first type, whose two peripheral vertices fire together at time one. The remaining \(k-a\) triangles each have two orientations. At time zero no peripheral vertex fires; at time one exactly \(k+a\) peripheral vertices fire; at time two exactly \(k-a\) fire. If the hub initially has \(x\) chips, its next two counts are \(x-2k\) and \(x-k+a\). The hub fires at time zero and waits at times one and two exactly when
\[
2k\le x\le 3k-a-1.
\]
Thus \(a\le k-1\), and writing \(x=2k+r\), there are \(k-a\) integer choices \(0\le r\le k-a-1\). The total chips at time zero are
\[
|\sigma|=(2k+r)+(2a+(k-a))=3k+a+r.
\]
Because every vertex has fired exactly once during the prescribed three rounds, its net chip change over these rounds is zero. Therefore every feasible schedule above returns to its starting state, and the nonconstant hub word ensures that its least period is three. For each \(a\), there are \(\binom{k}{a}2^{k-a}\) peripheral assignments. Counting the three hub firing phases, the one-firing generating polynomial is
\[
L_k(z)=3\sum_{a=0}^{k-1}\binom{k}{a}2^{k-a}\sum_{r=0}^{k-a-1}z^{3k+a+r}.
\]
For fixed \(j=a+r\), the allowed integers satisfy \(0\le a\le j\), hence \([z^{3k+j}]L_k=c_{k,j}\), for every \(0\le j\le k-1\); no other monomials occur.

**Two-firing case.** Every degree-\(d\) vertex in these period-three configurations has between zero and \(2d-1\) chips at every time. This follows from the explicit one-firing classifications above, and the same firing/waiting boundedness applies to any period-three state. Define chip complementation by \(C(\sigma)(v)=2\deg(v)-1-\sigma(v)\). To justify this bound for any primitive-three state, each vertex waits in at least one round, so its chip count is then below its degree; the next count is at most \(2\deg(v)-1\), and this upper bound is preserved by subsequent updates. The threshold rule shows directly that \(U(C(\sigma))=C(U\sigma)\) on the bounded state region: a vertex fires for \(C(\sigma)\) exactly when it waits for \(\sigma\), and the chip increments are opposite. Thus complementation is a bijection from one-firing primitive-three states to two-firing primitive-three states. Because the graph has \(3k\) edges and \(2k+1\) vertices, complementation maps chip total \(m\) to
\[
\sum_v(2\deg(v)-1)-m=(12k-2k-1)-m=10k-1-m.
\]
Hence \(H_k(z)=L_k(z)+z^{10k-1}L_k(z^{-1})\), giving the stated formula and support. Each coefficient is strictly positive. The two inner endpoints have coefficient \(3\sum_{a=0}^{k-1}\binom{k}{a}2^{k-a}=3(3^k-1)\). Summing the one-firing coefficients gives
\[
3\sum_{a=0}^{k-1}\binom{k}{a}2^{k-a}(k-a)=6k\cdot3^{k-1},
\]
using the binomial theorem's first derivative. Doubling produces \(12k\cdot3^{k-1}\) states, divisible by three because each primitive orbit has three distinct states.

**Limiting chip-mass law.** Conditional on a one-firing state, write \(A\) for the number of first-type triangles and \(B=k-A\). The counting weights show that \(B\) has exactly the size-biased binomial law associated with \(\mathrm{Bin}(k,2/3)\); equivalently \(B\overset{d}{=}1+\mathrm{Bin}(k-1,2/3)\). Given \(B\), the hub excess \(R\) is uniform on \(\{0,1,\dots,B-1\}\). Therefore \(A/k\to 1/3\) and \(R/k\Rightarrow(2/3)U\) with \(U\) uniform on \([0,1]\), and the one-firing mass \(3k+A+R\), divided by \(k\), tends to a uniform law on \([10/3,4]\). By the complementary mass identity, the twice-firing law tends to uniform \([6,20/3]\). The two sectors have the same number of states, proving the asserted equal-weight mixture.

## Verification

The accompanying scripts use two independent finite checks. `verify_exhaustive.py` directly updates every state with vertex chips in \([0,2\deg(v)-1]\) for \(k=1,2,3,4\), testing \(U^3\sigma=\sigma\ne U\sigma\) and its chip mass. This checks 1,099,840 configurations in total and yields period-three totals 12, 72, 324, 1296. Every primitive-three state must be inside this bounded domain because each vertex both fires and waits in a primitive-three orbit. `verify_patterns.py` independently enumerates all period-three firing-word choices, reconstructs their feasible chip-count intervals and computes the exact mass polynomial for \(1\le k\le12\). Both checkers agree with the formula. These computations are finite checks; the proof above establishes the theorem for all \(k\ge2\).

To reproduce: run `python verify_exhaustive.py` and `python verify_patterns.py` using Python 3 without third-party packages. The expected outputs are provided as `exhaustive_output.txt` and `patterns_output.txt`.

## Relationship to prior work

Bitar and Goles (1992) established the synchronous parallel chip-firing model and classified tree periods. Jiang (2010) analyzed complete bipartite/multipartite graph periods and the bounded/complemented-state framework. Jiang, Scully and Zhang (arXiv first public 2012) proved restrictions on periodic firing patterns and described motorized extensions. Ji, Li and Wang (2024) proved for *every* graph that primitive periods three and four are forbidden at masses strictly between \(2|E|-|V|\) and \(2|E|\). The friendship graph has \(2|E|-|V|=4k-1\) and \(2|E|=6k\). The formula above establishes exact positive populations at **both** sharp endpoints, and provides all period-three masses, counts and a nondegenerate large-graph mass limit. These detailed populations are not implied by the general forbidden interval itself.

Related exact primitive-three mass formulas for complete graphs and complete bipartite graphs concern different adjacency structures; the friendship graph is neither when \(k\ge2\). In the present graph, multiple triangles meet at a single vertex, requiring a separate hub-threshold count for every mixture of synchronized and split triangle firing phases.

## Limitations

Only initial states already of least temporal period three are enumerated. All other periods, incoming transient basins and arbitrary chip configurations are outside scope. The asymptotic law is weak convergence for a uniformly sampled primitive-three state, not a statement about random initial states of fixed chip density. The general firing-pattern framework is known; the asserted contribution is the exact friendship-graph mass enumerator, its simultaneous sharpness at both universal period-three density bounds and its limiting law. No historical-priority or independent-certification claim is made. The complete 1992 Bitar–Goles paper was not available through open sources; its abstract was inspected, and no full text could be obtained through lawful-access sources, leaving a residual literature-coverage risk.

## References

1. J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science **92** (1992), 291–300. DOI: `10.1016/0304-3975(92)90316-8`; public journal metadata: https://pure.uai.cl/en/publications/parallel-chip-firing-games-on-graphs/ (dated 1992-01-20).
2. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, first arXiv version 2010-03-04, arXiv:1003.0943. https://ar5iv.labs.arxiv.org/html/1003.0943
3. T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (first submitted 2012-11-29); SIAM J. Discrete Math. **29** (2015), 615–630. https://arxiv.org/pdf/1211.6786
4. D. Ji, M. Li and D. Wang, *Non-Stabilizing Parallel Chip-Firing Games*, first arXiv version 2024-08-20, arXiv:2408.10508. https://arxiv.org/pdf/2408.10508
