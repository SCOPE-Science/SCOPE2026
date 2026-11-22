# A residue-class phase transition for order-four affine derangements

## Finding
Let \(q=2^e\) for an integer \(e\ge1\), let \(n\ge2\), and choose uniformly among the elements of order **exactly four** in \(\operatorname{AGL}_n(\mathbb F_q)\). Denote by \(D_n(q)\) the probability of having no fixed point. There is one limiting probability \(L_s(q)\) for each dimension residue \(s\in\{0,1,2,3\}\):
\[
L_s(q)=\lim_{a\to\infty}D_{4a+s}(q).
\]
Define \(\Phi_j(q)=\prod_{k=1}^j(1-q^{-k})\) for every \(j\ge0\), and \(\Phi_0(q)=1\). For every weakly decreasing integer quadruple \(d=(d_1,d_2,d_3,d_4)\) with \(\sum_i d_i=s\), put
\[
W_q(d)=\frac{q^{-\sum_{i=1}^4d_i^2-d_4}}{\Phi_{d_1-d_2}(q)\Phi_{d_2-d_3}(q)\Phi_{d_3-d_4}(q)}.
\]
Then the convergent formula is
\[
\boxed{L_s(q)=\frac{\sum_d W_q(d)(1-q^{-(d_1-d_4)})}{\sum_d W_q(d)}}.
\]
The new asymptotic transition, for even prime powers \(q\to\infty\), is
\[
\boxed{L_0(q)=q^{-1}+O(q^{-2}),\qquad L_s(q)=1-q^{-1}+O(q^{-2})\ (s=1,2,3).}
\]
In particular the limiting derangement probability vanishes for dimensions divisible by four and approaches one in the other three residue classes, in this iterated order of limits (first dimension, then field size).

## Assumptions and scope
All fields are finite of characteristic two. The probability is conditioned on affine elements of exact order four, not on all affine transformations and not on elements whose order merely divides four. The large-dimension limit is along \(n=4a+s\), with \(q\) fixed, followed by the \(q\to\infty\) comparison. For \(n=1\) no affine element has exact order four in characteristic two, which is why the finite conditional probability is defined only for \(n\ge2\). This is not a classification of all derangements in affine groups.

## Proof
**1. Affine order and translations.** Write \(g(x)=(I+N)x+v\). Because the characteristic is two, \(g^4=I\) precisely when \(N^4=0\) and \(N^3v=0\). The equation \(g(x)=x\) has a solution if and only if \(v\in\operatorname{im}N\). Since \(\operatorname{im}N\subseteq\ker N^3\), the numbers of translations producing an affine order-dividing-four element and a derangement, respectively, are \(q^{n-\operatorname{rank}N^3}\) and \(q^{n-\operatorname{rank}N^3}-q^{\operatorname{rank}N}\).

**2. Exact finite sums.** Let \(c=(c_1,\ldots,c_h)\) be the column lengths of the nilpotent Jordan partition of \(N\), where \(c_1\ge\cdots\ge c_h\ge0\), \(\sum_i c_i=n\), and \(c_{h+1}=0\). For \(h=2,4\), write
\[
Z_h(c)=q^{\sum_{i=1}^h c_i^2}\prod_{i=1}^h\Phi_{c_i-c_{i+1}}(q),
\]
which is the standard centralizer order of the nilpotent matrix. Its conjugacy class contains \(|\mathrm{GL}_n(q)|/Z_h(c)\) matrices, and \(\operatorname{rank}N^{h-1}=c_h\), \(\operatorname{rank}N=n-c_1\). Consequently the exact counts of affine elements of order dividing \(h\) and of such derangements are
\[
T_h(n)=|\mathrm{GL}_n(q)|\sum_c\frac{q^{n-c_h}}{Z_h(c)},\qquad
F_h(n)=|\mathrm{GL}_n(q)|\sum_c\frac{q^{n-c_h}-q^{n-c_1}}{Z_h(c)}.
\]
For \(h=2\) the same argument uses \(g^2=I\) precisely when \(N^2=0\) and \(Nv=0\). Subtracting the order-dividing-two elements gives
\[
D_n(q)=\frac{F_4(n)-F_2(n)}{T_4(n)-T_2(n)}.
\]
These finite rational-canonical-form counts follow from classical formulas; they are included as an input, not asserted to be original.

**3. Suppression of order two.** For \(h\in\{2,4\}\), Cauchy–Schwarz gives \(\sum_i c_i^2\ge n^2/h\). The products \(\Phi_j(q)\) are bounded below by \(\Phi_\infty(q)=\prod_{j\ge1}(1-q^{-j})>0\). There are at most polynomially many partitions with at most four columns. A balanced four-column partition has squared-column norm \(n^2/4+O(1)\); thus, after cancellation of \(|\mathrm{GL}_n(q)|\),
\[
\frac{T_2(n)}{T_4(n)}=O_q(q^{-n^2/4+O(n)})\to0.
\]
Since \(0\le F_2\le T_2\), the same error estimate permits replacing exact-order-four counts by order-dividing-four counts in the limiting proportion.

**4. Centering four columns.** Write \(n=4a+s\) and \(c_i=a+d_i\). Then \(\sum_i d_i=s\), and the common factor in the four-column contribution is
\[
q^{-4a^2-2as+3a+s},
\]
leaving \(W_q(d)/\Phi_{a+d_4}(q)\). Its derangement proportion is \(1-q^{-(d_1-d_4)}\). For fixed \(d\), \(\Phi_{a+d_4}(q)\to\Phi_\infty(q)\). Further, \(\sum_i d_i^2+d_4\) is coercive under the fixed-sum constraint, while the products of reciprocal \(\Phi\)-factors are uniformly bounded by powers of \(\Phi_\infty(q)^{-1}\). Gaussian domination permits interchange of the limit and summation, yielding the displayed theta quotient. This also proves positivity and absolute convergence of the two series.

**5. The four residue classes over large fields.** Let \(E(d)=\sum_i d_i^2+d_4\). If the difference between largest and smallest entries is at least two, transfer one unit from a largest entry to a smallest one and reorder. The sum of squares drops by at least two and the smallest-entry term increases by at most one; thus \(E\) strictly decreases. The unique minimizer at fixed sum \(s\in\{0,1,2,3\}\) is the balanced quadruple with \(s\) entries equal to one and \(4-s\) entries equal to zero. Its exponent is \(E=s\). For \(s=0\) its derangement multiplier vanishes; the unique exponent-one competitor is \((1,0,0,-1)\), whose multiplier is \(1-q^{-2}\), giving \(L_0(q)=q^{-1}+O(q^{-2})\). For \(s=1,2,3\) the minimizer has multiplier \(1-q^{-1}\). Every other quadruple has weight smaller by at least a factor of \(q^{-1}\), and its multiplier differs from the minimizer's by at most \(q^{-1}\); hence \(L_s(q)=1-q^{-1}+O(q^{-2})\). The Gaussian tail is uniform for \(q\ge2\), proving the error bounds.

## Verification
The standalone file `check_affine4.py` computes integer centralizer and conjugacy class sizes and compares the resulting finite formula with separate exhaustive affine-matrix enumerations for \(q=2\), \(n\le4\), and \(q=4\), \(n\le2\). All six cases passed; representative exact-order-four pairs of (all elements, derangements) are \((420,252)\) for \(q=2,n=3\) and \((43680,18480)\) for \(q=2,n=4\). Run `python check_affine4.py` to reproduce the checks. The infinite and double limits are proved analytically above, not inferred from those finite checks.

## Relationship to prior work
Fulman's 2000 cycle-index theory gives broad affine rational-canonical-form distributions and is the source of the standard class-counting machinery; the finite counts in Step 2 are **not new**. Guest–Morris–Praeger–Spiga (2013) analyze affine transformations with very large permutation orders rather than exact small order conditioned derangements. Spiga (2017) gives a general formula for affine derangements of prime-power order, which is an especially close antecedent; its abstract was available but a full text inspection was not possible. The claim of distinctiveness is restricted to the explicit four dimension-residue theta limits and their opposite large-field regimes, not to the underlying cycle indices or all prime-power derangement enumerations.

## Limitations
No assertion is made that the finite exact-order-four formula is historically new. The directly relevant Spiga paper could not be compared line-by-line, so possible earlier derivation or implication of the theta-limit phase law remains a genuine priority risk. No independence or externally certified proof is claimed. The large-field limit and the large-dimension limit are **ordered** and cannot be interchanged without further argument. The simple numerical near-equality of two finite-q limits is not claimed as an identity.

## References
- Jason Fulman, *Finite Affine Groups: Cycle Indices, Hall–Littlewood Polynomials, and Probabilistic Algorithms*, first posted 2000-09-19, https://arxiv.org/abs/math/0009182.
- Simon Guest, Joy Morris, Cheryl E. Praeger and Pablo Spiga, *Affine transformations of finite vector spaces with large orders or few cycles*, first posted 2013-06-06, https://arxiv.org/abs/1306.1368.
- Pablo Spiga, *On the number of derangements and derangements of prime power order of the affine general linear groups*, *Journal of Algebraic Combinatorics* 45 (2017), 345–362, https://doi.org/10.1007/s10801-016-0709-3. Abstract inspected; full text not accessed.
