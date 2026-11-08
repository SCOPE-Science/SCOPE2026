# Parikh-spectrum intervals and a Dirichlet mean for Abelian squares in three-marker binary words

## Finding
For a finite binary word \(w\), call \(uv\) an Abelian square if the nonempty equal-length halves \(u,v\) have equal Parikh vectors. Two Abelian-square factors count as **one class** exactly when the Parikh vectors of their halves coincide. Let \(Q(w)\) be the number of these classes, *not* the number of different literal square factors or occurrences.

For all integers \(a,b,c,d\ge0\), put \(w=0^a1\,0^b1\,0^c1\,0^d\) and \(M=\max(a,b,c,d)\). For any nonnegative integers \(A,g,B\) define the possibly empty integer interval
\[
I(A,g,B)=\left\{r\in\mathbb Z:\ \left\lfloor\frac{g+3}{2}\right\rfloor\le r\le
\min\left(\left\lfloor\frac{A+B+g+2}{2}\right\rfloor,A+g+1,B+g+1\right)\right\}.
\]
Then the exact, all-length formula is
\[
\boxed{Q(w)=\left\lfloor\frac M2\right\rfloor+
\left|I(a,b,c)\cup I(b,c,d)\right|.}
\]
The first term counts Parikh vectors of all-zero square halves; the union counts vectors of halves with exactly one \(1\).

For every integer \(n\ge3\), let \(W_n\) be uniform among the \(\binom n3\) indexed words of length \(n\) with three ones. If \(X=(A,B,C,D)\) has the Dirichlet distribution with parameters \((1,1,1,1)\), define the continuous interval (empty if its upper endpoint is below its lower endpoint)
\[
J(A,g,B)=\left[\frac g2,\min\left(\frac{A+B+g}{2},A+g,B+g\right)\right].
\]
With \(\lambda\) denoting interval length, set
\[
Z=\frac12\max(A,B,C,D)+\lambda\bigl(J(A,B,C)\cup J(B,C,D)\bigr).
\]
Then
\[
\boxed{\frac{Q(W_n)}n\ \xrightarrow{\ d\ }\ Z,
\qquad \lim_{n\to\infty}\frac{\mathbb E Q(W_n)}n=\mathbb EZ=\frac{157}{288}.}
\]
The limiting law is nonconstant: for example, the continuous function defining \(Z\) takes values \(3/8\) and \(7/20\) at the interior simplex points \((1/4,1/4,1/4,1/4)\) and \((2/5,1/10,1/10,2/5)\), respectively.

## Assumptions and scope
The alphabet is \(\{0,1\}\), occurrences are contiguous, and the total number of ones is **exactly three**. The word is linear, with distinct labeled positions, and \(a,b,c,d\) can be zero. A square has positive half-length. Equivalence is by the common Parikh vector of the two halves. The population law samples all \(\binom n3\) three-one words uniformly, not necklaces or rotation classes. The theorem concerns an exact wordwise statistic and an asymptotic distribution, and makes no claim about unrestricted binary words or more than three ones.

## Proof
**One-pair interval lemma.** Consider a factor having exactly two ones separated by \(g\) zeros, with at most \(A\) zeros preceding the first and at most \(B\) zeros following the second without meeting another one. Every candidate factor is \(0^L1\,0^g1\,0^R\) with \(0\le L\le A\), \(0\le R\le B\). For it to be an Abelian square of half-length \(r\), both halves must contain exactly one one. Thus
\[
L+R=2r-g-2,\qquad 0\le L\le\min(A,r-1),\qquad 0\le R\le\min(B,r-1).
\]
The existence of such \(L,R\) is equivalent to \(2r-g-2\ge0\) and
\[
2r-g-2\le\min(A,r-1)+\min(B,r-1).
\]
Using \(\min(x,u)+\min(y,u)=\min(x+y,x+u,y+u,2u)\), and noting that the last resulting inequality is automatic for \(g\ge0\), these are precisely the lower and three upper bounds defining \(I(A,g,B)\). Hence all feasible half-lengths form exactly that integer interval, including the empty case.

Every Abelian square in a three-one word contains an even number of ones, hence either zero or two. The zero-one count is \(2r\) zeros for \(1\le r\le\lfloor M/2\rfloor\). If there are two ones they must be an adjacent pair in the ordered list of all three ones; the first pair has outer capacities \((a,c)\) and inner gap \(b\), and the second pair has outer capacities \((b,d)\) and gap \(c\). A vector with exactly one one in each half is specified solely by \(r\). The interval lemma and union eliminate duplicates and prove the formula.

For a uniform three-one word, \((a,b,c,d)\) ranges uniformly over the weak compositions of \(n-3\) into four parts. The normalized gaps converge in distribution to the uniform measure (density \(6\)) on the three-dimensional standard simplex, namely Dirichlet\((1,1,1,1)\). The endpoints in the integer intervals differ by at most a constant from \(n\) times their continuous counterparts. In fact, uniformly in all gap tuples, \(Q(w)/n\) differs by \(O(1/n)\) from the above continuous function evaluated at \((a,b,c,d)/n\). The continuous mapping theorem gives the distributional limit; boundedness gives convergence of expectations.

To evaluate its expectation, the standard simplex maximum formula gives
\[
\frac12\mathbb E\max(A,B,C,D)=\frac12\cdot\frac{H_4}{4}=\frac{25}{96}.
\]
For the union use inclusion-exclusion. In coordinates \((a,b,c,r)\), with \(d=1-a-b-c\), let \(P_1\) be the four-dimensional polytope defined by \(a,b,c,d,r\ge0\) and
\[
b\le2r\le a+b+c,\qquad r\le a+b,\quad r\le b+c.
\]
Let \(P_{12}\) be its intersection with
\[
c\le2r\le b+c+d,\qquad r\le c+d.
\]
Their Euclidean four-volumes are exactly \(1/32\) and \(13/864\), respectively, verified by the finite exact Ehrhart calculation below. Since Dirichlet density is \(6\), symmetry gives
\[
\mathbb E\lambda(J(A,B,C)\cup J(B,C,D))
=6\left(2\cdot\frac1{32}-\frac{13}{864}\right)=\frac{41}{144}.
\]
Adding \(25/96\) yields \(157/288\).

**Exact polytope-volume certificate.** Enumerating all intersections of four boundary hyperplanes and filtering against the inequalities gives seven vertices for \(P_1\) and ten for \(P_{12}\), all with denominators dividing \(12\). Thus Ehrhart's theorem says the lattice-point count of the dilate \(12kP\) is an ordinary polynomial in \(k\) of degree at most four (including \(k=0\)); its fourth finite difference is \(4!\,12^4\operatorname{vol}(P)\). For \(k=0,1,2,3,4\), exact counts are, respectively,
\[
L_{P_1}(12k)=(1,1225,14365,65341,195625),
\]
\[
L_{P_{12}}(12k)=(1,593,6923,31471,94205).
\]
Their fourth differences are \(15552\) and \(7488\), giving volumes \(1/32\) and \(13/864\). The included executable certificate independently enumerates vertices by rational Gaussian elimination and all lattice counts by integer inequalities; these finite computations do **not** substitute for the interval lemma or the application of Ehrhart's theorem.

## Verification
Run \(\texttt{python3 reproduce.py}\) from the folder containing the included standalone script. It independently builds every literal factor of each three-one word through length \(32\), directly checks Abelian squares and their half-Parikh vectors, and compares with the wordwise formula. It also verifies rational vertex denominators, lattice-point totals, fourth differences and the limiting constant using Python standard-library exact arithmetic. The checks below were executed using the exact included script before packaging. Full finite word enumeration is a check, not the proof of the infinite theorem.

## Relationship to prior work
Kociumaka, Radoszewski, Rytter and Waleń distinguish **literal distinct** from **Abelian-nonequivalent** squares and establish general extremal bounds and an \(O(nm)\) bound for words with \(m\) runs (2014 conference version; expanded 2016 paper). They do not give the exact three-one half-Parikh spectrum, its conditional limiting law, or the constant \(157/288\). The 2026 analysis by Fazekas and collaborators concerns minima of the number of **literal distinct** Abelian-square factors at fixed Parikh vectors, and its three-one minimizer theorem does not determine the nonequivalent population distribution. A separate exact formula for the number of *literal distinct* Abelian squares in three-one words counts individual factor strings, not their Parikh-vector images; that scalar count cannot recover the present interval union or its Dirichlet expectation without additional argument.

## Limitations
This is a self-reviewed mathematical result, not an independent audit. The proof uses the standard Ehrhart quasi-polynomial theorem; the finite vertex and lattice certificates are exact but require trusting a short Python script. The full limiting distribution is specified as an explicit Dirichlet functional, without a closed cumulative-distribution formula or convergence rate. Historical priority may be affected by unindexed results about weak squares, square vectors, or sparse binary words. Nothing here proves new extremal bounds for unrestricted words.

## References
- T. Kociumaka, J. Radoszewski, W. Rytter and T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, Developments in Language Theory 2014, DOI: 10.1007/978-3-319-09698-8_19; expanded preprint https://arxiv.org/abs/1604.02238 (first preprint release 2016-04-08).
- S. Z. Fazekas, A. Mammoliti, R. Mercaş and J. Simpson, *Binary Words Containing Few Abelian Squares*, https://arxiv.org/abs/2604.23188 (2026-04-25).
- OEIS A262265, maximum number of nonequivalent Abelian squares in a binary word: https://oeis.org/A262265 (general finite-length extremal data, not this fixed-weight conditional law).
