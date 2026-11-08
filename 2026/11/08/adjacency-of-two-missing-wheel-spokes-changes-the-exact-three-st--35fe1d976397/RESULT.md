# Adjacency of two missing wheel spokes changes the exact three-state excitation phase

## Finding
For each integer \(n\ge5\), take a cycle \(v_0v_1\cdots v_{n-1}v_0\) and an additional hub \(h\). Join \(h\) to every rim vertex except the **adjacent** vertices \(v_0,v_1\); call the graph \(A_n\). For the synchronous three-state cyclic cellular automaton (CCA) and the synchronous threshold-one Greenberg–Hastings model (GHM), let \(\alpha_C\) be the asymptotic fraction of CCA steps on which a fixed vertex advances, and \(\alpha_G\) the fraction of GHM steps on which it becomes excited (transition \(0\to1\)). For the same initial colouring,
\[
\alpha_C=3\alpha_G,\qquad \alpha_C\in\{0,3/5,1\}.
\]
All three values occur for every \(n\ge5\). For the uniform set of \(3^{n+1}\) labelled initial colourings, write \(R_n(r)\) for the number with \(\alpha_C=r\). Put \(q_0=q_1=2\), \(q_{j+2}=2q_{j+1}+q_j\), and \(t_0=6,t_1=18,t_2=50\), \(t_{j+3}=3t_{j+2}-t_{j+1}-t_j\). Then
\[
\begin{aligned}
R_n(0)&=\tfrac{27}{2}q_{n-1}-3t_{n-3},\\
R_n(3/5)&=3t_{n-3},\\
R_n(1)&=3^{n+1}-\tfrac{27}{2}q_{n-1}.
\end{aligned}
\]
The same populations have GHM rates \(0,1/5,1/3\), respectively. Conditional on having no initially rainbow hub triangle, the asymptotic probability of the intermediate rate is
\[
\lim_{n\to\infty}\Pr(\alpha_C=3/5\mid\text{no rainbow hub triangle})
=\frac{2(5+3\sqrt2)}{9(1+\sqrt2)^2}\approx0.3523969861.
\]

**Placement contrast.** For \(n\ge6\), remove instead the two **nonadjacent** spokes \(hv_0,hv_2\), giving \(B_n\). Every CCA rate on \(B_n\) belongs to \(\{0,3/4,1\}\), and all three occur; the GHM rates are a third of these. The graphs \(A_n,B_n\) have the same number of vertices, edges and vertex-degree multiset, yet have different nonzero intermediate excitation rates. At \(n=6\), the CCA initial-colouring populations \((0,\mathrm{mid},1)\) are \((729,378,1080)\) for \(A_6\) versus \((717,654,816)\) for \(B_6\).

## Assumptions and scope
All graphs are finite, undirected, simple, and labelled; the rim has exactly \(n\) vertices, plus one hub. The colour set is \(\{0,1,2\}\), with arithmetic modulo three. CCA advances \(c\) to \(c+1\) if some neighbour currently has colour \(c+1\), otherwise retains \(c\). In GHM, states \(1,2\) advance automatically, while state \(0\) advances to \(1\) only if a neighbour currently has state \(1\). All vertices update simultaneously. Exact counts concern **all labelled initial colourings**, not temporal orbits or independent random trajectories. The source's finite-graph activity theorem ensures the limits exist and are common to all vertices; the proof here evaluates them for the stated graph families.

## Proof
**1. A finite-graph contour reduction.** For a directed edge \((u,v)\), set \(\delta_C(u,v)\in\{-1,0,1\}\) to be the representative of the colour difference \(X(v)-X(u)\pmod3\). Theorem 3 of Gravner–Lyu–Sivakoff [1] gives
\[
\alpha_C=\max_C\frac{\left|\sum_{(u,v)\in C}\delta_C(u,v)\right|}{|C|},
\]
where the maximum ranges over simple undirected cycles given either orientation (and zero if every cycle has zero integral). Their theorem also applies to the GHM one-form. More explicitly, define \(\delta_G(u,v)=1\) on an edge directed from colour \(0\) to \(1\), \(-1\) on \(1\to0\), and \(0\) otherwise. Let \(\phi(0)=0,\phi(1)=-2,\phi(2)=-1\). Then
\[
\delta_C(u,v)=3\delta_G(u,v)+\phi(X(v))-\phi(X(u)).
\]
The potential term telescopes on every cycle, so the two cycle maxima differ by exactly a factor three for the **same** initial colouring. Every triangle has a nonzero contour integral exactly when its three vertices have distinct colours; such an integral has absolute value three and forces \(\alpha_C=1\), since \(|\delta_C|\le1\) on every edge.

**2. Adjacent missing spokes, and the cycle structure.** Consider the \(n-3\) triangular faces \((h,v_j,v_{j+1})\) for \(2\le j\le n-2\), together with the five-cycle \((h,v_{n-1},v_0,v_1,v_2,h)\). A cycle not traversing either missing vertex lies in the spoked fan and is a sum of its triangular face contours. Any simple cycle traversing the missing path uses both missing vertices and has length at least five; its contour equals that of the displayed five-cycle plus or minus some triangular face contours (or, for the outer rim, exactly their sum). This can also be seen from a fundamental-cycle basis formed by the hub spokes and the rim edges \((v_{n-1},v_0),(v_0,v_1)\) as a spanning tree, whose chords produce exactly those triangles and five-cycle.

If any triangular contour is nonzero, \(\alpha_C=1\). If all are zero, each nonzero cycle integral is the signed five-cycle integral, which is necessarily \(\pm3\) because any closed three-colour contour is divisible by three and a five-cycle has only five edges. Every such cycle has length at least five, while the five-cycle itself is present. Hence the maximum is exactly \(3/5\) if that integral is nonzero, and zero otherwise. All three phases occur: a constant colouring gives zero; a rainbow surviving hub triangle gives one; assigning colour zero to the hub and all spoked rim vertices and colours \((1,2)\) to \((v_0,v_1)\) gives five-cycle integral three and no rainbow triangle.

**3. Exact population transfer.** Fix the hub colour zero, multiplying by three at the end for arbitrary hub colours. Write the spoked rim word as \(w=(X(v_2),\ldots,X(v_{n-1}))\) of length \(n-2\). A hub triangle is rainbow exactly when consecutive letters of \(w\) are \((1,2)\) or \((2,1)\). Thus its allowable adjacency matrix is
\[
M=\begin{pmatrix}1&1&1\\1&1&0\\1&0&1\end{pmatrix}.
\]
Let \(F_n=\mathbf1^{\mathsf T}M^{n-3}\mathbf1\) be the number of allowable spoked words. An elementary characteristic-polynomial calculation, or the recurrence with initial values \(F_5=17,F_6=41\), gives \(F_n=q_{n-1}/2\). The two unspoked vertex colours are unrestricted, so the number without a rainbow triangle is \(3\cdot3^2F_n=27F_n\).

For an allowable word with last letter \(a=X(v_{n-1})\) and first letter \(b=X(v_2)\), inspect the nine possibilities for the missing-vertex pair \((X(v_0),X(v_1))\). The number giving nonzero signed five-cycle contour is
\[
N_{a,b}=\begin{pmatrix}2&3&3\\3&2&6\\3&6&2\end{pmatrix}_{a,b}.
\]
This table follows directly by summing the five edge differences on \((0,a,X(v_0),X(v_1),b,0)\), checking whether their absolute sum is three; it is also recomputed by the independent program. Therefore the number of intermediate-rate colourings is
\[
3\sum_{a,b}(M^{n-3})_{b,a}N_{a,b}
=3\operatorname{tr}(M^{n-3}N).
\]
The eigenvalues of \(M\) are \(1,1+\sqrt2,1-\sqrt2\). In particular the trace sequence \(t_j=\operatorname{tr}(M^jN)\) has initial values \(6,18,50\) and characteristic recurrence \(t_{j+3}=3t_{j+2}-t_{j+1}-t_j\). This proves the formula for \(R_n(3/5)\). Subtract it from \(27F_n\) for \(R_n(0)\), and subtract \(27F_n\) from \(3^{n+1}\) for \(R_n(1)\). The closed form
\[
t_j=(5+3\sqrt2)(1+\sqrt2)^j+(5-3\sqrt2)(1-\sqrt2)^j-4
\]
yields the stated positive conditional limit.

**4. Nonadjacent missing spokes.** With missing spokes \(hv_0,hv_2\), the fundamental cycles are the \(n-4\) surviving hub triangles and the two four-cycles \(C_1=(h,v_{n-1},v_0,v_1,h)\) and \(C_2=(h,v_1,v_2,v_3,h)\). If a hub triangle has nonzero integral then \(\alpha_C=1\), as before. Otherwise let \(c_1,c_2\in\{-3,0,3\}\) denote the two oriented four-cycle integrals. Any simple cycle that avoids both unspoked vertices has zero integral; one containing exactly one unspoked vertex has integral \(\pm c_1\) or \(\pm c_2\) and length at least four. A simple cycle containing both must traverse the rim missing-vertex paths in a common orientation, and therefore has integral \(\pm(c_1+c_2)\) and length at least six. (All other rim segments have zero contour integral because the hub triangles are irrotational.) Crucially, the six-cycle \((h,v_{n-1},v_0,v_1,v_2,v_3,h)\) realizes exactly \(c_1+c_2\).

If \(c_1=c_2=0\), the rate is zero. If both have the same nonzero sign, that six-cycle has absolute contour six, forcing rate one even **without** a rainbow triangle. Otherwise, when at least one is nonzero, the four-cycle realizes rate \(3/4\) and all other nonzero contour averages are at most \(3/4\): any contour traversing both gaps cancels if the windings have opposite signs, while a contour using a single gap has length at least four. Thus all rates belong exactly to \(\{0,3/4,1\}\). They are all realized: take a constant colouring for zero, a rainbow hub triangle for one, and for \(3/4\) take hub and all spoked rim vertices colour zero except \(v_1\) of colour two, and give \(v_0\) colour one. In contrast, assigning \((0,1,2,0,\ldots,0,1,2)\) around a suitable rim with hub colour one realizes the six-cycle rate one with no rainbow hub triangle. The graphs \(A_n,B_n\) have the same number of edges and degrees, but a different intermediate-rate spectrum.
## Verification
The source-dependent step is the finite-graph cycle-mean activity theorem [1]. Two standalone Python standard-library checks accompany this result: `direct_dynamics.py` independently iterates both dynamics until periodicity for every labelled initial state at rim sizes 5–8 (29,160 configurations **per model**), while `cycle_and_transfer.py` enumerates every simple cycle and evaluates all contours at rim sizes 5–8 for adjacent omissions and 6–8 for separated omissions (57,591 total colourings). The latter independently constructs the transfer counts through rim size 30. Re-running both produces the text files `direct_dynamics_output.txt` and `cycle_and_transfer_output.txt` embedded with the result. These finite checks corroborate the calculations; the all-size proof is the preceding contour and transfer argument.

## Relationship to prior work
[1] proves the general three-colour excitation-rate cycle-mean identity, which is used as an input, and does not state an exact adjacent-two-spoke wheel rate census or the nonadjacent placement contrast. Existing single-omitted-spoke calculations have a four-cycle intermediate phase \(3/4\); they do not determine the five-cycle count, the recurrence \(t_j\), or the same-degree-sequence placement phenomenon. Known Pell and Pell–Lucas recurrences are used as algebraic tools, not claimed new. We searched for equivalently worded wheel/fan, missing-apex-edge, excitable-network, and zero-circulation descriptions; no theorem implying the stated formulas was located. This does not prove priority against every unindexed source.

## Limitations
Only three-state synchronous threshold-one CCA and GHM on the stated families are covered. The distribution for the nonadjacent family is not given beyond the phase spectrum and illustrative finite counts; temporal entry times, orbit periods, and mixing of noisy variants are not addressed. The result is a mathematical derivation using an existing general cycle theorem and has not undergone independent scientific validation. Historical-priority uncertainty remains for potentially unindexed graph-specific enumerations.

## References
[1] J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, first posted 2016-10-24, Theorem 3 and Section 4, https://arxiv.org/abs/1610.07320.
[2] K. Piejko and I. Włoch, *On k-Distance Pell Numbers in 3-Edge-Coloured Graphs* (2014), https://doi.org/10.1155/2014/428020 (different colouring setting; cited only for the broader Pell-sequence context).
