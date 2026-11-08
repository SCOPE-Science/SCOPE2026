# Self-review

## Correctness — PASS

For each odd prime \(p\ge3\), verify the defining relations of the four one-dimensional and \(p-1\) two-dimensional unitary representations of \(\operatorname{Dic}_p\). Their squared dimensions sum to \(4p\), so they give all regular Fourier blocks. The odd blocks satisfy \(M_k^*M_k=(|A_k|^2+|B_k|^2)I\), and the even blocks have squared singular values \((|A_k|\pm|B_k|)^2\). Character zero conditions and modular arithmetic yield the five nullity classes; weighted separation counting yields every support count, including the \(p=3\) collision. Sharp cosine spacing and the conjugate-character endpoint give the exact positive condition-number range and both optimizer classes. The standalone checker evaluated 2450 finite rank instances, 525 explicit singular-spectrum comparisons, and the full support count for \(p=3,5\). The proof, not the finite check, establishes all dimensions.

## Originality — PASS, with historical risk

The closest full-text source, Arezoomand–Taeri (2013, Corollary 9), supplies a general characteristic-polynomial formula for Cayley digraphs with a cyclic index-two subgroup; it does not present singular values or an exact balanced-dicyclic support census. Eigenvalues alone do not fix the singular values of nonnormal convolution operators. The general Fourier-block machinery is classical and is not claimed as new. Ghorbani (2015) treats spectra of normal edge-transitive dicyclic Cayley graphs, not an identified complete arbitrary directed balanced four-tap family; the primary full text was not accessible, so coverage risk persists. A published three-tap generalized-dihedral classification and an earlier balanced four-tap generalized-dihedral theorem concern inversion semidirect products, not the nontrivial dicyclic central extension. The odd projective Fourier blocks and exhaustive separated-support census here are not inherited from that quotient. The bounded comparison of relevant published results found no matching full theorem, but this is not a proof of priority.

## Mathematical value — PASS

The two-plus-two selection is the smallest balanced support with genuine interaction between the cyclic and noncyclic cosets. The result classifies a natural singular convolution family completely: all nonzero and zero singular values, the exact count of every rank stratum, and the best/worst stable recovery factor with equality classes. The extremal condition number is reached even with minimal one-dimensional kernel, whereas the maximal-kernel antipodal configuration is perfectly conditioned on its image. This rank/stability reversal has concrete harmonic-analytic content beyond a character-table exercise.

## Closest sources and limitations

Arezoomand–Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs* (2013), DOI 10.37236/3105, especially the published Corollary 9. Liu–Zhou, *Eigenvalues of Cayley Graphs* (2022), DOI 10.37236/8569, especially its discussion of Ghorbani's dicyclic results. M. Ghorbani, *On the eigenvalues of normal edge-transitive Cayley graphs*, Bull. Iranian Math. Soc. 41(1) (2015), 101–107 (full text unavailable). Restricted to odd prime dicyclic groups, unweighted four taps with two in each coset; no independence or historical-priority certification.

Self-review: passed. Independent audit: not yet performed.
