# Sharp inverse ambiguity of \(q\)-ary palindromic fingerprints

## Finding

Fix integers \(q\ge4\) and \(n\ge2\). On an alphabet \(\Sigma\) of \(q\) distinct symbols, record for a word \(w\in\Sigma^n\) the maximal palindrome radius at every one of its \(2n-1\) letter and interletter centers. Write this full ordered observation as \(\mathsf M(w)\), and write \(\mathcal F(F)=\{w\in\Sigma^n: \mathsf M(w)=F}\) for the inverse fiber of an attainable fingerprint.

Then the maximum fiber size is

\[
\max_F |\mathcal F(F)|=q(q-1)(q-2)^{n-2}.
\]

Exactly one fingerprint attains the maximum: every even-center radius is zero and every odd-center palindrome consists only of its center letter. Its fiber consists precisely of words in which a letter differs from the preceding one and, wherever defined, from the letter two places earlier. Thus the largest ambiguity is realized by strings with no palindromic substring of length at least two. The maximizing fingerprint is unique even though its realizations are numerous.

## Assumptions and scope

Positions are indexed \(1,\ldots,n\). A center is either an integer position \(i\), with radius counted in letters and obligatory radius one, or an interletter center \(i+1/2\), with radius zero when the two adjacent letters differ. Equivalently, \(\mathsf M(w)\) specifies, for every contiguous interval, whether that substring is a palindrome: such an interval is palindromic exactly when its radius does not exceed the maximum radius at the same center. Equality of fingerprints is equality at all ordered centers, not equality of unordered palindrome lengths or mere counts.

The theorem concerns every fixed labeled alphabet of cardinality \(q\ge4\), with \(n\ge2\). No probability distribution is assumed. There is no claim for \(q\le3\).

## Proof

**1. Prefix observations are determined.** If two words have equal full fingerprints, their prefixes of any fixed length have equal fingerprints: at a center the prefix maximal palindrome is obtained by truncating the full center radius at the prefix boundary. More directly, the full array determines every palindrome/no-palindrome predicate for every interval, including intervals in each prefix.

**2. At most \(q-2\) continuations of a nonconstant prefix.** Let \(u\) be a fixed nonconstant prefix ending in a maximal constant run \(a^r\), preceded by \(b\ne a\). Let \(z\in\Sigma\) be the next letter, and suppose the fingerprint of the extended prefix \(uz\) is prescribed. The terminal length-two substring is a palindrome precisely when \(z=a\). If not, the terminal substring \(ba^rz\) is a palindrome precisely when \(z=b\): the middle run is symmetric and its two endpoint letters must agree. These are predicates read from the specified fingerprint. If either palindrome is required, there is exactly one choice of \(z\). If neither is allowed, then \(z\notin\{a,b\}\), leaving at most \(q-2\) choices. Since \(q\ge4\), in every case there are at most \(q-2\) compatible letters, with a strict reduction to one choice whenever one of these two terminal palindromes is forced.

**3. Bound every fiber.** Fix an attainable full fingerprint \(F\). It determines the number \(t\in\{1,\ldots,n\}\) of identical initial letters before the first change, taking \(t=n\) for a constant word, because it determines equality of each adjacent pair. If \(t=n\), the fiber has exactly \(q\) constant words. If \(t<n\), the constant initial symbol has \(q\) choices and the first different symbol has \(q-1\) choices. All further prefixes are nonconstant, so Step 2 bounds the fiber size by

\[
|\mathcal F(F)|\le q(q-1)(q-2)^{n-t-1}.
\]

When \(t\ge2\), this is strictly less than \(q(q-1)(q-2)^{n-2}\), since \(q-2\ge2\). When \(t=1\), it yields the claimed universal upper bound. A completely constant fiber also falls strictly below the stated maximum because \(q(q-1)>q\).

**4. Attainment and uniqueness.** Suppose \(t=1\). At every further position, a step forcing \(z=a\) or \(z=b\) in Step 2 admits only one letter instead of \(q-2\ge2\); the whole fiber is then strictly smaller than the upper bound. Hence equality is possible only if every continuation forbids both equalities, at every prefix. Starting from two distinct letters, these inequalities say exactly that \(w_i\ne w_{i-1}\) and \(w_i\ne w_{i-2}\) whenever their indices exist. Conversely, any such word has no length-two or length-three palindrome. Every longer palindrome contains a palindrome of length two or three at its center, so no longer palindromic substring is possible. All these words therefore have the same fingerprint consisting only of trivial one-letter palindromes. Their number, obtained by first choosing \(q\), then \(q-1\), then \(q-2\) at each later position, is exactly \(q(q-1)(q-2)^{n-2}\). Every other fingerprint has smaller fiber. For \(n=2\), the same calculation applies directly: the unequal-pair fingerprint has \(q(q-1)\) realizations, versus \(q\) for the equal-pair fingerprint. This completes the proof.

## Verification

The standalone program `verify.py` independently constructs fingerprints (i) by expanding palindromes around every center and (ii) by testing all substrings for palindromicity on the smaller ranges. It exhaustively groups all \(q^n\) words by their radius fingerprints and checks that the unique largest group has the claimed size and trivial-palindrome signature. The replayed finite ranges are \(q=4\), \(2\le n\le9\); \(q=5\), \(2\le n\le8\); and \(q=6\), \(2\le n\le7\). Run `python3 verify.py` with the standard library. These computations test concrete cases; the four-step proof, not the finite experiment, establishes the infinite family.

## Relationship to prior work

I, Inenaga, Bannai and Takeda's SPIRE 2010 work introduces counting and reconstruction from maximal palindrome information, and its accessible abstract announces enumeration of distinct fingerprints for alphabets of size at most three. The 2013 palindrome-pattern-matching work develops matching algorithms for palindromic equivalence, not this all-alphabet inverse-fiber extremum. Kim and Han's 2014/2016 work develops online multiple palindrome-pattern matching. Itzhaki's 2025 preprint proves a bijection between reconstructions and proper colorings of a fingerprint-associated restriction graph, and studies alphabet requirements and fingerprint enumeration; its inspected theorem statements do not identify this sharp maximum number of colorings over all fingerprints. In particular, an all-colorings correspondence does not imply the displayed sharp bound or unique extremal fingerprint without further analysis. This result adds a separate worst-case inverse-multiplicity invariant and a direct prefix proof. A full text of the 2010 chapter could not be retrieved and historical-priority uncertainty remains.

## Limitations

The theorem does not determine the number of distinct fingerprints or the size distribution of all their fibers. It does not extend the uniqueness assertion to smaller alphabets. Historical priority has not been independently established, and the inaccessible 2010 chapter is a residual comparison risk. No independent validation has been performed.

## References

1. T. I, S. Inenaga, H. Bannai, M. Takeda, *Counting and Verifying Maximal Palindromes*, SPIRE 2010, LNCS 6393, 135–146, DOI: https://doi.org/10.1007/978-3-642-16321-0_13 .
2. T. I, S. Inenaga, M. Takeda, *Palindrome Pattern Matching*, Theoretical Computer Science 483 (2013), 162–170, DOI: https://doi.org/10.1016/j.tcs.2012.01.047 .
3. H. Kim, Y. S. Han, *OMPPM: Online Multiple Palindrome Pattern Matching*, Bioinformatics 32 (2016), 1151–1157, https://academic.oup.com/bioinformatics/article/32/8/1151/1744595 .
4. M. Itzhaki, *Combinatorics of Palindromes*, arXiv:2507.13671 (2025), https://arxiv.org/abs/2507.13671 .
