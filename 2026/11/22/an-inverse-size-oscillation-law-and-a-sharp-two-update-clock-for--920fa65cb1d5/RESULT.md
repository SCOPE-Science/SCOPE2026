# An inverse-size oscillation law and a sharp two-update clock for ternary plurality on matching-deleted cliques

## Finding

For each integer \(m\ge2\), take the labelled graph \(G_m=K_{2m}\setminus M_m\), where the removed edges are the pairs \(\{2j,2j+1\}\) for \(0\le j<m\). Every vertex independently holds one of the opinions \(\{0,1,2\}\). At each synchronous update, it takes the *unique* most frequent opinion in its open neighborhood, if there is one, but otherwise retains its old opinion. Write \(F_m\) for this deterministic map.

For all \(m\ge2\) one has, **as an identity of maps on all \(3^{2m}\) configurations**,
\[
F_m^4=F_m^2.
\]
Every attractor is fixed or has least period two; first periodic entry takes at most two updates, and this bound is attained for every \(m\ge3\). There are exact all-size formulas below for the fixed population \(E_m\), the number \(Q_m\) of primitive two-cycle *orbits*, and the population \(B_m\) of initial labelled configurations whose trajectories eventually enter a two-cycle. In particular, under independent uniform initial opinions,
\[
\Pr(\hbox{eventual period }2)=\frac{B_m}{9^m}\sim\frac{27}{8\pi\sqrt2}\frac1m.
\]
Thus recurrent oscillation has asymptotic probability of order inverse graph size, even though the number of nontrivial oscillatory orbits itself grows exponentially.

## Assumptions and scope

The graph is simple and undirected with vertices labelled \(0,1,\dots,2m-1\), and the only non-neighbor of each vertex apart from itself is its matched partner \(v\oplus1\). All vertices update *simultaneously* using the colors of their open neighborhoods. For a tied plurality, including a two-way tie with the vertex currently holding a losing third opinion, the vertex keeps its current opinion. Counts refer to individually labelled configurations; the two phases of one primitive two-cycle are one orbit. All assertions are for each integer \(m\ge2\), not just a finite tested range.

For exact formulas let \(a,b,c,u,v,w\) denote the numbers of deleted-matching pairs with unordered opinion types \(00,11,22,01,02,12\), respectively, and define
\[
a+b+c+u+v+w=m,\qquad W_m(a,b,c,u,v,w)=\frac{m!2^{u+v+w}}{a!b!c!u!v!w!}.
\]
This is the exact number of labelled opinion assignments of that pair-type profile. Let \(\mathbf1_A\) denote the indicator of statement \(A\). Each sum below is over nonnegative integer indices satisfying its displayed constraints; an empty sum is zero.

The exact fixed-state formula is
\[
E_m=3+3\sum_{0\le c<m/3}\binom mc2^{m-c}
+\mathbf1_{3\mid m}\frac{m!}{((m/3)!)^3}+24\mathbf1_{m=2}.
\]
Define three explicitly finite basin contributions:
\[
S_m=3\sum_{\substack{2a+c+u+2v=m\\2a+u>2c+v\\a+v>0}}
\frac{m!2^{u+2v}}{(a!)^2c!u!(v!)^2},
\]
\[
R_m=12m\binom{m-1}{\lfloor(m-1)/2\rfloor}\mathbf1_{m\ge3},
\]
\[
T_m=\mathbf1_{3\mid m}
\sum_{\substack{a+b+c+u+v+w=m\\2a+u+v=2b+u+w=2c+v+w\\
\mathrm{top2}(a+w,b+v,c+u)}} W_m(a,b,c,u,v,w),
\]
where \(\mathrm{top2}(r,s,t)\) means that the two largest entries among \(r,s,t\) are equal and *strictly* larger than the third. Then the exact full two-cycle basin is
\[
B_m=S_m+R_m+T_m.
\]
The exact number of immediately periodic configurations of least period two is
\[
I_m=3\sum_{\substack{a\ge1,\;2a+c+u=m\\2a+u>2c}}
\frac{m!2^u}{(a!)^2c!u!}
+\mathbf1_{m\ge3,\;m\,\mathrm{odd}}R_m,
\qquad Q_m=I_m/2.
\]

## Proof

**1. Matched pair reduction.** Each endpoint of a deleted pair has *exactly the same open neighborhood*: all vertices outside that pair. Thus its outgoing update uses the same three neighbor-frequency counts. If those counts have a strict leader, both endpoints become that opinion; otherwise both retain their previous opinions. Global opinion counts are \(N_0=2a+u+v\), \(N_1=2b+u+w\), and \(N_2=2c+v+w\). Relabel opinions when ordering these totals as \(N_A\ge N_B\ge N_C\). The following cases cover every configuration.

**2. Global unique lead of at least two.** If \(N_A\ge N_B+2\), every pair except possibly an \(AA\) pair has a strict neighborhood leader \(A\); an \(AA\) pair either also selects \(A\) or retains its already unanimous \(A\) opinion at a tie. Thus the entire state becomes unanimous \(A\) in one update.

**3. Two globally tied leaders.** Let \(N_A=N_B>N_C\). The pair-type transition table (with \(A,B\) the tied leaders) is
\[
AA\mapsto BB,\quad BB\mapsto AA,\quad AC\mapsto BB,\quad BC\mapsto AA,
\quad AB\mapsto AB,\quad CC\mapsto CC.
\]
Writing the corresponding counts as \(a,b,c,u,v,w\), the global equality is \(2a+v=2b+w\). After one update there are \(b+w\) pairs of type \(AA\), \(a+v\) pairs of type \(BB\), and only \(AB,CC\) as remaining pair types. The new \(A-B\) total difference is \(2(w-v)\). If \(v\ne w\), the newly unique leader has a margin at least two, so the following update is consensus. If \(v=w\), equality forces \(a=b\), and the pair map is an involution on the already-reduced state, preserving the strict superiority of the two leaders over \(C\). A nontrivial two-cycle occurs precisely when \(a+v>0\). (If \(a+v=0\), the original configuration is fixed.) Its full *basin* consists of exactly the profiles counted by \(S_m\), after color relabelling. The weight follows from \(a=b\), \(v=w\) and \(m=2a+c+u+2v\); the inequality \(N_A>N_C\) is \(2a+u>2c+v\). The three choices for the absent third leader are disjoint.

**4. Three globally tied leaders.** If \(N_A=N_B=N_C\), every same-color pair stays monochromatic, and every mixed pair takes the *third* opinion: \(AB\mapsto CC\), \(AC\mapsto BB\), \(BC\mapsto AA\). Thus after one update every deleted-matching pair is monochromatic. Thereafter the map on the \(m\) pairs is the usual synchronous strict-plurality-with-incumbent-ties update on the complete graph \(K_m\) without self-interaction: the opinion of a supervertex is determined by the counts of other supervertices. A unique largest class becomes unanimous at the next update; two tied strict leaders exchange colors at every step, with the third class unchanged; three tied leaders are fixed. Consequently a triple-tie input enters a two-cycle precisely when the post-update pair totals \((a+w,b+v,c+u)\) have exactly two equal strict maxima, producing \(T_m\). Otherwise the input reaches a fixed point within at most two updates.

**5. Global unique lead by one, with a unique runner-up.** Suppose \(N_A=N_B+1>N_C+1\). The first update produces only \(AA,BB,AC\) pairs, of respective multiplicities \(b+c+u+w,a,v\). Its new totals are \(N'_A=2(b+c+u+w)+v\), \(N'_B=2a\), \(N'_C=v\). Since \(N_B>N_C\), one has \(b+c+u+w\ge1\), so \(N'_A>N'_C\). The initial margin equation implies
\[
N'_A-N'_B=2(c+u+v)+w-1\ge0.
\]
When the difference is at least two, the second update produces consensus; when it is one, necessarily \(c=u=w=0,v=1\), yielding \(a=b=(m-1)/2\) and a state already on a nontrivial two-cycle (possible only for odd \(m\ge3\)). When the difference is zero, necessarily \(c=u=v=0,w=1\), yielding \(a=m/2,b=a-1\), and a one-step predecessor of a nontrivial two-cycle (possible only for even \(m\ge4\)). Counting these two disjoint families over the six ordered choices of leaders, one mixed-pair location and its two orientations yields \(R_m\); only the odd-length family contributes to \(I_m\).

**6. Global unique lead by one, with tied runners-up.** Suppose \(N_A=N_B+1=N_C+1\). Then \(2m=3r+1\) with \(r=N_B=N_C\) odd. Every pair of types \(BB,CC,BC\) becomes \(AA\), while \(AA,AB,AC\) retains its type. Hence the first output has \(N'_A=2m-u-v\), \(N'_B=u\), \(N'_C=v\), and \(u+v\le r+1\). If \(r\ge3\), the new leader has a margin at least \(r-1\ge2\), so consensus arrives at the second update. If \(r=1\), necessarily \(m=2\); the only profiles up to opinion and pair relabelling are \(AA+BC\) (which becomes unanimous) and \(AB+AC\) (already fixed). There are exactly \(24\) labelled configurations of the second type. No other fixed or oscillatory classes occur.

**7. Fixed and immediately periodic counts; sharpness.** Apart from unanimous states, fixed configurations arise from a strict double-tie with only \(AB\) and \(CC\) pairs (\(m-c>2c\)), from a triple tie with exactly \(m/3\) monochromatic pairs per color, and from the \(24\) exceptional four-vertex configurations. This gives the stated \(E_m\). Immediately periodic two-cycle states arise either from the double-tie sector with no \(AC,BC\) pairs (\(v=w=0\)) and at least one \(AA,BB\) pair (\(a=b\ge1\)), or from the odd-size margin-one family. Their exact counts are \(I_m\), and each orbit contributes two states. All the cases give periodic entry by time two, proving \(F_m^4=F_m^2\). The maximum entry time is one for \(m=2\) and two for all \(m\ge3\), as witnessed at \(m=3\) by the three pair types \(AA,AB,BC\), and for every \(m\ge4\) by one \(AA\) pair, two \(BC\) pairs and \(m-3\) pairs of type \(AB\). Direct substitution gives initial transient depth two in each case.

**8. Inverse-size oscillation asymptotic.** Start with independent uniform opinions. Across different missing-edge pairs the unordered types \(AA,BB,CC,AB,AC,BC\) occur independently with probabilities \((1,1,1,2,2,2)/9\). To characterize a specific two-leader sector, define pair increments \(X=\mathbf1_{AA}-\mathbf1_{BB}\), \(Y=\mathbf1_{AC}-\mathbf1_{BC}\) and \(D=\#A-\#C\), the per-pair difference in opinion totals. The double-tie constraints are exactly \(\sum X=\sum Y=0\), with the third opinion strictly behind when \(\sum D>0\). The centered covariance matrix of \((X,Y,D)\) is
\[
\Sigma=\begin{pmatrix}
2/9&0&2/9\\0&4/9&2/9\\2/9&2/9&4/3
\end{pmatrix}.
\]
The two-dimensional lattice of \((X,Y)\) has full span \(\mathbb Z^2\), covariance determinant \(8/81\), and is aperiodic. The bivariate local central limit theorem therefore gives
\[
\Pr\{\textstyle\sum X=\sum Y=0\}=\frac{9}{4\pi\sqrt2\,m}+o(m^{-1}).
\]
Conditionally on this event, the normalized third coordinate is asymptotically centered Gaussian with Schur-complement variance \(4/3-2/9-1/9=1\); this follows from the joint lattice local central limit theorem and summation over \(D\). Hence the strict third-place inequality holds with conditional probability \(1/2+o(1)\). The excluded degenerate case \(a+v=0\) has unconditional probability at most \((1/3)^m\). Multiplying by three for the three possible pairs of tied leaders yields
\[
\frac{S_m}{9^m}=\frac{27}{8\pi\sqrt2\,m}+o(m^{-1}).
\]
The rare margin-one sector is exponentially negligible, since \(R_m/9^m=O(\sqrt m(2/9)^m)\). Finally, the triple-tie sector imposes two independent initial equality constraints plus one independent post-update equality. For example, the per-pair contributions to the three totals \( (N_A-N_B,N_A-N_C,a+w-b-v)\) have centered covariance matrix \(\begin{psmallmatrix}4/3&2/3&0\\2/3&4/3&0\\0&0&2/3\end{psmallmatrix}\), with positive determinant \(8/9\). The other two choices of post-update tied leaders are its opinion permutations. A three-dimensional lattice local central limit upper bound therefore gives \(O(m^{-3/2})\) probability for the required equalities. Thus \(T_m/9^m=O(m^{-3/2})\), proving the asymptotic expression for \(B_m\).

## Verification

The standalone program `verify_labelled.py` constructs every vertex's actual open-neighborhood adjacency list and performs exhaustive functional-graph analysis of every labelled state for \(2\le m\le5\) (and \(m=6\) with the `--extended` argument), checking least periods, all attraction depths, and the map identity. This is independent of the pair-profile argument. The separate `verify_profiles.py` enumerates every unordered six-type profile with its exact labelled multiplicity, evolves profiles directly by excluding the whole matched pair, and independently tests \(E_m\), \(I_m\), and \(B_m\) for every \(2\le m\le12\). It also checks each maximum transient depth. Both programs require only Python 3 standard libraries. Replay from this directory with `python3 verify_labelled.py --extended` and `python3 verify_profiles.py`. The included `verification_output.txt` records the observed verification results, not a replacement for proof.

For example, at \(m=2,3,4,5,6\), the triples \((E_m,Q_m,B_m)\) are respectively \((39,3,6)\), \((33,54,108)\), \((147,153,1314)\), \((339,915,6630)\), and \((861,3270,41100)\). Finite checks corroborate, but do not establish, the assertions for unbounded \(m\); those depend on the preceding exact case analysis and local-limit proof.

## Relationship to prior work

Mossel, Neeman and Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks* (arXiv:1207.0893v1, public 2012-07-04), analyzes networked plurality/majority and convergence under graph expansion, including multi-alternative period-two results *under a no-ties assumption*. Its inspected preprint provides neither the exact three-opinion incumbent-tie dynamics on a complete graph with a perfect matching removed, nor the two-update law and inverse-size oscillation coefficient. Goles and Olivos (1980) established eventual period at most two for *binary* symmetric threshold maps; this theorem does not enumerate the present three-opinion dynamics, and its full text was not available in the consulted access path.

Directly relevant accessible mathematical records are the exact **binary** majority census on matching-deleted complete graphs (published-finding corpus, 2026-11-17) and the **three-state excitable Greenberg–Hastings** orbit census on cocktail-party graphs (published-finding corpus, 2026-11-02). Their full result/proof sections were compared: neither update rule is the three-opinion incumbent-tie plurality rule, so their finite counts or implications do not give these formulas. Results for binary majority on tripartite graphs and three-opinion plurality on distinct friendship and Petersen families likewise do not imply this census. No equivalent or stronger prior result was identified after statement-level comparisons; coverage by unindexed papers or unavailable complete classical sources remains a historical-priority risk.

## Limitations

The theorem is for three named opinions, the precisely specified tie-retention rule, synchronous open-neighborhood updates, and a complete graph with a perfect matching deleted; it does not assert analogous laws for other tie-resolution conventions, numbers of opinions, weighted graphs, or arbitrary missing edges. Asymptotic probability assumes independent uniform initial opinions and concerns the *eventual least period*, not immediate periodicity. The exact summations are finite but are not simplified into a single elementary closed form. Historical-priority checks cannot prove universal uniqueness. 

## References

1. E. Mossel, J. Neeman and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893v1, first public 2012-07-04, https://arxiv.org/pdf/1207.0893 .
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
3. *Parity-gated majority oscillations on matching-deleted complete graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-parity-gated-majority-oscillations-on-matching-deleted-complete--e054374efd08 .
4. *Three-state excitation on cocktail-party graphs: a sharp period transition and exact orbit count* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-state-excitation-on-cocktail-party-graphs-a-sharp-period-t--b65add71b337 .
