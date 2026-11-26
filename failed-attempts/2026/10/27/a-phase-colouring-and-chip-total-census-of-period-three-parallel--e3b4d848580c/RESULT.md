# A phase-colouring and chip-total census of period-three parallel chip firing

## Finding

For any finite connected simple **labelled** graph \(G=(V,E)\) with \(|E|\ge1\), the exact least-period-three state count of the parallel chip-firing map is
\[
R_3(G)=2\sum_{\phi:V\to\mathbb Z/3\mathbb Z}\prod_{v\in V}h_{v,\phi(v)-1},
\]
where \(h_{v,t}=|\{u\sim v:\phi(u)=t\}|\), and phase indices are reduced modulo three. The product automatically vanishes unless every vertex has a neighbor in the immediately preceding phase.

A finer result counts these states by their conserved total number of chips. Put \(d_v=\deg(v)\), \(w_v=h_{v,\phi(v)-1}\), and
\[
L_v(\phi)=\begin{cases}d_v,&\phi(v)=0,\\d_v-h_{v,0},&\phi(v)=1,\\h_{v,2},&\phi(v)=2.\end{cases}
\]
With the convention that \(1+\cdots+z^{w-1}=0\) when \(w=0\), define
\[
Q_G(z)=\sum_{\phi}\prod_{v\in V}z^{L_v(\phi)}\bigl(1+z+\cdots+z^{w_v-1}\bigr).
\]
Then the exact total-chip generating polynomial for all **least-period-three** initial configurations is
\[
\boxed{P_{G,3}(z)=Q_G(z)+z^{4|E|-|V|}Q_G(z^{-1}).}
\]
In particular, its coefficient sequence is palindromic about \((4|E|-|V|)/2\), and \(P_{G,3}(1)=R_3(G)\). These are finite polynomials even though the displayed identity uses the substitution \(z^{-1}\).

For \(K_{a,b}\) with positive integer part sizes and labelled vertices, write phase-class sizes on the two shores as \((g_0,g_1,g_2)\) and \((h_0,h_1,h_2)\). The specialization is
\[
R_3(K_{a,b})=2\!\sum_{\substack{g_0+g_1+g_2=a,\ h_0+h_1+h_2=b\\g_i,h_i\ge1}}
\frac{a!}{g_0!g_1!g_2!}\frac{b!}{h_0!h_1!h_2!}\prod_{t=0}^{2}h_{t-1}^{g_t}g_{t-1}^{h_t}.
\]
In the natural thin-shore family,
\[
\boxed{R_3(K_{3,b})=12b(b-1)(b-2)3^{b-3}\quad(b\ge3),}
\]
while \(R_3(K_{3,b})=0\) for \(1\le b\le2\). In particular, \(R_3(K_{3,3})=72\) and \(R_3(K_{3,4})=864\). The period-three *existence threshold* for complete bipartite graphs was known previously; the contribution here is the exact count and its chip-total refinement.

## Assumptions and scope

Each vertex carries an arbitrary nonnegative **integer** number of chips \(x_v\). At every integer time, each vertex with at least \(d_v\) chips fires once, sending one chip along each incident edge; all firing decisions are synchronous. Thus
\[
F(x)_v=x_v-d_v\mathbf 1_{\{x_v\ge d_v\}}+\sum_{u\sim v}\mathbf 1_{\{x_u\ge d_u\}}.
\]
Vertices are labelled. All graphs are finite, loopless, simple, connected, and contain an edge, so every degree is positive. Here 'least period three' means \(F^3(x)=x\) and \(F(x)\ne x\), not merely eventual convergence to a three-cycle. All chip totals are sums over the state at a single time. The formula does not count transient states or other periods.

## Proof

**1. Uniform firing number.** For a three-step returning state, let \(k_v\in\{0,1,2,3\}\) count firings at vertex \(v\). The return identity implies \(d_vk_v=\sum_{u\sim v}k_u\). Thus \(k\) is a graph-harmonic real function. By the maximum principle on connected graphs, \(k_v=k\) at every vertex. If \(k=0\), nothing changes; if \(k=3\), each vertex fires at all three times and each time receives \(d_v\), again nothing changes. A genuine three-cycle therefore has common firing count one or two.

**2. One firing per vertex.** Suppose \(k=1\). Give each vertex the unique time \(\phi(v)\in\{0,1,2\}\) at which it fires. A vertex sees \(h_{v,t}\) firing neighbors at time \(t\). The three required firing/nonfiring inequalities simplify, for its initial chip count, to the following integer intervals:
\[
\begin{array}{c|c|c}
\phi(v)&\text{permitted }x_v&\text{number of choices}\\\hline
0 &[d_v,d_v+h_{v,2}-1]&h_{v,2}\\
1 &[d_v-h_{v,0},d_v-1]&h_{v,0}\\
2 &[h_{v,2},d_v-h_{v,0}-1]&h_{v,1}.
\end{array}
\]
For example, in phase zero, firing initially requires \(x_v\ge d_v\), and the requirement of *not firing* at time two is \(x_v-d_v+h_{v,0}+h_{v,1}<d_v\), giving \(x_v\le d_v+h_{v,2}-1\); the time-one inequality is weaker. The other rows follow by the same direct substitutions. Every such interval lies in \([0,2d_v-1]\), and empty intervals contribute no states. Different vertices' intervals are independent after \(\phi\) is fixed; each neighbor fires exactly once by construction. Over three updates the net vertex change equals \(\sum_{t}h_{v,t}-d_v=0\). Hence exactly the desired firing schedule occurs and the configuration returns. Every one-fire three-cycle gives a **unique** \(\phi\), so its chip-total enumerator is precisely \(Q_G(z)\).

**3. Boundedness of nontrivial recurrent states.** A returning state with common firing count less than three cannot contain \(x_v\ge2d_v\). Indeed, if the current value at \(v\) is at least \(2d_v\), then its predecessor value cannot have been below \(d_v\), because a nonfiring step could increase chips by at most \(d_v\). Thus the predecessor fired, and the update in a firing step never increases the vertex's value, so that predecessor also has at least \(2d_v\). Repeating backwards around the periodic orbit forces \(v\) to fire at all three times, contrary to the uniform count one or two. Therefore all coordinates of every nontrivial period-three state lie in \([0,2d_v-1]\).

**4. Complement symmetry and two firings.** On the invariant box \(\prod_v[0,2d_v-1]\), define the chip complement \((Cx)_v=2d_v-1-x_v\). Since the firing indicator flips under \(C\), substitution in the update formula gives \(CF=FC\). The involution therefore bijects one-fire and two-fire three-cycles, and preserves *least* period. It transforms total chip number \(s\) to \(\sum_v(2d_v-1)-s=(4|E|-|V|)-s\). This proves the polynomial identity and the factor two in the state count. A fixed configuration never enters either class because uniform firing count one or two is incompatible with repeating the same state each step on a connected graph.

**5. Complete bipartite specialization.** In \(K_{a,b}\), phase counts are \(g_t,h_t\). Each left vertex of phase \(t\) has \(h_{t-1}\) choices, and each right vertex has \(g_{t-1}\) choices. Positivity forces every phase to appear on both shores: nonempty phase supports on the opposite shores are related by the cyclic predecessor operation, and iterating it three times forces both supports to be the entire set of three phases. The multinomial count of assignments gives the stated finite sum. For \(a=3\), the left phase counts must all equal one, with six assignments. The weighted right-phase sum is
\(\sum_{\text{right colourings}}h_0h_1h_2=b(b-1)(b-2)3^{b-3}\): choose an ordered labelled witness for each of the three phases and assign other vertices freely. Multiplication by six and by the complement factor two gives the displayed closed form.

## Verification

The standalone `verify.py` independently (a) enumerates every state in the mathematically exhaustive bounded box for each specified finite graph, (b) tests exact prime-three recurrence under three direct synchronous updates, (c) enumerates all phase assignments independently and evaluates the weighting formula, (d) checks the multinomial expression on bipartite test graphs, and (e) compares the entire conserved-chip histogram with a separately implemented interval-product enumeration. The recorded `verification_output.txt` contains `VERIFY_OK` followed by five `HISTOGRAM_OK` checks. The mathematical proof, not the finite sample, establishes the formula for arbitrary graph size. The exact checker can be rerun with `python3 verify.py`.

## Relationship to prior work

Jiang (2010, arXiv:1003.0943) establishes the uniform activity property of periodic configurations and period feasibility for complete bipartite graphs. Those results cover the existence threshold, but not the present weighted fixed-graph exact state census or conserved-chip polynomial. Jiang, Scully and Zhang (2012 preprint, 2015 journal article) analyze allowed firing patterns and activity patterns, rather than enumerating all labelled prime-three states on each fixed graph. The 2011 Scully–Zhang–Jiang paper provides an exact condition for period two; its period-two criterion does not imply the period-three interval product. These represent the closest inspected primary literature. No originality proof follows from lack of a database match; the possibility of an unindexed equivalent remains.

## Limitations

The calculation covers **states already on exact period-three orbits**, not the basin size, transient lengths, or counts of periodic states with periods other than three. It assumes a connected loopless graph with positive vertex degrees and the conventional synchronous integer-chip threshold-degree rule. The threshold for period-three feasibility on complete bipartite graphs is earlier work, not a new discovery. The novelty assessment is bounded by accessible primary literature and indexed mathematical records and has not undergone independent review.

## References

- Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first version publicly posted 2010-03-04), https://arxiv.org/abs/1003.0943.
- Tian-Yi Jiang, Ziv Scully and Yan X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (first posted 2012-11-29), https://arxiv.org/abs/1211.6786; SIAM J. Discrete Math., DOI 10.1137/130933770.
- Ziv Scully, Yan Zhang and Damien Jiang, *Total Chip Numbers and Motors in the Parallel Chip-Firing Game*, MIT manuscript (2011), https://web.mit.edu/yzscully/www/motors.pdf.
