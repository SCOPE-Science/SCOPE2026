# Exact recurrent-state census for anti-coordination on friendship graphs

## Finding

For every integer \(m\ge1\), let \(W_m=K_1\vee(mK_2)\) have one central vertex \(v\) and \(m\) labelled disjoint edges \(a_i b_i\), each endpoint adjacent to \(v\). With synchronous binary **strict minority** updates and tie retention, the exact numbers of initially fixed and initially primitive-period-two configurations are, respectively,
\[
F_m=2\cdot3^m,\qquad P_m=2(3^m-2^m).
\]
There are exactly \(3^m-2^m\) distinct primitive two-orbits; the initially recurrent population is \(4\cdot3^m-2^{m+1}\). Every primitive two-cycle flips the central vertex, and every peripheral edge is either mixed or is monochromatic in the *current* hub color, with at least one monochromatic hub-color edge.

## Assumptions and scope

The graph is finite, undirected, simple, with \(2m+1\) individually labelled vertices; no parallel edges or self-loops. Each state is a vector \(x\in\{0,1\}^{V(W_m)}\). The update \(M\) is simultaneous: \(M(x)_u\) is the less frequent color in the **open neighborhood** of \(u\), except when both colors occur equally often, in which case \(M(x)_u=x_u\). A fixed state satisfies \(M(x)=x\); a primitive two-state satisfies \(M^2(x)=x\ne M(x)\). The result counts phase-labelled initial states, not temporal or graph-automorphism quotients. It does not assert that every initial configuration is periodic immediately.

## Proof

Write the hub's state as \(h\in\{0,1\}\). Its \(i\)-th peripheral edge has ordered bits \((a_i,b_i)\). Each peripheral vertex has exactly two neighbors, its partner and the hub. Consequently a one-step peripheral-edge update with hub bit \(h\) is the idempotent map \(f_h\) determined by
\[
 f_h(h,h)=(1-h,1-h),\quad
 f_h(h,1-h)=(h,1-h),\quad
 f_h(1-h,h)=(1-h,h),\quad
 f_h(1-h,1-h)=(1-h,1-h).
\]
Indeed only an edge with both bits equal to \(h\) has a strict minority at either endpoint; the other three edge states persist. Thus \(f_h^2=f_h\).

A fixed configuration with hub \(h\) can have no peripheral edge \((h,h)\), leaving three choices per edge. In any such choice at least one of the two peripheral bits differs from \(h\); among the \(2m\) neighbors of the hub there are therefore at least \(m\) bits opposite to \(h\). The hub updates to its own color \(h\), or retains it in the case of equality. Conversely, every fixed configuration must avoid \((h,h)\), by the peripheral rule. This proves \(F_m=2\cdot3^m\).

Suppose \(M^2(x)=x\ne M(x)\). If the hub had the same color at times zero and one, its color would be identical in both updates, and each peripheral edge would have to be in a two-cycle of \(f_h\). Idempotence forces every edge to be fixed, hence the entire state fixed, a contradiction. Therefore the hub switches each step. By binary complementation it suffices to analyze hub phases \(0\to1\to0\).

For a peripheral edge, two-step return under \(f_1\circ f_0\) holds exactly for initial ordered bit pairs \((0,0),(0,1),(1,0)\). Explicitly, \((0,0)\to(1,1)\to(0,0)\); mixed edges remain mixed both times; but \((1,1)\to(1,1)\to(0,0)\) does not return. If exactly \(q\) edges initially equal \((0,0)\), the number of zero peripheral bits at time zero is \(m+q\), while the number of one bits is \(m-q\). The minority hub moves from zero to one **if and only if** \(q\ge1\). At time one, the \(q\) zero edges have become \((1,1)\), and the same strict inequality reversed forces the hub from one to zero. Thus the two-step return condition is precisely that all \(m\) pairs lie in the three-element permitted list and at least one is \((0,0)\). For hub phase zero there are \(3^m-2^m\) such assignments. Global color complementation yields the same number for hub phase one, and each two-orbit has precisely two phase-labelled states. Hence \(P_m=2(3^m-2^m)\) and the claimed orbit count follows. The characterization is both necessary and sufficient for every \(m\ge1\).

## Verification

An independent direct bit-vector implementation of the simultaneous minority rule exhaustively enumerates all \(2^{2m+1}\) states for each \(1\le m\le7\), classifying states by the equalities \(M(x)=x\) and \(M^2(x)=x\ne M(x)\). It reproduces \((F_m,P_m)=(6,2),(18,10),(54,38),(162,130),(486,422),(1458,1330),(4374,4118)\). Execute `verify.py` with Python 3; its captured output is `verify.out`. These finite checks are not the proof for all \(m\).

## Relationship to prior work

Goles and Olivos (1980) prove eventual period at most two for symmetric binary threshold networks, but this does not enumerate the *initially recurrent* states of a particular cyclic graph family. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1) analyze general majority-dynamics convergence and random graphs, not this minority fixed/period-two census. Turau (arXiv:2202.01580v1) develops fixed-point and two-cycle structures for **trees**, rather than this triangular family. The explicit idempotent-blade mechanism and exact exponential count concern non-tree graphs. The generic structural relationship is acknowledged, not represented as novel.

## Limitations

No claim is made about transient lengths, basin sizes, asynchronous updates, larger blades, arbitrary graphs, or independent verification. Historical priority is qualified: inaccessible or unindexed descriptions of minority dynamics may contain the exact formula, despite no matching result in the checked records. Graph automorphism orbits are not counted. The result is a precise recurrent-state classification for the stated graph family and rule.

## References

- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (publicly posted 2014-05-11).
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (2022-02-03).
