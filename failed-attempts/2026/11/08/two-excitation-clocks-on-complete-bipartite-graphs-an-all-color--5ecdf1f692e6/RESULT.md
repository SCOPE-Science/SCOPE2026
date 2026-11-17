# Two excitation clocks on complete bipartite graphs: an all-color Greenberg–Hastings orbit census

## Finding

For every integer \(k\ge3\) and all positive integers \(m,n\), the threshold-one, \(k\)-state Greenberg–Hastings map \(F\) on the *labelled* complete bipartite graph \(K_{m,n}\) has only the following periodic states. Write \(s=\lceil k/2\rceil\) and define the number of onto functions
\[
U(a,b)=\sum_{j=0}^{b}(-1)^j\binom bj(b-j)^a=b!\,{a\brace b},
\]
with \(U(a,b)=0\) when \(b>a\). Set
\[
H=U(m,k)U(n,k),\qquad D=2U(m,s)U(n,s).
\]
There is one fixed configuration (every vertex in resting state \(0\)); exactly \(H\) configurations belong to primitive \(k\)-cycles in which *each shore contains every one of the \(k\) colors* at every time; and exactly \(D\) configurations belong to primitive \(2s\)-cycles in which the two shores alternate between complementary, size-\(s\) color supports. These three classes are disjoint, even if \(2s=k\).

Thus the exact number of primitive periodic orbits of each length \(\ell\) is
\[
C_\ell=\mathbf1_{\ell=1}+\mathbf1_{\ell=k}\frac{H}{k}
 +\mathbf1_{\ell=2s}\frac{D}{2s}.
\]
The dynamical zeta function of the recurrent part is
\[
\zeta_F(z)=\frac{1}{1-z}(1-z^k)^{-H/k}(1-z^{2s})^{-D/(2s)}.
\]
For odd \(k\), the only possible nontrivial least periods are \(k\) and \(k+1\), and for even \(k\), the only possible nontrivial least period is \(k\). Nontrivial periodic states exist if and only if \(\min(m,n)\ge s\). When \(k\) is odd, both distinct nontrivial periods occur exactly when \(\min(m,n)\ge k\). Every configuration not listed above is strictly preperiodic.

## Assumptions and scope

The vertex set is a disjoint union of labelled shores \(L\) and \(R\), with \(|L|=m\) and \(|R|=n\); all cross-shore edges are present and there are no within-shore edges. The alphabet is \(\{0,1,\ldots,k-1\}\). At each synchronous update, a vertex in a positive color \(j\) changes to \(j+1\pmod k\). A vertex in color \(0\) changes to color \(1\) if the opposite shore contains a color-\(1\) vertex, and otherwise remains color \(0\). The primitive period is the least positive time at which the full labelled configuration returns, not the period of its unlabelled color support. Statements concern periodic configurations, not the distribution of preperiods.

## Proof

**1. A two-step implication constrains every recurrent orbit.** Work on a bi-infinite extension of any periodic trajectory, and let \(a_t\), respectively \(b_t\), be the indicators that color \(1\) occurs on the left, respectively right, at time \(t\). Color \(1\) can arise only by excitation of a resting vertex; hence
\[
a_t\le b_{t-1},\qquad b_t\le a_{t-1},\qquad a_t\le a_{t-2},\qquad b_t\le b_{t-2}.
\]
Any periodic \(0/1\) sequence satisfying the two-step inequalities is equal to its shift by two: iterate the inequalities along the finite orbit of this shift. The first two inequalities are then equalities, since \(a_t\le b_{t-1}\le a_{t-2}=a_t\), and similarly for \(b\). Therefore \(a_t=b_{t-1}\), \(b_t=a_{t-1}\), and the excitation indicators are either zero at every time, one at every time on both shores, or alternate between the two shores on consecutive updates.

If both indicators vanish forever, then every positive color ages deterministically to \(0\) in at most \(k-1\) steps, and no new excitation occurs. Periodicity forces the configuration to be all-zero.

**2. Persistent two-shore excitation.** Suppose \(a_t=b_t=1\) for every \(t\). For each shore, the occurrence of positive color \(j\) at time \(t\) is equivalent to occurrence of color \(1\) at time \(t-j+1\), for every \(1\le j<k\), because each positive color advances unconditionally. Thus each positive color occurs on each shore at every time. Since \(a_{t+1}=b_t=1\), a resting vertex must also occur on the left at time \(t\), and similarly on the right. Both shores therefore contain *all* \(k\) colors. Conversely this property is invariant, and every vertex then increments its color by one modulo \(k\) at every step. Its exact labelled period is \(k\): any vertex changes on each update and returns exactly at multiples of \(k\). The independent labelled onto-colorings of the two shores number \(H\).

**3. Alternating excitation.** Choose the time origin so that \(a_t=1\) and \(b_t=0\) at even times (and the reverse at odd times). The positive-color aging equivalence above gives, at each even time, precisely the odd positive colors on the left and precisely the even positive colors on the right. Since a right-shore excitation occurs at the next step, right color \(0\) is present at the current even step. Left color \(0\) at an even step can only arise from a left color \(k-1\) at the preceding odd step: the other source of zero, a resting zero not excited, is impossible because the right shore was excited at that preceding step. At the preceding odd step, the left positive colors are exactly the even positive colors, so left zero occurs if and only if \(k\) is odd.

Consequently the two even-time supports are exactly
\[
O_k=\{1,3,5,\ldots<k\}\cup\bigl(\{0\}\text{ if \(k\) is odd}\bigr),
\qquad E_k=\{0,2,4,\ldots<k\}.
\]
Each has \(s\) elements, they are distinct, and the next update interchanges them. The alternative parity convention gives the second, disjoint class \((E_k,O_k)\). On either class the two-step update cyclically permutes the \(s\) phases of each vertex of each shore. For example, on the even-time left support \(O_k\), positive colors advance by two until the last phase wraps through resting color \(0\); in the odd-\(k\) case the wrap passes via \(0\) before the next excitation. The cycle length is exactly \(s\), not a proper divisor, because all \(s\) phases are present. Since the two distinct shore-support pairs are exchanged at odd steps, the exact full labelled period is \(2s\). Conversely, every assignment using all \(s\) phases on the left and right of either support pair has this prescribed alternating evolution. Each support pair contributes \(U(m,s)U(n,s)\) states, giving \(D\).

**4. Counting and boundaries.** The all-zero state and the two active mechanisms exhaust every periodic orbit by Step 1. Both active classes have precisely the periods proved above. Division of labelled periodic-state counts by their primitive periods gives the orbit numbers and zeta product. Surjections exist precisely for \(m,n\) not smaller than the target support size, yielding each threshold. In particular, when \(k\) is even, both active mechanisms have period \(k=2s\) but remain disjoint because their support cardinalities differ.

## Verification

`verify_exhaustive.py` independently constructs the full transition graph for 83 parameter triples with \(3\le k\le8\) and \(1\le m,n\le4\) under a maximum of 250,000 configurations per instance. It classifies recurrence by directed indegree elimination and compares all period counts with the closed formula: 1,095,764 labelled configurations were processed, with no discrepancies. Selected exact cases: \((m,n,k)=(3,3,3)\) has \(1\) fixed state, \(36\) states of least period \(3\), and \(72\) states of least period \(4\); \((3,3,5)\) has \(1\) fixed and \(72\) states of period \(6\).

`verify_support.py` uses a separate color-support transition algorithm, without the labelled-state transitions, to exhaustively check 349,504 support states across \(3\le k\le9\). Its recurrent support configurations are exactly the all-zero case, the two full-support mechanisms and the expected alternating pair, together with impossible empty-shore cases when the graph is required to have positive shore sizes. The infinite-family theorem depends on Steps 1–4, not on finite enumeration.

Both scripts use only the Python standard library; run them with `python verify_exhaustive.py` and `python verify_support.py` in the directory containing these files. Their captured outputs are included as `verify_exhaustive.log` and `verify_support.log`.

## Relationship to prior work

The Greenberg–Hastings rule and oscillatory excitable media are classical. Durrett and Griffeath's 1993 preprint studies threshold and spatial phase-transition phenomena on regular lattices, not a complete bipartite finite-state period census. Fisch, Gravner and Griffeath's 1993 framework likewise emphasizes spatially distributed oscillatory patterns and threshold-range scaling. Gravner, Lyu and Sivakoff's 2016 preprint (2018 journal version) proves on arbitrary finite graphs an oscillation/synchronization criterion and asymptotic excitation-rate characterization for three colors; its Theorem 3 does not state the above all-\(k\) classification, Stirling-number periodic-state census, or exact primitive orbit counts.

The novelty assessed here is the exact *complete bipartite, all-color* finite-orbit result, not the excitation rule, the general synchronization results, inclusion-exclusion for onto functions, or the elementary principle that periodic-state counts divided by period give orbit counts.

## Limitations

No claim is made about first-entry-time distributions or maximal transient times; only periodic states are classified. All counts concern labelled graph configurations, not equivalence classes under permutations of vertices. A generic finite-state algorithm or the general three-color criterion might yield the small-color cases after further computation; no claim of algorithmic impossibility is made. Historical priority cannot be established conclusively by literature searches; inaccessible older full texts or unindexed presentations could contain equivalent specializations. The 1978 foundational journal work is cited by month and year only; no exact day of initial public availability is asserted.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first arXiv submission 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, first arXiv submission 1993-04-02, https://arxiv.org/abs/patt-sol/9304001.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first arXiv submission 2016-10-24, https://arxiv.org/abs/1610.07320; *Annals of Applied Probability* 28 (2018), 3324–3357, DOI:10.1214/17-AAP1350.
4. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, *SIAM Journal on Applied Mathematics* 34 (May 1978), 515–523, DOI:10.1137/0134040.
