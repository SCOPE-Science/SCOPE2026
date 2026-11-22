# Exponential non-reconstruction from graded singleton types over three-level ultrametrics

## Finding

Let \(\mathbb U_3\) be the countable universal homogeneous ultrametric with positive distances \(1,2,3\). For a nonempty finite, individually named subspace \(A\), count complete nonalgebraic singleton types by two statistics: the smallest distance \(t\) to \(A\) and the number \(s\) of parameters at that smallest distance. Write \(\Phi_A(u,z)=\sum_{t,s}N_{t,s}(A)u^tz^s\). For each \(j\in\{1,2,3\}\), let \(\Pi_j(A)\) denote the partition into closed radius-\(j\) balls. The elementary extension correspondence gives

\[
\Phi_A(u,z)=\sum_{j=1}^{3}u^j\sum_{B\in\Pi_j(A)}z^{|B|}.
\]

The correspondence itself is background, not the new claim. Define \(F(n)\) as the largest number of mutually nonisometric \(n\)-point ultrametrics with distances in \(\{1,2,3\}\) and identical \(\Phi_A\). For \(n\ge2\), put

\[
k=\lceil2\log_2 n\rceil,\qquad
 t=\sum_{j=2}^{k+1}j=\frac{(k+1)(k+2)}2-1,\qquad
 m=\lfloor n/t\rfloor.
\]

Whenever \(n\ge t\), the new quantitative non-reconstruction bound is

\[
\boxed{F(n)\ \ge\ \frac{\binom{p(t)}m}{p(n)}\ \ge\
 \exp\!\left(m\log n-\pi\sqrt{2n/3}\right),}
\]

where \(p(v)\) counts integer partitions of \(v\). Consequently there is an absolute constant \(c>0\) such that

\[
\boxed{F(n)\ge\exp\!\bigl(cn/\log n\bigr)}
\]

for all sufficiently large \(n\). Thus a complete two-variable grading of all singleton types, even one retaining **every radius-wise ball-size distribution**, has exponentially many nonisometric realizations on some fibers. The theorem quantifies ambiguity; it does not claim a new small counterexample.

## Assumptions and scope

The language names each exact distance predicate and comparisons use the same fixed alphabet \(\{1,2,3\}\). All old parameters are fixed pointwise when taking types, while two *parameter bases* are counted the same in \(F(n)\) precisely when they are isometric as unlabelled finite metric spaces. Since the structure is homogeneous, complete nonalgebraic singleton types are determined by their exact distances to the named parameters. No limit is taken over alternate ambient languages or varying distance levels. All logarithms without subscript are natural logarithms.

A hierarchy of height three is encoded by the unordered multiset of radius-two balls; each radius-two ball is encoded by the integer partition formed by the cardinalities of its radius-one subballs. All such hierarchies are realizable as finite ultrametrics with the specified distance alphabet; unused levels are allowed.

## Proof

**1. The type-to-ball correspondence.** Take an admissible one-point distance vector \(f:A\to\{1,2,3\}\) and let \(j=\min_{a\in A}f(a)\). Choose \(b\) with \(f(b)=j\). The ultrametric triangle inequalities imply \(f(a)=\max\{j,d(a,b)\}\) for every \(a\in A\): if \(d(a,b)>j\), the distance to the new point equals \(d(a,b)\); if \(d(a,b)\le j\), both distance inequalities force \(f(a)=j\). Conversely, the displayed formula defines an ultrametric one-point extension for every choice of \(b\) and \(j\). The resulting vector depends only on the radius-\(j\) ball \(B=\{a:d(a,b)\le j\}\), and the parameters nearest to the new point are exactly \(B\). Distinct balls at a given level, or distinct minima, give distinct vectors. This proves the polynomial identity. The Fraïssé extension property realizes every admissible vector and homogeneity identifies it with a complete singleton type.

**2. A large controlled family of hierarchies.** Fix \(n\ge t\), let \(r=n-mt\), and write \(P=p(t)\). The set of partitions of \(t\) contains at least \(2^k\) elements: for each subset of \(\{2,\ldots,k+1\}\), use the selected elements as partition parts and fill the remaining sum with ones. Distinct subsets give distinct partitions and the sum is at most \(t\). Since \(k\ge2\log_2 n\), we have \(P\ge2^k\ge n^2\ge m\).

For each unordered selection of \(m\) distinct integer partitions \(\lambda_1,\ldots,\lambda_m\) of \(t\), make \(m\) radius-two balls of size \(t\), splitting the \(i\)-th ball into radius-one blocks with size partition \(\lambda_i\). If \(r>0\), add one more radius-two ball of size \(r\), made of a single radius-one block of size \(r\). Put distance three between different radius-two balls, distance two between distinct radius-one blocks in the same radius-two ball, and distance one within each radius-one block. This is an ultrametric on \(n\) points. Because \(r<t\), the optional residual ball is recognizable from its size. Isometries permute the size-\(t\) balls but preserve their internal partitions, so the selection of the \(m\) distinct partitions is recoverable from the isometry type. Therefore this family has exactly \(\binom Pm\) nonisometric members.

**3. Pigeonhole at fixed ball marginals.** Every constructed space has the same radius-two ball-size multiset, namely \(m\) copies of \(t\) and, if \(r>0\), one copy of \(r\). Every constructed space also has the same radius-three ball-size multiset \(\{n\}\). The only variable part of its type polynomial is the global multiset of radius-one block sizes. This is an integer partition of \(n\), so there are at most \(p(n)\) different type polynomials among all \(\binom Pm\) spaces. At least one fiber therefore has cardinality at least \(\binom Pm/p(n)\).

**4. Explicit lower bound and rate.** For integers \(P\ge m\ge1\), \(\binom Pm\ge(P/m)^m\). As \(P\ge n^2\) and \(m\le n\), this gives \(\binom Pm\ge n^m\). To bound partitions without an asymptotic theorem, write \(Q(x)=\prod_{j\ge1}(1-x^j)^{-1}=\sum_{v\ge0}p(v)x^v\). For any \(a>0\),

\[
\log Q(e^{-a})=\sum_{\ell\ge1}\frac1{\ell(e^{a\ell}-1)}
\le\frac1a\sum_{\ell\ge1}\frac1{\ell^2}=\frac{\pi^2}{6a}.
\]

Since \(p(n)e^{-an}\le Q(e^{-a})\), take \(a=\pi/\sqrt{6n}\) to obtain \(p(n)\le\exp(\pi\sqrt{2n/3})\). Combining with the preceding inequalities proves the explicit bound.

Finally \(k=O(\log n)\), hence \(t=O((\log n)^2)\) and \(m\ge n/t-1=\Omega(n/(\log n)^2)\). The positive term \(m\log n\) therefore grows on the scale \(n/\log n\), which dominates \(\sqrt n\). This proves the exponential-order assertion.

## Verification

Run `python3 verify_ultrametric_types.py` using standard-library Python 3.10 or later. The checker independently enumerates all admissible distance vectors for every isometry type with at most seven old points, evaluates the ultrametric inequalities directly, and agrees with the ball-count formula in all 220 checked types. Separately it generates all isometry types and groups them by graded polynomial through size eight: the number of isometry classes for orders one through eight is \((1,3,6,14,27,58,111,223)\), and the number of distinct polynomials is \((1,3,6,14,26,55,99,192)\). The first five-point collision is consistent with the previously published five-point non-rigidity phenomenon; it is not claimed as a new witness. The script also checks a numerical instance of the explicit lower-bound expression for \(n=10^6\). These finite checks do not prove the asymptotic theorem, which follows from the four steps above. The saved output file `verify_output.txt` ends with `VERIFY_OK`.

## Relationship to prior work

Nguyen Van Thé (2007) gives the homogeneous ultrametric Urysohn space framework and the finite-ball-tree correspondence. Carlsson and Mémoli (2010) develop the dendrogram–ultrametric viewpoint. Earlier finite-parameter singleton-type work established ungraded counts in terms of the number of radius-wise balls; another published theorem shows that all finite-arity tuple-type counts depend only on those numbers and documents the already-known five-point failure of reconstruction even after all ball-size marginals are supplied. Mémoli and Zhou (2022/2023) likewise gave a five-point nonisometric ultrametric pair with the same verbose Rips barcode; no novelty is asserted for a small-size collision.

A separate published result on distance-aware one-dimensional colour refinement proves that two rounds recover the entire three-level ultrametric and that one round has a unique first collision on eight points. Its one-round vertex signatures retain correlations between local and outer ball sizes that are deliberately absent from the graded singleton-type polynomial here. It does not assert the present quantitative lower bound for the smaller marginal invariant.

The claimed contribution is specifically the all-order \(\exp(\Omega(n/\log n))\) **isometry-fiber lower bound for the complete graded singleton-type polynomial**. The cited foundational results provide the tree/type dictionary or finite counterexamples, but do not themselves establish this lower bound by implication without the distinct-refinement family and pigeonhole argument.

## Limitations

This is a lower bound, not a matching upper bound or an exact formula for \(F(n)\). The construction permits radius-one and radius-two classes of size one and does not require every listed distance to be realized. The result concerns unlabelled isometry classes within a fixed three-level ultrametric language, not arbitrary finite metric spaces, detailed vertex-colour profiles, or the entire relational structure of all higher-arity extensions. Existing literature on hierarchical partition multiplicities may contain equivalent counting statements not found in the inspected sources; final priority requires independent assessment. No external independent audit has been performed.

## References

1. L. Nguyen Van Thé, *Ramsey degrees of finite ultrametric spaces, ultrametric Urysohn spaces and dynamics of their isometry groups*, arXiv:0710.2347, version 1 publicly submitted 2007-10-11. https://arxiv.org/abs/0710.2347 . Sections 1–2 provide the homogeneous-space and tree/ball representation.
2. G. Carlsson and F. Mémoli, *Characterization, stability and convergence of hierarchical clustering methods*, Journal of Machine Learning Research 11 (2010), 1425–1470. https://jmlr.org/papers/volume11/carlsson10a/carlsson10a.pdf . Section 3.3 identifies ultrametrics with dendrograms.
3. F. Mémoli and L. Zhou, *Ephemeral Persistence Features and the Stability of Filtered Chain Complexes*, arXiv:2208.11770 (first submitted 2022-08-24), SoCG 2023. https://arxiv.org/abs/2208.11770 . See the five-point counterexample in Example 3.20.
4. *Integral congruence of ultrametric one-type distance-feasibility matrices*, published mathematical record, identifier `cc0fbcfb-3a13-479a-95f1-a2a2e89e5cf1`.
5. *Finite-arity saturation and the first hidden-nesting collision of ultrametric type counts*, published mathematical record, identifier `9a251e70-0cfe-480e-b1c1-0c003c42cc36`.
6. *Distance-aware colour refinement on finite ultrametrics: two rounds suffice and eight points first defeat one*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-distance-aware-colour-refinement-on-finite-ultrametrics-two-roun--4e36345f61be .
