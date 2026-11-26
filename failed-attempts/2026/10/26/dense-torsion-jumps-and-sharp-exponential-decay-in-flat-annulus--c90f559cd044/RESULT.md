# Dense torsion jumps and sharp exponential decay in flat-annulus Bergman kernels

## Finding
Let \(\Lambda=\mathbb Z+i\mathbb Z\), \(E=\mathbb C/\Lambda\), \(X=E\setminus\{[0]\}\), and let \(\chi:\Lambda\to\mathbb T\) be any unitary character. The connected complex surface
\[
 B_\chi=\big((\mathbb C\setminus\Lambda)\times\{w:1<|w|<2\}\big)/\Lambda,
 \qquad \lambda\cdot(z,w)=(z+\lambda,\chi(\lambda)w)
\]
is Stein. Its square-integrable holomorphic canonical forms have an orthogonal Laurent decomposition containing precisely the degrees \(k\in\mathbb Z\) for which \(\chi^k=1\). Consequently, their complex dimension is one when \(\chi\) has infinite order and infinite when \(\chi\) has finite order.

Let \(\beta_0=dz\wedge dw/w\) and normalize the canonical norm as described below. The intrinsic diagonal evaluation density relative to \(\beta_0\), at a point represented by \((z,w)\) with \(|w|=t\in(1,2)\), depends only on \(t\). Write \(q\in\mathbb N\cup\{\infty\}\) for the order of \(\chi\). Its exact formula is
\[
 \mathcal K_\chi(t)=\begin{cases}
 (2\pi\log2)^{-1},&q=\infty,\\
 (2\pi\log2)^{-1}+\displaystyle\frac q\pi
 \sum_{j\ge1}\frac{j\big[(t/2)^{2qj}+t^{-2qj}\big]}{1-4^{-qj}},&q<\infty.
 \end{cases}
\]
For finite \(q\), denote the strictly positive surplus over the infinite-order value by \(\Delta_q(t)\). If \(I\Subset(1,2)\) and \(\sigma_I=\max_{t\in I}\max\{t/2,1/t\}<1\), then, uniformly for \(t\in I\),
\[
 \Delta_q(t)=\frac q\pi\big[(t/2)^{2q}+t^{-2q}\big]
 \big(1+O_I(\sigma_I^{2q})\big)\quad(q\to\infty).
\]
As a function of the character in the two-torus \(\operatorname{Hom}(\Lambda,\mathbb T)\), the density at each fixed \(t\in(1,2)\) is upper semicontinuous, continuous exactly at infinite-order characters, and discontinuous exactly at finite-order characters. The discontinuity set is countable and dense, with exact downward approach gap \(\Delta_q(t)\) at an order-\(q\) character.

## Assumptions and scope
All characters are *unitary*, the lattice is the square lattice, one point is deleted from the base elliptic curve, and the fiber is the fixed open annulus \(1<|w|<2\). This is a smooth, character-parametrized family of abstract Stein surfaces; no claim about a simultaneous holomorphic parameter family or embeddings in \(\mathbb C^2\) is made.

The Euclidean planar-area convention is \(dA(z)=dx\,dy\). Every canonical form has a unique lift \(\beta=F(z,w)\beta_0\), with \(F\) holomorphic and invariant under the displayed deck action. If \(Q=(-\tfrac12,\tfrac12)^2\subset\mathbb C\), its Hilbert norm is
\[
 \|\beta\|^2=\int_{Q\setminus\{0\}}\int_{1<|w|<2}
 |F(z,w)|^2\frac{dA(w)}{|w|^2}\,dA(z).
\]
This fixes the multiplicative normalization of the canonical \(L^2\) norm. The evaluation density is \(\mathcal K_\chi(t)=\sup_{\|\beta\|=1}|F(z,w)|^2\), independent of the representative and the angular coordinate.

## Proof
**Stein geometry.** The punctured elliptic curve \(X\) possesses a smooth proper strictly subharmonic exhaustion \(\tau\), for instance the sum of squared moduli of Weierstrass \(\wp\) and \(\wp'\) on this elliptic curve. Since deck transformations multiply \(w\) by unit-modulus constants, \(s=\log|w|\) descends to \(B_\chi\) and is locally pluriharmonic. Choose a smooth strictly convex function \(h\) on \((0,\log2)\) tending to \(+\infty\) at both ends, for example \(h(s)=1/s+1/(\log2-s)\). Then \(\rho=\tau+h(s)\) is proper and strictly plurisubharmonic: \(\tau\) controls every nonzero horizontal tangent component, while \(h''(s)|\partial s|^2\) controls the vertical direction. Thus \(B_\chi\) is Stein.

**All square-integrable Laurent modes.** Lift \(\beta\) to the covering and write
\[
 F(z,w)=\sum_{k\in\mathbb Z}c_k(z)w^k.
\]
The series converges normally on compact subannuli. Equivariance under the deck action gives
\[
 c_k(z+\lambda)=\chi(\lambda)^{-k}c_k(z).
\]
For \(C_k=2\pi\int_1^2u^{2k-1}\,du>0\), fiberwise Parseval and Tonelli yield
\[
 \|\beta\|^2=\sum_{k\in\mathbb Z}C_k\int_{Q\setminus\{0\}}|c_k(z)|^2\,dA(z).
\]
Each \(c_k\) is therefore square integrable near the deleted lattice point and extends holomorphically over it by the removable \(L^2\) singularity theorem. Equivariance extends it across every lattice point. Its absolute value is \(\Lambda\)-periodic, hence bounded on \(\mathbb C\). Liouville's theorem makes \(c_k\) constant. A nonzero constant satisfies the displayed equivariance if and only if \(\chi^k=1\). Conversely every finite combination of the permitted modes defines an integrable canonical form; completeness follows from the Parseval identity. This proves the exact orthogonal Hilbert sum of the modes. If \(q=\infty\), only \(k=0\) is allowed; if \(q<\infty\), exactly \(k\in q\mathbb Z\) are allowed.

**Kernel formula.** In the square fundamental cell, \(\int_QdA=1\). The norm of \(w^k\beta_0\) is \(\sqrt{C_k}\), and these permitted monomials form a complete orthogonal basis. Consequently
\[
 \mathcal K_\chi(t)=\sum_{\chi^k=1}\frac{t^{2k}}{C_k}.
\]
Explicit integration gives \(C_0=2\pi\log2\), \(C_n=\frac\pi n(4^n-1)\), and \(C_{-n}=\frac\pi n(1-4^{-n})\) for \(n\ge1\). Pairing the positive and negative degrees \(k=\pm qj\) yields the asserted series. The series converges absolutely and locally uniformly for \(1<t<2\), because the positive-degree terms decay as \((t/2)^{2qj}\) and the negative-degree terms as \(t^{-2qj}\).

**Sharp torsion-order tail.** For \(t\in I\), put \(a=(t/2)^2\), \(b=t^{-2}\), and \(s=\sigma_I^2<1\). The first pair \(j=1\) contributes
\[
 \frac q\pi\frac{a^q+b^q}{1-4^{-q}}.
\]
For \(x\in(0,1)\), \(\sum_{j\ge2}jx^j=x^2(2-x)/(1-x)^2\). Use this identity on \(x=a^q,b^q\), and the inequalities \((1-4^{-qj})^{-1}\le (1-4^{-q})^{-1}\). The remaining sum divided by the first-pair main scale \((q/\pi)(a^q+b^q)\) is \(O_I(s^q)\), uniformly in \(t\in I\). Also \((1-4^{-q})^{-1}=1+O(4^{-q})\), and \(4^{-q}\le s^q\) since \(\max\{t/2,1/t\}^2\ge1/2\). Therefore \(\Delta_q(t)=\frac q\pi(a^q+b^q)(1+O_I(s^q))\), as claimed.

**Exact discontinuity locus.** The character group identifies with the real two-torus via \(\chi(1)=e^{2\pi i\alpha}\) and \(\chi(i)=e^{2\pi i\gamma}\). Finite-order characters are precisely points with both \(\alpha,\gamma\in\mathbb Q/\mathbb Z\); they are countable and dense. At each such point the kernel exceeds the infinite-order baseline by \(\Delta_q(t)>0\), whereas arbitrarily close infinite-order characters have exactly the baseline kernel. Hence discontinuity holds at every torsion character. For a sequence of distinct torsion characters approaching an infinite-order character, their orders necessarily tend to infinity, because there are only finitely many characters of any bounded order. The uniform tail estimate then gives continuity at every infinite-order character. At a torsion character, there are only finitely many *different* bounded-order torsion characters, so a convergent sequence of distinct nearby parameters either has unbounded torsion order or infinite order; both types have kernels approaching the baseline. Exact repetitions contribute the higher value at the limit point. This proves upper semicontinuity everywhere.

## Verification
The accompanying Python 3 program `verify.py` checks the equality of two independently coded positive finite-series expressions for eighteen \((q,t)\) pairs, then checks twelve large-order comparisons to the leading asymptotic scale. The reported successful run was `VERIFY_OK direct_series_checks=18 tail_asymptotic_checks=12 all_checks=31`. These finite tests do not certify the infinite Laurent decomposition, uniform tail bound, or the topological continuity statement; those follow from the preceding proof.

## Relationship to prior work
Yuan's 2026 construction of a pseudoconvex domain with a one-dimensional Bergman space uses a punctured elliptic curve and an irrational annular twisting factor. Its Proposition 7 proves the single-character one-mode result and provides the foundational Laurent/Parseval argument, but does not classify all unitary characters, give the torsion-order kernel formula, or identify the dense discontinuity set and its exponential jump law. The present theorem stays on abstract flat annulus bundles and makes no new assertion about Euclidean domain embeddings.

Koltai–Kubasch–Szőke and Gallagher–Gupta–Vivas study bundle-valued Bergman spaces over Riemann surfaces, giving extensions and dimension criteria for base sections. Their statements do not directly describe the canonical Bergman kernels of two-dimensional annulus total spaces as the unitary character varies. Standard annular Laurent-series and orthogonality identities are used, not claimed as new. The claimed contribution is their joint application to the complete torsion transition and quantitative kernel discontinuity. Published priority beyond the inspected sources has not been exhaustively established.

## Limitations
Only the explicit square elliptic curve, one puncture, fixed radii \((1,2)\), unitary characters, and the specified canonical norm are treated. Results for other Riemann surfaces, nonunitary twists, other radii, higher-dimensional fibers, ambient Euclidean embeddings, or holomorphic parameter variations are not asserted. The new theorem has received self-review, not independent mathematical audit; priority relative to older annulus-bundle and deformation literature retains uncertainty.

## References
1. Yuan Yuan, *Pseudoconvex domains in complex Euclidean space with one-dimensional Bergman spaces*, arXiv:2610.21749v1, first posted 2026-10-15, especially Proposition 7 and Section 3. https://arxiv.org/html/2610.21749v1
2. L. Koltai, A. A. Kubasch, R. Szőke, *Bergman spaces on algebraic curves*, arXiv:2504.02341v1, first posted 2025-04-03, especially Theorem 2.19. https://arxiv.org/html/2504.02341v1
3. A.-K. Gallagher, P. Gupta, L. Vivas, *On the dimension of bundle-valued Bergman spaces on compact Riemann surfaces*, arXiv:2206.07120, first posted 2022-06-14; contextual result on base-curve sections. https://arxiv.org/abs/2206.07120
