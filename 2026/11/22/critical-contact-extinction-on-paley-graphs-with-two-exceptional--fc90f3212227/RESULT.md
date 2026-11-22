# Critical-contact extinction on Paley graphs, with two exceptional wave orders

## Finding

Let \(q\ge5\) be a prime power with \(q\equiv1\pmod4\). On the undirected Paley graph \(P(q)\), with vertex set \(\mathbb F_q\) and adjacency between distinct vertices whose difference is a square, run the synchronous three-state Greenberg–Hastings map \(F_q\). At each update, \(1\to2\to0\) unconditionally; a vertex in state \(0\) enters state \(1\) precisely when at least \(\theta=(q-1)/4\) neighbors are in state \(1\). The graph has degree \(2\theta\).

**Complete all-order periodic classification.** For every \(q\ge13\), all \(3^q\) initial configurations eventually reach the all-rest fixed configuration. At \(q=5\), the recurrent configurations consist of the all-rest state and exactly two primitive five-cycles, ten nonzero periodic configurations in total. At \(q=9\), they consist of the all-rest state and exactly four primitive three-cycles, twelve nonzero periodic configurations in total. In particular, \(q=5,9\) are the **only** admissible Paley orders permitting sustained excitation at the exact half-degree contact threshold.

**Exact small-order basin and relaxation classification.** In \(P(5)\) the rest basin has \(153\) configurations and each five-cycle basin has \(45\), among \(3^5=243\). The first-periodic-entry cutoff is four updates and is attained. In \(P(9)\), all twelve nonzero periodic configurations have no transient predecessors, so their four cycle basins have size three each; the other \(19671\) of \(3^9=19683\) configurations become completely resting. Its first-periodic-entry cutoff is five updates and is attained. The separate period-resolved entry census is:

| First periodic entry \(t\) | \(P(5)\), eventual rest | \(P(5)\), period five | \(P(9)\), eventual rest | \(P(9)\), period three |
|---:|---:|---:|---:|---:|
| 0 | 1 | 10 | 1 | 12 |
| 1 | 31 | 30 | 511 | 0 |
| 2 | 51 | 40 | 5641 | 0 |
| 3 | 40 | 10 | 9990 | 0 |
| 4 | 30 | 0 | 3438 | 0 |
| 5 | 0 | 0 | 90 | 0 |
| **Total** | **153** | **90** | **19671** | **12** |

## Assumptions and scope

Every graph is finite, connected, simple, undirected and labelled. The contact neighborhood excludes the vertex itself. Colors \(0,1,2\) mean resting, excited and refractory, respectively. A *primitive \(s\)-cycle* means an orbit of least temporal period \(s\), rather than \(s\) labelled states counted as separate cycles. Basin size counts all labelled initial configurations whose orbit eventually reaches the given temporal cycle. First-periodic-entry time is the least nonnegative update count at which the state is already recurrent. The all-rest state is the unique fixed state. The source date used for the archived dynamical model is the publicly dated March 1993 preprint, not a later journal issue.

## Proof

**1. The contact-budget identity on a connected \(2\theta\)-regular graph.** Consider an arbitrary nonzero periodic trajectory of period \(T\) on a connected, finite, simple, \(2\theta\)-regular graph. Let \(u_t(v)\in\{0,1\}\) indicate that vertex \(v\) is excited at time \(t\), with time indices modulo \(T\), and write \(m_v=\sum_{t\bmod T}u_t(v)\). Any vertex fires only at times separated by at least three updates. For an edge \(vw\), count the ordered predecessor-to-new-excitation contacts across this edge in both spatial directions and all times; call the count \(c_{vw}\). Each firing of \(v\) can contribute to at most one such contact on edge \(vw\), since \(w\) cannot fire at both \(t-1\) and \(t+1\); similarly each firing of \(w\) contributes at most once. Therefore

\[
 c_{vw}\le\min(m_v,m_w)\le\frac{m_v+m_w}{2}.
\]

Every firing at time \(t+1\) requires at least \(\theta\) contacts from time \(t\), so summing over the periodic trajectory and the edges gives

\[
 \theta\sum_v m_v\le\sum_{vw\in E}c_{vw}
 \le\frac12\sum_{vw\in E}(m_v+m_w)
 =\theta\sum_v m_v.
\]

All inequalities must be equalities. Thus \(m_v=m_w\) on every edge; connectivity makes the firing counts identical. Since the orbit is nonzero, every vertex fires. Every actual new excitation has *exactly* \(\theta\) predecessor contacts, and for every edge every firing at either endpoint is paired with **exactly one** firing at the other endpoint one step earlier or later. The matching property implies that a vertex has excited neighbors at time \(t\) only if it itself fires at \(t-1\) or \(t+1\). If it fires at \(t+1\), exactly \(\theta\) neighbors fired at \(t\); if it fires at \(t-1\), precisely \(2\theta-\theta=\theta\) neighbors fire at \(t\). These cases are mutually exclusive. Therefore the adjacency matrix \(A\) satisfies the **exact vector identity**

\[
 \boxed{Au_t=\theta(u_{t-1}+u_{t+1})}\quad(t\bmod T).
\]

No statistical or limiting approximation is used.

**2. Temporal Fourier obstruction.** For a temporal \(T\)-th root of unity \(\zeta\), let \(\widehat u(\zeta)=\sum_{t=0}^{T-1}u_t\zeta^{-t}\). Fourier transforming the identity gives

\[
 A\widehat u(\zeta)=\theta(\zeta+\zeta^{-1})\widehat u(\zeta).
\]

If \(\widehat u(\zeta)\ne0\), then \(\theta(\zeta+\zeta^{-1})\) is an adjacency eigenvalue. For \(\zeta\ne1\) it cannot equal the top eigenvalue \(2\theta\), and \(\zeta+\zeta^{-1}\) is necessarily an algebraic integer. If neither nonprincipal adjacency eigenvalue divided by \(\theta\) is an algebraic integer, every nonconstant Fourier coefficient vanishes. The excited indicators are then constant in time. They must be identically zero because consecutive firing is impossible; the purported nonzero recurrent orbit cannot exist. Finiteness of the state space now forces every initial state eventually to reach all-rest.

**3. Arithmetic of the Paley spectrum.** The Paley graph has strongly regular parameters

\[
 \left(q,\frac{q-1}{2},\frac{q-5}{4},\frac{q-1}{4}\right)
 = (4\theta+1,2\theta,\theta-1,\theta).
\]

Its adjacency spectrum consists of the simple eigenvalue \(2\theta\) and the two nonprincipal eigenvalues

\[
 \mu_\pm=\frac{-1\pm\sqrt q}{2},\qquad
 \mu_+\mu_-=-\theta,\qquad \mu_++\mu_-=-1.
\]

If \(q\) is not a perfect square and \(q\ge13\), then \(\theta\ge3\). The two numbers \(\mu_\pm/\theta\) are algebraic conjugates of degree two with trace \(-1/\theta\notin\mathbb Z\). Algebraic integers have integral trace, so neither is an algebraic integer. If \(q=s^2\ge25\), with \(s\) odd, then

\[
 \frac{\mu_+}{\theta}=\frac{2}{s+1},\qquad
 \frac{\mu_-}{\theta}=-\frac{2}{s-1}.
\]

Both are nonintegral rational numbers, hence neither is an algebraic integer. The Fourier obstruction proves global extinction for *every* admissible \(q\ge13\), including square orders, with no assumption that the finite field is prime.

**4. The two exceptional recurrent spectra.** For \(q=9\), \(\theta=2\) and the eigenvalues are \(4,1,-2\). The only possible nonzero temporal Fourier frequencies are the primitive cube roots, because \(-2/\theta=-1=\zeta+\zeta^{-1}\), while \(1/\theta=1/2\) is not an algebraic integer. Hence every nonzero recurrent state is exactly three-periodic. Since every vertex fires and cannot fire more than once in three steps, its excitation phase gives a proper three-coloring of the graph, and the contact-budget identity enforces exactly two neighbors of each other color. The field \(\mathbb F_9=\mathbb F_3[a]/(a^2+1)\) has nonzero square directions \(\{(\pm1,0),(0,\pm1)\}\); thus \(P(9)\) is exactly the \(3\times3\) rook graph. Proper three-colorings of that graph are precisely Latin squares of order three: six choices for the first row, two for the second, and the third forced. There are twelve states and four temporal three-cycles. All are legitimate threshold-two rotations because every vertex has two predecessors and two successors. Their predecessor in the *whole* state space is unique: any vertex whose target phase is zero must previously be refractory, not resting, because the two excited neighbors in the predecessor's preceding phase would otherwise trigger excitation. The other two target phases have forced predecessors. Therefore these twelve states have no transient in-neighbors or basin extensions.

For \(q=5\), \(P(5)=C_5\) and \(\theta=1\). The nonprincipal eigenvalues divided by \(\theta\) are \(2\cos(2\pi/5)\) and \(2\cos(4\pi/5)\), so every recurrent trajectory has period dividing five. Each vertex fires exactly once per five updates by the contact budget and refractory separation. Along each edge of the five-cycle the two firing phases differ by \(\pm1\pmod5\). The five signed edge differences sum to zero modulo five, so they must all be \(+1\) or all be \(-1\). This gives exactly two orientations, each with five temporal translations: two primitive five-cycles and no other nontrivial recurrent periods.

**5. Finite basin and sharp-entry certificates.** The two independently implemented complete enumerators, `verify_forward.py` and `verify_independent.py`, replay the literal update on all \(243\) and \(19683\) configurations for the five- and nine-vertex graphs. The first forms the entire base-three functional graph and follows unresolved paths backward; the second uses direct tuple trajectory tracing with a separately built edge set. The two agree on the complete first-entry/period table above and on each temporal-cycle basin. For \(q=9\) the independent program also constructs all twelve Latin-square periodic states and confirms they exhaust its nonzero recurrent configurations. As the programs explicitly visit all possible initial assignments (not a sample), these are finite exact exhaustive certificates for the stated basin counts and sharp finite entry cutoffs; they are not offered as a proof of the infinite-family assertion.

## Verification

Run `python3 verify_forward.py` and `python3 verify_independent.py` from the extracted files. Both require only the Python standard library; successful output ends with `FORWARD_OK` and `INDEPENDENT_OK` respectively. The companion captured outputs `forward.out` and `independent.out` record the exact same counts. Independent algebraic verification of the all-order statement consists of checking the contact-budget equality, the Paley strongly regular parameters and the quadratic trace/integrality argument above, each of which is explicit and does not depend on numerical extrapolation.

## Relationship to prior work

The thresholded three-state model is part of the excitable automata family studied by Durrett and Griffeath [1]. Their work addresses lattice wave phases and does not state the Paley-family threshold census. Gravner, Lyu and Sivakoff [2, opening and §§1–2] treat the threshold-one model on general graphs via a monotone covering process; changing one excited neighbor to a half-degree contact requirement changes the map and invalidates direct application of their period/circulation characterization. Doba [3, pp. 101–104 and §2] likewise fixes the one-contact update, so its graph-wide activity results do not imply the present classification.

A related published graph-dynamics result [5] gives a general equivalence for **initially three-periodic** states at half-degree threshold and counts them on squared cycles. That implication covers the *criterion* behind the twelve three-periodic states of \(P(9)\), but neither eliminates other periodic periods for the infinite Paley family nor proves the isolated basin and relaxation census. An existing exact finite computation for \(P(13)\) at threshold three already covers that single order; the present contribution is the all-prime-power order classification and the precise exceptional wave/basin boundary, not a claim to rediscover that finite calculation. The standard Paley parameters and exceptional small graph descriptions are given in [4].

## Limitations

The argument proves eventual extinction for \(q\ge13\) but does **not** give a uniform or optimal transient cutoff in those orders. Exact attraction basins and sharp relaxation counts are asserted only for the two exceptional orders and are backed by exhaustive finite certificates. There is no claim for contact thresholds other than exactly half the graph degree, for arbitrary strongly regular graphs, or for directed Paley tournaments. All-order proof and finite certificates do not establish historical priority by themselves; a preexisting but unindexed exact equivalent could change the originality assessment.

## References

[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, publicly submitted 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.

[2] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, preprint publicly submitted 2016-10-24, arXiv:1610.07320; open full text https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.

[3] N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems 27 (2018), 101–126, https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf.

[4] E. W. Weisstein, *Paley Graph*, MathWorld, https://mathworld.wolfram.com/PaleyGraph.html, giving the finite-field definition and strongly regular parameters; see also A. N. Elsawy, *Paley Graphs and Their Generalizations*, arXiv:1203.1818 (2012-03-07), https://arxiv.org/abs/1203.1818.

[5] *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d.
