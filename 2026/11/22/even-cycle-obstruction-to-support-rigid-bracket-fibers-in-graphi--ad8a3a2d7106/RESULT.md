# Even-cycle obstruction to support-rigid bracket fibers in graphical Lie algebras

## Finding

Let \(G=(V,E)\) be a finite simple graph, with \(n=|V|\), \(m=|E|\), and orient its edges. Over \(\mathbb F_q\) let \(L_G=\mathbb F_q^V\oplus\mathbb F_q^E\) be the graphical Lie algebra: the edge-coordinate summand is central and the oriented edge \(e=i\to j\) has bracket coordinate \([X,Y]_e=x_i y_j-x_j y_i\), for horizontal coordinates \(x,y\). Write \(F_G(z)=\#\{(X,Y)\in L_G^2:[X,Y]=z\}\). Call this fiber-count function support-rigid if it depends only on which target edge coordinates are nonzero.

**Theorem.** For each fixed prime power \(q>2\), \(F_G\) is support-rigid if and only if \(G\) has no even cycle. The cycle need not be induced. For \(q=2\), support-rigidity is automatic for every graph. For any graph with no even cycle and every \(q\ge 2\), let \(\nu(S)\) be the maximum matching size in the spanning subgraph on edge set \(S\). Set \(t_e(z)=q-1\) for \(z_e=0\) and \(t_e(z)=-1\) otherwise. Then the complete prescribed-fiber formula is
\[
F_G(z)=q^{2n+m}\sum_{S\subseteq E}q^{-2\nu(S)}\prod_{e\in S}t_e(z).
\]

## Assumptions and scope

The bracket is alternating, including in characteristic two. Counts are over ordered pairs of full Lie algebra elements; freely chosen central coordinates contribute \(q^{2m}\). Orientations only change the signs of edge coordinates. The proof allows disconnected graphs, isolated vertices, the empty graph, and unattained targets. The empty matching has size zero.

## Proof

### Fourier transform

For \(\lambda\in\mathbb F_q^E\), form the alternating matrix \(A_\lambda\) with entry \(\lambda_e\) at \((i,j)\) and \(-\lambda_e\) at \((j,i)\) for \(e=i\to j\), and zero elsewhere. Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). The sum of \(\psi(x^TA_\lambda y)\) over \(y\) is \(q^n\) if \(x^TA_\lambda=0\) and zero otherwise. Hence the Fourier coefficient with positive sign in the transform is
\[
\sum_zF_G(z)\psi(\lambda\cdot z)=q^{2(n+m)-\operatorname{rank} A_\lambda},
\]
and inversion gives
\[
F_G(z)=q^{2n+m}\sum_{\lambda\in\mathbb F_q^E}q^{-\operatorname{rank} A_\lambda}\psi(-\lambda\cdot z).
\]

### Rank on supports with no even cycle

In a graph having no even cycle, an induced subgraph cannot have two different perfect matchings, since their symmetric difference would contain an even cycle. Let \(S=\operatorname{supp}\lambda\), and take the \(2\nu(S)\) endpoints of a maximum matching. The principal Pfaffian on these vertices is the nonzero signed monomial for that matching, as no other perfect matching contributes. No larger principal Pfaffian is nonzero, as it would require a larger matching.

For clarity, the rank of an alternating matrix is the maximum size of a nonsingular principal submatrix over any field. One proves this by induction, choosing a nonsingular principal \(2\times2\) block at a nonzero off-diagonal entry. Its Schur complement is alternating by congruence elimination; choosing a principal nonsingular submatrix of that complement and adjoining the pivot indices gives a nonsingular principal submatrix in the original matrix. The rank drops by two at each elimination. The identity that the determinant of an even alternating matrix is the square of its Pfaffian holds in characteristic two as well. Thus \(\operatorname{rank}A_\lambda=2\nu(S)\).

In the inversion sum, group by \(S\). The nonzero choices of each \(\lambda_e\) contribute \(\sum_{a\ne0}\psi(-az_e)=t_e(z)\), independently across edges. This proves the formula and its support-only dependence.

### Obstruction from an even cycle

If \(G\) has a simple cycle of length \(2r\), give its edges nonzero weights and set every other frequency coordinate, including every chord, to zero. The top Pfaffian on the cycle vertices is a signed sum of the two alternating matching monomials. After fixing all but one weight, it has exactly one nonzero root in that weight: the two monomials are nonzero and exactly one involves the weight being varied. Another nonzero choice exists for \(q>2\). The ranks on these two equally supported frequencies are \(2r-2\) and \(2r\): deleting two adjacent vertices leaves a path with a unique perfect matching, so the rank at the root is at least \(2r-2\); singularity and even rank give equality. The argument also works in characteristic two.

Coordinatewise nonzero scalings act transitively on vectors of each fixed support. Fourier transformation intertwines each such scaling with its inverse, so a support-rigid fiber function would have a support-rigid Fourier transform. The two frequencies above have unequal Fourier coefficients by the rank formula. This proves necessity for \(q>2\). For \(q=2\), each support specifies a single target.

## Example from existing friendship-graph coverage

The bowtie illustrates that support-rigidity need not imply surjectivity. Its full fibers, and more generally those of any bouquet of triangles, were already determined in *Exact commutator fibers and commutator width for friendship graphical groups* (2026-10-18). That class-two group commutator has the identical edge determinant and free central-coordinate factor as the Lie bracket; reversing an orientation only changes a coordinate sign. In the bowtie a target is missed precisely when one triangle has both spoke coordinates zero and its internal coordinate nonzero, while the other has a nonzero spoke pair. This is the \(m=2\) specialization of the friendship-graph fiber formula: a zero hub cannot realize a nonzero spoke, and a nonzero hub cannot realize a nonzero internal coordinate on a triangle with both spokes zero. There are \(2q(q-1)(q^2-1)\) such targets. This application illustrates the boundary; the bowtie classification and count are not distinct contributions here.

## Verification

The accompanying `verify_graph_bracket_fibers.py` and `CHECK_OUTPUT.txt` provide finite tests of the matching formula and of explicit four-cycle witnesses. The recorded data include five-cycles over fields of sizes two, three, and four, as well as forests, triangles, bowties and a three-triangle bouquet. The enumerated input counts are horizontal counts; the full fibers additionally have the central-coordinate factor. The universal steps are the Fourier and alternating-rank arguments above, not the finite enumerations.

## Relationship to prior work and limitations

The graph Lie algebra is standard (Mainkar). Cavers et al. establish a no-even-cycle criterion for orientation-independent real skew-adjacency spectra and the related matching property. The theorem here concerns a different invariant: all prescribed finite-field bracket fibers. It uses arbitrary nonzero weights and Fourier inversion, including the two-term Pfaffian cancellation that forces distinct fibers within a target support. Rossmann studies graphical-group conjugacy and centralizers; aggregate data such as the total for a zero commutator are not the full prescribed-target law. The forest, single odd-cycle, and friendship-graph results below cover their respective subfamilies. The novelty claim is the arbitrary-graph support-rigidity criterion and accompanying matching formula across the no-even-cycle class, not the covered subfamilies. Same-day indexing of the single odd-cycle result is not used to infer relative priority.

No claim is made about general Lie algebras, complete formulas in the presence of even cycles, a polynomial-time evaluation algorithm, or definitive historical priority.

## References

- M. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414. https://arxiv.org/abs/1310.3414
- M. Cavers et al., *Skew-adjacency matrices of graphs*, Linear Algebra Appl. 436 (2012), 4512–4529, Theorems 4.2–4.3. https://doi.org/10.1016/j.laa.2012.01.019
- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bull. London Math. Soc. 54 (2022), 1923–1943. https://doi.org/10.1112/blms.12665
- *Prescribed bracket fibers of finite-field graphical Lie algebras on forests*, 2026-10-13. https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-prescribed-bracket-fibers-of-finite-field-graphical-lie-algebras--c92e90370f3f
- *Exact commutator fibers and commutator width for friendship graphical groups*, 2026-10-18. https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-exact-commutator-fibers-and-commutator-width-for-friendship-grap--152f534a63f7
- *Every prescribed bracket fiber on odd graphical cycles*, 2026-11-22. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-every-prescribed-bracket-fiber-on-odd-graphical-cycles--32d24769d1cd
