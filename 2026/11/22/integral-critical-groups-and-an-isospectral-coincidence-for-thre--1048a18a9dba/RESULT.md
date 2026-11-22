# Integral critical groups and an isospectral coincidence for three orchard line boundaries

## Finding

Let \(\mathcal A_i\), for \(i\in\{2,6,7\}\), be the three realizable real projective twelve-line arrangements denoted \(C_2,C_6,C_7\) in Bokowski–Pokora, with \(C_6\) the classical Böröczky arrangement. Over \(\mathbb C\), blow up their nineteen ordinary triple points, and let \(D_i\) be the reduced union of the twelve strict line transforms and nineteen exceptional curves. Ordinary double intersections are retained. Let \(\Gamma_i\) be the unweighted dual graph, and write \(C_m=\mathbb Z/m\mathbb Z\).

Each \(D_i\) is a connected stable nodal curve with thirty-one rational components, sixty-six nodes, and arithmetic genus thirty-six. Its integral graph Jacobian (critical group) has the exact isomorphism type

\[
\begin{aligned}
K(\Gamma_2)&\cong C_2^2\oplus C_6^6\oplus C_{672}\oplus C_{37753632},\\
K(\Gamma_6)&\cong C_2\oplus C_6^3\oplus C_{42}^3\oplus C_{210}\oplus C_{840}^2,\\
K(\Gamma_7)&\cong C_2\oplus C_6^3\oplus C_{42}^3\oplus C_{210}\oplus C_{840}^2.
\end{aligned}
\]

Thus three distinct intersection lattices with identical singular-point counts and *identical per-line incidence profiles* determine two distinct integral component groups. The nonisomorphic graphs \(\Gamma_6\) and \(\Gamma_7\) have the same Laplacian characteristic polynomial, as well as the same critical group:

\[
\begin{aligned}
\det(tI-L_6)=\det(tI-L_7)={}&t(t-7)^6(t-3)^7(t-2)^8\\
&\cdot(t^3-19t^2+107t-155)\\
&\cdot(t^3-17t^2+85t-120)^2.
\end{aligned}
\]

Their geometric Néron-component interpretation is conditional: for any proper regular split semistable one-parameter smoothing whose special fiber is \(D_i\) and whose nodes all have thickness one, the geometric component group of the Jacobian is \(K(\Gamma_i)\).

## Assumptions and scope

The base field for the three *geometric* arrangements is \(\mathbb C\); the line arrangements originate from real realizations. The triples are precisely the nineteen labeled triples in the cited primary source, pages seven and eight. Every unordered pair of the twelve lines belongs either to exactly one printed triple or to exactly one of the remaining nine ordinary double points. Each triple point is blown up exactly once. The boundary means the **reduced curve on the blowup**, not the original singular union of projective lines. No assertion is made about arbitrary arithmetic forms, arbitrary node thicknesses, or the Picard group of the ambient blown-up surface.

## Proof

**1. Reconstruction of the nodal graph.** For each printed triple \(T\), introduce one vertex \(e_T\) and three edges joining it to line vertices \(\ell_j\) with \(j\in T\). For each pair of line indices not belonging to a triple, add one line–line edge. The sixty-six unordered line pairs split into fifty-seven pair occurrences in the nineteen triples and nine other pairs; no pair occurs in two different triples. Thus there are \(19\cdot3+9=66\) graph edges and \(12+19=31\) vertices. Every exceptional component meets three strict transforms. Exactly nine strict transforms meet five exceptional curves and one other strict transform, and exactly three meet four exceptional curves and three other strict transforms. Consequently all components are rational and have at least three nodes; the connected boundary is stable. Its arithmetic genus is \(66-31+1=36\).

**2. Critical-group presentation.** Write the integral graph Laplacian with diagonals equal to vertex degrees and negative off-diagonals equal to edge multiplicities. Delete a line vertex to obtain a \(30\times30\) reduced Laplacian \(L_i'\). Since the graph is connected, the matrix-tree theorem and the chip-firing presentation give \(K(\Gamma_i)=\operatorname{coker}(L_i')\), a finite abelian group. The complete source triple arrays, the remaining ordinary pairs, and the construction of every entry of \(L_i'\) are specified in `verify.py`.

**3. Independent determinant certificate.** Delete the twelfth line vertex and put the remaining eleven line vertices first, followed by the nineteen trivalent exceptional vertices. The reduced Laplacian has block form \(\left(\begin{smallmatrix}A&B\\B^{\mathsf T}&3I_{19}\end{smallmatrix}\right)\). Define the integral \(11\times11\) matrix \(H_i=3A-BB^{\mathsf T}\). By Schur complementation,

\[
\det L_i'=3^{19}\det(A-BB^{\mathsf T}/3)=3^8\det H_i.
\]

Fraction-free Bareiss determinants give

\[
\begin{array}{c|rr}
 & \det H_i & \det L_i'\\ \hline
 C_2&721648091136&4734733125943296\\
 C_6&722835456000&4742523426816000\\
 C_7&722835456000&4742523426816000
\end{array}
\]

The prime factorizations of the orders are, respectively,

\[
2^{18}3^9 7^2 61\cdot307,\qquad 2^{14}3^9 5^3 7^6,\qquad 2^{14}3^9 5^3 7^6.
\]

**4. Full integral Smith factors.** For each prime dividing the corresponding determinant, elementary row and column operations over \(\mathbb Z/p^9\mathbb Z\), selecting at each step an entry of least \(p\)-adic valuation, diagonalize the reduced Laplacian through invertible operations. All detected valuations are at most five, so the modulus suffices. The positive valuations (with multiplicity) are:

\[
\begin{array}{c|ccccc}
& p=2&p=3&p=5&p=7&p=61,307\\\hline
C_2&1^8,5^2&1^7,2&-&1^2&1,1\\
C_6&1^8,3^2&1^9&1^3&1^6&-\\
C_7&1^8,3^2&1^9&1^3&1^6&-
\end{array}
\]

Here the notation \(1^8\) in this *valuation table* means eight valuations equal to one, not an invariant factor. Every prime absent from the determinant contributes only zero valuations. Padding each prime-valuation list with zeros to length thirty and aligning them in nondecreasing order gives twenty unit Smith factors and the ten nonunit invariant factors displayed in the finding. The product of the factors equals each independently computed determinant. In addition to the prime-local calculation, exact integer Smith forms with three different deleted vertices produce identical factors.

**5. Spectral and nonisomorphism comparison.** Direct characteristic-polynomial calculation from the complete Laplacians gives the identical factorization for \(C_6\) and \(C_7\) displayed above; \(C_2\) has a different polynomial. The full graph isomorphism enumeration verifies that all three graphs are pairwise nonisomorphic, with respective automorphism-group orders two, twelve, and thirty-six. This agrees with the primary classification of the underlying nonisomorphic line-incidence configurations. In particular, graph and group coincidences are not relabelings of one common arrangement.

## Verification

Run `python3 verify.py` in a Python 3 environment. The checker uses only the standard library for complete graph reconstruction, the independent eleven-dimensional determinants, and the prime-local Smith valuations. If SymPy is installed, it additionally checks the exact Smith normal forms at three different roots, determinant prime factorization, and the Laplacian polynomials; if NetworkX is installed, it also independently enumerates graph isomorphisms and automorphisms. The complete reproducible arrays and intermediate values are also recorded in `certificates/smith_data.json`. The recorded run succeeded with the terminal line `ORCHARD_B12_C2_C7_EXACT_INTEGRAL_COMPONENT_GROUPS_OK` and verified all optional checks.

## Relationship to prior work

Bokowski and Pokora (arXiv:1607.05864, first publicly posted July 20, 2016) provide the complete relevant triple lists, identify \(C_6\) with Böröczky's arrangement, and exhibit real realizations of \(C_2\) and \(C_7\). Farnik, Kabat, Lampa-Baczyńska, and Tutaj-Gasińska (2018) establish that the three arrangements have the same weak combinatorics but distinct incidence structures, and study symbolic-power containment, not these integral critical groups. General work on complexity groups and Raynaud's graph-component correspondence supplies the *interpretation*, not these numerical Smith forms. Published critical-group computations for other line arrangements or for unrelated Levi graphs do not cover the three thirty-one-vertex dual graphs here. This is a best-knowledge priority comparison, not a proof that no earlier unpublished or unindexed Smith-form computation exists.

## Limitations

The statement concerns three particular named complex realizations and their specified reduced boundary curves. Nonisomorphic incidence structures and distinct abstract groups should not be confused with differences in symbolic-power containment, which is a separate invariant. The two matching critical groups do not imply equality of the full Picard schemes or of arithmetic forms. The critical-group computation is unconditional for the graphs; the Néron statement is conditional on a smoothing with the specified regularity and thickness hypotheses. Historical priority and the computational proof have not received independent validation.

## References

- J. Bokowski and P. Pokora, *On the Sylvester–Gallai and the orchard problem for pseudoline arrangements*, arXiv:1607.05864, version 1 posted July 20, 2016; triple lists and realizations in sections 2–4, https://arxiv.org/abs/1607.05864.
- Ł. Farnik, J. Kabat, M. Lampa-Baczyńska, and H. Tutaj-Gasińska, *Containment problem and combinatorics*, Journal of Algebraic Combinatorics 50 (2019), published online September 15, 2018, https://doi.org/10.1007/s10801-018-0838-y.
- S. Busonero, M. Melo, and L. Stoppino, *On the complexity group of stable curves*, arXiv:0808.1529, https://arxiv.org/abs/0808.1529.
- G. Orecchia, *Semi-factorial nodal curves and Néron models of jacobians*, arXiv:1602.03700, https://arxiv.org/abs/1602.03700.
