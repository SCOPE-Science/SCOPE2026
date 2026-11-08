# Exact distinct-square counts and aggregate law for binary words with three ones

## Finding

A **square** is a nonempty contiguous factor of the form \(uu\). Two squares count as distinct only if their complete binary strings differ, irrespective of their occurrences or their positions. Write \(S(w)\) for the number of distinct squares in a finite word \(w\). For nonnegative integers \(p,q,t\), put
\[
\mathcal I(p,q;t)=\max\{0,\min(p,t)-\max(0,t-q)+1\}.
\]
For every \(a,b,c,d\in\mathbb Z_{\ge0}\), the binary word \(w=0^a1\,0^b1\,0^c1\,0^d\) satisfies
\[
\boxed{S(w)=\left\lfloor\frac{\max\{a,b,c,d\}}2\right\rfloor+
\mathcal I(a,c;b)+\mathcal I(b,d;c)-\mathbf1_{\{b=c\}}\mathcal I(a,d;b).}\tag{1}
\]
This includes zero gaps and the word \(111\).

For every integer \(m\ge0\), let \(T_m\) be the sum of \(S(w)\) over the \(\binom{m+3}{3}\) indexed binary words of length \(m+3\) with exactly three ones. Their complete ordinary generating function is
\[
\boxed{\begin{aligned}
H(z):=\sum_{m\ge0}T_mz^m
={}&\frac1{(1-z)^4}\sum_{j=1}^4(-1)^{j+1}\binom4j\frac{z^{2j}}{1-z^{2j}}\\
&+\frac{2}{(1-z)^3(1-z^2)^2}
-\frac1{(1-z)^2(1-z^3)^2}.
\end{aligned}}\tag{2}
\]
For a uniformly chosen length-\(n\) binary word \(W_n\) with exactly three ones, \(n\ge3\),
\[
\boxed{\mathbb E S(W_n)=\frac{37}{96}n+O(1).}\tag{3}
\]
There is also a nondegenerate limiting distribution. Let \((A,B,C,D)\sim\operatorname{Dirichlet}(1,1,1,1)\), write \(x_+=\max(x,0)\), and define
\[
F(A,B,C,D)=\tfrac12\max\{A,B,C,D\}
+\big(\min(A,B)-(B-C)_+\big)_+
+\big(\min(B,C)-(C-D)_+\big)_+.
\]
Then
\[
\boxed{S(W_n)/n\ \xrightarrow{\mathrm d}\ F(A,B,C,D),\qquad
\mathbb EF(A,B,C,D)=37/96.}\tag{4}
\]
The limiting variance is strictly positive. Equation (4) defines the law explicitly as a pushforward of the uniform simplex distribution; no claim is made that it has a simple named density.

## Assumptions and scope

All words are **linear, indexed, binary**, and contain exactly three symbols equal to one. The parameter \(m\) is the number of zeros, while \(n=m+3\) is the total length. Squares are literal factors, not cyclic factors, occurrences with multiplicity, Abelian squares, or cubes. Empty factors are excluded. The rational identity is an identity of formal power series (and converges for \(|z|<1\)). All uniform sampling is over the \(\binom n3\) labeled words, not over reversal or rotation classes.

## Proof

**Step 1: classify each square.** The number of ones in a square \(uu\) is twice the number in \(u\). Since \(w\) has exactly three ones, any square in \(w\) contains either zero or two ones. The zero-one-count squares are precisely \(0^{2k}\) for \(1\le k\le\lfloor M/2\rfloor\), where \(M=\max(a,b,c,d)\), contributing the first term of (1).

Any square with exactly two ones has a root with exactly one one, uniquely of the form \(0^x1\,0^y\), for integers \(x,y\ge0\). Its string is
\[
(0^x1\,0^y)^2=0^x1\,0^{x+y}1\,0^y.\tag{5}
\]
The two ones in (5) must be consecutive ones of \(w\): if they were the first and third, the middle one would lie inside the factor. For the first adjacent pair, (5) occurs exactly when \(x+y=b\), \(x\le a\), and \(y\le c\). The integer \(x\) ranges from \(\max(0,b-c)\) to \(\min(a,b)\), so there are \(\mathcal I(a,c;b)\) distinct shapes. For the second adjacent pair, the corresponding conditions are \(x+y=c\), \(x\le b\), \(y\le d\), and there are \(\mathcal I(b,d;c)\) shapes.

If \(b\ne c\), shapes from the two pairs cannot coincide because their internal zero runs have different lengths. If \(b=c\), a common shape (5) must have \(x+y=b\), \(x\le a\), and \(y\le d\), and these are the only remaining restrictions. Their number is \(\mathcal I(a,d;b)\). Inclusion-exclusion proves (1), including every boundary with zero gaps.

**Step 2: sum over all four zero gaps.** Put \(m=a+b+c+d\). For the zero-only contribution, write
\[
\lfloor M/2\rfloor=\sum_{k\ge1}\mathbf1_{\{M\ge2k\}}.
\]
The generating series for all nonnegative four-tuples is \((1-z)^{-4}\). The series for those with all four coordinates at most \(2k-1\) is \((1-z^{2k})^4(1-z)^{-4}\). Subtraction, binomial expansion, and summation over \(k\) yield
\[
\frac1{(1-z)^4}\sum_{j=1}^4(-1)^{j+1}\binom4j\frac{z^{2j}}{1-z^{2j}}.\tag{6}
\]
For a shape from the first adjacent pair, choose its two zero parameters \(x,y\ge0\). The admissible coordinates are uniquely \(b=x+y\), \(a=x+r\), \(c=y+s\), \(d=t\), with \(r,s,t\ge0\). Thus its aggregate generating series is
\[
\sum_{x,y,r,s,t\ge0}z^{2(x+y)+r+s+t}
=\frac1{(1-z)^3(1-z^2)^2}.\tag{7}
\]
The second pair gives the same series. A shape counted in both must have \(b=c=x+y\), with \(a=x+r\), \(d=y+s\), so the diagonal overlap series is
\[
\sum_{x,y,r,s\ge0}z^{3(x+y)+r+s}
=\frac1{(1-z)^2(1-z^3)^2}.\tag{8}
\]
Combining (6), twice (7), and subtracting (8) proves (2) *exactly*, not merely coefficientwise for a finite range.

**Step 3: asymptotic expectation.** Near \(z=1\), the sum in (6) has leading coefficient
\[
\frac12\sum_{j=1}^{4}(-1)^{j+1}\binom4j\frac1j
=\frac12\left(1+\frac12+\frac13+\frac14\right)=\frac{25}{24}
\]
when multiplied by \((1-z)^{-5}\). The contribution of the doubled series (7) is \(\tfrac12(1-z)^{-5}\), while (8) has pole order four. Other poles on the unit circle have smaller orders. Therefore
\[
T_m=\frac{37}{576}m^4+O(m^3),
\quad\frac{T_m}{\binom{m+3}{3}}=\frac{37}{96}m+O(1),
\]
proving (3) because \(n=m+3\).

**Step 4: limit law and its mean.** A uniform weak composition of \(m\) into four parts, divided by \(m\), converges in distribution to the uniform three-dimensional simplex measure, i.e. \(\operatorname{Dirichlet}(1,1,1,1)\). The first three terms of (1), after division by \(n\), converge to the displayed piecewise-linear \(F\). On the exceptional hyperplane \(b=c\) the fourth term need not be negligible pointwise, but the proportion of integer compositions with \(b=c\) is \(O(1/m)\); this hyperplane has probability zero under the limiting Dirichlet law. Hence (4) holds by the continuous-mapping theorem away from a null set.

For an exact evaluation of the mean, let \(E_1,E_2,E_3,E_4\) be independent unit exponentials and \(Q=E_1+E_2+E_3+E_4\). Then \((E_1,E_2,E_3,E_4)/Q\) is the stated Dirichlet vector and is independent of \(Q\), whose mean is four. The function \(F\) is positively homogeneous of degree one. The mean of the maximum of four unit exponentials is the harmonic number \(25/12\). Furthermore, the first interval-length term \(L_1=(\min(E_1,E_2)-(E_2-E_3)_+)_+\) has the integral representation
\[
\mathbb EL_1
=\int_0^\infty e^{-x}\int_x^\infty e^{-b}e^{-(b-x)}\,db\,dx
=\frac14.
\]
The second interval-length term has the same mean by exchangeability. Consequently
\[
\mathbb EF=\frac14\left(\frac12\cdot\frac{25}{12}+\frac14+\frac14\right)
=\frac{37}{96}.
\]
Because \(F\) takes different values on disjoint interior open subsets of the simplex (for instance, near \((0.25,0.24,0.26,0.25)\) versus near \((0.10,0.70,0.11,0.09)\)), and each open subset has positive Dirichlet probability, its variance is strictly positive. This completes the proof.

## Verification

The accompanying standalone `verify_squares.py` implements an independent direct factor scan (constructing the literal set of every square), compares it with formula (1) for all 31,465 binary words of weight three and lengths \(3\le n\le30\), and checks 240 additional deterministic long-word samples. It also recomputes coefficients of (2) from finite coefficient sums and compares them with the sum of (1) for each \(0\le m\le50\). All checks passed. The first values \(T_0,\ldots,T_{11}\) are
\[
1,4,17,42,89,160,270,432,663,966,1368,1880.
\]
These finite computations supplement but do not replace the unrestricted combinatorial proofs above. Reproduction: `python3 verify_squares.py` (Python standard library only).

## Relationship to prior work

Fraenkel and Simpson studied avoidance and the maximum number of distinct squares in unrestricted binary words [1,2]. Kucherov, Ochem and Rao studied the *number of occurrences*, rather than distinct square strings [3]. Deza, Franek and Thierry established structural global bounds through double squares [4], and Brlek and Li proved a sharp alphabet-sensitive global upper bound [5]. None of the inspected relevant statements supplies the fixed-three-one formula (1), the exact aggregate rational generating function (2), or the conditional limiting law (4); a general upper bound alone does not determine them. OEIS A229617 [6] counts unrestricted binary words with at most three distinct squares, not this conditional **sum** of square counts. The precise claim here is only the fixed-three-one classification and its aggregate/probabilistic consequences, not a new unrestricted square bound.

## Limitations

The formulas apply to linear binary words of Hamming weight exactly three and count distinct literal squares. No claim is made for higher Hamming weights, circular words, or multiplicity-weighted occurrences. The limiting law is specified as a Dirichlet pushforward without a closed density or exact variance. The diagonal case \(b=c\) contributes non-negligibly to individual exact counts and is expressly included in (1) and (2); it has vanishing sampling probability asymptotically. Historical priority is qualified by incomplete access to the full text of Fraenkel–Simpson (1998) and by possible unindexed equivalent work. Independent validation has not been performed.

## References

[1] A. S. Fraenkel and R. J. Simpson, *How Many Squares Must a Binary Sequence Contain?*, Electronic Journal of Combinatorics 2 (1995), R2; publicly dated 1994-12-11. https://doi.org/10.37236/1196

[2] A. S. Fraenkel and J. Simpson, *How Many Squares Can a String Contain?*, Journal of Combinatorial Theory A 82 (1998), 112–120. https://doi.org/10.1006/jcta.1997.2843

[3] G. Kucherov, P. Ochem and M. Rao, *How Many Square Occurrences Must a Binary Sequence Contain?*, Electronic Journal of Combinatorics 10 (2003), R12. https://doi.org/10.37236/1705

[4] A. Deza, F. Franek and A. Thierry, *How Many Double Squares Can a String Contain?*, first arXiv posting 2013-10-12. https://arxiv.org/abs/1310.3429

[5] S. Brlek and S. Li, *On the Number of Squares in a Finite Word*, first arXiv posting 2022-04-21. https://arxiv.org/abs/2204.10204

[6] J. Shallit, OEIS A229617, *Number of binary strings of length n containing at most 3 distinct squares* (2013). https://oeis.org/A229617
