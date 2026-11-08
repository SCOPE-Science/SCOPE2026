# Balanced two-run periods maximize distinct subsequences, with an exact length enumerator

## Finding
For integers \(a,b\ge1\), \(m\ge0\), write \(W_m=(0^a1^b)^m\). Let \(u\preceq w\) mean that the binary word \(u\) is obtained from \(w\) by deleting zero or more positions, and count equal output words only once. Define
\[
D_m^{a,b}(x)=\sum_{u\preceq W_m}x^{|u|},\qquad A_a(x)=\sum_{j=1}^{a}x^j,\quad B_b(x)=\sum_{j=1}^{b}x^j,
\]
where the empty subsequence contributes \(1\). Put \(K(x)=x^a+x^b+A_a(x)B_b(x)\). Then the **exact length enumerator** is
\[
\boxed{\sum_{m\ge0}D_m^{a,b}(x)z^m=\frac{(1+[A_a(x)-x^a]z)(1+[B_b(x)-x^b]z)}{(1-z)(1-K(x)z+x^{a+b}z^2)}.}
\]
Thus every coefficient \([x^j]D_m^{a,b}(x)\), for \(0\le j\le m(a+b)\), is specified by a rational two-variable generating function.

Writing \(s=a+b\), \(p=ab\), and \(d_m^{a,b}=D_m^{a,b}(1)\), evaluation at \(x=1\) gives
\[
\boxed{\sum_{m\ge0}d_m^{a,b}z^m=\frac{1+(s-2)z+(p-s+1)z^2}{(1-z)(1-(p+2)z+z^2)}.}
\]
For fixed \(s\ge2\) and \(m\ge1\), the total \(d_m^{a,b}\) increases strictly with \(p=ab\). Among all positive run lengths with \(a+b=s\), it is therefore maximized exactly at \(\{a,b\}=\{\lfloor s/2\rfloor,\lceil s/2\rceil\}\). Finally, setting
\[
\Lambda(p)=\frac{p+2+\sqrt{p(p+4)}}2,
\]
one has \(\lim_{m\to\infty}(d_m^{a,b})^{1/m}=\Lambda(p)\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). The parameters \(a,b\) are positive integers, and the number of periods \(m\) is any nonnegative integer. Subsequence containment is scattered, not contiguous; **distinct values**, not embedding multiplicities, are counted. The power-series identity is formal in \(z\) with coefficients in \(\mathbb Z[x]\). The extremal result is about totals \(D_m^{a,b}(1)\) for \(m\ge1\), not a claim of coefficientwise extremality at every length.

## Proof
**Step 1 — exact state update for a letter.** For a processed prefix, let \(E_0(x)\) and \(E_1(x)\) enumerate distinct nonempty subsequences ending in \(0\) and \(1\), respectively. They are disjoint classes. Upon appending \(0\), all currently attainable subsequences ending in \(0\) are precisely \(v0\) with \(v\) an old subsequence (possibly empty): using the last newly appended zero realizes all of these, and every earlier ending-zero subsequence occurs among them by dropping its final zero. Hence the update is exactly
\[
(E_0,E_1)\longmapsto(x(1+E_0+E_1),E_1).
\]
For appending \(1\), exchange the roles of the symbols. Repeating the zero update \(a\) times gives \(E_0'=x^a E_0+A_a(x)(E_1+1)\). Repeating the one update \(b\) times afterward gives \(E_1'=x^bE_1+B_b(x)(E_0'+1)\).

**Step 2 — a finite transfer and its inverse.** With column vector \((E_0,E_1,1)^\mathsf T\), a complete period acts by
\[
P(x)=\begin{pmatrix}
x^a&A_a(x)&A_a(x)\\
x^aB_b(x)&x^b+A_a(x)B_b(x)&B_b(x)(1+A_a(x))\\
0&0&1
\end{pmatrix}.
\]
Starting from \(v_0=(0,0,1)^\mathsf T\), the exact enumerator is \(D_m^{a,b}(x)=(1,1,1)P(x)^m v_0\). Thus
\[
\sum_{m\ge0}D_m^{a,b}(x)z^m=(1,1,1)(I-zP(x))^{-1}v_0.
\]
The upper-left two-by-two block of \(P(x)\) has trace \(K(x)\) and determinant \(x^{a+b}\). Consequently \(\det(I-zP)=(1-z)(1-K(x)z+x^{a+b}z^2)\). Multiplying the numerator of the displayed resolvent by this determinant and simplifying yields \((1+[A_a(x)-x^a]z)(1+[B_b(x)-x^b]z)\). This proves the first boxed identity for all parameters and coefficients, including \(m=0\). In particular \(D_0^{a,b}(x)=1\) and \(D_1^{a,b}(x)=(1+A_a(x))(1+B_b(x))\).

**Step 3 — the fixed-period-length extremal property.** Substitute \(x=1\): now \(A_a(1)=a\), \(B_b(1)=b\), and \(x^a=x^b=1\). The second boxed identity follows. Regard \(s\ge2\) as fixed and treat \(p\ge1\) as a continuous parameter. Write its right-hand side as \(F_s(p,z)\). Direct differentiation in the formal power-series ring \(\mathbb Q[p][[z]]\) gives
\[
\frac{\partial F_s}{\partial p}=\frac{z(1+sz-z^2)}{[1-(p+2)z+z^2]^2}.
\]
Set \(h_j=[z^j](1-(p+2)z+z^2)^{-1}\) for \(j\ge0\), with \(h_{-1}=0\). Then \(h_0=1\), \(h_1=p+2\), and \(h_{j+1}=(p+2)h_j-h_{j-1}\). For \(p\ge1\) these are strictly increasing positive numbers: the recurrence gives \(h_{j+1}-h_j=(p+1)h_j-h_{j-1}>0\), inductively. Define \(q_j=\sum_{i=0}^j h_i h_{j-i}\) for \(j\ge0\) and \(q_j=0\) for \(j<0\). The sequence \(q_j\) is strictly increasing on nonnegative indices since \(h_{j+1-i}>h_{j-i}\) and there is an additional positive convolution term. Therefore the coefficient of \(z^m\) in \(\partial F_s/\partial p\), namely
\[
q_{m-1}+s q_{m-2}-q_{m-3},
\]
is strictly positive for every integer \(m\ge1\) and \(p\ge1\). Thus \(d_m^{a,b}\), for fixed \(s\), is strictly increasing as a function of \(ab\). The integer product \(ab=a(s-a)\) has its unique maximizing unordered split at \(\{\lfloor s/2\rfloor,\lceil s/2\rceil\}\).

**Step 4 — the exact exponential base.** The two roots of \(\lambda^2-(p+2)\lambda+1=0\) are \(\Lambda(p)>1\) and \(\Lambda(p)^{-1}<1\). The smallest-modulus pole of the total generating function is therefore \(z=\Lambda(p)^{-1}\), strictly inside the pole at \(z=1\). It is simple and not canceled by the numerator \((1+(a-1)z)(1+(b-1)z)\), which is positive there. Partial fractions therefore show \(d_m^{a,b}=c\Lambda(p)^m+O(1)\) for some \(c>0\), proving the root limit.

## Verification
A standalone standard-library Python checker (`checker.py`) independently computes the full length profile via the two-ending-letter transfer, a polynomial recurrence extracted from the rational generating function, and (for bounded source lengths) explicit sets of distinct subsequence values. On this package it passed 112 transfer/recurrence comparisons, 73 direct value-set comparisons, and 190 finite balance comparisons. These finite tests are checks on the algebra, not substitutes for the proof above. For example, at \(s=6\), \(m=3\), the counts for run splits \((1,5),(2,4),(3,3)\) are respectively \(609,1563,2017\). The case \(a=b=1\) reproduces the Fibonacci extremal formula \(d_m^{1,1}=F_{2m+3}-1\).

## Relationship to prior work
Flaxman, Harrow and Sorkin (2004) prove that *globally* across all binary words of a given length, alternating words maximize the number of distinct subsequences, and give generating functions for these global maxima (Theorems 2 and 5). Their result covers \(a=b=1\) but does not specify the enumerators of arbitrary \((0^a1^b)^m\) or the optimal run split under a fixed period \(a+b\) when longer runs are required. Bruda (first public release June 30, 2026) considers the different statistic of indexed occurrences of a prescribed scattered pattern and enumerates words by that occurrence frequency; it does not identify distinct-subsequence value profiles or the fixed-run-length optimum. Related work on random-word expectations treats an average over input words, not this deterministic periodic family. The new result is a constrained structural identity and extremal comparison, not a claim to originate the underlying distinct-subsequence dynamic programming recurrence.

## Limitations
The conclusion does not concern subsequence embedding multiplicities, general nonperiodic inputs, aperiodic pattern families, or coefficientwise maximality for each subsequence length. The general DP method is classical; the specialized rational formula and strict balancing law are what is established here. An earlier unindexed specialization or a general equivalence not identified in the inspected literature could affect historical priority. Independent review has not been performed.

## References
- Abraham Flaxman, Aram W. Harrow, Gregory B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics **11** (2004), R8, https://doi.org/10.37236/1761 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r8/pdf .
- Glenn Bruda, *Enumerating binary words restricted by subsequence frequency*, first public preprint June 30, 2026, https://arxiv.org/abs/2607.02578 .
- Yonah Biers-Ariel, Anant Godbole, Elizabeth Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, Discrete Mathematics & Theoretical Computer Science **19**(2) (2018), https://doi.org/10.23638/DMTCS-19-2-10 .
