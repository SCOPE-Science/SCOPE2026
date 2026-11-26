# Six-point affine-circuit threshold for the Boolean Fourier algebra norm

## Finding
Let \(G=\mathbb F_2^d\), with \(d\ge3\), and write \(N=|G|=2^d\). For an indicator \(1_A\), use the normalized Walsh transform
\[
\widehat{1_A}(\xi)=\frac1N\sum_{a\in A}(-1)^{\xi\cdot a},\qquad
\|1_A\|_{\mathcal A}=\sum_{\xi\in G}|\widehat{1_A}(\xi)|.
\]
The complete six-element profile is as follows. An *affine circuit* is a minimally affinely dependent subset over \(\mathbb F_2\). Let \(r=\dim\operatorname{aff}(A)\). The unique dependence when \(r=4\) is an even-cardinality circuit of length four or six.

| Geometry of a six-point set \(A\) | \(\|1_A\|_{\mathcal A}\) | Number of such subsets of \(G\) |
| --- | ---: | ---: |
| \(r=3\) | \(3/2\) | \(N(N-1)(N-2)(N-4)/48\) |
| \(r=4\), four-element affine circuit | \(7/4\) | \(N(N-1)(N-2)(N-4)(N-8)/48\) |
| \(r=4\), six-element affine circuit | \(9/4\) | \(N(N-1)(N-2)(N-4)(N-8)/720\) |
| \(r=5\), affine independence | \(15/8\) | \(N(N-1)(N-2)(N-4)(N-8)(N-16)/720\) |

The four counts sum to \(\binom N6\); a row with an unavailable affine dimension has count zero. Every set of at most five points satisfies \(\|1_A\|_{\mathcal A}\le15/8\). Thus **six is the minimum possible indicator-support cardinality for Fourier algebra norm exceeding two**, and the threshold is exceeded exactly by six-element affine circuits. Such circuits occur precisely in dimensions \(d\ge4\).

## Assumptions and scope
All sets are subsets of a *binary vector space*, not of an arbitrary finite abelian group. Each element of \(A\) occurs exactly once, all Fourier coefficients are normalized by \(N^{-1}\), and the norm is the sum of their absolute values, not an operator spectral norm. Fourier norms and the classification are invariant under affine automorphisms and embedding in higher binary dimensions: a translation changes only character phases, a linear transformation permutes frequencies, and embedding repeats local unnormalized Walsh coefficients by the annihilator multiplicity.

For a six-point set the affine dimension must lie in \(\{3,4,5\}\). If it is four, there is exactly one nontrivial affine dependence, whose coefficient support has even size at least four. These conditions exhaust the geometry.

## Proof
**1. Affine normal forms.** Write \(e_j\) for the standard binary basis and use the integer bit representations in the verification artifact. Up to an affine automorphism, the four cases admit the following representatives:
\[
\begin{array}{c|l}
\text{type}&A\\\hline
r=3&\{0,e_1,e_2,e_1+e_2,e_3,e_1+e_3\}\\
r=4\text{ with a four-circuit}&\{0,e_1,e_2,e_1+e_2,e_3,e_4\}\\
r=4\text{ with a six-circuit}&\{0,e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}\\
r=5&\{0,e_1,e_2,e_3,e_4,e_5\}.
\end{array}
\]
Six points in an affine three-flat are the complement of two distinct points in its eight-element set, so all are equivalent. In affine dimension five, all six are independent and equivalent. In affine dimension four, translate one point to the origin and choose an affine basis from the set; the remaining point produces the unique affine dependence. Its even support must have size four or six, yielding the displayed normal forms after relabeling.

**2. Fourier magnitudes.** On the character group of each minimal affine span, form the *unnormalized* integer sum \(W_A(\xi)=\sum_{a\in A}(-1)^{\xi\cdot a}\). Direct substitution into the four normal forms gives these complete absolute-value histograms, with the notation \(v^{\times m}\) for \(m\) occurrences of \(v\):
\[
\begin{array}{c|l|c}
\text{type}&\{|W_A(\xi)|\}_{\xi}&\frac{1}{2^r}\sum_\xi|W_A(\xi)|\\\hline
r=3&\{6,2^{\times3},0^{\times4}\}&12/8=3/2\\
r=4,\ 4\text{-circuit}&\{6,4^{\times2},2^{\times7},0^{\times6}\}&28/16=7/4\\
r=4,\ 6\text{-circuit}&\{6,2^{\times15}\}&36/16=9/4\\
r=5&\{6,4^{\times6},2^{\times15},0^{\times10}\}&60/32=15/8.
\end{array}
\]
For example, the six-circuit representative has the signed Walsh polynomial
\[
1+s_1+s_2+s_3+s_4+s_1s_2s_3s_4,\quad s_j\in\{-1,1\}.
\]
It is six when every sign is positive and has absolute value two at each of the other fifteen inputs. The other histograms follow similarly from the normal forms; in the first case they also follow by subtracting a two-point indicator from an affine three-flat. The embedding invariance from the preceding section proves the norm claims in every dimension.

**3. Exact census.** The number of affine three-flats is \(2^{d-3}{d\brack3}_2\), and each contains \(\binom86=28\) six-sets; each six-set of affine dimension three belongs to a unique such flat. This yields the first polynomial. The number of affine four-flats is \(2^{d-4}{d\brack4}_2\). Within a fixed one, there are \(\binom{16}{6}=8008\) six-sets. Of these, \(30\binom86=840\) lie in affine three-flats. A six-circuit arises from an affinely independent five-subset by adjoining its unique affine-dependent sixth point, and every six-circuit is produced from exactly six five-subsets. Hence there are
\[
\frac1{6}\frac{16\cdot15\cdot14\cdot12\cdot8}{5!}=448
\]
six-circuits in that four-flat. The remaining \(8008-840-448=6720\) span it with a four-circuit. Multiplication by the number of four-flats gives the second and third polynomial counts. The final case counts unordered affinely independent six-tuples as
\[
\frac{N(N-1)(N-2)(N-4)(N-8)(N-16)}{6!}.
\]
The formulas also sum algebraically to \(\binom N6\).

**4. Sharp onset.** The lower cardinalities are classified by the same affine-normal-form argument. For one and two points the norm is one; for three points it is \(3/2\); for four points it is either one (affine plane) or \(3/2\) (affinely independent); for five points it is \(7/4\) in affine dimension three and \(15/8\) in affine dimension four. Each value follows from evaluating the corresponding Walsh polynomial, or, for five points in a three-flat, complementing a three-point set. No set of at most five points reaches norm two. The six-circuit representative shows that a six-point set can have norm \(9/4\) whenever \(d\ge4\), and the six-point classification proves uniqueness of its affine geometry.

## Verification
The accompanying standalone `checker.cpp` calculates binary affine ranks and all unnormalized Walsh coefficients using exact integers. It enumerates **every** subset of sizes one through six for \(d=3,4,5\) and checks the asserted norm against the rank-and-circuit classification. For six-point subsets it verifies the four multiplicities, in norm order \(3/2,7/4,15/8,9/4\), as:
\[
\begin{array}{c|rrrr}
d&3/2&7/4&15/8&9/4\\\hline
3&28&0&0&0\\
4&840&6720&0&448\\
5&17360&416640&444416&27776.
\end{array}
\]
Compile with `g++ -O2 -std=c++17 checker.cpp -o checker` and execute `./checker`; successful completion prints `CHECK_PASS`. The finite enumeration corroborates the proof; the proof of the infinite-dimensional assertion is the affine classification and closed counting argument, not extrapolation.

## Relationship to prior work
The Fourier algebra norm here is the indicator-function \(\ell^1\) Fourier norm studied by Cheung, Hatami, Zhao, and Zilberstein in *Boolean functions with small approximate spectral norm* (ECCC TR22-041, first public release March 23, 2022), and in earlier work of Green–Sanders and Shpilka–Tal–Volk. Those works provide structural and complexity bounds in terms of spectral norms and affine connectivity, rather than the four exact six-point classes, their frequencies, and the least support-size threshold above two. Xie–Xu–Xu classify Fourier-coefficient patterns with a restricted amplitude set; their hypotheses exclude the \(3/8\) coefficient of the normalized six-circuit representative. These distinctions are comparisons of statements, not a claim that all older Boolean-function tables have been exhausted.

## Limitations
The result is confined to indicator functions on binary vector spaces and to support sizes at most six (complete classification at six). It asserts neither a corresponding threshold for other groups nor a bound for all support cardinalities. Exhaustive computation was performed only in dimensions three through five; the general proof is symbolic. Although specific relevant theoretical papers were inspected, equivalent older tabulations of affine Boolean-function orbits cannot be fully excluded without broader bibliographic examination. No independent mathematical validation has been performed.

## References
1. T. M. Cheung, H. Hatami, R. Zhao, I. Zilberstein, *Boolean functions with small approximate spectral norm*, Electronic Colloquium on Computational Complexity TR22-041 (2022), https://eccc.weizmann.ac.il/report/2022/041/ ; https://eccc.weizmann.ac.il/report/2022/041/download .
2. B. Green, T. Sanders, *Boolean functions with small spectral norm*, Geometric and Functional Analysis 18 (2008), 144–162; https://arxiv.org/abs/math/0605524 .
3. A. Shpilka, A. Tal, B. L. Volk, *On the structure of Boolean functions with small spectral norm*, https://arxiv.org/abs/1304.0371 .
4. N. Xie, S. Xu, Y. Xu, *A generalization of a theorem of Rothschild and van Lint*, https://arxiv.org/abs/2103.16811 .
