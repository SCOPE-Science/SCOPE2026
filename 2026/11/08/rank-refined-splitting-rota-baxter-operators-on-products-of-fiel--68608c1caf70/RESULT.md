# Rank-refined splitting Rota–Baxter operators on products of fields

## Finding

Let \(F\) be **any field**, let \(n\geq1\), let \(A_n=F^n\) with coordinatewise multiplication, and fix \(\lambda\in F^\times\). A weight-\(\lambda\) Rota–Baxter operator is an \(F\)-linear map \(R:A_n\to A_n\) satisfying
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)+\lambda xy\bigr)
\]
for all \(x,y\in A_n\). Such an operator is **splitting** when there are subalgebras \(U,V\subset A_n\), not necessarily containing the ambient identity, for which \(A_n=U\oplus V\) as vector spaces and \(R|_U=0\), \(R|_V=-\lambda\,\mathrm{id}\).

Let \(S_{n,k}\) be the number of distinct splitting operators of \(F\)-linear rank \(k\). Then, for every \(0\leq k\leq n\),
\[
\boxed{S_{n,k}=\binom nk\,\tau(K_{1,k,n-k})},
\]
where \(\tau\) counts spanning trees of a graph and \(K_{1,k,n-k}\) is the complete multipartite graph with part sizes \(1,k,n-k\), with empty parts allowed. Explicitly, \(S_{n,0}=S_{n,n}=1\) and, when \(1\leq k\leq n-1\),
\[
\boxed{S_{n,k}=\binom nk(n+1)(n-k+1)^{k-1}(k+1)^{n-k-1}}.
\]
The rank distribution is independent of \(F\) and of the nonzero weight \(\lambda\). Its total is
\[
\boxed{\sum_{k=0}^{n}S_{n,k}=2(n+2)^{n-1}}.
\]

If \(K_n\) is the rank of a uniformly chosen splitting operator (uniform over distinct labeled operators, not conjugacy classes), then
\[
\boxed{\frac{K_n-n/2}{\sqrt n}\ \Longrightarrow\ \mathcal N(0,1/16)}.
\]
More precisely, uniformly over \(k\) satisfying \(\lvert k-n/2\rvert\leq B\sqrt n\) for any fixed \(B>0\),
\[
\boxed{\sqrt n\,\Pr(K_n=k)=\sqrt{\frac8\pi}\exp\!\left(-8\frac{(k-n/2)^2}{n}\right)+o(1)}.
\]
The mean rank is exactly \(n/2\) for each \(n\).

## Assumptions and scope

All counts are of actual endomorphisms of the fixed labeled algebra, not of isomorphism classes or automorphism-conjugacy orbits. The ground field need not be finite or algebraically closed. The weight is required to be nonzero; the zero-weight classification is not asserted. Ranks and probabilities refer only to splitting weight-\(\lambda\) operators. The asymptotic limit is for \(n\to\infty\), without a field-size parameter.

The structural bijection between splitting operators and properly two-colored forests obtained by deleting the root of a rooted labeled tree is a previously published theorem of Gubarev (2018, Theorem 2 and Corollary 2). The rank refinement and limit theorem below use this known bijection as an input.

## Proof

**1. Rank as a color count.** Gubarev's classification identifies the weight-\(\lambda\) operators on \(A_n\) with rooted trees on the labeled vertices \(\{0,1,\ldots,n\}\), with every vertex except \(0\) assigned one of two colors. The operator is splitting exactly when, after deleting root \(0\), adjacent vertices have opposite colors (Gubarev, 2018, Theorem 2). The color called black denotes the diagonal entry \(-\lambda\); white denotes diagonal entry zero. The corresponding operator is triangular after simultaneous permutation of coordinates. As \(R^2=-\lambda R\) and \(\lambda\neq0\), its eigenvalues are distinct and are zero and \(-\lambda\), so \(\mathrm{rank}(R)\) equals the number of black vertices. This includes characteristic two.

**2. Rank-refined spanning-tree enumeration.** Fix the \(k\) black vertices. The allowable tree edges either join root \(0\) to any non-root vertex or join non-root vertices of different colors. Thus the allowed edges form exactly \(K_{1,k,n-k}\). Every spanning tree of this graph is a valid rooted colored tree, and vice versa. The matrix-tree theorem gives, when \(0<k<n\),
\[
\tau(K_{1,k,n-k})=(n+1)(n-k+1)^{k-1}(k+1)^{n-k-1}.
\]
Indeed the nonzero Laplacian eigenvalues are \(n+1\), twice, \(n-k+1\) with multiplicity \(k-1\), and \(k+1\) with multiplicity \(n-k-1\). Their product divided by \(n+1\) gives the displayed count. With one color class empty the allowed graph is a star, with one spanning tree. Choosing the black set in \(\binom nk\) ways proves the rank formula.

**3. Total and symmetry.** Expand root \(0\) to two vertices \(0\) and \(*\), joined by a specified edge; attach the black neighbors of root \(0\) to \(0\) and its white neighbors to \(*\), keeping every non-root edge. Because all non-root edges connect opposite colors, the result is a tree on \(n+2\) labeled vertices containing the specified edge \(0*\). Conversely, in any tree with this edge, bipartition the tree with \(0\) white and \(*\) black, contract \(0*\), and retain the colors of the other \(n\) vertices. These are inverse operations. By edge symmetry in Cayley's \((n+2)^{n}\) labeled trees, the number containing a specified edge is \(2(n+2)^{n-1}\). Interchanging the two non-root colors gives \(S_{n,k}=S_{n,n-k}\), hence \(\mathbb E K_n=n/2\).

**4. Gaussian local limit.** Write \(k=nx\) with \(0<x<1\). Stirling's formula applied to the explicit count gives, uniformly for \(x\) in compact subintervals of \((0,1)\),
\[
\log S_{n,k}=(n-1)\log n+n\Phi(x)+O(\log n),\qquad
\Phi(x)=(1-2x)\log\frac{x}{1-x}.
\]
The smooth prefactors in this expansion vary by a factor \(1+o(1)\) for \(k=n/2+O(\sqrt n)\). The function \(\Phi\) is uniquely maximized at \(x=1/2\), and
\[
\Phi(1/2+u)=-8u^2+O(u^4).
\]
Consequently, for bounded \(t=(k-n/2)/\sqrt n\),
\[
\frac{S_{n,k}}{S_{n,\lfloor n/2\rfloor}}=e^{-8t^2}(1+o(1))
\]
uniformly on bounded \(t\)-intervals. A direct central Stirling calculation, using the exact total from step 3, gives
\[
\frac{S_{n,\lfloor n/2\rfloor}}{2(n+2)^{n-1}}
=\sqrt{\frac8{\pi n}}\,(1+o(1)).
\]
Multiplying proves the stated local limit. For each \(B\), Riemann sums of this local limit give convergence of the probability mass in \([-B,B]\) to the corresponding Gaussian integral. Since those integrals approach one as \(B\to\infty\), the laws are tight, yielding the stated weak convergence. No finite enumeration is used to justify the infinite limit.

## Verification

The independent standard-library script `verify.py` enumerates every matrix candidate admitted by the diagonal weight-one Rota–Baxter equations and checks the full operator equation, splitting equation and rank histogram over \(\mathbb F_2\) and \(\mathbb F_3\), for \(1\le n\le4\) as specified in the script. It separately enumerates all Prüfer-coded labeled trees and all their two-colorings for \(1\le n\le5\). Results for \(n=2,3,4,5\) include rank histograms
\[
(1,6,1),\quad (1,24,24,1),\quad (1,80,270,80,1),\quad (1,240,2160,2160,240,1).
\]
Execution: `python3 verify.py`. The extracted package script completed with `VERIFY_OK`. All infinite claims are supported by the proof, not by extrapolation from these tests.

## Relationship to prior work

Gubarev's *Rota–Baxter operators on a sum of fields* (arXiv:1811.08219, first submitted 2018-11-20) establishes both the full operator/tree bijection and its proper-color criterion for splitting operators. Table 1 lists the unrefined splitting totals \(2(n+2)^{n-1}\) with a question mark, so this total on its own is **not claimed as a novel conjecture or independently new theorem**. The exact rank-stratified operator counts and local Gaussian limit are the contribution assessed here.

Meir and Moon, *On the Bipartition Numbers of Random Trees, II* (Ars Combinatoria 51, 1999), study bipartition sizes and Gaussian laws for simply generated rooted trees, including labeled trees. This is strong methodological prior art. Their unconditioned tree ensemble does not explicitly enumerate splitting operator ranks or the equivalent trees conditioned to contain a particular designated edge. Classical Cayley enumeration and the matrix-tree theorem are acknowledged as prior results.

A search of available mathematical records and research literature found no statement that directly supplies this complete rank polynomial. This is a best-knowledge comparison, not a claim of global uniqueness: an uninspected formulation in the tree-enumeration literature could imply the formulas.

## Limitations

The formula classifies splitting operators only; non-splitting operators have a different and generally more complicated rank behavior. The input correspondence from Gubarev is taken as an established external theorem. The Gaussian law is asymptotic in the number of field factors, not field size. No publication-priority or independent validation certificate is asserted. The combinatorial rank law may have an alternative known description as a conditioned Cayley-tree bipartition count.

## References

1. V. Gubarev, *Rota–Baxter operators on a sum of fields*, arXiv:1811.08219 (submitted 2018-11-20), especially Theorem 2, Corollary 2 and Table 1. https://arxiv.org/html/1811.08219v1
2. A. Meir and J. W. Moon, *On the Bipartition Numbers of Random Trees, II*, Ars Combinatoria 51 (1999), 21–31. https://combinatorialpress.com/article/ars/Volume%2051/volume-51-paper-2.pdf
3. Kirchhoff's matrix-tree theorem and Cayley's labeled-tree formula (standard classical results).
