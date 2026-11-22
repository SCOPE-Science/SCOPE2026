# Weak-seam reversal of finite Ising-ring heat capacities

## Finding
Let \(n\ge3\) be an integer, \(J>0\), and \(K=J/(k_{\mathrm B}T)>0\). Consider two zero-field Ising rings of \(n\) labeled spins: the first has \(n-1\) bonds of coupling \(+J\) and one distinguished bond of coupling \(+rJ\); the second changes only that distinguished coupling to \(-rJ\). Write their total heat capacities as \(C_+(T)\) and \(C_-(T)\). The following statements hold.

**Uniform-bond rigidity.** At \(r=1\), \(C_+(T)>C_-(T)\) for every \(n\ge3\) and every \(0<T<\infty\).

**Weak-seam reversal.** At every fixed \(0<r<1\) and every \(n\ge3\), the inequality is \(C_+(T)>C_-(T)\) at all sufficiently high temperatures, but \(C_+(T)<C_-(T)\) at all sufficiently low temperatures. At least one positive-temperature equality must therefore occur.

**Sharp near-uniform crossover.** Write \(r=1-\epsilon\). For each fixed \(n\ge3\), as \(\epsilon\downarrow0\), there is a locally unique equality in the window
\[
K=\frac12\log\frac1\epsilon+O(1),
\]
whose position satisfies
\[
\boxed{K_\epsilon=\frac12\log\frac1\epsilon+\frac14\log\!\left(\frac{4n^2(n+1)}3\right)+o(1).}
\]
More precisely, if \(s_* = \tfrac14\log(4n^2(n+1)/3)\), then on each fixed bounded interval in \(s\),
\[
\epsilon^{-2}\,\frac{\partial^2}{\partial K^2}\operatorname{artanh}\!\left(\tanh^{n-1}K\,\tanh((1-\epsilon)K)\right)
\underset{K=\frac12\log(1/\epsilon)+s}{\longrightarrow}
\frac83(n^2-1)e^{-4s}-\frac{2(n-1)}{n^2},
\]
uniformly along with the first \(s\)-derivative. The limiting expression has exactly one simple zero at \(s_*\). Local uniqueness here does **not** assert global uniqueness of all finite-\(\epsilon\) crossings.

## Assumptions and scope
The spins \(\sigma_i\in\{-1,1\}\) have periodic indexing \(\sigma_{n+1}=\sigma_1\). The Hamiltonians (at zero magnetic field) are
\[
H_+(\sigma)=-J\sum_{i=1}^{n-1}\sigma_i\sigma_{i+1}-rJ\sigma_n\sigma_1,
\quad
H_-(\sigma)=-J\sum_{i=1}^{n-1}\sigma_i\sigma_{i+1}+rJ\sigma_n\sigma_1.
\]
The positive prefactor \(k_{\mathrm B}\) is Boltzmann's constant. Heat capacity means total canonical heat capacity at fixed \(J,r,n\), not a per-site quantity: \(C_\pm/k_{\mathrm B}=K^2\partial_K^2\log Z_\pm(K)\). No thermodynamic phase transition is claimed, and no nonzero magnetic field is included.

## Proof
Put \(t=\tanh K\), \(u=t^{n-1}\tanh(rK)\), and \(f_{n,r}(K)=\operatorname{artanh}u\). The high-temperature expansion of the cycle partition function (equivalently, its two-by-two transfer matrix) gives exactly
\[
Z_\pm(K)=2^n(\cosh K)^{n-1}\cosh(rK)(1\pm u).
\]
The sign-independent factor cancels on subtraction. Since
\(\log(1+u)-\log(1-u)=2\operatorname{artanh}u\),
\[
\boxed{\frac{C_+-C_-}{k_{\mathrm B}}=2K^2 f_{n,r}''(K).}\tag{1}
\]

For \(r=1\), set \(y=t^2\) and differentiate \(f_{n,1}=\operatorname{artanh}(t^n)\) twice. An exact factorization yields
\[
f_{n,1}''(K)=
\frac{n t^{n-2}(1-t^2)^4}{(1-t^{2n})^2}
\sum_{j=0}^{n-2}(j+1)(n-1-j)t^{2j}.
\tag{2}
\]
To verify it algebraically, the numerator of the unsimplified derivative contains
\[
(n-1)-(n+1)y+(n+1)y^n-(n-1)y^{n+1}
=(1-y)^3\sum_{j=0}^{n-2}(j+1)(n-1-j)y^j.
\]
Every factor in (2) is strictly positive for \(K>0\). Equation (1) proves uniform-bond rigidity.

For fixed \(0<r<1\), Taylor expansion at \(K=0\) gives
\[
f_{n,r}''(K)=rn(n-1)K^{n-2}+O(K^n)>0
\]
for small positive \(K\). To inspect the opposite limit, set \(\epsilon=1-r\), \(q=e^{-2K}\), and \(a=e^{2\epsilon K}\). Rewriting the ratio \((1+u)/(1-u)\) as a ratio of the even and odd parts of
\((1+q)^{n-1}(1+a q)\) yields, for \(q\to0\) with fixed \(a\),
\[
f_{n,r}(K)=K-\frac12\log(n-1+a)+q^2 B_n(a)+O(q^4),
\tag{3}
\]
where the displayed coefficient is the rational function
\[
B_n(a)=\frac12\left[
\binom{n-1}{2}+(n-1)a
-\frac{\binom{n-1}{3}+\binom{n-1}{2}a}{n-1+a}
\right],\qquad B_n(1)=\frac{n^2-1}{6}.
\tag{4}
\]
The remainder in (3) is analytic near \((q,a)=(0,1)\), and can be differentiated there. For the fixed-\(r\) low-temperature limit, use the same exact even/odd ratio directly with \(a=e^{2\epsilon K}\) growing and \(a q=e^{-2rK}\downarrow0\). Its leading contribution gives
\[
f_{n,r}(K)=rK-\frac{n-1}{2}e^{-2\epsilon K}+o(e^{-2\epsilon K}),
\]
with the same asymptotic property for the first two derivatives of the remainder. Consequently
\[
f_{n,r}''(K)=-2(n-1)\epsilon^2 e^{-2\epsilon K}
+o(e^{-2\epsilon K})<0
\]
for sufficiently large \(K\). Continuity and (1) prove a crossing. (The expansions are only invoked for fixed \(n\) and strictly positive fixed \(r\).)

Finally take \(\epsilon\downarrow0\) and \(K=\frac12\log(1/\epsilon)+s\) with \(s\) in any fixed compact set. Then \(q=\epsilon e^{-2s}\) and \(a=e^{2\epsilon K}=1+o(1)\). Differentiating (3) twice and using (4) shows
\[
\epsilon^{-2} f_{n,1-\epsilon}''(K)
=\frac83(n^2-1)e^{-4s}-\frac{2(n-1)}{n^2}+o(1)
\tag{5}
\]
uniformly on compact \(s\)-sets. Analyticity gives the same uniform control on its first \(s\)-derivative. The right-hand side is strictly decreasing with its unique simple zero at
\(s_*=\frac14\log(4n^2(n+1)/3)\). For each sufficiently small fixed neighborhood of this zero, uniform sign and derivative control give exactly one zero of the left-hand side there for all sufficiently small \(\epsilon\), and its location tends to \(s_*\). This proves the sharp crossover law.

## Verification
Run `python verification.py` after installing `mpmath` (tested against version 1.3.0). The standalone script checks the all-size polynomial identity at 24 sizes by integer arithmetic, verifies (1) against direct Boltzmann enumeration of the \(2^n\) spin states for six small ring lengths, checks the sign and factorization of (2), and numerically checks the low-temperature and logarithmic crossover regimes. Its reproducible outcome is `SPECIFIC_HEAT_CHECKS_PASSED 143`. These finite tests corroborate (1)–(5) but do not replace their analytical proof. No externally certified formal proof is asserted.

## Relationship to prior work
Minami (1998) derived general transfer-matrix thermodynamic formulas for uniform, periodic, and disordered Ising-type chains, explicitly including specific heat; his broad generality is substantive prior coverage, although the full text was not accessible for a clause-by-clause comparison. Tonchev and Dantchev (2024) derived periodic/antiperiodic partition formulas and **discussed and plotted the specific heat** for both; their model includes the \(r=1\) input and supplies the closest explicit thermodynamic comparison. Their 2026 paper derived a finite-chain partition function with a single defective bond, covering the general partition-function input at \(0<r<1\). The proposed contribution is **not** another partition function: it is the strict all-temperature comparison at equal seam magnitude, its universal reversal for weaker seams, and the sharp singular logarithmic weak-defect window. The examined material did not explicitly state or imply these three sign and crossover classifications as an already-established theorem. Nevertheless their formulas are sufficient to start a derivation, and undiscovered statements in prior work remain a material priority risk.

## Limitations
This is a finite-ring result for \(n\ge3\), zero field, and one seam of identical absolute coupling in the compared models. The lower-temperature reversal is shown for each fixed \(0<r<1\); its exact number of crossings is not classified. The asymptotic location concerns a locally unique crossing as \(r\uparrow1\), not an assertion that other finite-defect roots cannot exist. Minami's 1998 restricted full text was not inspected, limiting the originality comparison. Independent scientific validation has not been performed.

## References
1. K. Minami, *The Susceptibility in Arbitrary Directions and the Specific Heat in General Ising-Type Chains of Uniform, Periodic and Random Structures*, J. Phys. Soc. Jpn. **67** (1998), 2255–2269, https://doi.org/10.1143/jpsj.67.2255 (published 1998-07-01).
2. N. S. Tonchev and D. Dantchev, *Chebyshev Polynomials in the Physics of the One-Dimensional Finite-Size Ising Model: An Alternative View and Some New Results*, preprint first posted 2024-11-05, https://doi.org/10.20944/preprints202411.0276.v1; peer-reviewed version in *Condensed Matter* **9** (2024), 53, https://doi.org/10.3390/condmat9040053.
3. N. S. Tonchev and D. Dantchev, *The Algebra of Chebyshev Polynomials and the Transfer-Matrix Approach for the One-Dimensional Ising Model with a Defect*, *Mathematics* **14** (2026), 741, https://doi.org/10.3390/math14040741.
