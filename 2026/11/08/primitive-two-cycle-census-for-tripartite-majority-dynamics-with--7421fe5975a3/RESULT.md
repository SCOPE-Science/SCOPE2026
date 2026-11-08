# Primitive two-cycle census for tripartite majority dynamics with unequal shores

## Finding
Let \(a,b,c\ge1\) be integers and put \((n_1,n_2,n_3)=(a,b,c)\). Under synchronous binary strict open-neighbor majority, retaining each vertex's present opinion on an exact neighbor tie, the number \(P_2(a,b,c)\) of *distinct temporal orbits of least period two* on the labelled complete tripartite graph \(K_{a,b,c}\) equals
\[
P_2(a,b,c)=\mathbf{1}_{\{\text{the maximum of }a,b,c\text{ occurs once}\}}+
\sum_{1\le i<j\le3\, :\,n_i=n_j}\;
\sum_{h=0}^{n_k}\binom{n_k}{h}\,\mathbf{1}_{\{|2h-n_k|<n_i\}},
\qquad \{k\}=\{1,2,3\}\setminus\{i,j\}.
\]
Every orbit is of one of two types: (I) all three shores reverse opinions in every update, the strictly largest shore opposite to the other two; or (II) two equal-sized shores reverse their monochromatic and opposite opinions, while the remaining shore stays fixed in any binary assignment satisfying the displayed strict binomial-window inequality. These families are disjoint and exhaustive.

Consequently, with \(B_c(t)=\sum_{h=0}^c\binom ch\mathbf{1}_{\{|2h-c|<t\}}\), the result has the complete trichotomy
\[
P_2(a,b,c)=\begin{cases}
1,&a,b,c\text{ pairwise distinct},\\
B_c(t)+\mathbf{1}_{\{c>t\}},&\text{the multiset of shore sizes is }\{t,t,c\},\ c\ne t,\\
3(2^t-2),&a=b=c=t.
\end{cases}
\]
For a labelled graph, there are precisely \(2P_2(a,b,c)\) configurations already of primitive period two. The balanced third case was known in a broader equal-shore census; the contribution assessed here is the unequal-shore classification, including the exact binomial window and the single-orbit rigidity when all three sizes differ.

## Assumptions and scope
The three shores are nonempty, individually labelled vertex sets; all cross-shore edges and no within-shore edges occur. A bit \(x_v\in\{0,1\}\) at vertex \(v\) becomes one if strictly more than half of its open neighbors have bit one, becomes zero if strictly less than half do, and stays unchanged upon equality. An initial configuration is *primitive period two* if \(F^2(x)=x\) and \(F(x)\ne x\). Temporal orbits are unordered pairs \(\{x,F(x)\}\); vertex labels are never quotiented by permutations.

The formula counts *immediately periodic configurations*, not full eventual basins or entry times. The general known period-one-or-two theorem gives eventual-period context but is not needed to establish the displayed enumeration.

## Proof
Write \(X_i\) for the bits in shore \(i\), of size \(n_i\). All its vertices share the same open neighborhood, namely the union of the other two shores. At any update, if the neighbor majority is strict, the whole shore becomes monochromatic; if its neighbor votes tie, every bit in that shore is retained.

**Lemma 1 (frozen or completely reversing shores).** Suppose \(F^2(x)=x\). A shore which is mixed (contains both bits) at time zero must be identical at time one, because a strict vote would make it monochromatic and no later update can create a mixed shore from a monochromatic one. A shore monochromatic at time zero remains monochromatic at every later time. Hence each shore of a primitive period-two orbit is either frozen at an arbitrary fixed bit pattern or monochromatic and flips in both updates. At least two shores must flip: if only one shore flips, every neighbor bit of that shore is fixed, so its time-independent update cannot alternate its output.

**Lemma 2 (two reversing shores).** Let shores of orders \(u,v\) flip, with third shore of order \(c\) frozen and containing \(h\) one-bits. The reversing shores cannot flip in the same direction. If both are zero before an update and both must become one, then one of them requires \(2h>v+c\); for it to become zero at the next update requires \(2(v+h)<v+c\), a contradiction. The opposite direction is symmetric. Thus the two reversing shores must be oppositely monochromatic. The frozen shore sees exactly \(u\) one-neighbors at one phase and \(v\) one-neighbors at the other. A frozen zero shore can remain zero in both phases only if \(u,v\le(u+v)/2\); a frozen one shore can remain one only if both inequalities reverse; a mixed shore can be frozen only if both neighbor counts equal half. All cases force \(u=v=t\). Conversely, with equal orders the frozen shore always sees exactly \(t\) one-neighbors out of its \(2t\) neighbors and therefore retains each bit. A reversing shore has \(t+c\) neighbors: in its zero phase its neighbor-one count is \(t+h\), requiring \(2(t+h)>t+c\); in its one phase the count is \(h\), requiring \(2h<t+c\). Both strict conditions are equivalent to \(|2h-c|<t\). For each admissible \(h\), the frozen shore has \(\binom ch\) labelled bit patterns and the two complementary orientations of the reversing pair form one temporal orbit. This proves the pair summand.

**Lemma 3 (three reversing shores).** All shores monochromatically flip. The all-zero and all-one configurations are fixed, so a phase contains exactly one one-shore, of order say \(w\), and two zero-shores of orders \(u,v\). Each zero-shore must switch to one: the required strict majorities are \(w>u\) and \(w>v\) respectively. These inequalities are also sufficient: at the next phase the previously one-shore has zero and the two others have one; each of the latter sees fewer than half its neighbors as one, while the former sees only ones, so the first phase returns. Consequently there is one orbit exactly when the largest shore size is unique, and no such orbit otherwise.

Lemmas 1–3 exhaust all possibilities and count each temporal orbit exactly once, proving the formula. The explicit trichotomy follows by noting that a pair of equal orders has only one possible remaining shore, while for \(a=b=c=t\) each of the three shore pairs contributes \(2^t-2\), since the strict inequality excludes just \(h=0,t\).

## Verification
Two standalone Python 3 programs accompany this result. Run `python check_counts.py` and `python check_direct.py` from a directory containing those programs. The first independently enumerates *all occupancy vectors*, with multinomial label weights, for each of the 729 ordered triples of shore sizes one through nine. The second iterates each binary-labelled state directly, using bitmask neighborhoods rather than the occupancy map, for 80 unordered shore profiles with total graph order at most fifteen: 646,680 directly tested labelled configurations. Both independently calculate the theorem's right-hand side and compare exact orbit counts. Their captured outputs are in `checks/counts.out` and `checks/direct.out`; these have been replayed from the packaged programs.

These checks detect implementation and boundary errors but are not the unrestricted proof. The unrestricted result follows from Lemmas 1–3.

## Relationship to prior work
Goles and Olivos (1980, 1981) established eventual periods at most two for symmetric binary threshold dynamics; they do not supply a cited, checked tripartite exact census. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, May 11, 2014) explicitly formulate tie-retaining synchronous majority and discuss convergence on arbitrary and random graphs, not an unequal-tripartite two-cycle formula. Adams, Brass, Stokes and Troxell (arXiv:1102.5361v1, February 25, 2011) examine complete multipartite graphs under *irreversible* conversion, which cannot have the reversals counted here.

An earlier equal-sized complete-multipartite majority enumeration covers the balanced specialization \(P_2(t,t,t)=3(2^t-2)\), so that specialization is not advanced as original. Nor does the present result purport to replace the general finite-graph period-two theorem. The new claim concerns the dependence of *exact primitive two-cycle populations* on three possibly unequal shore sizes, particularly the single orbit for pairwise distinct sizes and the binomial-window enhancement when precisely two shore sizes coincide.

## Limitations
No claim is made about transient entrance times, attraction-basin populations, higher-part-count exact enumeration or stochastic majority. The complete text of the earliest general threshold-periodicity papers was not accessible during comparison, and unindexed older results may contain related exact censuses. The two explicitly inspected arXiv primary texts concern different or broader questions; this is a qualified priority assessment, not a proof of global uniqueness. A separate independent mathematical audit has not been performed.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
2. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics 3 (1981), 93–105, https://doi.org/10.1016/0166-218X(81)90034-2.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (first public submission May 11, 2014), https://arxiv.org/abs/1405.2486.
4. S. Spence Adams, Z. Brass, C. Stokes and D. Sakai Troxell, *Irreversible k-threshold and majority conversion processes on complete multipartite graphs and graph products*, arXiv:1102.5361v1 (first public submission February 25, 2011), https://arxiv.org/abs/1102.5361.
