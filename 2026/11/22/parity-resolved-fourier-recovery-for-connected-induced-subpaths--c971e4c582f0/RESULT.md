# Parity-resolved Fourier recovery for connected induced subpaths

## Finding
For every integer \(n\ge2\), let \(P_n\) be the path with labelled vertex set \([n]\). For \(p\in\{0,1\}\), let \(\mathcal I_n^{(p)}\) be the family of nonempty vertex intervals of cardinality congruent to \(p\pmod2\). Let \(f_n^{(p)}:\mathbb F_2^n\to\{0,1\}\) indicate their incidence vectors, and let \(T_n^{(p)}h=f_n^{(p)}*h\) be unnormalized XOR convolution. Write \(N=n+1\), \(a=\lceil N/2\rceil\), \(b=\lfloor N/2\rfloor\). Every Fourier multiplier of \(T_n^{(0)}\) or \(T_n^{(1)}\) has the form
\[
\lambda_n^{(0)}(j,k)=\frac{(a-2j)^2+(b-2k)^2-N}{2},\qquad
\lambda_n^{(1)}(j,k)=(a-2j)(b-2k),
\]
for \(0\le j\le a-1\) and \(0\le k\le b\), with multiplicity \(\binom{a-1}{j}\binom bk\). The superscript \(0\) means *even number of vertices*, not even number of edges.

In particular, even-order connected-subpath convolution is singular **if and only if** \(n+1\) is a sum of two integer squares. Equivalently, in the prime factorization of \(n+1\), every prime congruent to \(3\pmod4\) has even exponent. Odd-order connected-subpath convolution is invertible **if and only if** \(n\equiv1\pmod4\).

The exact nullities are
\[
Z_n^{(0)}=\sum_{j=0}^{a-1}\sum_{k=0}^{b}\binom{a-1}{j}\binom bk\,\mathbf1\bigl[(a-2j)^2+(b-2k)^2=N\bigr],
\]
\[
Z_n^{(1)}=\sum_{j=0}^{a-1}\sum_{k=0}^{b}\binom{a-1}{j}\binom bk\,\mathbf1\bigl[(a-2j)(b-2k)=0\bigr].
\]
Thus \(\operatorname{rank}T_n^{(p)}=2^n-Z_n^{(p)}\), over \(\mathbb R\) or \(\mathbb C\). Examples of even-order ranks at \(n=3,4,7,8,9,12\) are respectively \(4,10,96,226,312,3466\).

## Assumptions and scope
The path is simple and its vertices are distinguishable in path order. A nonempty connected vertex-induced subset is an interval \(\{i+1,\ldots,j\}\) with integer endpoints \(0\le i<j\le n\). All intervals are counted once, with no weights beyond their Walsh signs. Convolution is on the full group \(G=\mathbb F_2^n\), without averaging by \(|G|\); a character is \(\chi_\xi(x)=(-1)^{\sum_{r=1}^n\xi_rx_r}\). The Fourier multiplier is \(\widehat f(\xi)=\sum_{x\in G}f(x)\chi_\xi(x)\). Multiplicities count actual characters, not symmetry classes. No claim is made for the empty family at \(n=1\) in the even-order case.

## Proof
Fix a frequency \(\xi\in G\). For \(0\le i\le n\), define the prefix parity sign
\[
\varepsilon_0=1,\qquad \varepsilon_i=(-1)^{\xi_1+\cdots+\xi_i}\quad(i\ge1).
\]
The sign of interval \(\{i+1,\ldots,j\}\) is exactly \(\varepsilon_i\varepsilon_j\). The map \(\xi\mapsto(\varepsilon_1,\ldots,\varepsilon_n)\) is bijective, since \((-1)^{\xi_i}=\varepsilon_{i-1}\varepsilon_i\).

Split the \(N=n+1\) prefix indices according to their parity. Let \(X\) be the sum of the signs at the \(a\) even indices and \(Y\) the sum at the \(b\) odd indices. Even-cardinality intervals have endpoints in the same index-parity class. Since \(\varepsilon_i^2=1\), summing over unordered endpoint pairs gives
\[
\widehat f_n^{(0)}(\xi)=\frac{X^2-a}{2}+\frac{Y^2-b}{2}=\frac{X^2+Y^2-N}{2}.
\]
Odd-cardinality intervals have opposite-parity endpoints, so their signed sum is \(\widehat f_n^{(1)}(\xi)=XY\). If exactly \(j\) of the \(a-1\) freely chosen even-index signs are negative, and exactly \(k\) of the \(b\) odd-index signs are negative, then \(X=a-2j\), \(Y=b-2k\). All remaining choices are unconstrained, yielding \(\binom{a-1}{j}\binom bk\) characters with these values and proving both multiplier and nullity formulas.

For even-cardinality intervals, any Fourier zero gives \(N=X^2+Y^2\). Conversely suppose \(N=x^2+y^2\), with \(N\ge3\). When \(N\equiv0\pmod4\), both coordinates are even, matching the parity of \(a=b=N/2\). When \(N\equiv2\pmod4\), both coordinates are odd, matching \(a=b=N/2\). When \(N\equiv1\pmod4\), one coordinate is odd and the other even, matching \(a=(N+1)/2\) and \(b=(N-1)/2\) after swapping. No representation exists when \(N\equiv3\pmod4\). For \(N\ge6\), each coordinate has absolute value at most \(\sqrt N\le\lfloor N/2\rfloor\); at \(N=4\) and \(N=5\) the relevant representations \(4=0^2+2^2\) and \(5=1^2+2^2\) satisfy the bounds directly. Change signs to make both coordinates nonnegative. Hence the matched \((X,Y)\) lies in the allowed parity-and-magnitude ranges, and \(X\neq-a\) automatically because \(X\ge0\), so its prefix-sign pattern exists. This proves the if-and-only-if. The prime-exponent reformulation is the classical sum-of-two-squares theorem.

For odd-cardinality intervals, \(XY=0\) is achievable precisely when at least one of \(a,b\) is even. The anchored sign \(\varepsilon_0=1\) does not prevent \(X=0\) for even \(a\ge2\). As \(a,b\) are both odd exactly when \(N\equiv2\pmod4\), odd-order convolution is invertible precisely when \(n\equiv1\pmod4\). Finally, on a finite abelian group the Walsh characters diagonalize XOR convolution, so its complex and real ranks equal the number of nonzero multipliers.

## Verification
The standalone `verify.py` uses two independent paths to every Walsh value for \(2\le n\le13\): direct enumeration of every interval of the stipulated parity and direct character evaluation on its incidence vector, versus the claimed prefix-sign formulas. It compares every one of the \(2^n\) frequencies for each parity. It also compares actual zeros with the binomial nullity sums, and checks the two arithmetic invertibility classifications up to \(n=999\) using exact integer arithmetic. All tests pass. The finite tests corroborate but do not replace the all-order proof above. Run with `python verify.py` using Python 3.10 or later; no third-party packages are required.

## Relationship to prior work
Székely and Wang enumerate subtrees of trees and identify the path as the minimum-count tree. Yan and Yeh provide a multivariate weighted-subtree generating function, including arbitrary vertex weights on a path. The present multipliers are specializations of that known general generating function, and the elementary interval sum itself is not asserted new. The contribution assessed here is the precise **all-frequency** Fourier-rank classification after restricting to even or odd subtree orders: a sum-of-two-squares resonance with explicit binomial nullities on the even side, contrasted with a modulo-four invertibility law on the odd side. The standard sum-of-two-squares characterization is used, not claimed. The full-rank outcome for even-order paths cannot be read off merely from the ordinary subtree counts.

## Limitations
The theorem concerns path graphs and the two parity-restricted subpath families only; it does not characterize arbitrary trees, mixed weighted intervals, sharp endpoint projection norms, or spectral conditioning. Priority remains subject to discovery of an unindexed equivalent signed-parity-subpath study. No external independent validation has been performed.

## References
- L. A. Székely and H. Wang, *On subtrees of trees*, Advances in Applied Mathematics 34 (2005), 138–155; available online 2004-09-15. https://doi.org/10.1016/j.aam.2004.07.002
- W. Yan and Y.-N. Yeh, *Enumeration of subtrees of trees*, arXiv:math/0609475, first posted 2006-09-17. https://arxiv.org/abs/math/0609475
- P. Tittmann, I. Averbouch, and J. A. Makowsky, *The enumeration of vertex induced subgraphs with respect to the number of components*, European Journal of Combinatorics 32 (2011), 954–974. https://doi.org/10.1016/j.ejc.2011.03.017
- Classical sum-of-two-squares theorem, including the criterion for prime divisors congruent to \(3\pmod4\); for a modern statement, see https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
