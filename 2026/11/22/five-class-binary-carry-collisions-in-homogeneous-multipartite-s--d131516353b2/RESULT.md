# Five-class binary-carry collisions in homogeneous multipartite singleton-type counts

## Finding

**Theorem (exact profile collisions).** Fix an integer \(q\ge2\). Let \(M_q\) be the countable homogeneous graph equipped with a named equivalence relation \(E\) having exactly \(q\) infinite classes, no graph edges inside a class, and freely generic graph edges between distinct classes. Let \(A\) be an individually named finite substructure meeting **every** \(E\)-class, with positive class sizes \(a_1,\ldots,a_q\) and total size \(n=\sum_i a_i\). Write \(T(A)\) for the number of complete nonalgebraic singleton types over \(A\). Then

\[
T(A)=\sum_{i=1}^{q}2^{n-a_i},\qquad
P_A(z)=\sum_{i=1}^{q}(1+z)^{n-a_i},
\]

where \(P_A(z)\) grades these types by their numbers of adjacent named parameters. In particular, the scalar \(T(A)\) and the graded polynomial depend on the **unordered class-size profile**, not on the graph induced between different classes. The full polynomial \(P_A(z)\) reconstructs the unordered class-size profile for every \(q\ge2\).

**Rigidity for at most four classes at known size.** For \(2\le q\le4\), knowing \(q\), the common parameter cardinality \(n\), and the scalar \(T(A)\) uniquely determines the unordered class-size profile.

**Complete five-class collision classification at fixed size.** For \(q=5\), two different unordered positive class-size profiles of the **same total size** give the same scalar \(T\) if and only if, after exchanging them if necessary, there are integers \(t\ge3\) and \(1\le d\le t-2\) such that the profiles are

\[
\begin{aligned}
\lambda_{t,d}&=(t-1-d,\ t,\ t+1,\ t+1,\ t+d),\\
\mu_{t,d}&=(t-d,\ t-d,\ t-1,\ t+1+d,\ t+1+d).
\end{aligned}
\]

Both have \(n=5t+1\) parameters, and their common singleton-type count is exactly

\[
\boxed{2^{4t+2+d}+2^{4t+2}+2^{4t+1-d}.}
\]

For each \(n=5t+1\ge16\), exactly \(t-2\) scalar values have a two-element fiber on the set of unordered five-part profiles, and every other fiber is a singleton. For every other \(n\), all five-part profiles have different scalar counts. Therefore the **first** five-class collision occurs at \(n=16\), and is the unique collision pair at that size:

\[
\boxed{(1,3,4,4,4)\quad\text{and}\quad(2,2,2,5,5),\quad T=53248.}
\]

The theorem does not assert that these numbers reconstruct the induced *graph*: its cross-class edge pattern is invisible even when the class-size profile is recoverable.

## Assumptions and scope

The language contains equality, a named binary equivalence predicate \(E\), and an irreflexive symmetric graph predicate \(R\). The structures satisfy \(R(x,y)\Rightarrow\neg E(x,y)\). The age of \(M_q\) consists of all finite such structures with at most \(q\) equivalence classes; this class has the hereditary, joint embedding, and amalgamation properties. In amalgamations, new equivalence classes on opposite sides may be identified to remain within the \(q\)-class bound, while missing cross-edges are freely chosen. Its Fraïssé limit has precisely \(q\) infinite \(E\)-classes and the requisite free cross-class extension property. Isomorphisms of finite substructures may permute \(E\)-classes; they are not individually named unary sorts. The **parameters** are individually named, and the hypothesis that all \(q\) classes are met is essential. Each permissible one-point diagram is realized infinitely often, so the counted nonalgebraic quantifier-free diagrams are precisely complete nonalgebraic types by homogeneity and quantifier elimination.

A profile means the unordered multiset of positive numbers of old parameters in each \(E\)-class; no restriction is imposed on their old cross-class edges. The scalar collision theorem compares profiles at the same fixed \(q\) **and the same fixed total size \(n\)**. This common-size assumption is essential; there are scalar collisions between profiles of different total sizes even for three classes. For example \((1,4,4)\) at size nine and \((3,3,4)\) at size ten both give \(T=320\).

## Proof

**Step 1: exact one-point diagrams.** A new point must belong to one of the \(q\) old \(E\)-classes, say class \(i\). It is nonadjacent to the \(a_i\) old points in that class, and its adjacency to each of the \(n-a_i\) old points outside that class is arbitrary. This gives \(2^{n-a_i}\) complete nonalgebraic types, and the finer weight enumerator \((1+z)^{n-a_i}\). Summing proves the displayed formulas. The polynomials \((1+z)^e\) for distinct nonnegative \(e\) form a basis of the polynomial ring over \(\mathbb Q\), by triangular leading-degree elimination. Hence \(P_A\) determines the multiset of exponents \(e_i=n-a_i\). As \(\sum_i e_i=(q-1)n\), it determines \(n\) and every \(a_i\) for \(q\ge2\).

**Step 2: arithmetic reduction.** Write \(e_i=n-a_i\). For \(q\) positive parts the integer exponent multiset has length \(q\), its exponent sum is \((q-1)n\), and its base-two power sum is \(T(A)\). Conversely, any exponent multiset of length \(q\) with sum \((q-1)n\) and all \(0\le e_i<n\) defines a unique unordered positive profile by \(a_i=n-e_i\). If two profiles of size \(n\) collide, their exponent multisets have equal length, equal sums of exponents, and equal sums of powers of two.

The binary-splitting argument compares the two exponent sums only because the total parameter cardinality is fixed. When \(n\) differs, equality of the scalar is insufficient to force equality of exponent sums. Accordingly no scalar reconstruction across different parameter sizes is asserted.

For a positive integer \(N\), write its unique binary expansion \(N=\sum_{s=1}^{r}2^{b_s}\), with strictly different exponents. Every representation of \(N\) as \(q\) (repeated) powers of two is obtained from these \(r\) canonical summands by \(q-r\) successive binary *splits*, replacing \(2^b\) by two copies of \(2^{b-1}\). This follows by reversing carries until every coefficient in the binary representation is zero or one. A split of a source bit of exponent \(b\) changes the sum of exponents by \(b-2\); twice splitting that source into three leaves gives \((b-1,b-2,b-2)\), with total change \(2b-5\).

**Step 3: no distinct moment collisions with at most four powers.** For at most three summands, consider the number of canonical one-bits: there is either no split, a uniquely chosen split (distinguished by its exponent-sum change), or a unique three-leaf split tree. For four summands, one canonical bit has two possible four-leaf depth profiles, \((2,2,2,2)\) and \((1,2,3,3)\), whose exponent sums differ by one. Two canonical bits with exponents \(A>B\) admit, after two splits, changes \(2A-5\) (twice the larger bit), \(A+B-4\) (each once), and \(2B-5\) (twice the smaller). Their only possible equality is at \(A=B+1\), where the first two strategies produce exactly the same leaf multiset \((B,B-1,B-1,B-1)\). With three canonical bits, one split has distinct exponent-sum changes according to the source bit. Four canonical bits need no splits. Hence two different multisets of at most four powers of two cannot have both equal power sums and equal exponent sums. This proves profile rigidity for \(q\le4\) **at a fixed total size**.

**Step 4: complete five-summand classification.** A canonical representation having five bits admits no split. With four bits, its sole split is identified by its exponent-sum change. For a single source bit, the three distinct five-leaf depth profiles are \((2,2,2,3,3)\), \((1,3,3,3,3)\), and \((1,2,3,4,4)\): their exponent sums differ, so they cannot collide.

For two canonical bits \(A>B\), three splits are required. Subtracting the original exponent sum \(A+B\), the possible changes, respectively, are

\[
3A-8,\quad 3A-9,\quad 2A+B-7,\quad A+2B-7,\quad 3B-8,\quad 3B-9.
\]

All equalities among these numbers either are impossible for \(A>B\) or occur in exactly three cases: the first equals the third at \(A-B=1\); the second equals the third at \(A-B=2\); or the second equals the fourth at \(A-B=1\). Directly writing the four leaves of a three-split source shows that each such equality gives the **same five-leaf exponent multiset**, not a collision.

For three canonical bits \(A>B>C\), two splits are required. One can split one source \(b\) twice, changing the exponent sum by \(2b-5\), or split two distinct sources \(u,v\) once each, changing it by \(u+v-4\). Changes within either group are pairwise distinct. Equality between groups requires \(u+v=2b-1\). If the source \(b\) is also among \(u,v\), this equality forces the other bit to be \(b-1\), and the resulting multisets are identical. Otherwise the split-twice source must be the middle bit \(B\), and the exact condition is

\[
\boxed{A+C=2B-1.}
\]

It produces the following **two distinct** five-term exponent multisets:

\[
(A,C,B-1,B-2,B-2),\qquad(B,A-1,A-1,C-1,C-1).
\]

These representations are permissible precisely when the relevant split exponents are nonnegative; the positive part-size constraints below imply that condition. Thus this one binary-carry resonance accounts for **every** five-term collision.

**Step 5: positive profiles and their sharp census.** In either resonant representation, the exponent sum is \(5B-6\). Since it must equal \(4n\), necessarily \(B\equiv2\pmod4\). Write \(B=4t+2\), giving \(n=5t+1\). Parameterize \(A=B+d\) and \(C=B-d-1\), where \(d\ge1\). Subtracting the two exponent multisets from \(n\) produces exactly \(\lambda_{t,d}\) and \(\mu_{t,d}\) displayed above. All five part sizes are positive if and only if \(t\ge3\) and \(1\le d\le t-2\). Conversely all these profiles satisfy the necessary binary identity and therefore collide. Their power sum is the stated three-bit integer. Each integer has a unique binary expansion, so two different \(d\) cannot give the same count; there are exactly \(t-2\) disjoint two-element collision fibers. The smallest case is \(t=3,d=1\), namely \(n=16\). This completes the classification.

## Verification

The included `check.py` performs integer-exact, dependency-free checks. Its recursive nondecreasing-partition enumerator verified all profile groups for each \(2\le q\le5\) and every admissible \(n\le80\), visiting 364,194 profiles. It found 91 five-part collision groups, exactly the predicted two-element groups, with none for smaller \(q\). An independently constructed `itertools.combinations_with_replacement` enumeration verified the complete five-part census at orders five through sixteen (37 profiles at sixteen, one collision). A second check enumerated 20,349 five-term exponent multisets with exponents at most sixteen and matched all 49 equal-moment pairs to the three-bit carry resonance. Finally explicit class-assignment and adjacency-bit diagrams through small orders matched both the scalar counts and graded coefficients. The checker printed `VERIFY_OK` when run as `python3 check.py 80`.

These computations check examples and boundaries but are not the proof for arbitrary \(n\). The all-size proof is the splitting classification above.

## Relationship to prior work

The homogeneous generic multipartite graph framework belongs to the general classification program of Jenkinson, Truss and Seidel (2012) and Lockett and Truss (2014); the latter's freely generic multipartite construction is read in its open-access initial version. General finite-base one-point type-counting for the analogous structure with infinitely many equivalence classes was previously established: its scalar formula includes the types placing the new element in an entirely new class, as well as the sum from represented old classes. Accordingly, the elementary one-point count and its grading are **not claimed as new** here. The new statement is the exhaustive fixed-cardinality inverse classification with exactly five represented classes, together with the four-class rigidity threshold. That work classifies allowable multipartite structures rather than scalar finite-base singleton-type recovery. Related published results study tuple-orbit spectra of two-sided random bipartite reducts, induced-substructure profiles of pure equivalence relations, and four-moment reconstruction from complete-multipartite metric-graph distance histograms. Those invariants have different definitions and do not imply the five-part binary-carry collision formulas as stated. The use of binary carrying is elementary, but the exact all-size five-class fiber theorem and its sharp first logical-parameter threshold were not located in the searched sources. The historical-priority conclusion is provisional, not a proof of absence from unindexed literature.

## Limitations

The class sizes are unlabelled, yet the original parameters are individually named. Each of the \(q\) classes must contain a named parameter. The scalar classification compares profiles **at fixed parameter cardinality \(n\)**. Cross-size collisions do occur: already for \(q=3\), the profiles \((1,4,4)\) and \((3,3,4)\) share \(T=320\), despite their sizes nine and ten. The exact five-class collision theorem and four-class rigidity do not classify six or more classes. The scalar and graded counts never recover the old cross-class edge matrix. The binary splitting argument and the checker concern integer exact counts, with no independent external mathematical validation claimed.

## References

1. D. C. Lockett and J. K. Truss, *Homogeneous coloured multipartite graphs*, first publicly posted 2014-06-25, arXiv:1406.6517v1, https://arxiv.org/abs/1406.6517 . In particular Introduction and §§1, 3, 6, 7.
2. T. Jenkinson, J. K. Truss, and D. Seidel, *Countable homogeneous multipartite graphs*, *European Journal of Combinatorics* 33 (2012), 82–109, DOI:10.1016/j.ejc.2011.04.004. Background classification.
3. Y. Lu, *Reducts of the Random Bipartite Graph*, first posted 2011-01-10, arXiv:1101.1947, https://arxiv.org/abs/1101.1947 . Background on the two-class orbit problem, not a source of the five-class theorem.
