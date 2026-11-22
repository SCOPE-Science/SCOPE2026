# Complete two-primary Smith forms of Wendt binomial circulants at power-of-two-neighbor orders

## Finding
For every integer \(n\ge1\), write \(B_n\) for the integer circulant matrix with entries
\[
(B_n)_{i,j}=\binom{n}{(j-i)\bmod n},\qquad 0\le i,j<n,
\]
where the residue in the lower argument is chosen in \(\{0,\ldots,n-1\}\). This is the classical binomial circulant underlying Wendt's determinant. For every integer \(r\ge1\), its two-primary cokernel at the two neighboring orders is exactly
\[
\boxed{\operatorname{coker}(B_{2^r-1})[2^\infty]\cong
(\mathbb Z/2\mathbb Z)^{\,2^r-2},}
\]
and
\[
\boxed{\operatorname{coker}(B_{2^r+1})[2^\infty]\cong
\begin{cases}
(\mathbb Z/2\mathbb Z)^2,&r\text{ odd},\\
0,&r\text{ even}.
\end{cases}}
\]
In particular, every nontrivial two-primary elementary divisor in these families has exact order two. Equivalently, the two-adic Smith valuations are \(0\) once and \(1\) exactly \(2^r-2\) times in the minus family, and are either all zero or \(0\) exactly \(2^r-1\) times followed by two \(1\)'s in the plus family. For \(r=1\) the minus-family matrix has order one, so its cokernel is zero.

Consequently, for every \(r\ge1\),
\[
\nu_2(\det B_{2^r-1})=2^r-2,\qquad
\nu_2(\det B_{2^r+1})=\begin{cases}2,&r\text{ odd},\\0,&r\text{ even}.\end{cases}
\]
Both determinants are nonzero because their orders are odd and Wendt's determinant vanishes exactly when its order is divisible by six.

## Assumptions and scope
The entries and cokernels are integral; the Smith classifications concern the prime two only. The exponent \(r\) is an arbitrary positive integer. The proof works over the two-adic integers \(\mathbb Z_2\), and the two-primary component of an integral finite cokernel is unchanged by passing to \(\mathbb Z_2\). No assertions about odd-primary Smith factors or orders not of the displayed forms are made.

## Proof
**1. Circulant representation and diagonalization.** Write \(a_n(X)=\sum_{k=0}^{n-1}\binom nk X^k\). In \(\mathbb Z[X]/(X^n-1)\), multiplication by \(a_n(X)\) represents \(B_n\) up to transpose. Since \(X^n=1\) in this quotient,
\[
a_n(X)=(1+X)^n-X^n\equiv(1+X)^n-1\pmod{X^n-1}.
\]
All orders under consideration are odd. Hence \(X^n-1\) is separable modulo two, and it splits into distinct linear factors after a finite unramified extension of \(\mathbb Z_2\). Consequently the circulant becomes diagonal with entries
\[
\lambda_n(\zeta)=(1+\zeta)^n-1,\qquad\zeta^n=1,
\]
where the \(n\) roots are their unique odd-order two-adic lifts. Unramified base extension preserves the valuations and multiplicities of the Smith factors: invertible integral row and column operations remain invertible, and the uniformizer is still two. Thus it suffices to determine the valuation of every displayed eigenvalue.

**2. The minus family.** Let \(n=2^r-1\). At \(\zeta=1\), \(\lambda_n(1)=2^n-1\) is odd. Every other root \(\zeta\) reduces to a nontrivial element of \(\mathbb F_{2^r}^{\times}\), so both \(\zeta\) and \(1+\zeta\) are two-adic units. The elementary identity
\[
\nu_2\!\left(\binom{2^r}{k}\right)=r-\nu_2(k)
\quad(1\le k<2^r)
\]
follows from \(\binom{2^r}{k}=(2^r/k)\binom{2^r-1}{k-1}\) and Lucas's theorem, which makes the second binomial odd. Therefore the only intermediate binomial coefficient of \((1+X)^{2^r}\) not divisible by four is the central one, which is two modulo four. Hence
\[
(1+\zeta)^{2^r}\equiv1+\zeta^{2^r}+2\zeta^{2^{r-1}}
\equiv1+\zeta+2\zeta^{2^{r-1}}\pmod4,
\]
since \(\zeta^{2^r}=\zeta\). Dividing by the unit \(1+\zeta\) gives
\[
\lambda_n(\zeta)\equiv
\frac{2\zeta^{2^{r-1}}}{1+\zeta}\pmod4.
\]
The quotient multiplying two is a unit. Thus each of the \(n-1\) nonidentity roots gives valuation exactly one and the identity root gives valuation zero. The case \(r=1\) has no nonidentity roots and is included.

**3. The plus family.** Let \(n=2^r+1\). Lucas's theorem yields
\[
a_n(X)\equiv1+X+X^{2^r}\pmod2.
\]
At any odd-order root \(\zeta^n=1\), one has \(\zeta^{2^r}=\zeta^{-1}\), so the eigenvalue is even exactly when
\[
1+\bar\zeta+\bar\zeta^{-1}=0,
\quad\text{equivalently}\quad \bar\zeta^2+\bar\zeta+1=0
\]
in characteristic two. The two roots of this quadratic are the primitive cubic roots; both belong to the \(n\)-th roots precisely when \(3\mid n\), equivalently when \(r\) is odd. If \(r\) is even all eigenvalues are units. If \(r\) is odd, the two primitive cubic roots \(\zeta\) satisfy \(1+\zeta=-\zeta^2\). Since \(n\) is odd and divisible by three,
\[
\lambda_n(\zeta)=(-\zeta^2)^n-1=-2,
\]
so each has valuation exactly one, while every other eigenvalue is a unit. This proves the second classification.

**4. Integral conclusion.** Every order in the theorem is odd, hence is not divisible by six; the classical nonvanishing theorem ensures finite cokernels. The two-adic diagonal valuations in steps 2–3 are exactly the two-primary elementary divisors of these cokernels, and summing them gives the stated determinant valuations.

## Verification
Run `python3 verify_wendt_binary.py` in the same directory (Python 3 and SymPy required). The checker independently computes binomial circulants modulo four, extracts unit and valuation-one Smith counts using modular Schur complements and binary ranks, and compares with the formulas for the minus family at exponents \(1\le r\le7\) and the plus family at \(1\le r\le6\). It also computes complete integral Smith forms at orders \(1,3,5,7,9,15,17\), and tests the critical binomial-coefficient congruence for \(1\le r\le11\). These finite computations check arithmetic and normalization but are not the proof of the all-exponent theorem, which is given above.

## Relationship to prior work
Wendt's binomial circulant and its resultant representation are classical. Frame (1980) studies its prime factorization and proves a square-factor decomposition of its determinant. Helou (1997) studies discriminant formulas for certain even orders; Helou and Terjanian (2005) give general arithmetic congruences and norm representations. Those inspected results do not directly state or supply the displayed two-primary integral Smith classifications for both power-of-two-neighbor families. The determinant values indexed in OEIS A048954 are scalar data, not full Smith information. The recent Tang–Fan paper treats prime-characteristic restrictions for permutation binomials using Wendt determinants, not a stated two-primary Smith classification in its available abstract. Historical priority beyond the inspected sources remains uncertain.

## Limitations
This is a two-primary classification for two explicit infinite families, not a full integral Smith form or a theorem at all orders. The result does not sharpen or revise historical determinant formulas for arbitrary orders; it identifies additional lattice information at natural binary-order families. No assertion of independent validation or exhaustive literature coverage is made.

## References
- J. S. Frame, *Factors of the Binomial Circulant Determinant*, Fibonacci Quarterly 18(1) (1980), 9–23. https://www.fq.math.ca/Scanned/18-1/frame.pdf
- C. Helou, *On Wendt's Determinant*, Mathematics of Computation 66 (1997), 1341–1346. https://doi.org/10.1090/S0025-5718-97-00870-3
- C. Helou and G. Terjanian, *Arithmetical Properties of Wendt's Determinant*, Journal of Number Theory 115 (2005), 45–57; available online January 30, 2005. https://doi.org/10.1016/j.jnt.2004.09.003
- OEIS A048954, *Wendt determinant of n-th circulant matrix*. https://oeis.org/A048954
- Z. Tang and X. Fan, *Wendt's determinant and finiteness of prime characteristics for permutation binomials*, arXiv:2610.18584 (2026). https://arxiv.org/abs/2610.18584
