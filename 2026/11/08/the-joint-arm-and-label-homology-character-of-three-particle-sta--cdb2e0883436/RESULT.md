# The joint arm-and-label homology character of three-particle star configurations

## Finding
Let \(Y_m\) be the finite star graph with \(m\ge 3\) leaves and let
\[
F_3(Y_m)=\{(z_1,z_2,z_3)\in Y_m^3:z_i\ne z_j\text{ for }i\ne j\}.
\]
The product \(S_m\times S_3\) acts by permuting the arms and, independently, the three distinct particle labels. For \(\alpha\in S_m\), write \(f(\alpha)\), \(t(\alpha)\) and \(u(\alpha)\) for the numbers of its cycles of lengths one, two and three. Then the full rational first-homology character is
\[
\boxed{\operatorname{tr}((\alpha,\beta)\mid H_1(F_3(Y_m);\mathbb Q))=
\begin{cases}
1+f(f+1)(2f-5),&\beta=1,\\
1-2t,&\beta\text{ is a transposition},\\
1-3u,&\beta\text{ is a three-cycle}.
\end{cases}}
\]
All quantities on the right are evaluated on \(\alpha\). Moreover, \(F_3(Y_m)\) is connected with \(H_1(F_3(Y_m);\mathbb Z)\cong\mathbb Z^{1+m(m+1)(2m-5)}\), and \(H_j(F_3(Y_m);\mathbb Z)=0\) for all \(j\ge2\). The subspace fixed by every arm permutation is zero over \(\mathbb Q\) for every \(m\ge3\).

For the smallest star, \(m=3\), the nine traces, indexed by identity, transposition and three-cycle in each factor, form the matrix
\[
\begin{pmatrix}13&1&1\\-5&-1&1\\1&1&-2\end{pmatrix}.
\]
Its \(S_3\times S_3\)-module decomposes as
\[
(\mathrm{sgn}\boxtimes\mathbf 1)\oplus2(\mathrm{sgn}\boxtimes\mathrm{Std})
\oplus(\mathrm{Std}\boxtimes\mathbf 1)
\oplus(\mathrm{Std}\boxtimes\mathrm{sgn})
\oplus(\mathrm{Std}\boxtimes\mathrm{Std}),
\]
where the first factor always refers to arm permutations.

## Assumptions and scope
The graph is the topological star with one vertex of valency \(m\) and exactly \(m\) leaves. Particles are labeled and collisions are prohibited. The action of \(S_m\) preserves center-to-leaf order on each arm, while \(S_3\) merely relabels particles. There are precisely three particles, and \(m\) may be any integer at least three. The statement is about homology representations, not an equivariant homotopy classification.

## Proof
Use the canonical ordered-distribution graph model for star configuration spaces, constructed by forgetting distances but retaining the center-to-leaf orders of particles along every arm. The one-essential-vertex configuration-space retraction identifies this graph with a deformation retract of \(F_3(Y_m)\). It is simultaneously equivariant for particle and arm permutations: both operations only relabel entries of the ordered strings, and the retraction's equal-spacing and center-movement rules are identical on each arm.

A zero-cell is either (i) an assignment of all three labels to \(m\) ordered arm strings, or (ii) a choice of the label at the center together with ordered arm strings of the other two labels. A one-cell is specified by a moving label, an arm from which that label moves between the center and the nearest position on that arm, and an ordered distribution of the other labels. Orient every one-cell from its center-occupied endpoint to its arm-occupied endpoint. All automorphisms preserve these orientations. Thus the graph's cellular chain modules are ordinary permutation representations on vertices and oriented edges.

The number of vertices and edges is, respectively,
\[
V=m(m+1)(m+5),\qquad E=3m^2(m+1).
\]
The distribution graph is connected: particles can be moved to separate arms and then reordered using the branching vertex and a third arm; this is also the standard connectivity theorem for ordered configurations on a connected graph with a vertex of valency at least three. Its first integral homology is the integral cycle kernel of the graph boundary, hence free of rank \(E-V+1=1+m(m+1)(2m-5)\), with no homology above degree one.

For \(g=(\alpha,\beta)\), let \(V_g\) and \(E_g\) be the numbers of vertices and oriented edges fixed by \(g\). The cellular Lefschetz identity is \(1-\chi(g)=V_g-E_g\). If \(\beta=1\), only arms fixed by \(\alpha\) can contain particles. Counting ordered distributions gives
\[
V_g=f(f+1)(f+5),\qquad E_g=3f^2(f+1).
\]
If \(\beta\) is a transposition, its fixed third label must either occupy the center or a fixed arm, while the exchanged labels must occupy a paired pair of arms comprising a two-cycle of \(\alpha\). Consequently,
\[
V_g=2t(f+1),\qquad E_g=2tf.
\]
If \(\beta\) is a three-cycle, no label can occupy the center or be the moving label of a one-cell. All three labels must occupy a three-cycle of arms, in one of three equivariant arrangements:
\[
V_g=3u,\qquad E_g=0.
\]
Substitution in \(\chi(g)=1-V_g+E_g\) proves the three character formulas for every integer \(m\ge3\).

The invariant dimension under \(S_m\) is the average of the character at \((\alpha,1)\). Writing \((f)_j\) for the falling factorial and expanding the first formula,
\[
1+f(f+1)(2f-5)=1-6(f)_1+3(f)_2+2(f)_3.
\]
For a uniformly random permutation in \(S_m\), the expectation of \((f)_j\) is one for \(j=1,2,3\) whenever \(m\ge3\). The average is therefore \(1-6+3+2=0\). Rational character orthogonality gives the stated \(S_3\times S_3\) decomposition when \(m=3\).

## Verification
The standalone `verify_y3.py` enumerates the 96-vertex, 108-edge ordered-distribution graph for \(m=3\), verifies connectivity and the nine character traces, and checks their integer character-inner-product decomposition. It also checks the general character formula against every element of \(S_m\times S_3\) for \(m=3,4,5,6\): respectively \(36,144,720,4320\) actions. As an independent implementation check, an Abrams-style closed-disjoint-support cubical model subdivided two, three and four times per arm yields the same nine character values at \(m=3\), using signed fixed-cell traces. The companion `verification_output.txt` is the recorded program output. The finite checks are corroboration; the proof above establishes the uniform result for all \(m\).

## Relationship to prior work
Ghrist established graph-configuration spaces' homological-dimension bound and studied the \(Y\)-graph. Lütgehetmann constructed the equivariant ordered-distribution cube model and, for one-branched-vertex graphs, determined the \(S_n\) particle-label representation. Chettih--Lütgehetmann developed integral generating sets for graph configuration-space homology. Lütgehetmann subsequently studied representation stability under permutations of attached branches. Wawrykow computed particle-stability generators and relations for ordered configurations on stars, including separate discussions of the two \(S_3\)-actions in the three-leaf case. The formula here treats the complete *joint* action on \(H_1(F_3(Y_m);\mathbb Q)\) for every \(m\); knowing either factor's restricted character alone does not determine that joint representation. No homology rank or particle-only representation from those sources is asserted to be new.

## Limitations
This result does not identify an integral \(\mathbb Z[S_m\times S_3]\)-lattice decomposition, a full equivariant homotopy type, or the joint character for four or more particles. Although closely related published sources were compared, an equivalent but unindexed joint-character calculation cannot be excluded. The proof relies on the established ordered-configuration graph retraction and independently verifies the naturality of its cell descriptions under both relevant permutations.

## References
1. R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023, first public 1999-05-05.
2. D. Lütgehetmann, *Configuration Spaces of Graphs*, master's thesis, Freie Universität Berlin, October 2014, especially Theorem 2.3 and Proposition 3.5; https://userpage.fu-berlin.de/luetge/pdfs/masters-thesis-luetgehetmann.pdf.
3. S. Chettih and D. Lütgehetmann, *The homology of configuration spaces of trees with loops*, arXiv:1612.08290, first public 2016-12-25.
4. D. Lütgehetmann, *Representation stability for configuration spaces of graphs*, arXiv:1701.03490, first public 2017-01-12.
5. N. Wawrykow, *Homology generators and relations for the ordered configuration space of a star graph*, arXiv:2401.13821, first public 2024-01-24.
