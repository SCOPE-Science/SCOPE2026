# Parity sparsity under one additional digit in power partitions

## Finding
For each integer \(b\ge3\), let \(p_b(n)\) count representations
\[
n=\sum_{j\ge0}d_jb^j,\qquad d_j\in\{0,1,\ldots,b+1\},
\]
with finitely many nonzero digits. Define the number of odd coefficients in a complete base-power interval by
\[
A_b(m)=\#\{0\le n<b^m:p_b(n)\equiv1\pmod2\}\quad(m\ge0).
\]
Then, for every \(m\ge0\),
\[
A_b(0)=1,\qquad A_b(1)=b,\qquad
A_b(m+2)=(b-2)A_b(m+1)+4A_b(m)-2,
\]
and consequently
\[
\boxed{\sum_{m\ge0}A_b(m)z^m=
\frac{1+z-4z^2}{(1-z)(1-(b-2)z-4z^2)}.}
\]
Set
\[
\lambda_b=\frac{b-2+\sqrt{(b-2)^2+16}}2,
\quad \mu_b=\frac{b-2-\sqrt{(b-2)^2+16}}2,
\quad C_b=\frac{(b-1)\lambda_b}{(\lambda_b-1)(\lambda_b-\mu_b)}.
\]
The exact leading asymptotic is \(A_b(m)\sim C_b\lambda_b^m\), with \(C_b>0\). In particular, the odd coefficients have natural density zero, but their counting function has sharp polynomial order:
\[
\boxed{\#\{0\le n<X:p_b(n)\text{ is odd}\}
=\Theta_b\bigl(X^{\log_b\lambda_b}\bigr),
\qquad0<\log_b\lambda_b<1.}
\]
This is a genuine digit-cap effect: let \(h_b(n)\) be the analogous count with digits \(\{0,\ldots,b\}\) (one fewer allowed copy). Its previously determined parity-count exponent is \(\log_b\rho_b\), where
\[
\rho_b=\frac{b-1+\sqrt{(b-1)^2+8}}2.
\]
Although \(p_b(n)\ge h_b(n)\) for every \(n\), the odd-value support is asymptotically **sparser**: \(\lambda_b<\rho_b\) for all \(b\ge3\). At the exceptional endpoint \(b=2\), the corresponding enlarged-cap count is \(p_2(n)=\lfloor n/2\rfloor+1\), whose odd values instead have density \(1/2\).

## Assumptions and scope
The base \(b\) is a fixed integer at least three except in the explicitly separated binary endpoint. The index \(n\) and digit length \(m\) are nonnegative integers. A leading zero is permitted in a fixed-length base expansion, but it contributes no new representation. Each coefficient \(p_b(n)\) is a finite nonnegative integer. The asymptotic order has constants depending on the fixed base. Nothing is asserted about residues modulo four or higher, nor about the precise oscillations at arbitrary cutoffs \(X\).

## Proof
Define \(p_b(-1)=0\). The formal generating product is
\[
P_b(z)=\prod_{j\ge0}(1+z^{b^j}+\cdots+z^{(b+1)b^j})
=(1+z+\cdots+z^{b+1})P_b(z^b).
\]
Since \(b\ge3\), extracting coefficients gives the identities
\[
\begin{aligned}
p_b(bu)&=p_b(u)+p_b(u-1),\\
p_b(bu+1)&=p_b(u)+p_b(u-1),\\
p_b(bu+r)&=p_b(u),\qquad 2\le r<b,
\end{aligned}
\]
for all \(u\ge0\). They also hold at \(u=0\) with the stated convention.

Work modulo two. To each index \(u\ge0\) assign its ordered state \((p_b(u),p_b(u-1))\in\mathbb F_2^2\). Appending a least significant base-\(b\) digit \(r\) gives the exact state transformations
\[
\begin{aligned}
T_0(v,w)&=(v+w,w),\\
T_1(v,w)&=(v+w,v+w),\\
T_2(v,w)&=(v,v+w),\\
T_r(v,w)&=(v,v)\qquad(3\le r<b).
\end{aligned}
\]
The fourth state \((0,0)\) is absorbing and contributes no odd coefficient. Order the other three states as \((1,0),(1,1),(0,1)\). The row vector of their counts over all \(b^m\) fixed-length digit strings has initial value \((x_0,y_0,z_0)=(1,0,0)\) and evolves by
\[
(x_{m+1},y_{m+1},z_{m+1})=(x_m,y_m,z_m)
\begin{pmatrix}
1&b-1&0\\
1&b-3&1\\
0&2&1
\end{pmatrix}.
\]
The leading-zero transition fixes the initial state, so fixed-length words count each index \(0\le n<b^m\) once. The first coordinate is odd precisely in states \((1,0)\) and \((1,1)\), hence \(A_b(m)=x_m+y_m\). The matrix shows
\[
x_{m+1}=x_m+y_m=A_b(m),\qquad z_{m+1}=y_m+z_m.
\]
Therefore \(x_m-z_m\) is constant and equals one. Substituting \(z_m=x_m-1\) into the other transition yields
\[
\begin{aligned}
A_b(m+1)&=(b-2)A_b(m)+4x_m-2\\
&=(b-2)A_b(m)+4A_b(m-1)-2\quad(m\ge1).
\end{aligned}
\]
At level zero there is one odd coefficient; at level one all \(p_b(0),\ldots,p_b(b-1)\) equal one. These initial values give the claimed recurrence and, by multiplication of its generating series, the displayed rational function.

The nonconstant part of the recurrence has characteristic polynomial \(t^2-(b-2)t-4\), with roots \(\lambda_b\) and \(\mu_b\) as stated. Its constant particular solution is \(2/(b+1)\). Partial fractions at the simple pole \(z=1/\lambda_b\) give the leading coefficient
\[
C_b=\frac{(b-1)\lambda_b}{(\lambda_b-1)(\lambda_b-\mu_b)}.
\]
Since \(b\ge3\), one has \(\lambda_b>2\), \(|\mu_b|=4/\lambda_b<\lambda_b\), and \(\lambda_b<b\): the last statement follows because \(t^2-(b-2)t-4\) changes sign between \(0\) and \(b\). Thus the pole at \(1/\lambda_b\) dominates all others, proving \(A_b(m)\sim C_b\lambda_b^m\). Bounding an arbitrary \(X\) between two successive powers of \(b\) gives the sharp \(\Theta_b\) law and density zero.

For the cap comparison, the previously determined hyper-ary root \(\rho_b\) satisfies \(\rho_b^2-(b-1)\rho_b-2=0\). Hence
\[
\rho_b^2-(b-2)\rho_b-4=\rho_b-2>0
\]
for every \(b\ge3\); as the quadratic on the left has a unique positive root \(\lambda_b\), this implies \(\rho_b>\lambda_b\). Ordinary representation inclusion separately gives \(p_b(n)\ge h_b(n)\) for every \(n\). For \(b=2\), the digit cap three is \(2^2-1\), so the formal product telescopes to \((1-z)^{-1}(1-z^2)^{-1}\), with coefficient \(\lfloor n/2\rfloor+1\), odd exactly for \(n\equiv0,1\pmod4\).

## Verification
The standalone exact-integer program `verify_bounded_ary_parity.py` computes the full restricted product independently of the digit-state recurrence, compares their coefficient parities, verifies the three-state counts, and checks the claimed rational generating function. It checks complete base-power intervals for bases three through nine and the binary endpoint over 2,048 coefficients. The successful reported execution is `BOUNDED_POWER_PARITY_OK 39`. These finite tests corroborate the algebraic proof and are not used as a substitute for its infinite argument.

## Relationship to prior work
Coons (2026) studies the same bounded-multiplicity \(b\)-ary partitions in general digit caps, their coefficient growth, smoothness and monotonicity. Its accessible primary text neither states nor implies the exact modulo-two counting spectrum here from its explicitly established theorems. The published *A parity-sparsity transition for hyper-ary partitions* (2026) determines the corresponding parity-count law for the **different cap** \(b\), including the exponent \(\log_b\rho_b\) used in the comparison. That work's three-state transition and rational generating function count odd coefficients of \(h_b\), not of \(p_b\) with cap \(b+1\); its claimed theorem therefore does not provide the present recurrence or exponent. Earlier general digit/regular-sequence methods can compute values and imply finite-state descriptions, but this result supplies an exact all-base aggregate law and the strict reversal between pointwise representation monotonicity and parity-support exponent. A more general unpublished or unindexed parity classification could still cover it.

## Limitations
Only the smallest cap strictly above the hyper-ary bound is treated, and only parity is classified. The count at arbitrary \(X\) is bounded up to order of magnitude rather than by a complete periodic fluctuation formula. The existing pointwise digit algorithm and finite-state framework offer alternative ways of deriving the matrix; the contribution is the global exact enumerator, its exponent and cap-comparison. No independent mathematical audit has been performed.

## References
- M. Coons, *The Calkin--Wilf problems on \(\ell\)-ary partition functions*, arXiv:2611.08109v1, publicly submitted 5 November 2026. https://arxiv.org/html/2611.08109v1
- *A parity-sparsity transition for hyper-ary partitions*, published 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-parity-sparsity-transition-for-hyper-ary-partitions--bb0ad70479bb
- N. J. Calkin and H. S. Wilf, *Binary partitions of integers and Stern--Brocot-like trees*, unpublished preprint (1998; updated 2009), as cited by Coons; its full text was not inspected in this comparison.
