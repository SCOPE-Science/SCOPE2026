# Odd-power margins of cyclic monomial inverse semigroups

## Finding

Fix any odd integer \(n\geq3\) and any integer \(m\geq1\). Let \(\mu_n\) denote the group of complex \(n\)-th roots of unity and \(\mathcal P_m(\mu_n)\) the inverse monoid of all \(m\times m\) partial monomial matrices with entries in \(\mu_n\) on their nonzero positions, including the zero matrix. For the inverse-semigroup word \(\omega(x)=x^n\), the marginal equivalence relation on this monoid is precisely

\[
 A\sim_{\omega} B\quad\Longleftrightarrow\quad A=\zeta B\text{ for some }\zeta\in\mu_n.
\]

Here the zero matrix has a singleton class. In particular, this equivalence is already a semigroup and inverse-semigroup congruence, so the marginal congruence equals the marginal equivalence. The marginal inverse subsemigroup is

\[
 M_{\omega}(\mathcal P_m(\mu_n))=\{0\}\cup\{\zeta P_I: \varnothing\ne I\subseteq\{1,\ldots,m\},\ \zeta\in\mu_n\},
\]

where \(P_I\) is the diagonal projection with support \(I\). It is normal, and the exact cardinalities are

\[
 \left|M_{\omega}(\mathcal P_m(\mu_n))\right|=1+n(2^m-1),\qquad
 \left|\mathcal P_m(\mu_n)/{\sim_{\omega}}\right|=1+\sum_{r=1}^{m}\binom mr^{\!2}r!\,n^{r-1}.
\]

The oddness hypothesis is essential to this precise scalar-classification conclusion. For \(n=4,m=2\), the two matrices \(I_2\) and \(\operatorname{diag}(i,-i)\) are marginally equivalent for \(x^4\), but are not scalar multiples of one another.

## Assumptions and scope

A partial monomial matrix has at most one nonzero entry in each row and column; products are ordinary matrix products. For \(A,B\) in a semigroup, the power-word marginal equivalence is, by definition, simultaneous equality \((AX)^n=(BX)^n\) and \((XA)^n=(XB)^n\) for every \(X\) in the semigroup. Marginal elements are those equivalent to their support idempotent; this agrees with the inverse-semigroup word definition because a marginal element is completely regular and has a unique associated idempotent, as proved in Araújo–Araújo–Kinyon (2025), Lemma 4. We use the usual convention that the empty support matrix is zero. No commutativity of the whole inverse monoid is assumed. The result is for every odd \(n\ge3\) and all \(m\ge1\); no assertion of the same classification is made for arbitrary even exponents or other coefficient groups.

## Proof

**Step 1: the support maps of equivalent matrices agree.** Suppose \(A\sim_{\omega}B\). Pick a nonzero entry \(A_{ij}\) and let \(X=E_{ji}\), the rank-one matrix unit. Then \(AX=A_{ij}E_{ii}\), so \((AX)^n=E_{ii}\), because \(A_{ij}\in\mu_n\). If \(B_{ij}=0\), then \(BX\) is either zero or a scalar multiple of \(E_{ki}\) with \(k\ne i\), whose square is zero. Hence \((BX)^n=0\), a contradiction. Reversing the roles of \(A,B\), their nonzero positions coincide. Thus they have the same underlying partial permutation.

**Step 2: paired arrows determine all phase ratios.** For each common nonzero position label the coefficient of \(A\) relative to \(B\) by \(\delta_u\in\mu_n\). When their common rank is at least two, select any two arrows \(j_u\mapsto i_u\) and \(j_v\mapsto i_v\). Let \(X\) have exactly the two entries \(X_{j_v,i_u}=X_{j_u,i_v}=1\). Then \(AX\) and \(BX\) consist of one weighted two-cycle on the row indices \(i_u,i_v\). Write \(n=2k+1\). In \((AX)^n\), the coefficient on one of the two arrows differs from the corresponding coefficient of \((BX)^n\) by \(\delta_u^{k+1}\delta_v^k\); on the reverse arrow by \(\delta_v^{k+1}\delta_u^k\). Marginal equivalence requires both ratios to equal \(1\). Dividing yields \(\delta_u=\delta_v\). Because the pair of arrows was arbitrary, all ratios coincide with one \(\zeta\in\mu_n\). For rank one the common ratio is automatic. For rank zero both matrices vanish. Consequently \(A=\zeta B\).

**Step 3: the converse and congruence.** If \(A=\zeta B\) and \(\zeta^n=1\), then for every \(X\) we have \((AX)^n=\zeta^n(BX)^n=(BX)^n\) and the analogous right equality. This proves the characterization. If \(A=\zeta B\) and \(C=\eta D\), then \(AC=\zeta\eta BD\), establishing multiplicative compatibility. Inverse compatibility follows from \((\zeta A)^{-1}=\zeta^{-1}A^{-1}\) for these partial monomial matrices. Thus the equivalence is already a congruence; its congruence closure adds no pairs.

**Step 4: the margin and normality.** By Lemma 6 of Araújo–Araújo–Kinyon (2025), a marginal element centralizes every idempotent. In the partial monomial monoid, commuting with every rank-one diagonal projection forces a matrix to be diagonal. If \(A\) is diagonal, its inverse-semigroup support idempotent \(A^0\) is the diagonal projection \(P_I\) with precisely the same nonzero positions. From Steps 1–3, \(A\sim_{\omega}P_I\) exactly when \(A=\zeta P_I\) for one \(\zeta\in\mu_n\). Conversely every such matrix is marginal by the same equivalence. For every partial monomial \(X\), \(X^{-1}(\zeta P_I)X\) is either zero or \(\zeta P_J\) for a suitable \(J\). Hence the margin is invariant under conjugation and is a normal inverse subsemigroup.

**Step 5: exact count.** The support of rank \(r\) is any partial permutation between an \(r\)-element domain and an \(r\)-element image, yielding \(\binom mr^2r!\) possibilities. Over each support there are \(n^r\) phase assignments. Global multiplication by \(\mu_n\) acts freely on every nonzero rank, so each orbit and marginal equivalence class has exactly \(n\) elements. There are therefore \(n^{r-1}\) classes per rank-\(r\) support, plus the zero class. Each nonempty diagonal support has \(n\) scalar decorations and all are distinct, giving \(1+n(2^m-1)\) marginal elements.

**Step 6: a genuine even boundary.** In \(\mathcal P_2(\mu_4)\) let \(A=\operatorname{diag}(i,-i)\), \(B=I_2\). Both are diagonal of full rank and not global scalar multiples. For every \(X\) with rank at most one, \(AX\) and \(BX\) are either zero, square-zero, or one-point loops with fourth powers equal (each loop phase is a fourth root of unity). For a full-rank diagonal \(X\), both fourth powers are identity. For a full-rank off-diagonal \(X\), the weighted two-cycle in \(AX\) has the same product of its two edge phases as in \(BX\), because \(i(-i)=1\); their fourth powers therefore agree. These cases exhaust the possible \(X\); the same argument applies to \(XA,XB\). Thus \(A\sim_{x^4}B\), proving that oddness cannot simply be dropped.

## Verification

The self-contained script `verify_projective_rook.py` enumerates all partial permutations and phase labelings, implements multiplication as composition of decorated partial maps, computes both sequences of \(n\)-th powers for every possible multiplier, and constructs the actual marginal-equivalence classes from their complete signatures. It compares every class to the predicted global-scalar orbits, counts marginal elements by comparison with support idempotents, and checks the stated even boundary against all 49 matrices in \(\mathcal P_2(\mu_4)\). The recorded results in `verify_projective_rook.out` include exhaustive tests for \((m,n)=(1,3),(2,3),(2,5),(3,3)\), with 352 elements and 118 congruence classes in the largest odd case. These finite computations are independent corroboration, not a substitute for the proof for unbounded \(m,n\).

## Relationship to prior work

Araújo, Araújo and Kinyon (2025) introduced the inverse-semigroup marginal definition, proved basic structural lemmas including the idempotent-centralization property, and explicitly posed the marginal-equivalence/congruence question for power words in their Problem 11. Those definitions, lemmas, and the question are prior results. Brookes (2020) established a far broader classification framework for congruences on partial wreath products \(G\wr\mathcal I_m\), a family containing the monoids studied here; its general description of idempotent-separating congruences is prior. The present specific result identifies which of these congruences is selected by the odd power-word marginal relation, gives its exact fibers, identifies its margin, enumerates the quotient, and detects an even-exponent obstruction. It does not claim a new general theory of all congruences or solve the general inverse-semigroup question.

## Limitations

The result concerns only cyclic phase groups whose order equals the odd power exponent, and all partial monomial matrices of a given degree. It does not classify marginal relations for arbitrary finite groups decorating partial permutations, for even exponents beyond the displayed obstruction, or for arbitrary inverse semigroups. The full literature may contain equivalent statements phrased as scalar/projective congruences rather than marginal equivalences; no exhaustive historical-priority certification is asserted. Independent validation has not been performed.

## References

1. G. Araújo, J. Araújo and M. Kinyon, “Marginal subsemigroups and commutators in inverse semigroups,” *Semigroup Forum* **111** (2025), 351–361. First publicly verified July 7, 2025. DOI: 10.1007/s00233-025-10548-9; https://link.springer.com/article/10.1007/s00233-025-10548-9. Relevant passages: definitions (2)–(3), Lemmas 4 and 6, §5 Problem 11.
2. M. D. G. K. Brookes, “Congruences on the Partial Automorphism Monoid of a Free Group Action,” arXiv:2002.00891 (first posted February 3, 2020), https://arxiv.org/abs/2002.00891. Relevant passages: §2 partial wreath products, §3 congruence decomposition, and §3.8 idempotent-separating congruences.
