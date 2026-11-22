# Sharp endpoint Fourier norms of the \((n-2,1,1)\) Specht block

## Finding
For every integer \(n\ge4\), the central Fourier projection onto the irreducible representation \(S^{(n-2,1,1)}\) of the symmetric group has an exact sharp endpoint norm determined by the joint number of 1-cycles and 2-cycles of a permutation. More precisely, put
\[
d_n=\frac{(n-1)(n-2)}2,\quad a_j=\frac{(j-1)(j-2)}2\quad(j\ge0),
\]
and let \(D_m\) count permutations on \(m\) letters with neither 1-cycles nor 2-cycles (including \(D_0=1\)). Then
\[
\boxed{\|P_n\|_{\ell^1\to\ell^1}=\|P_n\|_{\ell^\infty\to\ell^\infty}=
2d_n\!\sum_{\substack{j,k\ge0,\ j+2k\le n\k>a_j}}
\frac{(k-a_j)D_{n-j-2k}}{j!\,2^k k!\,(n-j-2k)!}.}
\]
The hook character is strictly negative exactly when \(X_2>a_{X_1}\), where \(X_i\) counts cycles of length \(i\).

The normalized sharp norm has a constant limit with convergence faster than every fixed geometric rate. Define
\[
C=2e^{-3/2}\sum_{j=0}^{\infty}\sum_{k>a_j}\frac{k-a_j}{j!\,2^k k!}
=0.643322969593222967935346635089\ldots.
\]
For every real \(R>1\),
\[
\boxed{\frac{\|P_n\|}{d_n}=C+O_R(R^{-n}),\qquad
\lim_{n\to\infty}\frac{\|P_n\|}{n^2}=\frac C2.}
\]

## Assumptions and scope
The group is \(G=S_n\) for an integer \(n\ge4\), with normalized counting (Haar) measure. The standard representation is the \((n-1)\)-dimensional subspace \(V_n\subset\mathbb C^n\) on which coordinate sum is zero. Its exterior square \(\bigwedge^2 V_n\) is the irreducible hook Specht module \(S^{(n-2,1,1)}\) of dimension \(d_n\). The operator \(P_n\) is the central (full-isotypic) orthogonal projection on functions \(G\to\mathbb C\) onto the matrix-coefficient subspace of this representation. Its norm is measured on finite-dimensional \(\ell^1(G)\) or \(\ell^\infty(G)\) with normalized counting measure. No claims are made about noncentral subprojections or representations of other shapes.

## Proof
**1. Character polynomial and sharp convolution norm.** For \(\sigma\in S_n\) let \(X_i(\sigma)\) count its cycles of length \(i\). The character of \(V_n\) equals \(X_1-1\); the character at \(\sigma^2\) equals \(X_1+2X_2-1\). The exterior-square trace identity gives
\[
\chi_n(\sigma)=\tfrac12\big((X_1-1)^2-(X_1+2X_2-1)\big)
=\frac{(X_1-1)(X_1-2)}2-X_2=a_{X_1}-X_2.
\]
In particular, \(\chi_n<0\) precisely on \(X_2>a_{X_1}\). As \(\chi_n\) is a real, nontrivial irreducible character, its average is zero. The central projection is normalized convolution with \(d_n\chi_n\), so its \(\ell^\infty\) operator norm is \(d_n\mathbb E|\chi_n|\). Equality is attained at any chosen output point by taking the input to be the matching character sign, with arbitrary unit-bounded values where the character vanishes; translation gives all rowwise extremizers. The \(\ell^1\) norm is equal by duality. The mean-zero identity yields
\[
\mathbb E|\chi_n|=2\mathbb E\big[(X_2-a_{X_1})_+\big],
\quad t_+=\max\{t,0\}.
\]

**2. Exact two-short-cycle enumeration.** If \(\sigma\) has \(j\) fixed points and \(k\) transpositions, the remaining \(m=n-j-2k\) letters form a permutation with neither 1- nor 2-cycles. The number of such permutations is
\[
\frac{n!}{j!\,2^kk!\,m!}\,D_m.
\]
Consequently
\[
\mathbb P(X_1=j,X_2=k)=\frac{D_{n-j-2k}}{j!\,2^kk!\,(n-j-2k)!}
\]
when \(j,k\ge0\) and \(j+2k\le n\). Substitution into the preceding positive-part identity proves the exact sharp finite sum. In particular, \(D_1=D_2=0\), and \(D_m/m!\) has the generating function below. For example, the exact norms for \(n=4,5,6,7,8\) are \(9/4,3,20/3,10,4249/320\), respectively.

**3. Entire-function cancellation and the limiting constant.** The exponential formula for permutations all of whose cycles have length at least three gives
\[
\sum_{m\ge0}\frac{D_m}{m!}z^m
=\exp\!\left(\sum_{r\ge3}\frac{z^r}{r}\right)
=\frac{e^{-z-z^2/2}}{1-z},\qquad |z|<1.
\]
Set
\[
F(z)=\sum_{j,k\ge0}\frac{(k-a_j)_+}{j!\,2^kk!}z^{j+2k},\qquad
H(z)=e^{-z-z^2/2}F(z).
\]
The double series for \(F\) is entire because, on \(|z|=R\), \((k-a_j)_+\le k\) and
\[
|F(z)|\le e^R\cdot\frac{R^2}{2}e^{R^2/2}.
\]
Thus \(H\) is entire. The exact finite sum is equivalently the coefficient identity
\[
\frac{\|P_n\|}{2d_n}=[z^n]\frac{H(z)}{1-z}
=\sum_{m=0}^{n}[z^m]H(z).
\]
As \(H\) is entire, Cauchy's estimate on any circle \(|z|=R>1\) yields
\[
\left|\frac{\|P_n\|}{d_n}-2H(1)\right|
\le\frac{2\max_{|z|=R}|H(z)|}{(1-R^{-1})R^{n+1}}.
\]
At \(z=1\), the nonnegative absolutely convergent series defining \(F\) gives
\[
2H(1)=2e^{-3/2}\sum_{j\ge0}\sum_{k>a_j}\frac{k-a_j}{j!\,2^kk!}=C>0.
\]
This proves faster-than-any-fixed-geometric convergence, and \(d_n/n^2\to1/2\) proves the asymptotic norm formula. No claim of an elementary closed expression for \(C\) is necessary.

## Verification
The accompanying self-contained `checker.py`, requiring only Python 3's standard library, checks the character formula using directly enumerated cycle decompositions, compares the exact finite norm formula with full permutation enumeration for every \(n=4,\ldots,8\), independently reconstructs coefficient sequences of \(H\), and verifies the full permutation-moment identities through \(n=15\). Its terminal marker is `HOOK_SPECHT_EXACT_FOURIER_PROJECTION_CHECKS_PASS`. These finite computations supplement, and do not replace, the all-dimensional proof. Decimal digits of \(C\) follow from absolutely convergent positive series summation.

## Relationship to prior work
Church–Ellenberg–Farb establish the character-polynomial framework and explicitly give \(\binom{X_1}{2}-X_2\) for the exterior square of the **permutation** representation. Subtracting the standard summand yields the present (classical) hook character. Li–Xia–Zhou, Table 2, explicitly tabulate the same hook character and its dimension in work on normal Cayley graphs. Their eigenvalue problem is a character average over **selected generating conjugacy classes**, not the absolute character average over all permutations governing a central Fourier projection. General finite-group Fourier theory supplies \(\|P_n\|=d_n\mathbb E|\chi_n|\), but does not evaluate this nonlinear average. The neighboring two-row Specht shape \((n-2,2)\) has a different character with the opposite sign on the 2-cycle statistic and is not related to this hook block by a sign twist. The contribution here is the sharp all-\(n\) positive-part formula and the analytic faster-than-geometric convergence theorem, not a new character table.

## Limitations
The theorem concerns a single **central irreducible** Fourier block; it does not cover sums of blocks, noncentral partial matrix-coefficient projections, or other representations. The series defining \(C\) is absolutely convergent but no simpler closed expression is asserted. The coefficient identity is exact, and finite checks are not used to infer convergence. An unindexed historical table of character absolute averages or an equivalent cycle-index derivation could affect publication priority; exhaustive bibliographic uniqueness is not certified. Independent mathematical validation has not been performed.

## References
- T. Church, J. S. Ellenberg, B. Farb, *FI-modules and stability for representations of symmetric groups*, arXiv:1204.4533, first posted 2012-04-20, esp. Section 1 and the exterior-square character-polynomial example, https://arxiv.org/pdf/1204.4533 .
- Y. Li, B. Xia, S. Zhou, *The second largest eigenvalue of normal Cayley graphs on symmetric groups generated by cycles*, arXiv:2302.04022v1, posted 2023-02-08, esp. Table 2 (character and dimension of \((n-2,1,1)\)) and Theorems on normal Cayley-graph eigenvalues, https://arxiv.org/pdf/2302.04022 .
