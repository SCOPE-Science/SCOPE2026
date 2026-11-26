# Two-round freezing and hub loyalty in friendship-graph majority dynamics

## Finding

Let \(F_k=K_1\vee(kK_2)\) be the labelled friendship graph with \(k\ge1\) triangles sharing one hub. Under **synchronous binary strict open-neighbor majority with tie retention**, every initial state reaches a fixed state at or before update two; no nontrivial periodic orbit occurs. The sharp maximum first-entry time is two for \(k\ge3\), and one for \(k=1,2\).

For \(k\ge1\), define the integer
\[
 H_k=\sum_{u=\lceil k/2\rceil}^{k}\binom{k}{u}3^{k-u}
       -\mathbf{1}_{\{k\text{ even}\}}\binom{k}{k/2}.
\]
The subtracted term is by definition zero when \(k\) is odd; the central-binomial correction applies only to even \(k\).

For an initially fair, independent binary coloring, the probability that the **eventual hub opinion differs from its initial opinion** is exactly
\[
 R_k=\frac{H_k}{4^k}.
\]
Of the total \(2\cdot4^k\) labelled initial states, the numbers first entering the fixed set at times zero, one and two are respectively
\[
 T_0(k)=2\sum_{u=0}^{\lfloor k/2\rfloor}\binom{k}{u},\qquad
 T_2(k)=4^k-\binom{2k}{k}-2H_k,\qquad
 T_1(k)=2\cdot4^k-T_0(k)-T_2(k).
\]
Exactly \(2(3^k+1)\) initial states reach unanimous consensus.

The transient and eventual hub behaviors differ sharply:
\[
 \Pr\{\text{first fixed entry at update two}\}\longrightarrow\tfrac12,
 \qquad
 \Pr\{\text{eventual hub reversal}\}=R_k\longrightarrow0
 \quad\text{exponentially}.
\]
More precisely, as \(r\to\infty\),
\[
 R_{2r}\sim\frac{3}{2\sqrt{\pi r}}\left(\frac34\right)^r,
 \qquad
 R_{2r+1}\sim\frac{3}{4\sqrt{\pi r}}\left(\frac34\right)^r.
\]
Thus the hub reverses twice along nearly half the trajectories, but it almost always returns to its original opinion. Meanwhile the consensus probability is exactly \((3^k+1)/4^k\), which tends to zero exponentially.

## Assumptions and scope

The graph is simple, with vertices \(h,a_1,b_1,\ldots,a_k,b_k\), and edges \(ha_j,hb_j,a_jb_j\) for each \(j\in\{1,\ldots,k\}\), with no other edges. All vertices update **simultaneously**. Each vertex takes the strict majority of its neighbors' preceding binary states; on equality it retains its own state. No self-loops, spontaneous changes, random update order or stochasticity in the dynamics are present. Probabilities refer exclusively to the uniform product distribution on the \(2k+1\) initial bits. Time zero is the initial configuration. A first-entry time is the first time the entire configuration belongs to the fixed-point set.

## Proof

**1. Frozen peripheral pairs.** By global bit complementation it suffices to start with hub bit zero. Let \(u\), \(d\), \(m\) be the numbers of peripheral edges initially colored \((1,1)\), \((0,0)\) and mixed, respectively, so \(u+d+m=k\). Every mixed edge becomes \((0,0)\) at the first update: the initially zero endpoint sees one neighbor of each color and retains zero, while the initially one endpoint sees two zeros. A uniform edge never changes: both its vertices see their partner's color and, at worst, a tied hub of the other color. All peripheral edges are therefore uniform from time one onward, and uniform edges remain unchanged forever irrespective of the hub.

**2. Exact hub trajectory.** The hub has \(2k\) neighbors, with \(2u+m\) initial ones. It changes from zero to one at update one if and only if \(2u+m>k\). From time one onward exactly \(2u\) peripheral vertices carry one. Thus the hub at update two follows their strict majority, retaining its update-one value on a tie, and it never changes later. If the hub did not flip at time one then \(2u+m\le k\), hence \(2u\le k\); the hub cannot first flip at time two. A second hub flip occurs exactly when
\[
 2u<k<2u+m.
\]
These two flips characterize first fixed entry at time two, since peripheral vertices already freeze after update one.

**3. Hub-reversal census.** The eventual hub bit equals one precisely when either \(2u>k\), or \(2u=k\) and \(m\ge1\). Indeed, in the first case the hub already flips at time one; in the tie case it retains a first-step value of one exactly when at least one peripheral edge is mixed. For uniform independent initial bits, the number \(U\) of initially \((1,1)\) edges is \(\operatorname{Bin}(k,1/4)\). When \(k\) is odd, reversal is the event \(U\ge(k+1)/2\). When \(k\) is even, it is \(U\ge k/2\) except the configurations with \(U=k/2\) and no mixed edges. The latter event has probability \(\binom{k}{k/2}/4^k\), because every edge then is either \((1,1)\) or \((0,0)\). Thus the exact reversal probability is \(R_k=H_k/4^k\). Global complement symmetry gives \(2H_k\) reversing states in the full labelled space.

**4. Entry-time census.** The initial hub flips if and only if its \(2k\) initial peripheral-neighbor bits have strict opposing majority. By symmetry its probability is
\[
 \frac12\left(1-\frac{\binom{2k}{k}}{4^k}\right).
\]
Every first hub flip is either a permanent eventual hub reversal or the first of two opposite hub flips; there is no third possibility. Hence the number of double-flip states (equivalently first fixed entry at time two) is
\[
 (2\cdot4^k)\left[\frac12\left(1-\frac{\binom{2k}{k}}{4^k}\right)-R_k\right]
 =4^k-\binom{2k}{k}-2H_k.
\]
An initially fixed state must have \(m=0\) and a hub already consistent with the uniform peripheral edges. For initial hub zero, this requires \(2u\le k\), giving \(\sum_{u=0}^{\lfloor k/2\rfloor}\binom{k}{u}\) states; double by complementation to obtain \(T_0(k)\). All remaining states first become fixed at time one, yielding \(T_1(k)\). For \(k=1,2\), the inequality \(2u<k<2u+m\) has no solution. For each \(k\ge3\), such a solution exists: choose \((u,m)=(r,2)\) for \(k=2r+1\), \(r\ge1\), and \((u,m)=(r-1,3)\) for \(k=2r\), \(r\ge2\). This proves sharpness.

**5. Consensus census.** With initial hub zero, the final state is all zero exactly when \(u=0\), giving \(3^k\) choices of edge states: \((0,0),(0,1),(1,0)\). It is all one exactly when \(u=k\), giving one further state. The complementary initial-hub-one cases give the other \(3^k+1\) states. This proves \(2(3^k+1)\) consensus initial configurations.

**6. Sharp asymptotics.** At the lower endpoint of each binomial upper tail for \(U\sim\operatorname{Bin}(k,1/4)\), the ratio of consecutive probabilities tends to \(1/3\). The normalized tail divided by its first term therefore tends to \(1+1/3+1/9+\cdots=3/2\): domination follows by the uniformly bounded decreasing tail ratios. Stirling's formula gives the central first terms
\[
 \Pr\{U=r\}\sim\frac{(3/4)^r}{\sqrt{\pi r}}\quad(k=2r),
 \qquad
 \Pr\{U=r+1\}\sim\frac{(3/4)^r}{2\sqrt{\pi r}}\quad(k=2r+1).
\]
For even \(k\), the excluded no-mixed event contributes \(\binom{2r}{r}/4^{2r}\), exponentially negligible relative to the binomial tail. This proves both displayed asymptotic constants for \(R_k\). Moreover, \(\binom{2k}{k}/4^k\sim1/\sqrt{\pi k}\); hence the exact expression for \(T_2(k)/(2\cdot4^k)\) tends to \(1/2\). The exact consensus fraction \((3^k+1)/4^k\) tends to zero exponentially.

## Verification

The standalone standard-library programs `verify_direct.py` and `verify_counts.py` independently check the formulas. Run `python3 verify_direct.py` and `python3 verify_counts.py` from the directory containing this file. `verify_direct.py` implements majority updates directly using each vertex's actual adjacency mask, exhaustively checking every labelled initial coloring through \(k=8\), including first fixed entry, final hub opinion and consensus. `verify_counts.py` independently enumerates weighted categories of peripheral edge types (without importing the simulator) and verifies all exact identities for \(1\le k\le100\), with numerical leading-term comparisons through \(k=201\). Their captured outputs are `direct_output.txt` and `count_output.txt`. The programs test finite instances; the six proof steps above establish the results for all \(k\ge1\).

## Relationship to prior work

Mossel, Neeman and Tamuz [1] study how synchronous majority dynamics affects information aggregation and construct a different family with a small, influential social type (Section 3.1). Their example motivates examining concentrated influence but does not evaluate this fixed friendship-graph trajectory or its exact hub-reversal, entry-time and consensus counts. Benjamini, Chan, O'Donnell, Tamuz and Tan [2] use the same open-neighbor majority rule with tie retention and cite the classical eventual-period-at-most-two result. Their general and random-graph results do not give the graph-specific two-update cutoff and parity-sensitive exact distribution here.

The statement is specific to triangles sharing one hub; it does not follow merely by specializing calculations for larger clique windmills or a synchronous minority rule. Two-step freezing is obtained directly from the blade update structure, while the nontrivial counting and parity-sensitive tail estimates are evaluated here. No assertion of exhaustive historical priority is made.

## Limitations

These formulas assume exactly one shared vertex, two peripheral vertices per triangle, no extra edges and fully synchronous strict open-neighbor majority with tie retention. They do not describe random sequential updates, other tie conventions, general windmill clique sizes, biased initial distributions or perturbations of the graph. The source literature reviewed does not establish absolute absence of equivalent statements in unindexed or unpublished work. The finite verification checks do not independently certify the symbolic all-size proof. Independent scientific validation has not been performed.

## References

1. E. Mossel, J. Neeman and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893v1, first public 2012-07-04, especially Sections 1–3.1. https://arxiv.org/abs/1207.0893 .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public 2014-05-11, especially Introduction and Theorems 1.1–3. https://arxiv.org/abs/1405.2486 .
