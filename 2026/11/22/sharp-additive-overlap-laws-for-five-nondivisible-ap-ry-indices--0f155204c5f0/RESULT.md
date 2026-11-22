# Sharp additive overlap laws for five-nondivisible Apéry indices

## Finding

Define the classical Apéry numbers by
\[
A(n)=\sum_{j=0}^{n}\binom{n}{j}^{2}\binom{n+j}{j}^{2}\qquad(n\geq0).
\]
For each integer \(r\geq1\) and fixed integer \(h\geq0\), put
\[
Q_r(h)=\#\{0\leq n<5^r:5\nmid A(n),\ 5\nmid A(n+h)\}.
\]
For \(h>0\), let \(h=\sum_{j=0}^{L-1}d_j5^j\), with \(d_{L-1}\ne0\), be its ordinary base-five expansion (least significant digit first). Starting with \(c_0=0\), set
\[
c_{j+1}\equiv c_j+d_j\pmod2,\quad c_{j+1}\in\{0,1\},\qquad
w(d,c)=\begin{array}{c|ccccc}d&0&1&2&3&4\\\hline c=0&3&1&2&2&1\\c=1&1&2&2&1&3\end{array}.
\]
Then, **at every depth \(r\geq L\)**, the exact two-point count is
\[
\boxed{Q_r(h)=\begin{cases}
3^{r-L}\displaystyle\prod_{j=0}^{L-1}w(d_j,c_j),&h\text{ even},\\
0,&h\text{ odd}.
\end{cases}}
\]
The normalized relative overlap \(\rho(h)=\lim_{r\to\infty}Q_r(h)/3^r\) therefore exists. It satisfies \(\rho(0)=1\), \(\rho(h)=0\) for odd \(h\), and for even positive \(h\) is the positive rational product \(3^{-L}\prod_j w(d_j,c_j)\). In particular, every positive even shift gives infinitely many pairs of Apéry indices simultaneously prime to five; no odd shift gives a pair.

The **sharp first two positive-shift overlap levels** are
\[
\boxed{\max_{h\geq1}\rho(h)=\frac23,\quad
\rho(h)=\frac23\iff h=2\cdot5^i\ (i\geq0),}
\]
and, for every other positive shift, \(\rho(h)\leq4/9\). Equality \(\rho(h)=4/9\) occurs **exactly** in these two families, with integers \(0\leq i<j\):
\[
\boxed{h=2(5^i+5^j)}
\qquad\text{or}\qquad
\boxed{h=3\cdot5^i+4\sum_{t=i+1}^{j-1}5^t+5^j.}
\]
An empty sum is zero. The isolated top-level and runner-up families are an extremal classification, not an assertion about ordinary natural densities: the five-nondivisible Apéry indices themselves have density zero.

## Assumptions and scope

All indices and shifts are nonnegative integers. Divisibility is ordinary integer divisibility, not a statement about higher five-adic valuations. The counting interval is \(0\leq n<5^r\); \(n+h\) is not reduced modulo \(5^r\). The formulas concern every fixed shift, and the depth condition \(r\geq L\) is necessary for the given exact finite-level expression. The prime and the Apéry sequence are fixed as defined; no assertion is made for other primes or other Apéry-like sequences. The previously known Lucas congruence is an explicit premise rather than a new contribution.

## Proof

**Digit reduction.** Gessel's Lucas congruence for the Apéry numbers, as reproduced and discussed by Adamczewski–Bell and Malik–Straub, says that for any prime \(p\), if \(n=\sum_j n_jp^j\) then \(A(n)\equiv\prod_j A(n_j)\pmod p\). The five initial entries are
\[
(A(0),A(1),A(2),A(3),A(4))=(1,5,73,1445,33001).
\]
Thus \(5\nmid A(n)\) if and only if every base-five digit of \(n\) lies in \(E=\{0,2,4\}\). Consequently the number of such \(n\) in \([0,5^r)\) is exactly \(3^r\). Every such \(n\) is even, since the base is odd and all its digits are even.

**Carry factorization.** In adding \(h\) to an allowed \(n\), let \(x_j\in E\) be the \(j\)-th digit of \(n\), and \(c_j\in\{0,1\}\) the incoming carry. The output digit is \(x_j+d_j+c_j-5c_{j+1}\). Requiring it to be in \(E\) forces \(c_{j+1}\equiv d_j+c_j\pmod2\), independently of \(x_j\); this follows because both \(x_j\) and the output are even and five is odd. Direct enumeration of the three possible input digits gives exactly the ten entries in the displayed \(w\)-table, as well as the stated deterministic carry transition. Therefore the number of allowable low-digit choices through position \(L-1\) is \(\prod_{j<L}w(d_j,c_j)\).

The last carry \(c_L\) is congruent to \(\sum_{j<L}d_j\equiv h\pmod2\). If \(h\) is even it vanishes, and every higher input digit, through position \(r-1\), is freely chosen from \(E\). This gives the factor \(3^{r-L}\). If \(h\) is odd, both admissible integers would have to be even, which is impossible; equivalently, a positive carry after the last shift digit can only propagate through input digit four, and ultimately produces a forbidden leading digit one. This proves the exact formula at every depth \(r\geq L\), and all claims of existence and positivity.

**Extremal classification.** Normalize each digit weight by three. From the table, the only factor equal to one is the neutral transition \((c,d)=(0,0)\) or \((1,4)\); every other factor is \(2/3\) or \(1/3\). A nonzero shift must contain a nonneutral transition. A single \(2/3\) factor with all others neutral and final carry zero is possible only when one digit equals two and all remaining digits equal zero. This gives exactly \(h=2\cdot5^i\) and the sharp maximum \(2/3\).

For any other nonzero shift, either a \(1/3\) factor occurs (so the product is at most \(1/3<4/9\)), or at least two \(2/3\) factors occur (so it is at most \(4/9\)). Equality at \(4/9\) requires exactly two \(2/3\) factors and neutral factors everywhere else. From the carry-zero state, the only weight-two transitions are digit two, which retains carry zero, and digit three, which changes the carry to one. From carry one, the only weight-two transition that changes back to carry zero is digit one; the only neutral transition while retaining carry one is digit four. Consequently the two and only two equality patterns are: two digits equal to two with all others zero, or one digit three followed by any string of digit fours and then a digit one, with all outside digits zero. Translating these least-significant-digit-first patterns gives the two displayed families. All other products are smaller. \(\square\)

## Verification

The standalone `verify.py` checks the carry weights by independent enumeration, independently generates the first 301 Apéry numbers by their integer three-term recurrence, compares their divisibility by five with the digit criterion, evaluates the exact finite-shift counts for all tested shifts through \(5^5\), and exhaustively compares the two extremal families with all shifts below \(5^7\). Run with `python3 verify.py` using only the Python standard library. The checker is a finite consistency test; the preceding digit and carry argument is the proof for all indices, depths and shifts.

## Relationship to prior work

The Apéry Lucas congruence and its digit-automaton consequences are classical: Adamczewski–Bell explicitly exhibit the complete modulo-five automaton and forbidden digits one and three. Malik–Straub study Lucas congruences, periodicity and which primes divide sequence terms. Kumar–Rani–Chugh describe the same three-digit subset \(\{0,2,4\}\) as a five-adic Cantor set and study self-similarity/fractal strings. These statements establish the one-point digital support but do not state the exact **two-index fixed-shift counts**, the sharp positive-shift overlap level, or the runner-up equality families. The present result is a new evaluation of a natural two-point invariant arising from that established support; it is not presented as a new Lucas theorem or Cantor-set construction. A general automatic-sequence treatment could conceivably subsume this evaluation; no directly implying classification was located in the searches described in `AUDIT.json`.

## Limitations

The relative normalization by \(3^r\) is essential: normalized by all \(5^r\) indices, every fixed-shift pair count has limiting density zero. The overlap is one-sided in the finite interval, and the assertion does not address multi-shift patterns, full residue pairs, higher powers of five, or a complete historical priority classification. The proof is elementary once the existing Lucas congruence is granted. A related older paper on Apéry arithmetic was accessible only at abstract level, so earlier unlocated treatments of additive overlaps remain a priority risk. No independent mathematical audit has been performed.

## References

1. B. Adamczewski and J. P. Bell, *Diagonalization and Rationalization of algebraic Laurent series*, arXiv:1205.4090 (first posted 2012-05-18), §9 and Figure 1, https://arxiv.org/abs/1205.4090 ; journal PDF https://smf.emath.fr/system/files/2017-08/ens_ann-sc_46_963-1004.pdf .
2. A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297 (first posted 2015-08-03), §§1, 5–6, https://arxiv.org/abs/1508.00297 ; readable version https://ar5iv.labs.arxiv.org/html/1508.00297 .
3. A. Kumar, M. Rani and R. Chugh, *New 5-adic Cantor sets and fractal string*, SpringerPlus 2, article 654 (2013-12-05), Theorems 3.1–3.2, https://doi.org/10.1186/2193-1801-2-654 .
4. I. Gessel, *Some congruences for Apéry numbers*, Journal of Number Theory 14 (1982), 362–368, https://doi.org/10.1016/0022-314X(82)90071-3 .
5. F. Luca and I. E. Shparlinski, *Arithmetic properties of Apéry numbers*, Journal of the London Mathematical Society 78 (2008), 545–562, https://doi.org/10.1112/jlms/jdn031 .
