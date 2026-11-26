# Exact cyclic integrated sidelobe energy of binary order-five de Bruijn cycles

## Finding
Let \(\mathcal B_5\) be the set of binary de Bruijn cycles of order five, identified under rotation only. Every \(B\in\mathcal B_5\) has 32 symbols and contains each five-bit word exactly once as a circular factor. Assign \(x_j=2B_j-1\in\{-1,+1\}\), with indices modulo 32, and define the unnormalized periodic autocorrelation and integrated off-peak energy by
\[
R_B(t)=\sum_{j=0}^{31}x_jx_{j+t\bmod32},\qquad
E(B)=\sum_{t=1}^{31}R_B(t)^2.
\]
There are exactly 2048 rotation classes. Their energy takes exactly 47 distinct values, listed with multiplicities and peak-sidelobe refinements in `spectrum.csv`. The sharp extrema and their multiplicities are
\[
\min_{B\in\mathcal B_5}E(B)=192\quad(12\text{ cycles}),\qquad
\max_{B\in\mathcal B_5}E(B)=1952\quad(4\text{ cycles}).
\]
The twelve minimizers form exactly three four-element orbits, and the four maximizers one four-element orbit, under rotation, reversal and bit complementation. Each of the 47 attained energies is divisible by 32. For a uniformly selected rotation class,
\[
\mathbb E[E]=\frac{2813}{4},\qquad
\operatorname{Var}(E)=\frac{1336631}{16}.
\]
The full population of peak absolute sidelobes \(\max_{1\le t<32}|R_B(t)|\) is \(4:12,8:772,12:882,16:282,20:88,24:12\). Within the 772 cycles of peak sidelobe 8, the energy alone ranges from 224 to 992. Thus selecting on peak sidelobe magnitude does not determine energy, even inside one peak class.

## Assumptions and scope
Words use the labeled binary alphabet \(\{0,1\}\). Rotation identifies two cycles, but reversal and complementation do not identify them when counting the 2048 classes. Every positive and negative lag is included in the energy, with no factor of one-half or normalization by sequence length. The autocorrelation at lag zero is \(R_B(0)=32\) and is excluded. The peak absolute sidelobe is computed only over the other 31 lags. Symmetry orbits are taken after quotienting by cyclic rotation. The finite assertion concerns precisely order five, not all de Bruijn orders or arbitrary binary signals.

## Proof
Consider the directed binary de Bruijn graph with 16 vertices labeled by four-bit words and 32 edges labeled by five-bit words. An edge \(a_0a_1a_2a_3a_4\) runs from \(a_0a_1a_2a_3\) to \(a_1a_2a_3a_4\). Every vertex has exactly two incoming and two outgoing edges.

An Eulerian circuit induces at each vertex a bijection pairing its two incoming edges to its two outgoing edges, according to which edge follows which. Conversely, a choice of the local bijections gives a permutation of the 32 edges. Its permutation cycles are the directed circuits determined by those pairings. The choice is a single Eulerian circuit precisely when this permutation has one cycle of length 32. There are exactly \(2^{16}=65536\) such local choices to examine. Since edge `00000` appears exactly once, using it as the first edge chooses a unique root of every Eulerian circuit. Reading the first symbol on each successive edge recovers the corresponding de Bruijn cycle, and no two accepted local choices yield the same rooted cycle. Thus this procedure exhausts the 2048 rotation classes without duplications.

The independent depth-first Eulerian enumeration in `verify.py` searches all unused outgoing edges after fixing `00000`, and retains only full 32-edge tours returning to the initial vertex. Its output set coincides with the output of the complete local-pairing enumeration and has 2048 members.

For each such cycle, one computation directly evaluates \(R_B(t)\) by 32 products for every lag. A second computation uses the set \(S_B\) of 16 positions carrying a one. Writing \(k_t=|\{j\in S_B:(j+t)\bmod32\in S_B\}|\), balance gives exactly \(k_t\) zero-zero pairs and \(32-2k_t\) unequal pairs. Consequently
\[
R_B(t)=4k_t-32.
\]
These independently implemented methods give identical 32-tuples on all 2048 cycles. Squaring and summing the 31 nonzero-lag entries produces every frequency in `spectrum.csv`. The exact histogram has 47 occupied bins and total mass 2048, with minimum 192 of frequency 12 and maximum 1952 of frequency 4. Integer histogram sums give the displayed mean and variance. The script additionally verifies all row-level frequencies cross-classified by peak sidelobe and explicitly forms the reversal-complement orbits of all extremizers. Their respective orbit-size multisets are \(\{4,4,4\}\) and \(\{4\}\).

The normalized discrete Fourier transform convention \(\widehat x(k)=\sum_{j=0}^{31}x_j\exp(-2\pi\mathrm i jk/32)\) gives the standard exact identity
\[
E(B)=\frac1{32}\sum_{k=0}^{31}|\widehat x(k)|^4-1024,
\]
by the periodic correlation theorem and Parseval. This explains why the same invariant can be described as a fourth-moment or power-spectrum-flatness statistic. It is an algebraic equivalence, not an independent computation of the census.

## Verification
Place `verify.py` and `spectrum.csv` in the same directory and execute `python3 verify.py`. Only the Python standard library is needed. The verifier enumerates all 65536 local pairing assignments and separately every Euler circuit beginning at `00000`; requires equality of the full resulting 2048-member sets; evaluates all 32 lags of all cycles by direct products and by support intersections; checks the 47-row cross-tabulation against the CSV; checks exact moments and extrema; and verifies all extremal symmetry orbits. All calculations supporting the finite classification use exact integer or rational arithmetic. As an external numerical check, the mean normalized per-cycle RMS sidelobe \(\sqrt{E(B)/(31\cdot32^2)}\), over all cycles and over the peak-at-most-eight and peak-at-most-four subclasses respectively, is approximately \(0.145958\), \(0.123429\) and \(0.077771\); these round to the values \(0.146\), \(0.123\) and \(0.078\) independently reported in Spinsante et al., Table 3.

## Relationship to prior work
Spinsante, Andrenacci and Gambi (2011) study all 2048 order-five binary de Bruijn sequences as spreading codes and give peak-sidelobe threshold subsets (12 with peak at most 4 and 784 with peak at most 8), together with aggregate normalized mean and RMS sidelobe statistics. Those known counts agree with the peak marginals above but do not provide the 47-bin exact periodic energy distribution or its optimizing symmetry classes. Fujisaki and Nabeshima (2011) study worst and second-worst individual normalized periodic autocorrelation values, including order five, rather than the integrated squared energy distribution. Song, Babu and Palomar (2014) explain the integrated sidelobe objective and its use for periodic or aperiodic sequence design, optimizing over much broader complex unimodular sequence families; their unconstrained optimization is not a census of binary de Bruijn cycles. The present energy equals a cyclic Fourier fourth-moment statistic via the displayed identity, so literature under those names is relevant even when it does not mention the word 'energy'.

## Limitations
The theorem is an exhaustive finite result for order five. It does not assert a formula for all orders, optimality among all 32-bit binary words, low aperiodic sidelobes for any chosen cut, good mutual cross-correlation among selected distinct cycles, or a measured communication-system performance improvement. Earlier unindexed numerical energy tables or unreleased raw measurements are possible and leave some historical-priority risk.

## References
- S. Spinsante, S. Andrenacci, and E. Gambi, *Binary De Bruijn sequences for DS-CDMA systems: analysis and results*, EURASIP Journal on Wireless Communications and Networking, 2011:4, published 6 June 2011. https://doi.org/10.1186/1687-1499-2011-4
- H. Fujisaki and Y. Nabeshima, *On auto-correlation values of de Bruijn sequences*, Nonlinear Theory and Its Applications, IEICE 2(4), 400–408, 2011. https://doi.org/10.1587/nolta.2.400
- J. Song, P. Babu, and D. P. Palomar, *Optimization Methods for Designing Sequences with Low Autocorrelation Sidelobes*, arXiv:1501.02252, version dated 26 December 2014. https://arxiv.org/abs/1501.02252
