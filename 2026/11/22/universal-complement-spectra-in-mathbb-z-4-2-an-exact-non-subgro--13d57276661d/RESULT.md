# Universal complement spectra in \(\mathbb Z_4^2\): an exact non-subgroup obstruction census

## Finding

Let \(G=(\mathbb Z/4\mathbb Z)^2\). A translational tile is a nonempty \(A\subseteq G\) with a complement \(B\subseteq G\) for which every element of \(G\) has a unique representation \(a+b\). A *universal complement spectrum* for \(A\) is one set of frequencies that restricts to an orthogonal character basis on every such \(B\). Ordinary spectrality of the tile, or the availability of separate choices for its different complements, is not sufficient.

**Affine-orbit classification.** The following table gives, for each affine class of tiles, an explicit universal complement spectrum and the exact number of frequency subgroups that are universal complement spectra. Ten of the nineteen classes have no such subgroup: one class of pairs, four classes of four-point sets, and five classes of eight-point sets. The table distinguishes these classes and gives a usable common basis even for the obstructed classes. The aggregate fact that all 2,155 tiles have a universal spectrum and 1,168 lack a subgroup-coset choice is also reported in the order-sixteen census [2]; here those totals are checks on the orbit data, not a separate contribution.

Encode \((x,y)\) by \(x+4y\) for both points and frequencies. The column \(o\) counts the distinct members of the full affine orbit that contain 0; \(c\) counts the distinct tiling complements containing 0 for that representative; \(h\) counts the universal frequency **subgroups** (not their translates). Any frequency coset is a universal spectrum if and only if the subgroup it translates is one.

| Representative \(A\) | \(o\) | \(c\) | One universal spectrum | \(h\) |
|---|---:|---:|---|---:|
| \(\{0\}\) | 1 | 1 | \(G\) | 1 |
| \(\{0,1\}\) | 12 | 8 | \(\{0,1,4,5,8,9,12,13\}\) | 0 |
| \(\{0,2\}\) | 3 | 128 | \(\{0,2,4,6,8,10,12,14\}\) | 1 |
| \(\{0,1,2,3\}\) | 6 | 64 | \(\{0,4,8,12\}\) | 1 |
| \(\{0,1,2,4\}\) | 192 | 1 | \(\{0,1,2,3\}\) | 4 |
| \(\{0,1,4,5\}\) | 48 | 3 | \(\{0,1,4,5\}\) | 0 |
| \(\{0,2,4,6\}\) | 12 | 16 | \(\{0,2,4,6\}\) | 0 |
| \(\{0,1,3,8\}\) | 24 | 4 | \(\{0,1,8,9\}\) | 2 |
| \(\{0,5,7,8\}\) | 12 | 4 | \(\{0,1,10,11\}\) | 0 |
| \(\{0,5,6,9\}\) | 16 | 1 | \(\{0,1,4,5\}\) | 0 |
| \(\{0,2,8,10\}\) | 1 | 64 | \(\{0,2,8,10\}\) | 1 |
| \(\{0,1,2,3,4,5,6,7\}\) | 12 | 4 | \(\{0,4\}\) | 0 |
| \(\{0,1,3,4,5,6,7,8\}\) | 192 | 1 | \(\{0,1\}\) | 0 |
| \(\{0,1,4,5,6,7,8,9\}\) | 96 | 1 | \(\{0,1\}\) | 0 |
| \(\{0,2,4,5,6,7,8,10\}\) | 24 | 2 | \(\{0,2\}\) | 2 |
| \(\{0,2,4,5,6,7,9,11\}\) | 12 | 2 | \(\{0,4\}\) | 0 |
| \(\{0,1,2,3,8,9,10,11\}\) | 3 | 8 | \(\{0,8\}\) | 1 |
| \(\{0,1,2,4,5,7,9,12\}\) | 48 | 1 | \(\{0,1\}\) | 0 |
| \(G\) | 1 | 1 | \(\{0\}\) | 1 |

For an arbitrary member \(A'=M A+a\) of a row, the listed frequencies \(\Lambda\) give the spectrum \(M^{-\mathsf T}\Lambda\) for all complements of \(A'\). Thus the table classifies a specific simultaneous basis choice as well as the obstruction to selecting a subgroup. An ordinary affine census [1] partitions the same tiles into nineteen classes, but does not give these simultaneous basis data.

## Assumptions and scope

All sets are ordinary subsets. The characters are \(\chi_\xi(x)=i^{\langle x,\xi\rangle}\) using the coordinate dot product modulo 4, and orthogonality uses counting measure. Affine maps have arbitrary translation and linear part in \(\mathrm{GL}_2(\mathbb Z/4\mathbb Z)\). No group other than \(G\) is classified here.

## Proof and exact replay

For a set \(S\) write \(\delta(S)=(S-S)\setminus\{0\}\). At reciprocal sizes \(|A||B|=16\), the sets are a tiling pair exactly when \(\delta(A)\cap\delta(B)=\varnothing\): a repeated sum is equivalent to a shared nonzero difference, and distinctness exhausts the group. Translating \(A\) or \(B\) independently preserves the tiling-pair condition. It suffices to check complements with 0, since translating a complement multiplies each character sum by a nonzero phase.

For each such complement \(B\), form the nonzero zero set \(Z_B\) of \(\sum_{b\in B}i^{\langle b,\xi\rangle}\). Test a zero by counting the four exponents and checking \(c_0=c_2\) and \(c_1=c_3\). Let \(D(A)\) be the intersection of \(Z_B\) over the normalized complements. For \(|\Lambda|=16/|A|\), \(\Lambda\) is universal precisely when \(\delta(\Lambda)\subseteq D(A)\); this is the pairwise orthogonality condition, and the cardinality completes the basis. A subgroup satisfies \(\delta(H)=H\setminus\{0\}\). Translation of the frequency set preserves the condition. Finally, applying \(M\) sends each complement to one for \(A'\), and the identity \(\langle M b,M^{-\mathsf T}\xi\rangle=\langle b,\xi\rangle\) transports orthogonality in both directions.

The finite calculation can be replayed by the following exhaustive steps:

1. For each \(k=1,2,4,8,16\), enumerate all \(\binom{15}{k-1}\) anchored subsets \(A\) of size \(k\). Test against all \(\binom{15}{16/k-1}\) anchored subsets \(B\) of reciprocal size, using disjointness of difference sets. Keep precisely the rows with at least one complement. There are 6,907 candidates and the counts of kept sets by size are \((1,15,311,387,1)\).
2. For each listed representative, intersect the character zero sets of the complements found in step 1. Check the displayed witness for size and differences. For the subgroup count examine the normalized sets of size \(16/k\) closed under subtraction; there are \((1,3,7,3,1)\) such subgroups in sizes \(1,2,4,8,16\), respectively. Count those whose nonzero elements lie in the intersection. This gives columns \(c\) and \(h\), with none of the representatives having zero complements.
3. For each representative, take the two generator images in \(G\) with independent reductions in \(\mathbb F_2^2\). There are \(6\cdot 4^2=96\) ordered choices: the six ordered bases modulo 2 and four lifts of each image. They are exactly the invertible matrices, since an odd determinant is a unit modulo 4. Apply every such linear map and subtract each possible image element as a translation. Deduplicate these anchored images, obtaining the column \(o\). The nineteen anchored image sets are pairwise disjoint and their union equals the kept sets from step 1. This checks both exhaustiveness and inequivalence.

As checks, the number of orbit rows by size is \((1,2,8,7,1)\), and the number with \(h=0\) is \((0,1,4,5,0)\). The anchored sizes in the latter rows sum to \((0,12,88,360,0)\). Multiplying the anchored size counts by \(16/k\) gives the corresponding labelled counts, since each point belongs to the same number of translates in any translation-invariant family. This argument also includes periodic tiles.

The accompanying `orbit_witnesses.json` encodes the table. `verify_all.py` generates normalized complements by exact-cover recursion, rather than scanning complement pairs. `verify_orbits.py` directly checks sums for each representative, its displayed spectrum and subgroup count, and the affine-orbit coverage. Both checks use integer arithmetic and scope their conclusions to this finite group.

## References

1. *Exact Fuglede census in the sixteen-point group \(\mathbb Z_4^2\)* (2026), record `27eae8f2814b`.
2. *Universal complement spectra and subgroup obstructions in all sixteen-element abelian groups* (2026), record `f64ec186b45e`, \(\mathbb Z_4^2\) row.
3. J. C. Lagarias and Y. Wang, *Spectral Sets and Factorizations of Finite Abelian Groups*, J. Funct. Anal. 145 (1997), 73–98, [DOI](https://doi.org/10.1006/jfan.1996.3008).
4. B. Farkas, M. Matolcsi and P. Móra, *On Fuglede’s Conjecture and the Existence of Universal Spectra*, J. Fourier Anal. Appl. 12 (2006), 483–494, [arXiv:math/0612016](https://arxiv.org/abs/math/0612016).
