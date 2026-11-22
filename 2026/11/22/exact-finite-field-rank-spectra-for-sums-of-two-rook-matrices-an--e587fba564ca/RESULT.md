# Exact finite-field rank spectra for sums of two rook matrices and a characteristic-sensitive invertibility transition

## Finding
Let \(R_n\) be the set of \(n\)-by-\(n\) zero-one matrices having at most one nonzero entry in each row and column, including the zero matrix, and let \(\mathbb F_q\) be any finite field of characteristic \(p\). For \(n\geq 0\), define
\[
M_{n,p}(u)=\sum_{P,Q\in R_n}u^{\operatorname{rank}_{\mathbb F_q}(P+Q)}.
\]
Write \(\delta_{p,k}=1\) when \(p=2\) or \(k\) is even, and \(\delta_{p,k}=0\) otherwise. Then the **complete all-rank generating function** is
\[
\boxed{\sum_{a,b\geq0}\frac{x^a y^b}{a!b!}\sum_{P\in R_{a,b}}\sum_{Q\in R_{a,b}}u^{\operatorname{rank}(P+Q)}
=\exp\!\left(x+y+\frac{(2+x+y)xyu}{1-xyu}+\sum_{k\geq1}\frac{(xy)^k}{k}u^{k-\delta_{p,k}}\right).}
\]
Here \(R_{a,b}\) denotes zero-one \(a\)-by-\(b\) partial-injection matrices. Thus \(M_{n,p}(u)=(n!)^2[x^ny^n]\) of the displayed exponential. The formula depends only on the field characteristic being two or odd, not on field order.

In particular the numbers \(I_{n,p}\) of ordered pairs with \(P+Q\) nonsingular are
\[
\boxed{I_{n,2}=(n!)^2[t^n]\exp\!\left(\frac{2t}{1-t}\right),\qquad
I_{n,\mathrm{odd}}=(n!)^2[t^n]\exp\!\left(\frac{2t}{1-t}\right)\sqrt{\frac{1+t}{1-t}}.}
\]
If \(P,Q\) are independent uniform elements of \(R_n\), their nonsingular-sum probabilities, as \(n\to\infty\), satisfy
\[
\boxed{\Pr_{p=2}(\operatorname{rank}(P+Q)=n)\sim 2^{5/4}\sqrt\pi\,n^{-1/4}\exp(-(4-2\sqrt2)\sqrt n),}
\]
\[
\boxed{\Pr_{p\ne2}(\operatorname{rank}(P+Q)=n)\sim 2^{3/2}\sqrt\pi\,\exp(-(4-2\sqrt2)\sqrt n).}
\]
Consequently the probability in odd characteristic divided by that in characteristic two is asymptotic to \(2^{1/4}n^{1/4}\).

## Assumptions and scope
The binary entries are the field elements \(0\) and \(1\), **not arbitrary nonzero weights**. Each matrix is a partial permutation matrix; multiplication of matrices is not involved in the statistic. We count *ordered* pairs, with repetition allowed, over all square sizes \(n\geq0\). In the bivariate statement, row labels and column labels are drawn from disjoint labeled sets of sizes \(a,b\). All ranks are over the specified field and all formal generating-function identities are coefficientwise in \(x,y,u\). The asymptotic statements hold as \(n\) tends to infinity, with fixed arbitrary characteristic (indeed the counts are independent of \(q\) within each characteristic regime).

## Proof
**1. Colored bipartite components.** Associate \((P,Q)\) with the superposition of its two partial matchings on labeled row and column vertices. Color edges from \(P\) red and from \(Q\) blue, retaining multiplicity when both choose the same entry. Every vertex has degree at most one in each color, so the connected components are isolated vertices, alternating edge-colored paths, and alternating cycles. A repeated red-blue edge is an alternating cycle with one vertex on each side. The correspondence is reversible without ambiguity.

**2. Component ranks.** The sum is block diagonal after separately permuting row and column labels. For a path with \(r\) row vertices and \(s\) column vertices, its alternating-edge matrix has rank \(\min(r,s)\) over every field, because successive elimination starting at a path endpoint produces a full-rank triangular minor. For a cycle with \(k\) row vertices and \(k\) column vertices, the block is permutation-equivalent to \(I_k+C_k\), where \(C_k\) cyclically permutes coordinates. Its determinant is \(1-(-1)^k\); if zero, its kernel is one dimensional (the recurrence \(v_{j+1}=-v_j\)), including the \(k=1\) double edge. Hence its rank is \(k-\delta_{p,k}\). Rank is additive across components.

**3. Exact labeled enumeration.** An isolated row or column vertex contributes \(x\) or \(y\). For each \(k\geq1\), a path with \(k\) vertices in each class carries exactly two edge-colorings and contributes \(2(xy)^k u^k\) to the *exponential* component series. A path with \(k+1\) row vertices and \(k\) column vertices (or the transpose), with \(k\geq1\), contributes \(x^{k+1}y^k u^k\) (or \(x^ky^{k+1}u^k\)). These coefficients follow from \(k!^2\) and \((k+1)!k!\) possible labeled colored paths, respectively, divided by factorials in the bivariate exponential convention. A colored alternating cycle with \(k\) vertices of either class contributes \((xy)^k u^{k-\delta_{p,k}}/k\): the number of labeled colored cycles is \(k!(k-1)!\), including \(k=1\). Summing all component contributions yields
\[
x+y+\sum_{k\geq1}\left(2(xy)^k+(x+y)(xy)^k\right)u^k+\sum_{k\geq1}\frac{(xy)^k}{k}u^{k-\delta_{p,k}}.
\]
The labeled exponential formula proves the claimed bivariate expression and every rank coefficient.

**4. Full-rank specialization.** A component must have row-rank equal to the number of its rows and column-rank equal to the number of its columns: since a square direct sum has rank \(n\), every component must be balanced and nonsingular. Thus only equal-sided paths and cycles of zero defect remain, and there are no isolated vertices. Writing \(t=xy\), the equal-sided paths contribute \(2t/(1-t)\). In characteristic two no alternating cycle is nonsingular; in odd characteristic precisely the odd-\(k\) cycles are nonsingular, contributing
\[
\sum_{j\geq0}\frac{t^{2j+1}}{2j+1}=\tfrac12\log\frac{1+t}{1-t}.
\]
Exponentiating gives both displayed exact formulas. In particular, the contribution from two full permutation matrices is singular in characteristic two; allowing partial matchings supplies invertible examples.

**5. Sharp asymptotics.** The rook monoid order is
\[
|R_n|=\sum_{r=0}^{n}\binom nr^2r!=n!L_n(-1),\qquad L_n(-1)=[t^n]\frac{\exp(t/(1-t))}{1-t}.
\]
For fixed \(a>0\) and fixed \(\beta\in\{0,\tfrac12,1\}\), a saddle calculation gives
\[
[t^n]\exp\!\left(\frac{at}{1-t}\right)(1-t)^{-\beta}
\sim\frac{a^{1/4-\beta/2}}{2\sqrt\pi}\,n^{\beta/2-3/4}
\exp(2\sqrt{an}-a/2).
\]
For completeness, apply Cauchy's integral on the positive real saddle circle, with radius \(r_n=1-\sqrt{a/n}+O(n^{-1})\). Expanding the exponent \(at/(1-t)-n\log t\) at angle zero gives its real maximum \(2\sqrt{an}-a/2+o(1)\), and a negative quadratic in the angular coordinate of width \(\Theta(n^{-3/4})\). Integration of that quadratic produces the stated Gaussian prefactor. Outside an angular window larger than this width, the real part is uniformly smaller; the factor \((1-t)^{-\beta}\) is uniformly controlled on the saddle. The analytic factor \(\sqrt{1+t}\) in the odd-characteristic formula takes the value \(\sqrt2\) at the dominant saddle and changes only lower-order terms. Therefore
\[
\frac{I_{n,2}}{(n!L_n(-1))^2}
\sim2^{5/4}\sqrt\pi\,n^{-1/4}e^{(2\sqrt2-4)\sqrt n},
\]
\[
\frac{I_{n,\mathrm{odd}}}{(n!L_n(-1))^2}
\sim2^{3/2}\sqrt\pi\,e^{(2\sqrt2-4)\sqrt n}.
\]
This completes the unified rank-distribution and invertibility theorem.

## Verification
The accompanying standard-library-only program `check.py` independently constructs the exponential-formula coefficients using exact rational arithmetic and enumerates every pair of partial permutation matrices using Gaussian elimination modulo two and three for \(1\leq n\leq4\). All 43,681 ordered pairs in size four match the coefficients in both characteristics. For \(5\leq n\leq8\) it also checks that the rank polynomial sums to the square of the independently computed rook-monoid order. Re-run `python3 check.py`; full output is in `CHECKS.txt`. These finite checks corroborate but do not replace the proof for unbounded \(n\). Field extensions of characteristic two/odd share the same ranks because each component's only possible determinant obstruction is \(2\).

## Relationship to prior work
Solomon's treatment of rook-monoid representations and Malandro–Rockmore's Fourier theory supply the standard partial-permutation object and its order; neither is the asserted additive rank theorem. Wanicharpichat–Rangpung and a 2018 MathOverflow solution analyze nonsingularity/rank of sums of **full** permutation matrices via cycle decompositions. Their full-permutation setting lacks alternating paths, which are essential for invertible sums in characteristic two, and does not imply the all-rank rook-monoid formula or its probability asymptotics. General finite-field random-matrix rank distributions do not enforce the degree-two colored-matching constraint. Full-permutation cycle computations are credited as prior coverage of that special case, not claimed here.

## Limitations
The matrices are unweighted partial permutations and the statistic is the rank of the sum of **two**, not a general linear combination of weighted monomial matrices or arbitrary numbers of summands. The exact generating function counts all ranks, but no general limiting distribution is asserted for lower ranks. The proof is self-contained; historical priority is a best-knowledge assessment, not an independent publication certification, and a not-located equivalent specialized enumeration remains possible.

## References
1. L. Solomon, *Representations of the rook monoid*, Journal of Algebra **256** (2002), 309–342, `https://u.cs.biu.ac.il/~margolis/Representation%20Theory%20Seminar/Monoid%20Representations%20and%20Applications/Solomon%20Rook%20presentation.pdf` (the published paper, particularly the rook-matrix embedding and formula (1.2)).
2. M. Malandro and D. Rockmore, *Fast Fourier Transforms for the Rook Monoid*, arXiv:0709.4175, publicly submitted 2007-09-26, `https://arxiv.org/abs/0709.4175`.
3. W. Wanicharpichat and T. Rangpung, *Nonsingularity of Linear Combination of Permutation Matrices* (2015), DOI:10.13140/RG.2.1.3224.0808, `https://www.researchgate.net/publication/279173309_NONSINGULARITY_OF_LINEAR_COMBINATION_OF_PERMUTATION_MATRICES`.
4. G. Zaimi, response to *Distribution of sum of two permutation matrices* (2018), `https://mathoverflow.net/questions/311052/distribution-of-sum-of-two-permutation-matrices/311055`.
5. P. Flajolet and R. Sedgewick, *Analytic Combinatorics* (2009), `https://ac.cs.princeton.edu/home/` (labeled exponential constructions and saddle-point method).
