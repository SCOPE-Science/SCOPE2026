# Exact endpoint norms of the quadratic Specht Fourier block on \(S_n\)

## Finding
For every integer \(n\ge4\), let \(G=S_n\) and let \(P_n\) be the central Fourier projection on complex-valued functions on \(G\) corresponding to its irreducible Specht representation indexed by \((n-2,2)\). Write \(a_m\) for the number of permutations of \(m\) elements having no cycles of length one or two, with \(a_0=1\) and \(a_1=a_2=0\). Then the sharp endpoint operator norms satisfy
\[
\boxed{\|P_n\|_{\ell^1(G)\to\ell^1(G)}=\|P_n\|_{\ell^\infty(G)\to\ell^\infty(G)}=n(n-3)\left(\frac{a_{n-1}}{(n-1)!}+\frac{a_{n-2}}{2(n-2)!}\right).}
\]
Moreover,
\[
\boxed{\lim_{n\to\infty}\frac{\|P_n\|}{n(n-3)}=\frac32e^{-3/2}.}
\]
At each evaluation point, all \(\ell^\infty\)-norm extremizers are determined, up to one unimodular phase, by the signs of the \((n-2,2)\) character wherever that character does not vanish. The character is negative precisely on permutations with exactly one or two fixed points and no transpositions, where its value is \(-1\).

## Assumptions and scope
The Fourier projection acts on \(\ell^p(S_n;\mathbb C)\) with counting measure; this does not affect its operator norms because the same scalar normalization is used in domain and range. If \(\chi_n\) is the real character of the irreducible module and \(d_n=n(n-3)/2\) its degree, our normalization is
\[
(P_nf)(x)=\frac{d_n}{n!}\sum_{y\in S_n}\chi_n(y^{-1}x)f(y).
\]
The pair-permutation module has exactly three Fourier components: constants, the standard representation, and this quadratic Specht representation. The endpoint projection norm measures the sharp amplification when retaining only the last component in a bounded observable on permutations. The claim holds for all integers \(n\ge4\), without an asymptotic or genericity restriction. For \(\sigma\in S_n\), \(X_j(\sigma)\) denotes the number of cycles of length \(j\) in its disjoint-cycle decomposition.

## Proof
**(1) Character and degree.** Consider the permutation module \(V\) on the unordered two-element subsets of \([n]\). Its permutation character counts the subsets fixed by \(\sigma\), giving \(\binom{X_1(\sigma)}2+X_2(\sigma)\). The point-permutation module \(W\) embeds into \(V\) by sending the basis vector at \(i\) to the sum of pairs incident to \(i\): injectivity follows because \(c_i+c_j=0\) for all distinct \(i,j\) forces every \(c_i=0\). The modules \(\mathbf1\) and the standard module are the two constituents of \(W\). The action on pairs has precisely three orbitals, distinguished by whether two pairs meet in zero, one, or two points; therefore \(\dim\operatorname{End}_{S_n}(V)=3\). Consequently, the orthogonal complement of \(W\) is one irreducible constituent, the classical Specht module \(S^{(n-2,2)}\), of degree \(d_n=\binom n2-n\). Its character is
\[
\chi_n(\sigma)=\binom{X_1(\sigma)}2+X_2(\sigma)-X_1(\sigma).
\]
This also verifies the asserted projector formula by finite-group character orthogonality.

**(2) Complete sign classification.** For nonnegative integers \(r,s\), the expression \(\binom r2-r+s=\frac12r(r-3)+s\) is negative exactly when \(r=1\) or \(r=2\) and \(s=0\). At each such pair its value is precisely \(-1\); at \(r=0\) and \(r\ge3\) it is nonnegative. Because \(\chi_n\) is a nontrivial irreducible character, \(\sum_{\sigma\in S_n}\chi_n(\sigma)=0\). Thus
\[
\frac1{n!}\sum_{\sigma\in S_n}|\chi_n(\sigma)|=2\Pr\bigl(X_1\in\{1,2\},\ X_2=0\bigr),
\]
where the probability is for a uniform permutation of \(n\) letters.

**(3) Exact coefficient and sharpness.** Choosing the one or two fixed points and then permuting the remaining points in cycles of size at least three gives
\[
\Pr\bigl(X_1\in\{1,2\},\ X_2=0\bigr)=\frac{a_{n-1}}{(n-1)!}+\frac{a_{n-2}}{2(n-2)!}.
\]
The cycle-containing-an-element recursion \(a_m=\sum_{j=3}^m\binom{m-1}{j-1}(j-1)!a_{m-j}\) gives a reproducible integer computation of these counts. Each row and column of the central convolution matrix has absolute sum \(d_n n!^{-1}\sum|\chi_n|\), which is the sharp \(\ell^\infty\) and \(\ell^1\) norm. For the \(\ell^\infty\) equality cases, fix an output \(x\in G\). Equality at \(x\) in the triangle inequality occurs exactly when, for all \(y\) with \(\chi_n(y^{-1}x)\ne0\),
\[
f(y)=\omega\operatorname{sgn}\bigl(\chi_n(y^{-1}x)\bigr),\qquad |\omega|=1,
\]
while the remaining values may be arbitrary of modulus at most one. Every endpoint extremizer has this form for at least one \(x\); this is also sufficient.

**(4) Limit.** The exponential generating function for permutations with all cycle lengths at least three is
\[
\sum_{m\ge0}\frac{a_m}{m!}z^m=\exp\left(\sum_{j\ge3}\frac{z^j}{j}\right)=\frac{e^{-z-z^2/2}}{1-z}.
\]
If \(e^{-z-z^2/2}=\sum_{j\ge0}c_jz^j\), then \(a_m/m!=\sum_{j=0}^m c_j\). Since the exponential function here is entire, its coefficient series converges absolutely at \(z=1\), so \(a_m/m!\to e^{-3/2}\). Substitution into the exact finite formula yields the claimed limit.

## Verification
A standalone standard-library Python program, `verify_pair_fourier.py`, verifies the character formula and negativity classes by exhaustive enumeration of permutations for every \(4\le n\le8\), independently counts permutations with no one- or two-cycles by cycle-containing-an-element recursion, and confirms the generating-function coefficients through \(n=11\). It also checks the central character convolution identity exactly over all group elements for \(n=4,5\). Sample exact endpoint norms are \(4/3\), \(25/6\), \(117/20\), \(406/45\), and \(850/63\) for \(n=4,5,6,7,8\). The infinite-family theorem rests on the proof, not on these finite computations.

## Relationship to prior work
Character polynomials, the permutation-module decomposition, and irreducible Fourier projection kernels are classical; they are not claimed as new. Church–Ellenberg–Farb (arXiv:1204.4533) and Wilson (arXiv:1503.08510) develop the general stable-character-polynomial framework. A previously published result on the standard Fourier block of doubly transitive actions expresses its endpoint norm through derangements, but concerns the different representation indexed by \((n-1,1)\). Published Johnson-scheme projection norms act on subset permutation spaces, not on the full regular representation of \(S_n\). The present specific second-Specht central projector norm, its restricted negative-character class, and its exact large-rank coefficient are not implied merely by those norm statements; the indicated character analysis supplies their evaluation.

## Limitations
Only the \(\ell^1\) and \(\ell^\infty\) endpoint norms are evaluated. This is not an assertion of sharp \(\ell^p\) norms for other exponents, nor of a representation-free bound for all irreducible projections. The literature comparison is bounded rather than a proof of historical priority; a broader published result on absolute character means could encompass the formula.

## References
1. T. Church, J. S. Ellenberg, B. Farb, *FI-modules and stability for representations of symmetric groups*, arXiv:1204.4533, first posted 2012-04-20; especially the character-polynomial and stable Specht discussion in Sections 3.3–3.4.
2. J. C. H. Wilson, *FI_W-modules and constraints on classical Weyl group characters*, arXiv:1503.08510, first posted 2015-03-30; especially Section 4.1 on character polynomials of symmetric groups.
3. Finite-group character orthogonality and the cycle-index exponential formula (classical foundations).
