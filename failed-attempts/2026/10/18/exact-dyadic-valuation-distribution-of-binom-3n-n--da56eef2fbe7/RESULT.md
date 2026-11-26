# Exact dyadic valuation distribution of \(\binom{3n}{n}\)

## Finding
For all integers \(k\ge0\), define
\[P_k(z)=\sum_{n=0}^{2^k-1} z^{\nu_2(\binom{3n}{n})},\quad \nu_2(\binom00)=0.\]
The complete distribution of the valuation of this classical binomial subsequence over the first \(2^k\) indices is encoded by
\[\boxed{\sum_{k\ge0}P_k(z)x^k=\frac{(1+x)(1-zx)}{1-(1+z)x-(1-z+z^2)x^2+z(1+z)x^3}.}\]
This is an identity in formal power series in \(x\) with coefficients in \(\mathbb Z[z]\). In particular, every exact valuation fiber for every dyadic cutoff is computable by coefficient extraction from the same rational function.

Writing \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the following exact identities hold for all \(k\ge0\):
\[[z^0]P_k(z)=F_{k+2},\qquad [z^1]P_k(z)=0.\]
Thus \(\binom{3n}{n}\) is always odd or divisible by four. In addition,
\[\sum_{k\ge0}[z^2]P_k(z)x^k=\frac{x^2(1-x^2)}{(1-x-x^2)^2},\qquad
\sum_{k\ge0}[z^3]P_k(z)x^k=\frac{x^3(1-x^2)}{(1-x-x^2)^2}.\]
The equality of the last two generating functions after a factor of \(x\) gives a nontrivial relation between adjacent finite-length valuation strata, although the numerical second stratum itself occurs in existing sequence databases.

For \(V_k\) defined by sampling \(n\) uniformly from \(\{0,1,\ldots,2^k-1\}\), the mean is **exactly**
\[\mathbb E[V_k]=\frac{k}{2}-\frac23+\frac{3+(-1)^k}{6\cdot2^k}.\]
The second factorial moment is **exactly**
\[\mathbb E[V_k(V_k-1)]=\frac{9k^2-9k-16}{36}+\frac{(3k-1)(-1)^k/18+(k+1)/2}{2^k}.\]
In particular, \(\operatorname{Var}(V_k)=11k/12-14/9+O(k2^{-k})\) as \(k\to\infty\); this provides finite-length corrections to the already-known leading covariance law.

## Assumptions and scope
All counting indices are nonnegative integers, every length \(k\) is an integer at least zero, and the prime is exactly two. The binomial coefficient \(\binom{0}{0}\) equals one. The valuation \(\nu_2(m)\) means the exponent of two in a positive integer \(m\). The dyadic cutoff is strict: \(0\le n<2^k\). No assertions for arbitrary non-dyadic upper limits or for other primes are included.

## Proof
By Kummer's carry theorem, \(\nu_2(\binom{3n}{n})\) is the number of carries when adding \(n\) and \(2n\) in base two. Pad \(n\) to exactly \(k\) low-order binary positions and write \(n=\sum_{i=0}^{k-1}d_i2^i\), where \(d_i\in\{0,1\}\). Put \(d_{-1}=c_{-1}=0\). For \(0\le i<k\), the carry out of position \(i\) is
\[c_i=\left\lfloor\frac{d_i+d_{i-1}+c_{i-1}}2\right\rfloor.\]
After these \(k\) digits, position \(k\) can contribute one final carry
\[c_k=\left\lfloor\frac{d_{k-1}+c_{k-1}}2\right\rfloor,\]
and all later carries vanish. Consequently
\[\nu_2\!\left(\binom{3n}{n}\right)=\sum_{i=0}^k c_i.\]

Track the state \((d_{i-1},c_{i-1})\) in the order \((0,0),(0,1),(1,0),(1,1)\). For each choice of the next digit, weight the transition by \(z^{c_i}\). The exact weighted transition matrix, initial row, and terminal column are
\[T(z)=\begin{pmatrix}1&0&1&0\\1&0&0&z\\1&0&0&z\\0&z&0&z\end{pmatrix},\quad e=(1,0,0,0),\quad b(z)=(1,1,1,z)^{\mathsf T}.\]
Every padded word of length \(k\) occurs exactly once; by construction its total weight counts all carries including the terminal carry. Therefore
\[P_k(z)=eT(z)^k b(z).\]
Using the formal geometric matrix series gives
\[\sum_{k\ge0}P_k(z)x^k=e(I-xT(z))^{-1}b(z).\]
Direct rational elimination of the four linear equations for the components of \((I-xT(z))^{-1}b(z)\) yields the boxed rational function. This is an identity of formal series, so no convergence hypothesis is required.

Setting \(z=0\) gives \((1+x)/(1-x-x^2)\), whose \(x^k\) coefficient is \(F_{k+2}\). Differentiating at \(z=0\) gives identically zero, proving the excluded single-valuation layer. The second and third displayed fiber functions follow by coefficient extraction to degrees two and three in \(z\). All these manipulations occur in rational functions with denominator of constant term one.

At \(z=1\), \(P_k(1)=2^k\). Differentiation in \(z\) followed by specialization to \(z=1\) gives the ordinary generating functions for the first moment numerator and the second factorial moment numerator:
\[\sum_{k\ge0}P'_k(1)x^k=\frac{x^2(x-2)}{(x-1)(x+1)(2x-1)^2},\]
\[\sum_{k\ge0}P''_k(1)x^k=-\frac{2x^2(x^4-4x^3+2x^2-x+1)}{(x-1)^2(x+1)^2(2x-1)^3}.\]
Taking partial fractions, extracting \(x^k\) coefficients and dividing by \(2^k\) gives the exact formulas above. Finally, \(\operatorname{Var}(V_k)=\mathbb E[V_k(V_k-1)]+\mathbb E[V_k]-(\mathbb E[V_k])^2\); expanding the explicit expressions proves the stated asymptotic with error \(O(k2^{-k})\).

## Verification
The accompanying standalone `verify.py` computes the weighted carry-state distribution by integer dynamic programming for all \(0\le k\le30\), cross-checks complete histograms against Legendre's independent factorial-valuation formula for all \(0\le k\le12\), checks the polynomial recurrence induced by the rational denominator, and checks the two exact moment formulas. For small indices it also computes the binomial integer directly. The execution output was:

`BINOMIAL_3N_N_VALUATION_EXACT_OK dyadic_lengths=0..30 direct_inputs= 8191 rational_recurrences=28 moments=31`

The infinite result is established by the carry-state argument and rational-matrix identity, not by finite testing. Execute `python3 verify.py` with a standard Python 3 installation.

## Relationship to prior work
Kummer's theorem already equates binomial valuations with binary carries. The observation that \(\binom{3n}{n}\) is odd exactly when the binary digits of \(n\) have no adjacent ones is recorded in OEIS A003714 (comment dated 2003-03-08); hence the Fibonacci zero layer is not new. OEIS A036556 (2004-06-06 comment) also records the parity of these valuations. The numerical sequence corresponding to the two-valuation layer, after the relevant index shift, is OEIS A029907, with an already-published univariate generating function. Its values or univariate rational generating function are not claimed independently as new.

Rowland's arXiv:1001.1783 counts, for a **fixed** upper Pascal-row index, the binomial entries that are nonzero modulo a given prime power. It does not directly supply this diagonal **all-valuation** dyadic distribution. Finch–Sebah–Bai's arXiv:0802.2654 studies odd coefficients in Pascal-type multinomial triangles, not these valuation fibers. Drmota–Krattenthaler's arXiv:1803.02178 establishes general digit-sum central limit theorems and a covariance formula; applied to \(2s_2(n)-s_2(3n)\), it already implies the leading mean, leading variance coefficient \(11/12\), and normal limit. The contribution asserted here is the specific **exact rational two-variable distribution** and its complete finite-cutoff corrections, not a new central limit theorem.

## Limitations
The characterization is restricted to the particular binomial diagonal and dyadic index cutoffs. The formula does not determine the distribution for arbitrary cutoffs without further work. Existing general finite-state constructions might contain an implicit equivalent expression; the searches and inspections described in the review do not constitute proof of absolute novelty. Existing database entries cover the zero layer and numerical two-valuation layer. The first nonzero layer and the leading Gaussian variance are specifically identified as earlier knowledge where applicable; they should not be presented as separate independent discoveries.

## References
- Kummer, E. (1852), carry criterion for prime divisibility of binomial coefficients; cited in Rowland, arXiv:1001.1783.
- OEIS A003714, Fibbinary numbers; 2003-03-08 comment identifying the parity of \(\binom{3n}{n}\). https://oeis.org/A003714
- OEIS A036556, 2004-06-06 comment on valuation parity. https://oeis.org/A036556
- OEIS A029907, known sequence and univariate generating function. https://oeis.org/A029907
- Eric Rowland, *The number of nonzero binomial coefficients modulo prime powers*, arXiv:1001.1783v3 (first submitted 2010-01-12). https://arxiv.org/abs/1001.1783
- S. R. Finch, P. Sebah, Z.-Q. Bai, *Odd Entries in Pascal's Trinomial Triangle*, arXiv:0802.2654v1 (2008-02-19). https://arxiv.org/abs/0802.2654
- M. Drmota and C. Krattenthaler, *A Joint Central Limit Theorem for the Sum-of-Digits Function, and Asymptotic Divisibility of Catalan-like Sequences*, arXiv:1803.02178v2 (first submitted 2018-03-06). https://arxiv.org/abs/1803.02178
