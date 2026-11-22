# Sharp extension-defect threshold and rank profiles for finite equivalence relations

## Finding

Let \(E\) be an equivalence relation on a nonempty finite set \(V\), with \(n=|V|\). Write \(m_s\) for the number of its equivalence classes of cardinality \(s\), \(g=\prod_{s\ge1}(s!)^{m_s}m_s!\) for its automorphism-group order, and, if at least two distinct class sizes occur, put
\[
\delta=\min\{|s-t|:s\ne t,\ m_sm_t>0\}.
\]
A *partial automorphism* is an isomorphism between induced substructures on arbitrary subsets of \(V\), and is *extendible* if it is the restriction of an automorphism of \(E\). Its rank is the number of points in its domain.

**Sharp first-defect law.** If all classes have equal size, every partial automorphism is extendible. Otherwise, every partial automorphism of rank strictly greater than \(n-\delta\) is extendible, and the exact number \(d_E\) of nonextendible maps of rank \(n-\delta\) is
\[
\boxed{d_E=g\sum_{s\ge1:\,m_sm_{s+\delta}>0}m_sm_{s+\delta}\,\frac{\binom{s+\delta}{\delta}}{\delta!}>0.}
\]
Thus the distance between adjacent occurring class sizes is exactly the first possible rank deficiency of an unextendible finite partial symmetry; the displayed formula gives the whole first-defect stratum.

**Coupled exact rank profiles.** Let \(A_E(z)\) count every partial automorphism by its domain size, and let \(R_E(z)\) count the extendible ones. For each finite vector \(\alpha=(a_1,\ldots,a_n)\) of nonnegative integers, define
\[
D_\alpha=[u_1^{a_1}\cdots u_n^{a_n}]\prod_{s\ge1}\left(1+\sum_{j=1}^s\binom sj u_j\right)^{m_s}.
\]
Then, with all the sums finite,
\[
\boxed{A_E(z)=\sum_{\alpha}D_\alpha^2\prod_{j=1}^n a_j!(j!)^{a_j}\,z^{\sum_{j=1}^n j a_j}.}
\]
The extendible polynomial factors over occurring original class sizes:
\[
\boxed{R_E(z)=\prod_{s:m_s>0}\ \sum_{a_0+\cdots+a_s=m_s}\frac{(m_s!)^2}{(a_0!)^2\prod_{j=1}^s a_j!}\prod_{j=1}^s\left[\binom sj^2j!z^j\right]^{a_j}.}
\]
In particular, all coefficients of \(A_E-R_E\) above degree \(n-\delta\) vanish, and its coefficient at degree \(n-\delta\) equals \(d_E\). For example, for two classes of sizes \(1\) and \(3\), the first nonextendible rank is \(2\) and exactly \(9\) such maps occur.

## Assumptions and scope

The language contains only one binary relation interpreted as a reflexive, symmetric, transitive equivalence relation. All structures, their substructures, and maps are finite. Induced subsets inherit the relation, not a list of original class sizes. Automorphisms preserve actual complete original equivalence classes. The empty partial map is included. Rank here is *domain cardinality of a partial map*, not ordinal-valued Fraïssé extension rank or logical quantifier rank. The empty host is excluded from the threshold statement, but both polynomials for it equal \(1\). When there is only one occurring class size, \(\delta\) is undefined and every partial automorphism extends, including the case of a single class.

## Proof

**1. Structural description of partial maps.** Let \(S,T\subseteq V\). The nonempty intersections of \(S\) with original equivalence classes form the classes of the induced relation on \(S\). A bijection \(f:S\to T\) is a partial automorphism if and only if it sends each selected class intersection bijectively onto a selected class intersection of the same size, with different selected intersections going to different target intersections. It extends to an automorphism of \(V\) if and only if every paired source and target intersection belongs to original classes of *equal original capacity*. In that case the partial bijections may be completed classwise, and unused original classes of every size may be paired arbitrarily. The converse follows because a total automorphism necessarily preserves complete-class cardinalities.

**2. Enumerating all ranks.** Introduce indeterminates \(u_j\), one per positive selected-intersection size. The generating factor for one original class of size \(s\) is \(1+\sum_{j=1}^s\binom sj u_j\): either no point is selected, or exactly \(j\) are selected. Thus \(D_\alpha\) counts domain subsets whose selected-class multiset has \(a_j\) blocks of size \(j\); exactly the same count applies to possible target subsets. Once both subsets have the same multiset, there are \(\prod_j a_j!(j!)^{a_j}\) partial isomorphisms between them: bijectively pair the \(a_j\) blocks, then choose one of \(j!\) within-block bijections for each pair. Summing over \(\alpha\) proves \(A_E\).

For an extendible map, each original size class is independent of other sizes. Fix a size \(s\) with \(m=m_s\) original blocks and let \(a_j\) record how many of these blocks contain exactly \(j\) selected points in the domain, so \(\sum_{j=0}^s a_j=m\). The number of domain choices with this profile is \(m!/(\prod_{j=0}^s a_j!)\prod_{j\ge1}\binom sj^{a_j}\); the target has the same count. Pairing the selected blocks contributes \(\prod_{j\ge1}a_j!(j!)^{a_j}\). Multiplying and simplifying yields exactly the \(s\)-factor in \(R_E\). Distinct original sizes act independently, proving the product formula.

**3. Upper bound on the rank of a nonextendible map.** Suppose an induced partial automorphism does not extend. By Step 1 some selected intersection from an original class of size \(t\) maps to a selected intersection from an original class of distinct size \(s\). Their common selected size \(j\) satisfies \(j\le\min(s,t)\). Hence in whichever of the domain or target contains the larger original class, at least \(|s-t|\ge\delta\) points have been omitted. Since both domain and target have rank \(k\), we obtain \(n-k\ge\delta\). This establishes extendibility for all \(k>n-\delta\).

**4. Rigidity at the first defect.** Put \(k=n-\delta\). Take any nonextendible rank-\(k\) map and a block pairing with unequal original capacities. On whichever side of this pairing has the larger original capacity \(t\), write \(s<t\) for the other original capacity. Because the paired selected blocks have equal cardinality, Step 3 forces \(t-s=\delta\), their common selected size to equal \(s\), and **all** \(\delta\) omitted points on that side to come from this one \(t\)-class. The selected-class profile of that side is therefore obtained from the complete class-size profile by replacing one size-\(t\) block with one size-\(s\) block; in particular every size still occurring in its selected structure is an original class size.

The other side has the *same* selected-class profile and also omits exactly \(\delta\) points. This profile has **one more block of size \(s\)** than the complete original structure has. Such an excess is impossible if no class of some originally larger size is shortened to size \(s\): at most \(m_s\) blocks of size \(s\) can originate from original size-\(s\) classes, while deleting a complete small class can only *decrease* block counts. Thus some original class of size \(t'>s\) on the other side must be truncated to size \(s\), requiring at least \(t'-s\ge\delta\) omissions. Its full omission budget is exactly \(\delta\), so \(t'=s+\delta=t\), all its omitted points belong to that single class, and all other classes are fully selected. Therefore first-defect maps arise from a *single common* nearest pair of original capacities \((s,t)\) on both sides. Different pairs give disjoint sets of maps.

**5. Counting the first defect.** Fix an occurring pair \(s<t=s+\delta\). The domain and target independently choose one of their \(m_t\) original size-\(t\) classes and a set of \(\delta\) omitted points. There are \(m_t^2\binom t\delta^2\) ordered choices. For each choice, the selected structure has \(m_s+1\) blocks of selected size \(s\), \(m_t-1\) blocks of selected size \(t\), and unchanged full blocks of other sizes. The number of partial isomorphisms between a fixed domain and fixed target is
\[
(m_s+1)!(s!)^{m_s+1}(m_t-1)!(t!)^{m_t-1}\prod_{r\notin\{s,t\}}m_r!(r!)^{m_r}
=g\frac{(m_s+1)s!}{m_t t!}.
\]
Exactly a fraction \(1/(m_s+1)\) of these maps preserve the original capacity of the truncated block and hence extend. The nonextendible proportion is \(m_s/(m_s+1)\). Consequently the number for this pair equals
\[
m_t^2\binom t\delta^2\;g\frac{m_s s!}{m_t t!}=g\,m_sm_t\frac{\binom t\delta}{\delta!}.
\]
Sum over all occurring \(s<t=s+\delta\). At least one such pair exists by the definition of \(\delta\); each summand is positive. This proves the exact formula and sharpness. If all original classes have one common cardinality, the completion criterion of Step 1 applies to every partial map, proving the remaining case.

## Verification

Run `python3 verify.py` from this package; it uses Python's standard library only and prints `ALL_CHECKS_OK` at completion. First it reconstructs both rank polynomials for 30 partitions on up to six vertices through direct permutations of induced subsets, separately generates extendible partial maps as restrictions of all actual full automorphisms, and compares every coefficient to the independent closed formulas. It then checks the first-defect count for all 13 unequal partitions of seven vertices. The executable prints `EXHAUSTIVE_FORMULAS_AND_GLOBAL_RESTRICTIONS_OK 30`, `TOP_DEFECTS_SIZE_SEVEN_OK 13`, and `ALL_CHECKS_OK`. These finite experiments check enumeration logic and arithmetic but do not establish the all-size theorem; the proof above does.

## Relationship to prior work

Finite partial automorphisms and their inverse semigroups are classical. Chubb–Harizanov–Morozov–Pingrey–Ufferman (2008) study reconstructing equivalence structures from partial automorphism semigroups, not this sharp near-total-rank count. Jajcay–Jajcayová–Szakács–Szendrei (2018) study structural descriptions of inverse monoids of graph partial automorphisms. The published rank-spectrum calculation for homogeneous graphs includes unions of **equal-sized** cliques, where all partial automorphisms extend; this theorem agrees with and credits that special case. The new calculation is for *arbitrary nonuniform* finite equivalence relations and, most importantly, pinpoints the first nonextendible rank and its entire exact coefficient from the smallest gap between original class sizes.

Bartoš–Kubiś–Kwiatkowska–Malicki (first posted June 9, 2026) investigate extension and amalgamation of partial automorphisms in two-sorted ultrametric settings; their object is different. The theorem here concerns finite host-level extension of a partially specified map, not extension in a larger host or existence of generic automorphisms. The 2026 Fraïssé-rank paper investigates a different ordinal-valued invariant. These comparisons do not establish worldwide priority.

## Limitations

The theorem assumes a **single** finite equivalence relation with no additional colours, orders, functions, or named constants. No extension criterion is asserted for multiple equivalence relations or other Fraïssé classes. The full-polynomial expressions are finite coefficient formulas, not an asymptotic law. The previously known equal-block case is not claimed as new. Historical priority for the gap law remains best-knowledge rather than independently certified; a more specialized older finite-semigroup enumeration could subsume it. Independent mathematical validation has not been performed.

## References

1. A. Bartoš, W. Kubiś, A. Kwiatkowska and M. Malicki, *Generic dc-automorphisms of two-sorted ultrametric spaces*, arXiv:2606.11498, first posted June 9, 2026, https://arxiv.org/abs/2606.11498 .
2. J. Chubb, V. Harizanov, A. Morozov, S. Pingrey and E. Ufferman, *Partial automorphism semigroups*, Annals of Pure and Applied Logic 156 (2008), 245–258, https://repository.usfca.edu/math/3/ .
3. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first posted September 12, 2018, https://arxiv.org/abs/1809.04422 .
4. *Rank spectra and Gaussian deficiency laws for finite homogeneous graph partial automorphisms*, published-finding corpus record, published November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-spectra-and-gaussian-deficiency-laws-for-finite-homogeneous--cd9dfc7a9f4c .
5. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first posted April 15, 2026, https://arxiv.org/abs/2604.14461 .
