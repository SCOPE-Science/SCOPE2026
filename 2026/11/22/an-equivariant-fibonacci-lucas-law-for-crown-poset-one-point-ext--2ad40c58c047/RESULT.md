# An equivariant Fibonacci–Lucas law for crown-poset one-point extensions

## Finding
Let \(n\ge5\), and let \(P_n\) be the crown poset with minimal points \(a_i\) and maximal points \(b_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\), whose only strict order relations are \(a_i<b_i\) and \(a_{i+1}<b_i\). Regard all \(2n\) points as named parameters in the countable generic homogeneous poset \(\mathbb D\). Let \(X_n\) be the set of complete **nonalgebraic** one-types of a new point over this parameter copy. The dihedral group \(G_n=\operatorname{Aut}(P_n)\cong D_n\), of order \(2n\), acts on \(X_n\) by permuting parameters. Write \(\rho(a_i)=a_{i+1}\), \(\rho(b_i)=b_{i+1}\), \(\sigma(a_i)=a_{-i}\), \(\sigma(b_i)=b_{-i-1}\).

Write \(F_0=0,F_1=1\) for Fibonacci numbers and \(L_0=2,L_1=1\) for Lucas numbers, with both sequences satisfying the standard two-term additive recurrence. For each \(g\in G_n\), the **complete fixed-point character of the extension-type action** is
\[
\boxed{\begin{aligned}
|X_n^{1}|&=2L_{2n}+4n-1,\\
|X_n^{\rho^k}|&=2L_{2\gcd(n,k)}-1 &&(1\le k<n),\\
|X_n^{\rho^k\sigma}|&=2F_{n+3}+1 &&(0\le k<n).
\end{aligned}}
\]
In particular, the number \(Q_n\) of orbits (equivalently, of one-point extensions up to an isomorphism that may permute the base) is
\[
\boxed{Q_n=2+F_{n+3}+\frac1n\sum_{d\mid n}\varphi(n/d)L_{2d}.}
\]
Here \(\varphi\) is Euler's totient function. For \(n=5,6,7,8,9\), respectively, the orbit counts are \(50,96,180,376,794\), compared with the labelled-type totals \(265,667,1713,4445,11591\). All \(n\) reflections have **the same** type fixed-point count, even for even \(n\) where the two reflection classes are distinct.

Moreover, with \(\Phi=(1+\sqrt5)/2\), the quotient has asymptotic size \(Q_n\sim L_{2n}/n\), and the fraction of nonalgebraic one-types having a nontrivial stabilizer in \(G_n\) is \(O(n\Phi^{-n})\).

## Assumptions and scope
Every one-type is **complete over the named base** in the pure strict-order language, but the action on these types is by the **setwise** base automorphism group, not the pointwise stabilizer. By the extension property and homogeneity of \(\mathbb D\), such a type corresponds precisely to an admissible ordered pair \((A,B)\) of subsets of \(P_n\), where \(A\) is the set of old points below the new point and \(B\) the set above it. Admissibility means that \(A\) is a down-set (order ideal, including the empty set), \(B\) is an up-set (filter), and \(a<b\) for every \(a\in A,b\in B\). In particular, \(A\cap B=\varnothing\). Algebraic equality types are excluded. The statement concerns \(n\ge5\); no smaller-boundary claim is needed. The nontrivial assertion is the automorphism-equivariant fixed-character and quotient census, not the previously known count of individually named types or the Lucas count of ideals.

## Proof
**1. Types and symmetry.** Given an admissible \((A,B)\), adjoining a new point \(x\) with \(A<x<B\), leaving the other named points incomparable with \(x\), defines a finite partial order by the down-set/up-set and cross-order conditions. Every finite extension embeds into \(\mathbb D\), and its complete one-type is uniquely determined by this pattern. Conversely transitivity forces precisely those conditions. The cover graph of \(P_n\) is the \(2n\)-cycle, with degree-two minima and maxima, hence its order-preserving automorphisms are exactly the \(n\) rotations and \(n\) reflections displayed above. These act faithfully on the \(n\) minima; no order automorphism interchanges the minimal and maximal levels.

**2. One-sided and two-sided patterns.** There are two families of one-sided patterns: \((A,\varnothing)\) for every ideal \(A\), and \((\varnothing,B)\) for every filter \(B\). They overlap only in the entirely incomparable type \((\varnothing,\varnothing)\). Complementation gives an automorphism-equivariant bijection \(B\mapsto P_n\setminus B\) from filters to ideals. If \(A,B\ne\varnothing\), height two forces \(A\) to consist solely of minima and \(B\) solely of maxima. Since the common upper neighbours of a nonempty set of minima in the cycle are either the two maxima incident with one chosen minimum or the unique maximal point over a chosen adjacent pair, all such types fall into exactly three disjoint forms:

- \(A=\{a_i\}\), \(B=\{b_i\}\) or \(B=\{b_{i-1}\}\), giving \(2n\) types;
- \(A=\{a_i\}\), \(B=\{b_{i-1},b_i\}\), giving \(n\) types;
- \(A=\{a_i,a_{i+1}\}\), \(B=\{b_i\}\), giving \(n\) types.

The three forms give exactly \(4n\) mixed types and three \(G_n\)-orbits. A nonidentity rotation fixes no mixed type: its action cannot fix a singleton minimum, and an adjacent pair cannot be fixed setwise by a nonzero rotation for \(n\ge5\). Each reflection fixes exactly two mixed types. Indeed a reflection of the \(n\)-cycle has either one fixed vertex and one fixed edge (odd \(n\)), two fixed vertices (even vertex-axis), or two fixed edges (even edge-axis). Each fixed vertex contributes the second form, each fixed edge contributes the third form, and the first form contributes none; in each case the sum is two.

**3. Fixed ideals under rotations.** Choose the subset \(S\subseteq\{a_i\}\) of included minima. An upper point \(b_j\) is eligible for inclusion in an ideal exactly when both \(a_j\) and \(a_{j+1}\) lie in \(S\). Each eligible upper point may be chosen or omitted independently. Introduce the symmetric transfer matrix
\[
T=\begin{pmatrix}1&1\\1&2\end{pmatrix},\qquad T_{xy}=2^{xy}\quad(x,y\in\{0,1\}).
\]
Thus the total number of ideals is \(\operatorname{tr}(T^n)\). Since \(T\) has eigenvalues \(\Phi^2,\Phi^{-2}\), the trace is \(L_{2n}\). For rotation \(\rho^k\), put \(d=\gcd(n,k)\). A fixed ideal is specified by the inclusion bits of the \(d\) minimum orbits and the independently chosen eligible orbits of maxima. The quotient incidence cycle has \(d\) edges, with a loop when \(d=1\) or a pair of parallel edges when \(d=2\); multiplicity is retained. Its transfer count is \(\operatorname{tr}(T^d)=L_{2d}\), valid for both small quotient cases.

**4. Fixed ideals under reflections.** Regard an ideal as an assignment of binary inclusion bits to minima and eligible maxima. A reflection-invariant ideal is specified by bits on the vertex orbits of the \(n\)-cycle and one independent optional maximum-orbit bit for each orbit of edges whose two endpoint-orbits are selected. Set \(u=(1,1)\) and \(v=(1,2)\). In the cycle quotient, an ordinary path edge receives transfer \(T\); a loop at an endpoint receives weight \(v\) instead of \(u\). For odd \(n=2m+1\), the quotient is a length-\(m\) path with one endpoint loop, giving \(uT^mv^{\mathsf T}\). For even \(n=2m\), the vertex-axis and edge-axis quotients give \(uT^mu^{\mathsf T}\) and \(vT^{m-1}v^{\mathsf T}\), respectively. All three expressions equal \(F_{n+3}\). To check this without an unstated identity, use \(T^2=3T-I\). The odd expression starts \(3,8\) at \(m=0,1\), namely \(F_4,F_6\). The even vertex-axis expression starts \(2,5\) at \(m=0,1\), namely \(F_3,F_5\); the edge-axis expression starts \(5,13\) at \(m=1,2\), namely \(F_5,F_7\). Each sequence obeys \(h_{m+2}=3h_{m+1}-h_m\), which also governs every other Fibonacci number, so the asserted identity follows for all indices. In particular **each** reflection fixes exactly \(F_{n+3}\) ideals.

**5. Fixed-character and orbit formula.** For any symmetry \(g\), its fixed one-sided types number twice its fixed ideals minus one. Adding the fixed mixed types from Step 2 gives
\[
|X_n^g|=2|J(P_n)^g|-1+|\mathrm{Mixed}_n^g|,
\]
which immediately yields all three stated character cases. Burnside's lemma and the fact that exactly \(\varphi(n/d)\) rotations have \(\gcd(n,k)=d\) give
\[
Q_n=\frac{2\sum_{d\mid n}\varphi(n/d)L_{2d}+4n+2nF_{n+3}}{2n}
=2+F_{n+3}+\frac1n\sum_{d\mid n}\varphi(n/d)L_{2d}.
\]
This also proves integrality without assuming a divisibility identity. For any nonidentity rotation, its fixed type count is at most \(2L_n-1\), while each reflection fixes \(2F_{n+3}+1\). Since \(L_n=O(\Phi^n)\), \(F_{n+3}=O(\Phi^n)\) and \(|X_n|\sim2\Phi^{2n}\), a union bound over at most \(2n-1\) nonidentity group elements gives a nontrivial-stabilizer proportion of \(O(n\Phi^{-n})\). The orbit formula also yields \(Q_n\sim L_{2n}/n\), because all proper-divisor rotation terms and the reflection term are exponentially smaller than the identity term. \(\square\)

## Verification
The accompanying standard-library-only `verify.py` constructs ideals by direct subset enumeration, filters by complementation, and two-sided patterns by direct common-upper-neighbour enumeration. It independently applies every rotation and reflection to all actual pairs \((A,B)\), verifies each fixed-point count and the entire orbit partition, and compares the result to the stated formula for \(5\le n\le9\). It also tests the arithmetic divisor formula for \(5\le n\le50\). Executing `python3 verify.py` produces the included `verification_output.txt` and ends in `ALL_CHECKS_OK`. These finite checks corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
The ideal/filter description of one-point types is a classical feature of the countable generic poset; see Kwiatkowska–Sullivan–Winkel (2025/2026), and the public proof *Finite-parameter 1-type counting in the random poset is #P-complete* (2026). Munarini and Zagaglia Salvi (2002) established the Lucas ideal count and rank-polynomial refinements of crowns; this **unquotiented** ideal enumeration is not claimed as novel. The published result *Uniform cyclic-incidence one-type spectra and a sharp algebraic growth law* (2026) covers \(P_n\) as its width-two case and already gives the named total \(2L_{2n}+4n-1\), including the count \(4n\) of two-sided types. It does **not** supply the \(G_n\)-fixed character or the quotient count in this theorem. Another published result on equivariant commuting idempotents in crown incidence algebras counts a different algebraic object under crown rotations and does not imply these order-extension type counts. An earlier symmetry-refined study of standard-example posets covers the distinct incidence pattern in which all but the diagonal pairs are comparable, not this cyclic incidence family for \(n\ge5\). The claimed contribution is exactly the automorphism-equivariant fixed-point character and the induced complete isomorphism-class enumeration.

## Limitations
This is an orbit count for **nonalgebraic unary extension types**; it does not count all finite extensions with multiple new points or determine their full automorphism groups. The named scalar count and Lucas ideal count were already known; merely rewriting those facts is not a novelty claim. Historical priority for the dihedral fixed-character formula remains open to independent assessment. The full text of Munarini–Zagaglia Salvi (2002) was not available through lawful open routes in this research, although its abstract and detailed published review were inspected; an institutional-access request required human intervention and was not bypassed. No independent mathematical validation has been performed.

## References
1. A. Kwiatkowska, R. Sullivan, J. Winkel, *Embeddings into the random poset* (later *Embeddings into the generic poset*), arXiv:2502.16695, first public 23 February 2025. https://arxiv.org/abs/2502.16695 ; *Journal of Symbolic Logic*, online 30 October 2026, DOI:10.1017/jsl.2026.10262.
2. E. Munarini and N. Zagaglia Salvi, *On the rank polynomial of the lattice of order ideals of fences and crowns*, *Discrete Mathematics* 259 (2002), 163–177, DOI:10.1016/S0012-365X(02)00378-3. https://doi.org/10.1016/S0012-365X(02)00378-3
3. A. Conflitti, *On Whitney numbers of the Order Ideals of Generalized Fences and Crowns*, arXiv:math/0505636, first public 30 May 2005; *Discrete Mathematics* 309 (2009), 615–621. https://arxiv.org/abs/math/0505636
4. *Finite-parameter 1-type counting in the random poset is #P-complete*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1
5. *Uniform cyclic-incidence one-type spectra and a sharp algebraic growth law*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-uniform-cyclic-incidence-one-type-spectra-and-a-sharp-algebraic--11e9e11c0647
6. *Equivariant commuting-idempotent spectra of finite incidence algebras and crown rotations*, published mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-equivariant-commuting-idempotent-spectra-of-finite-incidence-alg--2ff7f5302a07
