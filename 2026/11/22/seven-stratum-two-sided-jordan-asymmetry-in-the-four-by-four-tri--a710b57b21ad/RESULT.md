# Seven-stratum two-sided Jordan asymmetry in the four-by-four triangular algebra

## Finding
Let \(k=\mathbb F_q\) be an arbitrary finite field, and let \(A=T_4(k)\) denote the ten-dimensional algebra of upper-triangular \(4\times4\) matrices. For each element \(x\) of its six-dimensional Jacobson radical \(J\), consider the nilpotent endomorphisms \(L_x:y\mapsto xy\) and \(R_x:y\mapsto yx\) of the **full** regular module \(A\). Let \(m_j^L(x)\) and \(m_j^R(x)\) be the multiplicities of the nilpotent Jordan block of size \(j\) in the respective operators, for \(1\le j\le4\), and put \(\Delta_j=m_j^L-m_j^R\).

The complete Jordan-block discrepancy is determined by \((\Delta_3,\Delta_2)\), because \(\Delta_4=0\) and \(\Delta_1=-3\Delta_3-2\Delta_2\). Precisely **seven** discrepancy pairs occur, with the following exact counts over every finite field, including characteristic two and nonprime fields:

| \((\Delta_3,\Delta_2)\) | Number of \(x\in J\) |
|---|---:|
| \((-1,0)\), \((1,0)\), each | \(q^3(q-1)^2\) |
| \((0,-2)\), \((0,2)\), each | \(q^2(q-1)\) |
| \((0,-1)\), \((0,1)\), each | \(q(q-1)(q^2-q+1)\) |
| \((0,0)\) | \(q(q^5-2q^4+2q^3-2q+2)\) |

Consequently \(L_x\) and \(R_x\) are similar over \(k\) if and only if \((\Delta_3,\Delta_2)=(0,0)\). The exact similarity probability for a uniform radical element is
\[
\boxed{1-\frac2q+\frac2{q^2}-\frac2{q^4}+\frac2{q^5}.}
\]
The seven-stratum law records the *difference* of two full Jordan multiplicity vectors; it does **not** assert that there are only seven individual Jordan types or seven joint pairs of Jordan types. This is the first directed-chain triangular matrix algebra in which a size-three Jordan-block discrepancy is possible: in the three-by-three case the only size-three principal block is common to the left and right actions. The four-by-four case also first permits a size-two block discrepancy of absolute value two.

## Assumptions and scope
Write the radical element uniquely as
\[
x=aE_{12}+bE_{23}+cE_{34}+dE_{13}+eE_{24}+fE_{14},
\qquad a,b,c,d,e,f\in k.
\]
Here \(E_{ij}\) is the standard matrix unit, products are ordinary associative matrix products, and all ten matrix-unit directions of the unital algebra are included in the regular representations. The input element is restricted to \(J\), not an arbitrary upper-triangular matrix with possibly nonzero diagonal. All formulas are exact for every prime-power \(q\). Similarity is similarity of the two \(10\times10\) nilpotent matrices over the specified field.

## Proof
**1. The column/row decompositions.** As vector spaces preserved by left multiplication,
\[
A=\bigoplus_{j=1}^{4}Ae_{jj}.
\]
The summand \(Ae_{jj}\) has basis \(E_{1j},\ldots,E_{jj}\) and the action of \(L_x\) is represented by the leading \(j\times j\) principal submatrix of \(x\). Likewise, right multiplication preserves
\[
A=\bigoplus_{i=1}^{4}e_{ii}A,
\]
with the action on \(e_{ii}A\) represented (under the row-basis convention) by the transpose of the trailing \((5-i)\times(5-i)\) principal submatrix of \(x\). Transposition preserves Jordan block multiplicities. The length-four summands on the two sides are therefore similar to the same nilpotent \(4\times4\) matrix. The one-dimensional summands each contribute a single size-one block. All discrepancies are contributed by the two- and three-dimensional summands.

**2. The three-dimensional block.** A strictly upper-triangular three-dimensional matrix
\[
M=\begin{pmatrix}0&u&w\\0&0&v\\0&0&0\end{pmatrix}
\]
has one size-three Jordan block if \(uv\ne0\), one block of size two and one of size one if \(uv=0\) but \((u,v,w)\ne(0,0,0)\), and three size-one blocks otherwise. Indeed, \(\operatorname{rank}M^2=\mathbf1_{uv\ne0}\); if that rank is zero, \(\operatorname{rank}M=\mathbf1_{(u,v,w)\ne0}\). The leading and trailing three-by-three blocks of \(x\) have successive entries \((a,b,d)\) and \((b,c,e)\), respectively. The size-two leading and trailing blocks have off-diagonal entries \(a\) and \(c\).

Use \(\alpha=\mathbf1_{a\ne0}\), \(\beta=\mathbf1_{b\ne0}\), \(\gamma=\mathbf1_{c\ne0}\), \(\delta=\mathbf1_{d\ne0}\), and \(\epsilon=\mathbf1_{e\ne0}\). The size-three and size-two discrepancies are exactly
\[
\Delta_3=\beta(\alpha-\gamma),
\]
\[
\Delta_2=\alpha+\mathbf1_{\alpha\lor\beta\lor\delta}-\alpha\beta
-\gamma-\mathbf1_{\beta\lor\gamma\lor\epsilon}+\beta\gamma.
\]
Here Boolean disjunction is evaluated in the integers. The final coefficient \(f\) does not enter any discrepancy, since it appears only in the cancelling common length-four block. This argument uses no division, so it is valid in every characteristic.

**3. Enumerate all seven strata.** If \(\beta=1\), then \(\Delta_2=0\) and \(\Delta_3=\alpha-\gamma\). The two nonzero possibilities \(\pm1\) occur when precisely one of \(a,c\) is nonzero. For each sign, choose its nonzero coordinate in \(q-1\) ways, choose \(b\) in \(q-1\) ways, and choose \(d,e,f\) freely. This yields \(q^3(q-1)^2\) elements per sign.

If \(\beta=0\), then \(\Delta_3=0\). Put
\[
\rho(s,t)=\mathbf1_{s\ne0}+\mathbf1_{(s,t)\ne(0,0)}.
\]
Then \(\Delta_2=\rho(a,d)-\rho(c,e)\). The independent pairs \((a,d)\) and \((c,e)\) each have \(1\), \(q-1\), and \(q(q-1)\) choices with \(\rho=0,1,2\), respectively. Therefore the values \(\Delta_2=\pm2\) occur in \(q\cdot 1\cdot q(q-1)=q^2(q-1)\) ways per sign, including the arbitrary \(f\). The values \(\Delta_2=\pm1\) occur in
\[
q\bigl[(q-1)+q(q-1)^2\bigr]=q(q-1)(q^2-q+1)
\]
ways per sign. The remaining stratum is obtained by subtracting the six nonzero discrepancy multiplicities from \(|J|=q^6\), giving \(q(q^5-2q^4+2q^3-2q+2)\). Each nonzero stratum is realized for all \(q\ge2\).

**4. Recover the entire difference.** The length-four Jordan block multiplicities agree because of step 1. Since both operators act on the same ten-dimensional vector space, \(\sum_{j=1}^4 j\Delta_j=0\), which reduces to \(\Delta_1+2\Delta_2+3\Delta_3=0\). Thus the two displayed discrepancies encode the entire four-entry Jordan-type difference; it vanishes exactly for the central stratum. Dividing its cardinality by \(q^6\) proves the similarity probability.

## Verification
The standalone program `check_asymmetry.py` constructs both actual ten-by-ten multiplication matrices in the matrix-unit basis, computes the rank of every power through the fourth, recovers their Jordan partitions from consecutive rank differences, and checks each individual discrepancy against the support formula and the complete distribution. Direct exhaustive checks were completed for all \(2^6=64\), \(3^6=729\), and \(5^6=15625\) radical elements over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). The recorded output is `check_asymmetry.out`; run `python3 check_asymmetry.py`. The checker uses prime-field arithmetic, not an explicit extension-field model. Finite checks are not the basis of the arbitrary-prime-power proof.

## Relationship to prior work
Carroll, Chindris and Lin, *Quiver representations of constant Jordan type and vector bundles*, arXiv:1402.2568v1, give a natural representation-theoretic setting for Jordan types of quiver operators. Their construction studies families of arrow operators on representations, not the two opposite regular multiplication actions of a radical element on \(T_4(k)\), and does not state this seven-stratum distribution. The published *Jordan-type gaps and a motivic transfer census for cyclic Nakayama radicals* classifies both regular actions for Loewy-length-three oriented cyclic quivers and finds that their Jordan types always agree; it does not imply the Loewy-length-four directed-chain asymmetry here. Published finite-field results on embedded centralizers, Lie commutator fibers and associative product fibers of the strictly upper-triangular \(4\times4\) algebra concern commuting equations or prescribed products rather than the two regular Jordan diagrams. Their finite-field coefficients do not give this complete discrepancy census without a separate calculation. The use of Jordan rank formulas and path/matrix-unit decompositions is classical; no novelty is claimed for those tools by themselves. No full historical priority certification is claimed.

## Limitations
The theorem treats one canonical four-vertex directed-chain algebra, not arbitrary quivers or full upper-triangular matrices with arbitrary diagonals. It classifies the complete **difference** between two Jordan multiplicity vectors, not their joint distribution and not conjugacy classes of elements. The numerical checks use prime fields, whereas the elementary proof treats every finite field. An unlocated general theorem on two-sided regular Jordan types may imply this special case; bibliography search and comparison cannot exclude that possibility. The result has not received an independent mathematical audit.

## References
1. Andrew T. Carroll, Calin Chindris and Zongzhu Lin, *Quiver representations of constant Jordan type and vector bundles*, arXiv:1402.2568v1, first posted 2014-02-11, https://arxiv.org/abs/1402.2568 .
2. *Jordan-type gaps and a motivic transfer census for cyclic Nakayama radicals*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-jordan-type-gaps-and-a-motivic-transfer-census-for-cyclic-nakaya--5ebbee94c07d .
3. *Exact embedded-centralizer spectrum of the strictly upper-triangular four-by-four algebra*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-embedded-centralizer-spectrum-of-the-strictly-upper-triang--d23fa671bcf4 .
4. *Three-stratum Lie-bracket fibers and adjoint ranks of strictly upper triangular four-by-four matrices*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-stratum-lie-bracket-fibers-and-adjoint-ranks-of-strictly-u--b92d2e107407 .
5. *Four product-fiber strata in the strictly upper-triangular four-by-four algebra*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-four-product-fiber-strata-in-the-strictly-upper-triangular-4-tim--9ed32ce5752d .
