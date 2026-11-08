# All isolated singular points of elementary symmetric cubic hypersurfaces in characteristic three

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\), let \(n\geq3\), and write \(e_3=\sum_{1\leq i<j<\ell\leq n}x_ix_jx_\ell\). Let \(X_n=V(e_3)\subset\mathbb P_k^{n-1}\). Suppose \(n\not\equiv2\pmod9\), the range in which the published dimension formula makes \(\operatorname{Sing}(X_n)\) zero-dimensional. The **complete geometric support** of its singular scheme is the disjoint union of the following sets of projective points:

1. **Support points:** for every nonempty \(S\subseteq[n]\) with \(|S|\equiv1\pmod9\), the point \(P_S=[x_1:\cdots:x_n]\) with \(x_i=1\) for \(i\in S\) and \(x_i=0\) otherwise.
2. **Signed bipartition points:** when \(n\equiv8\pmod9\), for every unordered proper bipartition \([n]=A\sqcup B\) with \(|A|\equiv|B|\equiv4\pmod9\), the point \(Q_{A|B}\) having coordinates \(1\) on \(A\) and \(-1\) on \(B\); when \(n\equiv5\pmod9\), the same construction with \(|A|\equiv|B|\equiv7\pmod9\). In the other residue classes there are no signed points.

All points are defined over \(\mathbb F_3\). The two families are disjoint, and distinct subsets or unordered bipartitions give distinct points. Consequently, the exact number \(N_n\) of geometric singular points is
\[
N_n=\sum_{\substack{1\leq m\leq n\\m\equiv1\;(\mathrm{mod}\,9)}}\binom nm+\frac12\mathbf1_{n\equiv8\;(\mathrm{mod}\,9)}\sum_{\substack{1\leq a<n\\a\equiv4\;(\mathrm{mod}\,9)}}\binom na+\frac12\mathbf1_{n\equiv5\;(\mathrm{mod}\,9)}\sum_{\substack{1\leq a<n\\a\equiv7\;(\mathrm{mod}\,9)}}\binom na.
\]
For \(n=8\), the singular locus of \(X_8\subset\mathbb P_k^7\) has **exactly \(43\) geometric points**: eight coordinate points and \(35=\frac12\binom84\) signed \((4,4)\)-bipartition points. These are two orbits under coordinate permutations.

## Assumptions and scope
The base field is algebraically closed of characteristic \(3\); in particular, Frobenius cubing is injective. The hypersurface is defined by the degree-three elementary symmetric polynomial with unit coefficients. The statement concerns the support of the reduced singular locus, not the scheme's primary decomposition, local lengths, or analytic types. The excluded congruence class \(n\equiv2\pmod9\) is the known positive-dimensional regime, where partition linear spaces occur.

## Proof
**1. At most two coordinate values.** Write \(e_j\) for the elementary symmetric functions of all \(n\) coordinates. The first derivative in coordinate \(i\) satisfies
\[
\partial_i e_3=e_2-x_i e_1+x_i^2.
\]
At a point where all first derivatives vanish, every coordinate is a root of the monic quadratic \(T^2-e_1T+e_2\). Hence the coordinates assume at most two values, without any assumption about their algebraicity over the prime field.

**2. The one-value case and zero coordinates.** Suppose every coordinate is the same nonzero value \(u\). Then the derivative and equation conditions are respectively \(\binom{n-1}{2}u^2=0\) and \(\binom n3u^3=0\). Modulo three, the first holds for \(n\equiv1,2\pmod3\) and the second for \(n\equiv0,1,2\pmod9\). Under \(n\not\equiv2\pmod9\), their conjunction is \(n\equiv1\pmod9\), giving \(P_{[n]}\).

Now suppose there are two distinct values \(u,v\), with multiplicities \(a,b\geq1\), \(a+b=n\). Since the quadratic in step 1 has roots \(u,v\), we have \(e_1=u+v\), \(e_2=uv\). Comparing this with \(e_1=au+bv\) and the identity \(2e_2=e_1^2-(au^2+bv^2)\), valid in characteristic three, yields
\[
(a-1)u+(b-1)v=0,\qquad (a-1)u^2+(b-1)v^2=0.
\]
Subtracting multiples gives \((a-1)u=0\) and \((b-1)v=0\), as \(u\ne v\). If one value is zero and the other nonzero, its nonzero multiplicity \(m\) must be \(1\pmod3\). The remaining equation is \(\binom m3u^3=0\), which by the base-three binomial coefficient rule is equivalent to \(m\equiv1\pmod9\). Thus exactly the stated support points occur, and their derivative equations also vanish by direct substitution.

**3. Two distinct nonzero values.** In this case \(a\equiv b\equiv1\pmod3\). Put \(h=(a-1)/3\) and \(j=(b-1)/3\), considered modulo three. The characteristic-three identity
\[
(1+uT)^a(1+vT)^b\equiv(1+uT)(1+vT)(1+h u^3T^3+j v^3T^3)\pmod{T^4}
\]
shows that \(e_3=h u^3+j v^3=(h u+jv)^3\). If both \(h,j\) vanished, then \(n\equiv2\pmod9\), excluded. If just one vanished, the displayed equation would force one of \(u,v\) to vanish. If both are nonzero, they are in \(\{1,-1\}\subset\mathbb F_3\). The relation \(h u+jv=0\) has distinct nonzero solutions only when \(h=j\), giving \(v=-u\). If \(h=j=1\) then \(a\equiv b\equiv4\pmod9\), so \(n\equiv8\pmod9\); if \(h=j=-1\) then \(a\equiv b\equiv7\pmod9\), so \(n\equiv5\pmod9\). Conversely, these signed points satisfy the first derivative identities and the cubic equation.

**4. Exhaustion, rationality, and enumeration.** The cases above exhaust every geometric singular point because of step 1. The coordinate sets contain only \(0,1,-1\) after projective scaling, establishing \(\mathbb F_3\)-rationality. A support point has a zero coordinate except possibly \(P_{[n]}\), whose all-equal coordinates cannot equal a genuine signed point. Each signed point determines its unordered partition uniquely, since changing the global sign interchanges the blocks. Thus no listed points coincide except the intentionally identified exchange \(A|B=B|A\). Counting support subsets and dividing ordered bipartitions by two gives the stated formula. At \(n=8\) the only possible support size is one, and the only signed sizes are four and four, yielding \(8+\binom84/2=43\).

## Verification
The standalone file `verify.py` enumerates every \(\mathbb F_3\)-projective point for \(3\leq n\leq11\), evaluates the cubic and gradient directly, and compares the resulting sets with those prescribed by the theorem. All nine comparisons pass, including the \(43\)-point case for \(n=8\). The \(n=11\) check also tests the positive-dimensional boundary (\(34\) rational points across eleven concurrent projective lines), which is outside the theorem's stated domain. The checker prints `CERTIFICATE_OK`. A finite-field census alone is **not** a proof that no further points exist over extensions or for larger \(n\); the quadratic-root and Frobenius argument above proves this for all algebraically closed characteristic-three fields.

## Relationship to prior work
Ying Xie's *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic* (arXiv:2610.00259v1, 24 September 2026) determines the dimension profile and the maximal-dimensional partition components, and expressly leaves smaller-dimensional components unclassified (Theorems 1.1, 1.3 and Section 7). For \(n\not\equiv2\pmod9\), its dimension formula implies finite projective singular support, but neither the exact points nor the signed-orbit count. Orzel's work (arXiv:2509.05009v3) provides bounds and special dimension criteria, not this classification. Cafure–Matera–Privitelli (arXiv:1109.2265) provide the general symmetric-hypersurface partition-space bound, not the stated cubic count. The at-most-two-values step is classical; the new content is the **complete zero-dimensional component classification and the signed congruence strata**.

## Limitations
The theorem excludes \(n\equiv2\pmod9\), does not determine primary or embedded components of the singular scheme, and does not classify local singularity types. Counts are geometric distinct-point counts, not scheme lengths. Full historical priority across all symmetric-cubic literature has not been independently established. No independent mathematical audit has been performed.

## References
1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1, submitted 2026-09-24. https://arxiv.org/abs/2610.00259
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3. https://arxiv.org/abs/2509.05009
3. A. Cafure, G. Matera and M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265. https://arxiv.org/abs/1109.2265
