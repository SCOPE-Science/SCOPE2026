# The sharp pentagonal modular-sampling gap and its quadratic stability law

## Finding
Let \(\zeta=e^{2\pi i/5}\), and equip \(\mathbb R^5\) with its ordinary Euclidean norm. Define the real first-harmonic sample plane
\[
E=\{(a\cos(2\pi j/5)+b\sin(2\pi j/5))_{j=0}^4:a,b\in\mathbb R\},
\]
let \(P\) be its orthogonal projector, and put
\[
\Delta(f)=\min_{n\in\mathbb Z^5}\|f-n\|_2\qquad(f\in E).
\]
Thus \(\Delta(f)\) is the Euclidean distance between the five samples of a real, zero-mean degree-one trigonometric polynomial and their reductions modulo one.

**Pentagonal modular-stability theorem.** For every nonzero \(n=(n_0,\ldots,n_4)\in\mathbb Z^5\) with \(\sum_jn_j=0\), define
\[
\beta_n=\frac{\sum_{j=0}^4n_j\zeta^j}{1-\zeta}\in\mathbb Z[\zeta].
\]
Then the **exact arithmetic product identity** is
\[
\boxed{\|Pn\|_2\,\|(I-P)n\|_2=\frac2{\sqrt5}\sqrt{|N_{\mathbb Q(\zeta)/\mathbb Q}(\beta_n)|}\ \ge\ \frac2{\sqrt5}.}
\]
Equality holds exactly when \(\beta_n\) is a unit of \(\mathbb Z[\zeta]\). Consequently, the modulo-one sampling map is injective on \(E\), and its sharp asymptotic distance constant is
\[
\boxed{\liminf_{\substack{f\in E\\\|f\|_2\to\infty}}\|f\|_2\Delta(f)=\frac2{\sqrt5}.}
\]
For its inverse Lipschitz amplification on the sample-energy ball,
\[
L(B)=\sup_{\substack{f\in E\\0<\|f\|_2\le B}}\frac{\|f\|_2}{\Delta(f)},
\]
one has, with \(\varphi=(1+\sqrt5)/2\), **for every \(B\ge2\)**,
\[
\boxed{\frac{\sqrt5}{2\varphi^2}B^2<L(B)\le2B^2.}
\]
In particular the quadratic growth exponent is optimal. Neither inequality asserts an exact leading constant for \(L(B)\).

## Assumptions and scope
The sampling grid comprises all five equally spaced sites on the unit circle. The signal is **real**, has no constant Fourier mode, and is restricted to frequencies \(\{-1,1\}\). Modulo one is applied coordinatewise; the appropriate output metric is \(\Delta(f-g)\) for the difference of two signals, not ordinary distance between discontinuously wrapped representatives. Euclidean sample energy is \(\|f\|_2^2=(5/2)(a^2+b^2)\). The integer lattice scale is exactly one; a different folding period rescales the statements. No claim is made for arbitrary Fourier bandwidth, irregular grids, additive sample noise models, or exact finite-radius leading constants.

## Proof
1. **Fourier decomposition.** For real \(n\), write \(S_r(n)=\sum_{j=0}^4n_j\zeta^{rj}\). Orthogonality of the fifth roots gives
\[
\|Pn\|_2^2=\frac25|S_1(n)|^2,\qquad
\|(I-P)n\|_2^2=\frac15|S_0(n)|^2+\frac25|S_2(n)|^2.
\]
2. **Exact cyclotomic norm.** If \(S_0(n)=0\), the polynomial \(\sum_jn_jz^j\) is divisible by \(1-z\) in \(\mathbb Z[z]\), so \(\beta_n\in\mathbb Z[\zeta]\). The four conjugates of \(\alpha=\sum_jn_j\zeta^j\) are \(S_1,S_2,\overline{S_2},\overline{S_1}\). Hence
\[
|S_1(n)|^2|S_2(n)|^2=|N(\alpha)|=5|N(\beta_n)|,
\]
because \(N(1-\zeta)=\Phi_5(1)=5\). If \(n\ne0\) with zero coordinate sum, \(\alpha\ne0\): otherwise its degree-at-most-four polynomial is an integer multiple of \(1+z+z^2+z^3+z^4\), whose coefficient sum cannot vanish unless it is zero. Thus \(N(\beta_n)\) is a nonzero integer. Substituting the Fourier decomposition gives the claimed identity. A cyclotomic integer has norm of absolute value one precisely when it is a unit (the adjugate gives an integral inverse), proving the equality classification.
3. **Injectivity and lower asymptotic estimate.** If \(f\in E\cap\mathbb Z^5\), then \(S_0(f)=S_2(f)=0\), so the above Galois relation forces \(S_1(f)=0\) and \(f=0\). For any \(f\in E\), let \(n\) be a nearest integer vector and let \(\delta=\Delta(f)\le\sqrt5/2\). If \(S_0(n)\ne0\), then \(\delta\ge1/\sqrt5\). If \(n=0\), then \(\delta=\|f\|_2\). In the remaining case \(n\ne0\) and \(S_0(n)=0\), the exact identity and orthogonality imply
\[
(\|f\|_2+\delta)\delta\ge\|Pn\|_2\|(I-P)n\|_2\ge2/\sqrt5.
\]
These three cases give \(\liminf_{\|f\|_2\to\infty}\|f\|_2\Delta(f)\ge2/\sqrt5\).
4. **Golden-unit upper sequence.** The cyclotomic unit \(u=1+\zeta+\zeta^{-1}\) has conjugate absolute values \(\varphi\) and \(\varphi^{-1}\) at \(\zeta\) and \(\zeta^2\), respectively. For every integer \(k\ge0\), let \(n^{(k)}\) be the unique augmentation-zero integer coefficient vector of \((1-\zeta)u^k\), obtained by cyclic convolution of \((1,-1,0,0,0)\) with \((1,1,0,0,1)\) exactly \(k\) times. For \(f_k=Pn^{(k)}\),
\[
\|f_k\|_2=\sqrt{\tfrac25}|1-\zeta|\varphi^k,\qquad
\Delta(f_k)\le\sqrt{\tfrac25}|1-\zeta^2|\varphi^{-k}.
\]
Their right-hand-side product is \(2/\sqrt5\), so \(\|f_k\|_2\to\infty\) and the reverse liminf bound follows.
5. **Sharp conditioning exponent.** For any \(0<\|f\|_2\le B\), the cases in step 3 give respectively \(\|f\|_2/\Delta(f)\le\sqrt5 B\), \(=1\), or at most \((\sqrt5/2)B(B+\sqrt5/2)\). For \(B\ge2\), each is at most \(2B^2\). Conversely choose the largest \(k\ge0\) with \(\|f_k\|_2\le B\). Since consecutive norms grow by \(\varphi\), one has \(\|f_k\|_2>B/\varphi\). The product upper bound in step 4 then gives
\[
L(B)\ge\frac{\|f_k\|_2}{\Delta(f_k)}\ge\frac{\sqrt5}2\|f_k\|_2^2>\frac{\sqrt5}{2\varphi^2}B^2.
\]
This proves all conclusions for every stated quantifier and boundary.

## Verification
Run `python3 check.py` with Python 3's standard library. It performs 624 exact integer checks of the cyclotomic multiplication norm, compares their projection products numerically, and checks the unit construction at 20 successive exponents. Its reported output ends in `PASS`. This is diagnostic evidence; the infinite theorem follows from the displayed algebraic argument and not from enumeration. In the checker, determinant computations and the representation of cyclotomic integers are exact integers, while trigonometric projection comparisons are floating-point diagnostics.

## Relationship to prior work
Romero and Shafkulovska (2026) establish qualitative unbounded-input instability and bounded-input stability for infinite-dimensional folded Paley–Wiener sampling, using a general lattice-distance formulation. Zhang et al. (2023/2024) and Mulleti–Eldar (2022/2024) treat identifiability of finite Fourier or periodic-bandlimited samples modulo a folding threshold; the present **injectivity** assertion is not claimed as new in isolation. The new quantitative object is the exact mixed-projection product for the five-point zero-mean first harmonic, including its cyclotomic-unit equality cases, sharp asymptotic distance constant, and quadratic inverse-Lipschitz growth. Existing cyclotomic ideal-lattice theory describes related norms but does not, among the relevant material inspected, give this particular modulo-sampling stability theorem. This is a comparison to inspected statements, not a claim that no equivalent result exists.

## Limitations
The problem is intentionally restricted to the first nontrivial small prime sample length: for three or four equally spaced samples, the analogous zero-mean first-harmonic plane contains nonzero integer sample vectors, hence modulo recovery is not globally injective. The exact liminf concerns unbounded signal energy and does not give the exact value of \(L(B)\) for every finite \(B\). Near-integer distance is measured after folding in a toral metric. Earlier algebraic-lattice or sampling work could contain an equivalent specialization; no independent mathematical review has been performed.

## References
- J. L. Romero and I. Shafkulovska, *Stability in unlimited sampling*, first posted 2026-03-25, https://arxiv.org/abs/2603.24425.
- Q. Zhang, J. Zhu, F. Qu, Z. Zhu, and D. W. Soh, *On the Identifiability from Modulo Measurements under DFT Sensing Matrix*, first posted 2023-12-30, https://arxiv.org/abs/2401.00194.
- S. Mulleti and Y. C. Eldar, *Modulo Sampling of FRI Signals*, first posted 2022-07-18, https://arxiv.org/abs/2207.08774.
- R. Cramer, L. Ducas, and B. Wesolowski, *Mildly Short Vectors in Cyclotomic Ideal Lattices in Quantum Polynomial Time*, J. ACM 68 (2021), https://doi.org/10.1145/3431725.
