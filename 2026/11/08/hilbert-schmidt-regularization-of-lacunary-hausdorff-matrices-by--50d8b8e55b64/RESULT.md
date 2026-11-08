# Hilbert–Schmidt regularization of lacunary Hausdorff matrices by the unilateral shift

## Finding

Let \(H^2\) be the classical complex Hardy space of the disk and \(S=M_z\) its unilateral shift. For \(0<t<1\), put
\[
(H_tf)(z)=\frac{1}{1-(1-t)z}\, f\!\left(\frac{tz}{1-(1-t)z}\right),\qquad C_t=H_tS-SH_t.
\]
The Hilbert–Schmidt inner product has the exact *two-parameter kernel*
\[
\langle C_t,C_s\rangle_{\mathcal S_2}
=K(t,s):=\frac{\min(t,s)\,[1-\max(t,s)]}{\max(t,s)\,(t+s-ts)}
\quad(0<t,s<1).
\]
Consequently \(\|C_t\|_{\mathcal S_2}^2=(1-t)/(t(2-t))\).

Fix \(\rho=1/16\) and \(t_j=\rho^j\) for integers \(j\ge1\). The sequence \((\sqrt{t_j}\,C_{t_j})_{j\ge1}\) is a Riesz sequence in the Hilbert space \(\mathcal S_2(H^2)\), with the following explicit (not claimed optimal) universal bounds. For every finite complex scalar sequence \((a_j)\),
\[
\left(\frac{15}{31}-\frac{2}{63}\right)\sum_j|a_j|^2
\le\left\|\sum_j a_j\sqrt{t_j}C_{t_j}\right\|_{\mathcal S_2}^2
\le\left(\frac12+\frac{2}{63}\right)\sum_j|a_j|^2.
\]
Thus the series of commutators converges in \(\mathcal S_2\) **if and only if** \((a_j)\in\ell^2\).

For every nonnegative \(a\in\ell^2\), define the finite positive atomic measure
\[
\mu=\sum_{j\ge1}a_j\sqrt{t_j}\,\delta_{t_j}.
\]
The corresponding Hausdorff operator \(H_\mu=\int H_t\,d\mu(t)\) maps each polynomial into \(H^2\). Its formal shift commutator on polynomials admits the unique Hilbert–Schmidt extension \(C_\mu=\sum_j a_j\sqrt{t_j}C_{t_j}\), with the exact convergent quadratic-form identity
\[
\|C_\mu\|_{\mathcal S_2}^2
=\sum_{i,j\ge1}a_i a_j\sqrt{t_it_j}\,K(t_i,t_j).
\]
In particular, taking \(a_j=1/j\) gives a **densely defined, unbounded** positive Hausdorff matrix on \(H^2\) whose formal commutator with \(S\) nevertheless extends to a Hilbert–Schmidt operator. The distinction is genuinely between boundedness of the parent operator and operator-ideal regularity of its commutator.

## Assumptions and scope

All Hilbert spaces and coefficients in the Riesz statement are complex. The \(H^2\) norm is \(\|\sum_{n\ge0}c_nz^n\|^2=\sum_{n\ge0}|c_n|^2\). The Hilbert–Schmidt norm is the sum of squared \(H^2\)-column norms against the monomial basis. The linear map \(H_\mu\) is initially defined on the polynomials, by its analytic integral representation; boundedness on the entire Hardy space is *not* presumed. In the application, \(a_j\ge0\), \(\sum a_j^2<\infty\), and \(0<t_j<1\).

## Proof

**1. Exact commutator symbol.** Put \(q_t=1-t\), \(\phi_t(z)=tz/(1-q_tz)\), and \(u_t(z)=(1-q_tz)^{-1}\). The operator \(H_t=u_tC_{\phi_t}\) is bounded on \(H^2\) for fixed \(t>0\). Directly,
\[
C_tf(z)=\psi_t(z)f(\phi_t(z)),\qquad
\psi_t(z)=u_t(z)(\phi_t(z)-z)
=-\frac{q_t z(1-z)}{(1-q_tz)^2}.
\]
Since \(C_tz^n=\psi_t\phi_t^n\), Parseval on the unit circle followed by the nonnegative geometric series gives
\[
\langle C_t,C_s\rangle_{\mathcal S_2}
=\int_{|z|=1}\frac{\psi_t(z)\overline{\psi_s(z)}}{1-\phi_t(z)\overline{\phi_s(z)}}\,\frac{|dz|}{2\pi}.
\]
This identity first follows on truncated monomial sums, then by dominated convergence: near the only boundary contact \(z=1\), the numerator vanishes to second order and cancels the denominator singularity. For \(t=s\), the limiting quotient is bounded there; for \(t\ne s\), the same holds. In particular every \(C_t\) is Hilbert–Schmidt.

Using \(\bar z=z^{-1}\), the circle integrand reduces to
\[
\frac{q_tq_s z(z-1)}{(1-q_tz)(z-q_s)(q_tz-q_s)}.
\]
After including the \(dz/z\) factor, the residues are those of
\[
R(z)=\frac{q_tq_s(z-1)}{(1-q_tz)(z-q_s)(q_tz-q_s)}.
\]
There is always a pole at \(z=q_s\), with residue
\( -q_t(q_s-1)/[(q_t-1)(q_tq_s-1)]\).
If \(q_s<q_t\), the additional pole at \(z=q_s/q_t\) lies inside the circle, with residue
\( -(q_t-q_s)/[(q_t-1)(q_s-1)]\).
Their sum, or just the first residue when \(q_s>q_t\), simplifies to the symmetric formula for \(K(t,s)\) displayed above. The diagonal case follows by a direct cancellation at \(q_s=q_t\), giving \(K(t,t)=(1-t)/(t(2-t))\).

**2. Riesz Gram bounds.** Let \(G_{ij}=\sqrt{t_it_j}K(t_i,t_j)\). On the diagonal,
\[
\frac{15}{31}\le G_{ii}=\frac{1-t_i}{2-t_i}<\frac12.
\]
For \(i\ne j\), writing \(u=\min(t_i,t_j)\) and \(v=\max(t_i,t_j)\),
\[
0<G_{ij}=\sqrt{uv}\,\frac{u(1-v)}{v(u+v-uv)}
\le\left(\frac uv\right)^{3/2}
=\left(\frac1{64}\right)^{|i-j|}.
\]
The total off-diagonal absolute row sum is at most \(2\sum_{k\ge1}64^{-k}=2/63\). The quadratic form estimates follow by the Schur test (or diagonal dominance of the Hermitian Gram matrix). Since the lower constant is positive, the synthesis map extends to a bounded-below linear map from \(\ell^2\) into \(\mathcal S_2\), and the partial sums are Cauchy exactly for square-summable coefficients.

**3. Polynomial domain of the Hausdorff operator.** For each fixed integer \(n\ge0\),
\[
H_tz^n=\frac{t^nz^n}{(1-(1-t)z)^{n+1}},\qquad
\langle H_tz^n,H_sz^n\rangle
=(ts)^n\sum_{k\ge0}\binom{n+k}{n}^{\!2}
(1-t)^k(1-s)^k.
\]
The elementary bound
\(\sum_{k\ge0}\binom{n+k}{n}^{2}r^k\le B_n(1-r)^{-(2n+1)}\), for \(0\le r<1\), implies
\[
\left|\left\langle \sqrt{t_i}H_{t_i}z^n,
\sqrt{t_j}H_{t_j}z^n\right\rangle\right|
\le B_n\rho^{(n+1/2)|i-j|}.
\]
Here \(B_n\) is finite and depends only on \(n\). Schur's row-sum bound therefore shows that \(\sum_j a_j\sqrt{t_j}H_{t_j}z^n\) converges in \(H^2\) for every \(a\in\ell^2\). The measure \(\mu\) is finite by Cauchy–Schwarz, and its analytic integral representation agrees with this series locally uniformly. Thus \(H_\mu\) has the polynomials in its domain. The bounded shift maps polynomials to polynomials, so the formal commutator there equals the strong polynomial restriction of the Hilbert–Schmidt sum obtained in Step 2. Density gives uniqueness of the extension and the quadratic norm formula.

**4. The parent can be unbounded.** Set \(a_j=1/j\), so \(\mu\) is finite and its commutator is Hilbert–Schmidt. We prove directly that \(H_\mu\) cannot be bounded. For a finite positive truncation \(\mu_J=\sum_{j\le J}a_j\sqrt{t_j}\,\delta_{t_j}\) and \(0<\alpha<1/2\), the Hardy function \(f_\alpha(z)=(1-z)^{-\alpha}\) obeys
\[
H_{\mu_J}f_\alpha=f_\alpha\,A_{J,\alpha},
\qquad A_{J,\alpha}(z)=\sum_{j\le J}a_j\sqrt{t_j}
(1-(1-t_j)z)^{\alpha-1}.
\]
The normalized boundary densities \(|f_\alpha|^2/\|f_\alpha\|_{H^2}^2\) concentrate at \(z=1\) as \(\alpha\uparrow1/2\). Because \(A_{J,\alpha}\) is continuous on the closed disk for fixed \(J\),
\[
\lim_{\alpha\uparrow1/2}
\frac{\|H_{\mu_J}f_\alpha\|_{H^2}}{\|f_\alpha\|_{H^2}}
=A_{J,1/2}(1)=\sum_{j=1}^J a_j.
\]
All Hausdorff matrix coefficients are nonnegative for positive \(\mu\), as are the Taylor coefficients of \(f_\alpha\). On polynomial truncations of \(f_\alpha\), the coefficientwise inequality \(H_\mu\ge H_{\mu_J}\) therefore gives a norm inequality. If \(H_\mu\) possessed a bounded extension of norm \(L\), passage to the polynomial limit would imply \(L\ge\sum_{j\le J}1/j\) for every \(J\), a contradiction.

## Verification

Run `python3 verify.py` with the Python standard library. It checks the exact finite Hausdorff matrix/commutator coefficient identity at rational parameters, the exact-rational square of the Gram-kernel bounds at fifteen lacunary scales, rational Riesz constants, and finite matrix pairing comparisons. Successful output is `ATOMIC_HAUSDORFF_COMMUTATOR_OK 871 exact assertions; analytic infinite proof separate`. The code does **not** certify the limit of the Hilbert–Schmidt series, the analytic residue calculation, or the unboundedness argument; these are established above.

## Relationship to prior work

Galanopoulos and Siskakis (2001) establish the foundational Hausdorff matrix/composition representation, and Galanopoulos and Papadimitrakis (2006) develop boundedness theory on analytic function spaces. Galanopoulos, Mahillo, Oliva-Maza and Siskakis (2026) study spectra on BMOA and the Bloch space and recall the Hardy-space boundedness criterion \(\int t^{-1/2}\,d\mu(t)<\infty\) for positive measures. That criterion already establishes the parent-operator obstruction; the assertion of originality here concerns the exact *two-parameter commutator Gram kernel*, its lacunary Riesz bounds, and the simultaneous existence of a polynomial-defined unbounded Hausdorff operator and a Hilbert–Schmidt shift commutator. General weighted-composition compactness and cross-adjoint commutator work does not itself state this synthesis phenomenon. Literature noncoverage is not a proof of priority.

## Limitations

The Riesz constants are convenient bounds, not optimized. The infinite sum is characterized as a Hilbert–Schmidt synthesis series; no claim is made that nonsquare-summable coefficients cannot admit some other regularized summation procedure. No trace-class threshold or full singular-value asymptotic is claimed. The conclusion about an unbounded parent uses positive coefficients and the polynomial domain; this is not a bounded-operator commutator identity on all of \(H^2\). A previously unknown general weighted-composition commutator Gram theorem might cover part or all of the finding.

## References

1. P. Galanopoulos, A. Mahillo, J. Oliva-Maza and A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, arXiv:2610.22554v1 (first submitted 15 October 2026), https://arxiv.org/html/2610.22554v1.
2. P. Galanopoulos and A. G. Siskakis, *Hausdorff matrices and composition operators*, Illinois Journal of Mathematics 45 (2001), 757–773, https://doi.org/10.1215/ijm/1258138149.
3. P. Galanopoulos and M. Papadimitrakis, *Hausdorff and quasi-Hausdorff matrices on spaces of analytic functions*, Canadian Journal of Mathematics 58 (2006), 548–579.
4. S. Jung, Y. Kim and E. Ko, *Commutator of weighted composition operators*, International Journal of Mathematics 25 (2014), 1450053. Related cross-adjoint commutator literature; not used as a theorem in the proof.
