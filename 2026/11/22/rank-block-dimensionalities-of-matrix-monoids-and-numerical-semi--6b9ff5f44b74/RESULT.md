# Rank-block dimensionalities of matrix monoids and numerical semigroups

## Finding
Let \(K\) be any field and \(n\ge 2\). Write \(M=M_n(K)\), \(G=\operatorname{GL}_n(K)\), and \(R_r=\{X\in M:\operatorname{rank}(X)=r\}\). Given any set partition \(\Pi\) of \(\{0,1,\ldots,n-1\}\), define the **rank-block equivalence** on \(M\) whose classes are \(\{I_n\}\), \(G\setminus\{I_n\}\), and \(R_B=\bigcup_{r\in B}R_r\) for \(B\in\Pi\).

An equivalence is called a *dimensionality* if its identity class is a singleton and the setwise product of any two equivalence classes is a union of entire equivalence classes (Jenča's lax-equivalence condition for an ordinary monoid).

**Theorem.** The rank-block equivalence is a dimensionality if and only if:

1. Every block of \(\Pi\) is an integer interval \([a_i,a_{i+1}-1]\), with \(0=a_1<a_2<\cdots<a_t\le n-1\) and \(a_{t+1}=n\).
2. The set \(A=\{a_1,\ldots,a_t\}\) is closed under truncated addition \(a\star b=\max(0,a+b-n)\).

Equivalently, \(T=\{0\}\cup\{n-a:a\in A\}\cup\{n+1,n+2,\ldots\}\) is a numerical semigroup whose conductor is at most \(n\). This establishes a canonical bijection between the rank-block dimensionalities and numerical semigroups with conductor at most \(n\), uniformly over every field. For \(n=2,\ldots,9\), their counts are \(2,3,5,7,12,16,27,37\), respectively. None is the orbit equivalence of a monoid automorphism subgroup.

## Assumptions and scope
Here \(K\) is arbitrary, including finite fields and characteristic two; \(n\) is an integer at least two. A numerical semigroup means a cofinite additive submonoid of \(\mathbb N_0\), and its conductor is the smallest \(c\ge0\) such that every integer at least \(c\) belongs to it. The classification concerns exactly the specified rank-block equivalences, **not** arbitrary equivalences on \(M_n(K)\). No group-inverse compatibility of the quotient is assumed.

## Proof
**1. Product ranks.** For any \(0\le r,s\le n\), Sylvester's rank inequality and the upper bound on product rank give
\[
R_rR_s=\bigcup_{k=\max(0,r+s-n)}^{\min(r,s)}R_k.
\]
Every such \(k\) occurs: choose a rank-\(r\) left factor and a rank-\(s\) right factor so that the right factor's image meets the left factor's kernel in exactly \(s-k\) dimensions. The inequalities on \(k\) are precisely the feasibility conditions. Arbitrary rank-\(k\) matrices follow by left and right multiplication by units, which preserve factor ranks. Thus setwise products of rank-union classes are saturated within each individual rank.

**2. Units impose no further constraints.** The identity class multiplies trivially. Since \(|G|>2\) for \(n\ge2\) over any field, \((G\setminus\{I_n\})^2=G\): for each \(g\in G\), choose \(u\in G\setminus\{I_n,g\}\), and then \(u^{-1}g\ne I_n\). For any singular rank-block class \(R_B\), \((G\setminus\{I_n\})R_B=R_B(G\setminus\{I_n\})=R_B\); in fact, multiplication by one chosen nonidentity unit permutes every individual rank stratum. Hence class-product saturation reduces to products of the singular rank blocks.

**3. Necessity of contiguous blocks.** Suppose a block \(B\) has \(a=\min B\), \(b=\max B\), and a missing integer \(a<k<b\). Let \(C\ne B\) be the block containing \(k\), and set \(c=\max C\). The product \(R_BR_C\) contains rank \(a\), because a rank-\(a\) factor can multiply a rank-\(k\) factor to yield rank \(a\). Saturation then forces rank \(b\) into the product; as every product has rank at most \(c\), this implies \(c\ge b\). Similarly, the product contains rank \(k\) (choose factor ranks \(b,k\) and arrange rank \(k\)); saturation then forces rank \(c\) into the product. Its rank is at most \(b\), so \(c\le b\). Hence \(c=b\), contradicting disjointness of \(B\) and \(C\). All blocks are consecutive intervals.

**4. Exact interval-block products.** Write \(B_i=[a_i,b_i]\) and \(B_j=[a_j,b_j]\). The product-rank set is precisely
\[
H_{ij}=[\max(0,a_i+a_j-n),\ \min(b_i,b_j)]\cap\mathbb Z.
\]
The bounds follow from Step 1. Conversely, for any integer \(k\) between them, select ranks \(r=\max(a_i,k)\in B_i\) and \(s=\max(a_j,k)\in B_j\). Then \(r+s\le n+k\) (check separately whether each maximum equals its left argument or \(k\)), and \(k\le\min(r,s)\). Step 1 gives every rank-\(k\) matrix as a product. The right endpoint \(\min(b_i,b_j)\) is always a right block endpoint. Therefore this product is a union of whole interval blocks exactly when its left endpoint \(\max(0,a_i+a_j-n)\) is a left block endpoint. This proves the two stated conditions are jointly necessary and sufficient.

**5. Numerical-semigroup correspondence.** As \(0\in A\), the map \(A\mapsto T=\{0\}\cup(n-A)\cup[n+1,\infty)\) gives a cofinite subset of \(\mathbb N_0\) containing all integers at least \(n\). For \(a,b\in A\), if \(a+b\le n\), their reflected numbers add to at least \(n\); if \(a+b>n\), the sum \((n-a)+(n-b)=n-(a+b-n)<n\) lies in \(T\) exactly when \(a+b-n\in A\). All other additive products are automatically in \(T\). Thus closure of \(A\) under \(\star\) is equivalent to \(T\) being a numerical semigroup. Conversely, any numerical semigroup with conductor at most \(n\) contains \(n\), and its entries in \([0,n]\) recover uniquely the reflected endpoint set \(A\); sorted endpoints recover \(\Pi\).

**6. Not an automorphism-orbit equivalence.** Every rank-one stratum lies entirely in one singular rank-block class. It contains the idempotent matrix unit \(E_{11}\) and the square-zero, nonidempotent matrix unit \(E_{12}\). A monoid automorphism preserves the equation \(X^2=X\), hence no subgroup of automorphisms can have these matrices in a common orbit. This applies for all \(n\ge2\) and all fields.

## Verification
The accompanying self-contained Python program `check_rank_dimensionalities.py` enumerates all matrices over \(\mathbb F_2\) for \(n=2,3\), computes exact products and confirms the attainable rank intervals for every pair of factor ranks. It independently enumerates **all set partitions** of \(\{0,\ldots,n-1\}\) for \(2\le n\le9\), checks class-product saturation by the Sylvester rank interval, and compares the valid partitions against exactly the interval partitions closed under truncated addition. The count sequence is \(2,3,5,7,12,16,27,37\). These finite checks are corroboration, not an infinite-field proof; the proof above covers arbitrary fields and all \(n\ge2\).

Run: `python3 check_rank_dimensionalities.py`.

## Relationship to prior work
Jenča's *Dimensionalities on monoids* (first posted November 13, 2026), Definition 3.2 and Proposition 3.3, provides the dimensionality notion and its singleton-identity / saturated-class-product characterization. Jenčová and Jenča's 2017 predecessor develops relational monoid adjunctions and a monic-polynomial degree example, not matrix-rank partitions. Its examples concern word length, monic-polynomial degree, and additive refinement, not the above matrix-rank block classification or numerical-semigroup bijection. The standard product-rank interval used here is a consequence of Sylvester's rank inequality and constructive linear algebra. The numerical-semigroup correspondence is the additional classification specific to full matrix monoids.

## Limitations
This does not classify all dimensionalities of \(M_n(K)\), nor distinguish isomorphism classes of their relational quotients. The initial counts are finite exhaustive computations; no new asymptotic formula is asserted. Earlier unindexed treatments of rank-class semigroup partitions or equivalent relational quotients could contain an implicit version; historical priority is not completely established. No independent mathematical audit has been performed.

## References
1. G. Jenča, *Dimensionalities on monoids*, arXiv:2611.18000v1, November 13, 2026, https://arxiv.org/abs/2611.18000 (especially Definition 3.2, Proposition 3.3, Examples 3.5–3.7).
2. Standard Sylvester rank inequality for products of matrices; the corresponding equality-realization argument is reproduced in the proof above.
3. Standard definition of numerical semigroups (cofinite additive submonoids of \(\mathbb N_0\)); the correspondence is proved above without relying on an external classification.
4. A. Jenčová and G. Jenča, *On monoids in the category of sets and relations*, arXiv:1703.03728, March 10, 2017, https://arxiv.org/abs/1703.03728 (especially Proposition 2 and Example 8).
