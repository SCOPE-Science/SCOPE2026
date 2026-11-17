# Sharp endpoint-mass law for Bell-diagonal entanglement under Kubo–Ando means

## Finding

Let \(\sigma\) be any normalized Kubo–Ando operator mean and \(\nu\) its unique probability measure representing it as a mixture of weighted harmonic means. Put \(c=\nu(\{0\})\), \(d=\nu(\{1\})\), and \(s=c+d\). On two qubits fix the four Bell rank-one projections \(P_1,P_2,P_3,P_4\). Let \(\mathcal B_{\mathrm{sep}}\) consist of all separable trace-one Bell-diagonal states. For \(A,B\in\mathcal B_{\mathrm{sep}}\) with \(A\sigma B\ne0\), normalize the positive output by its trace and write \(\mathcal N(\rho)=(\|\rho^{\Gamma}\|_1-1)/2\) for the standard entanglement negativity. Then

\[
\max_{\substack{A,B\in\mathcal B_{\mathrm{sep}}\\A\sigma B\ne0}}\mathcal N\!\left(\frac{A\sigma B}{\operatorname{Tr}(A\sigma B)}\right)=\frac{1-s}{2(1+s)}.
\]

The maximum is attained, simultaneously for every operator mean, by
\[
A=\tfrac12(P_1+P_2),\qquad B=\tfrac12(P_1+P_3).
\]

If \(s<1\), these extremal inputs produce positive negativity, and the same sharp value is the supremum for **strictly positive, interior-separable** Bell-diagonal input pairs, though it is not attained by any such interior pair. If \(s=1\), the mean is a weighted arithmetic mean and every output is separable. Thus on this commuting four-projector family the **entire sharp entanglement-amplification profile depends only on the two endpoint atoms** of the harmonic representing measure.

## Assumptions and scope

We use the computational two-qubit tensor decomposition, with Bell vectors \(\lvert\Phi^{\pm}\rangle=(\lvert00\rangle\pm\lvert11\rangle)/\sqrt2\) and \(\lvert\Psi^{\pm}\rangle=(\lvert01\rangle\pm\lvert10\rangle)/\sqrt2\), and their four respective projections \(P_i\) in any fixed order. Every Bell-diagonal density is \(X=\sum_{i=1}^{4}x_iP_i\), where \(x_i\ge0\), \(\sum_ix_i=1\). The partial transpose \(X^{\Gamma}\) has eigenvalue multiset \(\{\tfrac12-x_1,\ldots,\tfrac12-x_4\}\). Hence \(X\) is separable exactly when \(\max_i x_i\le1/2\), and its negativity is \(\max\{0,\max_i x_i-1/2\}\). The equivalence between PPT and separability here is the two-qubit Peres–Horodecki theorem.

The normalized Kubo–Ando mean is represented on commuting nonnegative arguments by the scalar operation
\[
m(a,b)=\int_{[0,1]}h_t(a,b)\,d\nu(t),\quad h_t(a,b)=\frac{ab}{(1-t)b+ta}\ (0<t<1),\quad h_0(a,b)=a,\ h_1(a,b)=b.
\]
The interior formula extends continuously to nonnegative boundary arguments by setting \(h_t(a,0)=h_t(0,b)=0\) for \(0<t<1\), and \(h_t(0,0)=0\) for every \(t\). We assume no symmetry of \(\sigma\), and allow singular inputs and all endpoint probabilities \(0\le c+d\le1\). Since the inputs commute, \(A\sigma B=\sum_i m(a_i,b_i)P_i\). If the output is zero, trace normalization is undefined and that pair is excluded. This is the only exclusion.

## Proof

**Harmonic representation and scalar bounds.** Let \(\theta=\int_0^1t\,d\nu(t)\). The harmonic–arithmetic inequality (also valid on the closed nonnegative quadrant by continuity) gives \(h_t(a,b)\le(1-t)a+tb\). Endpoint terms in the integral are exactly \(ca+db\); every remaining term is nonnegative. Therefore for all \(a,b\ge0\),
\[
ca+db\ \le\ m(a,b)\ \le\ (1-\theta)a+\theta b.
\tag{1}
\]
The same comparison holds at \(a=0\), \(b=0\), including measures concentrated entirely at the endpoints.

**A uniform output-population bound.** Fix any input coefficient arrays \(a_i,b_i\in[0,1/2]\) whose sums equal one, and an index \(i\). Write \(w_j=m(a_j,b_j)\) and suppose \(W=\sum_jw_j>0\). Set \(a=a_i\), \(b=b_i\), \(L=(1-\theta)a+\theta b\) and \(R=c(1-a)+d(1-b)\). By (1),
\[
\sum_{j\ne i}w_j\ge R,\qquad 0\le w_i\le L,
\]
so if \(R>0\) then \(w_i/W\le L/(L+R)\). When \(R=0\), the desired bound is immediate if \(c+d=0\), while if \(c+d>0\), the constraints \(a,b\le1/2\) imply \(R\ge(c+d)/2>0\); hence the latter case cannot arise. If \(s=c+d=0\), the elementary inequality \(w_i/W\le1=1/(1+s)\) suffices.

Assume \(s>0\). The function
\[
F(a,b)=\frac{(1-\theta)a+\theta b}{(1-\theta)a+\theta b+c(1-a)+d(1-b)}
\]
is nondecreasing in each variable for \(0\le a,b\le1/2\). Indeed, with \(R=c(1-a)+d(1-b)\), its derivative with respect to \(a\) has numerator \((1-\theta)R+cL\ge0\), and its derivative with respect to \(b\) has numerator \(\theta R+dL\ge0\); the common squared denominator is positive. Evaluating at the upper-right corner gives
\[
\frac{w_i}{W}\le F(a,b)\le F(1/2,1/2)=\frac{1/2}{1/2+(c+d)/2}=\frac1{1+s}.
\tag{2}
\]
Combining (2) with the Bell-diagonal negativity identity gives
\[
\mathcal N\!\left(\frac{A\sigma B}{W}\right)\le\max\{0,\tfrac1{1+s}-\tfrac12\}=\frac{1-s}{2(1+s)},
\]
because \(0\le s\le1\). This proves an upper bound for all eligible pairs, including all singular limiting configurations.

**Exact extremizer.** Take \(A=(P_1+P_2)/2\) and \(B=(P_1+P_3)/2\). They are separable because all Bell coefficients are at most \(1/2\). The boundary values of the weighted harmonic means yield
\[
A\sigma B=\tfrac12(P_1+cP_2+dP_3),\qquad W=\tfrac12(1+c+d)>0.
\]
The normalized output weights are \((1,c,d,0)/(1+s)\). Since \(c,d\le1\), the largest weight is \(1/(1+s)\), and the negativity is exactly \((1-s)/(2(1+s))\). Thus the displayed supremum is an attained maximum.

**Interior case and the arithmetic boundary.** If \(s<1\), then \(\nu((0,1))>0\). For every strictly positive \(a,b\), the integrand \(h_t(a,b)\) is strictly positive for every \(t\in(0,1)\), hence \(m(a,b)>ca+db\). If all eight input coefficients are strictly positive, for each \(i\) the inequality \(\sum_{j\ne i}m(a_j,b_j)>c(1-a_i)+d(1-b_i)\) is strict. When \(s>0\), this strictly improves (2); when \(s=0\), all output coefficients are positive and so none can equal the required bound one. Therefore no full-rank pair attains the maximum for \(s<1\). To approximate the maximum from the interior of the separable octahedron, put
\[
A_\varepsilon=(1-\varepsilon)A+\varepsilon I_4/4,\qquad B_\varepsilon=(1-\varepsilon)B+\varepsilon I_4/4,
\quad 0<\varepsilon<1.
\]
All input coefficients lie strictly between zero and \(1/2\), and continuity of finite-dimensional Kubo–Ando means and trace normalization at the nonzero extremal output gives convergence to the maximum as \(\varepsilon\downarrow0\). If \(s=1\), the measure has no interior mass, so \(m(a,b)=ca+db\) and \(A\sigma B=cA+dB\) is separable for every pair. This completes all cases.

## Verification

The proof does not rely on enumeration or extrapolation. It checks all normalized harmonic representing measures, all pairs in the compact separable Bell-diagonal octahedron for which the output is nonzero, and all four Bell components. The crucial inequality is (1), and the only maximization is a coordinatewise monotonicity bound on the exact square \([0,1/2]^2\), attained by the given commuting rank-two pair. The endpoint and interior conclusions are separately derived.

The self-contained accompanying `check.py` runs 20,012 supplementary assertions, checking random separable populations for five discrete harmonic-mixture measures, direct negative partial-transpose eigenvalues, explicit boundary equality, and one exact rational-arithmetic instance. It is diagnostic only: finite samples do not prove the universal formula. Run with Python 3 and NumPy: `python check.py`.

## Relationship to prior work

Kian, *Kubo–Ando Means and Rigidity of Quantum Positivity Cones* (arXiv:2605.26272v1, 2026), especially Theorem 3.3 and its proof, proves that only weighted arithmetic means preserve the separable cone and constructs non-arithmetic two-qubit PPT failures using local curvature. It does not provide a sharp trace-normalized entanglement negativity over the Bell-diagonal separable input region, an endpoint-mass formula, or boundary extremizers. Our scope is narrower in dimension and diagonal family but quantitatively complete for that family. No assertion is made about maximizing over **all**, possibly noncommuting separable two-qubit inputs.

Chansangiam, *Operator Means and Applications* (2012), gives the weighted-harmonic probability representation and the standard inequalities needed above; these are inputs, not new contributions. The Bell-diagonal PPT/negativity identities are standard. Verstraete et al., *Maximally entangled mixed states of two qubits* (2001), study optimization at a fixed spectrum under different transformations, not this binary operator-mean optimization. Kay, *Using Separable Bell-Diagonal States to Distribute Entanglement* (2012), concerns an entanglement-distribution protocol rather than Kubo–Ando averaging.

A targeted research-record and primary-literature comparison found no exact prior formulation of the endpoint-atom sharp maximum. This is a best-knowledge novelty assessment, not a priority certificate; an equivalent formula in older scalar-mean or quantum-information literature remains a residual risk.

## Limitations

The exact constant is only claimed for simultaneous Bell-diagonal separable trace-one inputs and trace-normalized output, not for arbitrary separable matrices, noncommuting inputs, or physical deterministic trace-preserving quantum operations. When \(A\sigma B=0\), normalization is impossible and the pair is excluded. The interior maximum is a supremum, not attained, if the mean has positive representing mass on \((0,1)\). The proof does not classify all boundary equality pairs. Mathematical self-review is not independent validation.

## References

1. M. Kian, *Kubo–Ando Means and Rigidity of Quantum Positivity Cones*, arXiv:2605.26272v1 (first public May 25, 2026), Sections 2–4, https://arxiv.org/abs/2605.26272.
2. P. Chansangiam, *Operator Means and Applications*, 2012, DOI:10.5772/46479, sections on representing probability measures and weighted harmonic means.
3. F. Verstraete, K. Audenaert, and B. De Moor, *Maximally entangled mixed states of two qubits*, arXiv:quant-ph/0011110 (2000/2001), https://arxiv.org/abs/quant-ph/0011110.
4. A. Kay, *Using Separable Bell-Diagonal States to Distribute Entanglement*, Physical Review Letters 109 (2012).
5. A. Peres, *Separability criterion for density matrices*, Physical Review Letters 77 (1996); M. Horodecki, P. Horodecki, R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Physics Letters A 223 (1996).
