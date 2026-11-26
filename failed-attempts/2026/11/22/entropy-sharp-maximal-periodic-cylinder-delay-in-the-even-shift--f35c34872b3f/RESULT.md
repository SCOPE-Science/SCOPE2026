# Entropy-sharp maximal periodic-cylinder delay in the even shift

## Finding
Let \(X\subset\{0,1\}^{\mathbb Z}\) be the **even shift**, comprising bi-infinite binary sequences in which every finite block \(10^{2j+1}1\) is forbidden. Let \(\mathcal L_n(X)\) denote its admissible words of length \(n\). For \(w\in\mathcal L_n(X)\) define \(\eta(w)\) to be the *least positive period* of any periodic point of \(X\) containing \(w\) at coordinates \(0,\ldots,n-1\), and define
\[
Q_n=\#\{w\in\mathcal L_n(X):\eta(w)=n+1\}.
\]
Then for every \(n\ge2\),
\[
\max_{w\in\mathcal L_n(X)}\eta(w)=n+1,
\qquad
\lim_{n\to\infty}\frac{\log Q_n}{n}=\log\varphi,
\quad \varphi=\frac{1+\sqrt5}{2}.
\]
Thus the set of words requiring the **maximal one-symbol periodic closing extension** grows at the full topological entropy of the even shift. This statement concerns the exponential rate; it does **not** assert a positive limiting fraction of all words.

## Assumptions and scope
All temporal periods are positive integers. The even shift includes the constant zero sequence and all bi-infinite sequences with an even number of zeros between successive ones; arbitrarily long zero tails are allowed. A periodic point of period \(k\) has a defining word of length \(k\), possibly with smaller least period. The word count is that of distinct labelled words, not graph paths. Every logarithm is natural. The result is about standard length-\(n\) cylinder observations; it is not a conjugacy-invariant supremum over generators.

## Proof
**Universal closing bound.** Consider an admissible finite word \(w\) containing a one, and let \(a,b\) be its numbers of initial and terminal zeros. Every internal gap between successive ones is even. If \(a+b\) is even, infinite repetition of \(w\) belongs to \(X\), so \(\eta(w)\le n\). If \(a+b\) is odd, infinite repetition of \(w0\) belongs to \(X\), so \(\eta(w)\le n+1\). For an all-zero word the all-zero fixed point suffices. For even \(n\ge2\), the word \(10^{n-1}\) has no nonempty proper border, and its own periodic repetition is forbidden. For odd \(n\ge3\), the same is true of \(110^{n-2}\). Indeed each starts with a one, ends with a zero, and no proper suffix can equal a proper prefix (for the second word, suffixes starting at the second one begin \(10\), whereas the prefix begins \(11\)). If a length-\(n\) word belongs to a \(k\)-periodic sequence with \(k<n\), it necessarily has the nonempty border of length \(n-k\). Therefore these two witnesses require period at least \(n\), while cyclic repetition of length \(n\) is invalid because its wraparound zero gap is odd. Thus \(\eta=n+1\), establishing sharpness at every \(n\ge2\).

**Large unbordered families.** Fix \(L\ge2\), and for any finite ordered list \(j_1,\ldots,j_s\in\{0,1,\ldots,L-1\}\) (including the empty list), set
\[
w(L;j_1,\ldots,j_s)=11\,0^{2L}1\,(0^{2j_1}1)\cdots(0^{2j_s}1)\,0010.
\]
Its length is \(2L+7+\sum_{i=1}^s(2j_i+1)\). All internal one-to-one zero gaps are even: the first long gap has length \(2L\), the following gaps have lengths at most \(2L-2\), and the final gap has length two. Its trailing zero run has length one, and its initial zero run has length zero. Hence periodic repetition of this word is inadmissible.

The word is also unbordered. Its initial two symbols are \(11\), the next \(2L\) symbols are zero, and its final five symbols are \(10010\). A proper border of length one or two is impossible by these endpoints; at length three the prefix is \(110\) and the suffix is \(010\). For each length \(d\) with \(4\le d\le2L+2\), the prefix ends in \(00\) whereas the suffix ends in \(10\). Any border of length at least \(2L+3\) would force a second occurrence, at a strictly positive starting position, of the marker \(110^{2L}1\). This is impossible: the marker requires a gap of \(2L\) zeros immediately following adjacent ones, whereas all gaps after the initial marker have at most \(2L-2\) zeros (the fixed terminal gap has two). Hence all such words have \(\eta=n+1\). Distinct lists determine distinct words by parsing gaps between ones.

Let \(c_L(m)\) count compositions of \(m\) into parts \(1,3,\ldots,2L-1\), with \(c_L(0)=1\). For each \(m\ge0\),
\[
Q_{2L+7+m}\ge c_L(m),\qquad
\sum_{m\ge0}c_L(m)z^m=\frac1{1-\sum_{j=0}^{L-1}z^{2j+1}}.
\]
The positive dominant root \(\rho_L\in(0,1)\) of \(\sum_{j=0}^{L-1}\rho_L^{2j+1}=1\) is unique for \(L\ge2\). Because the permitted parts include one, the recurrence is aperiodic and its nonnegative coefficients have precise exponential growth \(\lim_{m\to\infty}m^{-1}\log c_L(m)=\log\lambda_L\), where \(\lambda_L=\rho_L^{-1}\). As \(L\uparrow\infty\), the root tends to the solution of \(\sum_{j\ge0}\lambda^{-(2j+1)}=\lambda/(\lambda^2-1)=1\), namely \(\varphi\).

**Entropy upper bound.** The standard two-state labelled right-resolving presentation of the even shift has adjacency matrix \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\). Its path count gives \(\#\mathcal L_n(X)=F_{n+3}-1\), where \(F_0=0,F_1=1\) are Fibonacci numbers: every word containing a one has a unique presenting path, while the all-zero word has two paths. Consequently \(Q_n\le F_{n+3}-1\), yielding \(\limsup n^{-1}\log Q_n\le\log\varphi\). The composition construction gives \(\liminf n^{-1}\log Q_n\ge\log\lambda_L\) for every \(L\ge2\), and letting \(L\to\infty\) proves equality.

## Verification
The standalone `check.py` enumerates the complete finite language for lengths \(2\) through \(14\), computes shortest periodic-cylinder periods by testing every possible root up to length \(n+1\), and checks the sharp maximum. It independently constructs and checks 1,960 marker words for \(2\le L\le5\) and additional composition length at most 13. It is a finite consistency check only; the preceding argument proves the infinite result.

## Relationship to prior work
Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, arXiv:2611.13416v1 (10 November 2026), defines periodic penetration and proves a uniform linear closing bound for primitive finite-type shifts (Proposition 2.27); that does not determine the entropy growth of maximal-delay words in the strictly sofic even shift. Related results on short-period **deficits** in finite-type shifts and on zero-entropy periodic-cylinder spectra address different implications. The even shift's ordinary word entropy is classical; the new assertion isolates the full entropy of its maximal periodic-closing-delay language, with an explicit entropy-approximating unbordered construction.

## Limitations
No closed formula or leading constant is established for \(Q_n\). Equal exponential growth rates do not establish that \(Q_n/\#\mathcal L_n(X)\) has a positive limit. Historical priority of similar marker/unbordered arguments is not fully excluded; no independent mathematical audit has been conducted.

## References
- D. N. Pannipitiya, *Local Periodic Orbit Penetration in Dynamical Systems*, arXiv:2611.13416v1, first public 10 November 2026, https://arxiv.org/abs/2611.13416.
- D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press (1995), background on even shifts and presentations.
- *Entropy-sharp periodic cylinder closure and parity-oscillating short-period counts*, published published-finding corpus record, 17 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-entropy-sharp-periodic-cylinder-closure-and-parity-oscillating-s--22e18f2d92a1 (related finite-type short-period-deficit result; only indexed abstract available).
