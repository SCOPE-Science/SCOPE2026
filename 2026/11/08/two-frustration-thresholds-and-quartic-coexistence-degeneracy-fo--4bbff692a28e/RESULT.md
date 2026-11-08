# Two frustration thresholds and quartic coexistence degeneracy for hypercube Ising antiferromagnets

## Finding
For every integer \(d\ge4\), put an Ising spin \(\sigma_x\in\{-1,1\}\) at each of the \(2^d\) vertices \(x\in\{-1,1\}^d\). Give each unordered pair at Hamming distance one positive coupling \(J_1\) and each unordered pair at distance two positive coupling \(J_2\). There is no magnetic field. Write \(g=J_2/J_1\), \(\theta_1=1/(d-1)\), and \(\theta_2=1/(d-3)\). Define \(\theta_3=1/(d-5)\) for \(d\ge6\), and \(\theta_3=+\infty\) for \(d=4,5\).

The exact ground-state energy at **every** positive coupling ratio is
\[
E_0=2^{d-1}\min_{0\le k\le d}\left\{J_1(d-2k)+\frac{J_2}{2}\bigl((d-2k)^2-d\bigr)\right\}.
\]
For the first three open coupling regimes and their two boundaries, the **complete** numbers of labeled spin configurations attaining \(E_0\) are

| Coupling regime | Minimizing Fourier level(s) | Ground-state degeneracy |
|---|---|---|
| \(0<g<\theta_1\) | \(d\) | \(2\) |
| \(g=\theta_1\) | \(d-1,d\) | \(2(d+1)\) |
| \(\theta_1<g<\theta_2\) | \(d-1\) | \(2d\) |
| \(g=\theta_2\) | \(d-2,d-1\) | \(2d+2\binom d2+24\binom d3+24\binom d4\) |
| \(\theta_2<g<\theta_3\) | \(d-2\) | \(2\binom d2+24\binom d4\) |

For \(d\ge6\), no degeneracy statement is asserted at or beyond \(\theta_3\). The energy formula itself remains valid there. At the second boundary, the four-variable contributions make the finite-size coexistence degeneracy grow quartically in \(d\). The assertion is about finite systems with \(2^d\) sites, not thermodynamic phase transitions.

## Assumptions and scope
For an integer \(d\ge4\), let \(V=\{-1,1\}^d\), and let \(\operatorname{dist}(x,y)\) count differing coordinates. The Hamiltonian counts each pair exactly once:
\[
H(\sigma)=J_1\sum_{\{x,y\}:\operatorname{dist}(x,y)=1}\sigma_x\sigma_y
 +J_2\sum_{\{x,y\}:\operatorname{dist}(x,y)=2}\sigma_x\sigma_y,
\qquad J_1,J_2>0.
\]
Spins are labeled by distinct vertices; spin reversal counts as a different configuration. \(\binom dr=0\) when \(r>d\). The all-dimensional energy formula applies for arbitrary strictly positive \(J_1,J_2\); the displayed multiplicity table stops before the next Fourier-level crossing, if one exists.

## Proof
**1. Exact spectral bound and attainment.** For \(S\subseteq\{1,\ldots,d\}\), define the Walsh character \(\chi_S(x)=\prod_{i\in S}x_i\). The distance-one and distance-two adjacency operators act on \(\chi_S\) by the respective eigenvalues
\[
\lambda_1(k)=d-2k,\qquad
\lambda_2(k)=\binom d2-2k(d-k)=\frac{(d-2k)^2-d}{2},\quad k=|S|.
\]
Writing \(\widehat\sigma(S)=2^{-d}\sum_x\sigma_x\chi_S(x)\), Parseval gives \(\sum_S\widehat\sigma(S)^2=1\), hence
\[
H(\sigma)=2^{d-1}\sum_S\widehat\sigma(S)^2
 \bigl[J_1\lambda_1(|S|)+J_2\lambda_2(|S|)\bigr]
 \ge2^{d-1}\min_k(J_1\lambda_1(k)+J_2\lambda_2(k)).
\]
Every \(\chi_S\) is itself a legal \(\{-1,1\}\)-spin configuration, so equality is achieved at any minimizing \(k\); this proves the global energy formula. Equality occurs **only** when the Walsh support of \(\sigma\) lies in the minimizing levels.

**2. Thresholds.** Put \(\Lambda(k)=J_1(d-2k)+J_2((d-2k)^2-d)/2\). The exact adjacent difference is
\[
\Lambda(k)-\Lambda(k-1)=-2\bigl(J_1+J_2(d-2k+1)\bigr).
\]
Because \(J_2>0\), \(\Lambda\) is strictly convex as a function of real \(k\). Its last successive crossings, working down from \(k=d\), are therefore exactly \(g=1/(d-1)\), \(g=1/(d-3)\), and, when \(d\ge6\), \(g=1/(d-5)\). Only the levels in the table are minimizing in its stated open regimes; at each listed boundary exactly the two indicated adjacent levels tie.

**3. Reduction to low-degree Boolean functions.** Multiplying any spin function by \(\chi_{\{1,\ldots,d\}}\) complements each Fourier degree: level \(k\) becomes degree \(d-k\). Thus the phases in the table correspond respectively to Boolean functions (functions taking exactly the values \(\pm1\)) supported in Fourier degree: zero; zero or one; one; one or two; and two. The degree-zero case has two signs. A Boolean Fourier polynomial of degree at most one is a constant or \(\pm x_i\); the possible signs and coordinates give \(2(d+1)\), with \(2d\) for pure degree one.

**4. Complete finite bound for degree two.** A Boolean polynomial \(f\) of Walsh degree at most two depends on at most four coordinates. Indeed, if coordinate \(i\) is relevant, its discrete derivative \((f(x_i=1)-f(x_i=-1))/2\) is a nonzero affine function of the other variables. Such a function is nonzero on at least half the discrete cube, so \(\operatorname{Inf}_i(f)\ge1/2\). Parseval gives \(\sum_i\operatorname{Inf}_i(f)=\sum_S|S|\widehat f(S)^2\le2\). There are therefore at most four relevant coordinates. (This is the degree-two case of the classical degree/influence argument.)

For a **fixed** set of precisely \(r\) relevant coordinates, exhaustive enumeration of the complete \(2^{2^r}\) Boolean truth tables for \(r\in\{1,2,3,4\}\), retaining only zero-mean Fourier-degree-at-most-two tables, gives the exact counts
\[
(c_1,c_2,c_3,c_4)=(2,2,24,24).
\]
If Fourier degree is **exactly two with no degree-one or degree-zero coefficient**, the corresponding counts are \((0,2,0,24)\). These are finite theorems, not estimates: the included `verify.py` computes all integral Walsh sums and checks the exact classes. Independent constructive checks also recover the 24 three-variable balanced degree-two functions as signed two-branch multiplexers and the 24 four-variable pure-degree-two functions as signed \(2\times2\) cross products with negative sign product. Each of these 24 constructions is verified against the complete finite set of eligible truth tables.

The number of zero-mean degree-at-most-two Boolean functions on \(d\) variables is consequently \(\sum_{r=1}^4 c_r\binom dr\); the number with pure degree two is \(2\binom d2+24\binom d4\). These yield the final two entries of the table, completing the proof.

## Verification
Run `python3 verify.py` with standard Python 3; no third-party dependencies or network connection are needed. The script enumerates every \(\pm1\)-valued truth table on up to four Boolean variables, applies an exact integer Walsh–Hadamard transform, checks the variable-support and degree filters, and independently constructs the full three- and four-variable extremizer sets. Separately, a Gray-code enumeration visits all \(2^{16}=65536\) configurations of the four-dimensional hypercube spin model and reproduces the following \((J_1,J_2;E_0,\text{degeneracy})\): \((1,0;-32,2)\) as a boundary diagnostic outside the positive-coupling theorem, \((3,1;-48,10)\), \((2,1;-32,8)\), \((1,1;-16,140)\), and \((1,2;-32,36)\). Exact rational samples independently test the claimed minimizing Fourier levels for dimensions four through twenty. The global energy and multiplicity conclusions rely on the preceding analytic argument plus the complete four-variable finite census, not on extrapolation from these samples.

## Relationship to prior work
The frustrated nearest-/next-nearest-neighbor Ising system is established on the **square lattice** in Kalz, Honecker and Moliner (2011), but its graph and field-theoretic phase results do not imply the finite-Boolean-hypercube thresholds and multiplicities here. Nisan and Szegedy's (1994, originally 1992) degree/influence framework supplies a general four-coordinate reduction; its degree bounds are not this Ising counting theorem. Jovanovski (2017) studies ferromagnetic **nearest-neighbor-only** Ising dynamics on the Boolean hypercube with a field, a distinct Hamiltonian and question. The spectral method and the low-degree reduction are acknowledged as standard ingredients; the claimed result is their exact coupling-dependent ground-state classification and coexistence multiplicities for this two-range antiferromagnet.

## Limitations
No conclusion is drawn about thermal criticality, nonzero temperature, external fields, nonuniform couplings, or degeneracy at and beyond the third threshold when \(d\ge6\). Mathematical originality is conditional on accessible literature comparison: an unindexed exact enumeration of the same model could precede this classification. No independent scientific audit has been performed.

## References
- A. Kalz, A. Honecker, M. Moliner, *Analysis of the phase transition for the Ising model on the frustrated square lattice*, first posted 2011-05-24, https://arxiv.org/abs/1105.4836.
- N. Nisan, M. Szegedy, *On the degree of Boolean functions as real polynomials*, Computational Complexity 4 (1994), 301–313; earlier STOC 1992, https://doi.org/10.1007/BF01263419.
- O. Jovanovski, *Metastability for the Ising Model on the Hypercube*, Journal of Statistical Physics 167 (2017), 135–159, https://doi.org/10.1007/s10955-017-1736-8.
