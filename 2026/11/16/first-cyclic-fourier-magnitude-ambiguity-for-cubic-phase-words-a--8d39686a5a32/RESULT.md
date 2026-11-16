# First cyclic Fourier-magnitude ambiguity for cubic-phase words: a unique triple fiber

## Finding
Let \(\omega=e^{2\pi i/3}\). For \(1\le n\le6\), consider every full-support word \(f:\mathbb Z_n\to\{1,\omega,\omega^2\}\), and its *unscaled cyclic discrete Fourier intensities*
\[
I_f(k)=\left|\sum_{j=0}^{n-1}f(j)e^{-2\pi i kj/n}\right|^2,\qquad k\in\mathbb Z_n.
\]
Identify words only under the universal intensity-preserving operations of global multiplication by a cube root, cyclic translation, and conjugate reversal \(f(j)\mapsto\overline{f(-j)}\). Then every intensity fiber is a single equivalence class for \(1\le n\le5\). At \(n=6\), exactly one intensity fiber contains more than one equivalence class: it contains precisely three classes, each consisting of six words after fixing \(f(0)=1\). Its intensity vector is exactly
\[
(I_f(0),\ldots,I_f(5))=(9,3,9,3,9,3).
\]
Three exponent-word representatives, writing \(f(j)=\omega^{a_j}\), are
\[
(0,0,1,0,0,2),\quad(0,0,1,0,1,1),\quad(0,0,1,1,0,1).
\]
The first uses all three phases, with sorted phase occupancies \((1,1,4)\); the other two use only two phases, with sorted occupancies \((0,3,3)\). Thus even phase-alphabet occupancy cannot always be inferred from complete cyclic Fourier intensity.

The exact census is:

| \(n\) | Global-phase-normalized words | Distinct intensity vectors | Equivalence classes | Intensity fibers containing several classes |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 |
| 2 | 3 | 2 | 2 | 0 |
| 3 | 9 | 4 | 4 | 0 |
| 4 | 27 | 7 | 7 | 0 |
| 5 | 81 | 13 | 13 | 0 |
| 6 | 243 | 30 | 32 | 1 |

## Assumptions and scope
The index group is the cyclic group \(\mathbb Z_n\); the Fourier transform is sampled at all \(n\) characters and is *not* the aperiodically oversampled Fourier transform. Every input entry has unit modulus and belongs exactly to the cubic-root alphabet. Multiplication of a word by an overall cube root is removed uniquely by requiring \(f(0)=1\). The equivalence relation is generated only by phase, cyclic shift, and conjugate reversal; a plain reflection without conjugation is not universally intensity-preserving for complex words. The theorem quantifies over all lengths \(1\le n\le6\), not larger lengths, and all words for each length, with no assumed phase composition.

## Proof
Write each normalized word uniquely as \(f(j)=\omega^{a_j}\) with \(a_0=0\) and \(a_j\in\{0,1,2\}\). Its cyclic autocorrelation is
\[
C_f(\ell)=\sum_{j=0}^{n-1}f(j)\overline{f(j+\ell)}
=\sum_{r=0}^2c_{\ell,r}\omega^r,
\]
where the nonnegative integers \(c_{\ell,r}\) count indices satisfying \(a_j-a_{j+\ell}\equiv r\pmod3\). Since \(1+\omega+\omega^2=0\) and the minimal polynomial of \(\omega\) over \(\mathbb Q\) has degree two, equality of two autocorrelation coefficients is **exactly equivalent** to equality of the ordered integer pairs
\[
(c_{\ell,0}-c_{\ell,2},\ c_{\ell,1}-c_{\ell,2}).
\]
The discrete Wiener–Khinchin identity \(I_f(k)=\sum_{\ell=0}^{n-1}C_f(\ell)e^{2\pi i k\ell/n}\) makes equality of all intensities equivalent to equality of these pairs for every lag. This reduction involves no floating-point approximation.

The normalized phase, shift, and conjugate-reversal orbit of \(a\) is obtained by taking every shift \(s\in\mathbb Z_n\), both exponent maps \(j\mapsto a_{s+j}\) and \(j\mapsto-a_{s-j}\), and subtracting the exponent at index zero modulo three. Every universal symmetry has exactly this form. The lexicographically least resulting word is therefore a complete and unique equivalence-class key.

These facts reduce the theorem to **finite, fully exhaustive integer arithmetic**: at each \(n\) the nested loops visit exactly the \(3^{n-1}\) normalized words once, calculate every lag count, form the autocorrelation key, and partition each intensity fiber by its orbit key. The complete deterministic implementation in `check.py` gives the displayed six census rows and shows that the sole multi-orbit key at \(n=6\) is
\[
(C_f(0),C_f(1),\ldots,C_f(5))=(6,0,0,3,0,0).
\]
It has precisely the three displayed canonical representatives, whose normalized orbit cardinalities are each six. The Wiener–Khinchin identity gives \(I_f(k)=6+3(-1)^k\), yielding the displayed two-level intensity vector. Finally, sorted phase occupancies are preserved by each universal symmetry, so the first representative is demonstrably inequivalent to either of the other two; the exact orbit-key computation distinguishes the remaining pair. This completes the finite proof, including the no-earlier-ambiguity cutoff.

## Verification
Run `python check.py` and `python crosscheck.py` with Python 3 and no additional packages. The first directly counts differences in \(\mathbb Z/3\mathbb Z\) and uses a closed-form canonical orbit key. The second separately implements addition and multiplication in \(\mathbb Z[\omega]\), forms the full periodic correlation in that ring, and constructs orbits through a generator-based breadth-first walk. Both exhaust all \(364\) normalized words across lengths one through six and independently reproduce the table, exceptional fiber, and representative multiplicities. In the standalone scripts, `assert` statements are the finite certificate checks. The theoretical guarantee is exact finite enumeration, not sampling or an extrapolation to arbitrary lengths.

## Relationship to prior work
Bendory–Edidin–Gonzalez, *Finite alphabet phase retrieval* (first public January 25, 2023), develops the periodic-correlation/difference-set viewpoint for generic alphabet entries and tabulates examples of homometric partitions. Its general statement is not a classification of the fixed non-generic alphabet of cubic roots, whose relation \(1+\omega+\omega^2=0\) lets words of different phase compositions have exactly the same intensities. In particular, its balanced three-partition table at length six does not give the triple intensity fiber identified here. Edidin's *Geometry of ambiguity in one-dimensional phase retrieval* analyzes the continuously sampled, aperiodic Fourier intensity and its polynomial-factorization ambiguity, not this complete cyclic, cubic-phase census. Prior bit-retrieval work addresses real binary sequences. The present claim is restricted to the first onset and exact fiber structure of this special cubic-phase problem; standard autocorrelation identities and its symmetry group are not claimed as new.

## Limitations
No statement is made about any length above six, about other phase alphabets, stability to intensity noise, or uniqueness from partial frequencies. The exhaustive proof establishes only a small but natural first-failure threshold. The historical literature on small polyphase waveform tables may contain an equivalent unindexed census; priority is not independently certified. The scripts and their exact outputs support finite mathematical correctness, not independent publication review.

## References
- Tamir Bendory, Dan Edidin, Ivan Gonzalez, *Finite alphabet phase retrieval*, arXiv:2301.10647v1, first public 2023-01-25. https://arxiv.org/abs/2301.10647
- Dan Edidin, *The geometry of ambiguity in one-dimensional phase retrieval*, arXiv:1811.06963v1, first public 2018-11-16. https://arxiv.org/abs/1811.06963
- Veit Elser, *The complexity of bit retrieval*, arXiv:1601.03428v1, 2016-01-13. https://arxiv.org/abs/1601.03428
