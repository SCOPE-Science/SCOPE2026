# Universal complement spectra and subgroup obstructions in all sixteen-element abelian groups

## Finding

Let \(G\) be any finite abelian group of order sixteen and let \(A\subseteq G\) be a nonempty translational tile: at least one \(B\subseteq G\) satisfies \(A\oplus B=G\), meaning each group element has exactly one representation \(a+b\). A *universal complement spectrum* of \(A\) is a character set \(\Lambda\subseteq\widehat G\) that is an orthogonal basis of functions on **every** such \(B\). For each of the five isomorphism types of \(G\), every tile has a universal complement spectrum.

The following complete census distinguishes these spectra from spectra that can be cosets of subgroups of \(\widehat G\). The second count comprises tiles \(A\) having **no** universal complement spectrum that is a subgroup coset (though every one has a universal spectrum).

| \(G\) | All nonempty tiles | Tiles requiring a non-subgroup universal spectrum |
| --- | ---: | ---: |
| \(\mathbb Z_{16}\) | 795 | 764 |
| \(\mathbb Z_8\times\mathbb Z_2\) | 1,611 | 1,056 |
| \(\mathbb Z_4^2\) | 2,155 | 1,168 |
| \(\mathbb Z_4\times\mathbb Z_2^2\) | 3,147 | 896 |
| \(\mathbb Z_2^4\) | 4,747 | 0 |

The full size-resolved data, ordered by tile cardinality \(1,2,4,8,16\), are respectively:

| \(G\) | Tile counts | Counts requiring non-subgroup spectra |
| --- | --- | --- |
| \(\mathbb Z_{16}\) | \((16,120,380,278,1)\) | \((0,112,376,276,0)\) |
| \(\mathbb Z_8\times\mathbb Z_2\) | \((16,120,732,742,1)\) | \((0,96,688,272,0)\) |
| \(\mathbb Z_4^2\) | \((16,120,1244,774,1)\) | \((0,96,352,720,0)\) |
| \(\mathbb Z_4\times\mathbb Z_2^2\) | \((16,120,1436,1574,1)\) | \((0,64,576,256,0)\) |
| \(\mathbb Z_2^4\) | \((16,120,1820,2790,1)\) | \((0,0,0,0,0)\) |

Thus all five groups retain simultaneous Fourier bases for every tiling-complement family, but a subgroup-coset restriction is lossless for **every** tile precisely in the elementary abelian case. The cyclic example \(A=\{0,1\}\subset\mathbb Z_{16}\) already requires a non-subgroup universal spectrum: its eight-point complements are translates of the even subgroup, and \(\{0,1,\ldots,7\}\) is a common spectrum, whereas the unique eight-character subgroup has a repeated restriction on the even subgroup.

## Assumptions and scope

All groups are written in the standard coordinate models given above, with coordinatewise addition. Their duals are identified with the same coordinate models by characters
\[
\chi_y(x)=\exp\!\left(2\pi i\sum_{j=1}^d \frac{x_jy_j}{n_j}\right),\qquad G=\prod_{j=1}^d\mathbb Z_{n_j}.
\]
A character spectrum of \(B\) consists of precisely \(|B|\) distinct characters, orthogonal with respect to counting measure on \(B\). The counts concern **labelled subsets** of each specified group, not quotient classes under affine automorphisms. Translations of the frequency set do not affect the spectrum property; a frequency-coset spectrum is therefore equivalent to a subgroup spectrum after frequency translation. No claim concerns groups of order greater than sixteen.

## Proof

**1. Exact Fourier criterion.** For nonempty \(B\subseteq G\), put \(Z_B=\{y\in\widehat G\setminus\{0\}:\sum_{b\in B}\chi_y(b)=0\}\). Then \(\Lambda\) is a spectrum of \(B\) if and only if \(|\Lambda|=|B|\) and every nonzero pairwise frequency difference belongs to \(Z_B\). This follows immediately by taking inner products of the restricted characters. For a tile \(A\), define
\[
D_A=\bigcap_{B:\,A\oplus B=G} Z_B.
\]
Consequently, a universal complement spectrum exists if and only if the difference graph of \(D_A\), with vertices \(\widehat G\), contains a clique of size \(16/|A|\). A universal subgroup-coset spectrum exists if and only if some subgroup \(H\le\widehat G\) of order \(16/|A|\) satisfies \(H\setminus\{0\}\subseteq D_A\).

**2. Exact root test.** Each group has exponent \(E\in\{2,4,8,16\}\). Put \(\zeta=\exp(2\pi i/E)\), and for \(B,y\) let \(c_r\) count those \(b\in B\) for which \(\chi_y(b)=\zeta^r\). As \(\Phi_E(X)=X^{E/2}+1\), the cyclotomic integer \(\sum_r c_r\zeta^r\) vanishes if and only if
\[
c_r=c_{r+E/2}\quad(0\le r<E/2).
\]
This is a necessary and sufficient **integer** condition, not a floating-point approximation. It is used in both executable certificates.

**3. Exhaustive factorization and spectrum test.** A tile must have cardinality \(k\) dividing sixteen. For every \(k\in\{1,2,4,8,16\}\), `check_direct.py` enumerates **all** \(\binom{16}{k}\) row sets \(A\) and all \(\binom{15}{16/k-1}\) complementary-size subsets \(B\) containing zero. Each pair is tested by directly forming its sixteen sums and verifying that no group element repeats. Translation of \(B\) preserves its Fourier zeros, so testing complements containing zero includes every possible complement for the universal-spectrum question. The certificate intersects their exact Fourier zero sets, scans all frequency subsets of the required cardinality containing zero, and separately scans all frequency subgroups. Frequency translation permits restricting to candidate spectra containing zero. The reported counts are incremented only after a successful direct sumset test and the two exhaustive spectral tests.

**4. Independent complete check.** `check_recursive.py` instead enumerates only translates of tiles \(A\) containing zero. For each, it constructs all translation complements containing zero by recursively covering the first uncovered point with a disjoint translate \(A+b\). Every valid complement appears: that first uncovered point belongs to a uniquely determined translate in any tiling, and the algorithm branches over all such translates. It intersects the cyclotomic zero sets and finds a requisite clique by backtracking, then checks every frequency subgroup. Finally the counts from zero-containing tiles of size \(k\) are multiplied by \(16/k\), as follows by double counting pairs \((A,a)\) with \(a\in A\) and using translation invariance. Thus the two methods differ in both exhaustive factorization strategy and spectrum search strategy.

The two standalone checkers independently produce exactly the table above. Every tile has at least one universal spectrum, so the positive statement is certified for all cases; the explicit enumeration of all frequency subgroups certifies the negative subgroup-coset statements. The integer verification is exhaustive, rather than a sample, probabilistic test or numerical conjecture.

## Verification

With Python 3, run `python check_recursive.py` and `python check_direct.py` in the directory containing the embedded artifacts. Their JSON outputs match `recursive_results.json` and `direct_results.json` respectively after parsing, with the additional `examples` field present only in the recursive output. In particular, compare each group's `tile_count`, `tile_count_by_size`, `non_subgroup_universal_spectrum_count`, `non_subgroup_count_by_size`, and `all_tiles_have_universal_spectrum`. Both were run successfully from the standalone package. No third-party packages or input files are needed. The methods perform exact integer arithmetic throughout.

## Relationship to prior work

Lagarias and Wang introduced universal spectra for factorizations of finite abelian groups, and their 1997 Theorems 1.2–1.3 already cover universal-spectrum **existence in cyclic groups of prime-power order**. Kolountzakis and Matolcsi (2004) constructed failures of universal complement spectra in substantially larger finite groups, establishing that simultaneous spectra are not automatic in general; Farkas, Matolcsi and Móra (2006) clarify the general Fourier-zero criterion and dimensional implications. Thus the existence statement for \(\mathbb Z_{16}\) is not asserted as new, nor is the universal-spectrum concept or the basic difference-graph criterion.

Earlier exact censuses already establish the total tile counts for \(\mathbb Z_4^2\) and \(\mathbb Z_4\times\mathbb Z_2^2\), and a separate computation already determines the \(1{,}168\) non-subgroup-obstruction count for \(\mathbb Z_4^2\). The distinct result here is the **joint five-isomorphism-type classification**, including subgroup-coset counts for the other types not supplied by the cited records, the positive universal-spectrum check for every tile in all five groups, and the contrast with \(\mathbb Z_2^4\). Existing Fourier-minor rank tables and individual spectral/tiling equivalences do not themselves imply this simultaneous-complement incidence table.

## Limitations

This is a finite exact classification at order sixteen. It does not prove any universal-spectrum property for all finite abelian \(2\)-groups, provide formulas for arbitrary group order, or count the total number of different universal spectra per tile. The novelty comparison is bounded by accessible literature and searchable published records; an unindexed equivalent enumeration cannot be excluded. No independent mathematical audit has been performed.

## References

1. J. C. Lagarias and Y. Wang, *Spectral Sets and Factorizations of Finite Abelian Groups*, Journal of Functional Analysis **145** (1997), 73–98. DOI: https://doi.org/10.1006/jfan.1996.3008 ; author-hosted text: https://websites.umich.edu/lagarias/doc/fuglede.pdf
2. J. C. Lagarias and S. Szabó, *Universal Spectra and Tijdeman's Conjecture on Factorization of Cyclic Groups*, arXiv:math/0008132v1 (2000). https://arxiv.org/abs/math/0008132
3. M. N. Kolountzakis and M. Matolcsi, *Tiles with No Spectra*, arXiv:math/0406127v1 (2004). https://arxiv.org/abs/math/0406127
4. B. Farkas, M. Matolcsi and P. Móra, *On Fuglede's Conjecture and the Existence of Universal Spectra*, arXiv:math/0612016v1 (2006). https://arxiv.org/abs/math/0612016
5. *Exact Fuglede census in the sixteen-point group \(\mathbb Z_4^2\)*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-fuglede-census-in-the-sixteen-point-group-mathbb-z-4-2--27eae8f2814b
6. *Exact Fuglede census for \(\mathbb Z_4\times\mathbb Z_2^2\)*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-fuglede-census-for-mathbb-z-4-times-mathbb-z-2-2--5c6c05045dc1
