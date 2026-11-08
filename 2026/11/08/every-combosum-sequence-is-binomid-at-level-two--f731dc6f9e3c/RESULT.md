# Every ComboSum sequence is binomid at level two

## Finding

Let \((f_n)_{n\ge1}\) be any sequence of nonzero integers satisfying
\[
\gcd(|f_i|,|f_j|)\mid f_{i+j}\qquad(i,j\ge1).
\]
For \(0\le K\le N\), define the generalized binomial coefficient
\[
B_f(N,K)=\frac{\prod_{j=0}^{K-1}f_{N-j}}{\prod_{j=1}^{K}f_j},\qquad B_f(N,0)=1.
\]
Put \(c_n=B_f(n+1,2)=f_nf_{n+1}/(f_1f_2)\) for every \(n\ge1\). Then **every \(c_n\) is an integer and**
\[
B_c(N,K)\in\mathbb Z\qquad\text{for every }N\ge K\ge0.
\]
In particular, every ComboSum integer sequence is binomid at level two, the first nontrivial level in the binomid-pyramid question.

## Assumptions and scope

All sequence entries are nonzero integers, with no positivity, periodicity, recurrence, growth, or divisibility-chain hypothesis. The divisor in the ComboSum condition may be taken positive. The level-two column starts with \(c_1=1\) and may contain negative integers. The theorem concerns the second column only; it does not establish integrality at all higher levels.

## Proof

**A finite integer sumset lemma.** For finite nonempty integer sets \(X,Y\),
\(|X+Y|\ge|X|+|Y|-1\). To see this, sort their elements and follow a monotone path from the lower-left to upper-right corner of the index grid; each of its \(|X|+|Y|-1\) successive sums is strictly increasing. Furthermore, if equality holds and \(|X|,|Y|\ge2\), both sets are arithmetic progressions with the same positive difference. Indeed, every monotone grid path must then list the *entire* sumset. Interchanging two consecutive horizontal and vertical moves changes just one intermediate sum; equality of the two sorted complete lists forces \(x_{i+1}+y_j=x_i+y_{j+1}\) for every pair of adjacent indices. Thus all consecutive gaps in both sets coincide.

**A semigroup counting lemma.** Let \(S\subseteq\mathbb Z_{\ge0}\) be any additive submonoid containing zero, and put
\[
F(t)=|S\cap[1,t]|,\quad F(0)=0,\quad
\Delta(u,k)=F(u+k)-F(u)-F(k).
\]
For all \(u,k\ge0\), the preceding sumset bound applied to \(S\cap[0,u]\) and \(S\cap[0,k]\) gives \(\Delta(u,k)\ge0\).

We claim a strict refinement: if \(u,k\ge1\), \(1\notin S\), and \(u+1\in S\), then
\[
\Delta(u,k)+\Delta(u,k+1)\ge1.
\]
If \(k+1\notin S\), use the sumset bound on \(S\cap[0,u+1]\) and \(S\cap[0,k]\), observing that \(F(u+1)=F(u)+1\) and \(F(k+1)=F(k)\), to obtain \(\Delta(u,k+1)\ge1\).

Suppose instead that \(k+1\in S\), and assume for contradiction \(\Delta(u,k)=0\). Write \(X=S\cap[0,u]\), \(Y=S\cap[0,k]\). Since \(X+Y\subseteq S\cap[0,u+k]\), minimality forces \(X+Y=S\cap[0,u+k]\) and \(|X+Y|=|X|+|Y|-1\). If \(X=\{0\}\), the element \(k+1\in S\cap[0,u+k]\) lies beyond \(Y\), a contradiction. If \(Y=\{0\}\), use \(u+1\) similarly. Otherwise sumset rigidity gives \(X=\{0,d,\ldots,ad\}\) and \(Y=\{0,d,\ldots,bd\}\) for some \(d\ge2\) and \(a,b\ge1\). Since \(u+1,k+1\in S\cap[0,u+k]=X+Y\), both are multiples of \(d\). As \(d\in S\) and \(ad\) (respectively \(bd\)) is the last multiple of \(d\) not exceeding \(u\) (respectively \(k\)), necessarily \(u+1=(a+1)d\) and \(k+1=(b+1)d\). But \((a+b+1)d\in S\) and
\[
(a+b+1)d\le(a+b+2)d-2=u+k,
\]
while it exceeds \(\max(X+Y)=(a+b)d\). This is again a contradiction, proving the refinement.

**Prime-adic reduction.** Fix a prime \(p\). For each \(r\ge0\), put
\[
S_{p,r}=\{0\}\cup\{n\ge1:\nu_p(|f_n|)>r\}.
\]
The ComboSum hypothesis implies that each \(S_{p,r}\) is an additive submonoid: if both indices lie in it, their \(p\)-valuations are at least \(r+1\), so the same is true of their sum. Denote by \(a_n\) the indicator of the positive elements of one such submonoid and by \(F\) its preceding counting function. The exponent contribution to \(B_c(u+k,k)\), for \(u\ge0\) and \(k\ge1\), is
\[
\begin{aligned}
D(u,k)&=\sum_{j=1}^{k}\bigl(a_{u+j}+a_{u+j+1}-a_j-a_{j+1}\bigr)\\
&=\Delta(u,k)+\Delta(u,k+1)+a_1-a_{u+1}.
\end{aligned}
\]
For \(u=0\), this is zero. For \(u\ge1\), if \(a_{u+1}=0\), nonnegativity of \(\Delta\) gives \(D(u,k)\ge0\). If \(a_1=1\), then the semigroup contains every positive integer, so \(D(u,k)=0\). In the only remaining case \(a_{u+1}=1\), \(a_1=0\), the strict refinement proves \(D(u,k)\ge0\).

Finally \(\nu_p(|f_n|)=\sum_{r\ge0}\mathbf1_{S_{p,r}}(n)\). Consequently the \(p\)-valuation of \(B_c(u+k,k)\) is a finite sum of nonnegative \(D(u,k)\) values. This holds for every prime \(p\), hence \(B_c(u+k,k)\) is an integer. The cases \(k=0\) are one by definition. Taking \(k=1\) also establishes the integrality of every \(c_n\), because \(c_1=1\). This proves the theorem.

## Verification

The standalone `verify_level2.py` enumerates every additively closed subset of the positive integers truncated at 16, tests the semigroup-counting inequality for every admissible \(u,k\), and additionally checks 180 pseudorandom finitely generated submonoids up to index 180. The saved output in `verification_output.txt` reports 785 exhaustively checked closed masks, 94,200 first-stage comparisons, and 2,899,800 additional comparisons. It also directly reconstructs 61,425 generalized binomial coefficients from signed, mixed-prime sequences satisfying the ComboSum condition. These finite checks corroborate the algebraic argument; the infinite claim relies solely on the proof above.

## Relationship to prior work

Shapiro, *Divisibility Properties for Integer Sequences* (arXiv:2302.02243v1, 4 February 2023), defines ComboSum sequences and proves that they are binomid (Proposition 23); Open Question 24 asks whether they are binomid at every level. The published version retains the question. Theorem 15 of that paper proves the stronger all-level property for **divisor-product** sequences, but not for all ComboSum sequences. The result here settles level two for the entire ComboSum class; it does **not** resolve Shapiro's all-level question.

The class considered here genuinely exceeds the paper's divisor-product and divisor-chain sufficient conditions. For example, let \(T=\langle3,5\rangle\), and take \(f_n=2\) if \(n\in T\), \(f_n=1\) otherwise. It is ComboSum because \(T\) is additive. It is not a divisor-chain since \(f_3=2\) but \(f_4=1\); nor is it a divisor-product, since a putative divisor factor at index 15 would equal \(f_{15}f_1/(f_3f_5)=1/2\).

## Limitations

The theorem proves only level-two integrality. It does not settle higher binomid levels or classify all binomid sequences. Finite checks are not a substitute for the proof. The originality comparison covers the specified primary paper and searchable related records; unindexed or differently named work might contain an equivalent theorem.

## References

1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1 (2023), https://arxiv.org/html/2302.02243v1. Relevant statements: Definitions 1, 2, 4, 22; Theorem 15; Proposition 23; Open Question 24.
2. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, INTEGERS 23 (2023), Article A16, https://math.colgate.edu/~integers/x57/x57.pdf (published version; its Open Question 24 is reported in the accessible indexed passage).
