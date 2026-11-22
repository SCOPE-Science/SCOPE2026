# Sharp capacity and rigidity of \(3\times3\) cross-bibifix-free matrix codes

## Finding
Let \(q\ge2\) be an integer and \(\Sigma\) a labeled alphabet of \(q\) symbols. A code \(\mathcal C\subseteq\Sigma^{3\times3}\) is *cross-bibifix-free* if, for every ordered pair \(X,Y\in\mathcal C\), including \(X=Y\), the top-left and bottom-right \(r\times r\) submatrices are unequal for both proper sizes \(r=1,2\). Write \(M(q)\) for its maximum cardinality and put \(b_q=\lfloor(q+1)/3\rfloor\). Then

\[
M(q)=q^6 b_q(q-b_q)^2.
\]

This is a sharp upper bound without restricting codewords to have prescribed diagonals or assuming any lifted one-dimensional construction. For every \(q\ge3\), all maximum codes, on the labeled alphabet, have exactly one of two forms. Choose an unordered bipartition \(\Sigma=U\sqcup V\) with \(|V|=b_q\) and \(|U|=q-b_q\); the two codes consist of *all* matrices satisfying, respectively,

\[
(X_{11},X_{22},X_{33})\in U\times U\times V
\quad\text{or}\quad
(X_{11},X_{22},X_{33})\in V\times U\times U,
\]

with all six off-diagonal entries unrestricted. Here the bipartition is uniquely recovered by the corner-symbol sets of each displayed code. The number of labeled maximum codebooks is exactly \(2\binom q{b_q}\) for \(q\ge3\).

For \(q=2\), there are exactly \(32\) labeled maximum codebooks of size \(64\), of which exactly four are complete unrestricted-off-diagonal lifts of one-dimensional diagonal codebooks. The other \(28\) are described explicitly by four independent binary choices in the proof.

The first few pairs \((q,M(q),\#\text{maximum codebooks})\) are \((2,64,32)\), \((3,2916,6)\), \((4,36864,8)\), \((5,281250,20)\), and \((6,1492992,30)\).

## Assumptions and scope
All matrices are indexed by row and column positions \(1,2,3\). A biprefix \(P_r(X)\) is the top-left \(r\times r\) square of \(X\); a bisuffix \(S_r(X)\) is the bottom-right \(r\times r\) square. The requirement is \(P_r(X)\ne S_r(Y)\) for every \(X,Y\in\mathcal C\) and \(r\in\{1,2\}\). It forbids *diagonal square* overlaps; it does not purport to forbid translations in every direction, the stronger two-dimensional non-overlap convention used elsewhere. The empty code is allowed but never maximizes when \(q\ge2\).

## Proof
**1. Corner separation.** Let \(A=\{X_{11}:X\in\mathcal C\}\) and \(B=\{X_{33}:X\in\mathcal C\}\), with cardinalities \(a,b\). The size-one condition gives \(A\cap B=\varnothing\). For nonempty \(\mathcal C\), both \(a,b\ge1\) and \(a+b\le q\). Every matrix in the code has its top-left corner in \(A\) and bottom-right corner in \(B\). We upper-bound the code by considering *every* matrix with these corner restrictions.

**2. Exact conflict decomposition.** Call the center entry \(X_{22}\). An equality \(P_2(X)=S_2(Y)\) requires \(X_{11}=Y_{22}\in A\) and \(X_{22}=Y_{33}\in B\). Thus any matrix whose center lies outside \(A\cup B\) conflicts with no other eligible matrix; there are exactly \(ab(q-a-b)q^6\) such matrices.

For each \((\alpha,\beta,u,v)\in A\times B\times\Sigma^2\), form two sets of eligible matrices:

\[
\begin{aligned}
L_{\alpha,\beta,u,v}&=\{X:X_{11}=\alpha,\ X_{22}=\beta,\ X_{12}=u,\ X_{21}=v,\ X_{33}\in B\},\\
R_{\alpha,\beta,u,v}&=\{Y:Y_{22}=\alpha,\ Y_{33}=\beta,\ Y_{23}=u,\ Y_{32}=v,\ Y_{11}\in A\}.
\end{aligned}
\]

The four other unspecified entries in each set are arbitrary. Consequently \(|L_{\alpha,\beta,u,v}|=bq^4\) and \(|R_{\alpha,\beta,u,v}|=aq^4\). Every matrix whose center belongs to \(B\) lies in exactly one \(L\), and every matrix whose center belongs to \(A\) in exactly one \(R\). Because \(A\cap B=\varnothing\), these sets partition all non-neutral eligible matrices. Every matrix in one \(L\) conflicts with every matrix in its paired \(R\), and there are no other size-two conflicts. Hence the entire conflict graph is the disjoint union of \(abq^2\) complete bipartite graphs \(K_{bq^4,aq^4}\) and \(ab(q-a-b)q^6\) isolated vertices.

**3. Fixed corner sets and alphabet optimization.** A cross-bibifix-free code is an independent set in this graph. Each complete bipartite component has independence number \(\max(a,b)q^4\), attained by taking the entire larger part; if the part sizes are equal, one can take either entire side. All isolated vertices belong to every maximum independent set. Therefore the exact maximum with the *allowed* corner sets \(A,B\) is

\[
F_q(a,b)=ab(q-a-b)q^6+abq^2\max(a,b)q^4
=ab\bigl(q-\min(a,b)\bigr)q^6.
\]

Assume by symmetry \(a\ge b\). Since \(a\le q-b\),
\[
F_q(a,b)\le b(q-b)^2q^6,
\]
with equality only for \(a=q-b\). The real function \(t(q-t)^2\) is increasing until \(q/3\) and decreasing thereafter on the relevant interval. Comparing its two neighboring integer values shows the unique integer maximizer for \(1\le t\le\lfloor q/2\rfloor\) is \(b_q=\lfloor(q+1)/3\rfloor\): for \(q=3m+1\), \(g(m)-g(m+1)=m>0\); for \(q=3m+2\), \(g(m+1)-g(m)=m+1>0\); and for \(q=3m\), the maximum is \(m\). This proves the displayed capacity formula.

**4. Equality cases.** If \(q\ge3\), then \(b_q<q-b_q\), so every component has a strictly larger side. Equality forces both corner sets to partition the alphabet, their smaller size to be \(b_q\), and the larger side of *every* component to be included, together with all isolated vertices (none remain because the corner sets partition \(\Sigma\)). This gives precisely the two diagonal forms displayed in the finding and their count \(2\binom q{b_q}\). The two orientations are distinct, and different partitions give different observed corner sets.

If \(q=2\), the only corner-set choices are the two singleton orientations. Each orientation has four components \(K_{16,16}\) indexed by \((u,v)\in\Sigma^2\), with no neutral matrices. Each component independently contributes exactly one of its two full sides to an optimum, yielding \(2\cdot2^4=32\) distinct maximum codes. Of those, the all-left and all-right choices in each orientation are the only diagonal-cylinder lifts, two per orientation, hence four in total and 28 non-lifts. This proves the binary classification as well.

## Verification
The included `check_binary_optima.py` directly enumerates all \(512\) binary matrices, constructs overlap edges from the literal \(2\times2\) corners, identifies four \(K_{16,16}\) components in each corner orientation, and verifies all \(32\) optimal codebooks individually. The separate `check_milp.py` independently solves the two \(128\)-vertex conflict graphs as integer programs (each has \(1024\) edges) and obtains the optimum \(64\) in each orientation. The `check_exhaustive.py` script enumerates candidate matrices for several fixed corner-set configurations at \(q=2,3,4\), checks the exact component sizes and explicit full-code validity, and checks the unique integer maximizer for \(2\le q\le500\).

To reproduce with Python 3 and SciPy installed, run the three standalone scripts, for example `python check_binary_optima.py`, `python check_milp.py`, and `python check_exhaustive.py`. All passed in the packaged execution. The proof is valid for every integer \(q\ge2\) without assuming exhaustive computation for unbounded \(q\).

## Relationship to prior work
Chee, Kiah, Purkayastha, and Wang (2012/2013) construct cross-bifix-free codes over alphabets of arbitrary size. Blackburn (2013), Theorem 5, determines the exact length-three one-dimensional capacity: \(C(3,q)=b_q(q-b_q)^2\). Barcucci, Bernini, Bilotta, and Pinzani (2015), Section 4 and Proposition 4.2, show that filling all off-diagonal matrix entries above a one-dimensional cross-bifix-free diagonal code gives a cross-bibifix-free matrix code. Together these results give the **lower bound** \(M(q)\ge q^6 C(3,q)\). They do not establish the reverse inequality for arbitrary matrix codebooks, nor enumerate its equality cases: off-diagonal entries can prevent a square collision even when the projected diagonal words overlap. The present complete-bipartite decomposition proves the missing upper bound and classifies equality, including the \(28\) binary non-lift optima.

The stronger notion of non-overlapping matrices under every translation, studied by Barcucci and collaborators in later work, is not equivalent to the diagonal-square-only definition used here, so a construction for that stricter model does not give this exact extremal classification.

## Limitations
The result concerns only \(3\times3\) square matrices and only top-left/bottom-right proper square overlaps of sizes one and two. It is not a statement about arbitrary displaced row/column overlaps, noise tolerance, or higher matrix dimensions. No independent mathematical audit has been carried out. A historical equivalent reformulation, particularly one expressed through bipartite conflict graphs rather than cross-bibifixes, may exist outside the inspected sources; the claimed novelty is limited to the exact two-dimensional upper bound and equality classification, not Blackburn's known one-dimensional capacity or the previously known matrix lifting construction.

## References
- Y. M. Chee, H. M. Kiah, P. Purkayastha, and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, first posted 2012-09-03, especially Sections 2–3. https://arxiv.org/abs/1209.0236
- S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first posted 2013-03-05, especially Section 4, Theorem 5. https://arxiv.org/abs/1303.1026
- E. Barcucci, A. Bernini, S. Bilotta, and R. Pinzani, *Cross-bifix-free sets in two dimensions*, arXiv:1502.05275, first posted 2015-02-18, especially Definitions 2.1, 3.3–3.4 and Section 4, Proposition 4.2. https://arxiv.org/abs/1502.05275
- E. Barcucci, A. Bernini, S. Bilotta, and R. Pinzani, *Non-overlapping matrices*, arXiv:1601.07723, first posted 2016-01-28 (a different, stronger overlap convention). https://arxiv.org/abs/1601.07723
