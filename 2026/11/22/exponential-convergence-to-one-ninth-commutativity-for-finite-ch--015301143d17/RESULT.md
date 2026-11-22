# Exponential convergence to one-ninth commutativity for finite-chain partial translations

## Finding
Let \(S_n\) be the monoid of all order-preserving partial isometries of the linearly ordered metric space \([n]=\{1,\ldots,n\}\), including the empty map, and let \(E_n\) be its idempotent semilattice. Write
\[
C_n=\#\{(f,g)\in S_n^2:fg=gf\},\qquad
P_n=C_n/|S_n|^2.
\]
For every \(n\ge1\), the monoid has \(|S_n|=3\cdot2^n-2(n+1)\) elements and \(|E_n|=2^n\) idempotents (these two underlying counts were known). For each \(1\le r<n\), the number of ordered commuting pairs \((f,e)\) where \(f\notin E_n\) has rank \(r\) and \(e\in E_n\) is exactly
\[
\boxed{M_{n,r}=2\binom{n}{r+1}2^{n-r}.}
\]
Consequently the total number with a nonidempotent first factor and an idempotent second factor is
\[
\boxed{M_n=4\cdot3^n-(n+2)2^{n+1}.}
\]
Set \(N_n=\#\{(f,g)\in (S_n\setminus E_n)^2:fg=gf\}\). Then
\[
\boxed{C_n=4^n+2M_n+N_n.}
\]
For every \(n\ge16\), putting \(h=\lfloor n/8\rfloor\), the new quantitative estimate is
\[
\boxed{0\le N_n\le4^n\left[4h^2(5/8)^{(n-4h)/5}+8\,2^{-h}\right].}
\]
In particular, for a fixed constant \(0<\rho<1\), one can take \(\rho=\max\{(5/8)^{1/10},2^{-1/8}\}\), and obtain
\[
\boxed{P_n=\frac19+O(n^2\rho^n).}
\]
Moreover, conditional on commuting, two independent uniformly chosen monoid elements are both idempotent with probability \(1-O(n^2\rho^n)\). Thus the limiting probability of commutation is entirely supported on the Boolean semilattice of partial identities, unlike interval-only translation rook monoids.

## Assumptions and scope
An element of \(S_n\) is a partial injective map satisfying both \(|f(i)-f(j)|=|i-j|\) and order preservation wherever defined. Every nonempty element has a **unique** signed translation displacement \(a\in\{1-n,\ldots,n-1\}\) and a nonempty domain \(A\subseteq I_a=\{i\in[n]:i+a\in[n]\}\), acting as \(f(i)=i+a\) for \(i\in A\). The empty map is counted once. Products are ordinary composition; their equality is independent of whether row-action or function-action convention is adopted. Rank is domain size. The finite-field or characteristic notions are not involved.

Idempotents are precisely partial identity maps \(e_D:i\mapsto i\) on subsets \(D\subseteq[n]\), including the empty set. The notation \(M_{n,r}\) counts a particular **ordered orientation** of a commuting pair, rather than both orientations. The estimate for \(N_n\) is explicit for \(n\ge16\); the asymptotic conclusions concern \(n\to\infty\).

## Proof
**1. Translation and rank enumeration.** For each nonzero displacement \(a\), there are \(2^{n-|a|}-1\) nonempty translations. For displacement zero, there are \(2^n\) partial identities, including the empty map. Summing gives \(|S_n|=2^n+2\sum_{a=1}^{n-1}(2^{n-a}-1)=3\cdot2^n-2(n+1)\). For \(1\le r<n\), the number of nonidempotents of rank \(r\) is
\[
2\sum_{a=1}^{n-r}\binom{n-a}{r}=2\binom{n}{r+1}.
\]
The first formula is background in [1]; the rank refinement follows directly from the displacement decomposition.

**2. A commuting-idempotent forest lemma.** Fix a nonidempotent translation \(f\) with displacement \(a\ne0\) and domain \(A\), \(|A|=r\). The identities \(fe_D=e_Df\) hold if and only if
\[
\mathbf 1_D(i)=\mathbf 1_D(i+a)\quad\text{for every }i\in A.
\]
Indeed the two compositions are either simultaneously defined and equal at \(i\), or are simultaneously undefined, exactly when the two membership indicators agree. Consider the undirected graph on \([n]\) with edges \(\{i,i+a\}\) for \(i\in A\). For fixed signed nonzero \(a\), all edges move monotonically along disjoint arithmetic progressions, so this graph is a forest. Its \(r\) edges are distinct, and it has exactly \(n-r\) connected components. The membership indicator of \(D\) may be chosen independently but must be constant on each component. Therefore **exactly \(2^{n-r}\) idempotents commute with every specified nonidempotent of rank \(r\)**. Multiplying by its rank census proves \(M_{n,r}\). The binomial theorem and the hockey-stick identity then give
\[
M_n=2\sum_{r=1}^{n-1}\binom{n}{r+1}2^{n-r}=4\cdot3^n-(n+2)2^{n+1}.
\]
All ordered pairs of idempotents commute, giving the exact decomposition of \(C_n\).

**3. Suppression of nonidempotent commuting pairs.** Fix \(n\ge16\) and \(h=\lfloor n/8\rfloor\). First restrict to displacements \(a,b\ne0\) with \(|a|,|b|\le h\). To upper-bound the count of commuting nonempty translations, allow their source subsets to be empty and choose each eligible source position independently with probability \(1/2\). For every integer \(i\) in \(\{2h+1,\ldots,n-2h\}\), both compositions, if defined, have the same translation output \(i+a+b\). Commutation requires the bit constraint
\[
\mathbf 1_A(i)\mathbf 1_B(i+a)=\mathbf 1_B(i)\mathbf 1_A(i+b).
\]
All four displayed bits are independent, with both products independently equal to one with probability \(1/4\). The chance that the equality holds is therefore \((3/4)^2+(1/4)^2=5/8\).

For distinct tests at \(i\) and \(j\), the Bernoulli variables overlap only if \(j-i\in\{\pm a,\pm b\}\). The dependency graph of the \(n-4h\) tests has maximum degree at most four. It has an independent set of at least \((n-4h)/5\) tests (greedy graph coloring or greedy independent-set bound), and the constraints at these indices are genuinely independent. Thus the fraction of all choices for these fixed displacements that commute is at most \((5/8)^{(n-4h)/5}\). There are at most \((2h)^2=4h^2\) small nonzero displacement pairs, and each admits at most \(4^n\) choices of two subsets, yielding the first term of the displayed bound for \(N_n\).

For large displacements, the total number of nonempty maps with \(|a|>h\) is less than
\[
2\sum_{d=h+1}^{n-1}2^{n-d}<2^{n+1-h}.
\]
The total number of maps with nonzero displacement is less than \(2^{n+1}\). A union bound for which factor has large displacement thus gives fewer than \(2^{2n+3-h}=8\cdot4^n2^{-h}\) ordered pairs, irrespective of commutativity. Adding the small and large displacement contributions proves the claimed bound on \(N_n\), without any unjustified independence assumptions for overlapping constraints.

**4. Asymptotic law.** Since \(n-4h\ge n/2\), \(h\ge n/8-1\), and \((5/8)^{(n-4h)/5}\le (5/8)^{n/10}\), the upper bound on \(N_n/4^n\) is \(O(n^2\rho^n)\) for the stated \(\rho<1\). Also \(M_n/4^n=4(3/4)^n-(n+2)2^{1-n}\), and \(|S_n|/(3\cdot2^n)=1-O(n2^{-n})\). The exact decomposition gives
\[
\frac{C_n}{|S_n|^2}=\frac{4^n}{(3\cdot2^n-2(n+1))^2}+\frac{2M_n+N_n}{|S_n|^2}=\frac19+O(n^2\rho^n).
\]
Finally \(4^n/C_n=1-O(n^2\rho^n)\), because the numerator counts exactly the idempotent-idempotent commuting pairs and the remaining contributions are exponentially smaller. All quantifiers, including the boundary at \(n=1\), follow from the formulas and the stated restriction for the explicit exponential estimate.

## Verification
The standalone `verify.py` constructs every partial translation as a literal partial map and compares ordinary composition in both orders for **every** ordered pair for \(1\le n\le9\). It independently verifies the monoid size, idempotent count, rank-stratified mixed commuting-pair formula, and decomposition \(C_n=4^n+2M_n+N_n\). It prints `VERIFY_OK_ODP_COMMUTING`; its actual output is embedded as `verification_output.txt`. The exact commuting-pair counts for \(n=1,2,\ldots,9\) are \(4,26,144,686,2856,11014,40336,144258,510900\). These tests corroborate rather than replace the general forest proof and independent-set probability bound.

## Relationship to prior work
Kehinde and Umar [1] establish the finite-chain order-preserving partial-isometry inverse monoid and its cardinality, idempotent structure and Green relations; their Theorem 3.6 is the known size formula used here. Al-Kharousi, Kehinde and Umar [2] enumerate single-map height, fixed-point and class statistics, not ordered commuting pairs. Fernandes and Quinteiro [3] study semidirect-product decompositions rather than uniform commuting-pair probabilities.

The independently accessible paper *The product-rank law of finite-chain partial translations* [4] gives the unrestricted rank distribution of a **single composite** of two uniform elements, but it does not determine whether the two composite maps are **equal**. Its statement explicitly excludes conditional commuting pairs. The paper *A three-tenths commutativity law for interval-translation rook monoids* [5] computes the limiting commuting probability for maps whose domains are restricted to **contiguous intervals**, a different, polynomial-size inverse monoid. That \(3/10\) value is not transferable to the present arbitrary-subset, exponential-size monoid. The current claim determines the mixed-idempotent fibers and proves a contrasting one-ninth limit with explicit exponential convergence.

## Limitations
The theorem concerns order-preserving partial isometries, not order-reversing ones or the full symmetric inverse monoid. It does **not** give a closed exact expression for \(N_n\) or a complete finite-size formula for all commuting pairs. The convergence exponent is a valid uniform bound but is not asserted sharp. Exact counts for small \(n\) are finite tests, not infinite proofs. Prior publication overlap remains possible under alternative descriptions of the same commuting event; absence from the inspected records is not a proof of global priority. No independent mathematical audit has been carried out.

## References
1. R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049v1 (2010-12-30), Sections 1–3, especially Theorem 3.6. https://arxiv.org/abs/1101.0049
2. F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain*, Australasian J. Combin. **58** (2014), 365–375, Sections 2–3. https://ajc.maths.uq.edu.au/pdf/58/ajc_v58_p365.pdf
3. V. H. Fernandes and T. M. Quinteiro, *A note on bilateral semidirect product decompositions of some monoids of order-preserving partial permutations*, arXiv:1502.06097 (2015). https://arxiv.org/abs/1502.06097
4. *The product-rank law of finite-chain partial translations*, publicly accessible research record (2026), full result and proof inspected.
5. *A three-tenths commutativity law for interval-translation rook monoids*, publicly accessible research record (2026), full result and proof inspected. Compare Fikioris and Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863 (2021).
