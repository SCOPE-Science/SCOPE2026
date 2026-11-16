# Lattice Fourier samples distinguish finite mixtures of Euclidean balls in dimension at least two

## Finding
Let \(d\ge 2\) and let \(\Lambda\subset\mathbb R^d\) be an arbitrary full-rank lattice. For a center \(c\in\mathbb R^d\) and radius \(r>0\), write \(B(c,r)=\{x:|x-c|<r\}\). For every finite family of **distinct** parameters
\[
 ([c_j],r_j)\in (\mathbb R^d/\Lambda)\times(0,\infty),\qquad 1\le j\le m,
\]
the sequences of lattice Fourier samples
\[
 \left(\widehat{\mathbf 1_{B(c_j,r_j)}}(\xi)\right)_{\xi\in\Lambda^*},\qquad 1\le j\le m,
\]
are linearly independent over \(\mathbb C\). Here \([c]\) is the residue of the center modulo \(\Lambda\), and \(\Lambda^*=\{\xi:\langle\xi,\lambda\rangle\in\mathbb Z\ \forall\lambda\in\Lambda\}\).

Equivalently, **all** dual-lattice Fourier samples of a finite complex-weighted sum of ball indicators determine all parameter pairs \(([c],r)\) with nonzero aggregated coefficients, and their coefficients, after combining any repeated pairs. There is no restriction on radii, mutual overlaps, the number of balls, or the signs and phases of coefficients. Only lattice translation of an individual center is undetectable.

The dimension restriction is sharp. For \(d=1\) and \(\Lambda=s\mathbb Z\), with \(s>0\), the complete kernel consists precisely of finite sums \(f=\sum_j a_j\mathbf1_{(c_j-r_j,c_j+r_j)}\) satisfying **both**
\[
 \sum_j a_j\bigl(\delta_{[c_j-r_j]}-\delta_{[c_j+r_j]}\bigr)=0
 \quad\text{as a measure on }\mathbb R/s\mathbb Z,
\]
and
\[
 \sum_j 2a_jr_j=0.
\]
In particular, intervals of length \(s\) at distinct centers have identical complete Fourier samples on \(s^{-1}\mathbb Z\).

## Assumptions and scope
We use the Fourier convention
\[
 \widehat f(\xi)=\int_{\mathbb R^d}f(x)e^{-2\pi i\langle\xi,x\rangle}\,dx.
\]
Every sum is finite, every coefficient is complex, and every radius is strictly positive. Open versus closed balls makes no difference to these samples. In the independence statement, distinctness is for the combined pair \(([c],r)\), not necessarily for the radius alone or center alone. The sampled set includes the zero frequency. The one-dimensional condition describes the kernel, not merely a necessary obstruction.

## Proof
**1. Periodization preserves precisely the sampled information.** Set
\[
 (P_\Lambda f)(x)=\sum_{\lambda\in\Lambda}f(x+\lambda).
\]
For compactly supported integrable \(f\), this sum is locally finite and \(\Lambda\)-periodic. If \(Q\) is any fundamental cell, unfolding gives
\[
 \frac1{|Q|}\int_Q(P_\Lambda f)(x)e^{-2\pi i\langle\xi,x\rangle}\,dx
 =\frac1{|Q|}\widehat f(\xi),\qquad \xi\in\Lambda^*.
\]
Uniqueness of Fourier coefficients for \(L^1(\mathbb R^d/\Lambda)\) implies that all sampled coefficients vanish exactly when \(P_\Lambda f=0\) almost everywhere.

**2. A separating sphere patch exists in dimension at least two.** Suppose
\[
 \sum_{j=1}^m a_jP_\Lambda\mathbf1_{B(c_j,r_j)}=0\quad\text{a.e.}
\]
with pairwise distinct \(([c_j],r_j)\). Fix \(j\), and consider the sphere \(S_j=\partial B(c_j,r_j)\) in Euclidean space. Every boundary sphere in this locally finite periodized collection has the form \(\partial B(c_i+\lambda,r_i)\), for some \(i\) and \(\lambda\in\Lambda\). None is equal to \(S_j\), except the same \(i=j\) and \(\lambda=0\): equality of Euclidean spheres in dimension at least two forces equality of centers and radii, hence the same parameter pair. Two distinct Euclidean spheres have no relatively open common patch on \(S_j\); indeed their intersection, if nonempty, lies in a proper affine hyperplane obtained by subtracting their quadratic equations. Only finitely many of the other spheres meet a fixed compact neighborhood of \(S_j\). Therefore one can choose \(x_j\in S_j\) outside **every** other sphere.

Choose a sufficiently small connected Euclidean ball \(U\) centered at \(x_j\) that meets no boundary sphere other than \(S_j\). On \(U\), every other indicator in the periodized sum is locally constant. Only \(\mathbf1_{B(c_j,r_j)}\) changes from zero to one across \(S_j\). Thus the two almost-everywhere constant values of the alleged zero periodization on the respective sides of \(S_j\) differ by exactly \(a_j\). Both values must be zero, so \(a_j=0\). Since \(j\) was arbitrary, all coefficients vanish. Grouping equal parameter pairs establishes the full classification.

**3. The exact one-dimensional exception.** For \(d=1\), differentiation on the quotient circle \(\mathbb R/s\mathbb Z\) in the distributional sense gives
\[
 (P_{s\mathbb Z} f)'=\sum_j a_j\left(\delta_{[c_j-r_j]}-\delta_{[c_j+r_j]}\right).
\]
A locally integrable function on a connected circle with zero distributional derivative is constant almost everywhere. Its integral over one period is, by unfolding, \(\sum_j2a_jr_j\). Hence its constant value is zero exactly when the endpoint measure vanishes **and** that integral is zero. Step 1 now proves both directions of the asserted kernel criterion. For the sharp counterexample take any \(t\notin s\mathbb Z\):
\[
 f=\mathbf1_{(0,s)}-\mathbf1_{(t,t+s)}.
\]
Both interval periodizations equal one almost everywhere, so \(f\ne0\) has every dual-lattice Fourier sample zero.

## Verification
The proof is exact and works for an arbitrary full-rank lattice, arbitrary finite number of parameters, and every dimension claimed. The separating-patch argument uses local finiteness, rigidity of coincident spheres, and the fact that a nonempty sphere has positive dimension when \(d\ge2\). These are not finite-enumeration assumptions.

A reproducibility script, `CHECK.py`, evaluates the planar disk Fourier formula
\[
 \widehat{\mathbf1_{B(c,r)}}(k)=
 \begin{cases}\pi r^2,&k=0,\\
 e^{-2\pi i\langle k,c\rangle}\,rJ_1(2\pi r|k|)/|k|,&k\ne0,
 \end{cases}
\]
checks numerical rank for six illustrative disks and translation invariance on 81 frequencies, and checks the one-dimensional length-one interval alias. Run `python CHECK.py` with the packages in `requirements.txt`. This finite demonstration does **not** establish infinite-sample independence; the geometric proof does.

## Relationship to prior work
Asipchuk and Robins (2026), *Fourier sampling on a lattice*, Theorem 1, characterize equality of lattice samples of bounded set indicators by lattice equidecomposition; their Theorem 2 obtains single-translation rigidity under an anti-aliasing hypothesis. The result above instead classifies the entire kernel of lattice sampling on **finite weighted ball mixtures**, without anti-aliasing. The distinguishing new step is separation of curved boundary patches after arbitrary lattice folding; the cited set theorem does not state this weighted, unrestricted-radius classification. The class is structured and smaller than all measurable sets, and the result does not contradict their general counterexamples.

Kuratsubo and Nakai (2020), *Multiple Fourier series and lattice point problems*, introduce periodized radial ball indicators and their Fourier-Bessel coefficients, but the inspected discussion concerns Fourier-series convergence and lattice-point asymptotics, not the linear independence and alias classification here. Rocha-Neves (2026) proves a separate uniqueness result from lattice-point enumerators over **all real dilations and translates**, which is substantially more measurement information than one fixed dual-lattice frequency grid.

## Limitations
This is injectivity from **all** dual-lattice samples, not a finite-frequency recovery algorithm or a noise-stability estimate. It concerns finite linear combinations of Euclidean ball indicators, not arbitrary connected convex bodies or their Boolean unions. Since lattice translations of individual centers preserve all measurements, those translations cannot be recovered; identical parameter pairs must be aggregated. A prior equivalence in older curved-interface inverse problems remains a publication-priority risk.

## References
1. O. Asipchuk and S. Robins, *Fourier sampling on a lattice*, arXiv:2608.29217 (first publicly listed September 1, 2026), especially Theorems 1–2 and Section 3. https://arxiv.org/abs/2608.29217
2. S. Kuratsubo and E. Nakai, *Multiple Fourier series and lattice point problems*, arXiv:2011.06178 (2020), especially equations (1.7)–(1.9). https://arxiv.org/abs/2011.06178
3. A. Rocha-Neves, *A Fourier-analytic Uniqueness Theorem for Lattice-point Enumerators*, arXiv:2608.11078 (August 11, 2026). https://arxiv.org/abs/2608.11078
