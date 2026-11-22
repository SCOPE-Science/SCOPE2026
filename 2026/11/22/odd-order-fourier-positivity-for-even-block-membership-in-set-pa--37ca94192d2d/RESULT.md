# Odd-order Fourier positivity for even-block membership in set partitions

## Finding
Let \(\Pi_n\) be the set of all partitions of \([n]\). For a partition \(\pi\), put \(E(\pi)=\bigcup_{B\in\pi,\,|B|\text{ even}}B\). On \(G_n=(\mathbb Z/2\mathbb Z)^n\), let \(w_n(s)\) count the partitions with indicator \(1_{E(\pi)}=s\) and let \(T_n f=w_n*f\), using unnormalized convolution. Its Walsh multiplier at \(U\subseteq[n]\) is \(\lambda_n(U)=\sum_{\pi\in\Pi_n}(-1)^{|U\cap E(\pi)|}\).

**Theorem.** For all \(n\ge1\), every Walsh multiplier whose character weight \(|U|\) is even is strictly positive. Furthermore \(\lambda_n(U)=\lambda_n([n]\setminus U)\). Consequently, for **every odd \(n\ge1\)**, all \(2^n\) multipliers are strictly positive, and the counting convolution \(T_n\) is positive definite and invertible. For even \(n\), any possible zero or negative multiplier must have odd character weight. At \(n=2\), the ordered multipliers by weight are \(2,0,2\), so the rank is \(2\) and the nullity is \(2\).

Equivalently, the sign of a partition is \((-1)\) raised to the number of co-block marked--unmarked pairs: for a block with \(a\) marked and \(b\) unmarked vertices, \(a\,1_{\{a+b\text{ even}\}}\equiv ab\pmod 2\). Thus the finding also gives a strict signed cross-incidence inequality for every odd total number of vertices.

A constructive all-order identity is available. If \(k=|U|\), \(\ell=n-k\), and \(Z\) is Poisson with mean one, then
\[
\lambda_n(U)=\sum_{\rho\in\Pi_\ell}\mathbb E\!\left[(Z+e(\rho)-o(\rho))^k\right],
\]
where \(e(\rho)\) and \(o(\rho)\) count, respectively, the even-sized and odd-sized blocks of \(\rho\). This identity is exact with the convention that a zeroth power is one.

## Assumptions and scope
All partitions are unordered collections of nonempty blocks and all vertices are labelled. The count is unweighted; the Walsh transform and convolution use no normalization. No restriction is placed on block sizes, and the theorem holds for every integer \(n\ge1\). A parity-protected Fourier sector is established in all orders; complete strict positivity is proved here only for odd orders. The result is not a theorem of positive definiteness for every even order.

## Proof
For \(U\subseteq[n]\), write \(k=|U|\), \(\ell=n-k\), and temporarily distinguish the \(k\) marked from the \(\ell\) unmarked labels. A block containing \(a\) marked and \(b\) unmarked elements contributes the sign \((-1)^a\) when \(a+b\) is even, and contributes \(+1\) when \(a+b\) is odd. The labelled set-partition exponential formula therefore gives the bivariate exponential generating function
\[
F(x,y)=\sum_{k,\ell\ge0}\lambda_{k+\ell,k}\frac{x^k}{k!}\frac{y^\ell}{\ell!}
=\exp\left(\cosh(y-x)-1+\sinh(x+y)\right)
=\exp\left(e^x\cosh y+e^{-x}\sinh y-1\right).
\]
Here \(\lambda_{n,k}\) abbreviates the multiplier of any weight-\(k\) character; exchangeability makes the choice of labels irrelevant.

Split the last exponential into
\[
F(x,y)=\underbrace{\exp(e^x-1)}_{\mathbb E(e^{xZ})}\,\exp\left(e^x(\cosh y-1)+e^{-x}\sinh y\right).
\]
In the second factor, the coefficient of \(y^\ell/\ell!\) counts partitions \(\rho\in\Pi_\ell\), assigning the factor \(e^x\) to each even block and \(e^{-x}\) to each odd block. Hence it equals \(\sum_{\rho\in\Pi_\ell}e^{x(e(\rho)-o(\rho))}\). Since \(\exp(e^x-1)=\mathbb E(e^{xZ})\), the coefficient of \(x^k/k!\) is precisely
\(\sum_{\rho\in\Pi_\ell}\mathbb E[(Z+e(\rho)-o(\rho))^k]\).

If \(k\ge2\) is even, every summand is strictly positive: an integer shift of a nondegenerate Poisson variable cannot be identically zero, and its positive even moment is strictly positive. If \(k=0\), the expression is \(\sum_{\rho\in\Pi_n}1=B_n>0\). Thus all even-weight Fourier multipliers are strictly positive.

Finally, \(|E(\pi)|\) is even, being the sum of even block sizes. Thus
\[
(-1)^{|E(\pi)\cap U|}=(-1)^{|E(\pi)\cap([n]\setminus U)|}
\]
for every \(\pi\), so the complementary characters have equal multipliers. For odd \(n\), at least one of \(|U|\) and \(n-|U|\) is even; its multiplier is positive and equal to the other's. Walsh characters diagonalize convolution on \(G_n\); positive multipliers imply strict positive definiteness and invertibility. At \(n=2\), the only partitions have even-block profiles \(\varnothing\) and \(\{1,2\}\), each with count one; their Walsh sums by weight are \(2,0,2\). This proves every assertion.

## Verification
The accompanying Python 3 program `verify_evenblock.py` independently enumerates all set partitions for \(n\le9\), constructs the full profile kernel, computes its complete Walsh transform by a fast Walsh--Hadamard transform, and compares every frequency with an independent distinguished-block recurrence. It additionally checks the Poisson/Bell-moment identity for \(0\le\ell\le8\), \(0\le k\le12\), and both symmetry and protected-sector inequalities through \(n=30\). A successful run prints `PASS exact assertions: 2024`. The infinite theorem follows from the preceding argument, not from finite enumeration.

For example, at \(n=7\), the multipliers at weights \(0,1,\ldots,7\) are \(877,41,193,85,85,193,41,877\). At \(n=8\), the corresponding finite list is \(4140,162,908,66,684,66,908,162,4140\). The first list illustrates the proved odd-order result; the second is only a finite computation and implies no unproved even-order assertion.

## Relationship to prior work
The exponential formula, Bell-number enumeration, parity-restricted partition families and Poisson representation are classical. Calderbank--Hanlon--Robinson study partitions with prescribed block-size parity in the context of symmetric-group characters and poset homology. Chern--Diaconis--Kane--Rhoades give systematic generating functions and moments for set-partition statistics. Neither the inspected text of the latter nor the accessible abstract of the former establishes the strict Boolean Walsh positivity of the *vertex set belonging to even-sized blocks*. The present claim uses a separate two-colour Fourier signing and the resulting Poisson even-moment argument. An inaccessible complete 1986 text leaves a historical-priority risk, and no claim of exhaustive literature coverage is made.

## Limitations
This theorem does not classify odd-weight multipliers at even orders \(n\ge4\), determine all spectral minima or condition numbers, or provide an independent audit. Computations through \(n=30\) cannot settle those questions. Strict positivity at odd orders is proved exactly for the unnormalized counting kernel; normalizing by the Bell number scales all eigenvalues by the same positive factor. The comparison with the 1986 parity-partition article is limited by unavailable full text.

## References
1. A. R. Calderbank, P. Hanlon and R. W. Robinson, *Partitions into Even and Odd Block Size and Some Unusual Characters of the Symmetric Groups*, Proceedings of the London Mathematical Society s3-53 (1986), 288--320; published 1986-09-01, https://doi.org/10.1112/plms/s3-53.2.288.
2. B. Chern, P. Diaconis, D. M. Kane and R. C. Rhoades, *Closed expressions for averages of set partition statistics*, arXiv:1304.4309, first posted 2013-04-16; open-access journal version 2014, https://arxiv.org/abs/1304.4309 and https://doi.org/10.1186/2197-9847-1-2.
3. Classical Bell exponential and Dobinski formulas, as recalled in Reference 2, sections on set-partition enumeration and distributional formulas.
