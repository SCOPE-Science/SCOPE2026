# Constant-square-root fibers in partition-preserving transformation monoids

## Finding

Consider the partition-preserving total transformation monoid of an arbitrary finite nonempty partition, including partitions with unequal block sizes. We determine the cardinality of **every fiber of the square map above a specified constant transformation, refined by the entire induced block map**.

Let \(\mathcal P=\{C_0,\ldots,C_{m-1}\}\) partition a labeled finite nonempty set \(X\). Set \(n_i=|C_i|\ge1\), choose \(u\in C_0\), and let \(c_u(x)=u\). A total transformation \(f:X\to X\) belongs to \(T(X,\mathcal P)\) precisely when each block has image contained in some block. Since blocks are nonempty, there is a unique induced map \(e_f:\{0,\ldots,m-1\}\to\{0,\ldots,m-1\}\), determined by \(f(C_i)\subseteq C_{e_f(i)}\).

For each block map \(e\), write
\[
H_e=\#\{f\in T(X,\mathcal P):f\circ f=c_u,\ e_f=e\}.
\]
Then \(H_e>0\) exactly if \(e(0)=0\) and \(e(e(i))=0\) for every block index \(i\). For these and only these block maps, define
\[
F_e=\{j\in\{1,\ldots,m-1\}:e(j)=0\},\qquad
N_j=\sum_{\substack{i\ne0\\e(i)=j}}n_i\quad(j\in F_e).
\]
The exact prescribed-block-map fiber count is
\[
\boxed{H_e=\sum_{k=0}^{n_0-1}\binom{n_0-1}{k}
 k^{n_0-1-k}\prod_{j\in F_e}
 \left(\sum_{h=0}^{n_j}\binom{n_j}{h}k^{n_j-h}h^{N_j}\right).}
\]
For inadmissible block maps, \(H_e=0\). Adopt \(0^0=1\) throughout, including combinatorial empty-choice cases; empty products are one.

Consequently there are exactly
\[
\boxed{\sum_{r=0}^{m-1}\binom{m-1}{r}r^{m-1-r}}
\]
nonempty induced-block-map square-root fibers, independently of the block sizes. The total number of square roots of \(c_u\) in this monoid is the finite sum \(\sum_e H_e\). For two blocks of sizes \((a,b)\), with \(u\) in the size-\(a\) block, this simplifies to
\[
\boxed{\sum_{k=0}^{a-1}\binom{a-1}{k}k^{a-1-k}(k+1)^b.}
\]
Moreover \(c_u\) has exactly one square root in the monoid if and only if \(|X|\le2\), or there are exactly two blocks and the block containing \(u\) has size one.

## Assumptions and scope

All maps are total functions, not partial injections or arbitrary relations. The partition is labeled for bookkeeping, but the count is invariant under relabeling that preserves block sizes and the distinguished block. No uniform-block assumption is made. Composition is function composition; \(f^2=c_u\) means \(f(f(x))=u\) for **every** \(x\in X\). No group-theoretic or characteristic assumptions enter the proof.

## Proof

**1. Block-map constraints and root fixation.** If \(f^2=c_u\), then \(f^2(u)=u\). Suppose \(f(u)=v\ne u\); then \(f(v)=u\), and hence \(f^2(v)=v\ne u\), a contradiction. Thus \(f(u)=u\). Consequently \(e_f(0)=0\). Since \(f^2(C_i)\subseteq C_{e_f(e_f(i))}\) is also the singleton \(\{u\}\subseteq C_0\), one has \(e_f(e_f(i))=0\) for every \(i\). These conditions are necessary.

**2. Structure of admissible block maps.** Fix an \(e\) with \(e(0)=0\) and \(e^2(i)=0\). Every nonroot index is either in \(F_e\), mapping directly to index zero, or maps to one of the indices in \(F_e\). In particular, no nonroot index can be fixed by \(e\), and no block-level cycle other than the root fixed point is possible.

**3. Choice within the root block.** Every point of \(X\) maps either to \(u\) or to a point that maps to \(u\). Choose \(k\) of the \(n_0-1\) points of \(C_0\setminus\{u\}\) as direct preimages of \(u\) (the root's children). The other \(n_0-1-k\) points of \(C_0\) may map to any of these \(k\) children; they may not map directly to \(u\), otherwise they would also be children. This gives \(\binom{n_0-1}{k}k^{n_0-1-k}\) choices, with \(k\) ranging from zero to \(n_0-1\).

**4. Choice in each first-layer block.** Fix \(j\in F_e\). All \(n_j\) points of \(C_j\) map to \(C_0\). Choose exactly \(h\) of them to map directly to \(u\); the other \(n_j-h\) points must map to one of the \(k\) selected root-block children. There are \(\binom{n_j}{h}k^{n_j-h}\) such choices. Now, for any source block \(C_i\) satisfying \(e(i)=j\), each of its \(n_i\) points maps into \(C_j\), and must land at one of the \(h\) points whose image is \(u\). Across all such source blocks there are \(N_j\) independent point choices, yielding \(h^{N_j}\). Summing over \(h\) yields the stated parenthesized factor.

**5. Multiplication and exhaustion.** Choices within distinct blocks are independent. Conversely, the construction produces a partition-preserving total function with induced map \(e\) and square identically \(u\). The partition of image points into direct-root children and indirect points is uniquely recoverable from \(f\); hence no function is counted twice. Summing over \(k\) completes the formula. Every admissible \(e\) occurs: take \(k=0\), map all points in root and first-layer blocks to \(u\), and send every point in each second-layer block to an arbitrary element of its first-layer target block. Thus the support criterion is also sufficient.

**6. Number of admissible block maps.** Let \(r=|F_e|\). Choose those \(r\) first-layer block indices in \(\binom{m-1}{r}\) ways; every remaining nonroot index must map to one of them, giving \(r^{m-1-r}\) choices. The sum over \(r\) establishes the support count. For \(m=2\), the unique admissible induced block map sends both blocks to index zero; since its first-layer block has no block-level preimages, its factor is \((k+1)^b\), yielding the two-block formula.

**7. Unique-square-root threshold.** The constant map \(c_u\) is always one square root. If \(|X|\le2\), no depth-two nonconstant rooted map exists. If \(m=2\) and \(n_0=1\), the only admissible induced map sends both blocks into the singleton root block, so only \(c_u\) exists. In all remaining cases a nonconstant square root exists. For \(m=1\) with \(|X|\ge3\), select distinct \(x,y\ne u\) and set \(f(y)=x\), \(f(x)=u\), and send all other points to \(u\). For \(m=2\) with \(n_0\ge2\), choose \(x\in C_0\setminus\{u\}\) and \(y\in C_1\), set \(f(y)=x\), and send every other point to \(u\). For \(m\ge3\), choose two different nonroot blocks, send all points of one to a chosen point in the other, and all remaining points to \(u\). Each construction preserves the partition and squares to \(c_u\), proving the asserted equivalence.

## Verification

The bundled Python 3 program `square_root_partition_checker.py` computes the proposed formula from the block-size and induced-block-map data. Separately, it iterates over every labeled total function on the underlying set, tests composition twice, and checks preservation of the partition; it groups the survivors by their exact induced block map. The two distributions agree for all tested choices of distinguished root block in 15 block-size profiles, including blocks of unequal sizes and partitions with three blocks. The recorded stdout is in `square_root_partition_verification.txt`.

Run with `python3 square_root_partition_checker.py`; there are no third-party dependencies. Examples include total counts \(18,29,60\) for the respective root blocks of a partition of sizes \((1,2,3)\), and total count \(28\) for each root block of sizes \((2,2,2)\). Exhaustive finite tests validate small cases but are not substitutes for the proof for all finite partitions.

## Relationship to prior work

Araújo–Bentz–Mitchell–Schneider introduce the general partition-preserving transformation monoid and determine its generation rank [1]. Dolinka–East–Mitchell enumerate its idempotents and analyze idempotent generation [2]. Neither inspected result states the prescribed constant-square-root counts by induced block character. Earlier work of Snowden and Howie on square roots of full transformations, including the accessible thesis [3], and Higgins's full-transformation root construction [4], provides general root structure without partition-preserving fiber weights. The specialization to a one-block partition is a full-transformation case and is not claimed as new. The present theorem refines the root-count problem by the induced block map for arbitrary unequal block sizes, rather than supplying a novel general square-root existence criterion in the full monoid.

## Limitations

Only square roots of a **constant** target are counted; arbitrary target transformations, all higher powers, semigroup multiplication outside the specified fiber, and general rank distributions are not classified. The formula is an exact finite sum, not a universal polynomial-size algorithm in the number of blocks. Although relevant open literature and mathematical record statements were compared, an older equivalent partition-restricted enumeration may remain unidentified. The verification data cover only small finite instances.

## References

1. J. Araújo, W. Bentz, J. D. Mitchell, C. Schneider, *The rank of the semigroup of transformations stabilising a partition of a finite set*, arXiv:1404.1598v1, posted 6 April 2014. https://arxiv.org/abs/1404.1598
2. I. Dolinka, J. East, J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520v1, posted 9 April 2015. https://arxiv.org/abs/1504.02520
3. E. Mary Snowden, *Square Roots in Full Transformation Semigroups*, University of St Andrews MSc thesis, July 1979, accessible at https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/22136/EMarySnowdenMScThesis1979_original_C.pdf?sequence=1
4. P. M. Higgins, *A Method for Constructing Square Roots in Finite Full Transformation Semigroups*, Canadian Mathematical Bulletin 29 (1986), 344–351, doi:10.4153/CMB-1986-053-2. https://doi.org/10.4153/CMB-1986-053-2
5. M. Snowden and J. M. Howie, *Square Roots in Finite Full Transformation Semigroups*, Glasgow Mathematical Journal 23 (1982), 137–149. https://doi.org/10.1017/S0017089500004912
