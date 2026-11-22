# Power-sum overhead law for minimum-letter-restricted quasinecklaces

## Finding

Let \(s\ge2\) and consider the ordered alphabet \(\{0,1,\ldots,s\}\). Let \(Q_s(r,m)\) be the number of quasinecklaces with precisely \(r\ge1\) zeroes and \(m\ge0\) nonzero symbols, with no restriction on the nonzero content. For \(m\ge1\), put

\[
F_{L,t}(x)=s\sum_{j=0}^{L-1}x^j+(s-t+1)x^L
\qquad (L\ge1,\ 1\le t\le s).
\]

Then the entire minimum-letter-count spectrum is

\[
\boxed{Q_s(r,m)=\sum_{L=1}^{r}\sum_{t=1}^{s}[x^{r-L}]F_{L,t}(x)^{m-1}.}
\]

The boundary value is \(Q_s(r,0)=1\). Equivalently, its complete bivariate generating series is

\[
\sum_{r\ge1,m\ge0}Q_s(r,m)x^r y^m
=\frac{x}{1-x}+\sum_{L\ge1}\sum_{t=1}^{s}
\frac{x^L y}{1-yF_{L,t}(x)}.
\]

Let \(N_s(r,m)\) denote the number of ordinary necklace representatives among the same words, with \(n=r+m\). Then

\[
\boxed{N_s(r,m)=\frac1n\sum_{d\mid\gcd(r,m)}\varphi(d)
\binom{n/d}{r/d}s^{m/d}.}
\]

For each fixed \(s\ge2\) and \(r\ge2\), the exact limiting candidate-to-necklace ratio, as \(m\to\infty\), is

\[
\boxed{\lim_{m\to\infty}\frac{Q_s(r,m)}{N_s(r,m)}
=R_{s,r}=\frac{r}{s^r}\sum_{t=1}^s t^{r-1}.}
\]

For fixed \(s\), this limit is \(R_{s,r}\sim r/s\) as \(r\to\infty\). Thus a colexicographic quasinecklace generator can have arbitrarily large candidate/output overhead when restricted to a prescribed count of its smallest letter, even with the alphabet fixed and nonbinary. In the ternary case \(s=2\), \(R_{2,r}=r/2+r/2^r\). The special exact two-zero case, for \(m\ge2\), is

\[
Q_s(2,m)=s^m+\frac{(m-1)s(s+1)}2\,s^{m-2}.
\]

## Assumptions and scope

The *quasinecklace* notion is that of Gabrić and Sawada: if \(a\) is the least letter of a nonconstant word and \(L\) its greatest consecutive run length, the word begins with \(a^L\), ends with a letter greater than \(a\), and the successor of its initial \(a^L\) is no larger than the successor of every other complete run \(a^L\). Constant words qualify. The symbol \([x^j]\) extracts the coefficient of degree \(j\), and \(\varphi\) is Euler's totient function. We count literal linear representatives, not rotation classes, for \(Q_s\), and one lexicographically least representative per rotation class for \(N_s\). The source word contains zero because \(r\ge1\), so its least symbol really is zero.

The new nonbinary statement assumes \(s\ge2\). The binary specialization is a consistency check and is not claimed as a new binary result. All counts and asymptotics are valid for the quantified positive integer parameters; the limit keeps \(s,r\) fixed before allowing \(r\) to increase.

## Proof

**Exact quasinecklace spectrum.** Fix \(r\ge1,m\ge1\). Every admissible word has a unique initial zero-run \(0^L\), followed by its first nonzero letter \(t\), with \(1\le L\le r\) and \(1\le t\le s\). Its remaining \(m-1\) nonzero letters give a unique decomposition

\[
0^L t\;0^{j_1}b_1\;0^{j_2}b_2\cdots 0^{j_{m-1}}b_{m-1},
\qquad\sum_i j_i=r-L.
\]

Every exponent \(j_i\) lies between zero and \(L\), since \(L\) is maximal. When \(j_i<L\), the following letter \(b_i\) has exactly \(s\) possible values. When \(j_i=L\), the quasinecklace successor condition restricts it to \(t,t+1,\ldots,s\), giving \(s-t+1\) possibilities. These conditions are also sufficient: they enforce the maximal prefix run, all successor comparisons, and a nonzero final letter. Thus each of the \(m-1\) blocks contributes exactly \(F_{L,t}(x)\), and coefficient extraction gives the first boxed formula. The all-zero word supplies \(Q_s(r,0)=1\). Geometric summation over \(m\) proves the generating series as an identity of formal power series in \(x,y\) (each coefficient receives finitely many \(L\)-terms).

**Necklaces.** Apply Burnside's lemma to the cyclic group on \(n=r+m\) positions. A rotation with exactly \(d\) repetitions fixes a word of this content only if \(d\mid r\) and \(d\mid m\). For such a rotation, the repeated block has \(r/d\) zeros among \(n/d\) positions and its other entries have \(s\) choices, yielding \(\binom{n/d}{r/d}s^{m/d}\) fixed words. Exactly \(\varphi(d)\) rotations have repetition count \(d\). Dividing their sum by \(n\) proves the second boxed formula.

**Asymptotic overhead.** Fix \(s,r\ge2\). The term \(L=1\) in the exact spectrum is

\[
\binom{m-1}{r-1}s^{m-r}\sum_{t=1}^s t^{r-1}
\]

for \(m\ge r\). Indeed, after the initial zero, the other \(r-1\) zeros precede selected nonzero letters among the remaining \(m-1\) letters; if the initial successor is \(t\), their successors each have \(s-t+1\) possibilities. For every \(L\ge2\), the \(r-L\) remaining zeros can occupy at most \(r-2\) of the \(m-1\) interletter slots. Since \(r,s\) are fixed, all \(L\ge2\) terms total \(O_{r,s}(m^{r-2}s^m)\). Hence

\[
Q_s(r,m)=\frac{m^{r-1}}{(r-1)!}s^{m-r}
\sum_{t=1}^s t^{r-1}+O_{r,s}(m^{r-2}s^m).
\]

In the necklace formula the identity rotation contributes \(\binom{m+r}{r}s^m/(m+r)=m^{r-1}s^m/r!+O_{r,s}(m^{r-2}s^m)\). For every nonidentity rotation, \(d\ge2\) and its contribution is exponentially smaller in \(m\), since \(s\ge2\), with \(r\) fixed. Dividing the two leading terms proves \(R_{s,r}\). Finally,

\[
\frac{sR_{s,r}}r=\sum_{t=1}^s(t/s)^{r-1}
\longrightarrow1
\]

as \(r\to\infty\), proving the linear growth and hence the absence of any bound independent of the prescribed zero count. At \(r=2\), the only possible first-run lengths are \(L=1,2\); evaluating those two terms gives the stated exact finite formula. All deductions are symbolic, not extrapolations from finite cases.

## Verification

Run `python3 verification/verify_quasinecklace.py` with Python 3. The program independently implements the defining run and successor conditions and ordinary rotation minimality. It enumerated \(107{,}054\) source words in \(126\) content slices, comparing directly observed counts with both formulas. Another \(770\) coefficient and Burnside computations checked larger parameters and the special two-zero formula. See `verification/verification_output.txt` for the captured output. The finite checks test the formulas but are not substituted for the all-parameter proof.

## Relationship to prior work

Gabrić and Sawada (first public preprint 2026-07-06) introduced the nonbinary quasinecklace definition and gave an unrefined total-length recurrence (Section 3.1), and proved global constant-amortized generation and a bounded-total-symbol-weight variant (Section 4.3). Neither statement specifies the minimum-letter-count enumerator or its sharp, unbounded-in-count conditional candidate/output ratio. The power-sum law arises from the separate inter-run transfer description above. Earlier binary colex work uses pseudonecklaces, not the present nonbinary conditional spectrum. Published binary-specific quasinecklace counts and overhead bounds cover the excluded one-nonzero-symbol specialization; extending them by simply substituting alphabet size would miss the successor-order power sum.

## Limitations

The limit holds with the number of zeros and the alphabet fixed while the number of nonzero positions increases. It is not a uniform approximation when both counts grow simultaneously. The content restriction fixes only the number of zeroes, not the complete Parikh vector of the nonzero symbols. The result makes no claim of an improved generation algorithm, nor of independent verification or unique historical priority. A nonindexed equivalent enumeration or a stronger yet-unlocated result remains possible. The globally unrestricted quasinecklace/necklace bound is not contradicted: the known injection changes symbol content and does not preserve the fixed-zero-count slice.

## References

1. Daniel Gabrić and Joe Sawada, *Necklaces and Lyndon words in colexicographic order*, arXiv:2607.05324v1 (first posted 2026-07-06), https://arxiv.org/abs/2607.05324. In particular Definition 3, Theorem 4, Section 3.1, and Section 4.3.
2. Joe Sawada, Aaron Williams, and Dennis Wong, *Necklaces and Lyndon words in colexicographic and binary reflected Gray code order*, Journal of Discrete Algorithms 46–47 (2017), 25–35. https://doi.org/10.1016/j.jda.2017.10.002.
3. Publicly indexed result *Sharp exact-content overhead for binary quasinecklaces* (2026-10-26), consulted at abstract/summary level; pertains to the binary fixed-content specialization, not the nonbinary power-sum law.
