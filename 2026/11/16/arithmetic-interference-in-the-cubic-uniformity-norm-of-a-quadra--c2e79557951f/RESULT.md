# Arithmetic interference in the cubic uniformity norm of a quadratic cosine chirp

## Finding

For any odd prime \(p\) and integer \(n\ge1\), put \(q=p^n\), \(G=\mathbb F_p^n\), \(Q(x)=\sum_{j=1}^n x_j^2\) (computed in \(\mathbb F_p\)), and
\[
f(x)=\cos\!\left(\frac{2\pi Q(x)}p\right)
=\tfrac12\left(e^{2\pi i Q(x)/p}+e^{-2\pi i Q(x)/p}\right).
\]
Let \(\chi_p\) denote the quadratic Legendre character, let \(\epsilon_p=1\) for \(p\equiv1\pmod4\) and \(\epsilon_p=i\) for \(p\equiv3\pmod4\), and set \(\nu=\chi_p(-1)^n\). When \(\nu=1\), define the real sign \(\eta=(\epsilon_p\chi_p(2))^n\in\{-1,1\}\). Then, with the normalized Gowers cube average,
\[
256\|f\|_{U^3(G)}^8=
\begin{cases}
2+16\eta q^{-1/2}+68q^{-1}+112\eta q^{-3/2}+58q^{-2},&\nu=1,\\
2+20q^{-1}-6q^{-2},&\nu=-1.
\end{cases}
\]
The limiting independent-phase benchmark is \(1/128\) for \(\|f\|_{U^3}^8\). The exact sign of the finite-size correction is positive when \(\nu=-1\) or \((\nu,\eta)=(1,1)\), and strictly negative when \((\nu,\eta)=(1,-1)\). Thus a superposition of two individually perfect quadratic phases exhibits either constructive or destructive cubic-uniformity interference according to arithmetic parity. In particular, \(\|f\|_{U^3(\mathbb F_5)}^8=(7-3\sqrt5)/100\), below \(1/128\), while \(\|f\|_{U^3(\mathbb F_3)}^8=1/32\), above it.

## Assumptions and scope

The norm is defined, for every complex function \(g:G\to\mathbb C\), by
\[
\|g\|_{U^3(G)}^8=\mathbb E_{x,h_1,h_2,h_3\in G}\prod_{v\in\{0,1\}^3}\mathcal C^{|v|}g(x+v_1h_1+v_2h_2+v_3h_3),
\]
where \(\mathcal C\) is complex conjugation. Every expectation is uniform probability average, and the quadratic form is the diagonal nonsingular form over the **prime** field, not an arbitrary quadratic form or an arbitrary extension-field trace form. Since \(f\) is real, all eight factors inside the cube are simply values of \(f\).

## Proof

**Quadratic expansion.** Write \(e_p(t)=\exp(2\pi i t/p)\). Expanding each of the eight cosine factors gives \(2^8\) sign patterns \(c=(c_v)_{v\in\{0,1\}^3}\in\{-1,1\}^8\), with
\[
256\|f\|_{U^3}^8=\sum_c \mathbb E_{y\in(\mathbb F_p^n)^4} e_p\!\left(\sum_v c_v Q(x+v_1h_1+v_2h_2+v_3h_3)\right).
\]
For \(u_v=(1,v_1,v_2,v_3)^{\mathsf T}\in\mathbb Z^4\), introduce the integral symmetric matrix
\[
A_c=\sum_v c_v u_vu_v^{\mathsf T}.
\]
The exponent splits into \(n\) independent four-variable quadratic forms \(z^{\mathsf T}A_cz\). Hence the corresponding normalized average is the \(n\)-th power of a four-variable quadratic Gauss average.

**Complete finite matrix certificate.** Exhaustive *integer* evaluation of all \(256\) matrices gives the following counts, grouped by rank and by the sign and absolute value of the determinant of the first nonsingular maximal principal minor (indices in lexicographic order):

| Rank | Maximal principal-minor determinant | Count |
|---|---|---:|
| 0 | \(0\) | 2 |
| 1 | \(-2,+2\) | \(8,8\) |
| 2 | \(-4,+4,-16\) | \(38,24,6\) |
| 3 | \(-8,+8\) | \(56,56\) |
| 4 | \(-16,+16,+64\) | \(32,24,2\) |

These counts sum to \(256\). The finite certificate is not an extrapolation from numerical experimentation: the accompanying standalone `check.py` constructs each of the \(256\) sign matrices, computes all principal minors using their exact integer Leibniz determinants, and asserts every displayed count. Every nonzero maximal minor has determinant \(\pm2^j\). Therefore the rational ranks are unchanged modulo **every odd prime**: a nonzero maximal minor survives, while larger minors vanish identically over the integers. For a symmetric form in odd characteristic, a nondegenerate maximal principal subspace splits off the radical; its determinant represents the discriminant square class of the nondegenerate quotient.

**Gauss evaluation.** For a rank-\(r\) symmetric form with nondegenerate discriminant \(\Delta\) over \(\mathbb F_p\), the normalized average on \(\mathbb F_p^4\) is
\[
p^{-r/2}\epsilon_p^r\chi_p(\Delta).
\]
Apply this identity independently in the \(n\) coordinates and sum the certificate counts. Ranks \(1\) and \(3\) contribute respectively
\[
8(1+\nu)(\epsilon_p\chi_p(2))^nq^{-1/2},\quad
56(1+\nu)\nu(\epsilon_p\chi_p(2))^nq^{-3/2};
\]
rank \(2\) contributes \((24\nu+44)q^{-1}\); rank \(4\) contributes \((26+32\nu)q^{-2}\); rank \(0\) contributes \(2\). When \(\nu=-1\) the odd-rank terms cancel, yielding the second branch. When \(\nu=1\), the phase \(\eta\) is real and equals \(\pm1\), yielding the first branch.

**Sign law.** The correction in the \(\nu=-1\) case is \((20q-6)/(256q^2)>0\). For \(\nu=1,\eta=1\) it is visibly positive. In the remaining case, writing \(t=\sqrt q>1\), the numerator of the correction after multiplying by \(256q^2\) is
\[
-16t^3+68t^2-112t+58.
\]
It equals \(-2\) at \(t=1\), and its derivative is \(-8(6t^2-17t+14)<0\) for every real \(t\), since the quadratic has negative discriminant and positive leading coefficient. Thus the correction is strictly negative. This proves the complete arithmetic sign classification and the displayed examples.

## Verification

Running `python3 check.py` with Python's standard library reconstructs all \(256\) integer matrices and all maximal principal minors, then independently enumerates complete four-variable cubes for the seven cases \((p,n)=(3,1),(5,1),(7,1),(11,1),(13,1),(3,2),(5,2)\). Each brute-force value agrees with the theorem to an absolute tolerance of \(2\cdot10^{-10}\). This numerical check is supplementary; the finite exact matrix certificate and the universal Gauss-sum identity cover all odd primes and positive dimensions. The certificate does not require precomputed matrices or downloaded data.

## Relationship to prior work

Candela, González-Sánchez and Szegedy developed spectral decompositions and approximate Parseval identities for quadratic higher-order Fourier analysis; their manuscript uses individual quadratic chirps and Gauss sums in an operator example, but the inspected material and searches do not identify this explicit two-chirp Gowers norm or its sign bifurcation. Kuo developed estimation algorithms for \(U^k\) norms on finite abelian groups and gives no matching exact quadratic-cosine benchmark in the inspected text. Classical inverse theorems describe correlation with quadratic phases, but do not by themselves evaluate the mixed eight-cube interference of a *sum* of opposite quadratic phases. The essential new asserted computation is the dimension-uniform rank/discriminant enumeration and resulting exact arithmetic sign law, not the general theory of Gowers norms or quadratic Gauss sums.

## Limitations

The result is for the specific equal-amplitude opposite-phase pair defined above. No general formula is claimed for arbitrary phase weights, quadratic-form ranks, linear perturbations, or higher \(U^k\) norms. The proof's finite table is small and fully enumerated, but a related computation may exist under terminology such as Gaussian cubic correlations or quadratic bias; priority remains subject to independent literature scrutiny. The published higher-order Fourier framework supplies context rather than logically requiring this explicit formula. No independent audit has been performed.

## References

- P. Candela, D. González-Sánchez and B. Szegedy, *Spectral algorithms in higher-order Fourier analysis*, arXiv:2501.12287v1 (first submitted 2025-01-21); Forum of Mathematics, Sigma (2026), doi:10.1017/fms.2026.10238. https://arxiv.org/abs/2501.12287
- E.-J. Kuo, *Quantum algorithms for Gowers norm estimation, polynomial testing, and arithmetic progression counting over finite abelian groups*, arXiv:2508.01231 (first submitted 2025-08-02); Quantum Information Processing 25 (2026), article 141, doi:10.1007/s11128-026-05165-6. https://link.springer.com/article/10.1007/s11128-026-05165-6
- B. Green and T. Tao, *An inverse theorem for the Gowers \(U^3(G)\) norm*, Proceedings of the Edinburgh Mathematical Society 51 (2008), 73–153. https://doi.org/10.1017/S0013091505000325
- Classical quadratic Gauss sum evaluation (standard identity used in the proof); see e.g. B. C. Berndt, R. J. Evans and K. S. Williams, *Gauss and Jacobi Sums*, Wiley (1998).
