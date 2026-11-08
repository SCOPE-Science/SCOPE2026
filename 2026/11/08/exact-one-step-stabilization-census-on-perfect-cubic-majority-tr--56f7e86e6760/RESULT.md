# Exact one-step stabilization census on perfect cubic majority trees

## Finding
For each integer \(H\ge1\), let \(T_H\) be the finite rooted tree whose root has three children, each other nonleaf has two children, and all leaves lie at distance \(H\) from the root. Thus it has \(N_H=3\cdot2^H-2\) labelled vertices; labels distinguish vertices, and no quotient by automorphisms is taken. Every degree is odd. Run simultaneous binary strict open-neighbor majority, and write \(M\) for one global update. Define the first-periodic-entry time by
\[
\tau(x)=\min\{t\ge0:M^{t+2}x=M^t x\}.
\]
The exact one-step-entry population is \(A_H=\#\{x:\tau(x)\le1\}=\#\{x:M^3x=Mx\}\).

Let \(\mathcal H=\{0,1\}^3\), and let \(\operatorname{maj}(a,b,c)\) be \(1\) when at least two of its three inputs are \(1\), and \(0\) otherwise. For \(p,v\in\mathcal H\), put
\[
D_0(p,v)=\mathbf1_{\{v_1=p_0,\ v_2=p_1,\ v_1=p_2\}}.
\]
For each integer \(h\ge1\), define the exact nonnegative integer matrix
\[
D_h(p,v)=\sum_{a,b\in\mathcal H}D_{h-1}(v,a)D_{h-1}(v,b)
\mathbf1_{\{v_1=\operatorname{maj}(p_0,a_0,b_0),\ v_2=\operatorname{maj}(p_1,a_1,b_1),\ v_1=\operatorname{maj}(p_2,a_2,b_2)\}}.
\]
Then **for every** \(H\ge1\), without a finite-size cutoff,
\[
A_H=\sum_{v,a,b,c\in\mathcal H}D_{H-1}(v,a)D_{H-1}(v,b)D_{H-1}(v,c)
\mathbf1_{\{v_1=\operatorname{maj}(a_0,b_0,c_0),\ v_2=\operatorname{maj}(a_1,b_1,c_1),\ v_1=\operatorname{maj}(a_2,b_2,c_2)\}}.
\]
The recurrence has only eight temporal-history states, independent of tree height.

The first exact populations are:

| Height \(H\) | Vertices \(N_H\) | \(A_H\) |
| ---: | ---: | ---: |
| 1 | 4 | 16 |
| 2 | 10 | 1024 |
| 3 | 22 | 3591360 |
| 4 | 46 | 44727123784320 |
| 5 | 94 | 7011368815622449172248037376 |
| 6 | 190 | 172073825280280505732279917684494237852672500611916959488 |

The first delayed initial states appear sharply at height three: all initial states have \(\tau\le1\) for \(H=1,2\), while \(H\ge3\) admits \(\tau>1\). In particular, height three has exactly \(602944\) delayed initial configurations. The rare-event bound is
\[
\frac{A_H}{2^{N_H}}\le(1-2^{-14})^{3\cdot2^{H-7}}\quad(H\ge7),
\]
so the one-step-entry probability decays exponentially in the number of vertices. No claim of an optimal exponent or a limiting entropy value is made.

## Assumptions and scope
The graph has root degree three, internal nonroot degree three and leaf degree one. Opinions are binary, simultaneous, and updated from open neighbors; ties never arise. The height convention starts with \(H=1\), a four-vertex star. The count concerns **all** labelled initial configurations entering a state of period dividing two by time one; it is not a count of initial fixed points, initial two-cycles, or basins of a specified attractor. The period-two theorem for symmetric threshold networks ensures eventual entry, but is not used to derive the exact recurrence.

## Proof
Use one three-bit history \(v=(v_0,v_1,v_2)\) at each vertex for its opinions at times zero, one and two. Impose time three equal to time one. The resulting four-time word is \((v_0,v_1,v_2,v_1)\). For an attached subtree of height zero, the vertex is a leaf, so its updates must copy the parent at successive times; this gives precisely \(D_0\), with the first bit \(v_0\) unrestricted. For height \(h\ge1\), its root has one parent and exactly two children. Choose independent child histories \(a,b\), whose rooted-subtree multiplicities are \(D_{h-1}(v,a)\) and \(D_{h-1}(v,b)\). The root must satisfy the three majority equations at times zero, one and two; imposing them gives precisely the displayed quadratic recurrence. Summation over disjoint child subtrees multiplies counts, with no unaccounted temporal choices.

At the global root there is no parent but there are three children. Their three respective products and the three majority equations produce the final formula for \(A_H\). Every admissible assignment of histories corresponds to precisely one initial configuration, because majority dynamics determines all later time slices. Conversely, any initial configuration with \(M^3x=Mx\) gives such an admissible history assignment. Therefore the formula is an exact bijective census for every height.

For height one the leaves at time one all copy the root at time zero, and the root at time two copies its own original opinion, so each vertex at time three equals itself at time one. At height two the same implication follows levelwise: a depth-one vertex at time two equals its initial value (its two leaves at time one both copy that value), hence the root at time three equals its time-one majority; similarly depth-one vertices at time three copy their time-one values because their own two children agree at time two, and each leaf at time three copies its parent at time two. Therefore every one of the \(2^{N_H}\) initial states is one-step periodic for \(H=1,2\).

To prove sharpness and exponential rarity, observe a local obstruction centered at any vertex whose radius-three ball is a full cubic-tree ball. Prescribe all three distance-one neighbors to have initial opinion zero and all twelve distance-three vertices to have initial opinion one. The center's opinion at time one is zero. Each distance-two vertex has two distance-three neighbors initially one, so it has opinion one at time one. Each distance-one neighbor therefore sees two opinion-one neighbors at time one, so has opinion one at time two. The center has opinion one at time three, contradicting \(M^3x=Mx\). Complementing all fifteen prescribed bits gives a second disjoint obstruction. The two patterns have joint probability \(2^{-14}\) under uniform independent initial bits; the remaining bits are unrestricted.

Such a radius-three ball exists for every \(H\ge3\), proving delayed states at all those heights. For \(H\ge7\), select one vertex three levels below the root of each height-six descendant subtree rooted at depth \(H-6\). There are exactly \(3\cdot2^{H-7}\) disjoint height-six subtrees, and each selected radius-three ball lies entirely within its own subtree. The obstruction events are independent. To satisfy \(M^3x=Mx\), no selected ball can have either obstruction. Multiplying their complementary probabilities gives the stated upper bound, completing the proof.

## Verification
The accompanying standalone Python program `checks/verify_fast_entry.py` implements the eight-history recurrence and verifies the six tabulated values using integer arithmetic. Independently, `checks/direct_tree.c` enumerates every labelled initial configuration on the graphs of heights one, two and three, simulates three synchronous updates, and obtains respectively \(16\), \(1024\), and \(3591360\). The direct program examines \(16+1024+4194304=4195344\) distinct initial states. Both were executed from the files embedded in this package. The all-height statement is proved by the bijection above; finite checks are corroborative only.

## Relationship to prior work
Kaaser, Mallmann-Trenn and Natale (arXiv:1508.03519v1, publicly submitted August 14, 2015) prove general maximum-voting-time bounds, not this complete one-step initial-state population. Královič (2001) determined fixed-point counts for complete binary trees, as noted by Turau (arXiv:2202.01580v1); initial fixed points do not determine their one-step preimages. Turau characterizes periodic points and pure two-cycles on trees, but the present census counts configurations that may be nonperiodic at time zero. Benjamini, Zakharov and Zhukovskii (2026) establish sharp worst-case stabilization times on trees and typical stabilization-time scales on perfect cubic trees. Those results do not state the eight-history one-step census; the full 2026 article was not completely accessible for comparison. The local obstruction is consistent with their qualitative typical-time results rather than a claim that early entry is impossible. No absolute historical-priority conclusion is drawn.

## Limitations
The exponential upper bound is not claimed sharp, and no exact limiting rate is established. The recurrence counts the cumulative time-one class, not the complete entrance-time distribution for later times. A general tree dynamic-programming approach can count finite-horizon constraints; the distinguishing output here is the explicit uniform eight-history recursion, sharp height threshold and all-height exact population for this canonical cubic family. Possible unindexed equivalent formulations and incomplete access to certain primary full texts remain priority risks. No independent external audit has been performed.

## References
1. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1 (first public version August 14, 2015), https://arxiv.org/abs/1508.03519.
2. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (February 3, 2022), https://arxiv.org/abs/2202.01580.
3. I. Benjamini, G. Zakharov and M. Zhukovskii, *Majority Dynamics on Finite Trees*, *Random Structures & Algorithms* 69 (2026), https://doi.org/10.1002/rsa.70092.
4. R. Královič, *On Majority Voting Games in Trees*, SOFSEM 2001, 282–291, https://doi.org/10.1007/3-540-45627-9_25.
5. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, *Discrete Mathematics* 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
