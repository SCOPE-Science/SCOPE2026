# Exact three-phase convergence of dyadic Walsh–Kaczmarz Fejér norms

## Finding

Let \(G=\prod_{j\geq0}\mathbb Z_2\) have normalized Haar probability measure, and let \(K_N^\kappa=N^{-1}\sum_{k=1}^N D_k^\kappa\) be the Walsh–Kaczmarz Fejér kernel. For every integer \(n\geq1\), write \(n=3m+r\), where \(0\leq r\leq2\), and set \(L_n=\|K_{2^n}^\kappa\|_{L^1(G)}\). Then **the following identities hold exactly**:

\[
\begin{aligned}
\tfrac43-L_{3m}&=\tfrac52\,4^{-m}-\tfrac72\,8^{-m}+\tfrac43\,16^{-m} &&(m\geq1),\\
\tfrac43-L_{3m+1}&=\tfrac{19}{12}\,4^{-m}-\tfrac74\,8^{-m}+\tfrac12\,16^{-m} &&(m\geq0),\\
\tfrac43-L_{3m+2}&=4^{-m}-\tfrac78\,8^{-m}+\tfrac5{24}\,16^{-m} &&(m\geq0).
\end{aligned}
\]

Thus the convergence to the known limit \(4/3\) has the **sharp fractional exponent** \(2/3\): \(\tfrac43-L_n\asymp 2^{-2n/3}\). Its three exact phase constants are
\[
\lim_{m\to\infty}4^m(\tfrac43-L_{3m})=\tfrac52,\quad
\lim_{m\to\infty}4^m(\tfrac43-L_{3m+1})=\tfrac{19}{12},\quad
\lim_{m\to\infty}4^m(\tfrac43-L_{3m+2})=1.
\]
The exponent is sharp: replacing \(2/3\) by any greater exponent produces no uniform upper bound with a fixed constant.

## Assumptions and scope

The Walsh–Kaczmarz characters have the standard ordering \(\kappa_0=1\) and, for integers \(j\geq0\) and \(0\leq k<2^j\),
\[
\kappa_{2^j+k}(x)=(-1)^{x_j+\sum_{\ell=0}^{j-1}k_\ell x_{j-1-\ell}},
\]
where \(k_\ell\) is the \(\ell\)-th binary digit of \(k\), and \(x_j\in\{0,1\}\). Set \(D_k^\kappa=\sum_{h=0}^{k-1}\kappa_h\). The kernels depend on only \(x_0,\ldots,x_{n-1}\). The assertion applies to every integer \(n\geq1\) with the indicated boundary values; no assumptions on a function acted on by the Fejér operator are needed.

## Proof

Write \(N=2^n\), \(r_j(x)=(-1)^{x_j}\), and
\[
A_N(x):=N K_N^\kappa(x)=\sum_{h=0}^{N-1}(N-h)\kappa_h(x).
\]
Splitting the nonconstant terms into dyadic blocks \(2^j\leq h<2^{j+1}\) gives the exact identity
\[
A_N(x)=N+\sum_{j=0}^{n-1}r_j(x)\left[C_j\mathbf1_{x_0=\cdots=x_{j-1}=0}+\sum_{a=0}^{j-1}2^{2j-2-a}\mathbf1_{(x_0,\ldots,x_{j-1})=e_a}\right],
\]
with \(C_j=2^jN-\tfrac32 4^j+\tfrac12 2^j\) and \(e_a\) the length-\(j\) binary vector with one bit at position \(a\). To check the block identity, use character orthogonality to evaluate \(\sum_{k<2^j}(N-2^j-k)(-1)^{\sum k_\ell x_{j-1-\ell}}\): its Walsh transform has support only at the zero prefix and the \(j\) one-bit prefixes. Specifically, the transform of the constant part is \(2^j(N-2^j)\) at the zero prefix, and the transform of \(k\) is \(2^{j-1}(2^j-1)\) at zero and \(-2^{2j-2-a}\) at prefix \(e_a\). These yield the displayed coefficients, including \(j=0\).

For a binary sequence whose first two one-bits are \(a<b<n\), all terms after \(j=b\) vanish. Summing the preceding geometric series therefore gives
\[
A_N(x)=4^a-\frac{2^a}{3}\left(2\,4^{b-a-1}+1\right).
\]
For the all-zero prefix, \(A_N=N(N+1)/2>0\); when there is exactly one one-bit at \(a\), the same block identity gives
\[
A_N(x)=4^a+\sum_{j=a+1}^{n-1}2^{2j-2-a}>0.
\]
Thus **every negative value is determined entirely by the positions of the first two one-bits**, and it is negative precisely when
\[
3a\leq 2b-3.
\]
Indeed, multiplying the two-one formula by \(3/2^a\) reduces its sign to that of \(3\cdot2^a-2^{2(b-a)-1}-1\). Because the exponents and \(a\) are integers, the strict-negative threshold is exactly the displayed integer inequality, including the equality case \(a=0,b=1\), where the value is zero.

Each pair \(a<b<n\) occurs on precisely \(2^{n-b-1}\) binary cylinders of length \(n\). Since \(\int_G K_N^\kappa\,d\mu=1\), its \(L^1\) norm equals one plus twice the negative mass. With \(s_b=\lfloor(2b-3)/3\rfloor\), summing the contributions yields
\[
L_n=1+\frac1{3\cdot2^n}\sum_{b=2}^{n-1}\left(2^b-R_b\right),\quad
R_b=2^{b-1-s_b}-2^{s_b+1-b}+2^{2s_b+2-b}.
\]
The sum is empty for \(n\leq2\). When \(b=3k,3k+1,3k+2\), the terms \(R_b\), respectively, are
\[
2^{k+1}-2^{-k},\qquad \tfrac52\,2^k-2^{-k-1},\qquad 3\,2^k-2^{-k-1}.
\]
The first two cases begin at \(k=1\), and the third at \(k=0\). As \(\sum_{b=2}^{n-1}2^b=2^n-4\), we obtain
\[
\tfrac43-L_n=\frac{4+\sum_{b=2}^{n-1}R_b}{3\cdot 2^n}.
\]
Summing the three geometric progressions separately for \(n=3m\), \(3m+1\) and \(3m+2\) yields the three exact identities in the Finding. Positivity and the limits follow directly from the formula (or from the positive finite sum). Every step is finite, exact and valid for all stated integers.

## Verification

The accompanying `check.py` uses independent integer Walsh–Hadamard transforms of the coefficient weights \(N-h\), with reversed binary digit order on each Kaczmarz block. It compares direct \(L^1\) norms, the closed phase expressions, and independently summed negative-cylinder contributions at \(1\leq n\leq12\). It separately checks the integer sign threshold for all \(0\leq a<b<85\) and compares exact finite sums to the formulas for \(1\leq n\leq60\). These finite tests supplement, but do not prove, the all-integer theorem; the proof is the block-transform and geometric-sum argument above. Run with `python3 check.py` from this package.

## Relationship to prior work

Blahota (2026) proves the global Walsh–Kaczmarz–Fejér supremum \(71/50\), and for dyadic orders proves that \(L_n\) increases to \(4/3\), using Skvorcov's splitting identity. The exact three-phase finite-order formulas and the sharp fractional convergence exponent are a quantitative refinement of that motivating limit. The accessible abstract does not state them, but the complete 2026 paper was not available for direct comparison; overlap within its uninspected proofs remains an acknowledged risk. Nagy (2008) supplies the classical Walsh–Kaczmarz block identities and maximal-kernel estimates. Its inspected theorem and pointwise bounds do not explicitly give the stated finite-order norm formulas: the additional sign classification and exact weighted cylinder count are essential to the calculation. This is a quantitative sharpening, not a claim that Skvorcov's decomposition, the existence of the limit or its value are new.

## Limitations

The theorem concerns only dyadic indices \(N=2^n\), not the general integer-indexed Fejér sequence or maximal kernels. The 2026 motivating source was available only through its abstract, so it is possible that the precise formulas already occur in its inaccessible body, or that a further older source contains an equivalent. The result neither establishes publication priority nor provides an independent mathematical audit. The finite checker does not certify the infinite assertion.

## References

1. I. Blahota, *The exact \(L_1\)-norm supremum of Walsh--Kaczmarz--Fejér kernels*, arXiv:2607.13684, first public 2026-07-15, https://arxiv.org/abs/2607.13684.
2. K. Nagy, *On the \(L^1\) norm of the weighted maximal function of Fejér kernels with respect to the Walsh–Kaczmarz system*, Journal of Inequalities in Pure and Applied Mathematics 9(1), Article 16 (2008), https://delphi.icm.edu.pl/packages/EMIS/journals/JIPAM/images/170_07_JIPAM/170_07.pdf.
3. G. Gát, *On \((C,1)\) summability of integrable functions with respect to the Walsh–Kaczmarz system*, Studia Mathematica 130 (1998), 135–148, as cited in Nagy (2008).
