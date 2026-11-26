# Sharp Gaussian peak of cyclic binary dinucleotide reconstruction ambiguity

## Finding
For each integer \(n\ge1\), observe a binary circular word only through the four multiplicities of its cyclic adjacent pairs \(00,01,10,11\), with the last-first pair included. Identify words that differ by a rotation, but not by reflection or letter exchange. Let \(A_n\) be the largest number of distinct rotation classes with one common observation. Then
\[
\boxed{\lim_{n\to\infty}\frac{n^2 A_n}{2^n}=\frac4\pi.}
\]
More precisely, let \(a,b,d\) be nonnegative integers with \(a+d+2b=n\), and write \(N(a,b,d)\) for the number of rotation classes having adjacent-pair matrix
\[
\begin{pmatrix}a&b\\b&d\end{pmatrix}.
\]
For every fixed \(C>0\), uniformly over \(b\ge1\) and \(\max(|a-n/4|,|b-n/4|,|d-n/4|)\le C\sqrt n\),
\[
N(a,b,d)=\frac4\pi\frac{2^n}{n^2}
\exp\!\left(-\frac{(a-b)^2+(d-b)^2}{n}\right)(1+o_C(1)).
\]
In particular, every sequence of maximizing pair-count matrices has \(a/n,b/n,d/n\to1/4\), and choosing the feasible counts nearest \(n/4\) attains the sharp asymptotic constant.

## Assumptions and scope
The alphabet is labeled \(\{0,1\}\), and a circular word has indexed positions modulo \(n\) before taking rotation equivalence. Its observation records the ordered-pair counts at all \(n\) cyclic indices. In a realizable nonconstant binary profile, the off-diagonal counts agree, \(m_{01}=m_{10}=b\ge1\), and \(a=m_{00}\), \(d=m_{11}\). The remaining realizable profiles have \(b=0\) and represent the two constant words only. The statistic \(A_n\) is an ambiguity *in distinct necklaces*, not the number of indexed sources.

## Proof
**1. Exact run-composition orbit formula.** Fix \(b\ge1\). Start at a \(0\)-to-\(1\) transition and record the \(b\) successive positive zero-run lengths and \(b\) successive positive one-run lengths. Their excesses above one are two vectors \((u_i)_{i=1}^b\), \((v_i)_{i=1}^b\) of nonnegative integers with sums \(a\), \(d\). Two such descriptions determine the same circular binary word exactly when they differ by simultaneous cyclic rotation of the \(b\) run pairs. A rotation of order \(\ell\mid b\) fixes a description only if \(\ell\mid a,d\); then its \(b/\ell\) run pairs are repeated \(\ell\) times, and stars-and-bars gives \(\binom{a/\ell+b/\ell-1}{b/\ell-1}\binom{d/\ell+b/\ell-1}{b/\ell-1}\) fixed descriptions. There are \(\varphi(\ell)\) rotations of order \(\ell\). Burnside therefore yields, with \(g=\gcd(a,b,d)\),
\[
N(a,b,d)=\frac1b\sum_{\ell\mid g}\varphi(\ell)
\binom{a/\ell+b/\ell-1}{b/\ell-1}
\binom{d/\ell+b/\ell-1}{b/\ell-1}.
\tag{1}
\]
This is an exact all-length formula, used here to determine the peak and its local shape; it is not asserted to be novel in isolation from classical Markov-type enumeration.

**2. Periodic corrections are negligible uniformly.** For \(\ell\ge2\), each binomial product in (1) is at most \(2^{(a+2b+d)/\ell}=2^{n/\ell}\le2^{n/2}\). Since \(\sum_{\ell\mid b}\varphi(\ell)=b\), the total of all \(\ell\ge2\) summands after division by \(b\) is between zero and \(2^{n/2}\). Thus uniformly over all admissible profiles,
\[
N(a,b,d)=T(a,b,d)+O(2^{n/2}),\quad
T(a,b,d)=\frac1b\binom{a+b-1}{b-1}\binom{d+b-1}{b-1}.
\tag{2}
\]
Set \(r=a+b\) and \(s=d+b\), so \(r+s=n\). Direct cancellation gives
\[
T(a,b,d)=\frac{b}{rs}\binom rb\binom sb
=2^n\frac{b}{rs}p_r(b)p_s(b),
\tag{3}
\]
where \(p_m(k)=2^{-m}\binom mk\) is a fair-binomial point probability.

**3. Exact location of the exponential peak.** For \(u\in[0,1]\), let \(H(u)=-u\log_2u-(1-u)\log_2(1-u)\) with the usual zero convention. The estimate \(\binom mk\le2^{mH(k/m)}\) and (3) give \(T\le2^{n\Phi}\), where
\[
\Phi=\frac rnH(b/r)+\frac snH(b/s)\le1.
\]
Equality \(\Phi=1\) requires \(b=r/2=s/2\), equivalently \(a=b=d=n/4\). This is the unique point of equality on the compact normalized feasible triangle. Therefore, away from every fixed neighborhood of \((a/n,b/n,d/n)=(1/4,1/4,1/4)\), the bound is \(T\le2^{(1-\epsilon)n}\) for some \(\epsilon>0\), whereas the constructions in Step 5 attain order \(2^n/n^2\). Any maximizing triple hence converges to the balanced point after division by \(n\).

**4. Uniform local Gaussian estimate.** Fix \(C>0\). For all triples in the stated window, \(r=n/2+O_C(\sqrt n)\), \(s=n/2+O_C(\sqrt n)\), and \(b-r/2=(b-a)/2=O_C(\sqrt n)\), \(b-s/2=(b-d)/2=O_C(\sqrt n)\). The Stirling expansion of the central binomial coefficients, uniformly in such windows, is
\[
p_m(m/2+z)=\sqrt{\frac2{\pi m}}\exp\!\left(-\frac{2z^2}{m}\right)(1+o_C(1)).
\tag{4}
\]
Here the arguments are integers, even when \(m/2\) is a half-integer. Substitution into (3), using \(b/(rs)=(1+o_C(1))/n\), gives
\[
T(a,b,d)=\frac4\pi\frac{2^n}{n^2}
\exp\!\left(-\frac{(a-b)^2+(d-b)^2}{n}\right)(1+o_C(1)).
\]
The uniform error term \(O(2^{n/2})\) in (2) is exponentially negligible, proving the local formula.

**5. Sharp global optimum.** Choose feasible integers \(a,b,d\) with sum constraint and all three within a bounded distance of \(n/4\): for instance, take \(b=\lfloor n/4\rfloor\), \(a=\lfloor(n-2b)/2\rfloor\), \(d=n-2b-a\) for \(n\ge4\). Step 4 then gives \(A_n\ge(4/\pi+o(1))2^n/n^2\). For the converse, Step 3 confines every maximizing triple to \(r,s=(1/2+o(1))n\), \(b=(1/4+o(1))n\). For every integer \(k\), the fair-binomial point probability obeys \(p_m(k)\le\max_j p_m(j)=\sqrt{2/(\pi m)}(1+o(1))\) as \(m\to\infty\). Using this in (3) gives \(T\le(4/\pi+o(1))2^n/n^2\), and (2) controls the remainder. The two constant-word profiles have ambiguity one and cannot maximize asymptotically. This proves the asserted limit.

## Verification
The standalone Python 3 program `verify.py` independently enumerates indexed binary words, reduces each to its lexicographically smallest rotation, groups those necklaces by their literal cyclic ordered-pair profiles, and compares every resulting fiber size with the divisor-sum formula (1) for all \(1\le n\le15\). It also checks finite-length maximizers computed from the arithmetic formula up to length \(64\), and reports the scaled peak ratio against \(4/\pi\). None of these finite checks proves the asymptotic statement: Steps 1–5 do.

## Relationship to prior work
Whittle (1955) gave general exact Markov-chain transition-total enumerations; consequently, the orbit formula (1) is classical in spirit and is used as an intermediate lemma, not the novelty claim. Jacquet, Knessl and Szpankowski (2010) study the **number of distinct** Markov types and the balanced-frequency constraints, not the **largest number of rotation classes within one type** or its sharp Gaussian peak constant. Related work on linear two-mer reconstruction treats \(n-1\) adjacent observations with endpoints and does not imply the present cyclic-orbit asymptotic. The distinguishing claim is the sharp \(4/\pi\) global constant together with the explicit local Gaussian profile for cyclic binary necklaces.

## Limitations
This theorem is asymptotic and does not give exact finite-length optimizers. It counts necklaces and excludes reflection and symbol complementation; it does not assert the same constant for indexed words, linear strings, larger alphabets, or reads longer than two. Historical priority is qualified because Whittle's full 1955 paper was inaccessible, although its known exact enumeration is openly acknowledged. The old general type-class formulas may admit other derivations of the same constant not located in accessible sources. No independent mathematical validation is claimed.

## References
1. P. Whittle, *Some Distribution and Moment Formulae for the Markov Chain*, Journal of the Royal Statistical Society B 17(2), 235–242 (1955), DOI:10.1111/j.2517-6161.1955.tb00197.x.
2. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, Discrete Mathematics & Theoretical Computer Science, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768. Open full text: https://dmtcs.episciences.org/en/articles/2768/download.
3. R. Gabrys, O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018), for the different linear read-spectrum setting.
