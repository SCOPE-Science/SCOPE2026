# Sharp two-tier shift correlations for the modulo-nine Apéry character

## Finding
Let
\[
a_n(r,s)=\sum_{j=0}^{n}\binom nj^r\binom{n+j}{j}^s,
\quad r,s\in\mathbb Z_{>0},\quad r\equiv2\pmod3,\quad s\equiv2\pmod6.
\]
Let \(\vartheta:(\mathbb Z/9\mathbb Z)^\times\to\mathbb C^\times\) be the multiplicative character specified by \(\vartheta(5)=\omega=e^{\pi i/3}\), and let \(X(n)=\vartheta(a_n(r,s)\bmod9)\). All terms are units modulo nine by the cited Apéry congruence. For every positive integer shift \(h\), the ordinary Cesàro correlation exists:
\[
C(h)=\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}X(n+h)\overline{X(n)}.
\]
The convergence has error \(O_h(\log(2N)/N)\). All \(C(h)\) are strictly positive rational numbers. Writing \(h=\sum_{j=0}^m d_j3^j\), with \(d_j\in\{0,1,2\}\), one has the exact all-shift formula
\[
C(h)=(1,0)T_{d_0}T_{d_1}\cdots T_{d_m}\binom{1}{1/2},
\qquad
T_0=\begin{pmatrix}1&0\\1/3&1/3\end{pmatrix},\quad
T_1=\begin{pmatrix}1/3&1/3\\1/3&1/3\end{pmatrix},\quad
T_2=\begin{pmatrix}1/3&1/3\\0&1\end{pmatrix}.
\]
The two highest distinct positive correlation levels have exact rigidity:
\[
C(h)=\tfrac12\iff h\in\{3^j,2\cdot3^j:j\ge0\},
\]
\[
C(h)=\tfrac13\iff h=(u+3v)3^j
\quad\text{for some }j\ge0,\ u,v\in\{1,2\}.
\]
Every other positive shift has \(0<C(h)<1/3\). The infimum over positive shifts is zero, not attained: for every integer \(m\ge1\),
\[
C((3^m-1)/2)=\tfrac12(2/3)^{m-1}.
\]
Thus the character correlations are identical for all allowed pairs of Apéry parameters, rational despite the character being complex, and have a strict gap between the maximal and next-to-maximal values.

## Assumptions and scope
The base-three digit count \(s_1(n)\) is the number of digits equal to one in the finite ternary expansion of \(n\ge0\), with \(s_1(0)=0\). Every parameter pair is integral and positive with the stated residue conditions. The character is well defined because five generates the six-unit group modulo nine. The correlation uses unwrapped indices and the usual natural-average limit, not a cyclic modulo-power average. For \(h=0\), the same matrix convention gives \(C(0)=1\). The classifying statements apply to strictly positive shifts. There is no assertion for parameter classes outside the stated family, for other moduli, or for higher-point correlations.

## Proof
**1. Arithmetic digit formula.** Corollary 25 of Krattenthaler–Müller [1] asserts, for all parameters here and every index, that the residue of \(a_n(r,s)\pmod9\) is \(5^{s_1(n)}\pmod9\). In particular it is always invertible. Therefore
\[
X(n)=\omega^{s_1(n)},\qquad \omega+\overline\omega=1.
\]
This input congruence is an earlier theorem, not a contribution of this finding.

**2. Carry matrices.** To add \(h\) to a uniform ternary integer digit by digit, use carry state \(c\in\{0,1\}\). For each ternary input digit \(a\in\{0,1,2\}\) and digit \(d\) of \(h\), the output digit is \(b=(a+d+c)\bmod3\), and next carry is \(c'=\lfloor(a+d+c)/3\rfloor\). Assign the weight
\[
\omega^{\mathbf1_{b=1}-\mathbf1_{a=1}}.
\]
Averaging this weight over the three equally likely input digits produces a row-to-column matrix indexed by the old and new carries. Directly enumerating the nine pairs \((d,c)\) gives exactly the matrices \(T_0,T_1,T_2\) displayed in the finding. Every entry is rational and nonnegative because \(\omega+\overline\omega=1\).

**3. Terminal carry.** After the last nonzero shift digit, a carry of zero contributes tail expectation one. A carry of one propagates through each subsequent ternary digit two, and disappears at the first digit zero or one. Conditional on disappearing, these two first non-two digits are equally likely, and their weight factors are \(\omega\) and \(\overline\omega\), respectively. Hence the carry-one terminal expectation is \((\omega+\overline\omega)/2=1/2\). The carry almost surely disappears, proving the terminal column \((1,1/2)^T\). Iterated conditioning proves the displayed matrix product for the limit along complete ternary blocks. It also establishes its rationality and positivity: all entries are nonnegative, the terminal entries are positive, and both rows needed at any finite step have positive total mass.

**4. Ordinary Cesàro limit and quantitative error.** Fix \(h>0\). Consider a block of length \(3^L>h\) aligned at an integer multiple of \(3^L\). For all but at most \(h\) indices in that block, adding \(h\) causes no carry past the first \(L\) digits, so the character ratio is exactly the same as on the block beginning at zero. The two block sums consequently differ by at most \(2h\), since each summand has modulus one. In the zero-based block, the finite carry calculation differs from the infinite terminal expectation on at most \(h\) choices of the lower \(L\) digits, giving error at most another \(2h\). For small blocks \(3^L\le h\) the trivial error \(2\cdot3^L\le2h\) suffices. A base-three decomposition of any interval \([0,N)\) into at most two aligned blocks of each length has \(O(\log(2N))\) blocks. Thus the difference between the partial correlation sum and \(NC(h)\) is \(O_h(\log(2N))\). This proves the ordinary limit, not merely a subsequence limit.

**5. Rigidity of the two upper levels.** Multiplication by \(T_0\) on the right fixes \(v=(1,1/2)^T\), while multiplication by \(T_0\) on the left fixes the row \((1,0)\). We may thus disregard trailing zero digits above and below the nonzero digits of \(h\). The highest nonzero digit, whether one or two, gives \(T_1v=T_2v=(1/2,1/2)^T\). If this is also the lowest nonzero digit, the output is \(1/2\). Otherwise, all remaining carry matrices map the square \([0,1/2]^2\) to itself. The lowest nonzero digit maps a column \((x,y)^T\) to first coordinate \((x+y)/3\), so its output is at most \(1/3\). Equality requires \(x=y=1/2\). Any intervening zero gives \(T_0(1/2,1/2)^T=(1/2,1/3)^T\); any earlier nonzero digit gives \(T_1(1/2,1/2)^T=(1/3,1/3)^T\) or \(T_2(1/2,1/2)^T=(1/3,1/2)^T\). Once a coordinate becomes strictly less than \(1/2\), these nonnegative matrices cannot simultaneously restore both coordinates to \(1/2\). Hence equality at \(1/3\) occurs precisely for two nonzero digits in consecutive positions. The one-digit case characterizes equality at \(1/2\).

**6. Sharp infimum.** The matrix \(T_1\) maps a constant column \((c,c)^T\) to \((2c/3,2c/3)^T\). Since \(T_1v=(1/2,1/2)^T\), the consecutive-ones shifts have exactly \(\tfrac12(2/3)^{m-1}\) correlation. Their positive values converge to zero, proving the last assertion.

## Verification
The standalone Python 3 standard-library checker at `artifacts/verify.py` performs 20,472 exact assertions using rational arithmetic and integral binomial coefficients. It checks the earlier congruence in four parameter cases through index 71, all positive shift correlations below \(3^8\) and their complete upper-tier classification, invariance under multiplying shifts by three, finite block character sums for two block lengths and 120 shifts, and the exact consecutive-ones formula through 24 digits. Its finite tests are corroboration of the all-shift proof, not replacements for it. Execute `python3 artifacts/verify.py` from the package root.

## Relationship to prior work
The mod-nine digit characterization is **explicitly known** from Krattenthaler–Müller [1, Corollary 25] and, for classical Apéry numbers, from the earlier result of Gessel [3] as described by Rowland–Yassawi [2, Theorem 3.32]. That characterization is not claimed as new. The present statement adds natural shift-correlation limits, a concrete two-state rational carry formula, quantitative cutoff control, strict positivity, and the sharp first and second correlation levels with complete equality cases. The primary texts [1] and [2] were inspected in their Apéry-mod-nine sections; they describe residues and automata, rather than these pair-correlation extremizers. Related published findings on dyadic/quinquenary character shift correlations or Pascal-row overlap concern different digit weights and bases. They demonstrate the general applicability of carry methods but do not imply this exact ternary sixth-root specialization or its two-tier digit-rigidity classification.

## Limitations
This is a derived arithmetic theorem, not a new congruence for Apéry numbers. Its connection to the entire parameter family is inherited from [1]. An equivalent older result might appear in the general theory of \(q\)-multiplicative sequences or substitution autocorrelations, possibly without mentioning Apéry numbers; searches and comparison do not eliminate this risk. The asymptotic constant in the cutoff bound is not optimized, and no assertion is made about independent validation. The proof uses the fixed-shift, positive-integer setting only.

## References
[1] C. Krattenthaler and T. W. Müller, *Generalised Apéry numbers modulo 9*, arXiv:1401.1444v1, first public 2014-01-07, particularly Corollary 25, https://arxiv.org/abs/1401.1444.

[2] E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, first public 2013-10-31, particularly Section 3.6 and Theorem 3.32, https://arxiv.org/abs/1310.8635.

[3] I. M. Gessel, *Some congruences for Apéry numbers*, Journal of Number Theory 14 (1982), 362–368, Theorem 3(iii), as cited in [1] and [2].
