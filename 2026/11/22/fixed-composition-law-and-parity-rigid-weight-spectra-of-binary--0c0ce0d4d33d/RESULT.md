# Fixed-composition law and parity-rigid weight spectra of binary Abelian-unbordered words

## Finding

A nonempty binary word is *Abelian-unbordered* if no nonempty proper prefix has the same number of zeroes and ones as the equally long suffix. For every integer \(n\ge 1\), define \(U_n(u)=\sum_{k=0}^n a_{n,k}u^k\), where \(a_{n,k}\) counts such indexed words of length \(n\) containing exactly \(k\) ones. Binomial coefficients outside their integer range are zero.

**Exact fixed-composition theorem.** For every integer \(m\ge1\),
\[
U_{2m}(u)=2\sum_{j=0}^{m-1}\binom{m-1}{j}^{\!2}u^{2j+1}
+2\sum_{j=0}^{m-2}\binom{m-1}{j}\binom{m-1}{j+1}u^{2j+2},
\qquad U_{2m+1}(u)=(1+u)U_{2m}(u),
\]
with \(U_1(u)=1+u\). These formulas specify every composition count, not only the totals. The support for \(n\ge2\) is exactly \(1\le k\le n-1\), and every support coefficient is positive.

**Shape and moment consequences.** For even lengths \(2m\ge4\), the positive coefficient string is log-concave; at every even interior index \(k\), \(a_{2m,k}^{2}=a_{2m,k-1}a_{2m,k+1}\), and at every odd interior index the inequality is strict. For odd lengths \(2m+1\ge5\), the positive coefficient string is strictly log-concave at every interior index. The boundary cases \(n=1,2,3\) follow directly from the displayed polynomials. Under a uniformly random Abelian-unbordered binary word, the Hamming weight \(W_n\) has
\[
\mathbb{E}W_{2m}=m,\qquad
\operatorname{Var}(W_{2m})=\frac{m(m-1)}{2m-1};\qquad
\mathbb{E}W_{2m+1}=m+\frac12,\quad
\operatorname{Var}(W_{2m+1})=\frac{m(m-1)}{2m-1}+\frac14.
\]

**Sharp composition-conditioned asymptotic.** For any sequence of integers \(k_m\) with \(k_m/(2m)\to p\in(0,1)\), the probability that a uniformly sampled binary word of length \(2m\) and weight \(k_m\) is Abelian-unbordered satisfies
\[
\frac{a_{2m,k_m}}{\binom{2m}{k_m}}\sim\frac{2\sqrt{p(1-p)}}{\sqrt{\pi m}}.
\]
The same leading asymptotic holds for length \(2m+1\) and any weights satisfying \(k_m/(2m+1)\to p\in(0,1)\). The approximation is uniform when the limiting density is restricted to a compact subinterval of \((0,1)\).

## Assumptions and scope

All words are literal indexed linear words over the labeled alphabet \(\{0,1\}\); no rotations, reversals or complementation are identified. Abelian equivalence means equality of both letter counts. Only nonempty proper borders are tested, and all formulae have their explicitly stated integer ranges. The asymptotic excludes densities tending to zero or one. These results do not count ordinary (exact-match) unbordered words, nor do they generalize to an alphabet of more than two symbols without additional work.

## Proof

**1. A reflected killed walk.** Fix \(m\ge1\), and for a word \(w=w_1\cdots w_{2m}\) set
\[
D_j=\sum_{i=1}^{j}(w_i-w_{2m+1-i}),\qquad 1\le j\le m.
\]
The length-\(j\) prefix and suffix are Abelian equivalent precisely when \(D_j=0\). Any border of length greater than \(m\) is accompanied by one of complementary length less than \(m\), so \(w\) is Abelian-unbordered exactly when all \(D_j\ne0\). The nonzero walk has either all positive heights or all negative heights. In the positive case, its first paired letters are necessarily \((1,0)\), contributing one one. For each later inward pair, \((1,0)\), \((0,1)\), \((0,0)\), \((1,1)\) contribute steps \(+1,-1,0,0\) of weights \(u,u,1,u^2\), respectively. Introduce the step polynomial
\[
Q(z,u)=u z+(1+u^2)+u z^{-1}=(1+uz)(1+u z^{-1}).
\]
For positive paths of total \(m\) inward pairs ending at any positive height, reflection at the first visit to height zero subtracts unrestricted paths started at height \(-1\) from those started at height \(+1\). Reflection preserves each step weight, including the two distinguishable horizontal cases. At terminal height \(h\ge1\), the surviving weight after the initial pair is
\[
u\bigl([z^{h-1}]Q(z,u)^{m-1}-[z^{h+1}]Q(z,u)^{m-1}\bigr).
\]
The sum over all \(h\ge1\) telescopes to \(u([z^0]+[z^1])Q(z,u)^{m-1}\), using \([z^{-r}]Q^{m-1}=[z^r]Q^{m-1}\). Swapping the two entries in every inward pair sends each positive path to a negative path, preserving that pair’s total number of ones (also for the horizontal pairs \(00\) and \(11\)). Thus negative paths contribute an identical weight polynomial. Consequently
\[
U_{2m}(u)=2u\bigl([z^0]+[z^1]\bigr)(1+uz)^{m-1}(1+u/z)^{m-1}.
\]
Expanding the two factors gives exactly the two binomial-product sums in the finding. An arbitrary middle bit is independent of every border comparison for odd length, so \(U_{2m+1}(u)=(1+u)U_{2m}(u)\). A length-one word has no proper border.

**2. Exact coefficient geometry.** Write \(b_j=\binom{m-1}{j}\) for \(0\le j\le m-1\). The coefficients have the alternating representation \(a_{2m,2j+1}=2b_j^2\) and \(a_{2m,2j+2}=2b_jb_{j+1}\). Thus each even-indexed interior coefficient is exactly the geometric mean of its two neighbors. For odd interior indices the inequality \(b_j^2>b_{j-1}b_{j+1}\) is strict by strict log-concavity of positive binomial coefficients. This proves even-length log-concavity with its complete equality set. Multiplication by \(1+u\) takes the coefficient string to adjacent sums. Directly expanding \((a_k+a_{k-1})^2-(a_{k-1}+a_{k-2})(a_{k+1}+a_k)\) gives two adjacent log-concavity deficits and the nonnegative cross term \(a_ka_{k-1}-a_{k-2}a_{k+1}\). At any interior index at least one of the two deficits is strictly positive (or a support-boundary term is positive). This proves strictness for odd lengths \(2m+1\ge5\).

**3. Moments.** Vandermonde's identity gives
\[
U_{2m}(1)=2\binom{2m-2}{m-1}+2\binom{2m-2}{m-2}=\binom{2m}{m}.
\]
The coefficient identity \(a_{2m,k}=a_{2m,2m-k}\) yields the mean \(m\). For the second falling moment, use, for \(r\in\{0,1,2\}\) and \(s\in\{0,1\}\),
\[
\sum_j (j)_r\binom{N}{j}\binom{N}{j+s}=(N)_r\binom{2N-r}{N+s},
\]
where \((j)_r\) denotes the falling factorial. This identity follows by replacing \((j)_r\binom Nj\) with \((N)_r\binom{N-r}{j-r}\) and applying Vandermonde. With \(N=m-1\), inserting the odd exponents \(2j+1\) and even exponents \(2j+2\) of the exact polynomial yields
\[
U_{2m}''(1)=\frac{2m^2(m-1)}{2m-1}\binom{2m}{m}.
\]
Thus \(\operatorname{Var}(W_{2m})=U_{2m}''(1)/U_{2m}(1)+m-m^2=m(m-1)/(2m-1)\). For odd lengths the freely chosen center bit is an independent fair Bernoulli variable, proving the remaining moment identities.

**4. Microcanonical asymptotic.** Let \(p_m=k_m/(2m)\), where \(p_m\) stays away from zero and one. Express each of the two parity cases for \(a_{2m,k_m}\) as a product of two neighboring binomial coefficients of order \(m-1\). Stirling's formula, uniformly on compact interior density intervals, gives
\[
\frac{a_{2m,k_m}}{\binom{2m}{k_m}}=
\frac{2\sqrt{p_m(1-p_m)}}{\sqrt{\pi m}}(1+O(m^{-1})).
\]
The adjacent two terms in \(a_{2m+1,k}=a_{2m,k}+a_{2m,k-1}\), normalized using Pascal's identity, are a convex mixture of the even-length probabilities at weights \(k\) and \(k-1\). Their leading expressions agree, proving the odd-length asymptotic.

## Verification

Run the two standard-library-only Python programs `verify/bruteforce.py` and `verify/path_dp.py` from this package. The first enumerates every binary word of lengths \(1\) through \(18\) and compares its shortest-border test with the coefficient formula. The second independently constructs weighted killed walks, tests all coefficients for \(m\le40\), and checks exact normalization, symmetry, moments, and the log-concavity equality/strictness assertions. These finite checks are supplementary: the statements for all integer lengths follow from the reflection and binomial proofs above. The asymptotic is proved using Stirling's formula; selected numerical comparisons are not a proof of a limit.

## Relationship to prior work

Rampersad, Rigo and Salimov (2013), followed by Goč, Rampersad, Rigo and Salimov (2014), established the binary *unweighted* Abelian-unbordered count through Motzkin and nonreturning-walk bijections. Their result is recovered upon setting \(u=1\). Blanchet-Sadri, Chen and Hawes (2017), Theorems 1–3, counted words by shortest Abelian-border length or number of borders, without fixing the total number of ones; its first-return argument explicitly uses Narayana numbers. The present result does not claim the older bijections, unweighted counts, or first-return Narayana numbers as new. It determines the entire *unbordered* fixed-content polynomial, the parity-exact equality set in its log-concavity, exact weight moments, and the density-dependent sharp fixed-weight probability. Harju and Nowotka (2005) studied ordinary equality-border fixed-weight enumeration, a different predicate. These methods are related, so an unnoticed equivalent reformulation remains possible.

## Limitations

No result is claimed about ordinary unbordered words, multiple-letter-alphabet refinements, or the density regimes \(k=o(n)\) and \(n-k=o(n)\). The log-concavity statement is for the displayed finite coefficient strings, not arbitrary word-language closure operations. An independent scientific audit has not been performed. Priority comparisons include the relevant accessible primary literature but cannot rule out every historical equivalent treatment; the 2005 ordinary-border paper was compared using its accessible abstract rather than its complete text.

## References

1. N. Rampersad, M. Rigo, P. Salimov, *On the Number of Abelian Bordered Words*, Developments in Language Theory (2013), author's full preprint at https://orbi.uliege.be/bitstream/2268/144646/1/finalDLT2013.pdf ; public repository listing https://orbi.uliege.be/handle/2268/144646 .
2. D. Goč, N. Rampersad, M. Rigo, P. Salimov, *On the Number of Abelian Bordered Words (with an Example of Automatic Theorem-Proving)*, International Journal of Foundations of Computer Science (2014); https://orbi.uliege.be/bitstream/2268/178701/1/numberAbelianBorder.pdf .
3. F. Blanchet-Sadri, K. Chen, K. Hawes, *Dyck Words, Lattice Paths, and Abelian Borders*, AFL 2017; https://arxiv.org/abs/1708.06461 .
4. T. Harju, D. Nowotka, *Counting bordered and primitive words with a fixed weight*, Theoretical Computer Science 340 (2005), 273–279, https://doi.org/10.1016/j.tcs.2005.03.040 .
