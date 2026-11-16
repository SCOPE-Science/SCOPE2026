# First Fourier-rank separation of Coxeter antichains and order ideals

## Finding

For each irreducible simply-laced root system of rank at most four, let \(P\) be its positive-root poset. Its antichains \(\mathcal A(P)\) and downward order ideals \(\mathcal J(P)\) are canonically equinumerous, through sending an antichain to the ideal it generates. Regard each family separately as a subset of the same Boolean group \(G=\mathbb F_2^{P}\), using its zero-one incidence vectors. Let \(T_{\mathcal F}\) denote unnormalized counting convolution by the indicator of a family \(\mathcal F\subset G\).

The exact ranks and optimal endpoint projection norms are:

| Root system | Positive roots | Size of each family | \(\operatorname{rank}T_{\mathcal A}\) | \(\operatorname{rank}T_{\mathcal J}\) | \(\Lambda_{1,\infty}(\mathcal A)\) | \(\Lambda_{1,\infty}(\mathcal J)\) |
|---|---:|---:|---:|---:|---:|---:|
| \(A_1\) | 1 | 2 | 1 | 1 | \(1\) | \(1\) |
| \(A_2\) | 3 | 5 | 8 | 8 | \(1\) | \(1\) |
| \(A_3\) | 6 | 14 | 46 | 46 | \(51/16\) | \(51/16\) |
| \(A_4\) | 10 | 42 | **811** | **810** | \(3819/512\) | \(1901/256\) |
| \(D_4\) | 12 | 50 | **3294** | **3272** | \(10053/1024\) | \(1981/256\) |

Here \(\Lambda_{1,\infty}(\mathcal F)\) denotes the minimum of the operator norm of **any** real or complex linear projection onto \(\operatorname{ran}T_{\mathcal F}\), computed in either \(\ell^1(G)\) or \(\ell^\infty(G)\). The minimizers are Fourier-support projections; the asserted optimum is not limited to translation-invariant competitors.

Consequently, rank four is the *first* rank at which the antichain-to-ideal correspondence fails to preserve convolution rank among irreducible simply-laced root systems. In either rank-four type, the two naturally embedded families are not related by an invertible affine automorphism of their Boolean ambient group. For the \(D_4\) diagram-triality action, the zero-frequency sets consist of, respectively, \(10\), \(64\), \(100\) orbits of sizes \(1\), \(3\), \(6\) for antichains; and \(8\), \(76\), \(98\) such orbits for ideals.

## Assumptions and scope

The root order is \(\alpha\le\beta\) exactly when \(\beta-\alpha\) is a nonnegative integer combination of simple roots. The types under consideration are exactly \(A_1,A_2,A_3,A_4,D_4\); \(D_3\) is \(A_3\), and reducible root systems are excluded. In type \(A_r\), the positive-root coefficient vectors are the nonempty intervals of ones in \(r\) coordinates. For \(D_4\), use simple roots \(e_1-e_2,e_2-e_3,e_3-e_4,e_3+e_4\) in that order and all twelve roots \(e_i\pm e_j\) with \(i<j\). Thus every binary coordinate corresponds to a positive root, not to a simple root or a block of a partition.

For \(\mathcal F\subseteq G\), define the unnormalized Walsh multiplier at \(u\in G\) by
\[
W_{\mathcal F}(u)=\sum_{x\in\mathcal F}(-1)^{\langle u,x\rangle}.
\]
Counting convolution is \((T_{\mathcal F} f)(x)=\sum_{y\in\mathcal F}f(x+y)\). The rank means complex (equivalently, real) matrix rank on functions on the entire finite group, not the rank of a poset incidence matrix.

## Proof

**Exact root-family enumeration.** In simple-root coordinates comparability is componentwise. A mask represents an antichain exactly when none of its selected positive roots are comparable. A mask represents a downward ideal exactly when it contains every root below each selected root. Both predicates are finite explicit Boolean tests. Independently, recursively adjoining incomparable roots generates every antichain, and taking its down-closure generates every ideal. The two methods agree at every rank considered. The family counts in the table are therefore exhaustive, not samples.

**Exact convolution ranks.** Walsh characters diagonalize each counting-convolution operator, with eigenvalues \(W_{\mathcal F}(u)\); hence
\[
\operatorname{rank}T_{\mathcal F}=|G|-|\{u:W_{\mathcal F}(u)=0\}|.
\]
An exact-integer fast Walsh–Hadamard transform and separate direct sums at *every* frequency agree on all multiplier values. The zero counts for \(\mathcal A\) versus \(\mathcal J\) are, in the displayed type order, \((1,1),(0,0),(18,18),(213,214),(802,824)\). Subtracting from \(2^{|P|}\) proves each rank, including the first separation.

For a concrete rank-four obstruction in type \(A_4\), take the frequency whose simple-root coefficient supports are \((0,0,1,0)\), \((0,0,1,1)\), \((0,1,0,0)\), \((0,1,1,0)\). Its antichain and ideal multipliers are \(2\) and \(0\), respectively. Another frequency, with supports \((0,0,0,1)\), \((0,0,1,1)\), \((0,1,0,0)\), has respective multipliers \(0\) and \(-10\). The full counts are needed for the affine-invariant rank obstruction; these individual witnesses illustrate that both nullspaces have exclusive frequencies.

**Sharp unrestricted projection norm.** Put \(E=\{u:W_{\mathcal F}(u)\ne0\}\), and \(H(x)=\sum_{u\in E}(-1)^{\langle u,x\rangle}\). The Fourier-support projection onto \(\operatorname{ran}T_{\mathcal F}\) has kernel \(H(x)/|G|\) and both endpoint operator norms equal \(|G|^{-1}\sum_x|H(x)|\). For any other bounded linear projection onto that same range, averaging its conjugates by all group translations gives the Fourier-support projection without increasing the \(\ell^1\) or \(\ell^\infty\) norm. This proves global minimality among real and complex projections. A second exact Walsh transform computes the stated rational constants. The values are determined by integer arithmetic and reduction of rational fractions.

**Triality orbit check.** Permuting the three terminal simple roots of \(D_4\) induces six coordinate permutations of its twelve positive roots, preserving both families and their Walsh multipliers. Exhaustive enumeration of the resulting orbits on zero frequencies gives the orbit counts in the finding. Each orbit distribution has the claimed weighted total, \(802\) or \(824\).

## Verification

Run `python3 verify.py --csv` in the same directory as the supplied `verify.py`. This standard-library-only program regenerates `spectrum.csv` in a deterministic lexicographic root ordering. It independently enumerates antichains and ideals, evaluates every Walsh sum directly, compares with an exact fast transform, checks both Parseval identities, computes the canonical projection norms, and checks triality-orbit sizes. All five root types and both embedded families are tested exhaustively. The expected final marker is `ROOT_POSET_FOURIER_RANK4_PASS type_count=5 spectral_rows=154`.

The file `spectrum.csv` provides every signed multiplier and its multiplicity, not just ranks or norm summaries. No floating-point arithmetic, random sampling, external mathematical library, or infinite extrapolation enters the proof of the finite classification.

## Relationship to prior work

Positive-root posets, their antichains as nonnesting partitions, and the canonical correspondence with order ideals are classical. Panyushev studies covering polynomials of root posets and their ideal lattices, and Armstrong–Stump–Thomas construct a uniform bijection involving nonnesting and noncrossing partitions. Conflitti–Mamede give a type-\(D\) noncrossing/nonnesting bijection. Their inspected formulations address enumerative and bijective properties, not the Boolean coordinate-character convolution ranks or optimal endpoint projection constants here. General Fourier diagonalization and translation averaging are also established principles; only their exact evaluations on these two natural embeddings are asserted as the specific finding. The cited works do not, by equinumerosity alone, imply equality or inequality of the full signed Fourier spectra.

## Limitations

This is a complete finite classification **only through simply-laced rank four**. No claim is made about higher ranks, arbitrary root types, other embeddings of Coxeter objects, or inequivalence under nonlinear maps. A rank mismatch obstructs invertible affine equivalence, not every combinatorial bijection. Literature comparison is bounded and does not certify historical priority. No independent external mathematical audit was performed.

## References

1. D. I. Panyushev, *Two covering polynomials of a finite poset, with applications to root systems and ad-nilpotent ideals*, arXiv:math/0502386, first posted 2005-02-17. https://arxiv.org/abs/math/0502386
2. A. Conflitti and R. Mamede, *On Noncrossing and nonnesting partitions of type D*, arXiv:0905.4371, first posted 2009-05-27. https://arxiv.org/abs/0905.4371
3. D. Armstrong, C. Stump and H. Thomas, *A uniform bijection between nonnesting and noncrossing partitions*, arXiv:1101.1277, first posted 2011-01-06. https://arxiv.org/abs/1101.1277
