# Exact Walsh rank and optimal endpoint projection for four-variable antichains

## Finding

Let \(P=2^{\{1,2,3,4\}}\) be the sixteen-element Boolean lattice, and let \(G=\mathbb F_2^{P}\) be its Boolean incidence-vector group, of order \(2^{16}=65536\). Define \(\mathcal A\subseteq G\) to consist of the characteristic vectors of *all* antichains of \(P\), including the empty antichain. There are precisely \(168\) such vectors. For every \(u\in G\), put
\[
 W(u)=\sum_{a\in\mathcal A}(-1)^{\langle u,a\rangle}.
\]
Counting convolution \(C f=1_{\mathcal A}*f\), with the unnormalized group convolution, has exactly \(6611\) zero Walsh multipliers and therefore
\[
 \operatorname{rank} C=58925,\qquad \ker C\text{ has dimension }6611.
\]
Its complete signed multiplier histogram is `signed_walsh.csv`: it has \(79\) signed levels, least nonzero magnitude \(2\), maximum magnitude \(168\), and gcd of all multipliers \(2\). The \(6611\) zero frequencies form exactly \(199\) orbits under permutation of the four underlying elements and order reversal of \(P\), among \(2104\) total frequency orbits. Their orbit-size distribution is in `orbit_census.csv`.

Let \(E=\operatorname{ran} C\), as a subspace of real or complex functions on \(G\), equipped with either counting \(\ell^1\) or supremum \(\ell^\infty\). Among *all* bounded linear projections onto \(E\), not only translation-invariant ones, the exact least possible norms are
\[
 \Lambda_1(E)=\Lambda_\infty(E)=\frac{1526023}{32768}.
\]
The corresponding Fourier-support kernel has complete signed histogram `projection_kernel.csv` and unnormalized absolute sum \(3052046\). No claim is made about any different Boolean lattice size.

## Assumptions and scope

Identify each subset of \(\{1,2,3,4\}\) with the integer \(0,\ldots,15\) given by its four-bit membership mask. Identify each \(a\in G\) with the sixteen-bit mask whose bit \(s\) is one exactly when \(s\) belongs to the represented family. Such a family is an antichain if for every distinct included pair \(s,t\), neither \(s\subseteq t\) nor \(t\subseteq s\). The pairing is the usual bitwise dot product modulo two. Both Fourier transforms in the proof are *unnormalized*. The convolution itself is unnormalized; its Fourier eigenvalues are \(W(u)\). The Fourier projection is normalized by \(|G|^{-1}\).

## Proof

**Exact antichain set.** There are exactly \(3^4-2^4=65\) unordered comparable pairs in \(P\): a comparable pair is specified by choosing for each ground element whether it belongs to neither member, only the larger member, or both, and deleting the \(2^4\) equal pairs. For each integer \(a\) with \(0\le a<65536\), inspect all \(65\) pairs and set \(f(a)=1\) precisely when no pair has both coordinates selected. This deterministic finite test gives \(\sum_a f(a)=168\), in agreement with the known fourth Dedekind number. The complete definition in the two independent checkers is the finite proof of this assertion, rather than a sample of possibilities.

**Complete spectrum.** Define \(\mathcal H_{16}\) as the unnormalized Sylvester character matrix with entries \((-1)^{\langle u,a\rangle}\). The Walsh coefficients are \(W=\mathcal H_{16} f\). The exact-integer butterfly recurrence \((p,q)\mapsto(p+q,p-q)\), applied once along each of sixteen coordinates to the complete \(65536\)-entry vector, is an exhaustive calculation of every \(W(u)\). The checker `verify_antichain.py` recomputes all entries and compares the entire signed histogram to `signed_walsh.csv`. It finds exactly \(6611\) zeros, so Fourier diagonalization gives the displayed rank. Independently, `verify_direct.cpp` constructs the same family by the pairwise comparability criterion, evaluates all \(168\) character summands directly for each of the \(65536\) frequencies, and compares the same histogram without using a Walsh butterfly. Integer Parseval reads \(\sum_u W(u)^2=65536\cdot168\). The least nonzero multiplier and gcd follow directly from the complete histogram.

**Symmetry refinement.** Any permutation of four ground elements, together with optional complementation of each underlying four-bit subset, acts on the sixteen coordinates of \(G\) and preserves the antichain family. This is an action of \(S_4\times C_2\) with \(48\) transformations. The orbit enumerator in `verify_orbits.py` explicitly generates all \(48\) transformations, assigns every \(u\in G\) to its orbit, and checks that \(W\) is constant on each orbit. It produces \(2104\) orbits, of which \(199\) are zero orbits; summing their orbit sizes gives \(6611\). The full orbit census is embedded in `orbit_census.csv`.

**Sharp projection norm.** Put \(S=\{u\in G:W(u)\ne0\}\), so \(|S|=58925\), and let \(H(x)=\sum_{u\in S}(-1)^{\langle x,u\rangle}\). The Fourier-support projection \(Q\) acts by convolution with \(H/65536\). Consequently \(\|Q\|_{\ell^1\to\ell^1}=\|Q\|_{\ell^\infty\to\ell^\infty}=65536^{-1}\sum_x|H(x)|\). Applying the exact Walsh recurrence to \(1_S\) yields \(\sum_x|H(x)|=3052046\), as certified by `projection_kernel.csv` and `verify_antichain.py`. Independently, for each nonzero \(x\), \(H(x)=-\sum_{u\notin S}(-1)^{\langle x,u\rangle}\), while \(H(0)=|S|\). Thus `verify_direct.cpp` recomputes the same complete signed kernel histogram by direct sums over precisely \(6611\) zero frequencies, without a second Walsh transform. This gives the displayed rational constant.

To see optimality among *all* projections, let \(P_0\) be any linear projection onto \(E\). For the translation operators \(\tau_g\), average \(\widetilde P=65536^{-1}\sum_{g\in G}\tau_g^{-1}P_0\tau_g\). Since translations preserve \(E\), \(\widetilde P\) remains a projection onto \(E\), and its \(\ell^1\) and \(\ell^\infty\) operator norms do not exceed the corresponding norm of \(P_0\). It commutes with all translations; in Fourier coordinates it is therefore diagonal, equals one on \(S\), and equals zero off \(S\) because its image is \(E\). Thus \(\widetilde P=Q\), proving the minimum for real and complex scalars.

## Verification

All computation involves exact integer addition, subtraction, bit tests, character parity and integer histograms; no floating-point thresholds occur. From the directory containing the embedded files, execute `python3 verify_antichain.py`, `python3 verify_orbits.py`, and `g++ -O3 -std=c++17 verify_direct.cpp -o /tmp/verify_direct_b4 && /tmp/verify_direct_b4 .`. Each program recomputes its asserted invariants and fails if an exact comparison is violated. Both independent spectral paths were actually executed from their generated source files; the orbit checker was also executed. The signed spectral histogram includes all frequencies, not sampled frequencies. The support-kernel check is exhaustive, not an extrapolation. The exact identities \(\sum_u W(u)^2=65536\cdot168\) and \(\sum_xH(x)^2=65536\cdot58925\) give redundant Parseval checks.

## Relationship to prior work

The size \(|\mathcal A|=168\) is the classical fourth Dedekind number and is not a new enumerative result. Stephen and Yusun (arXiv:1209.4623v1) give the Dedekind-number table and count monotone Boolean functions up to variable-renaming equivalence; De Causmaecker, De Wannemacker and Yellen (arXiv:1602.04675v1) develop interval decompositions and counting formulas for the lattice of antichains. Bshouty and Tamon (ECCC TR95-032) analyze the Fourier degree spectrum of each monotone Boolean function on its *input cube*. That differs from the present Fourier transform of the indicator of the *ensemble* of all 168 antichains, regarded as points of a sixteen-coordinate Boolean group. The general Fourier multiplier and translation-averaging principles are classical and are not claimed as novel. The new evaluated quantities are the exact frequency nullity, signed spectrum and orbit structure, and resulting sharp endpoint projection norm for this natural complete antichain ensemble.

## Limitations

The calculation is specific to the sixteen-element Boolean lattice; it gives no general closed formula for arbitrary \(n\), no asymptotics and no assertion of independent mathematical validation. The novelty comparison is a bounded literature and mathematical-record search, not a claim that every historic source was accessible. These spectra must not be confused with the Fourier transforms of individual monotone Boolean functions in four variables.

## References

1. N. H. Bshouty and C. Tamon, *On the Fourier Spectrum of Monotone Functions*, Electronic Colloquium on Computational Complexity TR95-032, publicly posted 29 June 1995. https://eccc.weizmann.ac.il/report/1995/032/
2. T. Stephen and T. Yusun, *Counting Inequivalent Monotone Boolean Functions*, arXiv:1209.4623v1, 20 September 2012. https://arxiv.org/pdf/1209.4623
3. P. De Causmaecker, S. De Wannemacker and J. Yellen, *Intervals of Antichains and Their Decompositions*, arXiv:1602.04675v1, 15 February 2016. https://arxiv.org/pdf/1602.04675
4. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, Graduate Surveys 1, 25 September 2008, doi:10.4086/toc.gs.2008.001.
