# Borel-stable root-zero strata of maximal-order elements just beyond a unitriangular exponent threshold

## Finding

Let \(p\) be prime, \(k\ge1\), \(r=p^k\), \(n=r+2\), and let \(K\) be any field of characteristic \(p\). For \(g=I+N\in UT_n(K)\), put \(a_i=N_{i,i+1}\) for \(1\le i\le r+1\) and \(Z(g)=\{i:a_i=0\}\). The subset \(Z(g)\) is invariant under conjugation by the full upper-triangular invertible group.

The group \(UT_n(K)\) has exponent \(p^{k+1}\) in the sense that every element has order dividing that number and some have exactly that order. For a fixed zero pattern \(Z\subseteq\{1,\dots,r+1\}\), the locus of elements of order exactly \(p^{k+1}\) is **precisely** one of the following, with the remaining matrix coordinates arbitrary:

1. **Entire zero-pattern stratum:** \(Z=\varnothing\), \(Z=\{1\}\), or \(Z=\{r+1\}\).
2. **Complement of one linear hyperplane in the second-superdiagonal coordinates, fiberwise over each permitted choice of nonzero \(a_i\):** \(Z=\{j\}\) with \(2\le j\le r\), or \(Z=\{j,j+1\}\) with \(1\le j\le r\).
3. **Empty:** all other zero patterns.

In case 2, if \(b_j=N_{j,j+2}\) and an empty product equals one, the excluded hyperplane is explicitly
\[
\sum_{j=1}^{r}\left(\prod_{i=1}^{j-1}a_i\right)b_j\left(\prod_{i=j+2}^{r+1}a_i\right)=0.
\]
For each fixed first superdiagonal in case 2, this is a *nonzero* linear form in the \(r\) variables \(b_1,\ldots,b_r\), hence a genuine codimension-one hyperplane over **any** field. This classification is geometric/coordinate-stratified, not only a global Jordan-type count.

If \(K=\mathbb F_q\), the fraction of maximal-order elements within a zero-pattern stratum is respectively \(1\), \(1-q^{-1}\), or \(0\) in cases 1, 2, and 3. Consequently, for a uniform element of \(UT_{r+2}(\mathbb F_q)\),
\[
\boxed{\Pr(\operatorname{ord}(g)=p^{k+1})=(1-q^{-1})^r(1+r q^{-1}+q^{-2}).}
\]
The exact number of such elements is \(q^{\binom{r+2}{2}-r-2}(q-1)^r(q^2+rq+1)\). At the immediately preceding dimension \(r+1\), the corresponding maximal-order probability is \((1-q^{-1})^r\), which isolates the first new second-superdiagonal effect.

## Assumptions and scope

\(UT_n(K)\) denotes the group of upper triangular matrices over \(K\) with all diagonal entries one. A first-superdiagonal zero-pattern stratum prescribes which \(a_i\) vanish and requires every other \(a_i\) to be nonzero; all remaining entries are free. The root coordinate nomenclature refers to the simple roots in the standard type-\(A\) Borel group. The finite probability statements require \(q=p^e\), \(e\ge1\). The order and geometric statements work over arbitrary characteristic-\(p\) fields. Here \(r=p^k\ge2\) and \(n=r+2\) throughout.

## Proof

**Exponent boundary.** For \(g=I+N\) in characteristic \(p\), \((I+N)^{p^h}=I+N^{p^h}\). A strictly upper triangular \(n\)-by-\(n\) matrix satisfies \(N^n=0\). Since \(r<n=r+2\le pr=p^{k+1}\), every \(g\) has order dividing \(p^{k+1}\), and it has exact order \(p^{k+1}\) if and only if \(N^r\ne0\). The matrix with all first-superdiagonal entries one has \(N^r\ne0\), proving the exponent assertion.

**Only three potentially nonzero entries.** The \((i,j)\)-entry of \(N^r\) is the sum of products along strictly increasing paths \(i=i_0<i_1<\cdots<i_r=j\). Such a path requires \(j-i\ge r\). With \(n=r+2\), only the positions \((1,r+1)\), \((2,r+2)\), and \((1,r+2)\) can be nonzero. Let \(a_i=N_{i,i+1}\) and \(b_i=N_{i,i+2}\). The first two positions are
\[
A=\prod_{i=1}^r a_i,\qquad B=\prod_{i=2}^{r+1}a_i.
\]
The third position has total displacement \(r+1\) along exactly \(r\) steps, hence *exactly one* step has length two and all remaining steps have length one. It equals
\[
C=\sum_{j=1}^r\left(\prod_{i<j}a_i\right)b_j\left(\prod_{i>j+1}a_i\right).
\]
No higher superdiagonal enters the order test.

**Zero-pattern classification.** The condition \(A\ne0\) means \(Z\subseteq\{r+1\}\); \(B\ne0\) means \(Z\subseteq\{1\}\). This gives exactly the three full strata in case 1. If \(A=B=0\), the coefficient of \(b_j\) in \(C\) is nonzero exactly when all zeros in \(Z\) lie in \(\{j,j+1\}\). Under \(A=B=0\), this happens exactly for an internal singleton or two consecutive zeros. In those cases the coefficient vector of \(C\) is nonzero, and the surviving order-maximal locus is \(C\ne0\), the complement of its linear hyperplane. If neither type occurs then \(C=0\) identically. These cases exhaust all \(2^{r+1}\) zero patterns.

**Borel invariance.** If \(h\) is upper triangular and invertible with diagonal \((d_1,\ldots,d_n)\), then the first-superdiagonal entry of \(hgh^{-1}-I\) at \((i,i+1)\) is \((d_i/d_{i+1})a_i\). All ratios are nonzero, so \(Z(g)\) is unchanged. Conjugation also preserves element orders.

**Exact finite-field count.** Put \(z=q^{-1}\), \(t=1-z\). For a random first superdiagonal, the chance of case 1 is \(t^{r+1}+2zt^r=t^r(1+z)\). The internal singleton zero patterns have probability \((r-1)zt^r\), and the adjacent-pair patterns have probability \(rz^2t^{r-1}\). For either pattern type the nonzero linear form \(C\) survives with conditional probability \(t\). Thus
\[
\begin{aligned}
\Pr(N^r\ne0)&=t^r(1+z)+t\big((r-1)zt^r+rz^2t^{r-1}\big)\\
&=t^r(1+rz+z^2).
\end{aligned}
\]
Multiplying by \(|UT_n(\mathbb F_q)|=q^{\binom{n}{2}}\) gives the stated integral count. For \(n=r+1\), \(N^r\) has only one possible entry, the product of all \(r\) first-superdiagonal entries, giving the preceding-dimension formula.

## Verification

The standalone \(\texttt{ut_exponent_profile_verify.py}\) enumerates every strictly upper-triangular matrix over the *prime* fields \(\mathbb F_2\) in dimensions \(4,5,6\) and \(\mathbb F_3\) in dimension \(5\). It independently multiplies matrices to test \(N^r\ne0\), checks each individual first-superdiagonal zero-pattern count against the three-case conditional law, and verifies the global count. Prime-power cases include \((p,r,q)=(2,2,2),(2,4,2),(3,3,3)\). The intermediate \((q,r)=(2,3)\) test confirms the underlying arbitrary-\(r\) path-count identity, without asserting a new group-order theorem for that exponent. A successful execution ends with \(\texttt{UT_EXPONENT_ROOT_PATTERN_VERIFIED}\). This finite corroboration does not replace the algebraic proof for all \(p,k,q\).

## Relationship to prior work

Dolfi, Singh and Yadav study images of \(p\)-power maps and large conjugacy classes in unitriangular groups. Their full text does not classify the order-maximal locus **conditional on the simple-root zero pattern**. In particular, a power *image-set* cardinality does not give the sizes or geometry of order-maximal *source-element* strata. Their use of leading-diagonal weights motivates the Borel-invariant formulation.

Yip's complete Jordan-type enumeration for random strictly upper-triangular matrices does determine the **unconditional** number of maximal-order elements by summing Jordan types whose largest part exceeds \(r\). The unconditional formula here is therefore not claimed as a new independent counting invariant. Yip's formula does not provide the first-superdiagonal zero-pattern partition nor the fiberwise hyperplane geometry.

Van Peski's 2024 first-public version gives finite-rank and Jordan-law formulas for unrestricted random triangular matrices, not the Borel-root-conditioned geometry. The previously published uniform first-nonsurjective \(p\)-th-power image result deals with the target image in dimension \(p+3\), rather than the source maximum-order strata at dimension \(p^k+2\). A 2026 preprint of Mallahi-Karai, Ram and Salmasian supplies broad incidence-algebra Jordan-counting machinery potentially capable of **deriving the numeric conditioned counts by inclusion–exclusion**. Hence neither the global count nor abstract computability of the conditional numbers is claimed as novel; the contribution assessed here is the precise Borel-invariant *empty/full/hyperplane-complement* structure uniform in \(p,k,K\). This stronger geometric description is not stated in the inspected works.

## Limitations

No assertion is made for dimensions beyond \(r+2\), arbitrary upper-triangular diagonal entries, or the full conjugacy classification of unitriangular elements. Counts for a fixed zero pattern are over the standard upper-triangular coordinates and are not numbers of Borel conjugacy classes. This is a self-contained group-theoretic stratum description; an equivalent earlier root-support theorem may exist outside inspected sources. The explicit finite tests concern prime fields, and no independent audit has been performed.

## References

1. S. Dolfi, A. Singh, M. K. Yadav, p-Power conjugacy classes in U(n,q) and T(n,q), arXiv:1905.04244 (first posted 2019-05-10), https://arxiv.org/html/1905.04244v1.
2. M. Yip, Rook placements and Jordan forms of upper-triangular nilpotent matrices, arXiv:1703.00057 (first posted 2017-02-28), https://arxiv.org/html/1703.00057v1.
3. R. Van Peski, The rank of a random triangular matrix over F_q, arXiv:2407.19578 (first posted 2024-07-28), https://arxiv.org/abs/2407.19578.
4. Published result, A uniform first-nonsurjective power-image theorem for unitriangular groups in every prime characteristic, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-uniform-first-nonsurjective-power-image-theorem-for-unitriangu--0240d15e6f42.
5. K. Mallahi-Karai, S. Ram, H. Salmasian, Counting Matrices of Prescribed Jordan Type in Incidence Algebras, arXiv:2611.21451 (2026-11-16), https://arxiv.org/abs/2611.21451.
