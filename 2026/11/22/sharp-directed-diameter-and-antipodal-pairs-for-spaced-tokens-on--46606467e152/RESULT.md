# Sharp directed diameter and antipodal pairs for spaced tokens on cycles

## Finding

Fix integers \(r\ge2\), \(k\ge2\), and \(n\ge rk\). A state is a \(k\)-subset of the vertices \(\mathbb Z/n\mathbb Z\) such that successive occupied vertices in cyclic order are separated by at least \(r\) clockwise edges. A directed move replaces one occupied vertex \(v\) by \(v+1\pmod n\) and is permitted only if the resulting state is feasible. This is clockwise token sliding under separation, equivalently token sliding along the clockwise arcs of the base cycle while retaining independence in its \((r-1)\)-st power.

**Theorem.** When \(n=rk\), all \(r\) feasible states are isolated. When \(n>rk\), the directed reconfiguration graph is strongly connected. For two states \(X,Y\), define
\[
 p_j=\sum_{v=0}^{j}\bigl(\mathbf1_X(v)-\mathbf1_Y(v)\bigr),\qquad 0\le j<n.
\]
Its exact directed distance, namely the minimum number of clockwise slides taking \(X\) to \(Y\), is
\[
 d_{\to}(X,Y)=\sum_{j=0}^{n-1}\bigl(p_j-\min_{0\le h<n}p_h\bigr).
\]
Consequently its sharp directed diameter is
\[
 \operatorname{diam}_{\to}(n,k,r)=k\bigl(n-r(k-1)-1\bigr).
\]
There are exactly \(n\) **ordered** pairs at that diameter. With vertices indexed from zero, they are precisely the simultaneous cyclic rotations of
\[
 X_0=\{0,r,2r,\ldots,(k-1)r\},\qquad
 Y_0=\{n-1-(k-1)r,\ldots,n-1-r,n-1\}.
\]
Thus exactly \(n\) states have the maximum possible outgoing eccentricity, and each has exactly one state at that distance. For \(s=n-rk>0\), the reconfiguration digraph has
\[
 |V|=\frac nk\binom{s+k-1}{k-1},\qquad |A|=n\binom{s+k-2}{k-1}
\]
vertices and directed arcs, respectively.

## Assumptions and scope

Vertices of the underlying cycle have fixed labels \(0,1,\ldots,n-1\) and clockwise arcs \(v\to v+1\pmod n\). Tokens are indistinguishable; configurations are sets, not labelled-token permutations. Feasibility requires all \(k\) cyclic gaps to be at least \(r\), including the wraparound gap. These are one-site moves, not arbitrary slides along every edge of the cycle power. Directed distances count actual moves, with no zero-cost waiting. The theorem concerns \(r,k\ge2\); the one-token case is excluded to avoid a degenerate boundary convention.

## Proof

**1. Conservation and a sharp lower bound.** Write \(a_v=\mathbf1_X(v)\), \(b_v=\mathbf1_Y(v)\). If a directed transformation uses the arc \(j\to j+1\) exactly \(f_j\ge0\) times, conservation at every site gives \(f_j-f_{j-1}=a_j-b_j\) (indices modulo \(n\)). Hence \(f_j=p_j+c\), with an integer \(c\ge-\min_jp_j\). Every transformation has length at least \(\sum_j(p_j-\min_hp_h)\).

**2. This lower bound is always attained when \(n>rk\).** Choose an arc \(e=j\to j+1\) for which \(p_j\) is minimal and cut the cycle there. Unroll the following \(n\) sites as \(0,\ldots,n-1\). The nonnegative partial sums of \(a-b\) imply that, in increasing order, source positions \(x_1<\cdots<x_k\) and target positions \(y_1<\cdots<y_k\) satisfy \(x_i\le y_i\) for every \(i\). For a moment regard the \(k\) tokens as cyclically ordered, with token \(i\) intended to move rightward from \(x_i\) to \(y_i\).

There exists a monotone sequence of unit increments of these positions maintaining every cyclic spacing at least \(r\). Indeed, at an intermediate state write its positions as \(z_i\), where \(x_i\le z_i\le y_i\). Call token \(i\) unfinished if \(z_i<y_i\). If an unfinished token \(i<k\) cannot move, its clockwise gap to token \(i+1\) is exactly \(r\); feasibility of the target then implies \(y_{i+1}\ge y_i+r>z_i+r=z_{i+1}\), so token \(i+1\) is also unfinished. If unfinished token \(k\) is blocked by the wraparound gap, the target wraparound constraint similarly makes token \(1\) unfinished. If **no** unfinished token could move, blockage would therefore propagate around the entire ring, every token would be unfinished, and every cyclic gap would equal \(r\). This would require \(n=rk\), contrary to the strict slack assumption. Thus an unfinished token can always move; it never crosses the chosen cut because \(z_i<y_i<n\). Repeating finishes after precisely \(\sum_i(y_i-x_i)\) slides.

The arc-flow of this monotone route has \(f_j=0\) at the cut and is therefore the unique normalized nonnegative conservation flow \(f_h=p_h-\min p\). Its length attains the lower bound in step 1. This proves the exact distance formula and strong connectivity.

**3. Universal diameter and equality.** For a source or target satisfying all cyclic gaps at least \(r\), the unrolled positions obey \(x_i\ge r(i-1)\) and \(y_i\le n-1-r(k-i)\). Therefore, for each \(i\),
\[
 0\le y_i-x_i\le n-1-r(k-1).
\]
Summing gives the claimed diameter upper bound. Equality of the sum forces equality for **every** token, and hence \(x_i=r(i-1)\), \(y_i=n-1-r(k-i)\). Consequently every diameter pair is a simultaneous rotation of \((X_0,Y_0)\). Conversely these configurations satisfy the cyclic spacing constraints because their wraparound gap is \(n-r(k-1)>r\), and their monotone matching along the indicated cut has cost exactly \(k(n-1-r(k-1))\). Their nonminimal gap is unique, so their \(n\) rotations are distinct, proving the exact diametral-pair count and unique farthest targets for these \(n\) sources. Every nonpacked source has smaller outgoing eccentricity.

**4. Frozen boundary and enumeration.** At \(n=rk\), every gap equals \(r\), so moving one token would reduce the following gap below \(r\). The \(r\) different cyclic phases are isolated. For positive slack \(s=n-rk\), distinguish one token and record its \(k\) successive gaps \(r+h_i\), where the nonnegative \(h_i\) sum to \(s\). Choosing its position and the weak composition gives \(n\binom{s+k-1}{k-1}\) rooted configurations, exactly \(k\) per actual configuration. For an outgoing arc, distinguish its moving token and require its following extra gap \(h_i\ge1\); subtracting one from that entry gives \(n\binom{s+k-2}{k-1}\) possible arcs.

## Verification

The included `verify.py` independently constructs all feasible states and all legal clockwise arcs by bitmasks. It runs breadth-first search from every source and compares every ordered-pair distance to the prefix-flow formula. It also checks state counts, sharp diameter, and exactly \(n\) ordered diametral pairs, across \(73\) nonfrozen parameter triples with \(5\le n\le16\), \(2\le r\le5\), and \(2\le k\le5\) when feasible. The comparison covers \(1,896,844\) ordered pairs, with a maximum tested state space of \(672\). The exact output is in `verification_output.txt`. Run `python3 verify.py` in the directory containing both files. The finite checks are regression tests, not the proof for unbounded parameters.

## Relationship to prior work

Ito et al. introduced directed token sliding, deriving complexity results and a shortest-sequence algorithm on oriented trees. Banerjee, Engels and Hoang (2024) established polynomial-time reachability on oriented cycles; their Section 4.1 includes clockwise-cycle reachability arguments, but does not state this family-wide exact directed diameter or the unique-antipode classification. Zhang and Krauth (2024) computed diameters for symmetric exclusion and analysed the **lifted**, pointer-augmented totally asymmetric exclusion model, which is a different configuration graph. Lakatos and Chou (2003) study hard rods in asymmetric exclusion processes, but their published abstract focuses on stationary currents and phase behavior, not finite shortest-path geometry. Previously published circular bounded-gap sliding results concern **undirected** slides, and do not imply the one-way distance or antipodal count here.

## Limitations

The result concerns finite labelled cycles with a single global clockwise direction and a uniform minimum separation. It does not establish mixing times, which also depend on transition probabilities, or apply without changes to bidirectional moves, inhomogeneous gaps, multiple arc directions, or additional obstacles. These statements have not received independent external mathematical audit. A differently indexed or unpublished equivalent formulation remains a priority risk.

## References

1. T. Ito, Y. Iwamasa, Y. Kobayashi, Y. Nakahata, Y. Otachi, M. Takahashi and K. Wasa, *Independent set reconfiguration on directed graphs*, first arXiv version 25 March 2022, https://arxiv.org/abs/2203.13435.
2. N. Banerjee, C. Engels and D. A. Hoang, *Directed Token Sliding*, first arXiv version 25 November 2024, https://arxiv.org/abs/2411.16149, Section 4.1.
3. X. Zhang and W. Krauth, *Diameters of Symmetric and Lifted Simple Exclusion Models*, *Journal of Statistical Physics* 191, 103 (2024), https://doi.org/10.1007/s10955-024-03312-w.
4. G. Lakatos and T. Chou, *Totally asymmetric exclusion processes with particles of arbitrary size*, *Journal of Physics A* 36, 2027 (2003), https://doi.org/10.1088/0305-4470/36/8/302.
