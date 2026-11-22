# The sharp one-involution cutoff for coloured idempotent unary models

## Finding

Let \(q\geq1\) be an integer. An admissible finite model consists of a carrier \(X\), a total map \(f:X\to X\) satisfying \(f(f(x))=f(x)\), and a partition of \(X\) into \(q\) named colours. A colour class may be empty. Isomorphisms preserve the map and each colour. Let \(a_q(n)\) count the \(n\)-element **isomorphism classes with exactly two colour-preserving automorphisms**, and put \(F_q(t)=\sum_{n\geq0}a_q(n)t^n\), including the empty structure with coefficient zero.

**Theorem (complete first nonrigid symmetry stratum).** Set
\[
R_q(t)=\prod_{j=0}^{q}(1+t^{j+1})^{q\binom qj},\qquad
N_q=q2^{q-1}(q+2).
\]
Then \(F_q\) is the following explicitly computable **polynomial**:
\[
\boxed{\displaystyle
F_q(t)=R_q(t)\left(q^2t^3(1+t)^{q-1}
 +q\sum_{j=0}^{q}\binom qj\frac{t^{2j+2}}{1+t^{j+1}}\right).}
\]
Every displayed quotient cancels a factor in \(R_q\). The support is exactly
\[
\boxed{\{n\geq0:a_q(n)>0\}=\{2,3,\ldots,N_q+q+2\}.}
\]
There are **exactly \(q^2\)** isomorphism classes at the maximal size \(N_q+q+2\), and none beyond it. The number of labelled \(n\)-point admissible models with exactly two automorphisms is \(n!a_q(n)/2\). For \(q=1\), the nonzero coefficients, in sizes \(2\) through \(6\), are \(1,1,3,2,1\). For \(q=2\), the cutoff is \(20\), its leading coefficient is \(4\), and \(\sum_n a_2(n)=3072\).

## Assumptions and scope

All carriers are finite and may be empty for the generating-function convention; an empty model has automorphism-group order one. The function is total, and the idempotence equation is universal. The \(q\) colours are labelled, disjoint, exhaustive, and cannot be permuted by an automorphism. Roots and nonroots are not artificially distinguished by an extra predicate: roots are exactly the fixed points of \(f\). The count is up to isomorphism; its labelled counterpart follows by orbit-stabilizer. The integer \(q\) is fixed per polynomial, but the theorem holds for every \(q\geq1\).

## Proof

**Canonical component decomposition.** Every \(x\in X\) belongs to a fibre \(f^{-1}(r)\), where \(r=f(x)\) is fixed by idempotence. Every fibre has one root \(r\), whose colour is some \(c\in\{1,\dots,q\}\), and \(m_i\) additional vertices of colour \(i\), for integers \(m_i\geq0\). Thus a component type is uniquely the tuple \((c;m_1,\dots,m_q)\), and the whole model is a finite multiset of such types. All such multisets are realized.

**Automorphism factorization.** If component type \(\tau=(c;m_1,\dots,m_q)\) occurs \(k_\tau\) times, its permutations are the wreath product of the internal leaf-permutation group with the \(k_\tau\)-component symmetric group. Hence
\[
|\operatorname{Aut}(X,f)|=\prod_{\tau}\left(\prod_{i=1}^{q}m_i!\right)^{k_\tau}k_\tau!.
\]
Each factor is a positive integer, so this product is two if and only if *exactly one factor is two* and every other factor is one. There are two disjoint mechanisms.

**Mechanism I: an internal double leaf.** One component type has one colour \(i\) appearing twice among its nonroot vertices; every other leaf colour appears zero or one times. This component occurs exactly once. All remaining components must be pairwise nonisomorphic and internally rigid, namely each is one of the \(q\binom qj\) distinct star types consisting of a root colour and a set of \(j\) distinct leaf colours. Each rigid type may be present or absent independently. Their generating polynomial is exactly \(R_q(t)\). There are \(q\) choices of the exceptional root colour, \(q\) choices of its repeated leaf colour, and \(\binom{q-1}j\) choices of \(j\) other distinct leaf colours. The exceptional component then has size \(3+j\). Mechanism I contributes \(q^2t^3(1+t)^{q-1}R_q(t)\). The exceptional type cannot coincide with any rigid type, so there is no correction for overcounting.

**Mechanism II: a duplicated rigid component.** Every component is internally rigid, and exactly one rigid type occurs twice, while every other rigid type occurs at most once. If the duplicated type has \(j\) leaves, its size is \(j+1\), and there are \(q\binom qj\) choices for that type. Remove its optional singleton factor \(1+t^{j+1}\) from \(R_q(t)\), then add its mandatory double occurrence of weight \(t^{2j+2}\). This gives the sum in the theorem. The two mechanisms cannot overlap, since simultaneous internal and external transpositions produce at least four automorphisms. Their sum proves the formula for all sizes and all \(q\).

**Sharp support and top count.** The total size of all available rigid types is
\[
N_q=\sum_{j=0}^{q}q\binom qj(j+1)=q2^{q-1}(q+2).
\]
Every integer from \(0\) through \(N_q\) is a subset sum of the available rigid-type sizes. To see this, order the multiset of weights nondecreasingly. Its first weight is one, every weight \(1,2,\dots,q+1\) appears, and any subsequent weight \(w\) is at most one more than the sum of preceding weights (all smaller weights already appear). Inductively, adding each weight to a contiguous subset-sum interval preserves contiguity. Thus \(R_q\) has a positive coefficient at every degree from \(0\) through \(N_q\).

Mechanism I realizes every degree from \(3\) to \(N_q+q+2\): the optional other-colour leaves contribute every degree \(0\) through \(q-1\), and \(R_q\) contributes every degree \(0\) through \(N_q\). Mechanism II realizes degree \(2\) by duplicating a single-vertex rigid component. No model with exactly two automorphisms exists on fewer than two vertices. The greatest degree of mechanism II is at most \(N_q+(q+1)\), because the largest duplicated rigid type has size \(q+1\). Mechanism I has greater maximum \(N_q+q+2\), attained exactly when every rigid type is selected and the exceptional component contains one doubled leaf colour and each other colour once. Its root colour and repeated leaf colour are chosen independently, giving precisely \(q^2\) maximal types. This proves the cutoff, its exact support, and its top coefficient. Every order-two group gives \(n!/2\) labelled copies, completing the theorem.

## Verification

Run `python3 checker.py` using Python 3 standard library only. The program independently enumerates every finite idempotent map on labelled carriers and all named-colour assignments within the completed ranges \((q,n_{\max})=(1,6),(2,5),(3,4)\). For each model it enumerates all vertex permutations, explicitly checks colour preservation and commutation with \(f\), canonicalizes the structure separately by fibre data, and compares the resulting isomorphism-class counts and labelled counts against the polynomial. It also checks the canonical fibre group formula, the exact support, the cutoff, and the leading coefficient for \(q=1,\dots,5\). The completed output was `ALL_CHECKS_OK`, with 11,951 labelled models examined across the direct checks. These finite checks are *not* the proof of the all-size statements; the proof above is independent of finite bounds.

## Relationship to prior work

Kuželka's study of unary-function model counting and automorphism marking [1], first publicly posted 2026-08-31, supplies the enumerative motivation and the general orbit-stabilizer framework. Its automorphism-marking theorem handles arbitrary relational finite structures and does not state the specific order-two symmetry polynomial or sharp cutoff for coloured idempotent unary maps.

The publicly available result *Sharp rigidity capacity and exact census of coloured idempotent unary models* [2] already establishes the canonical star representation, the rigid polynomial \(R_q\), and its sharp cutoff \(N_q\). **These are prior results, not new claims.** They do not enumerate the exactly-two-automorphism stratum or give its full support and extremal multiplicity. The closely related published *Sharp one-involution capacity for coloured nested equivalences* [3] proves general rooted-multiset order-two recurrences for unrestricted nested-equivalence structures. Although its automorphism-factorization method is relevant, its univariate counts concern a different class: representing an idempotent map by a partition with one distinguished fixed point in every class imposes a nontrivial root-selection condition, not tracked by those unrestricted polynomials. The present explicit restricted polynomial and cutoff are therefore not numerical special cases of its displayed counts. General rooted-tree automorphism decompositions [4] also supply the method without the restricted exact enumerator. This distinction is a claim about the inspected statements, **not** proof of historical priority.

## Limitations

The result is confined to a single total idempotent operation and a fixed number of named exhaustive colours; it does not characterize the automorphism-order spectrum of general endofunctions or arbitrary additional relations. The exact polynomial is obtained from a standard wreath-product decomposition, so an earlier treatment of coloured rooted-star forests might include an equivalent formula; priority remains provisional. A general multivariate refinement of published rooted-multiset counting recurrences may imply the same polynomial by specialization, though the inspected published univariate statements do not. An independent mathematical or historical audit has not been performed.

## References

[1] O. Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580, first submitted 2026-08-31, https://arxiv.org/abs/2608.30580 (v2 full PDF Section 4.1 inspected).

[2] *Sharp rigidity capacity and exact census of coloured idempotent unary models*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-rigidity-capacity-and-exact-census-of-coloured-idempotent--4d19fd7927e8 (complete result and proof inspected).

[3] *Sharp one-involution capacity for coloured nested equivalences*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-one-involution-capacity-for-coloured-nested-equivalences--4dcdd3147eb1 (complete result and proof inspected).

[4] *An algorithm for uniform generation of unlabeled (Pólya) trees*, Forum of Mathematics, Sigma (2026), https://doi.org/10.1017/fms.2026.10218 (relevant automorphism-product lemma; partial accessible excerpt only).
