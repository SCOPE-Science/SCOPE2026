# Sharp Fourier-bandwidth-two determination and complete integer-resonance aliases of axis-parallel boxes

## Finding

Let \(d\ge1\) and let \(B=\prod_{j=1}^{d}(c_j-L_j/2,c_j+L_j/2)\subset\mathbb R^d\), with \(L_j>0\) and \(c_j\in\mathbb R\). With the convention
\[
F_B(n)=\int_B e^{-2\pi i n\cdot x}\,dx,\qquad n\in\mathbb Z^d,
\]
the \(2d+1\) complex Fourier measurements
\[
\boxed{F_B(0),\quad F_B(e_j),\quad F_B(2e_j)\quad(1\le j\le d)}
\]
**determine every** \(F_B(n)\) for \(n\in\mathbb Z^d\), without any upper bound on the side lengths. Here \(e_j\) denotes the \(j\)-th coordinate unit vector. For \(d\ge2\), the Fourier cube \(\{n:|n_j|\le1\text{ for all }j\}\) is **not** sufficient, even if all side lengths are nonintegers; hence coordinate bandwidth two is sharp. In contrast, if every side satisfies \(0<L_j<1\), the measurements \(F_B(0)\) and \(F_B(e_j)\) alone determine the box modulo translations by \(\mathbb Z^d\).

There is also an exact classification of all boxes giving the same *complete* sampled Fourier spectrum. Two boxes \(B\) and \(B'\) agree at every integer frequency if and only if:

1. They have equal volume \(\prod_jL_j=\prod_jL'_j\).
2. They have exactly the same coordinate set \(J=\{j:L_j\in\mathbb N\}=\{j:L'_j\in\mathbb N\}\) of positive-integer side lengths.
3. For every \(j\notin J\), one has \(L'_j=L_j\) and \(c'_j-c_j\in\mathbb Z\).

On \(j\in J\), the centers are unrestricted, while the positive integer lengths can vary subject only to preservation of their product. Thus if \(J=\varnothing\), integer-frequency samples identify the box up to integer translation; if \(J\ne\varnothing\), even infinitely many such samples cannot determine its centers on integer-length axes. For \(|J|\ge2\), different ordered positive-integer factorizations of the same product may produce additional width ambiguities. **The finite measurement set above gives exactly this same classification**, not merely a sufficient condition.

## Assumptions and scope

A box is a nonempty open Cartesian product of bounded intervals, considered modulo Lebesgue-null boundary changes. Coordinates are fixed and labelled; no permutation of axes is implicitly identified. Every side length is an arbitrary *positive real number*, and the Fourier samples are the complex-valued coefficients, including their phases, not their magnitudes alone. Integer frequencies correspond to the standard lattice \(\mathbb Z^d\). No claim is made for rotated boxes, general polytopes, unions of boxes, or arbitrary indicator functions.

Write the volume as \(V=F_B(0)>0\) and, for each coordinate, introduce normalized measurements
\[
b_{j,k}=\frac{F_B(k e_j)}{V},\qquad k=1,2.
\]
Their exact reconstruction formula is as follows. If \(b_{j,1}=0\), then \(L_j\) is a positive integer, and the entire normalized coordinate spectrum equals \(1\) at frequency zero and \(0\) at every nonzero integer frequency. If \(b_{j,1}\ne0\), set
\[
 r_j=\frac{|b_{j,2}|}{|b_{j,1}|},\qquad
 \boxed{L_j=\frac{\sqrt{1-r_j^2}}{\pi|b_{j,1}|}},\qquad
 z_j=\frac{b_{j,1}}{\sin(\pi L_j)/(\pi L_j)}.
\]
Then \(0\le r_j<1\), \(|z_j|=1\), and \(z_j=e^{-2\pi i c_j}\), so the center is recovered modulo \(\mathbb Z\). For any \(n\in\mathbb Z^d\), compute
\[
F_B(n)=V\prod_{j=1}^d a_j(n_j),\quad
 a_j(k)=\begin{cases}
 1,&k=0,\\
 0,&k\ne0\text{ and }b_{j,1}=0,\\
 \dfrac{\sin(\pi kL_j)}{\pi kL_j}z_j^k,&k\ne0\text{ and }b_{j,1}\ne0.
 \end{cases}
\]
All expressions involving \(L_j\) on the right-hand side use the *recovered* noninteger length, and no unknown integer length appears in this formula.

## Proof

**Step 1: Exact Fourier factorization.** For an interval of length \(L>0\) centered at \(c\), direct integration gives
\[
\int_{c-L/2}^{c+L/2}e^{-2\pi i kt}\,dt
=\begin{cases}L,&k=0,\\
 e^{-2\pi ikc}\dfrac{\sin(\pi kL)}{\pi k},&k\ne0.
\end{cases}
\]
Fubini's theorem therefore gives
\[
F_B(n)=V\prod_{j=1}^d e^{-2\pi i n_jc_j}
\frac{\sin(\pi n_jL_j)}{\pi n_jL_j},
\]
using the continuous extension \(\sin u/u=1\) at \(u=0\). In particular, \(b_{j,k}=e^{-2\pi ikc_j}\sin(\pi kL_j)/(\pi kL_j)\).

**Step 2: Invert one coordinate at frequencies one and two.** From the first coefficient, \(b_{j,1}=0\) holds exactly when \(\sin(\pi L_j)=0\), equivalently \(L_j\in\mathbb N\). All other nonzero integer-frequency coefficients then vanish, regardless of center. Otherwise, the double-angle identity gives
\[
\frac{|b_{j,2}|}{|b_{j,1}|}=|\cos(\pi L_j)|<1,
\qquad \pi L_j|b_{j,1}|=|\sin(\pi L_j)|.
\]
Squaring and adding proves \((\pi L_j|b_{j,1}|)^2+r_j^2=1\), and hence the stated *unique* positive length formula. Dividing the first complex coefficient by its now known nonzero real sinc factor recovers \(e^{-2\pi i c_j}\) without sign ambiguity. Inserting these recovered factors into Step 1 reproduces every integer-frequency sample; this also proves finite sufficiency when some side lengths are integers.

**Step 3: Exact alias fibers.** Equality of complete spectra implies equality of the samples in the displayed \(2d+1\)-element set, so Step 2 shows equality of the integer-side coordinate sets, equality of each noninteger side length and center residue, and equality of volume. Conversely, suppose precisely these three conditions hold. On integer-length axes the normalized coefficient is the Kronecker delta at frequency zero. On every other axis the normalized factor of Step 1 agrees by length and center residue. The product formula therefore yields \(F_B(n)=F_{B'}(n)\) for every integer vector \(n\). This proves necessity and sufficiency, including the exact integer-factorization freedom.

**Step 4: The first-bandwidth regime.** If \(0<L<1\), then \(s(L)=\sin(\pi L)/(\pi L)\) is positive and strictly decreasing from \(1\) toward \(0\). Indeed, for \(u\in(0,\pi)\), the function \(\sin u-u\cos u\) has derivative \(u\sin u>0\) and initial value zero, so \(s'(L)<0\). Thus the modulus \(|b_{j,1}|=s(L_j)\) uniquely determines each width in this regime, and its phase determines each center modulo one. For \(d=1\) the zeroth sample already determines \(L_1\) without a small-width restriction, so \(F_B(0),F_B(e_1)\) suffice in every dimension-one case.

**Step 5: Sharpness of coordinate bandwidth two when \(d\ge2\).** Define \(q(t)=|\sin(\pi t)|/(\pi t)\) for \(t>0\). Since \(q\) decreases continuously from \(1\) to \(0\) on \((0,1)\), there is a unique \(\lambda\in(0,1)\) satisfying
\[
 q(\lambda)=q(3/2)=\frac{2}{3\pi}.
\]
Take two planar boxes whose respective width vectors and center vectors are
\[
 (\lambda,3/2),\ (0,1/2),\qquad
 (3/2,\lambda),\ (1/2,0).
\]
Both have volume \(3\lambda/2\). Their normalized first coordinate coefficients are, in *both* axes, \(2/(3\pi)\): for the length \(3/2\), the negative sinc is offset by the center phase \(-1\). Hence every sample with both coordinates in \(\{-1,0,1\}\) agrees, by the product formula, including all mixed frequencies. But these boxes have unequal first-coordinate lengths and are not translates. Since the defining root satisfies \(1/2<\lambda<1\), its second sinc harmonic is nonzero, while the second harmonic of the length \(3/2\) is zero. Thus their frequency-\(2e_1\) coefficients explicitly differ. Appending identical extra intervals proves the same failure for all \(d>2\). Thus even the entire first-frequency cube does not give the exact alias classification, while coordinate bandwidth two does.

## Verification

The proof above is analytic and applies to every integer dimension and every positive real side length. The separate standard-library test script `verification/check.py` additionally checks the recovered Fourier coefficients against direct interval integration on randomly generated boxes in dimensions one through four, including integer-side resonance cases; it also checks the sharp first-frequency-cube counterexample. Run from the extracted package root:

```bash
python3 verification/check.py
```

It returned `PASS: 43460 supplementary checks; first-cube witness width=0.816725605173696; second-frequency gap=0.218056939355`. These are finite floating-point checks, *not* a proof of the universal theorem. The proof requires only Fubini's theorem, elementary trigonometric identities, and monotonicity on \((0,1)\).

## Relationship to prior work

Asipchuk and Robins (2026) prove that full Fourier agreement on a lattice is equivalent to measurable lattice-translation equidecomposability of bounded sets, and obtain rigidity under an anti-aliasing hypothesis. The present claim is more specific in geometry but addresses an additional inverse question: exactly which *finite* Fourier samples recover the entire sampled spectrum of arbitrary-size axis-parallel boxes, even when anti-aliasing fails, together with the explicit integer-resonance fibers and a sharp frequency cutoff. Their general equivalence theorem does not itself supply the finite cutoff or the stated width reconstruction formula.

Mao (2011) studies recovery of binary periodic signals from low Fourier coefficients, including signals with few jumps. Ongie and Jacob (2016) analyze finite Fourier recovery of piecewise-constant two-dimensional images via annihilating curves, assuming support in a unit cell. Both are important related finite-rate-of-innovation settings, but their statements inspected here do not give the arbitrary-multiwrap box alias classification and the global sharp cutoff in the present theorem. The classical sinc transform of an interval is an essential starting identity, not claimed to be new.

## Limitations

Only exact, noiseless complex samples are considered. Reconstruction of widths becomes poorly conditioned as a noninteger side approaches an integer, or becomes very long; no global noise-stability bound is claimed. An integer-width coordinate has an intrinsically invisible center regardless of how many integer Fourier frequencies are sampled. The theorem neither resolves general shape recovery nor implies an optimal sample *cardinality* among all conceivable nonuniform frequency sets; the sharpness assertion concerns maximum coordinate frequency. The available comparison is not an exhaustive historical priority proof, and an earlier equivalent finite-rate-of-innovation calculation remains possible. Independent external validation has not been performed.

## References

1. O. Asipchuk and S. Robins, *Fourier sampling on a lattice*, arXiv:2608.29217, first posted August 29, 2026. https://arxiv.org/abs/2608.29217
2. Y. Mao, *Reconstruction of Binary Functions and Shapes from Incomplete Frequency Information*, arXiv:1104.0446 (2011). https://arxiv.org/abs/1104.0446
3. G. Ongie and M. Jacob, *Off-the-Grid Recovery of Piecewise Constant Images from Few Fourier Samples*, arXiv:1510.00384 (2015; updated 2016). https://arxiv.org/abs/1510.00384
