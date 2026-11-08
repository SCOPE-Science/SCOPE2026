# First two point counts of prime-field maximal curves with trivial automorphism group

## Finding
Let \(p\) be an odd prime and let \(n\ge2\) be an integer. Let \(X_{p,n}\) be the smooth projective normalization over \(\mathbb F_p\) of
\[
 u v^p+v=-1-2\sum_{i=1}^{n}u^{a_i},\qquad
 a_i=\frac{p^{2i}-1}{2(p-1)}.
\]
Write \(\delta=1\) if \(p\mid(2n+1)\), and \(\delta=0\) otherwise; write \(\epsilon=1\) if \(p\equiv3\pmod4\), and \(\epsilon=0\) otherwise. Then
\[
 \boxed{\#X_{p,n}(\mathbb F_p)=p+1+p\delta\epsilon,}
 \qquad
 \boxed{\#X_{p,n}(\mathbb F_{p^2})=p^2+1+\frac{p(p-1)}2\delta.}
\]
In particular, the first two Frobenius power sums are
\[
 S_1=-p\delta\epsilon,\qquad S_2=-\frac{p(p-1)}2\delta.
\]
Consequently, if \(Z(X_{p,n},T)=P_{p,n}(T)/((1-T)(1-pT))\), the initial coefficients of the Hasse–Weil numerator are
\[
 P_{p,n}(T)=1+p\delta\epsilon T+
 \frac{p^2\delta\epsilon+\frac{p(p-1)}2\delta}{2}T^2+O(T^3).
\]

## Assumptions and scope
All point counts are on the **smooth projective normalization**, not only on the displayed affine plane model. The published construction supplies an absolutely irreducible smooth projective curve of genus \((p^{2n}-1)/4\), with trivial geometric automorphism group and maximality over \(\mathbb F_{p^{4n+2}}\) [1]. None of those published geometric or high-extension assertions is claimed as a new theorem. The new claim concerns the two smallest extension degrees over the prime field, and the corresponding initial zeta coefficients.

## Proof
Put \(B(u)=-1-2\sum_{i=1}^n u^{a_i}\). First account for points omitted by the affine \((u,v)\) chart. For finite \(u\ne0\), no point with \(v=\infty\) can occur: setting \(t=1/v\) yields
\[
 u+t^{p-1}=B(u)t^p,
\]
whose specialization at \(t=0\) forces \(u=0\). At \(u=0\), the affine equation has exactly the smooth point \(v=-1\) (its derivative with respect to \(v\) is \(1\)). The \(t\)-equation also has a distinct smooth point \((u,t)=(0,0)\), because its partial derivative with respect to \(u\) is \(1\) there. It is \(\mathbb F_p\)-rational and has local ramification index \(p-1\) over \(u=0\).

There is exactly one geometric point above \(u=\infty\). Indeed, \(a_n\) is the highest exponent of \(B\), its leading coefficient is nonzero, and \(a_n-1\not\equiv0\pmod p\). The Newton polygon at infinity forces a root valuation \(-(a_n-1)/p\), whose denominator is \(p\); hence the degree-\(p\) morphism is totally ramified there. As it is the unique geometric point in a fiber defined over \(\mathbb F_p\), it too is rational over \(\mathbb F_p\). Thus **exactly two rational points over every extension are absent from the affine chart**, one over \(u=0\) and one over \(u=\infty\).

For \(u,v\in\mathbb F_p\), the affine equation becomes \((u+1)v=B(u)\). All \(p-1\) values \(u\ne-1\) contribute one point each. The value \(u=-1\) contributes \(p\) points exactly when \(B(-1)=0\). Since
\[
 a_i=\frac{p+1}{2}\sum_{j=0}^{i-1}p^{2j},
\]
its parity is the parity of \(i(p+1)/2\). If \(p\equiv3\pmod4\), then \(B(-1)=-1-2n\), which vanishes precisely if \(p\mid2n+1\). If \(p\equiv1\pmod4\), then \(B(-1)\) is \(-1\) for even \(n\) and \(1\) for odd \(n\), so it never vanishes. Including the two off-chart points gives the first formula.

Now let \(K=\mathbb F_{p^2}\) and write \(N(u)=u^{p+1}\). For \(u\in K\), consider the \(\mathbb F_p\)-linear map \(L_u(v)=uv^p+v\). If \(N(u)\ne1\), the map has trivial kernel (for a nonzero kernel vector, \(v^{p-1}=-1/u\) forces \(N(u)=1\)) and is bijective. Hence each of the \(p^2-(p+1)\) elements of \(K\) with norm not equal to \(1\) contributes exactly one affine point.

For \(N(u)=1\), the kernel has \(p\) elements and the image is exactly the one-dimensional \(\mathbb F_p\)-subspace
\[
 \{b\in K:u b^p=b\}.
\]
Set \(w=u^{(p+1)/2}\). Then \(w\in\{1,-1\}\) and, since \(u^{p^2}=u\), the exponent formula gives \(u^{a_i}=w^i\). For \(w=-1\), \(B(u)\) is \(-1\) or \(1\); as \(u\ne1\), this nonzero \(\mathbb F_p\)-element does not satisfy \(uB(u)^p=B(u)\). Therefore these fibers have no points over \(K\). For \(w=1\), \(B(u)=-1-2n\in\mathbb F_p\). If \(p\nmid2n+1\), only \(u=1\) lies in the image condition, contributing \(p\) affine solutions. If \(p\mid2n+1\), then \(B(u)=0\) and all \((p+1)/2\) elements with \(w=1\) contribute \(p\) affine solutions each. Adding these contributions, together with the two off-chart points, yields
\[
 \#X_{p,n}(K)=\bigl(p^2-(p+1)\bigr)+p+\frac{p(p-1)}2\delta+2
 =p^2+1+\frac{p(p-1)}2\delta.
\]
Finally, the Weil point-count identity gives \(S_r=p^r+1-\#X_{p,n}(\mathbb F_{p^r})\); Newton identities imply the formula for the first two coefficients of \(P_{p,n}(T)\).

## Verification
Run `python3 verify_point_counts.py` from the directory containing this file. It uses only Python's standard library, performs exact exhaustive arithmetic in \(\mathbb F_p\) and \(\mathbb F_{p^2}\), and verifies the formulas for \((p,n)=(3,2),(3,4),(3,5),(5,2),(5,3),(7,2),(7,3),(11,2),(11,5)\). It accounts explicitly for the two rational places omitted by the affine chart. Every test reports `CHECK_OK`; the final line is `ALL_EXACT_FIELD_CHECKS_OK`. Finite tests corroborate but do not prove the universal theorem.

## Relationship to prior work
Bartoli, Borges, Timpanella and Zini [1, Theorem 1.3(ii), Proposition 2.1 and Section 6.1] construct exactly these curves, prove their genus, geometric automorphism triviality and maximality over a high extension, and describe ramification at \(u=0\) and \(u=\infty\). The inspected sections do not compute the prime-field and quadratic-extension point counts or the initial Hasse–Weil coefficients. The formulas above are not determined by maximality over \(\mathbb F_{p^{4n+2}}\) alone: that extremality constrains a high Frobenius power, while these formulas distinguish the first two traces. Other geometric studies of maximal curves with few automorphisms, including [2], concern different families. The previously obtained Weierstrass-semigroup computation for these same curves concerns pole orders at infinity, not these rational point counts.

## Limitations
The theorem does not determine point counts for higher small extension degrees or the full zeta numerator. It is restricted to odd primes and integers \(n\ge2\), and makes no claim about a positive-characteristic even-prime analogue. The proof is a direct arithmetic analysis of the new family; independent mathematical audit and exhaustive historical-priority confirmation have not been performed.

## References
[1] D. Bartoli, H. Borges, M. Timpanella, G. Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1 (first posted 2026-10-26), especially Proposition 2.1, Theorem 1.3(ii), Section 6.1. https://arxiv.org/abs/2610.35788

[2] H. Borges, L. Reis, *Maximal Curves with Few Automorphisms*, arXiv:2610.37777v1 (first posted 2026-10-27). https://arxiv.org/abs/2610.37777
