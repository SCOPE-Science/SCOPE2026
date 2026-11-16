# Exact Walsh cancellation beyond relabeling symmetry for six-vertex strong tournaments

## Finding

Let \(G=(\mathbb F_2)^{15}\), with coordinates indexed by lexicographically ordered pairs \(1\le i<j\le6\). The bit \(x_{ij}=1\) encodes the directed edge \(i\to j\), and \(x_{ij}=0\) encodes \(j\to i\). Let \(\mathcal S\subset G\) be the \(22,320\) orientations defining strongly connected tournaments. For all \(s\in G\), write
\[
W(s)=\sum_{x\in\mathcal S}(-1)^{\langle s,x\rangle}.
\]

The complete absolute Walsh spectrum has multiplicities

| \(\lvert W(s)\rvert\) | Number of frequencies |
|---:|---:|
| 0 | 24,352 |
| 16 | 6,120 |
| 32 | 420 |
| 48 | 15 |
| 96 | 300 |
| 112 | 165 |
| 128 | 720 |
| 144 | 540 |
| 272 | 45 |
| 1,360 | 30 |
| 1,552 | 60 |
| 22,320 | 1 |

Consequently, unnormalized counting convolution \(Tf=1_{\mathcal S}*f\) on \(G\) has rank \(8,416\), nullity \(24,352\), smallest nonzero multiplier magnitude \(16\), positive-spectrum condition number \(1,395\), and \(\|T^\dagger\|_{2\to2}=1/16\).

Under relabeling of the six vertices, the frequencies split into exactly \(156\) unoriented support-graph orbits. There are exactly \(124\) zero-multiplier orbits. For \(122\) of these, vanishing is forced either by reversing all tournament arcs (every odd-size support) or by a vertex relabeling preserving the support graph while reversing an odd number of its reference orientations. The **only two zero orbits not forced by either symmetry** have eight edges, each with \(360\) labeled supports. With one-based vertex numbering and the lexicographic edge-bit convention they are represented by the integer masks \(958\) and \(1883\), or equivalently

\[
\begin{aligned}
E_{958}&=\{13,14,15,16,23,25,26,34\},\\
E_{1883}&=\{12,13,15,16,24,26,34,35\}.
\end{aligned}
\]

Thus exactly \(720\) of the \(24,352\) zero frequencies have vanishing not explained by those two symmetries, and no such unexplained zero has fewer than eight edges. This statement concerns these precise symmetry mechanisms; it does not assert a classification of every conceivable algebraic identity.

The Fourier range projection \(P\) has sharp endpoint norm
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{5465}{128}.
\]
Moreover, this is the minimum endpoint operator norm among **all** real or complex projections onto the range of \(T\).

## Assumptions and scope

All sums are finite and unnormalized; counting measure is used on \(G\). Multiplication in characters takes place in \(\mathbb F_2\), while Fourier sums and operator norms are over \(\mathbb C\) or \(\mathbb R\). The result is only for tournaments on the labeled vertex set \(\{1,\ldots,6\}\), not an infinite-order extension. One mask bit corresponds to exactly one unordered pair of vertices, ordered lexicographically. For symmetry forcing, a relabeling is a permutation of the six vertices; global arc reversal acts by complementing all orientation bits. A zero is called symmetry-forced precisely if one of the two stated transformations maps its character to its negative while preserving \(\mathcal S\).

## Proof

**Exact signed decomposition.** For any nonempty subset \(V\) of the vertex set and any fixed frequency \(s\), put
\[
H_s(V)=\prod_{\{i,j\}\subseteq V,\ i<j}(1+(-1)^{s_{ij}}),\qquad H_s(\varnothing)=1,
\]
and let \(F_s(V)\) be the signed sum over strongly connected tournaments on \(V\). Every nonempty tournament has a unique source strongly connected component \(U\), and every arc from \(U\) to \(V\setminus U\) points outward. Let \(b_s(U,R)\) be the number modulo two of cross pairs \(i\in U,j\in R\) with \(i<j\) and \(s_{ij}=1\). Decomposing by the unique source component gives the exact integer recurrence
\[
F_s(V)=H_s(V)-\sum_{\varnothing\ne U\subsetneq V}(-1)^{b_s(U,V\setminus U)} F_s(U)H_s(V\setminus U).
\]
The base case is \(F_s(\{i\})=1\). In particular, \(W(s)=F_s(\{1,\ldots,6\})\). There are only \(2^{15}\) frequencies and \(2^6\) vertex subsets; the second program evaluates this recurrence **for every frequency** using exact integers.

**Independent complete enumeration.** The first program enumerates all \(2^{15}\) orientations, constructs outgoing adjacency bitsets and tests directed reachability from each of the six vertices. It thereby constructs exactly the \(22,320\) strong-tournament indicator values. The exact radix-two Walsh–Hadamard transform evaluates all \(2^{15}\) multipliers. The two constructions give identical ordered integer coefficient arrays (not merely matching histogram summaries). Their histogram is the displayed table; the equality \(\sum_s W(s)^2=2^{15}\cdot22320\) provides a separate Parseval check.

**Symmetry and exceptional orbits.** The first program enumerates every permutation of six vertices and its induced action on all \(15\)-bit support masks, yielding exactly \(156\) orbits. Invariance of \(\mathcal S\) under relabeling gives
\[
W(\pi s)=(-1)^{\varepsilon_\pi(s)}W(s),
\]
where \(\varepsilon_\pi(s)\) is the parity of supported reference orientations reversed by \(\pi\). A stabilizer of \(s\) with odd \(\varepsilon_\pi(s)\) forces \(W(s)=0\). Global arc reversal forces \(W(s)=0\) for odd \(\lvert s\rvert\). The finite complete orbit table `tournament_support_orbits.tsv` records each representative, orbit cardinality, coefficient magnitude and whether these symmetries force vanishing. Exactly two zero orbits have the final flag zero: masks \(958\) and \(1883\), of size \(360\) each. Exhaustiveness follows from the complete permutation and support-mask loops.

**Sharp projection constants.** Character diagonalization makes the rank and positive spectral gap immediate. The orthogonal range projection is convolution with
\[
p(z)=2^{-15}\sum_{s:W(s)\ne0}(-1)^{\langle s,z\rangle}.
\]
The second exact Walsh transform of the nonzero-multiplier indicator gives \(\sum_z\lvert2^{15}p(z)\rvert=1,399,040\), hence \(\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=1,399,040/32,768=5465/128\). Translation averaging of any projection onto the translation-invariant Fourier range cannot increase either endpoint norm; the unique translation-invariant projection onto that range is \(P\). Thus the value is optimal among all projections, not just Fourier multipliers.

## Verification

The reproducibility bundle contains `verify_tournament_enumeration.cpp`, `verify_tournament_scc.cpp`, `verify_all.py`, `walsh_coefficients.txt` and `tournament_support_orbits.tsv`. The driver compiles both programs using a C++17 compiler, checks both output sequences against the recorded complete coefficient certificate and each other, and checks the complete orbit certificate. The programs assert the family cardinality, full histogram, rank, Parseval identity, sharp smallest positive multiplier, orbit counts, exceptional supports and projection-kernel absolute sum. All integer operations are exact; no sampling, floating-point threshold or unverified extrapolation is used.

## Relationship to prior work

Wright (1970) and Moon–Moser's classical results concern enumeration and strong-component decomposition of tournaments. Kühn, Lapinskas, Osthus and Patel (2013) establish important structural consequences of strong connectivity, especially Hamiltonian cycles. Archer, Gessel, Graves and Liang (2019) compute descent-count generating functions and give a source-component recurrence; the recurrence above is its natural edge-wise signed specialization, not claimed as an original general enumeration principle. Their aggregate one-parameter descent data do not supply the coefficient values for arbitrary edge subsets or the two exceptional eight-edge Walsh orbits. Other finite Fourier results for regular tournaments and the weaker property of lacking a Condorcet winner concern different supports and do not imply the present strong-connectivity spectrum.

## Limitations

This is a self-contained finite classification of the six-vertex strong-tournament indicator. It does not predict all higher-order spectra or classify zero mechanisms outside the two explicitly defined symmetry actions. The numerical invariants have independent complete exact-arithmetic cross-checks, but priority depends on a bounded literature and mathematical-record search; an unindexed previous table could predate these computations. There has been no independent external mathematical audit.

## References

1. E. M. Wright, *The number of irreducible tournaments*, Glasgow Math. J. 11 (1970), 97–101, https://doi.org/10.1017/S0017089500000914.
2. D. Kühn, J. Lapinskas, D. Osthus, V. Patel, *Proof of a conjecture of Thomassen on Hamilton cycles in highly connected tournaments*, arXiv:1303.4213v1 (2013-03-18), https://arxiv.org/html/1303.4213v1.
3. K. Archer, I. M. Gessel, C. Graves, X. Liang, *Counting acyclic and strong digraphs by descents*, arXiv:1909.01550 (2019-09-04), https://arxiv.org/abs/1909.01550.
4. OEIS A054946, *Number of strongly connected labeled tournaments*, https://oeis.org/A054946.
