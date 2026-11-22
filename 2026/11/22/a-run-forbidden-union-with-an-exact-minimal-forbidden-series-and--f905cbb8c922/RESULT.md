# A run-forbidden union with an exact minimal-forbidden series and two entropy-maximizing phases

## Finding
For each integer \(m\ge 2\), let \(Y_m^{(0)}\subseteq\{0,1\}^{\mathbb Z}\) be the two-sided subshift avoiding the word \(0^m\), let \(Y_m^{(1)}\) avoid \(1^m\), and set \(X_m=Y_m^{(0)}\cup Y_m^{(1)}\). Write \(\mathcal M_m(n)\) for the set of minimal forbidden factors of length \(n\) of \(X_m\), and \(M_m(n)=|\mathcal M_m(n)|\).

The complete minimal-forbidden-word generating function is
\[
\sum_{n\ge1}M_m(n)z^n=\frac{2z^{2m}}{1-(z+z^2+\cdots+z^{m-1})^2}.
\]
In particular, these minimal forbidden words are infinite in number, so \(X_m\) is strictly sofic (sofic but not of finite type).

For each integer \(r\ge 1\), let \(\lambda_r\) denote the unique real number \(\lambda\ge1\) satisfying \(\sum_{j=1}^r\lambda^{-j}=1\) (thus \(\lambda_1=1\)). Then
\[
 h_{\mathcal M}(X_m)=h_{\mathrm{top}}(Y_m^{(0)}\cap Y_m^{(1)})=\log\lambda_{m-1}
 < h_{\mathrm{top}}(X_m)=\log\lambda_m.
\]
There are exactly two ergodic measures of maximal entropy on \(X_m\): the distinct Parry measures of the two mixing finite-type components \(Y_m^{(0)}\) and \(Y_m^{(1)}\). Both are Bernoulli. All maximal-entropy invariant measures are their convex combinations.

The strict entropy gap \(\Delta_m=\log(\lambda_m/\lambda_{m-1})\) tends to zero and satisfies
\[
\Delta_m\sim 2^{-m-1}\qquad(m\to\infty).
\]
Thus the minimal-forbidden entropy equals the entropy of the *overlap* of the two phases, despite the ambient system having exactly two ergodic maximal-entropy phases and an arbitrarily small positive entropy gap.

## Assumptions and scope
All sequences are indexed by \(\mathbb Z\) and carry the left shift. The subshifts are defined over the binary alphabet, and \(m\) ranges over all integers at least two. For a subshift \(Z\), its language \(\mathcal L(Z)\) comprises every finite factor of a point of \(Z\). A word \(w\notin\mathcal L(Z)\) is minimal forbidden when every proper contiguous factor lies in \(\mathcal L(Z)\); equivalently, both its proper length-\((|w|-1)\) prefix and suffix lie in \(\mathcal L(Z)\). The entropy \(h_{\mathcal M}(Z)\) is \(\limsup_{n\to\infty}n^{-1}\log|\mathcal M_Z(n)|\), with logarithms natural. The value at finitely many empty levels does not affect the limsup.

We make no claim that the entropy of arbitrary generating forbidden sets equals the minimal-forbidden entropy: only the standard inequality \(h_G(X_m)\le h_{\mathcal M}(X_m)\) is needed. Nor is the existence of a finite maximal-entropy phase count new in general; the contribution is an explicit family and all-parameter exact count, equal-overlap entropy identity, and sharp vanishing-gap law.

## Proof
**1. Language and minimal forbidden words.** A binary finite word can be extended to a bilateral point of \(Y_m^{(0)}\) precisely when it avoids \(0^m\): extend both ends with ones. The analogous assertion holds for \(Y_m^{(1)}\). Hence a finite word lies outside \(\mathcal L(X_m)\) if and only if it contains *both* \(0^m\) and \(1^m\).

Suppose \(w\) is minimal forbidden. Removing its final symbol must remove at least one of the two forbidden constant runs, and removing its first symbol must remove the other: a single run cannot lose its occurrence upon both deletions unless it spans the entire word, which is impossible when both symbols are present. Thus \(w\) begins with exactly \(m\) equal symbols of one kind and ends with exactly \(m\) equal symbols of the other kind, without any further occurrence of either long constant run. Conversely, any word with these properties contains both long runs, while deleting the first or last symbol eliminates one of them, so it is minimal forbidden.

Choose the orientation starting with \(0^m\) and ending with \(1^m\). Every such word has the unique form \(0^m v1^m\), where either \(v\) is empty or it begins with \(1\), ends with \(0\), and every maximal constant run of \(v\) has length between one and \(m-1\). The opposite orientation is obtained by interchanging symbols. For a nonempty \(v\), its successive maximal runs occur in alternating \(1,0\) pairs, each with independently chosen length in \(\{1,\ldots,m-1\}\). Therefore, with \(R_m(z)=\sum_{j=1}^{m-1}z^j\), the inner-word series is \(\sum_{k\ge0}R_m(z)^{2k}=1/(1-R_m(z)^2)\). The two orientations and the \(2m\) fixed terminal symbols yield the stated formula. In particular, for each \(k\ge0\), there are minimal forbidden words of length \(2m+2k\), proving infinitely many such factors.

**2. Minimal-forbidden entropy.** For \(m\ge3\), the power series above has nonnegative coefficients and its positive radius \(\rho_m\in(0,1)\) is the unique solution of \(R_m(\rho_m)=1\). The Cauchy–Hadamard formula, and the fact that the numerator does not cancel this singularity, imply
\[
h_{\mathcal M}(X_m)=-\log\rho_m=\log\lambda_{m-1}.
\]
For \(m=2\), the series is \(2z^4/(1-z^2)\), so its coefficients have subexponential growth and \(h_{\mathcal M}(X_2)=0=\log\lambda_1\).

**3. Component and overlap entropies.** The finite-state presentation of \(Y_m^{(0)}\) records the current terminal \(0\)-run length in \(\{0,1,\ldots,m-1\}\); reading \(1\) resets this to zero, and reading \(0\) increments it unless already at \(m-1\). Its adjacency matrix is primitive: every state connects to zero by one \(1\), zero connects to every state by zeros, and zero has a self-loop. The familiar \(m\)-step Fibonacci recurrence for avoidance of \(0^m\) has Perron root \(\lambda_m\), determined by \(\sum_{j=1}^{m}\lambda_m^{-j}=1\). Thus each component has entropy \(\log\lambda_m\) and a unique mixing (hence Bernoulli) Parry measure. The union has the maximum of its component entropies, \(h_{\mathrm{top}}(X_m)=\log\lambda_m\).

The intersection is the bounded-run shift in which both \(0\)- and \(1\)-runs have length at most \(m-1\). Each successive \(0\)-run/\(1\)-run pair has length series \(R_m(z)^2\), and allowing arbitrary boundary fragments changes finite-word counts by at most polynomial factors; hence its exponential growth rate is the reciprocal of the least positive solution of \(R_m(z)^2=1\), which is \(\rho_m^{-1}=\lambda_{m-1}\). This also holds at \(m=2\), where the intersection is the two-point alternating orbit. Therefore its entropy is \(\log\lambda_{m-1}\). Strict inequality follows because \(\lambda_r\) increases strictly with \(r\), as the defining sums do.

**4. Exactly two maximal measures.** Since both components are closed and shift-invariant, for any ergodic invariant probability measure \(\mu\) on \(X_m\), the measurable invariant event \(Y_m^{(0)}\) has probability zero or one. If this probability is one, \(\mu\) is supported there; otherwise it is supported on \(Y_m^{(1)}\). To have entropy \(\log\lambda_m\) it must equal that component's unique Parry maximal-entropy measure. The two measures are distinct: otherwise their common support lies in the intersection, whose entropy is strictly smaller. Conversely both Parry measures have entropy \(h_{\mathrm{top}}(X_m)\), so these are exactly the two ergodic maximizers. Ergodic decomposition gives all maximal-entropy measures as their convex combinations.

**5. Vanishing gap.** For \(r\ge2\), the defining equation is equivalent to \(2-\lambda_r=\lambda_r^{-r}\). The increasing sequence \(\lambda_r\) converges to two; since \(\lambda_r\ge\lambda_2=(1+\sqrt5)/2\), \(r(2-\lambda_r)\to0\). Consequently
\[
2-\lambda_r=2^{-r}(1+o(1)),
\]
and
\[
\Delta_m=\log\frac{2-(2-\lambda_m)}{2-(2-\lambda_{m-1})}
\sim\frac{2^{-(m-1)}-2^{-m}}2=2^{-m-1}.
\]
All assertions follow.

## Verification
The standalone Python 3 script `CHECKER.py` independently enumerates all binary words for \(2\le m\le5\), \(1\le n\le16\), tests minimal-forbidden status through prefix/suffix language membership, and compares the exact counts with coefficients obtained by formal-power-series recursion. It passes all 64 parameter-length comparisons. This finite computation is a regression check; the infinite-domain result is proved by the preceding arguments and not inferred from enumeration.

For illustration, at \(m=3\) the counts for lengths six through ten are \(2,0,2,4,4\). The general series gives each coefficient exactly, without finite truncation.

## Relationship to prior work
Wu and Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts* (arXiv:2611.03758v1, first public November 2, 2026), establish that \(h_G<h_{\mathrm{top}}\) implies finitely many ergodic maximal-entropy measures, Bernoulli up to a finite period. Their general theorem implies *finiteness* for the present family because \(h_G\le h_{\mathcal M}<h_{\mathrm{top}}\), but does not count the phases or provide the family-specific minimal-forbidden series and overlap-entropy equality. Their Examples 1 and applications concern other constructions.

Béal, Crochemore, Mignosi, Restivo, and Sciortino, *Computing forbidden words of regular languages* (2003), provide an algorithm for a regular factorial language's minimal forbidden words, and the general fact that the resulting enumeration is rational. The result here does not claim rationality or algorithmic computability as novel. It identifies a uniform closed form for a natural binary union, its entropy equality to the phase intersection, the exact phase count and the asymptotically sharp entropy gap. Standard finite-type Perron–Frobenius and Parry-measure results are invoked, not claimed as discoveries.

Related results on two maximizing phases for antisquare-good shifts and modular spacing shifts address different languages and do not state this forbidden-run union formula. Previous work on correlation polynomials for one forbidden word supplies classical component entropy techniques but not the present mixed minimal-obstruction identity.

## Limitations
The theorem is confined to the specified binary union of two complementary single-run avoidance shifts, for integer \(m\ge2\). It is not an arbitrary-union theorem, nor does it establish equality of \(h_G\) with \(h_{\mathcal M}\). The general phenomenon of multiple maximal-entropy measures for reducible sofic systems is classical. The novelty claim is the precise family-wide quantitative characterization; unindexed older examples might contain an equivalent closed formula. No independent audit has been performed.

## References
- X. Wu and X. Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758v1 (2026), https://arxiv.org/abs/2611.03758.
- M.-P. Béal, M. Crochemore, F. Mignosi, A. Restivo, and M. Sciortino, *Computing forbidden words of regular languages*, Fundamenta Informaticae 56 (2003), https://doi.org/10.3233/FUN-2003-561-208.
- N. Agarwal, H. Cheriyath, S. N. Tikekar, *A combinatorial approach to study subshifts associated with multigraphs*, arXiv:2211.06068, https://arxiv.org/abs/2211.06068. (General transfer and Perron methodology.)
- W. Parry, *Intrinsic Markov chains*, Transactions of the AMS 112 (1964), 55–66. (Uniqueness of maximal entropy measures for mixing shifts of finite type.)
