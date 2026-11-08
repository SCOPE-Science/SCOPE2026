# Sharp one-impulse repair of prime-power cubic Gabor chirps
## Finding
Let \(p\ge5\) be prime, \(a\ge2\) an integer, \(N=p^a\), \(\omega=e^{2\pi i/N}\), and \(0<\varepsilon\le1\). On \(\mathbb Z_N\) define the cubic chirp and its one-site perturbation by
\[
c(j)=\omega^{j^3},\quad h_\varepsilon(j)=c(j)+\varepsilon\mathbf 1_{\{0\}}(j),\quad g_\varepsilon(j)=\frac{h_\varepsilon(j)}{\sqrt{N+2\varepsilon+\varepsilon^2}}.
\]
For the unnormalized self-ambiguity convention
\[
A_f(k,\ell)=\sum_{j\in\mathbb Z_N}\overline{f(j)}f(j-k)\omega^{\ell j},
\]
the **sharp global ambiguity margin** is
\[
\boxed{\min_{k,\ell\in\mathbb Z_N}|A_{g_\varepsilon}(k,\ell)|=\frac{2\varepsilon\sin(\pi/(2p^{a-1}))}{N+2\varepsilon+\varepsilon^2}.}
\]
It is attained at translation \(k=p\) and modulation \(\ell=(p^{a-1}\pm1)/2\), interpreted modulo \(N\). Every ambiguity coefficient is nonzero, so all \(N^2\) cyclic Gabor intensity measurements recover every complex vector up to global phase, and the associated full complex-linear matrix-lifting map is invertible. Its sharp Hilbert--Schmidt-to-data condition number is
\[
\boxed{\kappa(\mathcal L_{g_\varepsilon})=\frac{N+2\varepsilon+\varepsilon^2}{2\varepsilon\sin(\pi/(2p^{a-1}))}.}
\]
In contrast, the unperturbed chirp \(c\) has matrix-lifting rank exactly
\[
\boxed{\operatorname{rank}\mathcal L_c=\frac{pN^2+1}{p+1},\qquad\dim\ker\mathcal L_c=\frac{N^2-1}{p+1}.}
\]
The strength \(\varepsilon=1\) maximizes the normalized minimum ambiguity over the stated interval \(0<\varepsilon\le1\).

## Assumptions and scope
All indices are modulo \(N\), with the standard unnormalized inner product on \(\mathbb C^N\). Put \((T_kf)(j)=f(j-k)\), \((M_\ell f)(j)=\omega^{\ell j}f(j)\), and \(\pi_{k,\ell}=M_\ell T_k\). Let \(P_{k,\ell}=\pi_{k,\ell}g_\varepsilon g_\varepsilon^*\pi_{k,\ell}^*\). The lifted map is the complex-linear analysis operator
\[
\mathcal L_{g_\varepsilon}(X)=\big(\operatorname{Tr}(P_{k,\ell}X)\big)_{k,\ell\in\mathbb Z_N}
\]
from matrices with the unnormalized Hilbert--Schmidt norm to data with the unnormalized Euclidean norm. For a signal \(x\), data \(|\langle x,\pi_{k,\ell}g_\varepsilon\rangle|^2\) are precisely the analysis values of the rank-one matrix \(xx^*\). The result neither assumes nor concludes that every \(N\)-element subfamily of the Gabor orbit is a basis (full spark).

## Proof
**1. Exact cubic sum.** For any nonzero \(k\), expansion of the cubic phase yields
\[
C(k,\ell):=A_c(k,\ell)=\omega^{-k^3}\sum_{j\bmod N}\omega^{-3kj^2+(3k^2+\ell)j}.
\]
Write \(t=v_p(k)\), so \(0\le t\le a-1\), and \(d=p^t\). Group the summands by \(j=x+m(N/d)\) with \(x\bmod N/d\), \(m\bmod d\). Since the quadratic coefficient is divisible by \(d\), the inner geometric sum vanishes unless \(d\mid3k^2+\ell\); this condition is equivalent to \(d\mid\ell\) because \(d\mid k\). When this divisibility holds the sum is \(d\) times a quadratic Gauss sum modulo \(N/d=p^{a-t}\), with quadratic coefficient \(-3k/d\) invertible modulo \(p\). Since \(p\ge5\) and \(2\) is invertible, the standard direct computation
\[
\left|\sum_{x\bmod q}e^{2\pi i(Ax^2+Bx)/q}\right|^2
=\sum_{u,v\bmod q}e^{2\pi i(Auv+Bu)/q}=q,
\quad q=p^{a-t},\ \gcd(A,q)=1,
\]
uses the invertible change \(u=x-y\), \(v=x+y\) (the linear term is a harmless character in \(u\)). Therefore
\[
C(k,\ell)=0\iff p^t\nmid\ell,
\qquad |C(k,\ell)|=p^{(a+t)/2}\text{ otherwise.}
\]
For \(k=0\), the pure chirp ambiguity is \(N\mathbf1_{\{\ell=0\}}\).

**2. Impulse expansion.** Directly expanding the perturbed factors gives, for \(k\ne0\),
\[
A_{h_\varepsilon}(k,\ell)=C(k,\ell)+\varepsilon\omega^{-k^3}(1+\omega^{\ell k}).
\]
When \(k=0\), the value is \(N+2\varepsilon+\varepsilon^2\) at \(\ell=0\) and \(2\varepsilon+\varepsilon^2\) at \(\ell\ne0\). The norm identity \(\|h_\varepsilon\|_2^2=N+2\varepsilon+\varepsilon^2\) gives the normalization.

**3. Sharp global minimum.** Whenever \(C(k,\ell)\ne0\) with \(k\ne0\), the reverse triangle inequality yields
\[
|A_{h_\varepsilon}(k,\ell)|\ge \sqrt N-2\varepsilon\ge5-2\varepsilon\ge3.
\]
The zero-translation coefficients have modulus at least \(2\varepsilon\). At a pure-chirp zero with \(k\ne0\), necessarily \(t=v_p(k)\ge1\) and \(p^t\nmid\ell\); the perturbation has exact modulus
\[
|A_{h_\varepsilon}(k,\ell)|=\varepsilon|1+\omega^{\ell k}|.
\]
Here \(\omega^{\ell k}\) has odd order dividing \(p^{a-t}\le p^{a-1}\). Among odd \(d\)-th roots of unity the minimum of \(|1+z|\) is \(2\sin(\pi/(2d))\). Consequently these coefficients have modulus at least \(2\varepsilon\sin(\pi/(2p^{a-1}))\). Taking \(k=p\) and \(\ell=(p^{a-1}\pm1)/2\) makes \(\omega^{\ell k}\) a root nearest to \(-1\) of order \(p^{a-1}\), so equality holds. The lower bounds for the other coefficients strictly exceed this value: \(3\ge2\varepsilon\), whereas the sine factor is strictly below one. Division by \(\|h_\varepsilon\|_2^2\) proves the first box.

**4. Lifting spectrum and conditioning.** The matrices \(\pi_{k,\ell}/\sqrt N\) form an orthonormal Hilbert--Schmidt basis. Conjugating one basis element by a Gabor shift multiplies it by a phase-space character. Therefore the images of these basis vectors under \(\mathcal L_{g_\varepsilon}\) are mutually orthogonal, and their norms are precisely \(\sqrt N|A_{g_\varepsilon}(k,\ell)|\), up to index reflection which preserves the multiset. This proves the complete singular-value multiset, positivity, and invertibility. By Cauchy--Schwarz, \(|A_{g_\varepsilon}(k,\ell)|\le\|g_\varepsilon\|_2^2=1\), with equality at \((0,0)\). Dividing the largest singular value by the minimum from Step 3 gives the stated condition number. The nonvanishing self-ambiguity criterion for Gabor phase retrieval is also proved in [2, Theorem 2.2]; here invertibility of the entire lifting map yields injectivity directly.

**5. Unperturbed rank.** For each \(t\in\{0,\ldots,a-1\}\), precisely \((p-1)p^{a-t-1}\) nonzero translations have valuation \(t\), and exactly \(p^{a-t}\) modulations are divisible by \(p^t\). Thus, including \((0,0)\), the number of nonzero ambiguity coefficients equals
\[
1+\sum_{t=0}^{a-1}(p-1)p^{2(a-t)-1}
=1+\frac{p(p^{2a}-1)}{p+1}=\frac{pN^2+1}{p+1}.
\]
Step 4 identifies this count as the matrix-lifting rank; subtracting from \(N^2\) gives the nullity. Finally, the derivative of \(\varepsilon/(N+2\varepsilon+\varepsilon^2)\) has numerator \(N-\varepsilon^2>0\) on \((0,1]\), proving the last assertion.

## Verification
Run `python CHECK.py` in the same directory as this file. It evaluates the defining time-domain ambiguity sum independently and compares the sharp global margin and original rank census in prime-power dimensions \(25,49,125\), with multiple positive perturbation strengths. It checks a sharp minimizing index, exact Gauss-sum zero-pattern predictions, and the expected singular-value/condition formula. These finite computations corroborate the exact all-parameter proof, which does not rely on exhaustive numerical enumeration.

## Relationship to prior work
Dongwei Li [1, Proposition 5.1] explicitly proves the vanishing of the *unmodified* cubic chirp's ambiguity at prime powers; this obstruction and the starting Gauss sum are previously known. Li's constructions that remove ambiguity zeros use algebraic perturbation and different seeds, and do not state the present one-real-impulse repair, its sharp all-mode constant, or the complete unmodified lifting nullity. Bojarovska and Flinth [2, Theorem 2.2] furnish the general nonvanishing-ambiguity phase-retrieval criterion but no specific one-site cubic theorem. A previously published exact one-positive-impulse classification for **quadratic** chirps [3] has pure-chirp ambiguity on one line and a different half-order sine margin; neither its formula nor its rank mechanism covers the imprimitive quadratic sums created by a **cubic** phase modulo prime powers. In particular the present theorem is not a claim of optimizing over all windows or of a simultaneous full-spark construction.

## Limitations
All formulas require the odd-prime-power cyclic ring, \(p\ge5\), exponent \(a\ge2\), and real \(0<\varepsilon\le1\). There is no global optimality statement among arbitrary perturbations or all Gabor windows. The sharp condition number is for full complex-linear lifting with all \(N^2\) measurements, not a direct Euclidean-distance Lipschitz bound between phase equivalence classes; no finite-sample or adversarial erasure guarantee or full-spark property is claimed. Although the compared primary texts do not state the new sharp one-site result, analogous formulations in older radar-sequence and finite-frame literature remain a publication-priority risk.

## References
1. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614, first submitted 2026-09-09; in particular Proposition 5.1, Sections 2--3 and 5, full primary text inspected.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first submitted 2015-03-19; Theorem 2.2, full primary text inspected.
3. *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, published research result, `2026/10/11/SCOPE-single-impulse-quadratic-chirps-exact-cyclic-gabor-tomography-sp--03361b3cff9c`; primary `RESULT.md` inspected in full.
