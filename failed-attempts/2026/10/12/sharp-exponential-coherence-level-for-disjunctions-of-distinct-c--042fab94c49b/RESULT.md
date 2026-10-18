# Sharp exponential coherence level for disjunctions of distinct constancy atoms

## Finding
For every integer \(r\ge 1\), let \(\Phi_r=\mathrm{dep}(x_1)\vee\cdots\vee\mathrm{dep}(x_r)\) where the variables are pairwise distinct, \(\mathrm{dep}(x_i)\) says the value of \(x_i\) is constant throughout a team, and \(\vee\) is lax split disjunction. The **exact coherence level** of \(\Phi_r\) is \(2^r\), over all structures, with finite or infinite teams. More explicitly, for every team \(T\),
\[
T\models\Phi_r \quad\Longleftrightarrow\quad
\text{every }S\subseteq T\text{ with }|S|\le 2^r\text{ satisfies }\Phi_r.
\]
No smaller nonnegative threshold has this equivalence for all teams. This is equivalent to the sharp finite-obstruction statement for covering a subset of \(D^r\) by at most one coordinate hyperplane \(\{t:t_i=a_i\}\) in each coordinate \(i\).

## Assumptions and scope
The result assumes a standard nonempty first-order domain \(D\), pairwise distinct variables, and standard *lax* team semantics. Assignments can carry additional variables; locality reduces them to the displayed \(r\) coordinates. A constancy atom is true of a subteam precisely when all its assignments agree on its coordinate (also true on the empty team). A disjunction is satisfied when the team is a union of subteams satisfying the respective disjuncts; overlap is allowed. The theorem imposes **no cardinality bound** on \(D\) or the team. In the usual definition, \(k\)-coherence checks all subteams having exactly \(k\) members. The at-most formulation above is equivalent here because every team of cardinality smaller than \(2^r\) is shown to satisfy the formula, and the formula is downward closed.

For a tuple set \(T\subseteq D^r\), call a selector \(a=(a_1,\dots,a_r)\in D^r\) a *cover* when each \(t\in T\) has \(t_i=a_i\) for at least one \(i\). If \(T\) is empty, it has a cover for any choice of selector. Lax splitting gives the elementary equivalence
\[
T\models\Phi_r\quad\Longleftrightarrow\quad
\exists a\in D^r\ \forall t\in T\ \exists i\in\{1,\dots,r\}:t_i=a_i.
\]
Indeed, select the constant coordinate values from the disjunct subteams (choosing arbitrary values if a subteam is empty), and conversely assign each row to any one matching disjunct. This equivalence fixes the semantic reduction used below.

## Proof
**Step 1 — every failure has a finite failing subteam.** Prove this by induction on the number \(r\) of coordinates, temporarily allowing \(r=0\). With no coordinates, every nonempty tuple set is noncoverable, and any singleton is a finite failure. Suppose \(r\ge1\) and \(T\subseteq D^r\) has no selector cover. Pick \(t^0\in T\). For each coordinate \(j\), let \(T_j\) comprise the projections to the other \(r-1\) coordinates of those \(t\in T\) with \(t_j\ne t^0_j\). If some \(T_j\) were coverable using its \(r-1\) coordinates, setting \(a_j=t^0_j\) would cover the remaining rows of \(T\), a contradiction. Thus each \(T_j\) is noncoverable. By induction choose a finite noncoverable subset of each \(T_j\), and lift its tuples to finitely many original rows of \(T\) with \(t_j\ne t^0_j\). Together with \(t^0\), these form a finite noncoverable subteam: any putative cover must match \(t^0\) in some coordinate \(j\), after which the lifted rows for \(T_j\) would have to be covered entirely through the other coordinates, contradicting their selection. This proves the assertion even for infinite \(T\).

**Step 2 — a multilinear upper bound for minimal failures.** Let \(U\) be an inclusion-minimal finite noncoverable tuple set. For each \(u\in U\), let \(a^{(u)}\in D^r\) cover \(U\setminus\{u\}\). Because \(U\) itself is not coverable, no coordinate of this selector equals the corresponding coordinate of \(u\). The total set of values occurring among the finitely many tuples \(u\) and selectors \(a^{(u)}\) is finite; choose an injection \(\iota\) from those symbols into \(\mathbb Q\).

For each \(t\in U\), define
\[
P_t(Z_1,\ldots,Z_r)=\prod_{i=1}^{r}\bigl(Z_i-\iota(t_i)\bigr)\in\mathbb Q[Z_1,\ldots,Z_r].
\]
Every \(P_t\) is multilinear (degree at most one in each variable). At the evaluation point \(\iota(a^{(u)})\), we have \(P_t(\iota(a^{(u)}))=0\) when \(t\ne u\), because selector \(a^{(u)}\) covers \(t\), whereas \(P_u(\iota(a^{(u)}))\ne0\), since that selector misses \(u\) in every coordinate. Therefore the evaluation matrix with rows indexed by \(u\) and columns indexed by \(t\) is diagonal with nonzero diagonal. The polynomials \(\{P_t:t\in U\}\) are linearly independent over \(\mathbb Q\). But all multilinear polynomials in \(r\) variables belong to the \(2^r\)-dimensional span of the squarefree monomials. Hence \(|U|\le 2^r\). Step 1 now gives a noncoverable subteam with at most \(2^r\) members whenever the original team fails the formula. Downward closure supplies the opposite implication.

**Step 3 — sharpness for every \(r\).** Take the full binary cube \(U_r=\{0,1\}^r\). Given any selector \(a\), choose \(u_i=1\) if \(a_i=0\), and \(u_i=0\) otherwise. Then \(u_i\ne a_i\) for every \(i\), so no selector covers \(U_r\). On deleting any cube vertex \(u\), choose \(a_i=1-u_i\) in every coordinate. Every other binary vertex has some coordinate different from \(u_i\), hence matches the selector; thus \(U_r\setminus\{u\}\) is coverable. All proper subsets of the cube are therefore coverable. Every threshold smaller than \(2^r\) falsely accepts the full cube, proving exactness.

## Verification
The standalone `verify.py` requires only Python's standard library. Run `python verify.py` in the directory containing this document and the checker. It independently enumerates all teams over binary carriers for \(r=1,2,3,4\) and ternary carriers for \(r=1,2\): **66,332** team masks in total. It checks the cover condition by exhaustive selector enumeration and verifies that every inclusion-minimal finite failure has cardinality at most \(2^r\). It also verifies that every binary cube is minimally noncoverable for \(r=1,2,3,4\), and over \(\mathbb Q\) calculates the full rank \(2^r\) of the corresponding multilinear-coefficient matrices. An additional seeded sample of 12,000 ternary three-coordinate teams checks minimal failures against the same bound. The complete universal theorem, especially its infinite-team case, follows from the proof above, **not** from finite sampling.

## Relationship to prior work
Fröhlich, Kolaitis and Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146, Corollary 23, establishes the \(r=2\) special case: \(\mathrm{dep}(y)\vee\mathrm{dep}(z)\) has coherence level four. Their Section 4 and higher-arity Section 5 study exactly **two** disjuncts and do not state the arbitrary-number-of-distinct-constancy-atoms sharp formula proved here. The case \(r=2\) is acknowledged as prior coverage, not asserted to be new. Kontinen introduced coherence and the relation to tractable model checking. Barlag et al., *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269 (abstract examined), establish broad links between first-order rewritability and existence of some coherence threshold for quantifier-free dependence logic; their publicly inspected abstract does not give this exact family of thresholds. The independent geometric reformulation can be compared with polynomial-method results on coordinate or Boolean hyperplanes, but Alon–Füredi-type cube *hyperplane-covering numbers* are different from the present minimum size of a team not coverable by one coordinate slice in each direction.

## Limitations
The result treats only disjunctions of constancy atoms on pairwise distinct variables, with lax disjunction. It does not classify arbitrary disjunctions of functional-dependence atoms, strict-splitting interpretations, or the isomorphism types of all minimal bad teams. General algebraic hyperplane-covering methods might imply a formulation of the bound under other terminology. The full text of the 2026 paper *Aspects of Coherence in Dependence Logic* was not retrievable through the open preprint endpoints checked; its abstract, rather than every theorem, was inspected, leaving a documented prior-coverage risk. No independent review is claimed.

## References
1. Nicolas Fröhlich, Phokion G. Kolaitis, Arne Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146 (first public 2025-08-22); CSL 2026, LIPIcs 363, paper 10, DOI:10.4230/LIPIcs.CSL.2026.10. Original HTML: https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html.
2. Timon Barlag et al., *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269 (2026-05-29); full text unavailable during the stated comparison, abstract consulted.
3. Jarmo Kontinen, *Coherence and computational complexity of quantifier-free dependence logic formulas*, Studia Logica 101 (2013), 267–291, DOI:10.1007/s11225-013-9481-8.
4. S. Venkitesh, *Covering Symmetric Sets of the Boolean Cube by Affine Hyperplanes*, Electronic Journal of Combinatorics 29(2) (2022), article P2.22, DOI:10.37236/10600 (related polynomial covering context, distinct claim).
