# Sharp self-commutator asymptotics for critical power-Fock Volterra shifts

## Finding

Fix an integer \(m\ge3\) and let \(\mathcal F_m\) be the Hilbert space of entire functions with squared norm
\[
\|f\|_m^2=\int_{\mathbb C}|f(z)|^2 e^{-2|z|^m}\,dA(z),
\]
where \(dA\) is planar Lebesgue measure. For \(V_m f(z)=\int_0^z m w^{m-1}f(w)\,dw\), the positive self-commutator \(D_m=V_m^*V_m-V_mV_m^*\) is trace class, with
\[
\operatorname{tr}D_m=m,\qquad s_j(D_m)\sim\frac{m(3m-4)}{2j^2}\quad(j\to\infty).
\]
In particular \(D_m\in\mathcal S_p\) exactly for \(p>1/2\) (among \(p>0\)). The singular-value constant refers to the full space, with multiplicities and singular values indexed from one. It quantifies the compact self-commutator of the noncompact critical Volterra operator.

## Assumptions and scope

Only the critical pure symbol \(g(z)=z^m\) at exponent \(m\ge3\) is treated. Neither a classification of monomial or mixed polynomial normality nor the Gaussian case \(m=2\) is asserted as a contribution. The operator is initially defined on polynomials; the bounded extension below agrees with the integral on the space by its Taylor coefficients. For \(p>0\), \(\mathcal S_p\) consists of compact operators whose singular values have summable \(p\)-th powers.

## Proof

Angular integration makes the monomials an orthogonal complete basis: integrating the Taylor series on each circle gives the sum of squared coefficients times powers of the radius, and one can integrate the nonnegative terms radially. With \(h_n=\|z^n\|_m\), substitution \(t=2r^m\) gives
\[
h_n^2=\frac{2\pi}{m}\,2^{-(2n+2)/m}\Gamma((2n+2)/m).
\]
Thus in the normalized basis \(e_n=z^n/h_n\), \(V_m e_n=\sqrt{q_n}\,e_{n+m}\). Integration of the monomial gives the factor \(m/(n+m)\); the gamma arguments in \(h_{n+m}^2/h_n^2\) differ by two. Hence
\[
q_n=\frac{(n+1)(n+1+m/2)}{(n+m)^2}
=1-\frac{A_m}{n+m}+\frac{B_m}{(n+m)^2},
\quad A_m=\frac{3m}{2}-2,\quad B_m=(m-1)(m/2-1).
\]
The two factors \((n+1)/(n+m)\) and \((n+1+m/2)/(n+m)\) are positive, strictly increasing and below one. Their product tends to one, so \(V_m\) is bounded of norm one and is not compact: the orthogonal images of the monomials have norms tending to one.

The commutator is diagonal on this basis, with entries \(d_n=q_n\) for \(0\le n<m\) and \(d_n=q_n-q_{n-m}\) otherwise. All entries are positive. The rational expression gives the exact first difference for \(n\ge m\):
\[
d_n=\frac{A_m m}{n(n+m)}-\frac{B_m m(2n+m)}{n^2(n+m)^2}
=\frac{C_m}{n^2}+O_m(n^{-3}),\qquad C_m=\frac{m(3m-4)}2>0.
\]
The diagonal is summable, and the partial trace through \(N+m-1\) equals \(\sum_{n=N}^{N+m-1}q_n\), which tends to \(m\).

To account for decreasing rearrangement, let \(N_m(t)=\#\{n\ge0:d_n>t\}\). For \(0<\varepsilon<C_m\), discard finitely many indices so that the remaining entries are between \((C_m-\varepsilon)n^{-2}\) and \((C_m+\varepsilon)n^{-2}\). Counting indices for those two bounding sequences and then sending \(\varepsilon\downarrow0\) gives \(N_m(t)\sim\sqrt{C_m/t}\) as \(t\downarrow0\). Inverting these two bounds gives \(s_j(D_m)\sim C_mj^{-2}\). Comparison to \(\sum_j j^{-2p}\) proves membership for \(p>1/2\) and failure at and below the endpoint.

## Verification

The proof uses exact gamma identities, rational first differences, telescoping, and a counting argument, rather than a fixed finite truncation. The accompanying `checker.py` provides optional finite rational checks of monotone weights, positive first differences, partial trace identities, and the asymptotic coefficient at selected large indices. It also retains tests of background beta moments. These checks are not relied on for the universal statements.

## Relationship to prior work

The degree-based boundedness and compactness background comes from generalized Fock-space Volterra theory. The same super-Gaussian critical weights, their subnormality, and their beta-product measures are explicitly present in *Pure-top-degree rigidity for normaloid polynomial Volterra operators on super-Gaussian power-Fock space*, which treats the broader polynomial problem. These facts are not counted here as separate contributions. The contribution is the quantitative commutator law for the critical monomial: its trace, the leading constant of its full decreasing singular-value sequence, and the sharp ideal boundary. The broader polynomial classification gives the requisite weights, but does not give that commutator spectrum or its asymptotic count. The Gaussian comparator below has the same pure-symbol Schatten exponent, but uses the Gaussian weights; the coefficient here pertains to strictly super-Gaussian exponents.

## Limitations

There is no assertion about quasi-Schatten cutoffs for mixed symbols, about general radial weights, or about a simultaneous large-\(m\) and large-\(j\) limit. The comparison with available sources is not a historical-priority certificate.

## References

1. J. Bonet, T. Mengestie and M. Worku, *Dynamics of the Volterra-type integral and differentiation operators on generalized Fock spaces*, arXiv:2112.05420, Section 3. https://arxiv.org/abs/2112.05420
2. *Pure-top-degree rigidity for normaloid polynomial Volterra operators on super-Gaussian power-Fock space*, Resultary. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-pure-top-degree-rigidity-for-normaloid-polynomial-volterra-opera--25962684b171
3. *A Schatten threshold jump in self-commutators of Gaussian Fock Volterra operators*, Resultary. https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-a-schatten-threshold-jump-in-self-commutators-of-gaussian-fock-v--0f4283bb6246
4. T. Mengestie and M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces*, doi:10.1007/s40840-023-01476-4, Theorem 2.3. https://doi.org/10.1007/s40840-023-01476-4
