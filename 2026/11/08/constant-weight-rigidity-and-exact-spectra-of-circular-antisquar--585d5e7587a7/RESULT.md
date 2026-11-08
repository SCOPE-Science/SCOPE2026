# Constant-weight rigidity and exact spectra of circular antisquare-good binary words

## Finding

For any integer \(n\ge 1\), call a labeled binary word \(w=w_0\cdots w_{n-1}\) **periodically antisquare-good** when its two-sided periodic extension \(w^\mathbb Z\) has no factor \(v\overline v\) with \(|v|\ge2\), where \(\overline v\) is the bitwise complement. Define
\[
A_n(u)=\sum_{\substack{w\in\{0,1\}^n\\ w\;\mathrm{periodically\ antisquare\text{-}good}}}u^{|w|_1},
\qquad
\mathcal Z(z,u)=\exp\!\left(\sum_{n\ge1}\frac{A_n(u)}n z^n\right).
\]
Here different starting positions are counted as different words, but identical words coming from a shorter primitive period are counted only once at a fixed length. Then, as an identity of formal power series,
\[
\boxed{\mathcal Z(z,u)=
\frac{1}{(1-z-uz^4-u^2z^6)(1-uz-u^3z^4-u^4z^6)}.}
\]

More explicitly, let \(C_{n,t}=[u^t]A_n(u)\). Then \(C_{n,0}=C_{n,n}=1\). For \(0<t<n\), set \(r=\min(t,n-t)\). We have
\[
\boxed{C_{n,t}=n\!\sum_{\substack{0\le j\le\lfloor r/2\rfloor\\4r-2j\le n}}
\frac{1}{r-j}\binom{r-j}{j}\binom{n-3r+j-1}{r-j-1}.}
\]
In particular, the exact criterion for a positive constant-composition class is
\[
\boxed{C_{n,t}>0\ \Longleftrightarrow\ n\ge3r+(r\bmod2),\qquad 0<t<n.}
\]
Thus every nonconstant admissible periodic binary word has its one-density at most \(1/3\) or at least \(2/3\); the forbidden central density interval is sharp, with equality at \(1/3\) (and \(2/3\)) precisely attainable when \(n\) is divisible by six. The count at equality is exactly six for each of the two densities.

## Assumptions and scope

The alphabet is exactly the labeled binary alphabet \(\{0,1\}\); the complement interchanges these two symbols. Antisquare avoidance applies to **every** finite factor of the infinite periodic extension, not merely factors lying within one displayed copy. The case \(n=1\) and all repetitions of shorter periods are included. The length variable \(z\) and weight variable \(u\) are formal indeterminates. The formula counts marked-origin binary words, not conjugacy classes; primitive necklaces can subsequently be obtained by Möbius inversion of the weight-refined counts.

## Proof

**1. Forbidden factors and the cyclic transition code.** The minimal-antisquare theorem of Baranwal–Currie–Mol–Ochem–Rampersad–Shallit [1, Theorem 11] lists the order-two exclusions \(0011,1100,0110,1001\), the order-three exclusions \(010101,101010\), and a family of longer minimal antisquares, all of which contain either \(001011\) or \(110100\) as a factor. Their Proposition 18 shows that a two-sided good word containing either exceptional factor is asymptotic to alternating words on both sides and cannot be periodic. Consequently, for a **periodic** word, goodness is equivalent to cyclic avoidance of the eight-element set
\[
\mathcal F=\{0011,1100,0110,1001,010101,101010,001011,110100\}.
\]
For any periodic binary word set \(p_i=w_i\oplus w_{i+1}\), taking subscripts modulo \(n\). Taking consecutive differences turns the eight forbidden patterns into the four transition patterns \(010,101,11111,01110\), respectively (up to complementation of the original binary pattern). Thus a nonconstant valid periodic transition word has zero-runs of length at least two and one-runs of length exactly two or four. The all-zero transition word corresponds to the two constant binary words; an all-one transition word is disallowed by \(11111\). This local description also appears in [1, Section 7] in its noncyclic form.

Every one-run in \(p\) has even length. Following \(w\) across such a run changes its symbol and returns to the starting symbol, so all long zero-runs of \(p\) carry a common **background bit**. The opposite bit occurs only as isolated singleton runs in \(w\). Between consecutive occurrences of this minority bit, the number of background bits is either one or at least three. A gap of one occurs exactly once within a four-transition run of \(p\), and therefore no two one-gaps are cyclically adjacent. Conversely, any nonconstant circular word with this gap property has transition-one runs of length two or four and transition-zero runs of length at least two, hence avoids \(\mathcal F\) and is good. The background bit is uniquely determined: it has a run of length at least three, whereas the minority bit has only singleton runs.

**2. Weighted periodic-point zeta function.** First fix background bit \(0\). Every nonconstant admissible circle is a uniquely decipherable cyclic concatenation of the groups
\[
1 0^g\quad\text{and}\quad1 0 1 0^g,\qquad g\ge3.
\]
Indeed, each group ends with one of the long gaps, and a short gap (if present) is necessarily paired with the following long gap. Their joint length/one-weight generating function is
\[
B_0(z,u)=\sum_{g\ge3}\bigl(uz^{g+1}+u^2z^{g+3}\bigr)
=\frac{uz^4+u^2z^6}{1-z}.
\]
The elementary cyclic-block counting identity says that the periodic-point zeta function of a uniquely circularly decipherable block system is \((1-B_0)^{-1}\). One direct proof expands
\( -\log(1-B_0)=\sum_{m\ge1}B_0^m/m\): multiplying the coefficient at length \(n\) by \(n\) marks an arbitrary bit position, while the denominator \(m\) removes the choice of first block among \(m\) cyclic blocks. The identity remains correct for words with a shorter primitive period because the marking and block-rooting are counted with their multiplicities. Including the all-zero word for each length multiplies by \((1-z)^{-1}\), giving
\[
\mathcal Z_0(z,u)=\frac{1}{(1-z)(1-B_0(z,u))}
=\frac{1}{1-z-uz^4-u^2z^6}.
\]
Complementation replaces a length-\(n\), one-weight-\(t\) word by one of weight \(n-t\), so the background-one factor is obtained by substituting \((z,u)\mapsto(uz,u^{-1})\):
\[
\mathcal Z_1(z,u)=\frac{1}{1-uz-u^3z^4-u^4z^6}.
\]
The two classes are disjoint, including their distinct constants. Taking the product proves the bivariate identity.

**3. Coefficients and sharp support.** Suppose that \(1\) is the minority bit and there are exactly \(r\ge1\) occurrences of it. Let \(j\) of the \(r\) cyclic gaps be short (one zero); no two short gaps are neighbors. For \(0\le j\le\lfloor r/2\rfloor\), the number of cyclically indexed short/long assignments is
\[
\frac{r}{r-j}\binom{r-j}{j}.
\]
There are \(r-j\) long gaps, each containing at least three zeroes. The least possible word length is \(2j+4(r-j)=4r-2j\), and the excess \(e=n-4r+2j\ge0\) can be distributed among the long gaps in
\[\binom{e+r-j-1}{r-j-1}=\binom{n-3r+j-1}{r-j-1}\]
ways. Double-counting words with a distinguished one-position gives a factor \(n/r\). Multiplication and summation yield the displayed exact coefficient formula. Complementing handles minority-zero words. The two constants contribute one apiece.

The smallest possible length for \(r\) minority occurrences is attained by taking the maximum allowed \(j=\lfloor r/2\rfloor\) and all long gaps of length three. This minimum equals \(3r+(r\bmod2)\). Every larger length is possible by lengthening any long gap, proving the support equivalence. In particular \(n\ge3r\), so \(r/n\le1/3\). Equality requires even \(r\), alternating short and long gaps, and no excess. Thus \(n=3r\) is divisible by six, and there are exactly six marked-origin words with minority bit one and six with minority bit zero. This proves the density assertion.

## Verification

The included standard-library script `VERIFY.py` recomputes the closed constant-weight formula using exact rational arithmetic. It exhausts all \(131070\) labeled binary words of lengths \(1\) through \(16\), compares the eight-pattern predicate with direct antisquare checks through order \(3n\) for all \(4094\) words of lengths \(1\) through \(11\), and independently computes bivariate periodic-point counts with a 32-state forbidden-pattern de Bruijn transfer automaton through length \(40\). It also tests the support criterion for all lengths through \(120\). The run returned `VERIFY_OK`. These are finite checks; the proof for arbitrary lengths uses the cited minimal-antisquare classification and the preceding combinatorial argument, not extrapolation from the tests.

Some sample weight polynomials are
\[
A_4(u)=1+4u+4u^3+u^4,
\]
\[
A_6(u)=1+6u+6u^2+6u^4+6u^5+u^6,
\]
\[
A_{12}(u)=1+12u+42u^2+40u^3+6u^4+6u^8+40u^9+42u^{10}+12u^{11}+u^{12}.
\]

## Relationship to prior work

Baranwal et al. [1] establish the minimal forbidden antisquares, periodic-compatibility constraints and the supergolden exponential growth rate of all good finite words. In particular their cyclic transition constraints provide an essential premise, not a new claim here. The **unweighted** periodic-point function \(\mathcal Z(z,1)=(1-z-z^4-z^6)^{-2}\) also has a prior derivation; that specialization and its ordinary primitive-necklace counts are not claimed as new. This finding instead classifies **every fixed-weight class**, proves the exact missing interval of possible symbol densities with its parity-dependent boundary, and gives the full bivariate series. The univariate identity alone cannot recover any of these coefficients. Complement avoidance [2] concerns forbidding complementary pairs of factors rather than the antisquare factor condition, and the circular-repetition setting [3] is different.

## Limitations

No claim is made for nonperiodic finite prefixes, alphabets larger than two, different complement involutions, or avoidance of other patterns. The statement uses all factors of the periodic extension, rather than only factors fitting in one length-\(n\) representative. The novelty assessment is relative to the sources actually inspected; an equivalent unindexed bivariate counting formula remains possible. Independent external audit has not been performed.

## References

1. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, and J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223 (first submitted 2022-09-19), DMTCS 25:2 #11 (2023), DOI:10.46298/dmtcs.10063. https://arxiv.org/abs/2209.09223 . Theorem 11, Proposition 18, and Section 7.
2. J. Currie et al., *Complement Avoidance in Binary Words*, arXiv:2209.09598 (2022), DOI:10.37236/11555. https://arxiv.org/abs/2209.09598 .
3. H. Mousavi and J. Shallit, *Repetition Avoidance in Circular Factors*, arXiv:1212.0052 (2012). https://arxiv.org/abs/1212.0052 .
