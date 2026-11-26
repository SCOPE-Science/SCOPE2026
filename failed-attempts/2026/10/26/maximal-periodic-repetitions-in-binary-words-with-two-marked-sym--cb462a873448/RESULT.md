# Maximal periodic repetitions in binary words with two marked symbols

## Finding

Let \(a,b,c\) be arbitrary nonnegative integers, and let \(w=0^a1\,0^b1\,0^c\). A *run* is a maximal factor whose length is at least twice its **least** period; a run records its start, end and least period. Write \(\rho(w)\) for the total number of runs, and \([P]\) for \(1\) when proposition \(P\) holds and \(0\) otherwise. Then

\[
\rho(w)=[a\ge2]+[b\ge2]+[c\ge2]+[b=0\ \text{or}\ (b\ge1\ \text{and}\ a+c\ge b)].
\]

In particular, \(\rho(w)\le4\), with equality exactly when \(a,b,c\ge2\) and \(a+c\ge b\). Among binary words of length \(n\) containing exactly two ones, the maximum number of runs equals \(1\) for \(n=2,3\), \(2\) for \(n=4,5\), \(3\) for \(n=6,7\), and \(4\) for every \(n\ge8\). The first four-run word is \(00100100\).

More precisely, put

\[
B(z,u)=1+z+\frac{uz^2}{1-z},\qquad
F(z,u)=\sum_{n\ge2}z^{n-2}\!\sum_{\substack{|w|=n\\ |w|_1=2}}u^{\rho(w)}.
\]

The **complete** run-count distribution is encoded by the rational bivariate generating function

\[
F(z,u)=B(z,u)^3+(u-1)\left[(1+z)B(z,u)^2-z
+\frac{uz^2}{1-z}\left(B(z,u)^2-1-\frac{B(z^2,u)^2-1}{z}\right)\right].
\]

All displayed expressions are formal power series in \(z\); the apparent division by \(z\) in the last bracket has no negative powers. If \(E_n\) counts the words of length \(n\) with exactly two ones and exactly four runs, then

\[
\sum_{n\ge8}E_nz^n=
 z^8\left(\frac1{(1-z)^3}-\frac{z^3}{(1-z)(1-z^2)^2}\right).
\]

For \(n\ge8\), put \(t=n-8\) and \(h=\min\{t,\lfloor(t+2)/2\rfloor\}\). An equivalent closed form and asymptotic are

\[
E_n=\frac{(h+1)(2t+2-h)}2,
\qquad E_n=\frac38n^2+O(n),\qquad
\lim_{n\to\infty}\frac{E_n}{\binom n2}=\frac34.
\]

## Assumptions and scope

Words are finite, linear, and binary. The symbol \(1\) appears **exactly twice**, at arbitrary distinct positions. A factor is contiguous. Its period is the least positive integer \(p\) such that equalities hold at all positions separated by \(p\) within the factor. A run has factor length at least \(2p\), and it cannot be extended one symbol left or right while retaining period \(p\). A length-one constant block does not count. This is the standard **maximal-periodic-repetition** sense of *run*, not the alternative term meaning a maximal block of equal letters, and not the run count of a Burrows–Wheeler transform.

The generating function enumerates actual words, not reversal classes or necklaces; the coefficient of \(z^{n-2}u^r\) counts words of length \(n\) having exactly \(r\) runs. Nothing is asserted for words with a different number of ones or for cyclic periodicity.

## Proof

**1. Complete set of possible runs.** Index letters from \(0\). The two occurrences of \(1\) are at positions \(a\) and \(a+b+1\). Every least-period-one run is a maximal equal-symbol block of length at least \(2\). Hence they consist of the three zero blocks when their lengths are at least \(2\), together with the middle block \(11\) when \(b=0\).

Suppose a run has least period \(p\ge2\). It cannot be all zeros. In any factor of length at least \(2p\), each occurrence of \(1\) has a partner exactly \(p\) positions to its left or right **within the factor**: if its relative position is before \(p\), move right, otherwise move left. Because the entire word has exactly two ones, the run must contain both, and they must be separated by exactly \(p\). Thus \(b\ge1\) and necessarily \(p=b+1\). No second higher-period run is possible.

For \(b\ge1\), the period-\(b+1\) repetition containing both ones extends left across exactly \(L=\min(a,b)\) zeros and right across exactly \(R=\min(c,b)\) zeros, and then cannot extend farther. Its inclusive interval is

\[
[a-L,\ a+b+1+R],
\qquad p=b+1,
\qquad \text{length}=b+2+L+R.
\]

Its least period really is \(p\): any smaller period would have to repeat a \(1\) at smaller separation, impossible in a word with exactly two ones and at least two-period-length factor. It qualifies as a run precisely when \(L+R\ge b\). Because \(L=\min(a,b)\) and \(R=\min(c,b)\), this inequality is equivalent to \(a+c\ge b\). This proves the complete classification and the cardinality formula, including \(b=0\) and zero-length outer gaps.

**2. Sharp maximum.** All four contributions in the displayed count can occur precisely when \(a,b,c\ge2\) and \(a+c\ge b\). The least length is \(2+2+2+2=8\), achieved by \(a=b=c=2\); increasing either outer gap gives examples at every longer length. For \(n=2,3\), at most one run is possible; for \(n=4,5\), at most two can occur; for \(n=6,7\), at most three can occur, since no quadruple-contributing triple exists, and they are realized respectively by \(a=b=2,c=0\) and \(a=2,b=2,c=1\) (with the shorter cases immediate from the formula). This proves the asserted finite-prefix maximum and the sharp universal bound.

**3. Bivariate distribution.** Assign each zero gap of size \(m\) the weight \(z^m u^{[m\ge2]}\). Its series is \(B(z,u)\). Without the additional middle run, every triple contributes to \(B^3\). Let \(T(z,u)\) enumerate precisely those triples giving an additional run, **but with weights for their zero blocks only**. The condition from step 1 partitions them into \(b=0\), \(b=1\), and \(b\ge2\):

\[
T=B^2+z(B^2-1)+\sum_{b\ge2}u z^b
\sum_{a+c\ge b}z^{a+c}u^{[a\ge2]+[c\ge2]}.
\]

For fixed \(m=a+c\ge2\), the admissible middle gaps in the last sum are \(2,\ldots,m\), with weight \(u z^2(1-z^{m-1})/(1-z)\). On summing over \(m\) this yields

\[
T=(1+z)B^2-z+\frac{uz^2}{1-z}
\left(B^2-1-\frac{B(z^2,u)^2-1}{z}\right).
\]

An additional run multiplies the weight of its triple by \(u\) instead of \(1\); hence \(F=B^3+(u-1)T\), the announced rational identity.

**4. Four-run count.** The four-run condition is \(a,b,c\ge2\), \(a+c\ge b\). Write \(a=2+A\), \(b=2+B\), \(c=2+C\). For \(n\ge8\), \(A+B+C=t=n-8\), with \(A,B,C\ge0\), and the inequality becomes \(B\le A+C+2\), or \(2B\le t+2\). Thus \(0\le B\le h=\min\{t,\lfloor(t+2)/2\rfloor\}\), and for each \(B\) exactly \(t-B+1\) ordered pairs \((A,C)\) exist. Their sum is \((h+1)(2t+2-h)/2\). Among all \(\binom{t+2}2\) triples, those violating the inequality have \(B\ge A+C+3\). Their generating series is \(z^3/((1-z)(1-z^2)^2)\) by choosing \(A,C\ge0\) and the excess \(B-A-C-3\ge0\). Subtraction yields the univariate rational expression. Finally \(h=t/2+O(1)\) gives \(E_n=3n^2/8+O(n)\), and division by \(\binom n2\) gives the limit \(3/4\).

## Verification

A standalone pure-Python checker (`verify.py`) constructs every possible factor interval of each tested word, finds its least period, checks both nonextension conditions, and compares **the full sets of run triples** to step 1. It verifies 1,330 gap triples with \(a+b+c\le18\), including all length-two through length-twenty words containing two ones. It independently checks the bivariate generating-function coefficients by evaluation at \(u\in\{0,1,2,3,4\}\), enumerates coefficients of the four-run generating function through length \(149\), and checks the sharp maximum at lengths \(2\) through \(19\). Run from the same directory with `python verify.py`; expected output begins `VERIFY_OK`. The finite computations serve as error checks, **not as substitutes for the all-length proofs** in steps 1–4.

## Relationship to prior work

Bannai et al., *The “Runs” Theorem* (arXiv:1406.0263, first public 2014-06-02), defines maximal periodic runs and establishes a global bound on their number for arbitrary words, together with bounds parameterized by the number of distinct symbols. Fischer et al., *Beyond the Runs Theorem* (arXiv:1502.04644, first public 2015-02-16), improves the worst-case general binary bound. Neither global bound specializes to the exact sparse-two-marker run set, its sharp constant, or the exact run-distribution generating function by simple substitution; the restriction to *two occurrences* of one symbol is different from restricting the alphabet to two distinct symbols.

Madden, *A Generating Function for the Distribution of Runs in Binary Words* (arXiv:1707.04351, first public 2017-07-13), uses the different convention that a run is a maximal constant-symbol block. That distribution does not cover higher-period runs such as the period-three run in \(00100100\). No claim of priority over unpublished or unindexed equivalent classifications is made.

## Limitations

The classification is for the precise domain of binary words with exactly two ones. The calculation does not provide bounds for arbitrary fixed positive weight, circular words, or periodicity under rotations. The bivariate formula counts **all maximal periodic runs** including period-one runs; it does not count only nontrivial-period runs. The literature comparison cannot rule out an unindexed earlier equivalent fixed-weight-two result, and no independent audit has been performed.

## References

1. H. Bannai, T. I, S. Inenaga, Y. Nakashima, M. Takeda, K. Tsuruta, *The “Runs” Theorem*, arXiv:1406.0263, https://arxiv.org/abs/1406.0263, submitted 2014-06-02.
2. J. Fischer, Š. Holub, T. I, M. Lewenstein, *Beyond the Runs Theorem*, arXiv:1502.04644, https://arxiv.org/abs/1502.04644, submitted 2015-02-16.
3. J. J. Madden, *A Generating Function for the Distribution of Runs in Binary Words*, arXiv:1707.04351, https://arxiv.org/abs/1707.04351, submitted 2017-07-13. This paper uses a different definition of a run.
