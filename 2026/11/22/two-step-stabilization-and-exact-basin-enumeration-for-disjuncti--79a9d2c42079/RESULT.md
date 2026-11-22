# Two-step stabilization and exact basin enumeration for disjunctive knowing-whether on finite epistemic grids

## Finding
For integers \(m,n\geq2\), consider the full two-agent epistemic grid \(W=[m]\times[n]\). The first information partition consists of rows, and the second of columns. For every event \(E\subseteq W\), define the disjunctive knowing-whether transformer
\[
T(E)=\bigl(K_1E\cup K_1(W\setminus E)\bigr)\cup\bigl(K_2E\cup K_2(W\setminus E)\bigr),
\]
where \(K_iE\) consists of worlds whose whole agent-\(i\) information cell is contained in \(E\). Write \(R(E)\subseteq[m]\) and \(C(E)\subseteq[n]\) for the monochromatic rows and columns of the Boolean matrix of \(E\), respectively. Put
\[
X_{R,C}=(R\times[n])\cup([m]\times C).
\]
The following statements hold for **every** \(E\):

1. \(T(E)=X_{R(E),C(E)}\), and \(T^3(E)=T^2(E)\). The bound of two rounds is sharp for all \(m,n\ge2\).
2. The fixed-point set, equal to \(\operatorname{im}(T^2)\), is exactly \(\{W\}\) together with \(X_{R,C}\) for every \(\varnothing\ne R\subsetneq[m]\) and \(\varnothing\ne C\subsetneq[n]\). Thus
\[
|\operatorname{im}(T^2)|=1+(2^m-2)(2^n-2).
\]
3. Define the standard positive-degree binary-matrix count, for \(a,b\ge1\), by
\[
H(a,b)=\sum_{i=0}^a\sum_{j=0}^b(-1)^{i+j}\binom ai\binom bj 2^{(a-i)(b-j)}.
\]
Then for each proper nonempty pair \((R,C)\), with \(r=|R|\), \(c=|C|\),
\[
\left|(T^2)^{-1}(X_{R,C})\right|=2H(m-r,n-c).
\]
The remaining fiber has the exact size
\[
\left|(T^2)^{-1}(W)\right|=2^{mn}-2\sum_{r=1}^{m-1}\sum_{c=1}^{n-1}\binom mr\binom nc H(m-r,n-c).
\]
These formulas determine **every** eventual-state multiplicity for uniformly labelled initial events, not only the total number of fixed points.
4. If \(E\) is uniformly random among all \(2^{N^2}\) events on an \(N\times N\) grid, then
\[
\Pr\bigl(T^2(E)\ne W\bigr)=N^2 2^{2-2N}\,(1+o(1))\quad(N\to\infty).
\]
The exceptional non-universal terminal events therefore have a sharp leading rare-event probability.

## Assumptions and scope
The two information relations are the equivalence relations of equal first and equal second coordinates, respectively, on the *full* finite Cartesian product. No extra propositional predicates, probabilities, or restrictions on \(E\) are assumed. A row or column is *monochromatic* if all its cells belong to \(E\) or none does. The notation \(T^k\) refers to repeated application of this one set transformer, not to nested availability of individual agents' modalities. The count \(H(a,b)\) is the number of \(a\)-by-\(b\) Boolean matrices with no all-zero row and no all-zero column; this follows by inclusion–exclusion. \(R\) and \(C\) are labelled subsets, and terminal events are labelled cell subsets.

## Proof
**Step 1 (exact image geometry).** The first knowing-whether disjunct is true at precisely the cells in a monochromatic row; the second at the cells in a monochromatic column. Their union is \(X_{R(E),C(E)}\), establishing the first formula.

**Step 2 (cross dichotomy).** Consider \(X_{R,C}\). If \(R=[m]\) or \(C=[n]\), it is \(W\), and \(T(W)=W\). If both \(R\) and \(C\) are nonempty and proper, then precisely the rows indexed by \(R\) and the columns indexed by \(C\) are monochromatic: each selected one is all ones, while each unselected row and column has a one in its intersection with the other selected coordinate set and a zero outside both sets. Hence \(T(X_{R,C})=X_{R,C}\). Finally, if \(R=\varnothing\) or \(C=\varnothing\), all columns or all rows of the cross are monochromatic, so \(T(X_{R,C})=W\). Thus \(T^2(E)\) is always a fixed point and \(T^3=T^2\). For a two-by-two checkerboard \(E\), no row or column is monochromatic, giving \(T(E)=\varnothing\) and \(T^2(E)=W\); embed a checkerboard-type configuration with no monochromatic rows or columns in arbitrary dimensions by choosing nonconstant rows and columns (for instance, a diagonal one in the leading two rows, with other rows and columns filled to remain nonconstant). The checkerboard case already establishes sharpness uniformly at the level of the frame family; to prove it for each \(m,n\ge2\), use a matrix whose entry is one precisely when its row index and column index have the same parity. Both parities occur in each dimension, so every row and column is nonconstant, yielding the same \(\varnothing\to W\) progression.

**Step 3 (fixed-point classification).** Every fixed point belongs to the image of \(T\), hence is a cross. Step 2 says that the fixed crosses are exactly \(W\) and the proper nonempty crosses. Conversely each listed cross maps to itself, so it belongs to \(\operatorname{im}(T^2)\). The named row/column supports of any proper nonempty cross can be recovered as its full rows and full columns, establishing that the \((2^m-2)(2^n-2)\) proper crosses are pairwise distinct.

**Step 4 (all inverse fibers).** Fix \(\varnothing\ne R\subsetneq[m]\) and \(\varnothing\ne C\subsetneq[n]\). By Step 2, \(T^2(E)=X_{R,C}\) exactly when \(R(E)=R\) and \(C(E)=C\). Every selected monochromatic row meets every selected monochromatic column, so all selected rows and columns necessarily have a *common* bit \(\epsilon\in\{0,1\}\). A nonselected row already has an \(\epsilon\)-entry in a column of \(C\); it is nonmonochromatic exactly when it has at least one \(1-\epsilon\)-entry among the residual columns. The symmetric statement holds for nonselected columns. Thus, after choosing \(\epsilon\) (two options), the complementary-bit positions in the residual \((m-r)\times(n-c)\) rectangle form an arbitrary Boolean matrix with no zero row or column. The number of such matrices is \(H(m-r,n-c)\), proved from inclusion–exclusion over zero rows and columns. This gives the first fiber formula. All other initial events map to \(W\), so subtracting the disjoint proper-cross fibers from the \(2^{mn}\) inputs gives the second formula.

**Step 5 (sharp random rate).** Let \(A_{ij}\) be the event that row \(i\) and column \(j\) of a uniformly random \(N\times N\) binary matrix are both monochromatic. Their common cell forces a common bit, so \(\Pr(A_{ij})=2^{2-2N}\). There are \(N^2\) such events. For two distinct pairs, the joint probability is \(2^{3-3N}\) if they share one row or column, and \(2^{5-4N}\) if their rows and columns are both distinct. There are \(O(N^3)\) and \(O(N^4)\) such unordered pairs, respectively, so Bonferroni gives
\[
\Pr\!\left(\bigcup_{i,j}A_{ij}\right)=N^2 2^{2-2N}+O(N^3 2^{3-3N}+N^4 2^{5-4N}).
\]
By Steps 2–3, \(T^2(E)\ne W\) means there exists a monochromatic row and column, but neither is the entire coordinate set. The only matrices with a monochromatic row and column *and* all rows or all columns monochromatic are the two constant matrices: a selected monochromatic column enforces the same bit in every row, or symmetrically. The difference from the union probability is exactly \(2^{1-N^2}\), which is lower-order. This proves the asserted equivalent.

## Verification
The standalone `verify.py` enumerates all Boolean events on the grids \(1\times5\), \(2\times2\), \(2\times3\), \(3\times3\), \(3\times4\), \(4\times3\), \(2\times5\), and \(5\times2\). Independently from the closed formulas it evaluates modal semantics using row and column bit masks, iterates the operator, checks \(T^3=T^2\), confirms the stated fixed-point structure, and groups initial events by their terminal state. It compares every grouped fiber with the inclusion–exclusion formula for \(H(a,b)\), verifies normalization to \(2^{mn}\), and checks the pair-event joint counts for squares through side four. A successful run prints `VERIFY_OK`. This finite test does not substitute for the arbitrary-dimension argument in the Proof.

## Relationship to prior work
Ding and Yang, *A General Theory of Propositional Modal Bundled Modalities* (arXiv:2603.26268, March 27, 2026), establishes the semantic and axiomatic framework for bundled modalities, and studies the different connective \(\bigvee_iK_i\varphi\) in its case studies. Fan, Wang and van Ditmarsch, *Knowing Whether* (arXiv:1312.0144), establishes the individual non-contingency modality. Fan, Grossi, Kooi, Su and Verbrugge, *Commonly Knowing Whether* (arXiv:2001.03945), investigates several **iterated everyone-knows-whether conjunctions**, rather than the present disjunction and its finite-grid inverse-fiber distribution. The recent *Exact eight-type algebra and sharp three-column cutoff for disjunctive knowing-whether on two-row epistemic grids* studies the **entire Boolean formula algebra** over a fixed two-row frame, varying one proposition's valuation; it proves a depth-two syntax cutoff but not this full-dimension set-transformer fixed-point/fiber law, and it does not imply the present count for arbitrary row dimensions. In contrast, the present theorem classifies the eventual behavior of repeatedly applying one operator to *individual events*, including the exact number of initial events flowing to every fixed event. The standard formula for \(H(a,b)\) is reused combinatorial background and is not claimed as new.

## Limitations
The claims concern only full two-dimensional product frames with the particular disjunction of two knowing-whether operations; nonfull incidence graphs, three or more agents, and arbitrary sequences of Boolean connectives are outside scope. The asymptotic concerns square grids and unbiased independent atomic valuations. Exact historical priority is not independently certified; a possible equivalent older matrix-dynamical formulation remains a residual literature risk. Only the finite portions are checked by executable enumeration; all-dimensional statements rely on the written proof.

## References
1. Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268, first public version March 27, 2026. https://arxiv.org/abs/2603.26268
2. J. Fan, Y. Wang, and H. van Ditmarsch, *Knowing Whether*, arXiv:1312.0144, first public version November 30, 2013. https://arxiv.org/abs/1312.0144
3. J. Fan, D. Grossi, B. Kooi, X. Su, and R. Verbrugge, *Commonly Knowing Whether*, arXiv:2001.03945, first public version January 12, 2020. https://arxiv.org/abs/2001.03945
4. *Exact eight-type algebra and sharp three-column cutoff for disjunctive knowing-whether on two-row epistemic grids* (2026); distinct prior Boolean formula-algebra classification.
5. Standard inclusion–exclusion formula for zero-free Boolean incidence matrices; see P. Cameron, T. Prellberg, and D. Stark, *Asymptotics for incidence matrix classes*, arXiv:math/0510155 (2005). https://arxiv.org/abs/math/0510155
