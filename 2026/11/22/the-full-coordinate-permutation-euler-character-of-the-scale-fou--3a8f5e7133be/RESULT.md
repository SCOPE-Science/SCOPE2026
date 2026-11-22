# The full coordinate-permutation Euler character of the scale-four six-cube Rips complex

## Finding

Let \(Q_6=\{0,1\}^{6}\) carry Hamming distance and let \(X=\operatorname{VR}(Q_6;4)\) be the inclusive Vietoris–Rips complex: a finite set of binary words is a face precisely when its pairwise Hamming distances are at most four. The coordinate-permutation group \(S_6\) acts on \(X\). In the rational representation ring of \(S_6\), define the reduced alternating homology module
\[
 E=\sum_{j\ge0}(-1)^{j+1}[\widetilde H_j(X;\mathbb Q)].
\]
The complete character of \(E\), on the eleven conjugacy classes, is as follows. Partitions indicate the cycle type of a coordinate permutation.

| Cycle type \(\lambda\) | Admissible vertex orbits | \(\chi_E(\lambda)\) |
|---|---:|---:|
| \((6)\) | 12 | 3 |
| \((5,1)\) | 16 | 3 |
| \((4,2)\) | 20 | 5 |
| \((4,1,1)\) | 24 | 7 |
| \((3,3)\) | 24 | 13 |
| \((3,2,1)\) | 24 | 5 |
| \((3,1,1,1)\) | 32 | 7 |
| \((2,2,2)\) | 32 | 3 |
| \((2,2,1,1)\) | 40 | 29 |
| \((2,1,1,1,1)\) | 48 | 11 |
| \((1,1,1,1,1,1)\) | 64 | 253 |

Writing \(S^{\mu}\) for the rational Specht module of partition shape \(\mu\vdash6\), the exact decomposition in the rational representation ring is
\[
\begin{aligned}
E={}&7[S^{(6)}]+4[S^{(5,1)}]+5[S^{(4,2)}]+[S^{(4,1,1)}]\\
&+4[S^{(3,3)}]+4[S^{(3,2,1)}]+[S^{(3,1,1,1)}]\\
&+4[S^{(2,2,2)}]+5[S^{(2,2,1,1)}]+2[S^{(2,1,1,1,1)}]\\
&+2[S^{(1,1,1,1,1,1)}].
\end{aligned}
\]
In particular, for the *genuine geometric quotient* by coordinate permutations,
\[
 \widetilde\chi\bigl(|X|/S_6;\mathbb Q\bigr)=-7,\qquad
 \chi\bigl(|X|/S_6;\mathbb Q\bigr)=-6.
\]
Consequently its positive-degree rational homology is nonzero. These assertions are about a **virtual graded character** and a quotient Euler characteristic; no individual homological-degree Specht decomposition is asserted.

## Assumptions and scope

All vertex sets, group actions, distances, faces, and fixed spaces are finite and exact. The scale is inclusive, the dimension is exactly six, the coefficient field is \(\mathbb Q\), and the symmetry group is the subgroup \(S_6\) permuting coordinates without independently complementing them. For a coordinate permutation \(\sigma\), the permutation of the \(64\) binary words has vertex orbits \(\mathcal O\). Call an orbit admissible when its Hamming diameter is at most four. Define \(F_\sigma\) on admissible orbits: distinct orbits \(O,O'\) are adjacent if some \(u\in O\), \(v\in O'\) have Hamming distance greater than four. Write \(I_G(t)=\sum_{A\in\operatorname{Ind}(G)}t^{|A|}\), counting the empty set.

## Proof

**1. Geometric fixed-space model.** A point of the geometric realization \(|X|\) has unique barycentric coordinates supported on a face of \(X\). It is fixed by \(\sigma\) if and only if those coefficients are constant on the \(\sigma\)-orbits of vertices. A nonzero orbit coefficient is possible precisely for an admissible orbit; a family of orbit coefficients can be positive simultaneously precisely if every two orbits are compatible, or equivalently, their vertices form an independent set in \(F_\sigma\). The orbit barycenters therefore give an exact simplicial model
\[
 |X|^{\sigma}\cong |\operatorname{Ind}(F_\sigma)|.
\]
The map is affine on each orbit simplex and its inverse replaces an orbit coordinate by equal weights on its constituent vertices. This proves that the model includes stabilizers and is not merely a count of setwise-fixed faces.

**2. Lefschetz sign and independence evaluation.** Apply the finite simplicial Lefschetz formula after barycentric subdivision. The reduced alternating trace is the reduced Euler characteristic of the geometric fixed space. For any graph, including the empty graph with the standard augmented convention,
\[
 \widetilde\chi\bigl(|\operatorname{Ind}(G)|\bigr)=-I_G(-1).
\]
Thus
\[
 \chi_E(\sigma)= -\sum_j(-1)^j\operatorname{Tr}
 (\sigma\mid\widetilde H_j(X;\mathbb Q))=I_{F_\sigma}(-1).
\]

**3. Exact finite exhaustion of all conjugacy classes.** Each \(\sigma\in S_6\) has one of the eleven partitions in the displayed table. For each representative, enumerate all \(64\) words, take exact orbits, filter their within-orbit diameters, and build the incompatibility graph by the stipulated Hamming inequality. To evaluate \(I_G(-1)\), choose any vertex \(v\) and use the exact inclusion/exclusion recurrence
\[
 I_G(-1)=I_{G-v}(-1)-I_{G-N[v]}(-1),\qquad I_{\varnothing}(-1)=1.
\]
The accompanying standalone program enumerates all eleven cases in full and memoizes only exact integer results; the table is its complete exhaustive output, not an inference from sampled parameters. The maximum graph has \(64\) vertices; its two deletion orders inspect \(3{,}974{,}224\) distinct bit masks each. Both orders produce identical integers for all cases.

**4. Irreducible decomposition.** For the conjugacy class of cycle partition \(\lambda\), its size is
\[
 |C_\lambda|=\frac{6!}{\prod_{k\ge1}k^{m_k(\lambda)}m_k(\lambda)!}.
\]
Using the Murnaghan–Nakayama rim-hook recurrence for \(\chi^{\mu}(\lambda)\), calculate
\[
 m_\mu=\frac{1}{6!}\sum_{\lambda\vdash6}|C_\lambda|\chi_E(\lambda)\chi^{\mu}(\lambda).
\]
The eleven values \(m_\mu\) are respectively \(7,4,5,1,4,4,1,4,5,2,2\) in the partition order displayed in the decomposition. They are nonnegative integers and their dimension-weighted sum is \(253\). The exact Specht character matrix also passes the full class-weighted orthogonality check. This proves the representation-ring identity.

**5. Quotient.** Barycentric subdivision makes the finite group action simplicial with invariant simplexes handled by fixed vertices, and rational homology of a finite-group geometric quotient is the invariant rational homology. Thus its reduced Euler characteristic is the alternating invariant trace. The multiplicity of the trivial representation \(S^{(6)}\) in \(E\) is seven, so the reduced Euler characteristic of \(|X|/S_6\) is \(-7\). The cube edges already make \(X\) connected; hence the quotient is connected and has ordinary Euler characteristic \(-6\). In particular, the negative reduced Euler characteristic forces positive-degree rational homology.

## Verification

Run `python3 verify.py` (standard library only) in the directory containing the checker. It constructs all eleven exact orbit-incompatibility graphs, computes \(I_G(-1)\) twice with distinct tie-breaking, tests the recursion against brute-force enumeration in smaller independently generated cubes, and calculates the Specht multiplicities. The attached `character_table.csv` is the complete class table, and `verification_output.txt` is the actual passing transcript of numerical results. The Murnaghan–Nakayama characters also satisfy exact class-weighted orthogonality. Calculations are bounded, not heuristic or extrapolated, although the identity class requires millions of cached masks and appreciable memory.

## Relationship to prior work

Bendersky–Elia–Grbić, first public on 1 May 2026, study connectivity, coconnectivity, and cohomology-class constructions for hypercube Rips complexes; their full text does not give the eleven coordinate-permutation Lefschetz values at scale four on the six-cube. Galetto–Montaño–Wellner, first public on 18 June 2026, determine hyperoctahedral homology representations at scales at most three and at the terminal penultimate scale \(r=n-1\), not the intermediate case \((n,r)=(6,4)\). An existing calculation of the six-cube scale-four *translation-subgroup* character gives the identity trace \(253\), agreeing with the calculation here, but translations and coordinate permutations are different subgroups and its seven Hamming-weight trace values do not determine the eleven character values reported here. Other work on the global \(S_n\)-fixed locus at scale \(n-2\) concerns a different invariant than the elementwise trace and orbit quotient. The present result claims neither a new nonequivariant Betti number nor a complete hyperoctahedral character.

## Limitations

The eleven class values are a virtual alternating character, not a degree-by-degree decomposition. The formula does not determine integral torsion, quotient homotopy type, or the full signed-coordinate automorphism-group action. Exhaustive finite calculation is justified here because the statement has fixed parameters \((6,4)\) and only eleven conjugacy classes; it is not evidence for an unproved all-dimensional family. Literature and indexed results checked to date cannot exclude every unpublished or differently indexed equivalent result. Independent mathematical validation has not been carried out.

## References

- M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705, first public 2026-05-01; journal DOI: 10.1017/prm.2026.10175. https://arxiv.org/abs/2605.00705
- F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first public 2026-06-18. https://arxiv.org/abs/2606.20784
- *The rational translation character of the scale-four six-cube Vietoris–Rips complex*, publicly indexed analysis, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-rational-translation-character-of-the-scale-four-six-cube-vi--be304e2c20fb
- *Coordinate-symmetric fixed spheres at the penultimate hypercube Rips scale*, publicly indexed analysis, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-coordinate-symmetric-fixed-spheres-at-the-penultimate-hypercube--f9f58b2a8627
