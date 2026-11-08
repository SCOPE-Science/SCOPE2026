# Generic conjugate recovery from a Boolean-star Walsh window

## Finding
Let \(n\ge2\) be even, let \(V=\mathbb F_2^n\), and put \(S=\{0,e_1,\ldots,e_n\}\). For every complex signal \(f:V\to\mathbb C\), measure the complete squared Walsh short-time Fourier magnitudes
\[
I_f(t,b)=\left|\sum_{s\in S}f(t+s)(-1)^{b\cdot s}\right|^2,\qquad t,b\in V.
\]
The measurements determine each \(|f(x)|^2\) and each real Gram entry \(\operatorname{Re}(f(x)\overline{f(y)})\) whenever the Hamming distance between \(x,y\) is at most two. The complex-linear span of the associated rank-one measurement projectors has exact rank
\[
2^n+2^{n-1}\binom{n+1}{2}.
\]
If \(n=2\), the measurements determine **every** signal up to multiplication by a constant unit-modulus scalar and/or simultaneous complex conjugation.

For even \(n\ge4\), the same conclusion holds for every signal in the explicit nonempty real-Zariski-open set
\[
\mathcal U_n=\Bigl\{f:\operatorname{Im}(f(0)\overline{f(e_1)})\ne0,\quad
\operatorname{Im}(f(u)\overline{f(v)})\ne0\ \text{for every pair }d_H(u,v)=2\Bigr\}.
\]
Thus the actual fixed, real-valued Walsh-Gabor measurement frame (rather than a randomly chosen frame) gives generic conjugate phase retrieval. The generic qualification is necessary when \(n\ge4\): some two-site signals have continuous, inequivalent phase ambiguities.

## Assumptions and scope
All character and group operations are in \(\mathbb F_2^n\). The measuring window is exactly the unnormalized indicator of the radius-one Hamming ball. Measurements are all \(2^{2n}\) intensities, not a subsample. There is no assumption that a competing signal belongs to \(\mathcal U_n\): whenever \(f\in\mathcal U_n\) and \(I_f=I_h\) for an arbitrary \(h:V\to\mathbb C\), necessarily \(h=e^{i\theta}f\) or \(h=e^{i\theta}\overline f\). The exceptional two-site construction is a statement of nonuniformity, not a classification of all exceptional signals. Only even \(n\) is asserted; no claim is made for odd \(n\).

The set \(\mathcal U_n\) is nonempty: assigning \(f(v)=1+i\operatorname{index}(v)\), where distinct binary vectors have distinct integer indices, satisfies the listed nonvanishing determinants. It is the complement of finitely many nonzero real polynomial zero sets, hence is open, dense and full measure in the ordinary real coordinates of \(\mathbb C^V\).

## Proof
**1. Exact local Walsh-correlation inversion.** Define
\[
C_f(t,a)=2^{-n}\sum_{b\in V}I_f(t,b)(-1)^{a\cdot b}.
\]
Character orthogonality gives, for all \(t,a\in V\),
\[
C_f(t,a)=\sum_{s\in S\cap(S+a)}f(t+s)\overline{f(t+s+a)}.
\]
The intersection geometry of the star \(S\) therefore yields
\[
\begin{aligned}
C_f(t,0)&=\sum_{s\in S}|f(t+s)|^2,\\
C_f(t,e_i)&=2\operatorname{Re}(f(t)\overline{f(t+e_i)}),\\
C_f(t,e_i+e_j)&=2\operatorname{Re}(f(t+e_i)\overline{f(t+e_j)})\quad(i\ne j),\\
C_f(t,a)&=0\quad\text{if }\operatorname{wt}(a)\ge3.
\end{aligned}
\]
In particular every individual real Gram entry on an edge of the square of the Boolean cube is recovered from exactly one such correlation: for an edge of difference \(e_i\), use shift \(t=x\); for difference \(e_i+e_j\), use shift \(t=x+e_i\).

**2. Individual magnitudes and the linear rank.** Put \(d(t)=|f(t)|^2\) and \(H(t)=C_f(t,0)\). Then \(H=(I+A)d\), where \(A\) is the ordinary cube adjacency operator. The Walsh character indexed by \(b\) is an eigenvector with eigenvalue \(n+1-2\operatorname{wt}(b)\). For even \(n\), this is an odd nonzero integer for every \(b\); hence \(d\) is recovered uniquely by Walsh division.

The same equations apply to an arbitrary real symmetric matrix \(X\) replacing the real Gram matrix: the measured linear functionals are exactly its diagonal convolved with \(I+A\) and its individual off-diagonal entries at Hamming distance one or two, each multiplied by two. There are \(2^n\) diagonal degrees of freedom and \(2^{n-1}(n+\binom n2)=2^{n-1}\binom{n+1}{2}\) such unordered off-diagonal pairs. They are independent. Since the measurement projectors are real symmetric, the real and complex dimensions of their spans equal this sum. This proves the asserted complex-linear rank without any unstated normalization.

**3. Constructive recovery on \(\mathcal U_n\).** Regard each complex coordinate of a signal as a vector in \(\mathbb R^2\), so \(\operatorname{Re}(f(x)\overline{f(y)})\) is its Euclidean inner product. Suppose \(I_f=I_h\). Step 2 provides equal lengths and all equal inner products for Hamming-distance-at-most-two pairs. The two vectors indexed by \(0,e_1\) are linearly independent by the first condition defining \(\mathcal U_n\). The equality of their \(2\times2\) Gram matrices produces one orthogonal map \(Q\in O(2)\) taking these two vectors of \(f\) to the corresponding vectors of \(h\).

Order the remaining cube vertices by increasing Hamming weight. Each other weight-one vertex \(e_i\) has the already recovered, independent comparison vertices \(0,e_1\), both at distance at most two from \(e_i\). For a vertex \(x\) of weight at least two, choose distinct indices \(i,j\) in its support; both predecessors \(u=x+e_i\) and \(v=x+e_j\) have weight one smaller and have Hamming distance two from each other. The condition on \(\mathcal U_n\) ensures these two known vectors of \(f\) are linearly independent. Their images under \(Q\) are likewise independent. Two prescribed inner products with an independent pair determine a vector in \(\mathbb R^2\) uniquely. Induction therefore forces \(h(x)=Qf(x)\) at every vertex. Every element of \(O(2)\) acting on complex coordinates is either global multiplication by a unit scalar or that multiplication followed by conjugation.

When \(n=2\), every pair of vertices is at distance at most two, so Steps 1–2 recover the entire real Gram matrix \(\operatorname{Re}(f(x)\overline{f(y)})\). Any two finite configurations in \(\mathbb R^2\) with the same complete Gram matrix differ by an orthogonal map, regardless of degeneracy. This establishes the unconditional assertion in dimension four.

**4. Sharp nonuniformity for higher even dimensions.** For even \(n\ge4\), choose two distinct vertices \(u,v\) at Hamming distance three. Let \(f\) vanish off \(\{u,v\}\), with nonzero values \(1,e^{i\alpha}\) there. No translate of \(S\) can contain both vertices, because all differences of elements of \(S\) have Hamming weight at most two. Consequently every \(I_f(t,b)\) depends only on \(|f(u)|,|f(v)|\), not on \(\alpha\). Two choices \(\alpha,\beta\) with \(\beta\not\equiv\pm\alpha\pmod{2\pi}\) yield identical measurements but are neither global-phase nor global-conjugation equivalent. Thus generic recovery cannot be strengthened to uniform conjugate recovery for \(n\ge4\).

## Verification
The standalone standard-library program `verify.py` tests every translation and modulation in dimensions \(n=2,3,4,5,6\). Its tests (i) invert each squared Walsh-magnitude array and check every local correlation exactly, (ii) recover the diagonal by rational Walsh division for even \(n\), (iii) reconstruct all complex coordinates by exact rational two-neighbor linear systems, and (iv) independently count nonzero star ambiguity coefficients and compare the predicted projector-span ranks. Odd dimensions in the script serve solely as a contrast for the convolution eigenvalue; they do not imply an odd-dimensional recovery theorem. Output ends in `BOOLEAN_STAR_WALSH_STFT_CHECKS_OK`. The universal proof above is symbolic; these finite calculations are reproducibility checks, not infinite certificates.

## Relationship to prior work
Bojarovska and Flinth [1] develop Gabor PhaseLift and ambiguity nonvanishing tests for global complex phase retrieval; a fixed real Walsh frame cannot be globally complex-phase-retrievable, and the star ambiguity vanishes extensively. Evans and Lai [2] develop conjugate phase retrieval by real frames and prove generic **frame** sufficiency. Here the frame is fixed, highly structured, rank-deficient as a linear matrix-sensing map, and the genericity concerns signals rather than measurement vectors. Cheng, Daubechies, Dym and Lu [3] treat locally stable complex phase retrieval via graph connectivity under local phase-retrievable measurement hypotheses. The binary-star real measurements do not locally distinguish conjugation; the argument uses explicit real Gram recovery and two-dimensional lateration instead. Bartusel [4] studies ordinary complex STFT phase retrieval for cyclic groups and broad ambiguity-function conditions; the present exponent-two Walsh group has only real characters and cannot have ordinary complex phase retrieval. The claimed contribution is the precise fixed-window conjugate-recovery theorem, rank and exceptional-signal boundary, not the general underlying frameworks.

## Limitations
No statement of historical priority beyond the bounded comparisons is made. The property is generic for even \(n\ge4\), not uniform; stability in noise and any odd-dimensional analogue are unproved. The condition defining \(\mathcal U_n\) is sufficient, not claimed necessary. The checker covers only five finite dimensions. Independent mathematical validation has not been performed.

## References
[1] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first public version 2015-03-19. Theorems 2.2–2.4, pp. 3–6. https://arxiv.org/abs/1503.05800

[2] L. Evans and C.-K. Lai, *Conjugate Phase Retrieval on \(\mathbb C^M\) by Real Vectors*, arXiv:1709.08836, first public version 2017-09-26. Theorems 2.3 and 2.5, pp. 5–9. https://arxiv.org/abs/1709.08836

[3] C. Cheng, I. Daubechies, N. Dym and J. Lu, *Stable Phase Retrieval from Locally Stable and Conditionally Connected Measurements*, arXiv:2006.11709, first public version 2020-06-21. Section 2, Proposition 2.6. https://arxiv.org/abs/2006.11709

[4] D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)*, arXiv:2206.06729, first public version 2022-06-14. Introduction, Section 2 and Section 4. https://arxiv.org/abs/2206.06729
