# Sharp signed shift correlations in central Delannoy numbers modulo seven

## Finding
Let the central Delannoy numbers and their quadratic-character signs be
\[
D_n=\sum_{j=0}^{n}2^j\binom{n}{j}^{2},\qquad
f(n)=\left(\frac{D_n}{7}\right)\in\{-1,0,1\},\qquad n\ge0,
\]
where the Legendre symbol is zero exactly on multiples of seven. Given an integer shift \(h\ge1\), write its base-seven expansion as \(h=\sum_{i=0}^{k-1}d_i7^i\) with \(d_{k-1}\ne0\), and define the following integer matrices (rows indicate incoming addition carry and columns outgoing carry):
\[
\begin{aligned}
T_0&=\begin{pmatrix}6&0\\0&1\end{pmatrix},&
T_1&=\begin{pmatrix}0&1\\-1&-2\end{pmatrix},&
T_2&=\begin{pmatrix}-1&-2\\2&-1\end{pmatrix},\\[3pt]
T_3&=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},&
T_4&=\begin{pmatrix}-1&2\\-2&-1\end{pmatrix},&
T_5&=\begin{pmatrix}-2&-1\\1&0\end{pmatrix},\\[3pt]
T_6&=\begin{pmatrix}1&0\\0&6\end{pmatrix}.
\end{aligned}
\]
Define integers \((a_h,b_h)=(1,0)T_{d_0}\cdots T_{d_{k-1}}\). Then for **every** integer \(r\ge k\) the signed two-point sum has the exact finite-block formula
\[
\boxed{\sum_{0\le n<7^r}f(n)f(n+h)=a_h6^{r-k}-b_h.}
\]
The natural nonzero-index population within \([0,7^r)\) is exactly \(6^r\). Consequently the normalized signed correlation exists for every fixed \(h\ge1\):
\[
\boxed{C(h)=\lim_{r\to\infty}6^{-r}\sum_{0\le n<7^r}f(n)f(n+h)=\frac{a_h}{6^k}.}
\]
The full family has the sharp universal interval
\[
\boxed{-\frac13\le C(h)\le\frac13,\qquad h\ge1.}
\]
Both endpoints are attained, and their entire equality classes are
\[
\boxed{C(h)=\frac13\iff h=3\cdot7^j,\qquad
C(h)=-\frac13\iff h=5\cdot7^j,\qquad j\ge0.}
\]
The zero shift is excluded from the sharp inequality; it has \(C(0)=1\).

## Assumptions and scope
All indices and shifts are nonnegative integers, and \(h\) is a fixed positive integer before taking \(r\to\infty\). The sums are not cyclic; \(n+h\) is evaluated at its ordinary nonnegative integer value even if it exceeds \(7^r-1\). No asymptotic is claimed for shifts varying with \(r\). The character normalization is by \(6^r\), not by \(7^r\), since the indices with \(f(n)\ne0\) have density zero in the natural numbers.

## Proof
**Digit signs.** The Lucas congruence for central Delannoy numbers, proved in the classical literature, says that for any base-seven expansion \(n=\sum n_i7^i\),
\[
D_n\equiv\prod_iD_{n_i}\pmod7.
\]
It also follows directly from the binomial formula and Lucas' theorem. The seven initial Delannoy numbers are
\[
(D_0,D_1,\ldots,D_6)=(1,3,13,63,321,1683,8989).
\]
The quadratic residues modulo seven are \(1,2,4\), so the digit-character vector is
\[
(w_0,\ldots,w_6)=(1,-1,-1,0,-1,-1,1),
\qquad f(n)=\prod_i w_{n_i}.
\]
Exactly six digits have nonzero weight, proving \(\sum_{0\le n<7^r}f(n)^2=6^r\).

**Two-carry transfer.** To add one digit \(d\in\{0,\ldots,6\}\) of \(h\) to a digit \(u\) of \(n\) with incoming carry \(c\in\{0,1\}\), the resulting digit is \(v=(u+d+c)\bmod7\), and the new carry is \(c'=\lfloor(u+d+c)/7\rfloor\). The weight of the pair of digits is \(w_uw_v\). Hence
\[
(T_d)_{c,c'}=\sum_{\substack{0\le u<7\\\lfloor(u+d+c)/7\rfloor=c'}}w_u w_{(u+d+c)\bmod7}.
\]
Evaluating these fourteen finite sums for every \(d\) yields exactly the displayed matrices. After all \(k\) digits of \(h\) have been processed, the row vector is \((a_h,b_h)\). Each extra zero digit of the shift multiplies this vector by \(T_0=\operatorname{diag}(6,1)\). At digit position \(r\), the remaining carry is either zero or one; the extra leading digit of \(n+h\) contributes \(w_0=1\) or \(w_1=-1\), respectively, while \(n\) has leading digit zero. Thus for every \(r\ge k\), the exact sum is \((a_h6^{r-k},b_h)\cdot(1,-1)^\mathsf T=a_h6^{r-k}-b_h\). Division by \(6^r\) proves the limit formula.

**Sharp norm and equality.** For a row vector \(v\) use \(\|v\|_\infty=\max(|v_0|,|v_1|)\). The operator norm for right multiplication by \(T_d\) is its maximum absolute column sum; the seven bounds in digit order are
\[
(6,3,3,3,3,3,6).
\]
Initial zero digits of \(h\) only multiply its starting row \((1,0)\) by powers of six. At its least significant nonzero digit, the normalized first rows for digits \(1,\ldots,6\) are
\[
(0,1),\ (-1,-2),\ (2,-1),\ (-1,2),\ (-2,-1),\ (1,0).
\]
Every row has norm at most two, and every later digit multiplies the norm by at most six. Therefore \(|a_h|\le2\cdot6^{k-1}\), where the initial zero digits, if any, contribute the same scaling on both sides. This proves \(|C(h)|\le1/3\).

Equality forces all more significant digits after the least significant nonzero digit to be zero: a later digit in \(\{1,2,3,4,5\}\) reduces the maximum attainable normalized norm strictly, and a later digit \(6\) can preserve that norm only in its carry-one coordinate while strictly reducing the carry-zero coordinate; subsequent zero or six digits cannot restore the carry-zero maximum, and any intervening digit in \(\{1,\ldots,5\}\) contracts the norm. With all later digits zero, the first carry-zero coordinate has absolute value two exactly for digits \(3\) and \(5\). Their signs are positive and negative, respectively. Trailing zero digits of \(h\) do not affect the normalized value. This gives exactly the two asserted equality families.

## Verification
The standalone file `verify_delannoy7.py` uses only the Python standard library. Run `python3 verify_delannoy7.py`. It independently reconstructs the seven transfer matrices from digit-weight sums, compares the digit signs with direct binomial coefficients for the first 100 indices, tests the exact noncyclic finite-block identity over numerous shifts and levels, and checks the sharp extremizers for all positive shifts below \(7^5\). Its expected report is `PASS: 17262 exact finite assertions`. These finite tests check arithmetic and implementation; the unrestricted statements follow from the displayed carry identity and norm argument.

## Relationship to prior work
Deutsch and Sagan's Lucas congruence for generalized Apéry numbers, specialized to central Delannoy numbers, supplies the acknowledged digit-factorization step. Pan's later \(q\)-Delannoy work cites the classical two-variable Lucas property and proves a \(q\)-analogue. Rowland and Yassawi give general algorithms for residue automata of combinatorial sequences. These results explain why a digit approach is natural but do not themselves state the evaluated signed, normalized, all-shift seven-adic correlation or the exact positive and negative equality families. OEIS A001850 records the underlying numbers, not the theorem's all-shift correlation function.

## Limitations
The theorem concerns the quadratic character of the ordinary central Delannoy numbers modulo exactly seven, not other primes, prime powers, or higher-order correlations. It addresses fixed positive shifts and aligned base-seven index blocks, not arbitrary moving windows. General theories of automatic-sequence correlations may offer alternate deductions; comprehensive historical priority has not been independently established.

## References
1. Emeric Deutsch and Bruce E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326v1 (public 2004-07-19); *Journal of Number Theory* 117 (2006), 191–215, Theorem 5.9. https://arxiv.org/abs/math/0407326
2. Hao Pan, *A Lucas-type congruence for q-Delannoy numbers*, arXiv:1508.02046v1 (2015-08-09), Introduction and Theorem 1.1. https://arxiv.org/abs/1508.02046
3. Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635v1 (2013-10-31), *J. Théor. Nombres Bordeaux* 27 (2015), 245–288. https://arxiv.org/abs/1310.8635
4. OEIS Foundation, A001850, *Central Delannoy numbers*. https://oeis.org/A001850
