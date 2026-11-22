# A sharp two-collision \(\Lambda(4)\) plateau and the first two taxicab resonances

## Finding
Let \(G\) be a compact abelian group with normalized Haar measure and let \(\Lambda\subset\widehat G\) be a finite set of distinct characters. Assume that the unordered pair-product map
\[\{\lambda,\mu\}\longmapsto\lambda\mu,\qquad \lambda,\mu\in\Lambda,\]
with repetitions allowed in the input pair, is injective except at **exactly two distinct products**, each having exactly two unordered preimages. Assume also that both collisions involve four distinct characters, and their two four-character supports share **exactly one** character. For every complex trigonometric polynomial \(F=\sum_{\lambda\in\Lambda}a_\lambda\lambda\),
\[
\boxed{\ \|F\|_{L^4(G)}^4\le\frac94\left(\sum_{\lambda\in\Lambda}|a_\lambda|^2\right)^2.\ }
\]
The coefficient \(9/4\) is sharp. Every nonzero equality polynomial is supported on **one** of the two collision quartets, has four coefficients of the same modulus, and satisfies the aligning phase relation \(a_u a_v\overline{a_w a_z}>0\) when that quartet obeys \(uv=wz\). Conversely, every such polynomial is an equality case.

**Cubic-spectrum consequence.** Put \(\Lambda_N=\{e^{ik^3t}:1\le k\le N\}\) on the circle. Its sharp coefficient-\(\ell^2\) to Fourier-\(L^4\) constant \(K_4(\Lambda_N)\) satisfies
\[
K_4(\Lambda_N)^4=\begin{cases}
2-1/N,&1\le N\le11,\\
9/4,&12\le N\le23.
\end{cases}
\]
For \(N\in[12,15]\), all extremizers use only modes \(\{1,9,10,12\}\); for \(N\in[16,23]\), they use exactly one of \(\{1,9,10,12\}\) and \(\{2,9,15,16\}\), with equal magnitudes and the corresponding aligned phases. In particular, the **second** cubic two-sum resonance at \(2^3+16^3=9^3+15^3\) does not increase the sharp fourth-moment constant. The first two resonance values are \(1729\) and \(4104\).

## Assumptions and scope
A pair-product collision means two different unordered multisets of two characters with the same product. A collision on four distinct characters is equivalent, in additive frequency notation, to a nontrivial equality of two disjoint two-element sums. The two collided product values must be different; all other unordered pair products have multiplicity one. The quartets have exactly one common character and therefore seven characters in their union. The group can be infinite or finite, and all coefficients can be complex. Norms use Haar probability measure. No claims are made for arbitrary sets with three or more collided products, two collision quartets intersecting in two or more characters, or higher Fourier moments.

For the cubic consequence, \(L^4\) uses normalized Lebesgue measure on \(\mathbb T\), and frequencies are positive integer cubes. Finite ranges through \(N=23\) are claimed; the next distinct collision occurs at \(N=24\), so no continuation of this formula is asserted.

## Proof
**1. The exact fourth-moment identity.** Parseval for \(F^2\) gives a baseline \(2S^2-\sum_\lambda|a_\lambda|^4\), where \(S=\sum_\lambda|a_\lambda|^2\), when unordered products are all distinct. Each collision of two disjoint off-diagonal pairs \(uv=wz\) contributes exactly
\[8\operatorname{Re}(a_ua_v\overline{a_wa_z}).\]
By hypothesis these are the only corrections. Label the common character \(0\), and relabel the other six so the two product identities are \(\lambda_0\lambda_1=\lambda_2\lambda_3\) and \(\lambda_0\lambda_4=\lambda_5\lambda_6\). Thus
\[
\|F\|_4^4=2S^2-\sum_j|a_j|^4+8\operatorname{Re}(a_0a_1\overline{a_2a_3}+a_0a_4\overline{a_5a_6}),
\]
with any other characters included in the negative sum.

**2. Reduction to seven coefficients.** Homogeneity lets us take \(S=1\). Put \(t_j=|a_j|^2\) on the seven collision characters, and \(T=\sum_{j=0}^6 t_j\le1\). Let \(M(t_0,\ldots,t_6)\) denote the negative sum \(-\sum_{j=0}^6t_j^2\) plus the two aligned, nonnegative quartic interference terms. The next steps prove \(M\le T^2/4\) for all seven nonnegative weights. Then automatically
\[\|F\|_4^4\le2+T^2/4-\sum_{\mathrm{outside}}|a_\lambda|^4\le9/4.\]
Equality requires \(T=1\), so all outside coefficients vanish.

**3. Seven-weight bound.** If \(T>0\), divide all squared moduli by \(T\), and henceforth assume \(T=1\). Write \(x=t_0\), \(A=t_1+t_2+t_3\), \(B=t_4+t_5+t_6\), so \(x+A+B=1\). The arithmetic-geometric mean and Cauchy inequalities give
\[
\sum_{j=1}^3t_j^2\ge A^2/3,\quad
\sqrt{t_1t_2t_3}\le(A/3)^{3/2},
\]
with corresponding inequalities for \(j=4,5,6\). Therefore
\[
\|F\|_4^4\le \Phi(x,A,B):=
2-x^2-\frac{A^2+B^2}{3}
+\frac{8\sqrt x}{3\sqrt3}(A^{3/2}+B^{3/2}).\tag{1}
\]
(The displayed \(F\) here refers to the seven-character polynomial.) If \(x=0\) or \(x=1\), its fourth power is at most \(2\), strictly below \(9/4\). Otherwise let \(\rho=1-x>0\) and \(A=\rho z\), \(B=\rho(1-z)\). The derivative of the \(z\)-dependent part of (1) is
\[
(\sqrt z-\sqrt{1-z})\left[-\frac{2\rho^2}{3}(\sqrt z+\sqrt{1-z})
+\frac{4\sqrt x\,\rho^{3/2}}{\sqrt3}\right].\tag{2}
\]
On \([1/2,1]\), \(\sqrt z+\sqrt{1-z}\) is decreasing. Thus the bracket in (2) increases, and any interior stationary point away from \(z=1/2\) is a **minimum**, not a maximum. By symmetry the maximum over \(z\in[0,1]\) occurs either at \(z=0,1\) or at \(z=1/2\).

If \(z\in\{0,1\}\), only one collision is active. Let \(u_1,\ldots,u_4\ge0\) be the four squared moduli, with sum one. Then \(\sum u_i^2\ge1/4\) and \(\sqrt{u_1u_2u_3u_4}\le1/16\), giving
\[2-\sum_{i=1}^4u_i^2+8\sqrt{u_1u_2u_3u_4}\le9/4.\]
Equality occurs only when all four weights equal \(1/4\).

If \(z=1/2\), (1) reduces to
\[
\Phi_{\mathrm{bal}}(x)=2-x^2-\frac{(1-x)^2}{6}
+\frac{8}{3\sqrt6}\sqrt x(1-x)^{3/2}.\tag{3}
\]
With \(y=\sqrt{x/(1-x)}\ge0\), the strict inequality \(\Phi_{\mathrm{bal}}(x)<9/4\) is equivalent to
\[
15y^4+6y^2+5-\frac{32}{\sqrt6}y>0.\tag{4}
\]
The exact sum-of-squares identity
\[
15y^4+6y^2+5-\frac{32}{\sqrt6}y
=15(y^2-1/4)^2+\frac{27}{2}\left(y-\frac{32}{27\sqrt6}\right)^2+\frac{1169}{1296}
\]
proves (4) strictly. Thus any optimizer concentrates on a **single** collision quartet. Equality in the initial phase and balancing inequalities then requires exactly four equal squared moduli \(1/4\) and the aligned product phase. This completes the general theorem.

**4. Cubic prefix enumeration.** The exhaustive finite integer computation described in the verification script enumerates every unordered pair \((j,k)\) with \(1\le j\le k\le23\), groups by \(j^3+k^3\), and finds precisely the two multiple-preimage sums
\[
1729=1^3+12^3=9^3+10^3,\qquad
4104=2^3+16^3=9^3+15^3.
\]
The first appears exactly when \(N=12\), the second exactly when \(N=16\); their quartets share only mode \(9\). At \(N=24\) a third appears: \(13832=2^3+24^3=18^3+20^3\). For \(N\le11\), the no-collision identity and Cauchy yield \(K_4^4=2-1/N\), with all magnitudes equal at equality. For \(12\le N\le15\), the elementary single-quartet argument above gives \(9/4\), and for \(16\le N\le23\), the general theorem gives \(9/4\). In both regimes all equality cases are as stated.

## Verification
Run \(\texttt{python3 verify\_cubic\_two\_collisions.py}\) with Python 3 and SymPy. Its exact integer enumeration checks all \(2300\) unordered cubic pair sums across prefix lengths \(1\) through \(23\), tests the third collision at \(24\), and verifies the seven-character model. Seven hundred seeded Gaussian-integer coefficient vectors test the complete fourth-moment identity by two independent computations: direct convolution and the two-collision formula. Two equality witnesses are evaluated in exact rational arithmetic, and the symbolic sum-of-squares identity is expanded and checked exactly. Expected output:

```text
VERIFY_OK finite_prefixes=23 unordered_pairs=2300 exact_moment_checks=700 equality_witnesses=2 sos_identity=1
```

The finite checks certify the finite pair-sum enumeration, not the universal inequality. The latter is proved analytically in Steps 1–3. No numerical optimization, sampling, or finite experiment substitutes for a proof over arbitrary compact abelian groups.

## Relationship to prior work
Vasilyev's August 19, 2026 preprint, *Norm bounds on Fourier series with polynomial spectra and constrained coefficients*, proves uniform fourth-moment control for polynomial Fourier spectra under nonincreasing coefficient magnitudes; it does not give the exact two-collision constant for unrestricted complex coefficients. Gabdullin and Konyagin's earlier *Trigonometric polynomials with frequencies in the set of cubes* explicitly identifies the taxicab relation at \(1729\), establishes short-interval Sidon results and qualitative fourth-moment estimates, but does not determine the full first-two-resonance sharp norm or its optimizers.

The published note *Sharp \(\Lambda(4)\) constants for a single pair-product collision* proves the sharp \(9/4\) value when there is **only one** disjoint-pair collision. The present theorem addresses the different configuration of **two distinct** collisions with overlapping four-character supports. Its conclusion does not follow by simply applying the one-collision theorem, whose hypothesis fails for the seven-character core and for cubic prefixes \(N\ge16\). The proof above controls their interacting quartic contributions simultaneously. The plateau is an implication stronger than the first-collision fact alone.

## Limitations
The result concerns only fourth moments, exactly two pair-product collisions of the specified incidence type, and cubic prefixes up to index \(23\). It does not resolve the general \(\Lambda(4)\)-set problem for all cubes or the sharp constants once further taxicab representations appear. An unindexed or differently phrased theorem about two-overlap additive-energy configurations may exist; novelty is assessed relative to the searched sources, not certified historical uniqueness. There has been no independent mathematical audit.

## References
1. I. Vasilyev, *Norm bounds on Fourier series with polynomial spectra and constrained coefficients*, arXiv:2608.19132, first public 2026-08-19, https://arxiv.org/abs/2608.19132.
2. M. R. Gabdullin and S. V. Konyagin, *Trigonometric polynomials with frequencies in the set of cubes*, arXiv:2311.14937, first public 2023-11-25, https://arxiv.org/abs/2311.14937.
3. *Sharp \(\Lambda(4)\) constants for a single pair-product collision*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-lambda-4-constants-for-a-single-pair-product-collision--b11b0dc59997.
