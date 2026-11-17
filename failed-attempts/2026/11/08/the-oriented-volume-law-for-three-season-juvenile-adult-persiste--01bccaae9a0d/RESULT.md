# The oriented-volume law for three-season juvenile–adult persistence

## Finding

For a population with juvenile and adult abundance, let three distinct seasonal projection matrices be
\[
B_i(\mu)=\begin{pmatrix}0&\mu b_i\\s_i&a_i\end{pmatrix}\quad(i=1,2,3),
\]
where \(0<a_i<1\), \(0<s_i<1\), \(b_i>0\), and \(\mu>0\). Write \(P_+=B_3B_2B_1\) for the repeating season order \(1,2,3\), and \(P_-=B_2B_3B_1\) for the repeating season order \(1,3,2\). The other four orders are cyclic rotations of these two and therefore have the same respective Floquet multipliers. Let
\[
\Delta=\det\begin{pmatrix}a_1&b_1&s_1\\a_2&b_2&s_2\\a_3&b_3&s_3\end{pmatrix}.
\]
For all admissible vital rates and every \(\mu>0\),
\[
\operatorname{sgn}\bigl(\rho(P_+)-\rho(P_-)\bigr)=\operatorname{sgn}(\Delta).
\]
The two orientations have *identical full Floquet spectra* if and only if \(\Delta=0\). In particular, the better orientation for long-run linear population growth is independent of the scale \(\mu\) of adult fertility.

When \(\Delta\ne0\), the two orientations have distinct critical fertility multipliers, and some open range of \(\mu\) makes one orientation exponentially growing and the other exponentially declining. With only one or two seasonal matrices, permutation of the same matrices can never change the long-run Floquet spectrum; three seasons is the smallest possible period for this phenomenon.

## Assumptions and scope

The state \((J_t,A_t)^\mathsf T\) gives nonnegative juvenile and adult abundances at discrete times. The matrix \(B_i(\mu)\) maps one census to the next: adults produce \(\mu b_i\) juveniles, juveniles survive and mature with probability \(s_i\), and adults survive in the adult stage with probability \(a_i\). Adult fertility may exceed one; survival probabilities are strictly between zero and one. Each of the three seasonal environments is used exactly once per repeating three-step cycle. Only their temporal order varies; the environment-specific triplets \((a_i,b_i,s_i)\) and \(\mu\) do not change. The deterministic system is linear, representing low-density asymptotic growth or decline. The per-step asymptotic multiplicative growth factor is \(\rho(P)^{1/3}\).

The result concerns spectral thresholds and deterministic low-density abundance, not a stochastic extinction probability, not nonlinear persistence under density dependence, and not a real-world change of climate-season order.

## Proof

Define the positive constants
\[
A=a_1a_2a_3,\qquad Q=b_1b_2b_3s_1s_2s_3,
\]
\[
C_+=a_1b_2s_3+a_2b_3s_1+a_3b_1s_2,
\]
\[
C_-=a_1b_3s_2+a_2b_1s_3+a_3b_2s_1.
\]
Direct two-by-two matrix multiplication yields the exact characteristic data
\[
\operatorname{tr}(P_\pm)=A+\mu C_\pm,\qquad
\det(P_\pm)=-\mu^3Q.
\]
The determinant equality also follows by multiplying \(\det B_i=-\mu b_is_i\). Expanding the determinant of the matrix of vital-rate triples gives
\[
C_+-C_-=\Delta.
\]
For any three square matrices, cyclic rotations of the product preserve characteristic polynomials (here also because all \(B_i\) are invertible), hence the six time orders reduce to the two displayed orientations.

As every \(B_i\) has nonnegative entries and positive off-diagonal and bottom-right entries, any three-factor product is strictly positive. Its two eigenvalues are real and of opposite sign because its determinant is negative. Its Perron root is therefore
\[
R(T)=\frac{T+\sqrt{T^2+4\mu^3Q}}2,
\]
where \(T>0\) is the trace. This expression is strictly increasing in \(T\). Since the determinant is the same for both orientations and the trace difference is \(\mu\Delta\), their Perron-root difference has exactly the sign of \(\Delta\). Equality of the two traces is equivalent to equality of their characteristic polynomials, proving the isospectral case.

For stability boundaries, put \(g_\pm(\mu)=A+\mu C_\pm+\mu^3Q\). Because \(0<A<1\) and \(C_\pm,Q>0\), each \(g_\pm\) is strictly increasing from \(A\) to infinity and crosses one at a unique \(\mu_\pm>0\). The characteristic polynomial evaluated at one is
\[
\det(I-P_\pm)=1-g_\pm(\mu).
\]
The second eigenvalue is negative, so \(\rho(P_\pm)>1\) precisely when \(g_\pm(\mu)>1\). If \(\Delta>0\), then \(C_+>C_-\), so \(\mu_+<\mu_-\), and for \(\mu_+<\mu<\mu_-\) the plus orientation grows while the minus orientation declines. For \(\Delta<0\) the roles reverse. At \(\Delta=0\) the two thresholds coincide. With two seasons, the two orders differ only by exchanging factors \(B_1B_2\) and \(B_2B_1\), which always have identical characteristic polynomials. For one season there is no ordering choice. This proves sharpness.

For a completely rational witness take
\[
(a_1,a_2,a_3)=(1/4,1/2,3/4),\quad
(b_1,b_2,b_3)=(1/2,2,1/2),\quad
(s_1,s_2,s_3)=(1/2,1/2,1/2),\quad \mu=1.
\]
Then
\[
\Delta=-3/8,\qquad \operatorname{tr}(P_+)=21/32,\qquad
\operatorname{tr}(P_-)=33/32,\qquad
\det(P_\pm)=-1/16.
\]
Consequently \(\det(I-P_+)=9/32>0\) while \(\det(I-P_-)=-3/32<0\), so \(\rho(P_+)<1<\rho(P_-)\). Thus changing only the order of the same three environmental vital-rate vectors reverses the deterministic persistence threshold.

## Verification

The complete symbolic proof requires only direct multiplication of three two-by-two matrices, the determinant identity, and monotonicity of the Perron-root formula. A reproducible exact-arithmetic checker `verify.py` verifies the universal symbolic trace and determinant identities, the rational witness, the two classes of all six temporal permutations, and 1,000 generated rational-parameter instances. It requires Python 3 and SymPy; run `python verify.py`. Exact sampled checks support, but do not replace, the universal algebraic proof above.

## Relationship to prior work

Cushing (2006) derives a general periodic juvenile–adult projection model and studies how phases of vital-rate oscillations affect critical fertility. Its three-period calculation concerns the *local derivative* of a critical threshold with respect to fertility-amplitude perturbation. The present result instead fixes three arbitrary positive vital-rate triples, permutes them, and gives a global, all-\(\mu\) ordering law by a signed determinant. Cushing and Ackleh (2011), Caswell and Trevisan (1994), and Caswell and Shyu (2012) treat periodic population matrices, reproduction thresholds, and sensitivities more generally. Cyclic order invariance is classical and is expressly not claimed as a new phenomenon. The determinant ranking, exact equality surface, minimal period and opposite-growth witness are the combined contribution here. An equivalent result in earlier matrix-product or population-matrix literature remains a priority risk.

## Limitations

Only the two-stage matrix form with zero juvenile-to-juvenile stasis and positive adult stasis is covered. With additional stages or different transition placement, the signed determinant rule need not hold. The findings concern Floquet multipliers, not finite-time transient size, nonlinear coexistence, stochastic extinction, or practical instructions to reorder seasons. The literature comparison is a best-knowledge result rather than proof of absolute historical novelty; some full texts were not accessible.

## References

1. J. M. Cushing, “A juvenile-adult model with periodic vital rates,” *Journal of Mathematical Biology* 53 (2006), 520–539, first published online April 24, 2006. DOI: https://doi.org/10.1007/s00285-006-0382-6 . Author-hosted full text: https://math.arizona.edu/~cushing/AJuvenileAdultModelWithPeriodicVitalRates%20JMB06.pdf .
2. J. M. Cushing and A. S. Ackleh, “A net reproductive number for periodic matrix models,” *Journal of Biological Dynamics* (2011), online February 18, 2011. DOI: https://doi.org/10.1080/17513758.2010.544410 .
3. H. Caswell and M. C. Trevisan, “Sensitivity analysis of periodic matrix models,” *Ecology* 75 (1994). DOI: https://doi.org/10.2307/1937455 .
4. H. Caswell and E. Shyu, “Sensitivity analysis of periodic matrix population models,” *Theoretical Population Biology* (2012). DOI: https://doi.org/10.1016/j.tpb.2012.03.008 .
5. H. Caswell, “Periodic Models,” in *Sensitivity Analysis: Matrix Methods in Demography and Ecology* (2019), https://link.springer.com/chapter/10.1007/978-3-030-10534-1_8 .
