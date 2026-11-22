# A sharp three-update extinction clock and exact first-hitting census for two-contact excitation on quadrilateral books

## Finding

For every integer \(m\ge1\), let the labelled quadrilateral book \(B_m\) have two hub vertices \(u,v\) joined by an edge and \(m\) disjoint ordered page pairs \((a_i,b_i)\), with edges \(ua_i,a_ib_i,b_iv\) for \(1\le i\le m\). Thus \(B_m=K_{1,m}\square K_2\), with \(m\) four-cycles sharing one hub edge. Apply synchronous three-state Greenberg–Hastings excitation, using the open neighborhood and **contact threshold two**: a vertex in state \(1\) changes to \(2\), a vertex in state \(2\) changes to \(0\), and a vertex in state \(0\) changes to \(1\) exactly when at least two distinct neighbors are in state \(1\).

The global map satisfies \(F_m^3(x)=\mathbf0\) for **every** initial configuration \(x\in\{0,1,2\}^{2m+2}\). The three-update bound is sharp for every \(m\ge1\). In particular, the all-rest configuration is the unique recurrent configuration, and no two-contact oscillator exists on any of these books.

Define \(\tau(x)=\min\{t\ge0:F_m^t(x)=\mathbf0\}\), and let \(N_t(m)\) count labelled configurations with \(\tau=t\). Put
\[
S_m=9^m+7^m+2\cdot8^m+4\cdot6^m+6m\,6^{m-1}+(m+2)^2 4^{m-1}.
\]
Then the **complete** first-extinction-time distribution, for every integer \(m\ge1\), is
\[
\boxed{N_0(m)=1,\quad N_1(m)=4^{m+1}-1,\quad N_2(m)=S_m-4^{m+1},\quad N_3(m)=9^{m+1}-S_m,\quad N_t(m)=0\ (t\ge4).}
\]
In particular, for a uniformly sampled initial coloring, the extinction time converges in distribution to a two-point law:
\[
\lim_{m\to\infty}\Pr(\tau=2)=\frac19,\qquad
\lim_{m\to\infty}\Pr(\tau=3)=\frac89.
\]
This gives an exact threshold contrast on the same graph family: the published threshold-one classification has primitive periods three and four for suitable page counts and positive four-cycle populations for every page count, whereas threshold two produces no nonzero recurrent orbit at all.

## Assumptions and scope

The vertices and page pairs are labelled, all graph edges are exactly those specified, and the state alphabet is \(\{0,1,2\}\). Updates are simultaneous. The threshold is the absolute count of **two distinct excited neighbors**, with no self-loop and no randomization. Each \(N_t(m)\) counts initial labelled configurations without identifying graph automorphisms or time shifts. Only \(m\ge1\) is claimed. The stopping time is first arrival at the all-zero configuration, which is absorbing.

## Proof

**1. No new excitation at update two.** We prove that no vertex has state \(1\) at time \(2\), regardless of the initial state. If a hub, say \(u\), had become excited at time \(2\), it would be in state \(0\) at time \(1\) and would have at least two excited neighbors at time \(1\). But if any page vertex \(a_i\) is excited at time \(1\), its two neighbors \(u,b_i\) must both have been excited at time \(0\); in particular \(u\) was excited at time \(0\) and consequently is refractory at time \(1\). This contradicts the required resting state of \(u\). If no page vertex \(a_i\) is excited at time \(1\), the only other neighbor of \(u\) is \(v\), so there cannot be two excited neighbors. The argument for hub \(v\) is symmetric.

If a page vertex \(a_i\) became excited at time \(2\), then both its neighbors \(u,b_i\) would be excited at time \(1\) while \(a_i\) would be resting at time \(1\). Yet \(b_i\) being excited at time \(1\) implies that its other neighbor \(a_i\) was excited at time \(0\); therefore \(a_i\) is refractory at time \(1\), a contradiction. The same proof applies to \(b_i\). Hence no vertex is excited at time \(2\). All refractory states at time \(2\) vanish one update later, so \(F_m^3=\mathbf0\).

For sharpness, choose initially \(u=0\), \(v=1\), \(a_1=1\), and all other vertices \(0\). The hub \(u\) has two excited neighbors at time zero, hence is excited at time one, refractory at time two and resting only at time three. Thus \(\tau=3\) for every \(m\ge1\).

**2. Exact counting.** The sole initial all-zero configuration contributes \(N_0=1\). An initial configuration reaches rest at update one if and only if it contains no initially excited vertex: a state \(1\) becomes refractory, while an initial coloring over \(\{0,2\}\) produces no new excitation. Therefore exactly \(4^{m+1}\) configurations have \(\tau\le1\).

By the preceding lemma, all states at time two are \(0\) or \(2\). Thus \(F_m^2(x)=\mathbf0\) precisely when **no vertex becomes newly excited at update one**. We enumerate these initial colorings by the two initial hub states \(h=x(u),j=x(v)\). For a page \((a,b)\), discard \((a,b)\) whenever \(a=0,h=1,b=1\) or \(b=0,j=1,a=1\). The bivariate page polynomial
\[
P_{h,j}(X,Y)=\sum_{\substack{a,b\in\{0,1,2\}\\
\neg(a=0,h=1,b=1)\\
\neg(b=0,j=1,a=1)}}X^{\mathbf1_{a=1}}Y^{\mathbf1_{b=1}}
\]
encodes the numbers of initially excited page vertices on either side. If \(h=0\), the sum of the first-side excited page count and \(\mathbf1_{j=1}\) must not exceed one; if \(j=0\), the analogous second-side count plus \(\mathbf1_{h=1}\) must not exceed one. Nonresting hubs impose no additional constraints. The exact contributions from all nine hub assignments are:

| Initial hub pair | Number of initial configurations with no update-one excitation |
|---|---:|
| \((2,2)\) | \(9^m\) |
| \((1,1)\) | \(7^m\) |
| \((1,2),(2,1)\) | \(8^m\) each |
| \((0,1),(1,0)\) | \(6^m\) each |
| \((0,2),(2,0)\) | \(6^m+3m6^{m-1}\) each |
| \((0,0)\) | \((m+2)^2 4^{m-1}\) |

For instance, in the \((0,0)\) case every page contributes \((X+2)(Y+2)\), and each hub allows at most one excited page neighbor, giving \((2^m+m2^{m-1})^2\). In the \((0,2)\) case a page contributes \(3(2+X)\) after ignoring the unconstrained second coordinate, hence the allowed first-coordinate coefficients sum to \(6^m+3m6^{m-1}\). The remaining cases follow by the explicitly stated one-page exclusions. Summing all nine contributions yields \(S_m\), the exact number with \(\tau\le2\). Subtracting successive cumulative counts from the total \(3^{2m+2}=9^{m+1}\) proves every stated \(N_t\).

**3. Asymptotic law.** In \(S_m\), the unique term with largest exponential base is \(9^m\); all other terms are polynomial multiples of bases at most eight. Hence \(S_m/9^{m+1}\to1/9\), while \(4^{m+1}/9^{m+1}\to0\). The asserted limiting masses at times two and three follow. The sharp three-update witness and the nonnegativity of all counts also follow independently from the preceding construction.

## Verification

The standalone C++17 program `code/verify_direct.cpp` implements the graph edges and simultaneous state transition directly for each labelled configuration, without using the symbolic generating-polynomial construction. Compile from the package root with `g++ -std=c++17 -O3 code/verify_direct.cpp -o verify_direct` and run `./verify_direct`. It exhausts all \(5{,}380{,}830\) labelled initial configurations for page counts \(1\) through \(6\), verifies extinction by three updates, and checks each of the four first-arrival populations against the theorem. Its captured output is `evidence/direct_output.txt`.

A separate Python 3 standard-library checker `code/verify_symbolic.py` computes all nine hub-assignment contributions by explicit nine-state page enumeration and constrained bivariate coefficient convolution; it does not evaluate graph trajectories. Running `python3 code/verify_symbolic.py` verifies the closed form for \(m=1,\ldots,30\), with selected outputs in `evidence/symbolic_output.txt`. Finite checks are independent corroboration, not the all-parameter proof, which is the local causal and exact polynomial enumeration above.

## Relationship to prior work

Three-state Greenberg–Hastings dynamics and contact thresholds were developed in the classical excitable-cellular-automata literature, including Durrett and Griffeath (1993). Gravner, Lyu and Sivakoff's 2016 full text, especially its update definition and Theorem 3, treats **one-contact** excitation on arbitrary connected graphs, identifying synchronization through initial circulation; it does not address this two-contact rule. The published quadrilateral-book classification under the **one-contact** rule enumerates primitive three- and four-cycles and their attraction basins on exactly the same graph family. Its conclusions are not statements about threshold two and cannot supply the present three-step extinction-time distribution by specialization.

A published maximum-induced-density criterion already guarantees eventual extinction for three-state excitation at threshold \(q\) whenever every induced subgraph has fewer than \(q\) edges per vertex. It applies here for \(q=2\) because each induced subgraph of \(B_m\) is two-degenerate and has fewer than twice as many edges as vertices. Consequently, **eventual extinction alone is not claimed as novel**. The additional contribution is the size-independent sharp three-update cutoff, full first-hitting census, and its limiting two-point distribution, none of which follows from the cited general excitation-budget bound. Related exact threshold-two results on complete bipartite, tripartite, ladder, and sunlet graphs concern different edge and neighborhood structures and do not contain the displayed formulas by a graph-family inclusion or parameter substitution.

## Limitations

The result concerns only the specified quadrilateral-book topology and the synchronous three-state, absolute two-neighbor rule. It does not give a comparable clock for arbitrary two-degenerate graphs or for other numbers of colors. Published statements about period-one and period-four waves on other networks do not imply analogous behavior here. The computations verify finite page counts and are not substitutes for the all-size proof. The literature comparison is extensive but not a proof that no unindexed historical equivalent exists; an external independent mathematical audit has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, publicly submitted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, publicly submitted 2016-10-24, particularly Section 1 and Theorem 3. https://arxiv.org/html/1610.07320v1
3. *Exact three- and four-phase excitation on quadrilateral books*, published mathematical research record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-three-and-four-phase-excitation-on-quadrilateral-books--b7d28b39fb97
4. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics*, published mathematical research record, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91
