# Exact cubic Fourier blind space and quartic recovery for order-five alternating-sign matrices

## Finding

Let \(\mathcal A_5\) be the set of all fully row- and column-labelled alternating-sign matrices of size \(5\), namely matrices with entries in \(\{-1,0,1\}\), each row and column summing to one and having alternating nonzero signs. There are exactly \(429\) such matrices.

For \(0\le d\le25\), define \(V_d\subseteq\mathbb R^{\mathcal A_5}\) as the linear span of all cell-cylinder functions
\[
  A\longmapsto\prod_{(i,j)\in S}\mathbf1\{A_{ij}=b_{ij}\},
  \qquad S\subseteq[5]\times[5],\quad |S|\le d,
  \quad b\in\{-1,0,1\}^{S}.
\]
Equivalently, after identifying \(-1,0,1\) with the three residues modulo three, \(V_d\) is the restriction of the Fourier-character space on \((\mathbb Z/3\mathbb Z)^{25}\) spanned by characters supported on at most \(d\) cell coordinates.

**The exact ranks are**
\[
  \boxed{\dim V_3=425,\qquad \dim V_4=429.}
\]
Thus the annihilator of every marginal involving at most three cells is exactly four-dimensional; adding all four-cell marginals identifies **every** signed measure, hence every probability distribution, on \(\mathcal A_5\). An explicit integer basis of this blind space is supplied. Its four vectors have \(16,16,134,120\) nonzero coordinates, all coefficients \(\pm1\), and each sums to zero. The two 16-term vectors separately produce pairs of distinct eight-point-supported probability laws with all three-cell marginals equal. The same three-cell observations have full recovery rank for orders two, three and four, so this is their first loss of identifiability among ASM orders up to five.

## Assumptions and scope

Cell positions are labelled; no quotient by row or column permutations, dihedral symmetries or sign changes is taken. All joint cell-value observations for **all** subsets with size at most \(d\) are available. Rank is over \(\mathbb R\), equivalently \(\mathbb C\); computations modulo primes supply rigorous rank lower bounds, not the definition of rank. The statement is about arbitrary distributions supported on the complete finite set \(\mathcal A_5\), not just the uniform distribution and not just the six-vertex partition function.

## Proof

**Complete enumeration.** Each possible row is a \(0,\pm1\) word with odd nonzero length and alternating signs, beginning and ending in \(+1\). Traverse all such rows in order of increasing odd support cardinality, then lexicographic support combinations. Append rows recursively if every column prefix sum stays in \(\{0,1\}\); retain depth-five matrices with all column sums one. This enumerates all and only ASMs, because a column with final sum one and partial sums in \(\{0,1\}\) necessarily has alternating nonzero entries beginning and ending positive. This explicit finite enumeration gives \(429\) distinct matrices. A second enumeration via interlacing monotone triangles independently gives \(429\).

**Rank via a counting Gram matrix.** Let \(F_d\) have one row for each \(A\in\mathcal A_5\) and one column for every joint cell-value cylinder of degree at most \(d\). If \(m(A,B)\) denotes the number of cell positions at which \(A\) and \(B\) agree, its integer Gram matrix satisfies
\[
  (G_d)_{A,B}=(F_d F_d^{\mathsf T})_{A,B}
   =\sum_{k=0}^{d}\binom{m(A,B)}{k}.
\]
Indeed, each common assignment to a \(k\)-element set of positions contributes one precisely when all those positions agree; there are exactly \(\binom{m(A,B)}k\) such sets. Therefore \(G_d\) is positive semidefinite and \(\operatorname{rank}_{\mathbb R}G_d=\dim V_d\). Since the three single-site indicator functions and the three one-site characters both form bases of all functions on \(\mathbb Z/3\mathbb Z\), the spans of all interactions of degree at most \(d\) coincide, as claimed above.

**Lower bound and annihilator certificate at degree three.** The complete integer matrix \(G_3\), constructed by the formula, has rank \(425\) over \(\mathbb F_{101}\), as checked by exact modular Gaussian elimination in `verify_asm.py`. Hence a \(425\)-minor is a nonzero integer, and \(\operatorname{rank}_{\mathbb R}G_3\ge425\). The separate `kernel_certificate.json` lists four vectors by integer row indices in the stated enumeration order. Direct exact integer multiplication shows \(G_3v=0\) for every vector. Their coordinates at indices \(279,321,344,428\) form the identity matrix, so they are linearly independent over \(\mathbb Z\). Thus \(\operatorname{rank}_{\mathbb R}G_3\le429-4=425\), proving equality. As \(G_3=F_3F_3^{\mathsf T}\), its kernel equals the kernel of \(F_3^{\mathsf T}\): these vectors annihilate every three-cell marginal, not merely an aggregate quadratic expression.

**Quartic recovery.** The full integer matrix \(G_4\) has rank \(429\) over \(\mathbb F_{101}\) by the same exact elimination, so its integer determinant is nonzero. It therefore has rank \(429\) over \(\mathbb R\), and \(F_4\) determines every signed measure. The independent monotone-triangle checker repeats both rank calculations over \(\mathbb F_{1009}\). For orders two, three and four, exact checks of the analogous degree-three matrices modulo \(101\) give full rank.

**Two explicit probability ambiguities.** Either of the first two signed 16-term kernel vectors contains eight positive and eight negative unit coefficients. Its positive and negative parts, each divided by eight, are different probability measures with identical marginals through degree three. The 134- and 120-term vectors complete the basis and show that these local ambiguities are not the whole kernel.

## Verification

The files `verify_asm.py`, `verify_independent.py` and `kernel_certificate.json` are a complete executable finite certificate. From a directory containing these files, use Python 3 and NumPy and run `python verify_asm.py` and `python verify_independent.py`. Both were executed successfully from their actual final artifact paths. No numerical floating-point rank calculation is needed. A complete finite exhaustive calculation here is a proof of this finite statement, but not a proof for larger orders.

## Relationship to prior work

The classical ASM enumeration theorem supplies the number \(429\), while the six-vertex-model literature studies fixed boundary statistics, multiply refined generating functions and selected two-point correlations. In particular, Behrend's analysis of multiply refined enumeration includes multiple row/column statistics, and Colomo–Pronko calculate two boundary-point correlations. These results establish a substantial background for studying local observables but do not, in the inspected sections, assert the linear rank of all three-cell observations as functions of arbitrary distributions on order-five ASMs. The new claim is a simultaneous full-correlation *identifiability* statement and a complete four-dimensional kernel certificate, not a formula for a selected correlation or an ASM counting formula. Related low-degree reconstruction results on Latin squares and Shidoku concern different state spaces and do not imply these ASM ranks.

## Limitations

The theorem is finite and specific to order five and the stated, fully labelled observation model. No ranks for order six or beyond, no sparsest-basis classification and no sharp conditioning of the Fourier frame are claimed. Published index searches and full-text inspections did not identify a dominating result, but unindexed computational tables, unpublished folklore and deeper implications of general six-vertex correlation formulas remain priority risks; priority is not mathematically certified by a negative search.

## References

1. R. E. Behrend, *Multiply-refined enumeration of alternating sign matrices*, arXiv:1203.3187 (first submitted 2012-03-14), https://arxiv.org/abs/1203.3187. Sections 1, 3.5, 3.6, 4.1 and 4.2.
2. F. Colomo and A. G. Pronko, *On two-point boundary correlations in the six-vertex model with DWBC*, arXiv:math-ph/0503049 (2005), https://arxiv.org/abs/math-ph/0503049. Introduction and boundary-correlation construction.
3. D. Zeilberger, *Proof of the alternating sign matrix conjecture*, Electronic Journal of Combinatorics 3(2), R13, first published 1995-07-25, https://doi.org/10.37236/1271.
4. J. Propp, *The many faces of alternating-sign matrices*, DMTCS Proceedings AA (2001), https://doi.org/10.46298/dmtcs.2292.
