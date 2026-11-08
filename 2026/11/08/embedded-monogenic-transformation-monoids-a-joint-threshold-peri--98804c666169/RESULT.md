# Embedded monogenic transformation monoids: a joint threshold, period, and stable-rank census

## Finding

For each integer \(n\geq 1\), let \(T_n\) be the full transformation monoid of the labeled set \([n]\), with the ambient identity included. Count **distinct subsets** \(\langle f\rangle=\{1,f,f^2,\ldots\}\subseteq T_n\) that are monogenic submonoids, rather than their isomorphism types. For a transformation \(f\), let \(h\) be its power threshold (the least \(h\geq0\) such that \(f^{h+p}=f^h\) for some \(p\geq1\)); let \(p\) be its least eventual period; and let \(s\) be the stable rank \(|\operatorname{im}(f^h)|\). Equivalently, in the functional digraph, \(s\) is the number of vertices on directed cycles, \(p\) is the least common multiple of their lengths, and \(h\) is the largest distance to a directed cycle.

For integers \(s,d\geq1\), define \(P_{s,d}\) as the number of permutations of \([s]\) whose orders divide \(d\). One explicit finite expression is
\[
P_{s,d}=s!\!\!\sum_{\substack{m_\ell\geq0\ (\ell\mid d)\\\sum_{\ell\mid d}\ell m_\ell=s}}
\prod_{\ell\mid d}\frac{1}{\ell^{m_\ell}m_\ell!},\qquad
Q_{s,p}=\sum_{d\mid p}\mu(p/d)P_{s,d}.
\]
Thus \(Q_{s,p}\) counts permutations of exact order \(p\), and vanishes if that order does not occur in \(S_s\). Define a bounded-height rooted-forest number \(L_{m,s,h}\) by \(L_{m,s,-1}=0\), \(L_{0,s,h}=1\) for \(h\geq0\), \(L_{m,s,0}=0\) for \(m>0\), and for \(m,h\geq1\),
\[
L_{m,s,h}=\sum_{j=1}^{\min(m,h)}\ \sum_{\substack{a_1+\cdots+a_j=m\\a_1,\ldots,a_j\geq1}}
\frac{m!}{a_1!\cdots a_j!}\,s^{a_1}\prod_{i=2}^{j}a_{i-1}^{a_i}.
\]
Set \(E_{m,s,h}=L_{m,s,h}-L_{m,s,h-1}\) and \(c(h,p)=\varphi(p)\) for \(h=0,1\), and \(c(h,p)=1\) for \(h\geq2\).

**Theorem.** For all \(n\geq1\), \(1\leq s\leq n\), \(0\leq h\leq n-s\), and \(p\geq1\), the exact number of distinct embedded monogenic submonoids with invariants \((h,p,s)\) is
\[
\boxed{M_{n;h,p,s}=\frac{\binom ns\,Q_{s,p}\,E_{n-s,s,h}}{c(h,p)}.}
\]
This is an integer, with zero understood when the stated cycle order does not occur. In particular the generator multiplicity is \(\varphi(p)\) for thresholds \(0\) and \(1\), but exactly \(1\) for all thresholds at least \(2\).

Let \(C_s=\sum_{p\geq1}Q_{s,p}/\varphi(p)\), the number of distinct cyclic subgroups of \(S_s\). The total \(M_n\) of **embedded** monogenic submonoids of \(T_n\) has the independent closed form
\[
\boxed{M_n=n^n-\sum_{s=1}^{n}\binom ns(s!-C_s)s^{n-s}.}
\]
Consequently,
\[
0\leq1-\frac{M_n}{n^n}\leq n\exp(\tfrac12-n/3),
\qquad\text{so}\qquad M_n\sim n^n.
\]
The first values for \(n=1,2,3,4,5,6\) are \(1,4,26,237,2842,42488\). These enumerate distinct embedded submonoids, not abstract isomorphism types.

## Assumptions and scope

All maps are arbitrary functions from the labeled set \([n]\) to itself, composed as functions; \(\langle f\rangle\) includes the full transformation monoid's identity. The stable rank is the cardinality of the eventual-image set, not the rank of the single map \(f\). The three invariants are well-defined on the embedded submonoid, because all possible generators have the same triple. The ranges above include permutation generators (\(h=0\)) and idempotent generators (\(p=1\)). The formulas do not identify submonoids under conjugacy by \(S_n\).

## Proof

**Step 1 (decomposition).** The functional digraph of every transformation consists uniquely of directed cycles and rooted trees feeding into them. Choose the \(s\) cyclic vertices, in \(\binom ns\) ways. On those vertices, the map is a permutation with exact order \(p\), in \(Q_{s,p}\) ways. All \(m=n-s\) remaining labeled vertices form a rooted directed forest whose roots are the specified cyclic vertices. To have exactly \(j\) nonempty positive-distance layers, choose their ordered sizes \((a_1,\ldots,a_j)\) with sum \(m\); allocate labels in \(m!/(a_1!\cdots a_j!)\) ways; choose each level-one parent among \(s\) cycle vertices, in \(s^{a_1}\) ways; and choose each level-\(i\) parent in level \(i-1\), in \(a_{i-1}^{a_i}\) ways. Every such assignment is acyclic and has the prescribed layers. Summing over \(j\leq h\) gives \(L_{m,s,h}\); subtracting the previous bound gives exactly \(E_{m,s,h}\). Hence the number of generator transformations with triple \((h,p,s)\) is \(\binom ns Q_{s,p}E_{n-s,s,h}\). The cycle-type expression for \(P_{s,d}\) is the standard permutation cycle census; Möbius inversion over divisors yields \(Q_{s,p}\).

**Step 2 (the generator boundary).** Any two transformations generating the same monogenic submonoid are powers of one another. If \(h=0\), the monoid is a cyclic permutation group of order \(p\), with exactly \(\varphi(p)\) generators. If \(h=1\), its powers are \(1,f,f^2,\ldots,f^p\) and satisfy \(f^{p+1}=f\); the generating elements are precisely \(f^k\) with \(1\leq k\leq p\) and \(\gcd(k,p)=1\). Their functional digraphs all have the same cyclic set, and all noncyclic points still enter that set in one step; thus \((h,p,s)\) is unchanged, and the generator count is \(\varphi(p)\). If \(h\geq2\), no exponent \(j\geq2\) satisfies \(f^j=f\), since this would force power threshold at most one. Consequently \(f\) cannot lie in \(\langle f^k\rangle\) for any \(k\geq2\), so the monoid has the unique generator \(f\). Dividing the transformation count by exactly these multiplicities proves the boxed joint formula and its integrality.

**Step 3 (total formula).** There are \(n^n\) generator transformations in total. The transformations with \(h\leq1\) are exactly those in which every offcycle vertex maps directly into the cycle set. If that set has size \(s\), their number is \(\binom ns s!s^{n-s}\). Their corresponding distinct submonoids number \(\binom ns C_s s^{n-s}\), because each cyclic subgroup of \(S_s\) represents \(\varphi(p)\) generating permutations of order \(p\). Transformations with \(h\geq2\) correspond bijectively to their own generated submonoids. Subtracting the overcount only in the two small-threshold cases gives the second boxed formula.

**Step 4 (asymptotic).** The subtraction is nonnegative and at most \(\sum_s\binom ns s!s^{n-s}\). Divide the summand by \(n^n\), set \(k=n-s\), and bound
\[
\frac{\binom ns s!s^{n-s}}{n^n}
=\prod_{i=0}^{s-1}(1-i/n)(s/n)^{n-s}
\leq\exp\left[-\frac{s(s-1)}{2n}-\frac{(n-s)^2}{n}\right]
\leq\exp(\tfrac12-n/3).
\]
The last inequality follows by completing the square: \(s^2/(2n)+(n-s)^2/n\geq n/3\), and \(s/(2n)\leq1/2\). There are at most \(n\) summands, which proves the explicit bound and \(M_n\sim n^n\).

## Verification

The attached standalone `verify.py` uses only the Python standard library. Its formula engine counts exact permutation orders by a cycle-containing-the-first-label recurrence and counts bounded-depth rooted forests by independent choices of distance layers. A separate engine exhaustively enumerates every function on \([n]\) for \(1\leq n\leq6\), constructs the entire generated monoid as an actual set of transformations, and compares the full \((h,p,s)\) distribution against the displayed formula. It also directly enumerates permutation orders for sizes up to six, and checks the generator-fiber multiplicity separately. All six tests end in `CHECK_OK` and the program ends in `VERIFY_OK`. Example: for \(n=4,h=1,p=3,s=3\), the formula gives \(12\) embedded submonoids although \(24\) transformations have that triple; for \(n=5,h=2,p=2,s=3\), it gives \(180\), with no generator division. These finite computations corroborate, but do not replace, the preceding proof for all \(n\).

Run with `python3 verify.py`.

## Relationship to prior work

Elliott, Levine, and Mitchell (arXiv:2303.12387, first public 2023-03-22), in their Theorem 1 and Lemmas 3–4, enumerate the **isomorphism types** of monogenic transformation monoids by threshold and period. Their result does not specify how many distinct labeled submonoids of \(T_n\) realize each type, nor the stable cyclic rank; the present count is a different, embedding-sensitive invariant. The functional-digraph decomposition into a root forest and a permutation on the cyclic vertices is classical and appears, for instance, in Hansen and Jaworski's study of random mappings conditioned on the number of cyclic points. East, Egri-Nagy, and Mitchell (arXiv:1403.0274, §4.1) already identify equivalent generators of the same cyclic subsemigroup; their finite computational table includes the degree-three one-generated-subsemigroup count \(26\). Thus generator equivalence itself is **not** claimed as a novel lemma, nor are the constituent permutation cycle index and rooted-forest counts. Their general subsemigroup enumeration methods do not provide the all-degree triple-refined expression or its total asymptotic. The assessed contribution is the complete embedded joint census with its correct boundary-dependent quotient and the explicit asymptotic comparison with all transformations.

## Limitations

The result is an enumeration theorem for labeled embedded monogenic submonoids, not a classification of arbitrary submonoids, their conjugacy orbits, or inverse monoids. The exponential inequality is not asserted optimal. While specific related sources have been compared by mathematical implication, exhaustive publication-priority verification is not possible; the formulas could potentially be derivable from a broader existing enumeration of finite functional digraphs or transformation subsemigroups. Finite verification reaches \(n=6\), not all integers. No independent external mathematical audit has been performed.

## References

1. L. Elliott, A. Levine, J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (first submitted 2023-03-22); *Communications in Algebra* 51 (2023), 4654–4661, DOI: 10.1080/00927872.2023.2214821. https://arxiv.org/abs/2303.12387
2. J. C. Hansen, J. Jaworski, *Random mappings with a given number of cyclical points*, *Ars Combinatoria* 94 (2010), 341–359. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/
3. J. East, A. Egri-Nagy, J. D. Mitchell, *Enumerating Transformation Semigroups*, arXiv:1403.0274; *Semigroup Forum* 95 (2017), 109–125. https://arxiv.org/abs/1403.0274
4. A. A. Grusho, *Limit Distribution of the Number of Cyclic Points in a Random Mapping of Bounded Height*, *Theory of Probability and Its Applications* 20 (1976), 533–544, DOI: 10.1137/1120059 (related bounded-height background, not used as a theorem input).
