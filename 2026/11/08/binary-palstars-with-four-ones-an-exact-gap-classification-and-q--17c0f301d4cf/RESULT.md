# Binary palstars with four ones: an exact gap classification and quasipolynomial census

## Finding

A **palstar** is a finite word that is a concatenation of nonempty even-length palindromes. For every integer \(m\ge 2\), let \(P_m\) count indexed binary palstars of length \(2m\) containing exactly four occurrences of \(1\). Then

\[
\boxed{P_m=\frac{4m^4-4m^3+2m^2-8m+3-3(-1)^m}{24}.}
\]

The generating function, with the variable recording the number of *pairs of zero symbols*, is

\[
\boxed{\sum_{m\ge2}P_m x^{m-2}=\frac{1+5x+x^2+x^3}{(1-x)^5(1+x)}.}
\]

In particular, among binary length-\(2m\) words with exactly four ones, the proportion that are palstars tends to \(1/4\). This is a density within the weight-four slice, not among unrestricted binary words.

There is also an exact membership test involving only the five zero gaps, given below.

## Assumptions and scope

The alphabet is the *labeled* binary alphabet \(\{0,1\}\). Words are linear and indexed, not necklaces or reversal classes. Empty palindrome blocks are excluded; the empty word is irrelevant to positive weight. Each palindromic block has even length, hence contains an even number of ones.

Write any weight-four word uniquely as

\[
w=0^a1\,0^b1\,0^c1\,0^d1\,0^e,
\qquad a,b,c,d,e\in\mathbb Z_{\ge0}.
\]

For total length \(2m\), the gaps satisfy \(a+b+c+d+e=2m-4\). Put \(\alpha\in\{0,1\}\) for the parity of \(a\), and \(\beta\in\{0,1\}\) for the parity of \(e\).

**Complete structural criterion.** The word is a palstar if and only if at least one of these alternatives holds:

1. **Two positive blocks:** \(b\) and \(d\) are even, \(c\ge\alpha+\beta\), and \(c\equiv\alpha+\beta\pmod 2\).
2. **One positive block:** \(b=d\), \(c\) is even, and \(\alpha=\beta\).

The alternatives can overlap. All variables range over nonnegative integers, including empty zero runs.

## Proof

An even-length palindrome contains an even number of each symbol, by pairing symmetric positions. Therefore any palstar with exactly four ones has either (I) precisely one palindromic factor that contains all four ones, or (II) precisely two positive-one palindromic factors, each containing two ones. All other factors consist entirely of an even number of zeros. No third case is possible.

**Case II: two positive blocks.** A palindrome containing exactly two ones has the unique form \(0^r1\,0^{2s}1\,0^r\), for integers \(r,s\ge0\). Thus \(b,d\) must be even. Let \(r\) and \(t\) be the symmetric zero padding of the first and second positive blocks. Any remaining all-zero blocks must have even lengths, so

\[
a=2u+r,\qquad c=r+t+2v,\qquad e=2z+t
\]

for nonnegative \(u,v,z,r,t\). Necessarily \(r\equiv a\pmod 2\) and \(t\equiv e\pmod 2\). Consequently \(c\ge \alpha+\beta\) and \(c\equiv\alpha+\beta\pmod2\). Conversely, if these inequalities and congruences hold, choose \(r=\alpha\), \(t=\beta\), \(u=(a-\alpha)/2\), \(z=(e-\beta)/2\), and \(v=(c-\alpha-\beta)/2\). This explicitly constructs the required factorization. Hence alternative 1 is necessary and sufficient in Case II.

**Case I: one positive block.** A four-one even palindrome has equal first and third internal zero gaps and an even central zero gap, so \(b=d\) and \(c\) is even. Its outer symmetric zero padding is some \(r\), while all-zero factors outside it have even length: \(a=2u+r\), \(e=2z+r\). Thus \(\alpha=\beta\). Conversely, take \(r=\alpha\) and use the palindromic block \(0^r1\,0^b1\,0^c1\,0^b1\,0^r\), preceded and followed by the remaining even zero runs. Hence alternative 2 is necessary and sufficient in Case I.

To enumerate, let \(x\) mark one pair of zeros, so the exponent is \((a+b+c+d+e)/2=m-2\). In Case II, choose \(a=2u+\alpha\), \(e=2z+\beta\), \(c=\alpha+\beta+2v\), \(b=2s\), \(d=2t\). Summing all nonnegative parameters gives

\[
G_{II}(x)=\frac{(1+x)^2}{(1-x)^5}.
\]

In Case I, write \(b=d=j\), \(c=2v\), \(a=2u+\alpha\), \(e=2z+\alpha\). Hence

\[
G_I(x)=\frac{1+x}{(1-x)^4}.
\]

For the intersection, \(b=d=2s\), \(c=2v+2\alpha\), \(a=2u+\alpha\), \(e=2z+\alpha\); therefore

\[
G_{I\cap II}(x)=\frac{1+x^2}{(1-x^2)(1-x)^3}.
\]

Inclusion-exclusion gives

\[
G(x)=G_I(x)+G_{II}(x)-G_{I\cap II}(x)
=\frac{1+5x+x^2+x^3}{(1-x)^5(1+x)}.
\]

Extracting the coefficient of \(x^{m-2}\) by a partial fraction expansion yields the displayed quasipolynomial, valid also at \(m=2\). Its leading term is \(m^4/6\). Since \(\binom{2m}{4}\sim 2m^4/3\), the proportion tends to \(1/4\). All steps are exact, for every integer \(m\ge2\).

## Verification

Run `python3 verify.py` with Python 3 and only the standard library. It checks the structural criterion against a logically separate dynamic program that decides factorability by trying every even-palindromic block. The exhaustive part tests every weight-four word at lengths \(4,6,\ldots,22\) (18,832 words), and compares the observed counts with the quasipolynomial. It also checks the generating-function coefficient expressions at semilengths \(2\) through \(39\). A successful run prints `VERIFY_OK`. The direct dynamic program does not rely on the gap criterion.

The first counts \(P_m\), for \(m=2,\ldots,11\), are \(1,9,32,84,181,345,600,976,1505,2225\). Finite checks support but do not establish the infinite theorem; the case decomposition and generating-function algebra constitute the unrestricted proof.

## Relationship to prior work

Rampersad, Shallit and Wang (2010), *Inverse Star, Borders, and Palstars*, establish the general prime-palstar/unbordered-word correspondence and prime factorization, not a weight-four palstar classification. Richmond and Shallit (2013 preprint; 2014 journal), *Counting the Palstars*, give an unrestricted generating relation and total-count asymptotics, but neither the present five-gap membership criterion nor the weight-four quasipolynomial. OEIS A246019 records total binary palstar counts without fixing the number of ones. The present theorem solves a separate content-refined counting question by distinguishing the two positive-factor configurations and subtracting their overlap.

The global language results are stronger in a different direction; this statement does not claim to improve unrestricted total palstar enumeration. It gives explicit content-refined information not displayed in the inspected sources.

## Limitations

Only the binary weight-four slice and even word lengths are classified. The result does not enumerate all weight slices, all alphabets or the prime-palstar subset, and the limit \(1/4\) is conditional on exactly four ones. Existing general language identities can support alternative derivations; additional unindexed literature might contain an equivalent specialization. No independent mathematical audit has been carried out.

## References

1. N. Rampersad, J. Shallit, M.-w. Wang, *Inverse Star, Borders, and Palstars*, arXiv:1008.2440 (first posted 2010-08-14), https://arxiv.org/pdf/1008.2440 . Inspected Sections 2–3 and Theorems 3, 6.
2. L. B. Richmond, J. Shallit, *Counting the Palstars*, arXiv:1311.2318 (first posted 2013-11-10), published *Electronic Journal of Combinatorics* 21(3) (2014), P3.25, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i3p25/pdf/ . Inspected Sections 1–4 and especially Theorem 2.
3. OEIS Foundation, A246019, *Number of palstars of length \(2n\) over an alphabet of size \(2\)*, https://oeis.org/A246019 . Total-count table, not a fixed-weight table.
