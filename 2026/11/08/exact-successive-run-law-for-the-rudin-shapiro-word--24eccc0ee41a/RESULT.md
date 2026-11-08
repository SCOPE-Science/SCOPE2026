# Exact successive-run law for the Rudin–Shapiro word

## Finding

Let \(r=r_0r_1\cdots\) be the sign-valued Rudin–Shapiro word: \(r_n=+\) if the number of possibly overlapping occurrences of `11` in the base-two expansion of \(n\) is even, and \(r_n=-\) otherwise. A **run** is a maximal contiguous string of equal signs. All runs have lengths in \(\{1,2,3,4\}\).

For \(1\le i,j\le4\), let \(q_{ij}^{+}\) be the limiting number of occurrences per input symbol of the pattern \(-+^i-^j+\), and let \(q_{ij}^{-}\) be the corresponding limit for \(+-^i+^j-\). These patterns describe a complete run of one sign of length \(i\), immediately followed by a complete run of the other sign of length \(j\), with both ends witnessed. Both limits exist, coincide, and equal the entries of

\[
Q=(q_{ij}^{+})=(q_{ij}^{-})=
\frac{1}{64}\begin{pmatrix}
2&2&2&2\\
2&0&0&0\\
3&0&1&0\\
1&0&1&0
\end{pmatrix}.
\]

Consequently, exactly nine ordered pairs of run lengths occur, each infinitely often. Under the limiting distribution of runs, successive lengths have common marginal \(p=(1/2,1/8,1/4,1/8)\) and conditional transition matrix

\[
P=\begin{pmatrix}
1/4&1/4&1/4&1/4\\
1&0&0&0\\
3/4&0&1/4&0\\
1/2&0&1/2&0
\end{pmatrix}.
\]

The successive-run mutual information is exactly

\[
I(R_k;R_{k+1})=\frac18+\frac{3}{16}\log_2 3
=0.422180468885\ldots\text{ bits}.
\]

This dependence contrasts with **independence of adjacent signs**: each of the four two-sign factors occurs with limiting frequency \(1/4\).

## Assumptions and scope

The word is one-sided, indexed by all integers \(n\ge0\); signs are literal \(+\) and \(-\), not unspecified binary renamings. A frequency means the limit of the count of occurrences with starting index less than \(N\), divided by \(N\), as \(N\to\infty\). Such an occurrence is permitted to extend beyond index \(N-1\), which changes finite-prefix counts only by a bounded boundary term. Run-length marginal and joint probabilities are obtained by counting complete runs whose left boundary is below \(N\), and then normalizing by the number of such runs. The displayed \(Q\) is **per symbol**, whereas \(P\) is **per run**. Mutual information is computed in bits from the limiting ordered-pair distribution; no Markov assumption is made.

The relevant underlying substitution is the well-known primitive two-uniform substitution \(\phi\) on \(A=\{a,b,c,d\}\):

\[
\phi(a)=ab,\quad\phi(b)=ac,\quad
\phi(c)=db,\quad\phi(d)=dc,
\]

with coding \(\tau(a)=\tau(b)=+\), \(\tau(c)=\tau(d)=-\). The fixed point \(\omega=\phi^\infty(a)\) satisfies \(\tau(\omega)=r\), with this indexing convention.

## Proof

**1. Existence of factor frequencies.** The substitution graph is strongly connected and has a loop, so \(\phi\) is primitive. The standard elementary Perron–Frobenius argument for primitive constant-length substitutions gives a positive frequency for each occurring finite hidden factor and existence of all finite factor frequencies. Equivalently, the fixed point is uniformly recurrent and uniquely ergodic. Let \(F_k(w)\) be the limiting frequency of a hidden length-\(k\) word \(w\), with value zero for absent words.

The substitution's four-letter incidence matrix has constant row and column sums two. Its normalized positive eigenvector is uniform, hence

\[
F_1(a)=F_1(b)=F_1(c)=F_1(d)=\frac14.
\]

For a hidden length-two word \(uv\), half of its possible starting positions lie **inside** one substituted letter and half **cross** a substituted-letter boundary. Accordingly,

\[
F_2(uv)=\frac12\sum_{s\in A}F_1(s)
\mathbf1_{\{\phi(s)=uv\}}
+\frac12\sum_{s,t\in A}F_2(st)
\mathbf1_{\{\phi(s)_2\phi(t)_1=uv\}}.
\]

Here the subscripts \(1,2\) refer to positions within a two-letter substituted block. Substitution into these equations gives precisely eight positive pairs,

\[
\{ab,ac,ba,bd,ca,cd,db,dc\},
\]

all with frequency \(1/8\), with every other hidden pair of frequency zero. The finite balance identities are checked independently by `verify.py`. Primitivity makes this solution unique among block-frequency vectors.

**2. A finite exact recurrence for longer factors.** Splitting the starting index by parity gives, for every \(k\ge3\) and \(w\in A^k\),

\[
\begin{aligned}
F_k(w)={}&\frac12\sum_{v\in A^{\lceil k/2\rceil}}
F_{\lceil k/2\rceil}(v)
\mathbf1_{\{\phi(v)[0:k]=w\}}\\
&+\frac12\sum_{v\in A^{\lceil(k+1)/2\rceil}}
F_{\lceil(k+1)/2\rceil}(v)
\mathbf1_{\{\phi(v)[1:k+1]=w\}}.
\end{aligned}
\]

The bracket notation specifies zero-based half-open substrings. Both antecedent lengths are strictly smaller than \(k\). Thus the preceding four one-letter and eight two-letter frequencies determine all later frequencies by a terminating, rational computation. For any sign word \(z\), its frequency is

\[
G(z)=\sum_{w\in A^{|z|}:\tau(w)=z}F_{|z|}(w).
\]

**3. Exact classification.** Applying the finite recurrence through length ten gives \(G(+++++)=G(-----)=0\). As every factor actually occurring in a primitive substitution has positive frequency, no run can have length five or more. For the two families of complete adjacent-run patterns, the same recurrence gives \(G(-+^i-^j+)=G(+-^i+^j-)=Q_{ij}\) for every \(i,j\in\{1,2,3,4\}\), with \(Q\) exactly as in the Finding. These are 32 separate exact rational evaluations, reproducible from the eight hidden pair frequencies and the displayed recurrence. Nonzero entries correspond to occurring factors, so all nine listed run-length transitions occur infinitely often; zeros correspond to absent factors.

**4. Run-level normalization.** The sum of all entries of \(Q\) is \(1/4\) for each initial sign, so the density of all run boundaries is \(1/2\). Its row sums are \((1/8,1/32,1/16,1/32)\). Dividing by \(1/4\) gives the marginal \(p\), and row normalization gives \(P\). Since the two signs have the identical \(Q\), combining them leaves the same run-level distribution. The distribution satisfies \(pP=p\) directly.

The marginal entropy is \(H(R_k)=7/4\) bits. With \(h_2(u)=-u\log_2u-(1-u)\log_2(1-u)\),

\[
H(R_{k+1}\mid R_k)
=\frac12(2)+\frac14h_2(1/4)+\frac18(1)
=\frac{13}{8}-\frac{3}{16}\log_2 3.
\]

Subtracting yields the displayed exact mutual information. Finally, coding the eight positive hidden pairs shows that the four sign pairs \(++,+-,-+,--\) each have frequency \(2/8=1/4\). Hence adjacent signs are independent despite positive information between adjacent run lengths.

## Verification

The standalone Python 3 program `verify.py` contains no external packages. Its first checker verifies all sixteen hidden pair-balance equations exactly with rational arithmetic, applies the fixed parity recurrence through hidden block length ten, and verifies the 32 sign-specific run-pair entries, the two absent monochromatic length-five factors, and four adjacent-sign frequencies.

An independent second checker constructs the first \(2^{18}=262144\) signs by substitution, compares **every position** against the binary-digit definition using bit operations, and enumerates complete runs directly. This checked prefix contains \(131072\) runs; the observed pair frequencies are compared separately against the exact limits. Running `python3 verify.py` produces the documented `VERIFY_OK` line. Finite prefix tests are corroboration only: the infinite statement follows from substitution primitivity and the exact rational factor-frequency recurrence.

## Relationship to prior work

The run-length sequence itself is explicitly listed as OEIS A203531 (first authored January 2, 2012); its defining word is OEIS A020985. The 2015 Schaeffer–Shallit paper gives the same four-symbol substitution and classifies several factor properties (closed, palindrome-related, balanced and others). The 2016 Lü–Chen–Wen–Wu paper studies abelian complexity, a different invariant. Hendel (2025), Section 8, discusses maximal runs and their starting positions and states the known maximal length four for Rudin–Shapiro. The published items inspected do not state the complete **ordered adjacent-run frequency matrix** or the exact run-level mutual information. The fact that those values are computable from a published substitution is not mistaken for a pre-existing explicit evaluation; they are a new finite consequence of that substitution subject to historical-priority checking. Related work on Rudin–Shapiro string attractors concerns minimum factor-hitting sets, not consecutive-run statistics.

## Limitations

The exact matrix describes adjacent runs, not arbitrary run separations, nor does it imply that the sequence of run lengths is a first-order Markov process. No finite-prefix convergence rate is asserted. The infinite-word result depends on the standard primitive-substitution frequency theorem; the small exact transfer calculations have also been independently checked by code but have not undergone external audit. Relevant unindexed or older run-length literature might contain an equivalent frequency table; that residual historical-priority risk remains.

## References

- OEIS Foundation, [A203531: Run lengths in Golay-Rudin-Shapiro sequence](https://oeis.org/A203531), initially authored January 2, 2012, and [A020985](https://oeis.org/A020985).
- Luke Schaeffer and Jeffrey Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, preprint posted August 9, 2015, [arXiv:1508.02074](https://arxiv.org/abs/1508.02074), especially Section 3.
- Xiaotao Lü, Jin Chen, Zhixiong Wen and Wen Wu, *On the abelian complexity of the Rudin-Shapiro sequence*, preprint posted June 22, 2016, [arXiv:1606.06935](https://arxiv.org/abs/1606.06935).
- Russell Jay Hendel, *A Family of Sequences Generalizing the Thue Morse and Rudin Shapiro Sequences*, preprint posted May 26, 2025, [arXiv:2505.20547](https://arxiv.org/abs/2505.20547), Section 8.
