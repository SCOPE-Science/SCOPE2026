# Exact weight census of pointwise-minimal Roman domination on cycles

## Finding

Let \(C_n\) be the labelled simple cycle on \(n\ge3\) vertices. If \(P_n(z)\) is the weight enumerator of its **pointwise-minimal Roman dominating functions**, then

\[
\boxed{\sum_{n\ge3}P_n(z)x^n =
\frac{x^3z^2\left(3+z+x(z+4z^2)+x^2(6z^2+z^3)+x^3(z^3+z^4)+x^4z^4\right)}
{1-zx-z^2x^3-z^4x^4-z^4x^5}.}
\]

The representation gives the complete polynomial for every cycle order, not just an extremal weight or the unweighted number. Every coefficient in its support is positive, and its exact support is

\[
\boxed{\operatorname{supp} P_n=\{\lceil 2n/3\rceil,\lceil2n/3\rceil+1,\ldots,n\}.}
\]

A direct coefficient formula is available. With the convention \(\binom ab=0\) when \(a<0\), \(b<0\), or \(b>a\), write

\[
\boxed{[z^w]P_n(z)=\mathbf{1}_{\{w=n\}}+
\sum_{\ell=1}^{\lfloor n/3\rfloor}\sum_{s=0}^{\ell}
\frac n\ell\binom\ell s\binom{s}{n-w-\ell+s}
\binom{w-\ell-2s-1}{\ell-1},}
\]

where summands with \(w<2(\ell+s)\) are zero. This formula has nonnegative integer values despite its \(n/\ell\) presentation.

The unweighted specialization, previously present as an abstract integer sequence rather than an identified Roman-domination count, is

\[
\sum_{n\ge3}P_n(1)x^n
=\frac{x^3(4+5x+7x^2+2x^3+x^4)}{1-x-x^3-x^4-x^5}.
\]

Accordingly \(P_n(1)\) for \(n=3,4,\ldots\) begins \(4,9,16,22,36,65,112,186,309,\ldots\). These integers and their rational univariate generating function already appear, after reindexing, in Plouffe's 1992 list of Fielder sequences (A.178). Their *numerical sequence* is explicitly **not** claimed as new. The newly identified object here is the weighted distribution on minimal Roman functions, with its cycle-specific gap classification.

## Assumptions and scope

The cycle \(C_n\), for every integer \(n\ge3\), has vertex labels in \(\mathbb Z/n\mathbb Z\) and edges joining consecutive residues. A Roman dominating function (RDF) is a map \(f:V(C_n)\longrightarrow\{0,1,2\}\) such that each vertex assigned \(0\) has a neighbor assigned \(2\). Its weight is \(w(f)=\sum_v f(v)\). A minimal RDF means **minimal in the pointwise partial order**: no other distinct RDF \(g\) has \(g(v)\le f(v)\) for every vertex. This is not the condition of merely attaining minimum total weight; those are different notions. Define \(P_n(z)=\sum_{f\ \mathrm{pointwise\ minimal}} z^{w(f)}\), counting labelings on the fixed labelled cycle without identifying rotations or reflections. All formal generating-function identities are identities in \(\mathbb Q[z][[x]]\).

## Proof

**1. Pointwise minimality.** Let \(S=\{v:f(v)=2\}\). If \(S=\varnothing\), feasibility requires \(f(v)=1\) at every vertex; this is one minimal RDF, of weight \(n\). Suppose \(S\neq\varnothing\). Any vertex outside \(S\) adjacent to \(S\) must receive \(0\) in a minimal RDF, since replacing its label \(1\) by \(0\) preserves feasibility. Every other outside vertex must receive \(1\), since it lacks a neighbor with label \(2\). Thus \(S\) uniquely determines the labels: \(2\) on \(S\), \(0\) on \(N(S)\setminus S\), and \(1\) elsewhere. The resulting RDF is minimal if and only if every \(v\in S\) has an **open private neighbor** \(u\notin S\) whose only neighboring \(2\)-vertex is \(v\). Necessity follows by reducing \(f(v)\) from \(2\) to \(1\) when no such \(u\) exists. Conversely, any decrease of a \(1\)-vertex makes an undefended \(0\), and any decrease of a \(2\)-vertex leaves its private \(0\) without a neighboring \(2\). All strictly smaller functions perform at least one such decrease and cannot be RDFs.

**2. Cyclic gaps.** List the \(k=|S|\) selected \(2\)-vertices clockwise. Between each selected vertex and the next, let \(g_i\ge0\) be the number of intervening vertices. Then \(\sum_i(g_i+1)=n\). A gap \(g_i\in\{0,1\}\) is *short*; a gap \(g_i\ge2\) is *long*. The private-neighbor condition at the \(i\)-th \(2\)-vertex is exactly that at least one of its two adjacent gaps be long. This is also true for \(k=1\): its unique gap has length \(n-1\ge2\). Therefore a defender set gives a minimal RDF exactly when the circular word of gaps has **no two consecutive short gaps** (including the wraparound pair). There must be at least one long gap.

**3. Block weights and cyclic generating function.** Attach to each selected \(2\)-vertex the clockwise following gap. For a long gap \(g\ge2\), internal positions adjacent to its ends have label \(0\), and the \(g-2\) internal middle positions have label \(1\), so its block contributes \(x^{g+1}z^g\). For a short gap \(g=0\) or \(g=1\), all non-defender positions in the block carry \(0\), so its contribution is \(z^2x^{g+1}\). Thus

\[
L(x,z)=\sum_{g\ge2}x^{g+1}z^g=\frac{z^2x^3}{1-zx},\qquad S(x,z)=z^2(x+x^2).
\]

The two-state transition matrix \(T=\begin{pmatrix}L&S\\L&0\end{pmatrix}\) records long and short successive blocks. Hence \(\operatorname{tr}(T^k)\) enumerates length-\(k\) cyclic words of valid blocks, with a distinguished starting block; it excludes consecutive short blocks. Each labelled minimal RDF with \(k\) defenders is represented by exactly \(k\) choices of first defender and \(n\) possible vertex positions for that choice, giving the factor \(n/k\). In particular, periodic gap words require no separate symmetry correction: both the choices of distinguished defender and starting position count their true multiplicities. Thus

\[
P_n(z)=z^n+n[x^n]\sum_{k\ge1}\frac{\operatorname{tr}(T^k)}{k}.
\]

The formal trace-log identity and determinant evaluation give

\[
\sum_{k\ge1}\frac{\operatorname{tr}(T^k)}k
=-\log\det(I-T)
=\log\frac{1-zx}{1-zx-z^2x^3-z^4x^4-z^4x^5}.
\]

Both this logarithm and \(z^n\) have no terms of length below three in the relevant proper cases. Summing over \(n\ge3\) and applying \(x\partial_x\) therefore gives

\[
\sum_{n\ge3}P_n(z)x^n
=\frac{(zx)^3}{1-zx}
+x\partial_x\log\frac{1-zx}{1-zx-z^2x^3-z^4x^4-z^4x^5}.
\]

Combining the two terms, using the common denominator \(1-zx-z^2x^3-z^4x^4-z^4x^5\), and simplifying gives exactly the displayed rational generating function. The numerator is divisible by \(x^3\), so the identity contains no terms of cycle order below three. This calculation is a formal-series identity and does not use an asymptotic approximation.

**4. Coefficients.** Suppose there are \(\ell\ge1\) long gaps and \(s\in\{0,\ldots,\ell\}\) short gaps. Let \(b\) of these short gaps have length one, and let \(H\ge0\) be the total additional length beyond two in all long gaps. Then the total cycle length and RDF weight are

\[
n=3\ell+H+s+b,\qquad w=2(\ell+s)+H,
\]

so \(b=n-w-\ell+s\). The number of legal circular long/short arrangements with a distinguished first block is \((\ell+s)\binom\ell s/\ell\), since each of the \(\ell\) long gaps can host at most one short gap after it. Short-gap type choices contribute \(\binom sb\). Distributing \(H=w-2(\ell+s)\) over the \(\ell\) long gaps contributes \(\binom{H+\ell-1}{\ell-1}\). Multiplying by \(n/(\ell+s)\) for labelled cycles proves the stated explicit coefficient formula.

**5. Exact weight support.** Every RDF obeys \(n\le3|S|+|V_1|\le(3/2)w(f)\), since the \(2\)-vertices collectively cover at most three vertices each, while label \(1\) accounts for one additional vertex each. Thus \(w\ge\lceil2n/3\rceil\). The all-one labeling has weight \(n\). For a minimal RDF with long gaps \(\ell\) and short gaps of lengths zero and one, with counts \(a,b\), the preceding formulas give \(n-w=\ell-a\ge0\), since each short gap is separated by a long one. Conversely, for each integer \(j\in\{1,\ldots,\lfloor n/3\rfloor\}\), take \(j\) defender vertices spaced so that all gaps have at least two intervening vertices. The resulting minimal RDF has \(n-w=j\). Together with the all-one RDF this supplies every weight in the claimed interval, with no intermediate holes.

**6. Total count and asymptotics.** Setting \(z=1\) gives the rational univariate specialization. For \(n\ge3\), the logarithmic formula at \(z=1\) also yields

\[
P_n(1)=n[x^n]\left[-\log(1-x-x^3-x^4-x^5)\right],
\]

and hence \(P_n(1)=\sum_{j=1}^5\lambda_j^n\), where the \(\lambda_j\) are the roots, with multiplicity, of \(\lambda^5-\lambda^4-\lambda^2-\lambda-1=0\). Its companion matrix is nonnegative, irreducible, and primitive (positive recurrence steps of lengths one, three, four, five), so the positive Perron root \(\alpha=1.685137110165\ldots\) strictly dominates the other roots. Consequently \(P_n(1)\sim\alpha^n\), with leading constant exactly \(1\). This unweighted number sequence is independently present in the 1992 Plouffe table; its numerical values and algebraic recurrence are **not** novelty claims here.

## Verification

The standalone standard-library script `verify.py` checks the theorem independently in three ways. It tests **all** \(3^n\) labelings for \(3\le n\le11\) directly for feasibility and pointwise minimality, independently tests **all** \(2^n\) candidate defender sets for \(3\le n\le18\) against the private-neighbor construction, and checks the coefficient formula against the rational generating function through \(n=45\). It also checks the exact support and total-count recurrence through \(n=65\). Successful execution prints:

`VERIFY_OK bruteforce_labelings_n=3..11 265707 independent_defender_subsets_n=3..18 524280 explicit_coefficients_n=3..45 1075 recurrence_and_support_n=3..65 PASS`

Sample polynomials are \(P_3(z)=3z^2+z^3\), \(P_4(z)=4z^3+5z^4\), \(P_5(z)=10z^4+6z^5\), and \(P_9(z)=3z^6+36z^7+54z^8+19z^9\). Finite tests corroborate the formula; the proof above establishes all cycle orders.

## Relationship to prior work

Abu-Khzam, Fernau, and Mann (2022, arXiv:2204.04765) established the general pointwise-minimal RDF definition and the private-neighbor characterization. In particular their exact total of 16 minimal RDFs on \(C_5\) is preexisting and is **not** a novel result. Their paper does not state the bivariate cycle polynomial above.

The follow-up *Roman Census* (arXiv:2208.05261) develops enumerations on **paths**, not an all-weight cycle enumeration; its conclusion explicitly identifies other simple graph classes as unexplored. The present argument specializes the general minimality criterion but derives the cycle gap-word encoding, weighted polynomial, explicit coefficient formula and full weight support.

Deepak, Alwardi, and Indiramma (2021), *Roman Domination Polynomial of Cycles*, computes \(R(C_n,z)\) for **all** Roman dominating functions, not just pointwise-minimal ones. The polynomial of all RDFs does not equal \(P_n(z)\); only the minimum-weight coefficient must agree. Their previously known values for \(\gamma_R(C_n)\) and counts of minimum-weight RDFs are therefore not claimed as new.

Plouffe's 1992 generating-function compilation contains the univariate sequence \(1,1,4,9,16,22,36,65,112,\ldots\), entry A.178, with denominator \(1-x-x^3-x^4-x^5\). Our \(P_n(1)\), starting at \(n=3\), equals that known sequence starting at the entry \(4\). This match is fully disclosed: the **existing integer sequence and univariate recurrence are prior art**. No Roman-cycle or bivariate coefficient interpretation was found in the inspected entry. An unindexed equivalent bivariate result remains possible.

## Limitations

The theorem concerns labelled simple cycles only and pointwise-minimal RDFs under the precise coordinatewise order; no extension to paths, cycle powers, other Roman variants, or unlabelled orbits is claimed. The minimum weight and the numerical total-count sequence are already known independently, as explained above. The 2021 all-RDF paper's indexed primary text was inspected, but a page-image retrieval returned HTTP 403, leaving some residual comparison risk. Literature and indexed-record searches cannot certify exhaustive priority. Verification is finite and does not replace the unrestricted proof. No independent mathematical audit has been performed.

## References

1. F. N. Abu-Khzam, H. Fernau, K. Mann, *Minimal Roman Dominating Functions: Extensions and Enumeration*, arXiv:2204.04765, first posted 2022-04-10. https://arxiv.org/abs/2204.04765
2. F. N. Abu-Khzam, H. Fernau, K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261, first posted 2022-08-10. https://arxiv.org/abs/2208.05261
3. Deepak G., A. Alwardi, M. H. Indiramma, *Roman Domination Polynomial of Cycles*, International J. Math. Combin. 2021(3), 86–97 (2021). https://fs.unm.edu/IJMC/Roman_Domination_Polynomial_of_Cycles.pdf
4. S. Plouffe, *Approximations de séries génératrices et quelques conjectures*, master's thesis, Université du Québec à Montréal, August 1992, Appendix A, entry A.178 (Fielder sequence). https://oeis.org/A000051/a000051_2.pdf
