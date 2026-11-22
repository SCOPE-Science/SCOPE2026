# Complete nilpotent Jordan multiplicities in finite-field hook centralizers

## Finding

Let \(q\) be any prime power and \(n\ge3\). Fix \(N=J_n(0)\oplus J_1(0)\) over \(\mathbb F_q\), and let \(\mathcal C^{\mathrm{nil}}_{n,q}\) denote the nilpotent matrices commuting with \(N\). **Every prescribed nilpotent Jordan partition has an exact multiplicity**, computable from the finite rank-profile table below, without field-characteristic exceptions. The table gives a complete closed arithmetic census for every \(n,q\), with coincident partitions combined by addition. In total,
\[
\#\mathcal C^{\mathrm{nil}}_{n,q}=q^{n+1}.
\]

For \(1\le s\le n-2\) set \(F_s=(q-1)q^{n-s-1}\). To read the table, a row specifies the rank profile \((r_0,r_1,r_2,r_3,\ldots)\) of \((I,X,X^2,X^3,\ldots)\), and its multiplicity among matrices \(X\). In every row \(r_0=n+1\); unless specified otherwise, \(r_k=\max(n-ks,0)\) for all \(k\ge3\).

| Condition | \(r_1\) | \(r_2\) | Multiplicity |
|---|---:|---:|---:|
| \(1\le s\le n-2,\ 2s<n-1\) | \(n-s\) | \(n-2s\) | \(F_s q^2\) |
| \(1\le s\le n-2,\ 2s=n-1\) | \(n-s\) | \(1\) | \(F_s(q^2-q+1)\) |
| \(1\le s\le n-2,\ 2s=n-1\) | \(n-s\) | \(0\) | \(F_s(q-1)\) |
| \(1\le s\le n-2,\ 2s>n-1\) | \(n-s\) | \(1\) | \(F_s(q-1)^2\) |
| \(1\le s\le n-2,\ 2s>n-1\) | \(n-s\) | \(0\) | \(F_s(2q-1)\) |

Additionally, with all powers beyond the final displayed rank equal to zero, there are exactly three residual profiles:
\[
\begin{array}{c|c|c}
\text{partition}&(r_0,r_1,r_2,r_3,\ldots)&\text{multiplicity}\\\hline
(1^{n+1})&(n+1,0,0,\ldots)&1\\
(2,1^{n-1})&(n+1,1,0,\ldots)&(q-1)(2q+1)\\
(3,1^{n-2})&(n+1,2,1,0,\ldots)&q(q-1)^2
\end{array}
\]

The table determines a partition uniquely by taking the multiplicity of blocks of length \(j\) to be
\[
\mu_j=r_{j-1}-2r_j+r_{j+1}.
\]
Add multiplicities whenever two rows or a residual profile yield the same partition. All positive counts and no other partitions occur. Thus the theorem specifies exact labeled-matrix cardinalities, rather than only which Jordan shapes occur.

For example, at \(n=5,q=3\), the partition-count pairs are \((5,1):486\), \((3,2,1):126\), \((3,1,1,1):36\), \((2,2,2):36\), \((2,2,1,1):30\), \((2,1,1,1,1):14\), and \((1^6):1\), summing to \(3^6\).

There is also an exact limiting Jordan-block law. For \(n\ge4\), a uniform random \(X\in\mathcal C^{\mathrm{nil}}_{n,q}\) has Jordan type \((n,1)\) with probability exactly \(1-q^{-1}\). With \(q\) fixed and \(L_n\) the largest Jordan block length of \(X\),
\[
\frac{L_n}{n}\ \xrightarrow[n\to\infty]{\mathrm{law}}\ \frac1S,
\qquad \Pr(S=s)=(q-1)q^{-s}\quad(s=1,2,\ldots),
\]
so \(\lim_{n\to\infty}\mathbb E[L_n/n]=(q-1)\log(q/(q-1))\).

## Assumptions and scope

The field is any \(\mathbb F_q\) (not necessarily of prime order), \(n\) is an integer at least three, and \(J_n(0)\) is a single nilpotent Jordan block. A matrix is counted once for every actual choice of its entries in the **fixed** centralizer; this is not a count of orbits modulo conjugacy. The claim includes all nilpotent commuting matrices, not just square-zero elements, and does not require semisimplicity or a characteristic-zero assumption. Jordan partitions have total size \(n+1\).

## Proof

**(1) The commutant and its nilpotent locus.** Put \(R=\mathbb F_q[t]/(t^n)\), \(M=R\oplus\mathbb F_q\), and let \(N\) act by multiplication by \(t\) on \(M\). Since \(\operatorname{End}_R(R)=R\), \(\operatorname{Hom}_R(\mathbb F_q,R)=t^{n-1}\mathbb F_q\), and \(\operatorname{Hom}_R(R,\mathbb F_q)=\mathbb F_q\) via evaluation at zero, every commuting endomorphism has unique coordinates
\[
X(f,a,b,c)(P,z)=(f(t)P+a t^{n-1}z,\ bP(0)+cz),\quad
f\in R,\ a,b,c\in\mathbb F_q.
\]
The subspace \(tR\) is \(X\)-stable; on it the only possible eigenvalue is \(f(0)\), while on the two-dimensional quotient \(M/tR\) the induced matrix is triangular with diagonal \(f(0),c\). Thus \(X\) is nilpotent if and only if \(f(0)=c=0\). There are \(q^{n-1}\) such polynomials and independently \(q^2\) choices for \(a,b\), establishing the total \(q^{n+1}\).

**(2) Powers.** Henceforth \(f(0)=c=0\), and write \(s=v_t(f)\in\{1,\ldots,n\}\), setting \(s=n\) if \(f=0\). Multiplying the displayed block operators gives
\[
X^2(P,z)=((f^2+ab\,t^{n-1})P,0),\qquad
X^k(P,z)=(f^kP,0)\quad(k\ge3).
\]
Here \(t^{n-1}P=P(0)t^{n-1}\). The off-diagonal terms vanish from the square because \(f(0)=0\); in higher powers the correction is annihilated by multiplication by \(f\) or by \(t^{n-1}\). Consequently, for all \(k\ge3\), \(\operatorname{rank}X^k=\max(n-ks,0)\).

**(3) First two ranks.** Suppose \(1\le s\le n-2\). The image of \(X\) on \(tR\) is \(t^{s+1}R\), of dimension \(n-s-1\). The image of \((1,0)\) has \(t^s\)-coefficient nonzero, so adds one dimension; the image of \((0,1)\) belongs to the already spanned \(t^{s+1}R\). Therefore \(\operatorname{rank}X=n-s\). Now \(X^2\) is multiplication by the polynomial \(f^2+ab\,t^{n-1}\) on \(R\), and zero on \(\mathbb F_q\). If \(2s<n-1\), its valuation is \(2s\) and its rank is \(n-2s\). If \(2s=n-1\), its only potentially nonzero coefficient is \(f_s^2+ab\), where \(f_s\in\mathbb F_q^\times\) is the coefficient of \(t^s\). If \(2s>n-1\), its only potentially nonzero coefficient is \(ab\). Thus its rank is zero or one in the latter cases, precisely as given in the table.

**(4) Counting the central correction.** There are \(F_s=(q-1)q^{n-s-1}\) polynomials of valuation exactly \(s\). When \(2s<n-1\), \(a,b\) are arbitrary, accounting for \(F_s q^2\) elements. When \(2s=n-1\), the equation \(ab=-f_s^2\) has exactly \(q-1\) solutions, because its right-hand side is nonzero; the complementary \(q^2-q+1\) pairs yield rank one. When \(2s>n-1\), the equation \(ab\ne0\) has \((q-1)^2\) solutions, and \(ab=0\) has \(2q-1\) solutions. No characteristic restrictions enter these counts.

**(5) The final two polynomial-valuation strata.** For \(s=n-1\), \(f=f_{n-1}t^{n-1}\) with \(f_{n-1}\ne0\). The images \(X(1,0)=(f_{n-1}t^{n-1},b)\) and \(X(0,1)=(a t^{n-1},0)\) are independent exactly when \(ab\ne0\). If independent, \(X^2\) has rank one, hence the Jordan partition is \((3,1^{n-2})\); otherwise the rank is one with square zero, yielding \((2,1^{n-1})\). For \(s=n\), so \(f=0\), the images of these two basis vectors have ranks determined by the nonzero values of \(a,b\). If both are nonzero, the same rank-two, square-rank-one profile arises; if exactly one is nonzero, one gets rank-one square-zero; if both vanish, one gets zero. Combining the \(s=n-1\) contributions \((q-1)(q-1)^2\) and \((q-1)(2q-1)\) with those of \(s=n\) gives the three residual counts exactly \(q(q-1)^2\), \((q-1)(2q+1)\), and \(1\).

**(6) Jordan reconstruction and exhaustiveness.** Any nilpotent operator with Jordan-block multiplicity \(\mu_j\) satisfies \(\operatorname{rank}X^k=\sum_{j>k}(j-k)\mu_j\). Taking successive second differences recovers \(\mu_j=r_{j-1}-2r_j+r_{j+1}\). The valuation strata above partition every nilpotent commuting matrix without overlap, and all listed coordinate conditions are attainable over every field. Therefore the table determines, by addition of weights for duplicate rank sequences, the exact cardinality of every Jordan type and vanishes outside this list. As a sum check, the strata yield \(q^2(q^{n-1}-1)+q^2=q^{n+1}\).

**(7) Limiting law.** Under the uniform distribution, \(f\) is uniform among polynomials in \(tR\). Thus for each fixed \(s<n\), \(\Pr(v_t(f)=s)=(q-1)q^{-s}\), and \(\Pr(f=0)=q^{-(n-1)}\). When \(s=1\) and \(n\ge4\), the first row gives the partition \((n,1)\), so its probability is \((q-1)/q\). For each fixed \(s\), as \(n\to\infty\), the ranks from the power formula have nilpotency index \(\lceil n/s\rceil\) (once this exceeds three); therefore \(L_n/n\to1/s\) on that event. The geometric tail \(\Pr(s>K)=q^{-K}\) is uniform in \(n>K\), proving distributional convergence. Because \(0\le L_n/n\le (n+1)/n\) is uniformly bounded, expectation converges to \((q-1)\sum_{s\ge1}q^{-s}/s=(q-1)\log(q/(q-1))\).

## Verification

The standalone `checker.py` enumerates all \(q^{n+1}\) choices \((f,a,b)\) in each tested centralizer, constructs the actual \((n+1)\)-dimensional matrix, computes every power and its rank using finite-field elimination, checks the rank-profile formula case-by-case, and aggregates independently determined partitions against the closed table. It uses only Python's standard library and constructs \(\mathbb F_4\) and \(\mathbb F_9\) via irreducible quadratic polynomials. Reproduce from the accompanying files using `python checker.py`; `checker_output.txt` records the completed run. The result was 113,305 matrices in 19 exhaustive field-size configurations, including \(q=2,3,4,5,7,9\) and \(3\le n\le7\). These finite checks are consistency evidence; steps (1)–(7) prove all prime powers and all \(n\ge3\).

## Relationship to prior work

Britnell–Wildon's 2010 preprint studies commuting similarity classes and, in its two-part-partition analysis, develops centralizer coordinates and rank-profile arguments for support. These classical ingredients are credited; the new claim is not a new classification of which pairs of types commute, but rather the explicit **finite-field cardinality of every nilpotent Jordan fiber** in the fixed hook centralizer, for each field size and dimension. Khatami–Košir (2026) classifies possible Jordan types commuting with general hook partitions, a broader *support* statement but not an evaluated all-type finite-field multiplicity law; that work is expressly not being displaced. The published study *Parity geometry and rank census in hook nilpotent centralizers* supplies the complete square-zero rank subcase, which is therefore known prior work and not claimed independently. The present table incorporates that subcase while evaluating every non-square-zero stratum, a different quantitative assertion. Other cited centralizer studies concern generic partitions or other fixed Jordan types. Source identifiers and scope comparisons appear in `AUDIT.json`.

## Limitations

This counts labeled matrices within a fixed centralizer; it does not determine simultaneous-similarity orbit counts, scheme structure, or a formula for an arbitrary fixed Jordan partition. The 2010 and 2026 support results make this computation approachable, so an unindexed Hall-polynomial identity or independent full-fiber census could supersede historical originality. The limiting law concerns only the maximal Jordan block length, not joint fluctuations of all block sizes. No independent mathematical audit or proof assistant certification has been performed.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811v1, publicly submitted 2010-01-06; subsequently *J. Lond. Math. Soc.* 83 (2011), 470–492, DOI:10.1112/jlms/jdq088. https://arxiv.org/abs/1001.0811
2. L. Khatami and T. Košir, *Jordan types commuting with a hook partition*, arXiv:2605.27692v1, 2026-05-26. https://arxiv.org/abs/2605.27692
3. *Parity geometry and rank census in hook nilpotent centralizers*, published mathematical research record, 2026-10-26, record identifier `50a5542dfb83`; available in the public published-finding corpus 2026 collection. https://github.com/published-finding corpus/2026
4. R. Basili, A. Iarrobino, and L. Khatami, *Commuting nilpotent matrices and Artinian algebras*, *J. Commut. Algebra* 2 (2010), 295–325, DOI:10.1216/JCA-2010-2-3-295.
5. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, *Linear Algebra Appl.* 690 (2024), 59–90, DOI:10.1016/j.laa.2024.03.008.
