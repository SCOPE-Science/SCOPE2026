# Hard-core minority defects and exponential tie-sector entropy in ternary plurality on cycle complements

## Finding

Let \(n\ge5\). Let \(G_n=\overline{C_n}\) be the simple graph on the indexed cyclic vertex set \(\mathbb Z/n\mathbb Z\), with an edge between two vertices precisely when they are distinct and not consecutive on the deleted cycle. Each vertex carries one of three **labelled** opinions \(A,B,C\). At a simultaneous update, a vertex changes to the opinion with uniquely greatest count in its open neighborhood; if two or three opinions attain the maximum, it keeps its incumbent opinion, even if that opinion is not one of the maximizers.

For every integer \(r\ge1\) satisfying \(n-r\) even and \(n\ge3r+2\), put \(L=(n-r)/2\). The fixed configurations with global opinion-count multiset exactly \(\{L,L,r\}\) are **precisely** those obtained by choosing the uniquely smallest opinion's \(r\) sites at mutual cyclic distance at least three on the deleted cycle, then placing the other two opinions alternately on the remaining vertices in their cyclic order. Thus their exact number, with both vertex positions and opinion names labelled, is

\[
Q_{n,r}=\frac{6n}{r}\binom{n-2r-1}{r-1}.
\]

In particular, let \(B_n\) denote the number of all fixed configurations having exactly two equally frequent, strictly leading opinions and a nonempty third opinion. Define

\[
M(z)=\begin{pmatrix}0&1&0\\0&0&1\\z&0&1\end{pmatrix},\qquad H_n(z)=\operatorname{tr}(M(z)^n).
\]

Then for every \(n\ge5\),

\[
B_n=3\bigl(H_n(1)+(-1)^n H_n(-1)\bigr)
-6\mathbf1_{2\mid n}-18\mathbf1_{3\mid n}.
\]

The spectral radius \(\lambda=1.465571231876\ldots\) is the unique real root greater than one of \(\lambda^3-\lambda^2-1=0\). Consequently

\[
B_n=3\lambda^n+O(1.152^n),\qquad
\lim_{n\to\infty}\frac{\log B_n}{n}=\log\lambda.
\]

This is an exact classification of a *specified histogram sector*, not a claim about every fixed configuration or every orbit of the system.

## Assumptions and scope

The simple graph convention applies to \(n\ge5\); its open neighborhood of \(i\) consists of all vertices except \(i-1,i,i+1\). For a word \(x\in\{A,B,C\}^n\), let \(N_D\) denote the global count of opinion \(D\), and \(s_D(i)\) the number of occurrences of \(D\) in the deleted triple \((x_{i-1},x_i,x_{i+1})\). The current neighborhood count is \(N_D-s_D(i)\). A word is fixed exactly when, at every site, either the current opinion is the **unique** maximizing neighbor opinion or there is a tie for maximum. The total number of opinions is exactly three, labels are distinct, and there are no stochastic updates or self-loop neighbors.

Within the theorem's stratum, after permuting the opinion names, \(N_A=N_B=L\) and \(N_C=r<L\). The smallest-class condition is strict. The boundary \(n=3r\), when all three counts are equal, is excluded; so is the case of an absent third opinion. Counts outside this sector are not covered.

## Proof

**Step 1: separation and alternating neighbors at minority sites.** Fix the counts \(L,L,r\) with \(r<L\). A nonconstant fixed word cannot contain two adjacent \(C\) vertices. Indeed, at the boundary of any cyclic \(C\)-run, a \(C\) with a \(C\) neighbor and an \(A\) neighbor has neighbor-count vector \((L-1,L,r-2)\): opinion \(B\) is uniquely maximal, contradicting fixation of that \(C\). The case with \(B\) adjacent is symmetric. A cyclic pattern \(C A C\) is impossible: at its middle \(A\) the neighbor counts are \((L-1,L,r-2)\), so \(B\) is again uniquely maximal. The analogous \(C B C\) is impossible. Therefore the \(C\) sites have cyclic separation at least three.

An isolated \(C\) cannot have the same high-frequency opinion on both sides. If the deleted triple is \(A C A\), the neighbor-count vector is \((L-2,L,r-1)\), which has unique maximum \(B\). The symmetric \(B C B\) is also impossible. Thus the two closest high-frequency vertices across each \(C\) are oppositely colored.

**Step 2: alternation between minority sites.** Write \(\Delta=L-r\ge1\). No fixed word can contain \(A A A\), because its middle \(A\) sees \(B\) as the unique maximum. An adjacent \(A A\) pair cannot touch a \(C\): the \(A\) at a \(C A A\) triple sees \(B\) uniquely maximal; similarly for \(A A C\). If the deleted triple is \(B A A\), its center \(A\) sees \((L-2,L-1,r)\). For \(\Delta\ge2\), the \(B\) count is uniquely maximal and the configuration is not fixed. Exactly the same argument applies to \(B B\). Hence, for \(\Delta\ge2\), every pair of consecutive high-frequency vertices (also across a deleted \(C\)) must alternate.

It remains to treat \(\Delta=1\). By Step 1 the \(r\) gaps between successive \(C\) sites contain at least two high-frequency vertices each. Their total number is \(2L=2r+2\), so at most one such gap has four or more high vertices. Within a gap, an equal-colored pair can survive only with the four consecutive high-frequency symbols \(B A A B\) or \(A B B A\). In particular an equal-colored pair requires a gap of at least four high vertices. With only two spare high vertices beyond the minimum, there can be at most one equal-colored edge in the **cyclic high-frequency subsequence** obtained after deleting all \(C\) sites. The bridges across deleted \(C\) sites are unequal by Step 1. But a cyclic binary word of even length \(2L\) always has an even number of equal-colored adjacent pairs: its number of changes is even, and the total number of adjacent pairs is even. Thus one equal-colored pair is impossible. This proves alternation also when \(\Delta=1\).

**Step 3: sufficiency.** Conversely, choose any \(r\) sites separated by at least three deleted-cycle steps, place \(C\) there, and alternately color the \(n-r=2L\) remaining cyclic sites \(A,B\). At a \(C\) vertex, the deleted triple contains one of each color; its neighbor counts are \((L-1,L-1,r-1)\), so a tie between \(A\) and \(B\) preserves \(C\). At a high-frequency vertex (say \(A\)), the deleted triple is either \(B A B\) or one of \(B A C\), \(C A B\). In the first case its neighbor counts are \((L-1,L-2,r)\), so \(A\) is maximal or tied for maximal; in the remaining cases they are \((L-1,L-1,r-1)\), giving a tie. Hence no vertex changes.

**Step 4: exact counting.** For a fixed named minority opinion, choose its \(r\) cyclic positions at pairwise forward separation at least three. Mark one of these positions and list the \(r\) cyclic spacings. Writing each spacing as three plus a nonnegative integer gives \(\binom{n-2r-1}{r-1}\) ordered spacing lists. There are \(n\) choices of the marked site; each unmarked set was counted \(r\) times. Hence there are \(\frac{n}{r}\binom{n-2r-1}{r-1}\) site sets. The remaining \(2L\) vertices admit precisely two alternating \(A,B\) assignments, and there are three choices of the named minority opinion. Their product proves the formula for \(Q_{n,r}\).

**Step 5: transfer expression.** The three-state weighted matrix \(M(z)\) records distances from the last selected minority site: newly selected, one intervening unselected site, and at least two unselected sites. A new selection is possible only from the third state, with weight \(z\). Consequently \(H_n(z)\), for \(n\ge3\), is the cyclic spacing-at-least-three independence polynomial, including the empty set. The coefficient of \(z^r\) for \(r\ge1\) is the spacing count from Step 4. Alternation of the remaining two opinions requires \(n-r\) even, equivalently \(r\equiv n\pmod2\). Parity extraction uses \(\frac12(H_n(1)+(-1)^nH_n(-1))\). The empty set contributes only for even \(n\), and must be subtracted. At exactly \(n=3r\), the largest possible packing consists of precisely three equally spaced site sets; these have no strictly smaller opinion class and must also be subtracted. Multiplying the remaining sum by six proves the stated \(B_n\) expression, including both correction terms.

**Step 6: exponential rate.** The characteristic polynomial of \(M(z)\) is \(t^3-t^2-z\). For \(z=1\), the simple Perron root is \(\lambda\), and the other two roots have modulus approximately \(0.82604\). For \(z=-1\), every root has modulus at most \(1.150964\). Therefore \(H_n(1)=\lambda^n+O(0.827^n)\) and \(H_n(-1)=O(1.151^n)\). The bounded correction terms are absorbed into \(O(1.152^n)\), giving \(B_n=3\lambda^n+O(1.152^n)\). Since this is positive for all sufficiently large \(n\), the asserted entropy limit follows.

## Verification

The standalone C++ program `check_equilibria.cpp` enumerates every ternary colouring in the stated two-tied-leaders histogram sector for every \(5\le n\le16\), evaluates open-neighbor plurality directly, and compares the fixed-point predicate against the separation-and-alternation characterization. It additionally verifies the exact \(Q_{n,r}\) formula for every admissible \((n,r)\) in that range. The script `check_transfer.py` verifies, by exact integer matrix multiplication and independent cyclic-spacing binomial formulas, all transfer and parity identities for \(5\le n\le90\). Their respective captured outputs are `check_equilibria.out` and `check_transfer.out`. These calculations independently test the formulas over finite ranges; the six proof steps above establish the infinite claims.

## Relationship to prior work

Mossel, Neeman and Tamuz (2012) study majority/plurality information aggregation, including plurality on expanders, but avoid ties through perturbations of edge weights when extending their statements to multiple alternatives. The present rule deliberately **retains an incumbent on every leading tie**, including a nonleading incumbent, and counts fixed colourings in a specific dense deterministic graph family. Becchetti and collaborators (first posted 2013) study random three-neighbor sample consensus on complete graphs, not this full-open-neighborhood deterministic equilibrium census. A separately published binary-majority classification on cycle complements establishes an odd-order \(2n+2\) fixed-state count and a long even-order transient witness; its binary-state restriction cannot contain the strictly positive third-color population classified here. The appearance of distance-three hard-core placements and their exact cubic transfer polynomial is not implied by these prior statements.

## Limitations

Only the sector with exactly two tied leading populations and one strictly smaller positive population is classified. This result does not enumerate all ternary equilibria, determine basins of attraction, establish global convergence, or classify nontrivial periodic orbits. The asymptotic concerns the size of this specified fixed-point subset, not the total fixed-state population. Novelty searches and the available primary text do not exclude unindexed equivalences; no external historical-priority guarantee or independent validation is claimed.

## References

1. E. Mossel, J. Neeman, O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893v1, publicly posted July 4, 2012, https://arxiv.org/abs/1207.0893.
2. L. Becchetti, A. Clementi, E. Natale, F. Pasquale, R. Silvestri, L. Trevisan, *Simple Dynamics for Plurality Consensus*, arXiv:1310.2858v1, publicly posted October 10, 2013, https://arxiv.org/abs/1310.2858.
3. *Parity and long transients in majority dynamics on cycle complements*, published mathematical finding, November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-and-long-transients-in-majority-dynamics-on-cycle-complem--c1a31cd30a7a.
