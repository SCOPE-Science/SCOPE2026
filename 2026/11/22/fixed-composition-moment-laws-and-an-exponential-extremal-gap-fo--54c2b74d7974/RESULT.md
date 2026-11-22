# Fixed-composition moment laws and an exponential extremal gap for monochromatic complement deletions

## Finding

Fix a finite alphabet \(\Sigma\) with \(q\ge 2\) symbols and a distinguished symbol \(a\in\Sigma\). Let \(m,b\ge 1\) and choose uniformly a word \(W\in\Sigma^{m+b}\) containing exactly \(m\) copies of \(a\) (all other symbols may be any of the other \(q-1\) letters). For \(0\le k\le m\), define
\[
X_k(W)=|C(W,a^k)|,
\]
where \(C(W,u)\) is the set of **distinct residual words** after deleting the positions of an embedded subsequence \(u\); in particular \(a^0\) denotes the empty word. Put \(r=b+1\) and \(Y(W)=\sum_{k=0}^m X_k(W)\). The summands represent distinct residual lengths, so \(Y\) counts all residual words from deleting any number of copies of \(a\).

**Exact fixed-composition mean and joint moments.** For every \(0\le k,\ell\le m\),
\[
\boxed{\mathbb E X_k=
\frac{\binom{r+k-1}{k}\binom{r+m-k-1}{m-k}}
{\binom{m+r-1}{m}}.}
\]
Define the following rational formal power series:
\[
H(x,u,v)=\frac{1}{(1-u)(1-v)}\left(
\frac1{1-x}-\frac{u}{1-xu}-\frac{v}{1-xv}+\frac{uv}{1-xuv}\right).
\]
Then the **entire second-moment matrix** is
\[
\boxed{\mathbb E(X_kX_\ell)=
\frac{[x^m u^k v^\ell]H(x,u,v)^r}
{\binom{m+r-1}{m}}.}
\]
In particular,
\[
\boxed{\mathbb EY=\frac{\binom{m+2r-1}{m}}{\binom{m+r-1}{m}},\qquad
\mathbb EY^2=\frac{[x^m](1+x)^r(1-x)^{-3r}}{\binom{m+r-1}{m}}.}
\]
The variance is the second expression minus the square of the first. These laws do not depend on \(q\), once the number of copies of \(a\) is fixed.

**Sharp bound and its complete simultaneous equality class.** For a deterministic word, write its \(a\)-gap lengths as \((c_0,\ldots,c_b)\). If \(m=rs+h\) with \(0\le h<r\), then for every \(k\),
\[
\boxed{X_k\le[z^k](1+z+\cdots+z^s)^{r-h}
(1+z+\cdots+z^{s+1})^h.}
\]
The full vector \((X_0,\ldots,X_m)\) simultaneously attains the indicated upper vector, or equivalently \(Y\) attains its largest possible value \((s+1)^{r-h}(s+2)^h\), exactly when \(h\) gaps have length \(s+1\) and the other gaps length \(s\). There are exactly \(\binom rh(q-1)^b\) labeled maximizing words. *This balancing step is elementary and related to known deletion-pattern bounds; the new focus is the exact conditional moment profile and the exponential mean/extremum separation below.*

**Balanced-frequency exponential separation.** At \(b=m\), so that exactly half the positions contain \(a\),
\[
\boxed{\max_WY(W)=2^m,\qquad
\frac{\mathbb EY}{\max_WY}
=\frac{\binom{3m+1}{m}}{2^m\binom{2m}{m}}
\sim\frac{3\sqrt3}{4}\left(\frac{27}{32}\right)^m.}
\]
Moreover the fraction of labeled host words attaining the maximum is exactly
\[
\boxed{\frac{m+1}{\binom{2m}{m}}\sim\sqrt\pi\,m^{3/2}4^{-m}.}
\]
Thus both the mean relative to the sharp optimum and the frequency of optimizers decay exponentially; this is an exact comparison, not a claim about the median or a limiting distribution.

## Assumptions and scope

All words are linear and their positions are indexed. Deleting \(a^k\) means choosing \(k\) distinct positions originally occupied by \(a\), retaining all other positions in order. Identical output strings are counted once, even when multiple position selections produce them. The probability distribution is uniform on all words of length \(m+b\) with exactly \(m\) copies of \(a\), with \(q\ge2\), \(m,b\ge1\). The letters other than \(a\) need not be distinct. All coefficient extractions are in formal power series about zero. Statements are exact for finite parameters except the explicitly indicated asymptotics as \(m\to\infty\).

## Proof

**1. Positional gap bijection.** Every eligible source has a unique factorization
\[
W=a^{c_0}d_1a^{c_1}\cdots d_ba^{c_b},\qquad d_i\neq a,
\quad c_i\ge0,\quad\sum_{i=0}^{b}c_i=m.
\]
Each residual after deleting \(a^k\) retains the \(b\) indexed non-\(a\) letters in the same order and retains \(c_i-e_i\) copies of \(a\) in gap \(i\), where \(0\le e_i\le c_i\) and \(\sum e_i=k\). The residual uniquely determines these gap counts by scanning between successive non-\(a\) letters, even if some consecutive non-\(a\) letters are equal. Conversely every bounded deletion vector \((e_i)\) can be realized. Writing \(F_c(z)=1+z+\cdots+z^c\), we obtain the exact identity
\[
X_k(W)=[z^k]\prod_{i=0}^{b}F_{c_i}(z),\qquad
Y(W)=\prod_{i=0}^{b}(c_i+1).
\tag{1}
\]

**2. Uniform compositions.** Every weak composition \((c_i)_{i=0}^b\) of \(m\) into \(r=b+1\) parts corresponds to exactly \((q-1)^b\) source words, from the unrestricted choices of the \(d_i\). Since there are \(\binom{m+r-1}{m}\) such compositions, the gap vector is uniform over weak compositions.

**3. The first moments.** The identity
\[
\sum_{c\ge0}x^cF_c(z)=\frac{1}{(1-x)(1-xz)}
\]
shows that the sum of the polynomials in (1) over all gap compositions is \([x^m](1-x)^{-r}(1-xz)^{-r}\). Extracting \(z^k\) gives \(\binom{r+k-1}{k}\binom{r+m-k-1}{m-k}\). Divide by the number of compositions to obtain \(\mathbb E X_k\). Summing over \(k\) also follows from
\[
\sum_{c\ge0}(c+1)x^c=(1-x)^{-2},
\]
which gives the displayed formula for \(\mathbb EY\).

**4. The entire second moments.** Squaring the single-gap polynomial with two independent marking variables gives
\[
\sum_{c\ge0}x^cF_c(u)F_c(v)
=\frac{1}{(1-u)(1-v)}\left(
\frac1{1-x}-\frac{u}{1-xu}-\frac{v}{1-xv}+\frac{uv}{1-xuv}\right)=H(x,u,v).
\]
Taking its \(r\)-th power independently accounts for all \(r\) gaps. Coefficient extraction of \(x^m u^k v^\ell\) and normalization by the composition count proves the full joint-moment formula. Similarly
\[
\sum_{c\ge0}(c+1)^2x^c=\frac{1+x}{(1-x)^3}
\]
proves the exact expression for \(\mathbb EY^2\). No independence between gap lengths is asserted: conditioning on their sum is performed by extracting \(x^m\).

**5. Sharp bound and equality.** If two gap sizes are \(A\ge B+2\), the elementary identity
\[
F_{A-1}(z)F_{B+1}(z)-F_A(z)F_B(z)
=z^{B+1}+z^{B+2}+\cdots+z^{A-1}
\]
has nonnegative coefficients and at least one positive coefficient. Multiplying by the other \(F_{c_i}\), whose constant terms equal one, retains coefficientwise domination and strictness somewhere. Repeating the transfer reduces the sum of squared gap sizes and terminates at the unique balanced multiset of \(r-h\) copies of \(s\) and \(h\) copies of \(s+1\). Therefore the balanced product dominates every coefficient simultaneously. Strictness somewhere shows that no unbalanced composition matches the whole vector. Evaluating at \(z=1\) shows strict increase of \(Y\) under any such transfer. The equality classification and \(\binom rh(q-1)^b\) count follow.

**6. Exact rate at balanced frequency.** For \(m=b\), \(r=m+1\), so \(s=0\), \(h=m\); hence \(Y_{\max}=2^m\) and the maximizer fraction is \((m+1)/\binom{2m}{m}\). Substituting \(r=m+1\) in the mean gives \(\mathbb EY=\binom{3m+1}{m}/\binom{2m}{m}\). Stirling's formula yields
\[
\binom{3m+1}{m}\sim\frac{3}{2}\sqrt{\frac{3}{4\pi m}}\left(\frac{27}{4}\right)^m,
\qquad
\binom{2m}{m}\sim\frac{4^m}{\sqrt{\pi m}},
\]
which proves the \(27/32\) rate and constant. The same central-binomial asymptotic proves the stated optimizer fraction. This completes the finite identities and the asymptotics.

## Verification

The self-contained standard-library scripts `verification/verify_monochromatic.py` and `verification/verify_moments.py` implement two distinct checks: direct position-subset enumeration of complement outputs versus bounded-composition coefficients, and enumeration of weak compositions versus trivariate generating-function coefficients. The recorded outputs are `verification/verification_output.txt` and `verification/moments_output.txt` respectively. The first checks all words over alphabets of sizes two, three, and four up to lengths 11, 8, and 7, including every eligible deletion count, the sharp coefficients, equality counts, and mean identities. The second verifies 32 parameter pairs and 21,648 second-moment coefficient cells, and the total first/second-moment identities. These exhaustive finite checks corroborate the proof; the unrestricted identities are established symbolically in the preceding section.

## Relationship to prior work

Adamson, Fleischmann, and Huch introduced complement scattered-factor sets and general algorithms, with a stated interest in closed cardinality formulas. Their March 2026 primary text does not give fixed-composition moment laws or an exponential mean-to-maximum gap for a prescribed repeated-letter deletion pattern. The deleted pattern here is \(a^k\) while the host varies over a complete fixed-content ensemble.

The distinct-letter \(ab\) run-pair formula in the published research record concerns a different prescribed deletion pattern and includes an independent-letter expectation; it does not determine the present fixed-content joint moments. The published collision-threshold result for **unrestricted** deletion spheres uses the same known smoothing polynomial to bound all deletion-pattern counts. Li, Wang, and Fu also develop balancing for unrestricted nonbinary deletion balls. Accordingly, the smoothing identity and bare balanced upper bound are **not claimed to be original by themselves**; the assessed contribution is the conditional first- and second-moment laws, exact optimizer prevalence, and the \(27/32\) exponential separation in the complement-scattered-factor setting.

## Limitations

The deleted pattern must be monochromatic; different target letters can create collisions not represented by independent gap lengths. The random source is fixed-composition uniform, rather than an independent-letter source. The exponential statement specializes to equal populations of the distinguished symbol and all other symbols combined. No asymptotic median, limit distribution, channel capacity, or extension to unrestricted deleted patterns is claimed. A general probabilistic composition identity published under unrelated terminology could imply the moment formulas; such priority cannot be ruled out without a broader historical audit. Independent scientific validation has not been performed.

## References

1. D. Adamson, P. Fleischmann, and A. Huch, “(Sets of) Complement Scattered Factors,” arXiv:2603.20790v1, first public 21 March 2026. https://arxiv.org/html/2603.20790v1
2. H. Li, X. Wang, and F.-W. Fu, “On the Number of Subsequences in the Nonbinary Deletion Channel,” arXiv:2601.06493v2, first public 10 January 2026. https://arxiv.org/html/2601.06493v2
3. “A run-pair formula for two-letter complement scattered factors,” published research record, 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-run-pair-formula-for-two-letter-complement-scattered-factors--3b99e07a61fe
4. “Exact run-pattern collision thresholds and short-deletion extremal counts,” published research record, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-pattern-collision-thresholds-and-short-deletion-extrem--2036e6f8e3be
