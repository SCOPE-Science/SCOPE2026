# Persistent maximal-extinction mass in multistate excitation on double-star trees

## Finding

Let \(q\ge4\) and \(a,b\ge1\) be integers. On the double-star tree \(D_{a,b}\), join two hubs by an edge, attach \(a\) labelled leaves to the first hub and \(b\) labelled leaves to the second. Evolve the synchronous \(q\)-state Greenberg–Hastings system with one-neighbor excitation. If \(\tau(x)\) is the first update at which every vertex is resting for an initial configuration \(x\), then
\[
\max_x\tau(x)=q+2.
\]
Define
\[
L_q(m)=q^m-(q-1)^m,\qquad
R_q(m)=q^m-(q-3)^m+(q-1)^m-(q-4)^m.
\]
The **exact number of labelled initial configurations attaining this maximum** is
\[
\boxed{M_q(a,b)=L_q(a)R_q(b)+L_q(b)R_q(a).}
\]
For uniformly independent initial colors and any fixed \(q\ge4\), the terminal-shell probability has a nonzero large-branching limit:
\[
\boxed{\lim_{\min(a,b)\to\infty}\Pr\{\tau=q+2\}=\frac{2}{q^2}.}
\]
The result concerns the sharp **last extinction layer**, not the full distribution of earlier extinction times.

## Assumptions and scope

The state set is \(\{0,1,\ldots,q-1\}\). A site in state \(0\) becomes \(1\) precisely when at least one adjacent site is in state \(1\) at the current time; otherwise it remains \(0\). Every nonzero state advances by one modulo \(q\) at each update. All vertices update simultaneously. The hubs and leaves are individually labelled; symmetries are **not** quotiented out. All assertions hold for every pair of positive integers \(a,b\), including the four-vertex path at \(a=b=1\), and every integer \(q\ge4\).

## Proof

**1. Ancestry and the diameter clock.** For any tree \(T\) and any excitation \(X_t(v)=1\) at an integer time \(t\ge1\), there exists an adjacent vertex that was excited at time \(t-1\), because \(1\) can only arise from resting state \(0\) by contact. Repeatedly selecting such a predecessor produces a walk \(v_0,v_1,\ldots,v_t=v\), with \(X_j(v_j)=1\) for each \(0\le j\le t\). This walk cannot immediately backtrack: \(v_{j+2}=v_j\) would require the same site to be excited at both times \(j\) and \(j+2\); from state \(1\), its state two updates later is \(3\) (when \(q\ge4\)), not \(1\). In a tree every nonbacktracking walk is simple. Therefore \(t\le\operatorname{diam}(T)\).

Let \(D=\operatorname{diam}(T)\). No vertex is excited at a time greater than \(D\). An excitation at time \(t\) clears after exactly \(q-1\) further steps, while any initially refractory vertex clears in at most \(q-2\) steps unless it is excited again. Consequently every configuration is completely resting by time \(D+q-1\). Moreover, equality \(\tau=D+q-1\) occurs **if and only if** an excitation occurs at time \(D\). Indeed, such an excitation is still nonzero one step before the bound; without it, all last excitations occur no later than \(D-1\), and all vertices have cleared by \(D+q-2\).

**2. Characterize length-three excitation histories.** The double star has diameter \(D=3\). The only pairs of vertices at distance three are one leaf on each side, so an excitation at time three must have a simple ancestry path from a leaf of one shore to a leaf of the other. Orient such a path from the \(a\)-leaf shore to the \(b\)-leaf shore. Denote the hubs by \(u\) and \(v\), respectively. Necessary and sufficient conditions for at least one such propagation are:

* \(u\) starts in state \(0\), and at least one of its \(a\) leaves starts in state \(1\), so \(u\) is excited at time one;
* either \(v\) starts in state \(0\) and **none** of its \(b\) leaves starts in state \(1\), or \(v\) starts in state \(q-1\); exactly these possibilities ensure that \(v\) is resting at time one and is excited at time two;
* at least one of the \(b\) leaves starts in \(\{0,q-2,q-1\}\), exactly the colors that leave it resting at time two, because \(v\) is not excited at times zero or one.

These are both necessary and sufficient: the three required excitations occur on successive steps and the indicated intermediate resting conditions permit them. For \(q\ge4\), the three target colors are mutually distinct and none is \(1\).

**3. Count the two exclusive orientations.** There are \(L_q(a)=q^a-(q-1)^a\) initial assignments to the \(a\) leaves containing at least one \(1\). If \(v\) begins at \(0\), its leaf shore must contain no \(1\) and at least one color in \(\{0,q-2,q-1\}\); this yields \((q-1)^b-(q-4)^b\) assignments. If \(v\) begins at \(q-1\), its leaves are unrestricted except for containing one of those three target colors, yielding \(q^b-(q-3)^b\) assignments. The choices are disjoint and the first hub has its fixed starting color \(0\). Thus the number of left-to-right histories is \(L_q(a)R_q(b)\). Exchanging the shores gives \(L_q(b)R_q(a)\).

These two orientation events cannot both occur. For both to occur the initial hubs would both have to be \(0\); the left-to-right event then requires an initial \(1\) on the left shore and **none** on the right, while the right-to-left event requires the reverse. This is impossible. Summation therefore gives \(M_q(a,b)\) with no overcounting, and every counted configuration has \(\tau=q+2\). Since \(a,b\ge1\), the count is strictly positive, proving sharpness.

**4. Limit.** For fixed \(q\ge4\), as \(m\to\infty\), both \(L_q(m)/q^m\) and \(R_q(m)/q^m\) tend to one, since every base of the subtracted terms is strictly smaller than \(q\). There are \(q^{a+b+2}\) labelled initial configurations. Divide the exact formula by this number and let both shore sizes diverge to obtain \(2/q^2\).

## Verification

The independent programs `check_exhaustive.py` and `check_independent.cpp` are included. The first tests every initial word in fourteen parameter cases, comparing first-extinction times directly to the formula. The second uses a separate base-\(q\) integer enumeration, independently constructs adjacency, and verifies pointwise equivalence of the explicit oriented event conditions and maximal extinction, in addition to exact counts. These finite checks do not establish the all-parameter theorem; the preceding proof does.

Examples from the full-state tests are \(M_4(1,1)=12\), \(M_4(2,2)=336\), \(M_4(3,3)=6660\), \(M_4(3,4)=28182\), and \(M_5(2,3)=3816\). The scripts use only the Python standard library or a C++17 compiler and require no outside datasets. Compile the C++ source with `c++ -std=c++17 -O2 check_independent.cpp -o check_independent` and execute it; execute the Python script with `python check_exhaustive.py`.

## Relationship to prior work

Fisch and Gravner's one-dimensional deterministic Greenberg–Hastings analysis (1995, especially Section 5) defines single-line percolating excitation paths for arbitrary state count and studies infinite-line survival. Its line-path criterion supplies relevant physical intuition but does not classify maximal-extinction configurations on a branching double star or count the competing branch-screening cases. Gravner, Lyu and Sivakoff (2016 preprint, 2018 journal version) prove a general maximum-representation and finite-tree convergence results for **three-state** excitation; the present four-or-more-state labelled-branch terminal-shell formula is not a special case of their three-state theorem. The published finite-path three-state maximal-extinction enumeration also concerns a different graph and number of states, and its square-root generating function does not give this branching formula. The new count is derived directly from state-level excitation conditions rather than assumed from any general decay theorem.

## Limitations

The theorem does not give all earlier extinction-time populations, and it assumes a tree with exactly two adjacent hubs, pendant leaves, synchronous updates, and a one-excited-neighbor threshold. The asymptotic requires both leaf counts to diverge with the state count fixed. Historical-priority uncertainty remains for unindexed finite-tree excitation enumerations; searches and comparisons do not constitute proof of global novelty. Independent mathematical review has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first submitted 1993-03-22; https://arxiv.org/abs/patt-sol/9303002 .
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, *Complex Systems* **9** (1995), 329–348; https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf .
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, submitted 2016-10-24; https://arxiv.org/abs/1610.07320 . Journal version: *Annals of Applied Probability* **28** (2018), 3324–3357; https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
4. *A square-root law for maximal extinction times in three-state excitation on finite paths*, public result dated 2026-11-08; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-square-root-law-for-maximal-extinction-times-in-three-state-ex--2a387c4efac2 .
