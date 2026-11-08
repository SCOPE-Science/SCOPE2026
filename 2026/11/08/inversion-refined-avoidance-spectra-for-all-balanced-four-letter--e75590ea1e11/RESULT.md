# Inversion-refined avoidance spectra for all balanced four-letter scattered patterns

## Finding

Let \(A,B\) be nonnegative integers. For any binary word \(w\) with exactly \(A\) zeros and \(B\) ones, put \(c(w)=\binom{w}{01}\), the number of scattered occurrences of \(01\). Given a length-four balanced binary pattern \(p\), define

\[
F^{p}_{A,B}(t)=\sum_{\substack{|w|_0=A,\ |w|_1=B\\p\not\preceq w}}t^{c(w)},
\]

where \(p\not\preceq w\) means that \(p\) does not occur as a scattered subsequence. Define the following three explicit polynomials:

\[
U_{A,B}(t)=\sum_{c=0}^{AB}t^c,\qquad
D_{A,B}(t)=1+\sum_{d=1}^{A}\sum_{q=1}^{B}t^{dq},
\]
\[
T_{A,B}(t)=\begin{cases}1,&A=0,\\
\displaystyle\sum_{i=0}^{B}t^i+\sum_{j=2}^{A}\sum_{i=0}^{B-1}t^{i+j},&A\ge1.\end{cases}
\]

All sums with an empty index range are zero. Then the *complete six-pattern classification*, valid also for \(A=0\) or \(B=0\), is

\[
\begin{aligned}
F^{0110}_{A,B}(t)&=F^{1001}_{A,B}(t)=U_{A,B}(t),\\
F^{0101}_{A,B}(t)&=D_{A,B}(t),& F^{1010}_{A,B}(t)&=t^{AB}D_{A,B}(t^{-1}),\\
F^{0011}_{A,B}(t)&=T_{A,B}(t),& F^{1100}_{A,B}(t)&=t^{AB}T_{A,B}(t^{-1}).
\end{aligned}
\]

In particular, every one of these six patterns has *exactly* \(AB+1\) avoidance words with composition \((A,B)\), even though their distributions among fixed Parikh-matrix classes are uniform, divisor-controlled, or piecewise linear, respectively. For a nonempty class
\[
L_{A,B,C}=\{w:|w|_0=A,\ |w|_1=B,\ c(w)=C\},\quad 0\le C\le AB,
\]
the exact conditional containment probability is
\[
\Pr(p\preceq w\mid w\in L_{A,B,C})
=1-\frac{[t^C]F^p_{A,B}(t)}{[t^C]{A+B\brack A}_t},
\]
where the denominator is the strictly positive coefficient of the Gaussian binomial polynomial.

The coefficient formulas, for \(0\le C\le AB\), are
\[
[t^C]U_{A,B}=1,
\quad
[t^C]D_{A,B}=
\begin{cases}1&C=0,\\
\#\{d\mid C:1\le d\le A,\ 1\le C/d\le B\}&C>0,
\end{cases}
\]
\[
[t^C]T_{A,B}=\mathbf 1_{C\le B}+
\max\bigl(0,\min(A,C)-\max(2,C-B+1)+1\bigr).
\]

For \(A,B\ge2\), *every* representative of \(L_{A,B,C}\) contains \(0011\) exactly when \(C\ge A+B\); every representative contains \(1100\) exactly when \(AB-C\ge A+B\). In contrast, no such class forces \(0110\) or \(1001\). Requiring \(0101\) in every representative is equivalent to the absence of an admissible divisor in the displayed formula (and its reversed analogue gives \(1010\)).

Under the uniform distribution over the \(AB+1\) avoidance words of any fixed pattern, the expectation of \(c(w)\) for \(0110,0101,0011\), respectively, equals
\[
\frac{AB}{2},\qquad
\frac{AB(A+1)(B+1)}{4(AB+1)},\qquad
\frac{AB(A+B)}{2(AB+1)}.
\]
These different first moments demonstrate that the unrefined equal-cardinality phenomenon loses its symmetry on passing to individual two-deck classes.

## Assumptions and scope

The alphabet is the ordered binary alphabet \(\{0,1\}\). Subsequence containment is scattered (letters need not be contiguous). Both \(A\) and \(B\) may be zero, the empty host is included, and the six listed patterns are exactly those with two zeros and two ones. Counts of \(01\) use increasing position pairs. All identities hold for arbitrary nonnegative integers, with no asymptotic restriction. Inverse powers in reflected polynomials are interpreted after multiplication by \(t^{AB}\), which gives an ordinary polynomial.

## Proof

**1. The uniform type.** Write an arbitrary word with \(A\) zeros uniquely as
\[
w=1^{x_0}0\,1^{x_1}0\cdots0\,1^{x_A},\qquad
x_i\ge0,\quad \sum_{i=0}^{A}x_i=B.
\]
Its scattered \(01\)-count is \(c(w)=\sum_{j=1}^{A}j x_j\). A word contains \(0110\) if and only if at least two ones occur strictly between its first and last zeros, i.e., \(\sum_{j=1}^{A-1}x_j\ge2\). Thus an avoider has no interior one or precisely one interior one. For \(A>0\), write \(C=Ak+r\), \(0\le r<A\). The unique avoider at count \(C\) is
\[
\begin{cases}
1^{B-k}0^A1^k,&r=0,\\
1^{B-k-1}0^r1\,0^{A-r}1^k,&1\le r<A.
\end{cases}
\]
All displayed exponents are nonnegative because \(0\le C\le AB\). If \(A=0\), the unique host is \(1^B\). Consequently every admissible \(C\) has one \(0110\)-avoider, proving \(F^{0110}=U\). Complementing both symbols exchanges \(0110\) with \(1001\), and reverses the \(01\)-count after interchanging \(A,B\). Since the uniform polynomial is symmetric in \(A,B\) and palindromic, \(F^{1001}=U\).

**2. The divisor type.** A word avoids \(0101\) if and only if it has the form \(1^*0^*1^*0^*\). If \(C=0\), the sole word in its class is \(1^B0^A\). If \(C>0\), every avoider is uniquely expressible as
\[
w=1^{B-q}0^d1^q0^{A-d},\qquad1\le d\le A,\quad1\le q\le B,
\]
and then \(C=dq\). Conversely each such choice gives an avoider with that count, yielding \(D_{A,B}\) and its coefficient-by-divisor formula. Reversal maps \(0101\) to \(1010\) and \(C\) to \(AB-C\), proving the reflected identity.

**3. The interval type.** For \(0011\), use the same unique block representation in step 1. Such a word contains \(0011\) precisely when at least two ones occur to the right of the second zero, i.e. \(\sum_{j=2}^{A}x_j\ge2\). An avoider therefore has either no one in these blocks, contributing \(\sum_{i=0}^{B}t^i\), or exactly one one in block \(j\in\{2,\dots,A\}\), leaving \(x_1=i\in\{0,\dots,B-1\}\) and contributing \(t^{i+j}\). There are no repeated representations. The result is \(T_{A,B}\) for \(A\ge1\); for \(A=0\) the only host is \(1^B\), giving \(T_{0,B}=1\). Intersection of the integer constraints \(2\le j\le A\) and \(C-B+1\le j\le C\) gives its coefficient formula. Reversal maps \(0011\) to \(1100\) and sends \(C\mapsto AB-C\), proving the remaining identity.

**4. Consequences.** Evaluation at \(t=1\) gives \(AB+1\) for all three types: for \(T\), the two summands give \(B+1\) and \((A-1)B\) (with empty ranges handled separately), and for \(D\) they give \(1+AB\). A word has fixed-class size \([t^C]{A+B\brack A}_t\) by the standard rectangle-partition correspondence; the division is valid since every \(C\) in the interval occurs. For \(A,B\ge2\), the support of \(T\) is exactly the integer interval \([0,A+B-1]\), proving the sharp universal containment thresholds. For the mean formulas, differentiate the three polynomials at \(t=1\), divide by \(AB+1\), and sum the arithmetic progressions. The numerator derivatives are, respectively, \(AB(AB+1)/2\), \(AB(A+1)(B+1)/4\), and \(AB(A+B)/2\). This proves all claims.

## Verification

A standalone exhaustive Python program `verify.py` independently enumerates all \(2^n\) binary words of every length \(0\le n\le14\). For each of the six patterns, every composition, and every realized \(01\)-count, it directly tests scattered containment and compares the counts against the polynomial coefficients above. It checks 11,640 coefficient instances and verifies the \(AB+1\) total and the exact first moments for every \(0\le A,B\le25\). The reproducible command is `python3 verify.py`. These finite tests are corroboration only; the unbounded statement is established by the block-decomposition proof.

## Relationship to prior work

Fazekas, Huang, and Mercaş (first public preprint 2026-10-05) study existential and universal subsequence containment in binary Parikh-matrix classes. Their Section 5 identifies the \(0101\)-avoiding run language and reduces its existential avoidance to bounded factoring; their general probability theorem gives additive approximations, but not the present exact six-pattern coefficient spectrum. Golafshan (2026) and the earlier lexicographic-representative theory give a canonical word in each two-binomial class; the uniform \(0110\)/\(1001\) line is accordingly treated as established background rather than independently novel. Richomme's 2025 preprint and Golafshan's work give the rectangle-partition and Gaussian-binomial class-size theory, not a complete balanced-length-four pattern-resolved avoidance distribution. The new contribution is the full comparison of all six balanced patterns after refinement by the exact \(01\)-count, especially the interval distribution and its sharp universal threshold, together with divisor and uniform profiles and the differing first moments.

## Limitations

The theorem classifies only the six length-four patterns with two zeros and two ones. It makes no claim for other compositions, longer patterns, or joint avoidance of several patterns. The unrefined total \(AB+1\), Gaussian class sizes, and canonical representatives are previously known; they are not presented as discoveries. Directly accessible prior works were checked for the specific six-pattern coefficient formulas; undiscovered equivalent tables or classical inversion-refined scattered-pattern identities remain a residual priority risk. Scientific results have not undergone independent validation.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717v1 (first public 2026-10-05), https://arxiv.org/abs/2610.06717.
2. M. Golafshan, *Binary binomial equivalence via hyperplane arrangements*, arXiv:2606.23426v1 (first public 2026-06-22), https://arxiv.org/abs/2606.23426.
3. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159v1 (first public 2025-10-08), https://arxiv.org/abs/2510.07159.
4. M. Rigo and P. Salimov, *Another generalization of abelian equivalence: binomial complexity of infinite words*, 2015; cited for binary two-binomial class counting in Golafshan (2026).
