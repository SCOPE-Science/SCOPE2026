# A parity-sparsity transition for hyper-ary partitions

## Finding
For each integer \(b\ge 2\), let \(h_b(n)\) be the number of partitions of a nonnegative integer \(n\) into powers of \(b\), with each power used at most \(b\) times. Write
\[
H_b(k)=\#\{0\le n<b^k:h_b(n)\equiv1\pmod2\},\qquad k\ge0.
\]
Then the exact level-count generating function is
\[
\boxed{\sum_{k\ge0}H_b(k)z^k=\frac{1-2z^2}{(1-z)(1-(b-1)z-2z^2)}.}
\]
In particular, \(H_b(0)=1\), \(H_b(1)=b\), and
\[
\boxed{H_b(k+1)=(b-1)H_b(k)+2H_b(k-1)-1\quad(k\ge1).}
\]
Define
\[
\lambda_b=\frac{b-1+\sqrt{(b-1)^2+8}}2,\qquad
\mu_b=\frac{b-1-\sqrt{(b-1)^2+8}}2,
\quad A_b=\frac{(b-1)(b+1-\mu_b)}{b(\lambda_b-\mu_b)}.
\]
For all \(b\ge2\), the exact level counts satisfy
\[
H_b(k)=\frac1b+A_b\lambda_b^k+\left(\frac{b-1}{b}-A_b\right)\mu_b^k,
\]
so \(H_b(k)=A_b\lambda_b^k+O_b(1)\) with \(A_b>0\). In the binary case, the odd values have natural density \(2/3\). In every fixed base \(b\ge3\), their natural density is \(0\), but they obey the sharp sparsity law
\[
\boxed{\#\{0\le n<X:h_b(n)\text{ odd}\}=\Theta_b(X^{\alpha_b}),
\quad\alpha_b=\log_b\lambda_b\in(0,1).}
\]
Thus a sharp positive-density/zero-density transition occurs between base two and every higher base; in particular the count growth exponent is exactly determined for each base.

## Assumptions and scope
The base \(b\) is any fixed integer at least two, the index \(n\) is any nonnegative integer, and \(k\) is a nonnegative integer. No primality or squarefreeness assumptions occur. \(h_b(0)=1\) counts the empty partition. A natural density is the limit of the fraction of indices below \(X\) with odd partition count, as real \(X\to\infty\). A \(\Theta_b\) assertion allows positive constants depending on the fixed base, not on \(X\). The result does not determine the distribution modulo any integer larger than two.

## Proof
The restricted-partition generating product gives the standard recurrences for \(n\ge1\):
\[
h_b(bn)=h_b(n)+h_b(n-1),\qquad h_b(bn+r)=h_b(n)\quad(1\le r<b),
\]
with the convention \(h_b(-1)=0\). Introduce \(s_b(0)=0\), \(s_b(n)=h_b(n-1)\) for \(n\ge1\). The resulting identities, valid for \(n\ge0\), are
\[
\begin{aligned}
s_b(bn)&=s_b(n),\\
s_b(bn+1)&=s_b(n)+s_b(n+1),\\
s_b(bn+r)&=s_b(n+1)\quad(2\le r<b).
\end{aligned}
\]
All subsequent pairs are reduced modulo two. At the index \(n\), record the parity state \((s_b(n),s_b(n+1))\). Appending a least-significant base-\(b\) digit \(r\) maps a pair \((u,v)\) to
\[
T_0(u,v)=(u,u+v),\quad
T_1(u,v)=(u+v,v),\quad
T_r(u,v)=(v,v)\ (2\le r<b),
\]
with additions in \(\mathbb F_2\). The last equality covers \(r=b-1\) because \(s_b(bn+b)=s_b(n+1)\). The initial state at \(n=0\) is \((0,1)\). The state \((0,0)\) is absorbing and makes no odd contribution. With columns ordered \((0,1),(1,0),(1,1)\), the numbers \((x_k,y_k,z_k)\) of indices \(0\le n<b^k\) in the three nonzero states therefore evolve as
\[
(x_{k+1},y_{k+1},z_{k+1})
=(x_k,y_k,z_k)
\begin{pmatrix}1&0&b-1\\0&1&1\\1&1&b-2\end{pmatrix},
\qquad(x_0,y_0,z_0)=(1,0,0).
\]
The difference \(x_k-y_k\) stays equal to one. Because \(s_b(0)=0\), \(s_b(b^k)=s_b(1)=1\), and \(h_b(n)=s_b(n+1)\), the requested count is \(H_b(k)=1+y_k+z_k=x_k+z_k\). The matrix yields \(x_{k+1}=x_k+z_k=H_b(k)\) and
\[
H_b(k+1)=(b-1)H_b(k)+2x_k-1
=(b-1)H_b(k)+2H_b(k-1)-1\quad(k\ge1).
\]
Starting from \(H_b(0)=1\) and \(H_b(1)=b\) proves the recurrence. Multiplying \(\sum H_b(k)z^k\) by its recurrence denominator gives the stated generating function, with initial numerator \(1-2z^2\).

The homogeneous characteristic equation is \(t^2-(b-1)t-2=0\), whose roots are \(\lambda_b>0\) and \(\mu_b<0\). The constant particular solution is \(1/b\). Solving from the two initial conditions gives the displayed exact closed formula. Since \(b\ge2\), \(\lambda_b\ge2\), \(|\mu_b|=2/\lambda_b\le1\), and \(A_b>0\), we obtain \(H_b(k)=A_b\lambda_b^k+O_b(1)\).

For \(b=2\), \(\lambda_2=2\), \(A_2=2/3\). For any integer \(X\), the initial segment below \(X\) is bracketed between two successive powers of two, and the known exact binary parity relation \(h_2(n)\equiv0\pmod2\iff n\equiv2\pmod3\) gives its natural density \(2/3\). For \(b>2\), the inequality \(\lambda_b<b\) is equivalent to \(8<4b\). If \(b^k\le X<b^{k+1}\), monotonicity of counting and the exact level asymptotic bound the count between positive multiples of \(\lambda_b^k\) and \(\lambda_b^{k+1}\). Consequently it is \(\Theta_b(X^{\log_b\lambda_b})\) for every real \(X\ge2\), and its ratio to \(X\) tends to zero. This completes the proof.

## Verification
The standalone script `verify_hyper_odd.py` independently enumerates the restricted-partition counts using exact integer recurrences, checks the three-state parity automaton and closed recurrence for all bases from two through eleven at every complete level not exceeding 175,000 indices, checks the rational generating-function identity at 22 coefficients for bases two through nineteen, and checks the binary congruence on 65,536 indices. It uses no floating-point arithmetic or external packages. The reported execution was `VERIFY_OK`; this bounded test is corroboration rather than the proof of the infinite statements.

## Relationship to prior work
Courtright and Sellers (2004) established the hyper-ary partition recurrences and fixed-arithmetic-progression congruences; for base two they proved the exact mod-two periodicity used above. Defant (2015, arXiv:1506.07824) studied maximal values of the generalized Stern sequence; maximal order of individual counts differs from the number of indices having odd counts. Flowers and Lockard (2016) developed an \(m\)-ary tree and subsequence relation. Eom, Jeong and Sohn (2016) studied pointwise evaluation using recurrences, matrices and trees; the full text was not accessible during comparison. Edgar (2018) provides a general digit-wise product formula for each individual partition count. That pointwise formula is broader data at the single-index level and could furnish an alternate derivation, but its inspected main theorem and related corollaries do not state the global all-base level-count generating function, sharp asymptotic sparsity exponent, or positive/zero density transition. Thus the asserted contribution is **only** the quantitative aggregate parity distribution and its sharp exponent, not the underlying recurrences, binary parity, or pointwise evaluation method. Unindexed or inaccessible covering statements remain a priority risk.

## Limitations
No statement is made about residues modulo odd primes or higher powers of two, nor about a local fluctuation formula for every real \(X\). A pointwise digit formula in prior work can compute each value of \(h_b(n)\), and further bibliography could contain an unstated direct aggregate-parity corollary; the historical-priority assessment is qualified accordingly. The proof concerns a fixed base as the cutoff tends to infinity and does not claim uniform asymptotics in the base. Independently validated mathematical certification has not been performed.

## References
- K. M. Courtright and J. A. Sellers, *Arithmetic Properties for Hyper m-Ary Partition Functions*, Integers **4** (2004), A06, published 23 April 2004. https://math.colgate.edu/~integers/e6/e6.pdf
- C. Defant, *Upper Bounds for Stern's Diatomic Sequence and Related Sequences*, arXiv:1506.07824, first posted 25 June 2015; Electron. J. Combin. **23** (2016), P4.8. https://arxiv.org/abs/1506.07824
- T. B. Flowers and S. R. Lockard, *Identifying an m-Ary Partition Identity through an m-Ary Tree*, Integers **16** (2016), A10. https://files01.core.ac.uk/download/pdf/48838118.pdf
- J. Eom, G. Jeong and J. Sohn, *Three Different Ways to Obtain the Values of Hyper m-Ary Partition Functions*, Bull. Korean Math. Soc. **53** (2016), 1857–1868. https://doi.org/10.4134/BKMS.b151039
- T. Edgar, *On the Number of Hyper m-Ary Partitions*, Integers **18** (2018), A47. https://math.colgate.edu/~integers/s47/s47.pdf
