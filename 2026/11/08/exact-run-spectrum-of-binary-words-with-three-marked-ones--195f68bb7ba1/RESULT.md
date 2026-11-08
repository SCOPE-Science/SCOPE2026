# Exact run spectrum of binary words with three marked ones

## Finding
A *run* (maximal periodicity) in a word is an interval whose factor has least period \(p\), length at least \(2p\), and cannot be extended one position to either side while retaining period \(p\). Runs are occurrences/intervals, not distinct factor spellings and not merely maximal constant-symbol blocks.

Write a binary word with exactly three occurrences of \(1\) uniquely as
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\ge0}.
\]
Let \(R(w)\) be the total number of runs. Then the **complete gap classification** is
\[
\boxed{R(w)=1+\sum_{t\in\{a,b,c,d\}}\mathbf1_{\{t\ge2\}}
+\mathbf1_{\{b>c,\ a\ge b-c\}}
+\mathbf1_{\{c>b,\ d\ge c-b\}}.}
\tag{1}
\]
Here the sum counts the four zero blocks *with multiplicity of positions*: equal zero-block lengths in different places are different runs.

Consequently, every weight-three binary word has at most six runs. Six runs occur if and only if all four zero gaps have length at least two and either \(b>c\) with \(a\ge b-c\), or \(c>b\) with \(d\ge c-b\). Six is attainable precisely from length \(12\) onward. At length \(12\), the only two words attaining it are \(001000100100\) and its reversal \(001001000100\).

For the complete finite-length distribution, set
\[
G=1+z+\frac{uz^2}{1-z},\quad
A=1+uz+\frac{u^2z^2}{1-z},\quad
B=1+uz^2+\frac{u^2z^4}{1-z^2},
\]
\[
C=u(1+z^2)+\frac{u^2z^4}{1-z^2},\qquad
E=1+z^2+\frac{u^2z^4}{1-z^2}.
\]
Then the bivariate ordinary generating function, with a length variable \(z\) and run-count variable \(u\), is the rational function
\[
\boxed{F(z,u)=\sum_{n\ge3}\ \sum_{\substack{w\in\{0,1\}^n\\|w|_1=3}}z^nu^{R(w)}
=z^3u\left[G^2E+2G\left(zAB+C\left(\frac{z^2G}{1-z}+\frac{(u^2-u)z^4}{(1-z)(1-z^2)}\right)\right)\right].}
\tag{2}
\]
In particular, if \(N_6(n)\) is the number of length-\(n\) weight-three words having six runs, then
\[
\boxed{\sum_{n\ge3}N_6(n)z^n=\frac{2z^{12}(1+z-z^2)}{(1-z)^2(1-z^2)^2}.}
\tag{3}
\]
If \(W_n\) is uniformly chosen from the \(\binom n3\) length-\(n\) weight-three words, its number of runs converges in law to a fair choice between five and six:
\[
\boxed{\mathbb P(R(W_n)=5)\longrightarrow\tfrac12,\qquad
\mathbb P(R(W_n)=6)\longrightarrow\tfrac12.}
\tag{4}
\]
All other run counts have vanishing probability. Thus \(\mathbb E R(W_n)\to11/2\) and \(\operatorname{Var}R(W_n)\to1/4\).

## Assumptions and scope
Words are finite, **linear**, binary, position-indexed, and have exactly three ones. They may start/end in zero, and any zero gap can be empty. A run means a maximal periodic interval with exponent at least two and its *least* period. Reversal changes the interval positions but not the number of runs. The parameter \(n=a+b+c+d+3\) is at least three. The law (4) uses the uniform distribution on labeled words, not on reversal classes.

## Proof

**1. Restrict the possible periods.** Let an interval of least period \(p\) and length at least \(2p\) contain a one. Its initial \(2p\) positions comprise two identical length-\(p\) blocks. Hence the number of ones there is even and positive. As the whole ambient word has only three ones, these two blocks contain exactly one one each, in the same residue class modulo \(p\). If a third one appears in a further periodic tail, its earlier copies at shifts \(p\) and \(2p\) must also occur; hence it belongs to the same residue class. Thus the ones in the interval form a progression of step \(p\), with either two or three terms. In particular, any one-containing run has period equal to the distance \(b+1\) or \(c+1\) between neighboring ones. A period whose repeated primitive block has exactly one one cannot have a smaller period: the length-\(p\) block is primitive.

**2. Existence for each neighboring pair.** Number positions from zero and let the first two one positions be \(x_1\) and \(x_2=x_1+b+1\). A period-\(b+1\) two-copy core containing these ones can use up to \(\min(a,b)\) zeros to the left of the first one and up to \(\min(c,b)\) zeros immediately to the right of the second. Such a core has length at least \(2(b+1)\) precisely when
\[
\min(a,b)+\min(c,b)\ge b,
\]
equivalently, when \(b\le c\) or \(a\ge b-c\). When it exists, it extends uniquely to a maximal period-\(b+1\) run; if \(b=c\), that extension includes the third one. Symmetrically, the last two ones give a run of period \(c+1\) precisely when \(c\le b\) or \(d\ge c-b\).

If \(b\ne c\), these runs have different periods and are distinct, even when their intervals overlap. If \(b=c\), the three ones form a single period-\(b+1\) progression: the two pair constructions extend to the same maximal run, which is counted only once. Because one of the inequalities \(b\le c\) and \(c\le b\) always holds, at least one one-containing run always exists. Its total contribution is
\[
1+\mathbf1_{\{b>c,\ a\ge b-c\}}
+\mathbf1_{\{c>b,\ d\ge c-b\}}.
\]
Each maximal block of at least two zeros adds exactly one run of least period one; a shorter zero block adds none. By Step 1 there are no other runs. This proves (1).

**3. Sharpness.** There are at most four zero-block runs and two one-containing runs, hence \(R(w)\le6\). Equality requires the four gaps to be at least two and two different period runs. The inequalities in (1) give exactly the stated two alternatives. In either alternative the unequal middle gaps require at least \(2+3\) zeros; the outer gaps require at least \(2+2\), yielding \(n\ge3+9=12\). The gap quadruples \((2,3,2,2)\) and \((2,2,3,2)\) are the only minima, and arbitrary additional zeros in the first gap (or its reverse counterpart) give examples at every larger length.

**4. Rational enumeration.** A gap of length \(t\) contributes \(z^tu^{\mathbf1_{\{t\ge2\}}}\); summing over \(t\ge0\) gives \(G\). On the diagonal \(b=c\), summation over \(b\) yields \(E\), and the other two gaps yield \(G^2\), with one one-containing run. This contributes \(z^3uG^2E\).

For \(b>c\), let \(b=c+h\), where \(h\ge1\). The extra one-containing run is present exactly when \(a\ge h\), while \(d\) has generating function \(G\). For \(h=1\), the weighted sums over \(a\) and \(c\) are \(A\) and \(B\). For all \(h\ge2\), the weighted sum over \(c\) is \(C\), whereas the sum over \(a\) is
\[
\sum_{a\ge0} z^a u^{\mathbf1_{\{a\ge2\}}+\mathbf1_{\{a\ge h\}}}
=G+\frac{(u^2-u)z^h}{1-z}.
\]
Multiply by \(z^h\) and sum \(h\ge2\) to obtain the bracket in (2). The case \(c>b\) is its reversal and doubles the off-diagonal contribution. This proves (2). Setting \(u=1\) gives \(F(z,1)=z^3/(1-z)^4\), as required for \(\binom n3\) words.

**5. Six-run distribution and asymptotics.** In the six-run class we have \(a,b,c,d\ge2\). By symmetry take \(b=c+h\), \(h\ge1\), \(a\ge h\), and sum the independent lengths:
\[
\sum_{n\ge3}N_6(n)z^n
=2z^3\frac{z^2}{1-z}\frac{z^4}{1-z^2}
\left[\frac{z^3+z^4}{1-z}+\frac{z^6}{(1-z)(1-z^2)}\right],
\]
which simplifies to (3). As \(z\to1\) through real values below one, the rational expression in (3) is asymptotic to \(\frac12(1-z)^{-4}\), so \(N_6(n)\sim n^3/12\). Since \(\binom n3\sim n^3/6\), the six-run probability tends to \(1/2\). Among all gap compositions of total \(n-3\), those with some gap below two or with \(b=c\) number only \(O(n^2)\). Every remaining word has either five or six runs by (1), giving (4). Boundedness \(1\le R\le6\) yields the stated moment limits.

## Verification
The accompanying standalone Python 3 program `verify.py` independently enumerates all periodic intervals and their least periods, and checks (1) for every \(8,855\) binary word of weight three with length between three and twenty-two inclusive. It independently expands the rational expression (2) as a truncated bivariate formal power series and compares its coefficients against gap enumeration for every length from three to thirty-six. It also verifies the six-run coefficient formula (3) over this range and the two length-twelve extremizers. Run `python3 verify.py` from the same folder; expected final lines are `DIRECT_PERIOD_CHECK_OK 8855`, `RATIONAL_GF_CHECK_OK lengths=3..36`, and `SHARP_MAXIMUM_AND_HALF_LIMIT_OK`.

## Relationship to prior work
Glen and Simpson's *The total run length of a word* (arXiv:1301.6568; initial public version 2013-01-28) studies total lengths of maximal periodic runs and their unrestricted-alphabet averages. Bannai et al.'s *The “Runs” Theorem* (arXiv:1406.0263; initial public version 2014-06-02) proves a universal linear bound and establishes the Lyndon-root framework for maximal repetitions. Fischer et al.'s *Beyond the Runs Theorem* (arXiv:1502.04644; initial public version 2015-02-16) improves the universal bound for binary words. None of these statements directly gives the complete fixed-weight-three gap classification or the bivariate distribution above; our argument uses only the standard definition of a run. Results about ordinary *runs of ones* (maximal constant-letter blocks) concern a different statistic and cannot supply this periodicity spectrum.

## Limitations
The theorem is restricted to **linear binary words with exactly three ones**. It does not determine spectra at larger weights, under cyclic boundary conditions, or for general alphabets. The limiting law follows from the explicit generating function and applies only to uniformly selected fixed-weight-three words. Finite checks are verification supplements, not substitutes for the infinite proofs. A comprehensive historical-priority guarantee against unindexed equivalent work is not claimed.

## References
1. A. Glen and J. Simpson, *The total run length of a word*, arXiv:1301.6568, first posted 2013-01-28, https://arxiv.org/abs/1301.6568.
2. H. Bannai, T. I, S. Inenaga, Y. Nakashima, M. Takeda, and K. Tsuruta, *The “Runs” Theorem*, arXiv:1406.0263, first posted 2014-06-02, https://arxiv.org/abs/1406.0263.
3. J. Fischer, Š. Holub, T. I, and M. Lewenstein, *Beyond the Runs Theorem*, arXiv:1502.04644, first posted 2015-02-16, https://arxiv.org/abs/1502.04644.
