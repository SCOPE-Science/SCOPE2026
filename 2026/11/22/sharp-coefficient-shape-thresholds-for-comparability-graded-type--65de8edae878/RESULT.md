# Sharp coefficient-shape thresholds for comparability-graded types over disjoint chains

## Finding
Let \(\mathbb P\) be the countable homogeneous universal strict partial order. Fix a finite induced parameter poset \(P\) whose points are individually named, and write \(c_j(P)\) for the number of complete nonalgebraic singleton types \(\operatorname{tp}(x/P)\) in which \(x\) is comparable with exactly \(j\) old points. Define \(C_P(z)=\sum_{j=0}^{|P|}c_j(P)z^j\).

For a disjoint union of \(k\) nonempty chains of sizes \(\ell_1,\ldots,\ell_k\), with no comparisons between different chains,
\[
C_P(z)=2\prod_{i=1}^k(1+z+\cdots+z^{\ell_i})-1+\sum_{i=1}^k\sum_{j=2}^{\ell_i}(j-1)z^j.
\]
For precisely two chains of sizes \(1\le a\le b\), their graded type spectrum is **unimodal if and only if** \(a\le2\) or \(b\le a+1\). It is **log-concave if and only if** \(a=1\) or \((a,b)\in\{(2,2),(2,3)\}\).

Among *all* nonempty disjoint unions of chains, every spectrum with at most seven parameters is unimodal. At eight parameters, the sole nonunimodal unordered chain-size profile is \((3,5)\), with spectrum
\[
C_{(3,5)}(z)=1+4z+8z^2+12z^3+11z^4+12z^5+6z^6+4z^7+2z^8.
\]
All spectra with at most five parameters are log-concave. At six parameters precisely the unordered profiles \((2,4)\) and \((3,3)\) fail log-concavity, with coefficient lists \((1,4,8,8,9,4,2)\) and \((1,4,8,12,6,4,2)\), respectively. Nonunimodal examples exist at every size \(n\ge8\), and non-log-concave examples at every size \(n\ge6\).

## Assumptions and scope
A singleton type is nonalgebraic when the new point is distinct from all named parameters. The named finite poset \(P\) is *induced*: comparabilities within each chain are all those of its linear order, and distinct chains are wholly incomparable. A sequence \((c_0,\ldots,c_n)\) is unimodal if it weakly increases up to some index and then weakly decreases; it is log-concave if \(c_j^2\ge c_{j-1}c_{j+1}\) for every \(1\le j<n\). All coefficients here are positive, so log-concavity implies unimodality. The chain sizes and parameters are unlabelled only when discussing the size-profile classification; the type counts themselves are over **individually named** old points. The case of one chain is included in the generating formula, whereas the shape classification applies specifically to two nonempty chains.

## Proof
**One-point extension classification.** Fix \(x\notin P\). Let \(L=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). A possible type has \(L\) a downward-closed set, \(U\) an upward-closed set, \(L\cap U=\varnothing\), and every member of \(L\) strictly below every member of \(U\). These conditions are necessary by transitivity and sufficient to define a finite strict partial order on \(P\cup\{x\}\); the extension property and ultrahomogeneity of \(\mathbb P\) ensure precisely one complete nonalgebraic type for each pair \((L,U)\).

If \(U=\varnothing\), then \(L\) is a freely chosen prefix of each of the \(k\) chains. The number with \(|L|=j\) is the coefficient of \(z^j\) in \(H(z)=\prod_{i=1}^k\sum_{h=0}^{\ell_i}z^h\). If \(L=\varnothing\), then \(U\) is independently an arbitrary suffix in each chain, giving the same polynomial. These pure cases meet only in the all-incomparable type, so their union contributes \(2H(z)-1\).

If \(L\) and \(U\) are both nonempty, every old point of \(L\) must be below every old point of \(U\). Hence all their elements lie in a *single* chain, because distinct chains have no comparisons. In a chain of length \(\ell\), a mixed type with exactly \(j\) comparable points chooses a nonempty initial prefix of length \(p\) and a nonempty final suffix of length \(q\), with \(p+q=j\). For every \(2\le j\le\ell\), the number of choices is exactly \(j-1\); there are none otherwise. Summing over chains proves the displayed generating function. In particular \(c_0=1\) and the top coefficient is \(c_{|P|}=2\) for two nonempty chains.

**Two-chain coefficients.** For \(1\le a\le b\), the coefficient of \(z^j\) in \((1+\cdots+z^a)(1+\cdots+z^b)\) is \(j+1\) for \(0\le j\le a\), \(a+1\) for \(a<j\le b\), and \(a+b-j+1\) for \(b<j\le a+b\). Adding the mixed corrections therefore gives
\[
c_0=1,\qquad c_j=\begin{cases}
4j,&1\le j\le a,\\
2a+j+1,&a<j\le b,\\
2(a+b-j+1),&b<j\le a+b.
\end{cases}
\]
Empty ranges are ignored (in particular when \(a=b\)). This is an exact closed formula for every grade.

**Unimodality classification.** The first range increases strictly, the second range increases strictly when it is present, and the final range decreases strictly. Hence a decrease followed by an increase can only arise where the first and second ranges meet. If \(a\ge3\) and \(b\ge a+2\), then \(c_a=4a\), \(c_{a+1}=3a+2\) and \(c_{a+2}=3a+3\); thus \(c_a>c_{a+1}<c_{a+2}\), and unimodality fails. Conversely if \(a\le2\), then \(4a\le3a+2\), so no such descent occurs. If \(b\le a+1\), the second interval has length at most one and cannot supply a renewed rise after the first decline. The final range only decreases. This proves both directions.

**Log-concavity classification.** If \(a=1\), the sequence is \((1,4,5,6,\ldots,b+3,2)\) for \(b\ge2\) (and \((1,4,2)\) for \(b=1\)). The middle entries form a positive affine sequence with decreasing adjacent ratios; the first and last boundary inequalities also hold. Direct substitution into the coefficient formula gives log-concavity for \((a,b)=(2,2),(2,3)\).

For \(a=2,b\ge4\), the three consecutive coefficients \((c_2,c_3,c_4)=(8,8,9)\) violate log-concavity at grade three. For \(a\ge3,b\ge a+2\), nonunimodality already implies non-log-concavity. If \(a=b\ge3\), the triple at grades \(a,a+1,a+2\) is \((4a,2a,2(a-1))\), and \((2a)^2<4a\cdot2(a-1)\). If \(b=a+1\) with \(a\ge3\), the triple at grades \(a+1,a+2,a+3\) is \((3a+2,2a,2(a-1))\), and \((2a)^2<(3a+2)\cdot2(a-1)\). These cases exhaust all positive \(a\le b\).

**Sharp first sizes and persistence.** Every unordered nonempty disjoint-chain profile of total size \(n\) is exactly an integer partition of \(n\). The recursive enumeration in `checks/verify.py` lists all such partitions at \(n\le8\) (there are respectively \(1,2,3,5,7,11,15,22\) for \(n=1,\ldots,8\)), and for each uses the exact formula **and an independent enumeration of all ternary new-point relation assignments** with the transitivity constraints above. The complete census shows no nonunimodal profile for \(n\le7\), exactly \((3,5)\) at \(n=8\), no non-log-concave profile for \(n\le5\), and precisely \((2,4),(3,3)\) at \(n=6\). This is an exhaustive finite certificate of the asserted minimality, not an extrapolation from samples. Finally \((3,n-3)\) for every \(n\ge8\) has the valley \(c_3=12>c_4=11<c_5=12\), while \((2,n-2)\) for every \(n\ge6\) has \(c_3^2=8^2<c_2c_4=8\cdot9\). This proves all persistence claims.

## Verification
Run `python3 checks/verify.py` using Python 3 and the standard library. The script independently constructs the strict order on every disjoint-chain profile up to eight points, loops over all \(3^n\) possible new-point relation assignments, rejects precisely those violating transitivity, and compares the resulting grade-count arrays with the generating formula. It exhaustively lists every integer partition of each size from one through eight. It also verifies the two-chain unimodality and log-concavity classifications over the \(3240\) unordered pairs \(1\le a\le b\le80\); these parameter-bounded tests supplement the unrestricted algebraic proof. The exact output concludes `VERIFY_OK`.

## Relationship to prior work
Cameron and Nešetřil (2006, §3, Proposition 3.1) describe the generic homogeneous poset and its finite extension property. A published finite-parameter type-counting analysis establishes the ideal/filter presentation, while a published incomparability-sensitive lower bound (2026) identifies disjoint unions of two chains as its scalar equality class. Its result is an inequality for the **ungraded total** number of types; it does not give their comparability-graded coefficients or coefficient-shape thresholds. Pach et al. (2011, §§1–3) study reducts and extension structure, not these coefficients. Kwiatkowska–Sullivan–Winkel (2025, §2, Theorem 5.1) use valid triples for one-point types to study uniquely extensive embeddings, but do not enumerate finite comparability-graded spectra. A superficially similar unimodality theorem for disjoint unions of chains, reviewed by Knauer–Martínez-Sandoval–Ramírez Alfonsín (2017, §4, Theorem 4.9), concerns the **descent polynomial of linear extensions** or an Ehrhart \(h^*\)-vector. That polynomial is not the one-point comparability enumerator here: the descent enumerator is always unimodal in the stated class, whereas the present type polynomial fails already at sizes \((3,5)\). The proof and quantitative boundaries are therefore not consequences of that literature.

## Limitations
The sharp two-chain classification does not classify unimodality for arbitrary numbers of chains or for arbitrary finite posets. The all-profile size-eight and size-six minimality assertions use a genuinely exhaustive, finite integer-partition census, while the two-chain inequalities and infinite families have symbolic proofs. Independent mathematical validation and complete historical-priority verification have not been performed. The 1984 Simion original mentioned by the 2017 paper was compared through the latter's full-text mathematical description rather than full direct inspection; its descent statistic is distinct, but unindexed equivalent graded-type results remain a residual risk.

## References
1. P. J. Cameron and J. Nešetřil, “Homomorphism-Homogeneous Relational Structures,” *Combinatorics, Probability and Computing* 15 (2006), 91–103, §3, https://doi.org/10.1017/S0963548305007091 (first online 2006-01-03).
2. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz and C. Szabó, “Reducts of the random partial order,” arXiv:1111.7109v1 (2011-11-30), https://arxiv.org/abs/1111.7109.
3. K. Knauer, L. Martínez-Sandoval and J. L. Ramírez Alfonsín, “On lattice path matroid polytopes: integer points and Ehrhart polynomial,” arXiv:1701.05529v1 (2017-01-19), §4, Theorem 4.9, https://arxiv.org/abs/1701.05529.
4. “An incomparability-sensitive lower bound for one-point types of the generic poset,” public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-an-incomparability-sensitive-lower-bound-for-one-point-types-of--00a0cbd4584a.
5. R. Simion, “A multiindexed Sturm sequence of polynomials and unimodality of certain combinatorial sequences,” *Journal of Combinatorial Theory A* 36 (1984), 15–22; discussed in Reference 3, DOI 10.1016/0097-3165(84)90075-X.
6. A. Kwiatkowska, R. Sullivan and J. Winkel, “Embeddings into the generic poset,” arXiv:2502.16695v1 (2025-02-23), §2 and Theorem 5.1, https://arxiv.org/abs/2502.16695.
