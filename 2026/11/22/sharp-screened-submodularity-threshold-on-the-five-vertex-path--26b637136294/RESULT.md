# Sharp screened-submodularity threshold on the five-vertex path

## Finding

Let \(P_5\) be the unit-weight path with vertices \(1,2,3,4,5\), and let \(\mathcal E\) consist of its six missing edges
\[
\mathcal E=\{13,14,15,24,25,35\}.
\]
For \(S\subseteq\mathcal E\), set \(L_S=L(P_5)+\sum_{ij\in S}(e_i-e_j)(e_i-e_j)^{\mathsf T}\). For \(\mu>0\) put
\[
F_\mu(S)=\operatorname{tr}((\mu I+L_\varnothing)^{-1})-\operatorname{tr}((\mu I+L_S)^{-1}).
\]
For \(\mu=0\), replace both inverse traces by their Moore–Penrose pseudoinverse traces. Every candidate edge has unit conductance.

**Theorem.** Over the full Boolean lattice \(2^{\mathcal E}\), the improvement function \(F_\mu\) is submodular **if and only if** \(\mu\ge\rho\), where \(\rho\in(5/4,13/10)\) is the unique positive zero of
\[
q(x)=x^4+6x^3+8x^2-10x-15,
\qquad \rho\approx1.26799968328824.
\]
For every \(0<\mu<\rho\), the explicit diminishing-returns violation is supplied by the two edges \(13\) and \(35\), with no other edges added. At \(\mu=\rho\), this pair gives equality; among the 240 elementary submodularity inequalities, 29 are identities for every \(\mu\) and all other 210 are strict at and above \(\rho\). At \(\mu=0\), the edge set \(\{24\}\) and edges \(13,35\) give a strict violation of size \(3/70\).

## Assumptions and scope

The graph is exactly the connected, undirected, unnormalized unit-conductance path on five labelled vertices; edges in \(\mathcal E\) are added once each with unit weight. The scalar \(\mu\) is a uniform nonnegative diagonal screening or killing parameter, not a change in edge conductances. The claim concerns all subsets of **all six** candidate edges, not only the historically observed three chords. No assertion is made for an arbitrary graph, another path length, heterogeneous screening, or nonunit added-edge weights.

## Proof

Write \(J_\mu(S)=\operatorname{tr}((\mu I+L_S)^{-1})\) for positive \(\mu\), and \(J_0(S)=\operatorname{tr}(L_S^+)\). Submodularity of \(F_\mu\) is equivalent to the 240 inequalities
\[
\Delta_{S;e,f}(\mu):=J_\mu(S\cup\{e\})+J_\mu(S\cup\{f\})-J_\mu(S\cup\{e,f\})-J_\mu(S)\le0,
\]
where \(\{e,f\}\subset\mathcal E\) and \(S\subseteq\mathcal E\setminus\{e,f\}\): exactly \(\binom62 2^4=240\) elementary tests. This equivalence follows by applying the local two-element diminishing-returns inequalities repeatedly.

Since every \(L_S\) is connected, write \(\det(\mu I+L_S)=\mu p_S(\mu)\) with \(p_S(\mu)>0\) for \(\mu\ge0\), since \(p_S\) is the product of \(\mu\) plus the four positive Laplacian eigenvalues. Differentiating the determinant gives
\[
J_\mu(S)=\frac1\mu+\frac{p'_S(\mu)}{p_S(\mu)}.
\]
In each \(\Delta\), the four common terms \(1/\mu\) cancel. Put \(A=S\), \(B=S\cup\{e\}\), \(C=S\cup\{f\}\), \(D=S\cup\{e,f\}\). Its negative has the exact rational form
\[
-\Delta_{S;e,f}(\mu)=\frac{N_{S;e,f}(\mu)}{p_Ap_Bp_Cp_D},
\]
where, with the products and derivatives evaluated at \(\mu\),
\[
N_{S;e,f}=p'_Ap_Bp_Cp_D-p_Ap'_Bp_Cp_D-p_Ap_Bp'_Cp_D+p_Ap_Bp_Cp'_D.
\]
All denominators are positive on \([0,\infty)\). The finite algebraic certificate `verify.py` constructs each of the 64 characteristic polynomials by the 120-term determinant expansion, forms all 240 numerator polynomials using integer convolution, and checks these **exhaustive polynomial identities and coefficient inequalities**, rather than relying on numerical samples.

For \(S=\varnothing\), \(e=13\), and \(f=35\), the certificate obtains the factorization
\[
N_{\varnothing;13,35}(\mu)=2\mu(\mu+3)^5(\mu^3+7\mu^2+13\mu+5)q(\mu).
\]
The coefficient list of \(q\), in descending order, has exactly one sign change, so Descartes' rule of signs gives at most one positive root. The exact values \(q(5/4)=-215/256\) and \(q(13/10)=15581/10000\) prove that this unique positive root is \(\rho\). As all other displayed factors are positive for \(\mu>0\), this witness violates submodularity precisely when \(0<\mu<\rho\).

For every other elementary triple \((S,e,f)\), the certificate verifies exactly one of the following: (i) \(N_{S;e,f}\) vanishes identically (29 triples), or (ii) every coefficient of the polynomial \(N_{S;e,f}(v+5/4)\) is nonnegative, and its constant coefficient is positive (210 triples). Thus the 210 inequalities are strict whenever \(\mu\ge5/4\). Since \(\rho>5/4\), all 240 inequalities hold for \(\mu\ge\rho\). At \(\mu=0\), the continuous limit of the four-term difference equals the corresponding pseudoinverse-trace difference; the direct rational identity \(\Delta_{\{24\};13,35}(0)=3/70>0\) gives the remaining failure case. This proves both directions and the equality statement.

## Verification

Run `python3 verify.py` in the directory containing the extracted files. It uses only Python's standard library, only exact integer and rational arithmetic, and performs 64 determinant computations and 240 pairwise inequalities. It checks the exceptional polynomial factorization, the rational root-isolation signs, the 29 identically vanishing comparisons, the 210 shifted-coefficient positivity certificates, and the unscreened defect \(3/70\). The determinant construction and coefficient test are fully included; no external symbolic oracle, precomputed table or unlisted data is needed. Independent validation has not been performed.

## Relationship to prior work

Summers, Shames, Lygeros and Dörfler (2014) investigated edge addition to improve coherence and asserted submodularity of the unscreened objective. Their later published correction supplies the five-vertex path and the three-chord violation; that correction does not establish the full six-edge, positive-screening threshold. Ma, Garnett and Schneider (2012) prove submodularity for **vertex-label observation** in a Gaussian random field, including diagonal regularization, but their set variable is observed vertices and their inverse is a remaining principal submatrix, not edge-addition updates of a fixed-vertex resolvent. Thus their result does not imply this edge-set threshold. No result with the stated complete six-edge screened classification was found in the inspected literature; this is not a proof of universal publication priority.

## Limitations

The positive screening threshold is exact **only on this fixed path with these candidate edges and weights**; no graph-uniform repair threshold or universal greedy guarantee follows. The finite certificate gives a rigorous exhaustive algebraic proof for this fixed combinatorial ground set and all real \(\mu\) through polynomial positivity, not an enumeration of infinitely many parameter values. Source coverage is limited to inspected publications and search records, and independent mathematical review remains outstanding.

## References

1. T. H. Summers, I. Shames, J. Lygeros, F. Dörfler, *Topology Design for Optimal Network Coherence*, arXiv:1411.4884, first posted 2014-11-18. https://arxiv.org/abs/1411.4884
2. T. H. Summers, I. Shames, J. Lygeros, F. Dörfler, *Correction to “Topology design for optimal network coherence”*, https://personal.utdallas.edu/~ths150130/papers/ECC_Correction.pdf
3. Y. Ma, R. Garnett, J. Schneider, *Submodularity in Batch Active Learning and Survey Problems on Gaussian Random Fields*, arXiv:1209.3694, 2012. https://arxiv.org/abs/1209.3694
