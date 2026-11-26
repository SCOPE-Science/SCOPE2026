# Finite-base ultrametric tuple spectra recover ball counts, but not branch sizes

## Finding

Fix a distance bound \(D\ge3\) and a nonempty finite ultrametric parameter space \(A\) with nonzero distances in \(\{1,\ldots,D\}\). Denote by \(b_0(A)=|A|\) its cardinality and by \(b_j(A)\) the number of its radius-\(j\) balls for \(1\le j\le D\); in particular \(b_D(A)=1\). Put
\[
U_0(z)=z,\qquad U_{j+1}(z)=\exp(U_j(z))-1.
\]
The counts \(i_k(A)\) of complete ordered \(k\)-types over the pointwise named base, requiring all new coordinates to be distinct from each other and from \(A\), and the unrestricted counts \(t_k(A)\) obey
\[
\sum_{k\ge0}i_k(A)\frac{z^k}{k!}=I_A(z)
=\exp\!\left(\sum_{j=1}^{D} b_j(A)U_{j-1}(z)\right),
\]
\[
\sum_{k\ge0}t_k(A)\frac{z^k}{k!}=T_A(z)
=\exp\!\left(\sum_{j=0}^{D} b_j(A)U_j(z)\right).
\]
All series are formal power series, and also entire analytic functions evaluated on positive real arguments.

**Exact profile equivalence.** For two nonempty finite parameter ultrametrics \(A\) and \(B\), all unrestricted type counts agree precisely when their complete ball-count vectors agree. The corresponding distinct-new-coordinate type counts agree precisely when their ball-count vectors at positive radii agree. Thus all tuple-type counts of the pointwise stabilizer forget sizes and incidence patterns inside the nested ball partitions, but remember the number of balls at each radius.

**Sharp collision.** For \(D\ge3\), take four points whose radius-one ball sizes are respectively \((3,1)\) and \((2,2)\), put distance one within each block, and distance two between blocks. These two bases are not isometric, but each has ball-count vector \((4,2,1,\ldots,1)\), hence identical unrestricted tuple-type counts at every arity. There is no such nonisometric collision on one, two, or three points. The smaller distance alphabets also admit the formulas, but their familiar Bell-number specializations are not asserted as new.

## Assumptions and scope

The ambient structure is the countable Fraïssé limit of nonempty finite ultrametric spaces with permitted positive distance values \(1,\ldots,D\), expressed by the finite family of binary distance predicates. The word “type” means a complete first-order type over the finite **individually named** base. The ultrametric triangle inequality forces each relation \(d(x,y)\le j\) to be an equivalence relation, and these relations are nested. Homogeneity implies that finite metric extensions and realized complete types are in bijection. Every permitted finite extension is realized; no infinitely many distance levels, unbounded metric, or uncountable language is considered.

Let \(i_0(A)=t_0(A)=1\). The new variables of an injective type must be pairwise distinct and outside \(A\). Unrestricted types may repeat variables, or identify them with specific members of \(A\). Coordinates remain ordered, which is why exponential generating functions enumerate labels on coordinate positions. All functions appearing above have nonnegative integer exponential coefficients.

## Proof

**1. Structural decomposition of distinct-variable extensions.** Let \(I_{A,D}(z)\) be the EGF of finite ultrametric extensions of \(A\) by an ordered set of distinct, fresh, labelled elements. There is precisely one ambient type for each such labelled isometry diagram over the fixed base: quantifier elimination follows from ultrahomogeneity in the finite relational distance language, and realization follows from the extension property.

For \(D=1\), all new points have mutual distance one and distance one to \(A\); hence \(I_{A,1}(z)=\exp(z)\). More generally, split any extension by its radius-\((D-1)\) equivalence classes. Each existing ball \(C\) of \(A\) has exactly one corresponding class in the extension, containing some set of newly labelled points. Every other new radius-\((D-1)\) class is a nonempty freely chosen ultrametric structure on a subset of new labels. All distances between distinct classes equal \(D\), so there is no further interaction. A nonempty finite space of permitted positive distances at most \(D-1\) is a set of nonempty lower-level classes, recursively counted by \(U_{D-1}(z)\), starting with \(U_0(z)=z\) for a singleton. Consequently the labelled SET exponential formula gives
\[
I_{A,D}(z)=\exp(U_{D-1}(z))
\prod_{C\in A/{\sim_{D-1}}}I_{C,D-1}(z).
\]
Iterating this identity, and observing that the radius-\(j\) ball counts within distinct radius-\((D-1)\) balls sum to \(b_j(A)\), gives
\[
\log I_{A,D}(z)=\sum_{j=1}^{D}b_j(A)U_{j-1}(z).
\]
This argument includes bases using only a proper subset of the permitted distances.

**2. Equality patterns.** An arbitrary type partitions its coordinate positions into equality blocks. Each position block is either assigned to a specified parameter point in \(A\), or represents one new element distinct from \(A\) and from all other new blocks. For each parameter point, the set of positions assigned to it contributes \(\exp(z)\); across \(b_0(A)\) named points this contributes \(\exp(b_0(A)z)\). Replacing each new element by a nonempty set of positions is exactly the labelled substitution \(z\mapsto \exp(z)-1\). Therefore
\[
T_A(z)=\exp(b_0(A)z)I_A(\exp(z)-1).
\]
Since \(U_{j-1}(\exp(z)-1)=U_j(z)\) for all \(j\ge1\), this is the asserted unrestricted EGF.

**3. Recovering every ball count.** For real \(z\to+\infty\), the recursively defined positive functions satisfy
\[
U_{j+1}(z)=\exp(U_j(z))-1,\qquad
\frac{U_j(z)}{U_{j+1}(z)}\longrightarrow0.
\]
Thus the functions \(U_0,\ldots,U_D\) are linearly independent: if a nonzero real linear combination vanished identically, divide by its highest-index nonzero term and let \(z\to\infty\), obtaining an impossible nonzero constant. Equality of all coefficients of two unrestricted EGFs forces equality of the analytic EGFs; taking their analytic real logarithms yields a linear relation in \(U_0,\ldots,U_D\), hence forces equality of all \(b_j\). The distinct-variable argument is identical, with \(U_0,\ldots,U_{D-1}\) and coefficients \(b_1,\ldots,b_D\). Conversely, the displayed EGFs immediately imply equality when the relevant ball counts coincide.

**4. Minimal failure of isometry recovery.** At most three labelled points, a nested partition chain (up to relabelling) is determined by its block count at each radius: from three blocks there is only one possible first merger type, and from two blocks only one possible final merger type, with the possibility of jumps recorded by the counts. Hence equal ball-count vectors imply isometry for \(|A|\le3\). On four points the two distinct radius-one partitions of block sizes \((3,1)\) and \((2,2)\) have two blocks each and collapse to one radius-two block. The resulting metrics differ in their number of distance-one pairs (three versus two), hence are not isometric, but the theorem gives the same entire type profile.

## Verification

The accompanying standalone `verify_ultrametric_types.py` enumerates finite nested equivalence relations independently of the labelled SET derivation, forms direct ultrametric extensions of small bases, and checks their distinct and unrestricted ordered-type counts against coefficients of the formulas. It tests 99 base configurations across distance bounds two and three, with the exact output preserved in `verify_ultrametric_types.out`. It also checks the four-point collision and absence of collisions through three points. Running `python3 verify_ultrametric_types.py` requires only Python's standard library. The proof above, rather than the finite enumeration, covers unbounded arity and all fixed finite \(D\ge3\).

## Relationship to prior work

Universal homogeneous ultrametric spaces and the equivalence-class/tree encoding belong to existing Fraïssé and Ramsey theory; see Nguyen Van Thé. The classical \(r\)-Bell generating function counts a marked-partition case of the lowest distance levels, and iterated Stirling/Bell generating functions already enumerate higher nested partitions without an arbitrary fixed labelled parameter ultrametric; see Mező's papers. The present statement combines finite named-base extension EGFs with an *if and only if* recovery theorem for every level's number of balls and a sharp nonisometric collision boundary. Neither the homogeneity construction, the set-partition exponential formula, nor the lower-level Bell specializations are claimed as original.

Related published orbit-profile classifications concern an ordered ultrametric expansion, a different ball-preserving ordered group, or general edge-distance weak-order structures. Their stated orbit counts do not imply the fixed-base formula or the sharp four-point profile collision. This is a best-knowledge comparison, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The theorem is specific to the finite distance chain and to types over the **pointwise** named base. The orbit counting for a setwise-stabilized or ordered ultrametric expansion is a different problem. The proof counts complete types, not model-theoretic ranks or definability within a language of unboundedly many distance predicates. The smallest collision is a *loss of information* phenomenon, not an assertion that two such bases are elementary equivalent as named structures. Literature on generalized Bell polynomials with distinguished hierarchical blocks may contain implicit equivalent transformations; no independent scientific audit has been performed.

## References

- L. Nguyen Van Thé, “Ramsey degrees of finite ultrametric spaces, ultrametric Urysohn spaces and dynamics of their isometry groups,” arXiv:0710.2347v1 (11 October 2007). Sections on finite ultrametric structures and homogeneous limits.
- I. Mező, “The \(r\)-Bell numbers,” arXiv:0909.4417 (2009). Exponential generating functions for partitions with distinguished blocks.
- I. Mező, “On powers of Stirling matrices,” arXiv:0812.4047 (2008). Higher-order Bell and iterated partition enumeration.
