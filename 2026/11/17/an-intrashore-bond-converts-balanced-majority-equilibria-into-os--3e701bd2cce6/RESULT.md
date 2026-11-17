# An intrashore bond converts balanced majority equilibria into oscillations

## Finding

For integers \(a,b\ge 3\), let \(G_{a,b}^{+}\) be the labelled graph obtained by adding an edge \(uv\) between two vertices of the \(a\)-vertex shore of \(K_{a,b}\). Run synchronous binary open-neighborhood majority, with the previous opinion retained on a tie. Let \(H(a,b)\) be the number of fixed configurations and \(C(a,b)\) the number of distinct primitive temporal two-cycles (unordered pairs of exchanged labelled configurations). Then:

\[
(H,C)=
\begin{cases}
(2,1),&a\text{ odd},\\
(2+2\binom{b}{(b-1)/2},1),&a=4,\ b\text{ odd},\\
(2,1),&a\ge6\text{ even},\ b\text{ odd},\\
\left(2+\left[\binom{a-2}{a/2}+\binom{a-2}{a/2-2}\right]\binom{b}{b/2},\;
1+\binom{a-2}{a/2-1}\binom{b}{b/2}\right),&a,b\text{ even}.
\end{cases}
\]

By contrast, for the unmodified \(K_{a,b}\), the fixed-point count is \(2+\binom{a}{a/2}\binom{b}{b/2}\) when both shores are even, and \(2\) otherwise; its only primitive temporal two-cycle alternates the two uniform opposite-shore configurations. (The binomial term is taken only in the stated even-even case.)

**Sharp edge response.** When \(a,b\) are even, write
\[
T_{a,b}=\binom{a-2}{a/2-1}\binom{b}{b/2}.
\]
Adding the single edge changes \((H,C)\) by \((-2T_{a,b},+T_{a,b})\). Thus \(H+2C\), the number of labelled recurrent configurations, is unchanged: precisely \(2T_{a,b}\) former equilibria are paired into \(T_{a,b}\) new two-cycles. When \(a=4\) and \(b\) is odd, the same edge instead creates \(2\binom{b}{(b-1)/2}\) fixed configurations and no additional two-cycle. In all remaining parity cases both counts remain unchanged. For \(a=b=2m\) with \(m\to\infty\), the created number of two-cycles satisfies \(T_{2m,2m}\sim16^m/(4\pi m)\).

## Assumptions and scope

The graph is simple, undirected, loopless, with all cross-shore edges present and exactly one extra intrashore edge. The two distinguished endpoints \(u,v\) belong to the shore of size \(a\), not the other shore; this orientation matters when \(a\ne b\). The integers satisfy \(a,b\ge3\). Every bit assignment to the \(a+b\) labelled vertices is counted separately. A two-cycle is counted once, not once per temporal phase. No spatial quotient or probabilistic assumption is used. This work counts periodic configurations, not their basins or longest transient lengths. General symmetric-threshold theory guarantees that eventual periods are at most two, but this classification needs only the equations for fixed states and two-cycles.

## Proof

Write \(U\) for the two distinguished vertices, \(A_0\) for the \(m=a-2\) ordinary vertices in their shore, and \(B\) for the opposite shore. For a configuration, denote the special bits by \(u,v\in\{0,1\}\), the number of active ordinary vertices by \(t\), and the number of active vertices of \(B\) by \(k\). Put \(S=t+u+v\). If \(M(q,d,z)\) means \(0\) when \(2q<d\), \(1\) when \(2q>d\), and \(z\) when \(2q=d\), the simultaneous update satisfies:

\[
\begin{aligned}
u'&=M(k+v,b+1,u),&v'&=M(k+u,b+1,v),\\
t'&=\begin{cases}0&2k<b,\\t&2k=b,\\m&2k>b,\end{cases}&
k'&=\begin{cases}0&2S<a,\\k&2S=a,\\b&2S>a.\end{cases}
\end{aligned}
\]

Whenever a block's count remains unchanged due to a tie, its entire labelled bit pattern is unchanged; whenever its count changes due to strict majority, the entire block becomes uniform. Thus these coordinate rules are exact for both counting and identifying recurrence, not approximations by mean populations.

**Uniform opposite shore.** Suppose a period-at-most-two configuration has \(B\) uniform in one of its phases. The next \(B\)-block is also uniform, and the entire \(a\)-shore is forced to the uniform opinion held by \(B\), since \(b\ge3\): the extra intrashore neighbor cannot overturn even a unanimous opposite shore. Looking one phase backward, the \(a\)-shore is uniform in both phases. The only recurrent possibilities are the two unanimous fixed configurations and the unique orbit exchanging opposite uniform shores.

**Mixed opposite shore.** Otherwise \(B\) is mixed in at least one phase. It cannot become uniform at either update and later recover a mixed labelled pattern: every future update of a uniform \(B\)-block remains uniform. Hence \(B\) is mixed and unchanged in both phases; each phase must have \(S=a/2\). In particular \(a\) is even. A fixed mixed \(B\)-block has \(0<k<b\).

If \(b=2s\), then \(k=s\) is necessary: for \(k<s\), every vertex in the \(a\)-shore becomes zero, and for \(k>s\), every such vertex becomes one, contradicting \(S=a/2\). At \(k=s\), ordinary vertices retain their bits and \((u,v)'=(v,u)\). Fixed configurations therefore have \(u=v=0\) and \(t=a/2\), or \(u=v=1\) and \(t=a/2-2\). Their counts are \(\binom{m}{a/2}\binom{b}{s}\) and \(\binom{m}{a/2-2}\binom{b}{s}\). Primitive two-cycles have \(u\ne v\) and \(t=a/2-1\). For each of the \(\binom{m}{a/2-1}\binom{b}{s}\) choices of the ordinary and opposite-shore bit patterns, the two orientations of \((u,v)\) are exchanged and constitute one orbit. This proves the even-even formulas after adding the uniform cases.

If \(b=2s+1\), only \(k=s\) or \(k=s+1\) can avoid an all-uniform \(a\)-shore. At \(k=s\), the ordinary vertices are forced to zero and the special pair is sent to \((u\wedge v,u\wedge v)\); at \(k=s+1\), ordinary vertices are forced to one and the special pair is sent to \((u\vee v,u\vee v)\). Each of these dynamics is idempotent on the special pair, so there is no primitive two-cycle with mixed \(B\). For \(S=a/2\) the first case needs the special pair \((1,1)\) and \(a/2=2\); the second needs \((0,0)\) and \(a/2=a-2\). Both are possible precisely at \(a=4\), producing one fixed configuration for each mixed \(B\)-pattern of weight \(s\) or \(s+1\). There are \(2\binom{b}{s}\) such configurations. This proves all odd-\(b\) cases.

Finally, on the original \(K_{a,b}\), both shores are uniform at any recurring state unless both have exactly half active vertices. The half-balanced case (possible only when \(a,b\) are even) is fixed, and the opposite-uniform pair is the sole primitive two-cycle. Pascal's identity
\[
\binom{a}{a/2}=\binom{a-2}{a/2}+2\binom{a-2}{a/2-1}+\binom{a-2}{a/2-2}
\]
shows that edge addition loses exactly \(2T_{a,b}\) equilibria, now forming \(T_{a,b}\) two-cycles. Since \(\binom{2m-2}{m-1}/\binom{2m}{m}=m/[2(2m-1)]\), Stirling's formula gives the stated asymptotic.

## Verification

`verify_direct.py` computes the update from explicit adjacency lists and exhaustively checks all \(1{,}024{,}064\) labelled configurations for 53 graphs with \(3\le a\le9\), \(3\le b\le10\), and \(a+b\le17\). `verify_signature.py` independently implements the four-coordinate block rule and weighted enumeration with binomial multiplicities for all 1,681 pairs \(3\le a,b\le43\). Both compare fixed and primitive-two-cycle counts to the formulas and passed. Their exact recorded outputs are provided alongside the scripts. In the weighted test, equality of both counts and special bits after two steps corresponds to equality of full labelled configurations: an initially nonuniform block can only return to itself if neither step made it uniform. All-size validity rests on the case analysis above, not finite enumeration.

For example \((a,b)=(4,4)\) gives 14 fixed states and 13 two-cycles; \((6,6)\) gives 162 and 121; \((4,5)\) gives 22 and one; \((8,8)\) gives 2,102 and 1,401.

## Relationship to prior work

The general period-at-most-two theorem of Goles and Olivos [1] supplies neither an exact orbit census nor this edge-response identity. Benjamini et al. [2] study eventual period-two behavior and agreement on infinite unimodular and random networks rather than exact counts on an intrashore-edge perturbation; its 2014 preprint was inspected. A published study of deleting a *cross-shore* edge of \(K_{a,b}\) [3] has a different graph operation and in fact retains exactly one primitive two-cycle, while the present edge insertion creates \(T_{a,b}\) new orbits for even-even sizes. A distinct study of three-colour excitation on the same edge-added graph [4] counts excitation rates for a different local rule; it does not imply these binary-majority orbit counts. Exact results on complete split graphs cover the smaller \(a=2\) special case, excluded here. The originality claim is the combined parity-sensitive all-size conversion law, not general threshold periodicity.

## Limitations

The proof excludes \(a=2\) and \(b\le2\), assumes one intrashore edge and tie retention, and does not count transient basins. It does not prove historical uniqueness: the complete original Goles–Olivos paper could not be read, and other unindexed work may exist. These limitations do not alter the internal all-size proof or the stated comparison to explicitly identified results. No independent mathematical validation is asserted.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI `10.1016/0012-365X(80)90121-1` (accessible abstract; full text unavailable).
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:`1405.2486v1`, first publicly posted 2014-05-11; preprint PDF `https://arxiv.org/pdf/1405.2486`.
3. *A one-edge majority defect has three exact basin responses*, publicly available scientific result, `https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-one-edge-majority-defect-has-three-exact-basin-responses--4c37e2b972d1/RESULT.md` (full text inspected; it deletes a cross-edge).
4. *A single internal edge produces an exact three-rate excitation law*, comparison with a distinct three-state dynamical rule (same underlying graph, different update and invariant).
