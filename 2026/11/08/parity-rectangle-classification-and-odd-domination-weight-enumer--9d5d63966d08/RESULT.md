# Parity-rectangle classification and odd-domination weight enumerator of rectangular rook graphs

## Finding

For every pair of integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph with labelled cells \((i,j)\). An *odd-dominating set* \(S\) meets the closed neighborhood of **every** cell in an odd number of cells. Let
\[
W_{m,n}(z)=\sum_{S\,\mathrm{odd\!\!-dominating}}z^{|S|}.
\]
Every such set has the following complete classification, with no repetitions:

* If \(m,n\) are both even, the entire board is the only solution, and \(W_{m,n}(z)=z^{mn}\).
* If \(m\) is even and \(n\) odd, the solutions are unions of an **odd number of complete rows**. Consequently
  \[
  W_{m,n}(z)=\sum_{\substack{1\le a\le m\\a\text{ odd}}}\binom ma z^{an}.
  \]
* If \(m\) is odd and \(n\) even, the solutions are unions of an **odd number of complete columns**, with
  \[
  W_{m,n}(z)=\sum_{\substack{1\le b\le n\\b\text{ odd}}}\binom nb z^{bm}.
  \]
* If \(m,n\) are both odd, select any odd-cardinality row set \(A\subseteq[m]\) and odd-cardinality column set \(B\subseteq[n]\). The solution is exactly the union of the two diagonal rectangles \((A\times B)\cup(A^c\times B^c)\); each solution has a **unique** such pair \((A,B)\). Therefore
  \[
  W_{m,n}(z)=\sum_{\substack{1\le a\le m\\a\text{ odd}}}\ \sum_{\substack{1\le b\le n\\b\text{ odd}}}\binom ma\binom nb\,z^{ab+(m-a)(n-b)}.
  \]

The total numbers of solutions in the four cases are respectively \(1\), \(2^{m-1}\), \(2^{n-1}\), and \(2^{m+n-2}\). The least possible cardinality is exactly
\[
\gamma_{\mathrm{odd}}(R_{m,n})=\begin{cases}
mn,&m,n\text{ both even},\\
n,&m\text{ even},\ n\text{ odd},\\
m,&m\text{ odd},\ n\text{ even},\\
\min(m,n),&m,n\text{ both odd}.
\end{cases}
\]
Every minimum set is, respectively: the entire board; one full row; one full column; or one full row or column of the shorter length. In the odd--odd case the number of minimum sets is \(n\) when \(m<n\), \(m\) when \(n<m\), and \(2m\) when \(m=n\). In the even--odd and odd--even cases the minimum counts are \(m\) and \(n\), respectively; in the even--even case it is \(1\).

## Assumptions and scope

All graphs are simple, finite, and labelled, and \(m,n\) range independently over integers at least two. Distinct cells are adjacent precisely when they share exactly one coordinate. A closed neighborhood includes its center. Parities and all matrix operations are taken over \(\mathbb F_2\). The enumerator counts subsets of cells, not configurations up to graph automorphism. For the standard closed-neighborhood binary Lights Out rule, the same polynomial counts sets of buttons pressed an odd number of times that turn the all-on board off. Open-neighborhood and nonbinary switching are not covered.

## Proof

Let \(x_{ij}\in\mathbb F_2\) indicate whether \((i,j)\in S\), and define its row and column parity sums by \(r_i=\sum_jx_{ij}\), \(c_j=\sum_ix_{ij}\). The parity of \(S\) in the closed neighborhood of \((i,j)\) is \(r_i+c_j+x_{ij}\), because the center occurs twice in the row-plus-column sum but only once in the closed neighborhood, and subtraction equals addition in characteristic two. Hence \(S\) is odd-dominating **if and only if**
\[
 x_{ij}=1+r_i+c_j\qquad(1\le i\le m,\ 1\le j\le n).
\]
Set \(T=\sum_i r_i=\sum_jc_j\). Summing the displayed equations over a row and over a column gives, in \(\mathbb F_2\),
\[
 (n+1)r_i=n+T,\qquad (m+1)c_j=m+T.
\]
These are necessary and, together with the original equations, sufficient for the following exact cases.

If both side lengths are even, every \(r_i\) and \(c_j\) equals \(T\). Summing all rows shows \(T=mT=0\), so all row and column sums vanish, and \(x_{ij}=1\) throughout. This full board is indeed feasible because every closed neighborhood has \(m+n-1\) cells, an odd number.

If \(m\) is even and \(n\) odd, the row equation forces \(T=1\), and the column equation then forces \(c_j=1\) for every \(j\). Thus \(x_{ij}=r_i\) is constant along each row, with \(\sum_i r_i=1\); conversely any odd selection of complete rows satisfies the equations. The opposite parity arrangement gives exactly odd unions of complete columns.

If both side lengths are odd, both displayed equations reduce to \(T=1\). Thus \(r=(r_i)\) and \(c=(c_j)\) must each have odd total parity, while \(x_{ij}=1+r_i+c_j\). Conversely, for **any** two odd-parity vectors \(r,c\), this formula produces a board whose computed row and column parities are exactly \(r,c\). Consequently the parameters are unique, and the selected cells are those for which \(r_i=c_j\), namely \((A\times B)\cup(A^c\times B^c)\) where \(A=\{i:r_i=1\}\), \(B=\{j:c_j=1\}\). This proves all four classifications; counting the possible row and column choices at each weight yields the displayed polynomials and total counts.

For completeness, determine the minimum in the odd--odd case. For odd \(a,b\) with \(1\le a\le m\), \(1\le b\le n\), the weight is \(w(a,b)=ab+(m-a)(n-b)\), linear in \(a\) with slope \(2b-n\). Because \(n\) is odd, this slope is never zero. If \(2b<n\), the minimum over admissible \(a\) occurs at \(a=m\), giving \(mb\ge m\), with equality only for \(b=1\). If \(2b>n\), it occurs at \(a=1\), yielding \(n+(m-2)(n-b)\ge n\), with equality only for \(b=n\) since \(m\ge3\). This establishes the claimed minimum and characterizes exactly all minimizers, including the equal-side case. The other three parity cases follow immediately from their all-row/all-column descriptions.

## Verification

Two dependency-free Python programs provide distinct finite checks. The first independently examines every binary subset of \(m\times n\) boards with \(2\le m,n\le4\), testing every closed-neighborhood parity directly. The second constructs the closed-neighborhood linear system over \(\mathbb F_2\), performs Gauss--Jordan elimination, enumerates all affine solutions, and compares their **complete weight histograms** against the formula for \(2\le m,n\le7\). Both programs were executed successfully; their exact outputs are included alongside them. The infinite-parametric theorem is proved algebraically above, not inferred from finite tests.

Run \(\texttt{python3 check_binary.py}\) and \(\texttt{python3 check_linear.py}\) from the directory containing the files; no third-party packages are needed. For example, the polynomial on the \(3\times3\) rook board is \(6z^3+9z^5+z^9\), and on the \(5\times5\) rook board it is \(10z^5+100z^{11}+100z^{13}+20z^{15}+25z^{17}+z^{25}\). The independent solvers reproduce both exactly.

## Relationship to prior work

Giffen and Parker (2013) relate Lights Out switching to parity domination over finite rings and analyze paths, cycles, complete bipartite graphs, and caterpillars. Their complete-bipartite host \(K_{m,n}\) is **not** its line graph \(L(K_{m,n})=K_m\square K_n\), the rook graph treated here. The 2013 article's entire sixteen-page published PDF was inspected; its statements do not give this board's complete solution families or their weight enumerators.

Peters, Goldwasser, and Young (2017) study universal solvability for Cartesian products. Their accessible abstract concerns the invertibility/solvability of switching operators, a coarser invariant than the complete distribution of weights of solutions to one fixed target. Their complete text could not be inspected, so unrecognized overlapping special cases remain a limitation. Berman, Borer, and Hungerbühler (2021) survey the binary linear-algebra framework and solvability, explicitly distinguishing finding *some* solution from minimizing the number of presses. Their accessible full-text presentation does not give the four-case rook-board weight enumerator.

A pre-existing published Hamming-product Lights Out nullity formula already determines the *total number* of all-on solution patterns and covers the four total counts above; these totals are **not claimed as independently new**. Exact nullity alone does not specify the weight distribution, the two-rectangle parameterization, or the full characterization and multiplicities of minimum-cardinality press patterns, which are the specific contributions here. Ordinary rook domination and rook graph homology involve different conditions and do not imply the result.

## Limitations

The theorem applies only to binary closed-neighborhood parity domination on two-factor rectangular rook graphs. It does not yield a weight enumerator for arbitrary starting configurations, higher-dimensional Hamming graphs, or general graph products. Neither independent scholarly validation nor a complete historical-priority census has been performed; the full text of the 2017 Cartesian-products paper was inaccessible. No originality claim is made for the general matrix formulation, all-on solvability, or the previously known solution-space dimension.

## References

1. A. Giffen and D. B. Parker, “On Generalizing the ‘Lights Out’ Game and a Generalization of Parity Domination,” *Ars Combinatoria* **111** (2013), 273–288, published 2013-07-31. https://combinatorialpress.com/ars-articles/volume-111-ars-articles/on-generalizing-the-lights-out-game-and-a-generalization-of-parity-domination/
2. T. Peters, J. Goldwasser, and M. Young, “LIGHTS OUT! on Cartesian Products,” *Electronic Journal of Linear Algebra* **32** (2017), 464–474, DOI: 10.13001/1081-3810.3483. https://journals.uwyo.edu/index.php/ela/article/view/1801
3. A. Berman, F. Borer, and N. Hungerbühler, “Lights Out on graphs,” *Mathematische Semesterberichte* **68** (2021), 237–255, DOI: 10.1007/s00591-021-00297-5. https://link.springer.com/article/10.1007/s00591-021-00297-5
4. E. W. Weisstein, “Rook Graph,” *MathWorld*, https://mathworld.wolfram.com/RookGraph.html (graph nomenclature and identification with \(L(K_{m,n})\)).
