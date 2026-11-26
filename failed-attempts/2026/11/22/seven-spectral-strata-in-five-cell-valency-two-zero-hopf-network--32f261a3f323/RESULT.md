# Seven spectral strata in five-cell valency-two zero–Hopf networks

## Finding

There are exactly **191 isomorphism classes** of connected five-cell regular directed multigraph networks of valency two whose adjacency matrix has simple eigenvalues \(2\), \(0\), and one nonzero purely imaginary conjugate pair, with no other eigenvalues on the imaginary axis. Precisely **56** of these classes are strongly connected. Their complete characteristic-polynomial strata are

\[
\chi_A(z)=(z-2)z(z-r)(z^2+q),
\qquad (r,q)\in\{(-2,1),(-2,2),(-2,3),(-2,4),(-1,1),(-1,2),(1,1)\}.
\]

| \(r\) | \(q\) | Labeled matrices | Isomorphism classes | Strongly connected labeled | Strongly connected classes |
|---:|---:|---:|---:|---:|---:|
| -2 | 1 | 1800 | 15 | 600 | 5 |
| -2 | 2 | 1620 | 15 | 420 | 5 |
| -2 | 3 | 120 | 1 | 120 | 1 |
| -2 | 4 | 360 | 4 | 60 | 1 |
| -1 | 1 | 7620 | 66 | 3420 | 29 |
| -1 | 2 | 3540 | 30 | 1140 | 10 |
| 1 | 1 | 6900 | 60 | 540 | 5 |
| **Total** | | **21960** | **191** | **6300** | **56** |

The higher-frequency strata \(q=3\) and \(q=4\) first occur at five cells for valency two: they comprise exactly five isomorphism classes, all having the additional real eigenvalue \(-2\). Of these five, exactly two classes are strongly connected. Each of the seven displayed spectral strata is realized. No other stratum occurs under the stated conditions.

## Assumptions and scope

A network has exactly five *labeled* cells, a single cell type and a single arrow type; loops and parallel directed arrows are allowed. Its adjacency matrix \(A=(a_{ij})\) has nonnegative integer entries \(a_{ij}\), the number of arrows from cell \(j\) to cell \(i\), with every row summing to two. The underlying undirected support is connected if every pair is joined by an undirected path; strong connectivity uses directed paths. Two matrices represent isomorphic networks precisely when \(B=PAP^{-1}\) for a permutation matrix \(P\). A zero–Hopf network here means the definition of Aguiar–Dias–Mokhtari: \(2\), \(0\), and \(\pm i\omega\) are simple eigenvalues with \(\omega>0\), and there are no other eigenvalues on the imaginary axis. This is a graph-spectral classification, not a claim that every nonlinear admissible vector field undergoes a nondegenerate zero–Hopf bifurcation.

## Proof

**1. The complete list of possible spectral factors is finite.** The row sum gives the eigenvalue \(2\). Since \(A\) is real and has five eigenvalues counting multiplicity, the remaining eigenvalue after \(2,0,\pm i\omega\) is a real number \(r\). Its trace relation yields \(r=\operatorname{tr}A-2\in\mathbb Z\). All eigenvalues satisfy \(|z|\le 2\) by the induced infinity norm; simplicity excludes \(r=0,2\), hence \(r\in\{-2,-1,1\}\). Division of the monic integral characteristic polynomial by the monic integer polynomial \((z-2)z(z-r)\) leaves \(z^2+q\in\mathbb Z[z]\), with \(q=\omega^2\in\{1,2,3,4\}\). Moreover, traces of powers satisfy

\[
\operatorname{tr}(A^2)=4+r^2-2q,
\quad\operatorname{tr}(A^3)=8+r^3,
\quad\operatorname{tr}(A^4)=16+r^4+2q^2,
\quad\operatorname{tr}(A^5)=32+r^5.
\]

**2. Exact exhaustive decision.** Each row is a multiset of two incoming arrows from five possible cells. There are exactly \(\binom{6}{2}=15\) possibilities, so every labeled network appears exactly once among \(15^5=759375\) ordered choices of rows. For each matrix, the checker computes \(r\) from the trace and \(q=(4+r^2-\operatorname{tr}(A^2))/2\), rejecting values outside the twelve candidate pairs above. For each survivor it compares the integer determinant \(\det(zI-A)\) with \((z-2)z(z-r)(z^2+q)\) at the four distinct integers \(-1,0,1,3\). Both monic quintic polynomials also agree at \(z=2\) because every row sum is two. Their difference has degree at most four and five distinct roots, so the test proves equality of the entire characteristic polynomials, not merely numerical proximity. Determinants are evaluated by the signed sum over all \(5!\) permutations, using integer arithmetic only. As an independent internal check on each accepted matrix, the checker multiplies integer matrices and verifies the three trace identities for powers three, four and five.

The enumeration yields exactly 21960 labeled matrices satisfying the full spectral condition; all 21960 are weakly connected. Directed reachability gives precisely 6300 strongly connected labeled matrices.

**3. Exact quotient by simultaneous relabeling.** Enumerate all \(5!=120\) cell permutations. For each retained matrix, choose the lexicographically least flattened row-major matrix under simultaneous row and column permutation. Distinct minima are exactly the isomorphism classes. There are 191 minima, 56 of them strongly connected. Independently, summing stabilizer sizes over all accepted labeled matrices gives \(22920\), and over the strongly connected ones gives \(6720\). Burnside's orbit-counting lemma therefore gives \(22920/120=191\) and \(6720/120=56\). Applying the same procedure separately by \((r,q)\) produces the table above. The complete list of canonical matrices, their automorphism-group orders and their orbit sizes is in `catalogue.tsv`.

**4. Two extremal-frequency witnesses.** For \(q=3\), a strongly connected representative is

\[
A_3=\begin{pmatrix}
0&0&0&0&2\\
0&0&0&1&1\\
0&0&0&2&0\\
1&1&0&0&0\\
0&0&2&0&0
\end{pmatrix},\quad
\chi_{A_3}(z)=z(z-2)(z+2)(z^2+3).
\]

For \(q=4\), a strongly connected representative is

\[
A_4=\begin{pmatrix}
0&0&0&0&2\\
0&0&0&0&2\\
0&0&0&2&0\\
0&2&0&0&0\\
0&0&2&0&0
\end{pmatrix},\quad
\chi_{A_4}(z)=z(z-2)(z+2)(z^2+4).
\]

These exact examples and the exhaustive absence of \(q\ge3\) except when \(r=-2\) establish the stated sharp higher-frequency transition. At four cells, the corresponding valency-two zero–Hopf classification has only the spectrum \(2,0,\pm i\), as established in the motivating source.

## Verification

Compile `checker.cpp` with `g++ -O2 -std=c++17 checker.cpp -o checker` and run `./checker > catalogue.tsv 2> summary.txt`. The executable uses no network access, no floating-point arithmetic and no external package. It deterministically examines exactly 759375 row configurations and performs the exact determinant and matrix-power tests, directed/undirected connectivity and all relabelings. The delivered `catalogue.tsv` and `summary.txt` are exact reproducible outputs. A separate SymPy enumeration of all four-cell valency-two matrices gave 216 labeled zero–Hopf matrices and nine isomorphism classes, agreeing with the published four-cell classification; this baseline is corroboration, not part of the five-cell proof. The five-cell proof rests on its complete finite enumeration and its deterministic executable specification, not on a sample or a runtime log alone.

## Relationship to prior work

Aguiar, Dias and Mokhtari introduce the zero–Hopf network definition, prove the four-cell valency-two classification with nine isomorphism classes and develop bifurcation normal forms. Their analysis provides the natural starting point but does not enumerate five-cell spectra. Older work on homogeneous-network enumeration counts networks irrespective of a simultaneous zero and imaginary adjacency spectrum. Older work on five-cell quotient networks treats a different restricted quotient and bifurcation family. The present result determines the new spectral filter, complete five-cell isomorphism census, new imaginary frequencies and strong-connectivity breakdown. The broader literature may contain independently derived equivalent finite tables not indexed by these keywords.

## Limitations

The result applies only to five cells, one edge type, valency two, loops/parallel arrows allowed and the spectral definition above. It does not classify all normal forms, robust synchrony patterns or nonlinear bifurcation branches and does not generalize the 191 count to six or more cells. The enumeration is an exhaustive finite proof for the specified 759375 matrices, not an infinite theorem. The nonavailability of full text for an older general-enumeration article leaves some historical priority uncertainty; its publicly available abstract describes total-network enumeration, not the spectral table asserted here. Independent external audit has not been performed.

## References

1. M. Aguiar, A. Dias, F. Mokhtari, *Zero-Hopf networks*, arXiv:2611.15221v1, originally posted 11 November 2026. https://arxiv.org/html/2611.15221v1 . See Definition 4, Section 5, Theorems 19–20, Section 7.
2. F. Aldosray and I. Stewart, *Enumeration of homogeneous coupled cell networks*, *International Journal of Bifurcation and Chaos* **15** (2005), 2361–2373. Repository abstract: https://wrap.warwick.ac.uk/34410/ .
3. M. A. D. Aguiar, A. P. S. Dias, M. Golubitsky, M. C. A. Leite, *Bifurcation from Quotient Coupled Cell Networks*, *Physica D* **238** (2009), 137–155. https://www.researchgate.net/publication/228991181_Bifurcation_from_Quotient_Coupled_Cell_Networks .
