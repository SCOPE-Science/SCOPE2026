# Sharp maximum automorphism-group order for simple complex evolution algebras

## Finding

For every integer \(n\ge1\), the maximum order of the automorphism group of a simple \(n\)-dimensional evolution algebra over \(\mathbb C\) is
\[
\boxed{\max\{n!,\;n(2^n-1)\}.}
\]
Both candidate values are attained by explicit simple perfect evolution algebras. In fact the maximum is \(n(2^n-1)\) for \(2\le n\le5\), and \(n!\) for \(n\ge6\); they are both \(1\) at \(n=1\). This proves the maximum-order conjecture for *simple* evolution algebras stated in the October 2026 survey by Kaygorodov, Martín González, and Viruel.

The structural bound underlying the proof is useful independently: if the directed graph of a simple \(n\)-dimensional evolution algebra has period \(d\), with cyclic-class sizes \(m_1,\ldots,m_d\), then
\[
|\operatorname{Aut}(E)|\le d(2^d-1)\prod_{i=1}^{d}m_i!\le d(2^d-1)(n-d+1)!.
\]
The period is the greatest common divisor of lengths of all directed cycles, and \(\sum_i m_i=n\).

## Assumptions and scope

An evolution algebra has a natural basis \(e_1,\ldots,e_n\) satisfying \(e_ie_j=0\) for distinct indices. Its structure matrix records coefficients of the basis squares. Here \(\mathbb C\) is the algebraically closed field of characteristic zero. Simple means no nonzero proper ideals and nonzero multiplication; for a finite-dimensional evolution algebra this implies the structure matrix is invertible and its associated directed support graph is strongly connected. Thus every automorphism is monomial and induces an automorphism of that support graph. These standard facts are part of the stated prior work.

We use directed loops and multiple outgoing arrows when present, but never multiple edges. The period \(d\) of a strongly connected finite digraph is the gcd of the lengths of closed directed walks; equivalently of all its directed cycles. Every vertex lies in exactly one of \(d\) nonempty cyclic classes, and every arrow advances a cyclic class by one step modulo \(d\).

## Proof

**1. The diagonal kernel is controlled by graph period.** Let \(G\) be the directed support graph of a simple evolution algebra. Monomiality supplies a homomorphism \(\pi:\operatorname{Aut}(E)\to\operatorname{Aut}(G)\). Its kernel \(D\) consists of diagonal automorphisms \(e_i\mapsto\lambda_i e_i\) with all \(\lambda_i\ne0\). Along every directed arrow \(i\to j\), comparison of coefficients in \(e_i^2\) gives
\[
\lambda_j=\lambda_i^2.
\]
Choose a base vertex \(v\). Strong connectivity ensures that every other vertex can be reached from \(v\), so the entire diagonal automorphism is uniquely determined by \(\lambda_v\). Every closed directed walk of length \(\ell\) from \(v\) forces \(\lambda_v^{2^\ell-1}=1\). The gcd of all such lengths is \(d\). The elementary identity
\[
\gcd(2^{a_1}-1,\ldots,2^{a_r}-1)=2^{\gcd(a_1,\ldots,a_r)}-1
\]
for finite positive-integer tuples, applied to finite subsets whose length gcd is \(d\), gives \(\lambda_v^{2^d-1}=1\). Over \(\mathbb C\), there are at most \(2^d-1\) possibilities. Hence \(|D|\le2^d-1\).

**2. The graph permutation group is controlled by cyclic classes.** Write the periodic decomposition as \(V_0\sqcup\cdots\sqcup V_{d-1}\) with edges advancing the index by one modulo \(d\), and let \(|V_i|=m_i\ge1\). This decomposition is intrinsic up to a cyclic shift: vertices \(u,w\) belong to the same class precisely when lengths of directed walks from a fixed base vertex to them are congruent modulo \(d\). Every graph automorphism therefore shifts the class indices by one common residue modulo \(d\). There are at most \(d\) choices for that shift, and, once fixed, at most \(\prod_i m_i!\) bijections within the classes. Thus
\[
|\operatorname{Aut}(G)|\le d\prod_i m_i!.
\]
The kernel/image exact sequence gives the first claimed estimate. For positive integers with sum \(n\), repeated use of \(a!b!\le(a+b-1)!\) gives \(\prod_i m_i!\le(n-d+1)!\), proving the second estimate.

**3. An exact numerical maximization.** Put \(B_d(n)=d(2^d-1)(n-d+1)!\). We verify
\[
\max_{1\le d\le n}B_d(n)=\max\{n!,n(2^n-1)\}.
\]
For \(n=1,2,3,4,5\), direct substitution gives maxima \(1,6,21,60,155\), respectively; the full rows of values are checked in the reproducibility program. At \(n=6\), the row is
\[
(B_1(6),\ldots,B_6(6))=(720,720,504,360,310,378),
\]
so each entry is at most \(6!\).

Inductively assume every \(B_d(n)\le n!\) for some \(n\ge6\). For \(d\le n\),
\[
B_d(n+1)=(n-d+2)B_d(n)\le(n+1)n!=(n+1)!.
\]
For the new index \(d=n+1\),
\[
B_{n+1}(n+1)=(n+1)(2^{n+1}-1)\le(n+1)!,
\]
because \(2^{n+1}\le n!\) holds for \(n=6\) and is preserved by induction. Thus \(B_d(n)\le n!\) for every \(n\ge6\), and equality occurs at \(d=1\). Combining small cases proves the maximization.

**4. Attainment.** For each \(n\), the cyclic evolution algebra
\[
e_1^2=e_2,\quad e_2^2=e_3,\quad\ldots,\quad e_n^2=e_1
\]
(with mixed products zero) is simple: its structure matrix is a permutation matrix and its graph is a directed cycle. Its diagonal automorphisms are parametrized by \(\lambda\in\mu_{2^n-1}\), using \(\lambda_i=\lambda^{2^{i-1}}\); the cyclic rotations of the basis all act. Consequently its full group has order exactly \(n(2^n-1)\).

For the factorial value take the evolution algebra with structure matrix \(I_n+J_n\), meaning every diagonal coefficient is \(2\) and every off-diagonal coefficient is \(1\). The matrix has eigenvalues \(n+1\) (once) and \(1\) (multiplicity \(n-1\)), so is invertible over \(\mathbb C\). Its graph has all arrows and loops, and is strongly connected. Every permutation of the basis is an automorphism. Each loop forces \(\lambda_i=\lambda_i^2\), hence \(\lambda_i=1\) for a diagonal automorphism. Thus \(\operatorname{Aut}(E)\cong S_n\), of order \(n!\). The larger of these two actual values attains the upper bound in every dimension.

## Verification

Run `python CHECK.py` using standard Python 3. It verifies each of the small rows, the integer inequalities for dimensions up to \(100\), the base inductive inequality and numeric formulas for both explicit construction families. The proof covers all positive dimensions via induction and graph-period theory; finite checks are independent corroboration only. Its output is stored in `CHECK_OUTPUT.txt`.

## Relationship to prior work

Sriwongsa and Zou (arXiv:2202.01333; first posted February 2022) proved monomiality for perfect evolution algebras, studied the graph permutation map and diagonal subgroup, and classified the maximal diagonal subgroup \(C_{2^n-1}\); they also identified the cyclic example's full automorphism group. These are acknowledged as prior, not new. The October 15, 2026 survey of Kaygorodov, Martín González and Viruel explicitly conjectured the global *combined* maximum \(\max\{n!,n(2^n-1)\}\) for simple algebras and reported computational confirmation only through dimension four. The new argument uses graph period to control the diagonal and permutation parts **simultaneously** and yields an exact upper bound in every dimension. Existing symmetry constructions supply equality cases.

published-finding corpus searches concerning maximum simple-evolution automorphism groups, period bounds for diagonal automorphisms, and the conjectured formula returned only different objects, such as an evolution-algebra parameter symmetry-jump result. No checked work was found whose statement already implies the period-sensitive bound or the full maximum conjecture. Older graph-automorphism results may contain overlapping lemmas, and exhaustive historical priority is not certified.

## Limitations

The theorem is for simple complex evolution algebras and the order of their full algebra automorphism groups, not all perfect but nonsimple evolution algebras, not classification of all maximizers, and not arbitrary coefficient characteristic. The factorial inequality uses characteristic zero only in the construction \(I_n+J_n\) and exact complex root count; the structural upper-bound mechanism works more generally where monomiality and strong connectivity apply.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, first submitted October 15, 2026; conjecture on largest automorphism groups of simple algebras. https://arxiv.org/abs/2610.22248
2. S. Sriwongsa, Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333, first submitted February 2, 2022, especially Section 2 (monomial and graph automorphisms) and Section 4 (maximal diagonal subgroups). https://arxiv.org/abs/2202.01333
3. The open-conjecture summary, *Largest automorphism groups of simple algebras*, https://www.emergentmind.com/open-problems/largest-automorphism-groups-simple-algebras (secondary problem locator).
