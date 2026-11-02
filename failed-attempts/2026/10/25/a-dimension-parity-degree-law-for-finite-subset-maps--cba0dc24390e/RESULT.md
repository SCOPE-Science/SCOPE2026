# A dimension-parity degree law for finite-subset maps

## Finding

Let \(M,N\) be closed connected smooth \(n\)-manifolds with \(n\ge 2\), let \(k\ge 1\), and let \(f:M\to N\) be continuous. Let \(\operatorname{Sub}_k(X)\) be the space of nonempty subsets of \(X\) of cardinality at most \(k\), with the quotient topology induced by \(X^k\), and let \(\operatorname{Sub}_k(f)\) be the induced map. Then

\[H_{nk}(\operatorname{Sub}_k(M);\mathbb{F}_2)\cong H_{nk}(\operatorname{Sub}_k(N);\mathbb{F}_2)\cong\mathbb{F}_2,\]

and the induced map on these groups is multiplication by
\[\deg_2(\operatorname{Sub}_k(f))=(\deg_2 f)^k=\deg_2 f.\]
If \(n\) is even and both manifolds are oriented, their top integral homology groups for the finite-subset spaces are each isomorphic to \(\mathbb{Z}\), and
\[\deg(\operatorname{Sub}_k(f))=(\deg f)^k.\]
For \(k\ge2\), the top integral homology of \(\operatorname{Sub}_k(M)\) is zero when \(n\) is odd or \(M\) is nonorientable. This is an orientation-sensitive, coefficient-sensitive degree law for the finite-subset construction.

## Assumptions and scope

The manifolds are closed, connected, smooth, and of the same dimension \(n\ge2\). The integer-degree assertion assumes that both manifolds are oriented and that \(n\) is even. The mod-two assertion does not require orientability. The space \(\operatorname{Sub}_k(X)\) consists of subsets of sizes from one through \(k\), not multisets; it is the quotient of \(X^k\) under equality of underlying finite subsets. No claim is made for noncompact manifolds, manifolds with boundary, or dimension one. Dimension one is genuinely exceptional: for the circle, finite-subset spaces have a different degree exponent.

## Proof

Put \(F_k(M)=\{(x_1,\ldots,x_k)\in M^k:x_i\ne x_j\text{ whenever }i\ne j\}\). The top stratum of \(\operatorname{Sub}_k(M)\) is the connected unordered configuration manifold \(F_k(M)/\mathfrak{S}_k\), of dimension \(nk\). Its complement is \(\operatorname{Sub}_{k-1}(M)\), of dimension at most \(n(k-1)\). Since \(n\ge2\), this complement has codimension at least two. The long exact sequence of the pair and the dimension bound identify top homology with the relative top group, which is the Borel–Moore top homology of the top stratum. Consequently the top mod-two group is \(\mathbb{F}_2\). The top stratum is orientable over \(\mathbb{Z}\) exactly when \(M\) is orientable and either \(n\) is even or \(k=1\): exchanging two \(n\)-dimensional factors changes product orientation by \((-1)^{n^2}=(-1)^n\). Thus for even \(n\) and oriented \(M\), the top integral group is \(\mathbb{Z}\); for odd \(n\) with \(k\ge2\), or nonorientable \(M\), it is zero.

First suppose \(f\) is smooth. Choose a configuration \(\{y_1,\ldots,y_k\}\) of distinct regular values. A point in its inverse image under \(\operatorname{Sub}_k(f)\) must contain exactly one point of \(f^{-1}(y_i)\) for every \(i\), so the preimages in the top stratum are obtained by choosing one preimage independently in each fiber. Modulo two, their number is
\[\prod_{i=1}^k \# f^{-1}(y_i)\pmod 2=(\deg_2 f)^k.\]
This is the induced top mod-two degree. Since \(\deg_2 f\in\{0,1\}\), its \(k\)-th power equals itself.

If \(n\) is even and both manifolds are oriented, the same regular-value count uses signs. The sign of a point in the unordered configuration stratum is the product of the local signs in the individual fibers, because permutations preserve product orientation in even dimension. Summing over all independent choices factors as
\[\prod_{i=1}^k\left(\sum_{x\in f^{-1}(y_i)}\operatorname{sign}(D f_x)\right)=(\deg f)^k.\]
This is the integer degree of the induced map. A continuous map between smooth closed manifolds is homotopic to a smooth map, and the finite-subset construction preserves homotopies, so the formulas hold for continuous \(f\).

## Verification

The dimension bound on \(\operatorname{Sub}_{k-1}(M)\) is \(n(k-1)\le nk-2\), which removes both adjacent homology groups needed in the pair exact sequence. The top-stratum orientation sign is the permutation sign on \(k\) blocks of dimension \(n\); a transposition contributes \((-1)^n\). The regular-value count has no multiplicity ambiguity: a target subset has \(k\) distinct points, so every preimage subset mapping onto it contains exactly one preimage of each target point. The proof is a degree count, not a finite enumeration. The one-dimensional case is excluded rather than inferred from this argument.

## Relationship to prior work

Tuffley’s study of finite subset spaces of closed surfaces proves the integer degree-power formula for maps between closed oriented surfaces and records the top mod-two homology framework for finite-subset spaces. His earlier circle paper gives a different exponent for \(\operatorname{Sub}_k(S^1)\), matching the explicit dimension-one exception. Handel’s work establishes foundational homotopy properties for these spaces. The present statement extends the coefficient-sensitive degree calculation from oriented surfaces to all even-dimensional oriented manifolds and gives the orientation-free mod-two degree law in every dimension \(n\ge2\). published-finding corpus searches returned related finite-subset homology and group-action findings, but no exact all-dimensional induced-degree statement. The proof is an extension of the regular-value argument, so the novelty claim is limited to this general formulation; an uninspected treatment may state an equivalent result.

## Limitations

The result concerns only top-degree homology. It does not determine lower homology, the homotopy type of \(\operatorname{Sub}_k(M)\), or the action of \(\operatorname{Sub}_k(f)\) on other groups. It assumes closed connected smooth manifolds of dimension at least two. The integral degree formula is asserted only for even-dimensional oriented manifolds; for odd dimension and \(k\ge2\), the top integral group vanishes. The primary surface theorem is inspected directly, but one potentially relevant paper on top homology of finite-subset spaces was available only as an excerpt; this leaves a literature-overlap risk.

## References

1. C. Tuffley, “Finite subset spaces of closed surfaces,” arXiv:math/0311371 (first public posting 21 November 2003).
2. C. Tuffley, “Finite subset spaces of \(S^1\),” *Algebraic & Geometric Topology* 2 (2002), 1119–1145; arXiv:math/0209077.
3. D. Handel, “Some homotopy properties of spaces of finite subsets of topological spaces,” *Houston Journal of Mathematics* 26 (2000), no. 4.
4. “Remarks on Finite Subset Spaces,” *Homology, Homotopy and Applications* 11 (2009), starting at p. 229; the accessible excerpt discusses top integral homology and orientation parity.
