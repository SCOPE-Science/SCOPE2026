# Sharp shift correlations for the odd-entry counts in binary Pascal rows

## Finding

Let \(F(n)=\#\{0\le j\le n:\binom nj\text{ is odd}\}=2^{s_2(n)}\), where \(s_2(n)\) is the number of ones in the base-two expansion of \(n\). For each integer \(L\ge1\), form the cyclic data \(F(n)\), \(0\le n<2^L\), and write \(\rho_L(h)\) for the ordinary Pearson correlation of \(F(n)\) with \(F((n+h)\bmod 2^L)\), for \(0\le h<2^L\). For every fixed nonnegative integer \(h\), \(\rho(h)=\lim_{L\to\infty}\rho_L(h)\) exists and is rational. The value at zero is \(\rho(0)=1\). For \(h>0\), let \(d_0,\ldots,d_{\ell-1}\in\{0,1\}\) be its standard binary digits **from least significant to most significant**, with \(d_{\ell-1}=1\). Set

\[
T_0=\begin{pmatrix}5&0\\2&2\end{pmatrix},\qquad
T_1=\begin{pmatrix}2&2\\0&5\end{pmatrix},\qquad
v=\begin{pmatrix}1\\2/3\end{pmatrix},\qquad e=(1,0).
\]

Then the exact all-shift formula is

\[
\boxed{\rho(h)=5^{-\ell}eT_{d_0}T_{d_1}\cdots T_{d_{\ell-1}}v.}
\]

For **every positive integer** \(h\),

\[
\boxed{0<\rho(h)\le\frac23,\qquad \rho(h)=\frac23\iff h\text{ is a power of }2.}
\]

The lower endpoint is sharp but never attained: define \(h_m=(4^m-1)/3\) for \(m\ge0\), and \(r_m=\rho(h_m)\). Thus \(r_0=1\), \(r_1=2/3\), and for every \(m\ge2\),

\[
\boxed{r_m=\frac{24}{25}r_{m-1}-\frac4{25}r_{m-2}.}
\]

More explicitly, with \(\lambda_\pm=(12\pm2\sqrt{11})/25\),

\[
r_m=\left(\frac12+\frac{7}{6\sqrt{11}}\right)\lambda_+^m
+\left(\frac12-\frac{7}{6\sqrt{11}}\right)\lambda_-^m\longrightarrow0.
\]

Therefore \(\sup_{h\ge1}\rho(h)=2/3\) with exactly the power-of-two equality cases, while \(\inf_{h\ge1}\rho(h)=0\) without equality.

## Assumptions and scope

All shifts \(h\) are fixed nonnegative integers while \(L\) tends to infinity. For finite \(L\), only \(0\le h<2^L\) is considered; the index shift is **cyclic** modulo \(2^L\). Means and variances are taken with the uniform distribution on the \(2^L\) indices. The two cyclic arrays have equal nonzero variance for all \(L\ge1\). The subsequent sequence of shifts \(h_m\) is allowed to grow only *after* the fixed-shift correlation limits have been taken. The underlying identity for \(F(n)\) is classical, not asserted to be new.

## Proof

**1. Marginal moments and normalization.** Lucas's theorem, or its original binary specialization, gives \(F(n)=2^{s_2(n)}\), since every binary one in \(n\) gives two possible choices of the corresponding digit of \(j\) in a nonzero binomial coefficient. Independent summation over the \(L\) binary positions gives the exact identities

\[
\sum_{n<2^L}F(n)=3^L,\qquad \sum_{n<2^L}F(n)^2=5^L.
\]

Thus the common sample mean is \((3/2)^L\), and the common variance is \((5/2)^L-(3/2)^{2L}>0\).

**2. Exact carry transfer.** Put \(C_L(h)=\sum_{n<2^L}F(n)F((n+h)\bmod2^L)\). When adding a binary digit \(d\) of \(h\) to the current digit \(x\) of \(n\) and the incoming carry \(c\in\{0,1\}\), the output bit is \(y=(x+d+c)\bmod2\), the outgoing carry is \(c'=\lfloor(x+d+c)/2\rfloor\), and the weight contributed to the product is \(2^{x+y}\). Sum this weight over \(x=0,1\) for each incoming-outgoing carry pair \((c,c')\). For \(d=0\) this gives \(T_0\), and for \(d=1\) it gives \(T_1\), as displayed above. The initial carry is zero. In the cyclic addition, the carry leaving the most significant digit is discarded, so either final carry is admitted. Consequently, if \(h\) has \(\ell\) bits and \(L\ge\ell\),

\[
C_L(h)=eT_{d_0}\cdots T_{d_{\ell-1}}T_0^{L-\ell}\mathbf1,
\qquad \mathbf1=(1,1)^{\mathsf T}.
\]

This is an exact identity for all integers in the specified finite range, not an asymptotic estimate.

**3. Limit and Pearson coefficient.** Direct matrix multiplication yields

\[
5^{-k}T_0^k\mathbf1=\begin{pmatrix}1\\\frac23+\frac13(\frac25)^k\end{pmatrix}\longrightarrow v.
\]

Hence \(C_L(h)/5^L\to 5^{-\ell}eT_{d_0}\cdots T_{d_{\ell-1}}v\). Since cyclic shifting permutes the values, the finite Pearson coefficient is exactly

\[
\rho_L(h)=\frac{C_L(h)/5^L-(9/10)^L}{1-(9/10)^L}.
\]

Taking \(L\to\infty\) proves the claimed matrix formula and its rationality. For \(h=0\), the two data vectors coincide and \(\rho_L(0)=1\) identically.

**4. Sharp positive-lag maximum.** The two identities \(eT_0=5e\) and \(T_0v=5v\) show that adding any low-order zero digits, or appending a high-order zero digit in a transfer word, does not change its normalized value. In particular \(\rho(2^j h)=\rho(h)\) and \(\rho(1)=5^{-1}eT_1v=2/3\). Moreover,

\[
T_1v=\begin{pmatrix}10/3\\10/3\end{pmatrix}
\le\begin{pmatrix}5\\10/3\end{pmatrix}=5v,
\]

with strict inequality in the first coordinate. Every matrix \(T_d\) has nonnegative entries and a strictly positive \((0,0)\)-entry. Therefore applying an additional one-digit at the more significant end, in place of a zero-digit, strictly decreases the normalized first-row product: the intermediate nonnegative row has a strictly positive first component. Starting with the unique required leading one, the value is \(2/3\); each further one strictly decreases it, and zeros have no effect. Every matrix entry and initial first-row component contributing to the product is nonnegative, with a strictly positive first-coordinate path, so all values stay positive. Thus the complete upper bound and its exact equality classification follow.

**5. Sharp unattained lower endpoint.** The binary expansion of \(h_m=(4^m-1)/3\) has \(m\) copies of the low-to-high digit block \((1,0)\). Accordingly,

\[
r_m=25^{-m}e(T_1T_0)^mv,
\qquad T_1T_0=\begin{pmatrix}14&4\\10&10\end{pmatrix}.
\]

This two-by-two matrix has trace \(24\), determinant \(100\), and eigenvalues \(12\pm2\sqrt{11}\). Cayley–Hamilton gives the displayed second-order recurrence with \(r_0=1\), \(r_1=2/3\). Solving that recurrence yields the explicit expression. Since \(0<\lambda_-<\lambda_+<1\), it follows that \(r_m\to0\), whereas the positive-lag argument gives \(\rho(h)>0\) for each finite \(h\). This proves the infimum assertion and the claimed exponential decay rate.

## Verification

The accompanying `verify.py` uses only the Python standard library. It independently computes every cyclic cross-sum directly from the values \(2^{s_2(n)}\) and compares it with the carry-matrix expression for **every lag** at every \(L=1,\ldots,11\). This checks \(5{,}592{,}404\) individual index-lag contributions. It also checks the exact rational all-shift formula, upper bound and equality cases for \(1\le h<4096\), plus the alternating-shift recurrence through \(m=14\). Run `python3 verify.py` alongside this document. Observed output begins:

```
VERIFY_OK checked_cyclic_lag_pairs=5592404 max_levels=11 bound_shifts=4095 alternating_m=14
```

This finite enumeration independently checks computations but is **not** the proof for arbitrary shifts and levels; the proof is the exact carry identity plus elementary matrix inequalities and Cayley–Hamilton.

## Relationship to prior work

Glaisher's 1899 observation, Fine's 1947 extension, and Rowland's 2010 treatment of counts modulo prime powers establish the binary Pascal-row count \(F(n)\) and related single-row arithmetic; they do not specify shifted Pearson correlations of the row-count sequence. Spiegelhofer's 2014 thesis (Chapter 2, particularly its introduction and Theorems 2.1–2.2) studies shifted digit-sum **differences** and correlations of unit-modulus digit weights. Emme and Prikhod'Ko (2015) and Emme and Hubert (2016) analyze measures describing \(s_2(n+h)-s_2(n)\); these are not the joint weighted products \(2^{s_2(n)+s_2(n+h)}\) normalized by their diverging variance. Such digit-carry techniques supply relevant mathematical background, but the specifically sharp positive-lag Pearson extremum, its equality classification, and its infimum along explicit alternating lags do not follow directly from those cited statements. This is a priority assessment, **not** proof that no earlier general weighted-correlation result exists.

## Limitations

The claim concerns **binary** Pascal rows and a specified dyadic cyclic sampling and limiting convention. It does not state a correlation formula for every prime, for arbitrary row weightings, or for shifts growing with the sampled block length. Historical priority is qualified: a general weighted q-multiplicative autocorrelation result not identified here might imply part or all of the theorem. The research is supported by a mathematical proof and finite checks, but there has been no independent mathematical validation.

## References

1. J. W. L. Glaisher, *On the residue of a binomial-theorem coefficient with respect to a prime modulus*, 1899 (classical count cited by Rowland).
2. N. J. Fine, *Binomial coefficients modulo a prime*, 1947 (classical row-count formula).
3. E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783, first posted 2010-01-12. https://arxiv.org/abs/1001.1783
4. L. Spiegelhofer, *Correlations for numeration systems*, 2014 doctoral thesis, especially Chapter 2. https://www.dmg.tuwien.ac.at/spiegelhofer/files/2014_thesis.pdf
5. J. Emme and A. Prikhod'Ko, *On the asymptotic behaviour of the correlation measure of sum-of-digits function in base 2*, arXiv:1504.01701. https://arxiv.org/abs/1504.01701
6. J. Emme and P. Hubert, *Central Limit Theorem for probability measures defined by sum-of-digits function in base 2*, arXiv:1605.06297. https://arxiv.org/abs/1605.06297
7. J. Emme and P. Hubert, *Normal distribution of correlation measures of binary sum-of-digits functions*, arXiv:1810.11234. https://arxiv.org/abs/1810.11234
