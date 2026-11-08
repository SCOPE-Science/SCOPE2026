# Sharp lower-edge escape among minimum-real-spectrum non-backtracking Laplacians

## Finding

For each integer \(a\ge2\), subdivide every edge of the balanced complete tripartite graph \(K_{a,a,a}\) once; call the resulting simple connected graph \(G_a\). It is bipartite and \((2,2a)\)-biregular. Write \(L_a=I-T_a\) for the non-backtracking Laplacian, where \(T_a\) is the Markov transition matrix indexed by oriented edges, with a transition from \((u,v)\) to \((v,w)\) of probability \(1/(\deg(v)-1)\) when \(w\ne u\).

The real spectrum of \(L_a\), with algebraic multiplicities, is exactly

\[
0\quad(1),\qquad 2\quad(1),\qquad
1\pm\frac{1}{\sqrt{2a-1}}\quad\bigl(3a(a-1)+1\text{ each}\bigr).
\]

There are therefore exactly \(6a^2-6a+4=2M-2N+4\) real eigenvalues, the universal minimum for connected bipartite graphs with minimum degree two. Nevertheless, \(G_a\) violates the **two-sided universal-cover Ramanujan condition** precisely for \(a\ge8\). In particular, the lower bound's equality does not characterize two-sided Ramanujan biregular graphs.

## Assumptions and scope

The parameter \(a\) is any integer at least two. The original complete tripartite graph has \(3a\) vertices and \(3a^2\) edges. Thus its subdivision \(G_a\) has

\[
N=3a+3a^2,\qquad M=6a^2,\qquad h=M-N=3a(a-1).
\]

All eigenvalues are counted with **algebraic multiplicity**, including the nonreal ones. Here two-sided biregular Ramanujan means that every nontrivial nonzero adjacency eigenvalue lies in the adjacency spectrum of the infinite \((2,2a)\)-biregular universal-cover tree: in absolute value, its allowed interval is

\[
\sqrt{2a-1}-1\ \le |\lambda|\le\ \sqrt{2a-1}+1.
\]

The zero adjacency eigenvalue is allowed, and the trivial Perron pair \(\pm2\sqrt a\) is excluded. Some usages of “biregular Ramanujan” impose only the **upper** edge of this interval; the distinction is essential here. No claim concerns that one-sided definition.

## Proof

**1. Incidence singular spectrum.** Let \(H_a=K_{a,a,a}\), and let \(C\) be the unsigned vertex-edge incidence matrix of \(H_a\), with \(3a\) rows and \(3a^2\) columns. Its adjacency matrix has eigenvalues \(2a\) once, \(-a\) twice, and \(0\) with multiplicity \(3a-3\). Indeed, vectors constant on each part yield the three eigenvalues of the equitable quotient, while vectors summing to zero within a part lie in the zero eigenspace. Every vertex has degree \(2a\), so

\[
CC^{\mathsf T}=2aI+A(H_a).
\]

Consequently, the eigenvalues of \(CC^{\mathsf T}\) are \(4a\) once, \(a\) twice, and \(2a\) with multiplicity \(3a-3\). The adjacency matrix of the subdivision is \(A(G_a)=\left(\begin{smallmatrix}0&C\\C^{\mathsf T}&0\end{smallmatrix}\right)\); thus its nonzero adjacency eigenvalues are \(\pm2\sqrt a\), \(\pm\sqrt a\) (each twice), and \(\pm\sqrt{2a}\) (each \(3a-3\) times). Its remaining \(3a^2-3a\) adjacency eigenvalues vanish.

**2. Exact non-backtracking polynomial.** Let \(B_a\) denote the unweighted Hashimoto matrix on the \(2M\) oriented edges of \(G_a\), and put \(d=2a-1\). The Ihara–Bass determinant identity gives

\[
\det(tI-B_a)=(t^2-1)^h\det\bigl(t^2I-tA(G_a)+D(G_a)-I\bigr).
\]

The block diagonal term is \((t^2+d)I_{3a}\) on the original vertices and \((t^2+1)I_{3a^2}\) on the inserted vertices. Taking its Schur complement and using Step 1 yields

\[
\begin{aligned}
\det(tI-B_a)
&=(t^2-1)^h(t^2+1)^h
 (t^4-2at^2+d)\\
&\qquad\cdot(t^4+d)^{3a-3}(t^4+at^2+d)^2\\
&=\boxed{(t^4-1)^h(t^2-1)(t^2-d)
(t^4+d)^{3a-3}(t^4+at^2+d)^2}.
\end{aligned}
\]

The Schur-complement calculation is initially valid away from \(t^2=-1\) and therefore holds identically as a polynomial. The polynomial has total degree \(2M=12a^2\), so it accounts for every eigenvalue. Since \(a,d>0\), both \(t^4+d\) and \(t^4+at^2+d\) are strictly positive for real \(t\). Thus the only real roots of \(B_a\) are \(\pm1\), each with multiplicity \(h+1\), and \(\pm\sqrt d\), each simple.

**3. From the Hashimoto operator to the Laplacian.** Since oriented edges alternate between degree-two and degree-\(2a\) destinations, ordering the oriented edges by destination yields two off-diagonal blocks. The non-backtracking transition matrix rescales one of these blocks by \(1/d\) and the other by \(1\). A block diagonal similarity (multiplying one block of coordinates by \(\sqrt d\)) therefore gives \(T_a\sim B_a/\sqrt d\). Hence the real eigenvalues of \(L_a=I-T_a\) are precisely \(0,2,1\pm1/\sqrt d\), with multiplicities claimed. Their total is

\[
2(h+1)+2=6a(a-1)+4=2M-2N+4.
\]

For connected bipartite graphs, the Mulas–Torres universal bound is \(2M-2N+2c+2b=2M-2N+4\) because \(c=b=1\). This proves exact attainment, not merely an upper bound.

**4. Sharp two-sided lower-edge transition.** By Step 1, the only nontrivial nonzero adjacency magnitudes are \(\sqrt{2a}\) and \(\sqrt a\). The former lies strictly inside the permitted interval \([\sqrt d-1,\sqrt d+1]\). The latter never exceeds the upper endpoint; it lies below the lower endpoint exactly when

\[
\sqrt a<\sqrt{2a-1}-1
\quad\Longleftrightarrow\quad a>4+2\sqrt3.
\]

For integral \(a\ge2\), this is equivalent to \(a\ge8\). Thus the two-sided universal-cover condition holds exactly for \(2\le a\le7\), and fails for every \(a\ge8\). The outlying low-magnitude adjacency eigenvalues contribute roots only to \(t^4+at^2+d\), which has no real roots. This explains why the real non-backtracking eigenvalue count is blind to this lower-edge violation.

## Verification

Run `python3 artifacts/verify.py` using only Python's standard library. The checker independently builds the graph from its edges, reconstructs the complete non-backtracking adjacency matrix and the integer characteristic polynomial from exact closed-walk traces and Newton identities for \(a=1,2,3\), and compares it with the displayed formula. It also checks the incidence singular-value power sums exactly for \(1\le a\le11\), and the arithmetic of the sharp two-sided threshold and real eigenvalue counts for \(2\le a\le79\). Its expected final line is `VERIFY_OK`.

These computations are finite corroboration, not an infinite-dimensional proof; the unrestricted statements follow from the algebraic derivation above.

## Relationship to prior work

Mulas and Torres (arXiv:2611.02194v1, first posted 2026-11-01 UTC) prove the universal real-eigenvalue lower bound, and characterize equality for **connected regular** graphs via strict Ramanujan spectra. The equality bound is used here without claiming it as new; the present family gives an explicit biregular equality phenomenon not addressed by their regular characterization.

Kempton (arXiv:1603.05553, Section 4.2, Theorem 6) and Brito–Dumitriu–Harris (arXiv:1804.07808, Lemma 2.2) already provide general biregular non-backtracking spectral identities. Neither the determinant machinery nor a general singular-value criterion is claimed as new. The separate contribution is the specific infinite incidence-graph family, its complete real spectrum, and the sharp \(a=8\) two-sided lower-edge escape. This is a direct specialized computation using established general identities, and unpublished or differently phrased equivalent examples remain a historical-priority risk.

## Limitations

This result does not classify all biregular equality graphs, does not strengthen the general real-eigenvalue lower bound, and does not disprove **one-sided** biregular Ramanujan definitions. It is restricted to once-subdivided balanced complete tripartite graphs. Independent validation and a comprehensive priority determination have not been performed.

## References

1. R. Mulas and L. Torres, *The real eigenvalues of the non-backtracking Laplacian*, arXiv:2611.02194v1 (first publicly posted 2026-11-01 UTC), https://arxiv.org/abs/2611.02194.
2. M. Kempton, *Non-backtracking random walks and a weighted Ihara's theorem*, arXiv:1603.05553 (2016), Section 4.2, https://arxiv.org/abs/1603.05553.
3. G. Brito, I. Dumitriu and K. D. Harris, *Spectral gap in random bipartite biregular graphs and applications*, arXiv:1804.07808; *Combinatorics, Probability and Computing* 31 (2022), 229–267, https://arxiv.org/abs/1804.07808.
