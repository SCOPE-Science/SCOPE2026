# Best-conditioned quasi-Hermitian metrics reduce to diagonal Gram scaling
## Finding
Let \(H\in\mathbb C^{n\times n}\) be diagonalizable with simple real eigenvalues, and choose Euclidean-unit right eigenvectors \(u_1,\ldots,u_n\). Put \(V=[u_1\ \cdots\ u_n]\) and \(G=V^\dagger V\). Every positive metric \(\eta\) satisfying
\[
H^\dagger\eta=\eta H
\]
has the form
\[
\eta=V^{-\dagger}DV^{-1}
\]
for a positive diagonal matrix \(D\), and conversely every such \(D\) gives an admissible metric. Moreover,
\[
\kappa_2(\eta)=\kappa_2\!\left(D^{-1/2}GD^{-1/2}\right).
\]
Thus the best-conditioned physical metric is exactly the optimal positive diagonal congruence scaling of the eigenvector Gram matrix.

For every pair \(i\ne j\), writing \(c_{ij}=|u_i^\dagger u_j|\), every admissible metric obeys the sharp pairwise obstruction
\[
\kappa_2(\eta)\ge \frac{1+c_{ij}}{1-c_{ij}},
\]
so in particular
\[
\kappa_2(\eta)\ge \max_{i<j}\frac{1+c_{ij}}{1-c_{ij}}.
\]
In dimension two this lower bound is the exact optimum. If \(c=|u_1^\dagger u_2|\), then
\[
\min_{\eta\succ0,\ H^\dagger\eta=\eta H}\kappa_2(\eta)
=\frac{1+c}{1-c}
=\kappa_2(V)^2,
\]
and the minimizing metric is unique up to a positive scalar multiple:
\[
\eta_*=(VV^\dagger)^{-1}.
\]
Equivalently, if \(\theta=\arccos c\) is the acute angle between the two eigendirections, the optimum is \(\cot^2(\theta/2)\), hence it diverges as \(4/\theta^2\) when the eigendirections coalesce.

## Assumptions and scope
The theorem is finite-dimensional. The spectrum of \(H\) is assumed simple and real, and \(H\) is assumed diagonalizable. The right eigenvectors are normalized in the reference Euclidean norm. The condition number is the spectral condition number \(\kappa_2(\eta)=\lambda_{\max}(\eta)/\lambda_{\min}(\eta)\). No claim is made for defective matrices, repeated eigenvalues, indefinite pseudo-metrics, or infinite-dimensional operators with unbounded metrics.

## Proof
Write \(H=V\Lambda V^{-1}\), where \(\Lambda\) is real diagonal with distinct entries. From \(H^\dagger\eta=\eta H\), multiplication on the left by \(V^\dagger\) and on the right by \(V\) gives
\[
\Lambda\,(V^\dagger\eta V)=(V^\dagger\eta V)\Lambda.
\]
Simplicity of the spectrum forces \(D:=V^\dagger\eta V\) to be diagonal. Positivity of \(\eta\) makes \(D\) positive, and therefore \(\eta=V^{-\dagger}DV^{-1}\). The converse follows by direct substitution.

Because
\[
\eta^{-1}=VD^{-1}V^\dagger,
\]
its eigenvalues equal those of the Gram matrix of \(VD^{-1/2}\), namely \(D^{-1/2}GD^{-1/2}\). Inverting a positive matrix does not change its spectral condition number, proving the diagonal-scaling identity.

For the pairwise bound, distinct real eigenvalues imply \(u_i^\dagger\eta u_j=0\). Change the phase of \(u_j\) so that \(u_i^\dagger u_j=c_{ij}\ge0\). Let \(m=\lambda_{\min}(\eta)\), \(M=\lambda_{\max}(\eta)\), and
\[
q=u_i^\dagger\eta u_i+u_j^\dagger\eta u_j.
\]
The cross terms vanish, so both \(u_i+u_j\) and \(u_i-u_j\) have squared \(\eta\)-norm \(q\). Their squared Euclidean norms are \(2(1+c_{ij})\) and \(2(1-c_{ij})\). Therefore
\[
q\ge 2m(1+c_{ij}),\qquad q\le 2M(1-c_{ij}),
\]
which gives \(M/m\ge(1+c_{ij})/(1-c_{ij})\).

When \(n=2\), after the same phase choice the normalized Gram matrix is
\[
G=\begin{pmatrix}1&c\\c&1\end{pmatrix}.
\]
For \(D=\operatorname{diag}(d_1,d_2)\), the scaled Gram matrix has diagonal entries \(d_1^{-1},d_2^{-1}\) and determinant \((1-c^2)/(d_1d_2)\). At fixed determinant its condition number is minimized by minimizing the trace, and the arithmetic-geometric mean inequality gives equality exactly when \(d_1=d_2\). Hence \(D\) is scalar, giving \(\eta_*=(VV^\dagger)^{-1}\), unique up to scale, with eigenvalue ratio \((1+c)/(1-c)\). The half-angle identity gives the final form.

## Verification
The accompanying `artifacts/verify.py` uses only the Python standard library. It reconstructs admissible metrics from random eigenbases in dimensions \(3,4,6\), checks the intertwining equation, checks the equality between the metric condition number and the diagonally scaled Gram condition number, and checks the pairwise lower bound. It also checks six two-dimensional overlaps, including \(c=0.99\), against the exact optimum and a broad one-parameter family of nonoptimal admissible metrics. These finite computations support the algebra but are not used as a proof of the quantified theorem.

## Relationship to prior work
Mostafazadeh and Özçelik gave the complete two-level family of quasi-Hermitian metric operators and made its nonuniqueness explicit; that metric parameterization is prior. Mostafazadeh later gave a general construction and symmetry interpretation for metrics of quasi-Hermitian Hamiltonians. Krejčiřík, Lotoreichik and Znojil introduced a different optimization principle, minimizing Hilbert-Schmidt distance to the reference metric, and explicitly noted that other norm-based optimization problems could be considered. Siegl and Krejčiřík related singular metric behavior to failure of the Riesz-basis property for the imaginary cubic oscillator.

The present result does not claim those constructions or qualitative singularity phenomena as new. It isolates the scale-invariant spectral-condition objective, reduces its full finite-dimensional optimization exactly to positive diagonal scaling of the eigenvector Gram matrix, and derives a universal sharp pairwise obstruction. In two dimensions it solves that objective in closed form. The closest inspected optimization paper uses Hilbert-Schmidt distance rather than spectral condition number and does not state this diagonal-scaling identity, pairwise lower bound, or the exact \((1+c)/(1-c)\) optimum.

## Limitations
The result is elementary once the metric family is expressed in an eigenbasis, and older Riesz-basis or matrix-scaling literature may contain equivalent inequalities in different language. The literature search found no claim-dominating statement, but absence from the inspected sources is not a proof of historical novelty. In dimension two, the ray selected by the condition-number objective can coincide with a metric selected by another normalization-dependent objective; the new claim is the condition-number theorem and its sharp value, not exclusive ownership of that metric ray. No infinite-dimensional extension is asserted.

## References
1. A. Mostafazadeh and S. Özçelik, “Explicit Realization of Pseudo-Hermitian and Quasi-Hermitian Quantum Mechanics for Two-Level Systems,” arXiv:quant-ph/0607120, first public 2006-07-18.
2. A. Mostafazadeh, “Metric Operators for Quasi-Hermitian Hamiltonians and Symmetries of Equivalent Hermitian Hamiltonians,” arXiv:0707.3075, DOI:10.1088/1751-8113/41/24/244017.
3. P. Siegl and D. Krejčiřík, “On the metric operator for the imaginary cubic oscillator,” arXiv:1208.1866, DOI:10.1103/PhysRevD.86.121702.
4. D. Krejčiřík, V. Lotoreichik and M. Znojil, “The minimally anisotropic metric operator in quasi-Hermitian quantum mechanics,” arXiv:1804.06766, DOI:10.1098/rspa.2018.0264.
