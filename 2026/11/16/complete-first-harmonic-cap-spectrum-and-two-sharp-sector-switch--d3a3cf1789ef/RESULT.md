# Complete first-harmonic cap spectrum and two sharp sector switches on the Cayley projective plane

## Finding

Let \(\mathbb OP^2=F_4/\mathrm{Spin}(9)\) have normalized invariant probability measure, let \(e=\operatorname{diag}(1,0,0)\) be a point represented by a primitive idempotent, and let \(\mathcal H_1\) be its real, \(26\)-dimensional first nonconstant Laplace eigenspace. For every \(0<t<1\), restrict this eigenspace to the geodesic cap \(C_t=\{P:\operatorname{tr}(e\circ P)\ge t\}\). Relative to the full-space \(L^2\) inner product, its concentration operator has precisely the following three eigenvalues, counting multiplicities:

\[
\begin{aligned}
\lambda_A(t)&=(1-t)^8(1+8t+36t^2+120t^3-1815t^4+5940t^5),&&\text{multiplicity }1,\\
\lambda_S(t)&=(1-t)^9(1+9t+45t^2+165t^3+495t^4),&&\text{multiplicity }16,\\
\lambda_V(t)&=(1-t)^{10}(1+10t+55t^2+220t^3),&&\text{multiplicity }9.
\end{aligned}
\]

The entire order is strict except at two thresholds. For \(0<t<1/4\) it is \(\lambda_S>\lambda_V>\lambda_A\); for \(1/4<t<1/3\), \(\lambda_S>\lambda_A>\lambda_V\); and for \(1/3<t<1\), \(\lambda_A>\lambda_S>\lambda_V\). At \(t=1/4\), the smallest eigenspace has dimension \(10\); at \(t=1/3\), the largest eigenspace has dimension \(17\). The sharp squared restriction condition number \(\kappa(t)=\lambda_{\max}(t)/\lambda_{\min}(t)\) satisfies
\[
\lim_{t\uparrow1}(1-t)^2\kappa(t)=15.
\]

## Assumptions and scope

The exceptional Jordan algebra \(J=H_3(\mathbb O)\) consists of octonionic Hermitian \(3\)-by-\(3\) matrices with Jordan product \(A\circ B=(AB+BA)/2\), trace pairing \(\langle A,B\rangle=\operatorname{tr}(A\circ B)\), and trace-free subspace \(J_0\) of real dimension \(26\). The points \(P\) of \(\mathbb OP^2\) are the primitive idempotents of trace one. By the standard exceptional-projective harmonic identification, \(J_0\) realizes the first positive Laplace eigenspace via \(f_A(P)=\langle A,P\rangle\). Indeed the first zonal Jacobi polynomial is \(P_1^{(7,3)}(2x-1)=12(x-1/3)\), and its \(F_4\)-translates span the irreducible \(J_0\). The cap variable \(x=\langle e,P\rangle=\cos^2 r\) takes values in \([0,1]\), with \(r\in[0,\pi/2]\) geodesic distance from \(e\). The values \(t=0\) and \(t=1\) are excluded because the associated concentration operators are trivial; limiting statements are one-sided.

The operators and eigenvalues are defined by \(\langle T_t f,g\rangle_{L^2(\mathbb OP^2)}=\int_{C_t}fg\,d\mu\), with \(\mu(\mathbb OP^2)=1\). This is a real self-adjoint operator on \(\mathcal H_1\). The condition number above is the ratio of concentration eigenvalues, equivalently the square of the singular-value condition number for restriction.

## Proof

**(1) Isotropy sectors.** The stabilizer of \(e\) is \(\mathrm{Spin}(9)\). Its orthogonal action on \(J_0\) splits into three pairwise inequivalent irreducibles: the axial line \(\mathbb R(e-I/3)\), the \(16\)-dimensional spin representation given by the two off-diagonal octonionic entries meeting the first row, and the \(9\)-dimensional vector representation given by the trace-free lower \(2\)-by-\(2\) Hermitian block. The cap is stabilizer invariant, so Schur's lemma implies the concentration form is scalar on each of these three summands.

**(2) Fixed-distance projection norms.** A primitive idempotent has \(P^2=P\), \(\operatorname{tr}P=1\), hence \(\|P-I/3\|^2=2/3\). At \(x=P_{11}\), the squared norms of its projections to the axial, spin and vector sectors, respectively, are
\[
q_A(x)=\frac32(x-\frac13)^2,\qquad q_S(x)=2x(1-x),\qquad q_V(x)=\frac12(1-x)^2.
\]
Indeed, the axial projection is \((3x-1)(e-I/3)/2\). The identity \((P^2)_{11}=P_{11}\) shows the sum of squared magnitudes of upper off-diagonal entries is \(x(1-x)\); each appears twice in the trace norm. The lower block is an octonionic Hermitian \(2\)-by-\(2\) rank-one matrix of trace \(1-x\), so the squared trace-free norm is \((1-x)^2/2\). These expressions add identically to \(2/3\), an independent normalization check. The same formulas follow from the standard primitive-idempotent local model and its rank-one block identities.

**(3) Radial measure and scalar eigenvalues.** The restricted-root multiplicities of \(\mathbb OP^2\) are \(8\) and \(7\). The invariant radial density for \(x=\cos^2r\) is \(x^3(1-x)^7/B(4,8)\), namely the \(\mathrm{Beta}(4,8)\) law. Orthogonality and irreducibility yield
\[
\lambda_j(t)=\frac{\int_t^1q_j(x)x^3(1-x)^7\,dx}{\int_0^1q_j(x)x^3(1-x)^7\,dx},\quad j\in\{A,S,V\}.
\]
Direct polynomial integration gives the three formulas in the finding. No finite-dimensional approximation is involved.

**(4) Complete order and exact degeneracies.** Factoring the exact polynomial differences gives
\[
\begin{aligned}
\lambda_A-\lambda_S&=2145t^4(1-t)^8(3t-1),\\
\lambda_A-\lambda_V&=1430t^4(1-t)^8(4t-1),\\
\lambda_S-\lambda_V&=715t^4(1-t)^9.
\end{aligned}
\]
The positive factors and the two linear factors prove all asserted strict orders and the only two interior crossings. Every eigenvalue is strictly between zero and one for \(0<t<1\) because each nonzero quadratic sector has nonzero mass both inside and outside the cap. The multiplicities then give the crossing-space dimensions.

**(5) Sharp thin-cap behavior.** As \(t\uparrow1\), the axial eigenvalue has leading term \(4290(1-t)^8\) and the vector eigenvalue has leading term \(286(1-t)^{10}\). Their ratio yields the stated exact limit \(15\).

## Verification

The cap volume is
\[
\mu(C_t)=(1-t)^8(1+8t+36t^2+120t^3).
\]
The complete-spectrum trace identity
\[
\lambda_A+16\lambda_S+9\lambda_V=26\mu(C_t)
\]
holds identically. The companion standalone standard-library checker independently integrates the three weighting polynomials using rational coefficients, verifies each closed form, each spectral-gap factorization and the trace at 17 distinct rational cap heights, and checks equality cases, order and the thin-cap constant. As every checked polynomial identity has degree at most 13, agreement at 17 distinct points proves equality of those polynomial expressions for every real cap height. The checker does not establish the geometric and representation-theoretic starting facts; those are justified analytically in the proof and the cited geometry literature.

Reproduce with `python3 check_cayley.py` in the same folder; no external packages or data files are required.

## Relationship to prior work

Parton and Piccinni describe the exceptional \(\mathrm{Spin}(9)\) geometry and its isotropy structure, while Baez describes primitive idempotents and the Albert algebra realization. Jaming and Speckbacher establish broad concentration upper bounds for finite eigenspace expansions on all compact two-point homogeneous spaces, including the Cayley plane. Those results provide the geometry and general harmonic-analysis framework. The specific three-branch first-band concentration formulas, their complete ordering, and their two sharp sector crossings are the assertions proved here; they are not stated in the inspected portions of those works. Older spherical-function tables or operator formulas could encode an equivalent specialization; historical priority is not independently certified.

## Limitations

The theorem concerns only the first nonconstant Laplace eigenspace and centered geodesic caps on the compact Cayley plane, not higher spectral bands, arbitrary measurable masks, or noncompact exceptional spaces. The nonassociativity of octonions is handled only through standard Jordan-algebra rank-one identities, not by general matrix-associativity assumptions. The originality comparison is limited to the cited accessible primary literature, available mathematical records, and prior related claims; older implicit formulas remain a potential priority risk.

## References

- M. Parton and P. Piccinni, *The Role of Spin(9) in Octonionic Geometry*, arXiv:1810.06288 (first public 2018-10-15), https://arxiv.org/abs/1810.06288 .
- P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474 (first public 2020-04-06), https://arxiv.org/abs/2004.02474 .
- J. C. Baez, *The Octonions*, arXiv:math/0105155 (first public 2001-05-17), https://arxiv.org/abs/math/0105155 .
