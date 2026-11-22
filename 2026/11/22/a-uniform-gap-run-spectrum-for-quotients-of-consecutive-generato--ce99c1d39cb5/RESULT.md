# A uniform gap-run spectrum for quotients of consecutive-generator numerical semigroups

## Finding

For every pair of integers \(p\ge2\), \(k\ge1\), define the numerical semigroup
\[
Q_{p,k}=\{n\in\mathbb N_0:pn\in\langle pk+1,pk+2\rangle\},
\qquad h=\left\lceil\frac p2\right\rceil.
\]
A *maximal gap run* is an inclusion-maximal nonempty interval of consecutive positive integers outside \(Q_{p,k}\). The entire length spectrum is
\[
\boxed{\mathcal R_{p,k}(z)=z^{hk}+p\sum_{\ell=1}^{k-1}z^\ell.}
\]
Here the coefficient of \(z^\ell\) counts the maximal gap runs of length \(\ell\), including coincident lengths (their multiplicities add). Equivalently, the initial run is exactly \(1,2,\ldots,hk\), and for each \(1\le\ell\le k-1\) there are exactly \(p\) more runs of length \(\ell\); there are no other runs. When \(k=1\), the summation is empty and only the initial run exists. The total number of runs is \(1+p(k-1)\).

The genus and Frobenius number are consequently
\[
\boxed{g(Q_{p,k})=hk+\frac{pk(k-1)}{2}},\qquad
\boxed{F(Q_{p,k})=pk^2-\left(\left\lfloor\frac p2\right\rfloor-1\right)k-1}.
\]
The spectrum itself has a rational bivariate generating function over \(k\):
\[
\sum_{k\ge1}\mathcal R_{p,k}(z)u^k
=\frac{uz^{h}}{1-uz^{h}}+\frac{pu^2z}{(1-u)(1-uz)}.
\]

## Assumptions and scope

The brackets \(\langle a,b\rangle\) mean the additive numerical semigroup of all combinations \(ax+by\) with \(x,y\in\mathbb N_0\). Its quotient by \(p\) means \(\{n\ge0:pn\in\langle a,b\rangle\}\), not division of individual generators. The generators \(pk+1\) and \(pk+2\) are consecutive and hence coprime. All quantifiers are over positive *integers* \(p,k\) in the displayed ranges, including both parities of \(p\) and the boundary \(k=1\). The genus counts missing positive integers; the Frobenius number is their largest.

## Proof

**Integer-interval decomposition.** Write \(a=pk+1\) and \(b=pk+2=a+1\). With exactly \(t\) generators in a representation, the possible sums are \(at,at+1,\ldots,bt\): selecting \(r\) copies of \(b\) and \(t-r\) copies of \(a\) gives \(at+r\) for each \(0\le r\le t\). Accordingly, the quotient semigroup is the union of integer intervals
\[
I_t=\left[kt+\left\lceil\frac tp\right\rceil,\ 
kt+\left\lfloor\frac{2t}p\right\rfloor\right]\cap\mathbb Z,
\qquad t\ge0,
\]
where an interval is empty if its left endpoint exceeds its right. Indeed \(pn\) lies between \(at\) and \(bt\) exactly when \(kt+t/p\le n\le kt+2t/p\).

**Initial gap and nonempty ordered intervals.** For \(1\le t<h=\lceil p/2\rceil\), the interval is empty: \(\lceil t/p\rceil=1\) and \(\lfloor2t/p\rfloor=0\). At \(t=h\), \(I_h\) is nonempty and begins at \(hk+1\). All intervals \(I_t\) with \(t\ge h\) are nonempty. To see this, write \(t=qp+r\) with \(0\le r<p\). If \(q\ge1\), their endpoint difference is
\[
\left\lfloor\frac{2t}p\right\rfloor-
\left\lceil\frac tp\right\rceil
=q+\left\lfloor\frac{2r}p\right\rfloor-\mathbf 1_{r>0}\ge0;
\]
if \(q=0\) and \(t\ge h\), the difference is zero. Both left and right endpoints are strictly increasing in \(t\) since \(k\ge1\). Thus, after \(I_h\), the only possible gaps lie between successive nonempty intervals.

**Exact run lengths.** Let \(L_t\) and \(U_t\) denote the endpoints of \(I_t\). The number of omitted integers strictly between \(I_t\) and \(I_{t+1}\) is the positive part of
\[
 d_t=L_{t+1}-U_t-1
 =k+\left\lfloor\frac tp\right\rfloor-\left\lfloor\frac{2t}p\right\rfloor
 =k-q-\mathbf1_{r\ge h},
\qquad t=qp+r,\quad0\le r<p.
\]
The first equality uses \(\lceil(t+1)/p\rceil=\lfloor t/p\rfloor+1\). For every \(j\in\{1,\ldots,k-1\}\), precisely the \(p\) consecutive indices
\[
(j-1)p+h\le t\le jp+h-1
\]
satisfy \(d_t=k-j>0\). This follows either by splitting at the multiple \(jp\), or directly from the preceding remainder formula. The indices begin at \(t=h\) and terminate at \(t=(k-1)p+h-1\). All later \(d_t\) are nonpositive. Consequently the initial missing interval \([1,hk]\) is maximal and each length \(k-1,k-2,\ldots,1\) occurs exactly \(p\) times, with no later gaps. This proves the claimed spectrum, including the case \(k=1\) when all \(d_t\le0\) from the outset.

**Global invariants.** Summing the lengths of the runs gives \(hk+p\sum_{\ell=1}^{k-1}\ell=hk+pk(k-1)/2\). For \(k=1\), the final missing integer is \(hk=h\). For \(k\ge2\), the last positive gap is after \(I_{(k-1)p+h-1}\); its final element is \(L_{(k-1)p+h}-1\). The same expression also applies at \(k=1\) (then \(L_h-1=hk\)). Since
\[
L_{(k-1)p+h}=k\bigl((k-1)p+h\bigr)+k,
\]
we obtain
\[
F(Q_{p,k})=pk^2-(p-h-1)k-1
=pk^2-\left(\left\lfloor p/2\right\rfloor-1\right)k-1.
\]
Finally, summing \(\mathcal R_{p,k}(z)\) over \(k\ge1\) gives the displayed rational bivariate generating function by two geometric-series identities.

## Verification

Run `python3 CHECK.py` with Python 3 and its standard library. For every \(2\le p\le40\) and \(1\le k\le25\), it tests every integer from 1 through and beyond the predicted conductor. It uses the **independent modular criterion** \(pn\in\langle a,a+1\rangle\) if and only if \(a+1\) times the least nonnegative residue of \(pn\bmod a\) does not exceed \(pn\). It directly enumerates maximal gap blocks and verifies their complete histogram, the starting run, the last gap, total number of runs, Frobenius number, and genus. All 975 parameter pairs and 246,675 complete maximal gap runs pass. These finite experiments corroborate, but do not replace, the proof for arbitrary \(p,k\).

## Relationship to prior work

The quotient construction is standard. Liu's 2023 study develops generating functions and generator descriptions for numerical-semigroup quotients; Cabanillas's 2019 full-text study gives lattice and continued-fraction algorithms for generators, pseudo-Frobenius numbers, Frobenius number, and genus of arbitrary quotients of two-generator semigroups. Adeniran and collaborators give general genus relations in 2018. Those sources provide relevant background and, in broad form, can determine the global invariants appearing here. The distinct contribution claimed is the *entire maximal consecutive-gap run-length frequency distribution*, uniformly in both the quotient modulus and the generator parameter. A related 2026 indexed result classifies isolated gaps in the special modulus-three family and supplies a full Apéry set there; that stronger Apéry information can in principle recover the complete modulus-three gap set, so no separate novelty is asserted for the modulus-three specialization. The claim here is the single explicit all-length frequency law uniform in every integer modulus. No claim is made to inventing quotient semigroups, their interval model, or global genus formulas.

## Limitations

This result covers precisely the two-parameter family \(\langle pk+1,pk+2\rangle/p\). For arbitrary generators or offsets, the same uniform length-frequency law need not hold. The proof is elementary and self-contained; its significance is a motivated exact local gap-spectrum invariant rather than a general new theorem on all quotient semigroups. Previous results may imply particular specializations or yield the formula after nontrivial specialization of general algorithms; no global publication-priority certification is asserted. Some related indexed 2026 work was accessible only through summaries and could not be compared appendix-by-appendix. Independent mathematical validation has not been performed.

## References

- F. Liu, *Generating functions for the quotients of numerical semigroups*, arXiv:2312.10889, first public version 2023-12-18, primary MSC 11D07, https://arxiv.org/abs/2312.10889.
- E. Cabanillas, *Quotients of numerical semigroups generated by two numbers*, arXiv:1904.08240, first public version 2019-04-17, https://arxiv.org/html/1904.08240v2.
- A. Adeniran, S. Butler, C. Defant, Y. Gao, P. E. Harris, C. Hettle, Q. Liang, H. Nam and A. Volk, *On the genus of a quotient of a numerical semigroup*, arXiv:1809.09360, first public version 2018-09-25, https://arxiv.org/abs/1809.09360.
