# Exact tropical decoding ranks of Hamming spheres and balls

## Finding

Let \(\Sigma\) be a finite alphabet with \(q\ge2\) symbols and a distinguished zero, and write \(\operatorname{wt}(w)\) for the number of nonzero positions of a word. For integers \(\ell,t\ge0\), \(m=\ell+t\), and \(0\le r\le m\), define the exact-weight sphere \(S_r=\{w\in\Sigma^m:\operatorname{wt}(w)=r\}\) and the Hamming ball \(B_r=\{w\in\Sigma^m:\operatorname{wt}(w)\le r\}\). Given \(C\in\{S_r,B_r\}\), let \(W_C\) have rows \(x\in\Sigma^\ell\), columns \(y\in\Sigma^t\), and entry
\[
W_C(x,y)=d_H(xy,C)=\min_{c\in C}d_H(xy,c).
\]
**Theorem.** The min-plus/Barvinok factor rank and the min-plus tropical rank of both conditional decoding matrices are equal to
\[
\operatorname{rank}_{\mathrm{Bar}}(W_{S_r})=
\operatorname{rank}_{\mathrm{trop}}(W_{S_r})=
\operatorname{rank}_{\mathrm{Bar}}(W_{B_r})=
\operatorname{rank}_{\mathrm{trop}}(W_{B_r})
=1+\min\{\ell,t,r,m-r\}.
\]
Thus the full profile over all cut positions \(i=0,\ldots,m\) is \(1+\min\{i,m-i,r,m-r\}\). Both profiles agree although the two distance matrices need not agree. At a fixed block length \(m\), ranks \(1,\ldots,\lfloor m/2\rfloor+1\) are all attained by choices of radius and cut. In particular, \(m=4\), \(\ell=t=r=2\) gives rank \(3\) over the binary alphabet, unlike the power-of-two ranks for linear binary codes in [1].

## Assumptions and scope

The alphabet may have any finite cardinality \(q\ge2\); it need not be a field. Both parts of the coordinate split and the radius may be zero. The center is the all-zero word, and Hamming distance counts substitutions of individual letters. For an arbitrary real matrix \(M\), its min-plus factor rank is the smallest positive integer \(k\) for which there are real-valued vectors \(u_j,v_j\) with \(M(x,y)=\min_{1\le j\le k}(u_j(x)+v_j(y))\). The tropical rank is the largest order of a square submatrix for which the minimum among the permutation-sums is attained uniquely. These are rank definitions, not claims of algorithmic hardness or minimum state complexity of a general nonlinear trellis.

## Proof

**1. Radial distance identities.** A single Hamming substitution changes weight by at most one. Changing exactly the necessary nonzero coordinates to zero (or zero coordinates to any nonzero symbol) attains the lower bound for the sphere, hence
\[
d_H(w,S_r)=|\operatorname{wt}(w)-r|.
\]
For the ball, every word of weight at most \(r\) is already feasible, and otherwise precisely \(\operatorname{wt}(w)-r\) nonzero coordinates must be changed to zero. Thus
\[
d_H(w,B_r)=\max\{0,\operatorname{wt}(w)-r\}.
\]
Both matrices therefore depend only on \(p=\operatorname{wt}(x)\in\{0,\ldots,\ell\}\) and \(s=\operatorname{wt}(y)\in\{0,\ldots,t\}\), through \(F(p+s)\), with \(F(z)=|z-r|\) (sphere) or \(F(z)=\max\{0,z-r\}\) (ball).

**2. Explicit factorization.** Set
\[
a=\max\{0,r-t\},\qquad b=\min\{\ell,r\},\qquad k=b-a+1.
\]
The radius assumptions give \(0\le a\le b\le\ell\). For each integer \(j\in\{a,\ldots,b\}\), set \(v_j(y)=F(j+\operatorname{wt}(y))\). Choose any real \(M>m\) and define \(u_j(x)\) in terms of \(p=\operatorname{wt}(x)\) as follows: when \(a\le p\le b\), set \(u_p(x)=0\) and all other \(u_j(x)=M\); when \(p<a\), set \(u_a(x)=a-p\) for the sphere and \(u_a(x)=0\) for the ball, and all other coefficients to \(M\); when \(p>b\), set \(u_b(x)=p-b\) and all other coefficients to \(M\). In the first exceptional region, necessarily \(a=r-t>0\), and both rows \(p\) and \(a\) lie entirely on one side of the threshold \(r\). In the second, necessarily \(b=r<\ell\), and both rows lie entirely above the threshold. Consequently in all three cases,
\[
F(p+s)=\min_{a\le j\le b}\{u_j(x)+v_j(y)\}
\]
for every \(s\in\{0,\ldots,t\}\): at the selected index the right side equals the required value, while all other terms exceed \(m\), and the required value never exceeds \(m\). Hence \(\operatorname{rank}_{\mathrm{Bar}}(W_C)\le k\). Direct case analysis also yields \(k=1+\min\{\ell,t,r,m-r\}\).

**3. Tropically nonsingular minor.** For each \(j\in\{a,\ldots,b\}\), choose a left word \(x_j\) of weight \(j\), and a right word \(y_j\) of weight \(r-j\) (both exist by the interval bounds). Index a \(k\)-square submatrix by these words. Its \((i,j)\) entry is
\[
W_{S_r}(x_i,y_j)=|i-j|,\qquad
W_{B_r}(x_i,y_j)=\max\{0,i-j\}.
\]
Every diagonal entry vanishes. For the sphere, all off-diagonal entries are positive, so the identity is the unique zero-cost permutation. For the ball, all entries below the diagonal are positive; every nonidentity permutation moves some row index to a strictly smaller column index, since the sum of all row indices equals the sum of all permuted column indices. It therefore has positive total cost. Thus the identity is also the unique minimum permutation for the ball. It follows that both tropical ranks are at least \(k\).

**4. Tropical rank never exceeds min-plus factor rank.** For completeness, suppose a \((k+1)\)-square matrix had a unique minimum assignment but admitted a factorization into only \(k\) min-plus outer products. For each of its \(k+1\) selected assignment cells choose a factor attaining its value. Two such cells share a factor; exchanging their assigned columns yields a new permutation whose cost is no greater, because the shared factor makes the two cross-term sums equal while the matrix entries are no larger than factor values. This contradicts uniqueness. Therefore tropical rank is always at most min-plus factor rank. Combining with Parts 2 and 3 gives equality.

The profile statement substitutes \(\ell=i\) and \(t=m-i\). For fixed \(m\), take a balanced cut and vary \(r\) from zero to \(\lfloor m/2\rfloor\) to realize all asserted ranks. This completes the proof.

## Verification

The accompanying `checker.py` is independent of the symbolic proof. It verifies 432 parameter/function cases of the explicit rank-one factorization, 6,762 matrix entries, 4,902 witness-permutation comparisons, and independently brute-forces tropical ranks in 252 cases. It also computes the actual minimum Hamming distance over all codewords for 3,258 small inputs across alphabet sizes 2, 3, and 4, instead of relying on the closed distance formula. Run `python3 checker.py` and require a `VERIFY_OK` line. The infinite-parameter theorem follows from the proof above, not these finite experiments.

## Relationship to prior work

Sheshadri [1], first publicly posted July 26, 2026, proves that the conditional Hamming-decoding matrix of a **binary linear code** has tropical and min-plus factor ranks both exactly a power of two, determined by its minimal-trellis state dimension. The present result changes the target to two canonical generally nonlinear radial sets and determines all cut positions, radii, and alphabet sizes; the binary rank-three case cannot be obtained merely by choosing a binary linear code in [1]. The full available text of [1] was checked, including its theorem, proof and concluding questions. Develin, Santos and Sturmfels [2] developed the general rank notions and comparisons but their general framework alone is not an explicit rank evaluation for these two radial decoding families. Standard Monge and staircase-matrix structure is a possible route to another proof, and undiscovered implicit prior coverage is not excluded.

## Limitations

The target sets are Hamming spheres and centered balls only; the theorem does not classify general nonlinear codes, arbitrary error costs, approximate factorizations, or the complexity of computing nearest codewords. Equality of ranks is exact in the min-plus real semiring; it is not a lower bound on conventional computational running time. The cited literature comparison is not an exhaustive historical-priority certification, and independent validation has not been performed.

## References

[1] K. Sheshadri, *Trellis State Complexity as an Exact Tropical Factorization Rank*, arXiv:2607.23471, first submitted 2026-07-26. https://arxiv.org/abs/2607.23471

[2] M. Develin, F. Santos, and B. Sturmfels, *On the rank of a tropical matrix*, arXiv:math/0312114; MSRI Publications 52 (2005), 213–242. https://arxiv.org/abs/math/0312114
