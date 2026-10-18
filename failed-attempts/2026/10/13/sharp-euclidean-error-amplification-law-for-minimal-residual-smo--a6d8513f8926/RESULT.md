# Sharp Euclidean-error amplification law for minimal residual smoothing

## Finding
Consider a real SPD linear system
\[
Ax=b,
\qquad
A=A^{\mathsf T}>0,
\]
and one exact minimal residual smoothing step. Let \(y\) be the current smoothed iterate and let
\[
x=y+d,
\qquad
d\ne0,
\]
be the incoming candidate. The smoothed update is
\[
y^+=y+\eta_*d,
\]
where
\[
\eta_*
=
\operatorname*{arg\,min}_{\eta\in\mathbb R}
\|b-A(y+\eta d)\|_2.
\]

If
\[
\kappa
=
\frac{\lambda_{\max}(A)}
{\lambda_{\min}(A)},
\]
then the exact worst one-step amplification of Euclidean solution error is
\[
\boxed{
\sup
\frac{\|y^+-x_*\|_2}
{\|y-x_*\|_2}
=
\frac{\kappa^2+1}{2\kappa},
}
\]
where the supremum ranges over every dimension at least two, every SPD matrix of condition number \(\kappa\), every nonzero current error, and every nonzero incoming direction.

The bound is attained in dimension two. Therefore every
\[
\kappa>1
\]
admits a step for which minimal residual smoothing strictly decreases the residual norm while increasing the Euclidean solution error.

A sharp equality family is
\[
A=
\operatorname{diag}(1,\kappa),
\qquad
e=
\begin{pmatrix}
1\\-\kappa
\end{pmatrix},
\qquad
d=
\begin{pmatrix}
\kappa\\1
\end{pmatrix}.
\]
Then
\[
\eta_*
=
\frac{\kappa^2-1}{2\kappa},
\]
and
\[
e^+
=
\frac{\kappa^2+1}{2}
\begin{pmatrix}
1\\-1/\kappa
\end{pmatrix}.
\]
Consequently
\[
\frac{\|e^+\|_2}{\|e\|_2}
=
\frac{\kappa^2+1}{2\kappa},
\]
while
\[
\frac{\|Ae^+\|_2}{\|Ae\|_2}
=
\frac{\kappa^2+1}
{\sqrt{2(\kappa^4+1)}}
<1
\]
for every \(\kappa>1\).

At
\[
\kappa=3,
\]
the residual decreases by
\[
\frac5{\sqrt{41}},
\]
but the Euclidean solution error grows by
\[
\frac53.
\]

## Assumptions and scope
The theorem concerns exact arithmetic, one minimal residual smoothing step, the Euclidean residual norm, and a real SPD coefficient matrix.

The minimizing parameter is allowed to range over all real numbers, exactly as in the classical minimal residual smoothing definition. The incoming candidate may therefore be interpolated or extrapolated.

The result is local: it places no restriction on how the primary candidate \(x\) was generated. It therefore applies to any iterative method to which the classical smoothing step is attached.

The error is measured in the ordinary Euclidean norm. In the residual-induced norm
\[
\|e\|_{A^2}
=
\|Ae\|_2,
\]
the step is an orthogonal projection and is necessarily nonexpansive.

No finite-precision statement is made. The theorem also does not analyze quasi-minimal residual smoothing, block smoothing, or smoothing in a weighted residual norm.

## Proof
Let
\[
x_*=A^{-1}b,
\qquad
e=y-x_*.
\]
Because the incoming candidate is
\[
x=y+d,
\]
the trial smoothed error is
\[
e+\eta d.
\]
The residual minimization is therefore
\[
\min_{\eta\in\mathbb R}
\|A(e+\eta d)\|_2^2.
\]
Differentiating gives
\[
\eta_*
=
-
\frac{d^{\mathsf T}A^2e}
{d^{\mathsf T}A^2d}.
\]
Hence
\[
e^+
=
P_de,
\]
where
\[
P_d
=
I-
\frac{d\,d^{\mathsf T}A^2}
{d^{\mathsf T}A^2d}.
\]
This is an idempotent projection whose kernel is
\[
\operatorname{span}\{d\}
\]
and whose range is the Euclidean hyperplane orthogonal to
\[
A^2d.
\]

For a codimension-one oblique projection of the form
\[
P
=
I-\frac{uv^{\mathsf T}}{v^{\mathsf T}u},
\]
its nonzero extreme singular value is
\[
\|P\|_2
=
\frac{\|u\|_2\|v\|_2}
{|v^{\mathsf T}u|}.
\]
Applying this with
\[
u=d,
\qquad
v=A^2d
\]
gives
\[
\|P_d\|_2
=
\frac{
\|d\|_2\,\|A^2d\|_2
}{
d^{\mathsf T}A^2d
}.
\]

It remains to maximize this quantity over \(d\). Put
\[
B=A^2,
\]
whose extreme eigenvalues are
\[
m=\lambda_{\min}(A)^2,
\qquad
M=\lambda_{\max}(A)^2.
\]
Normalize
\[
\|d\|_2=1
\]
and define
\[
q=d^{\mathsf T}Bd,
\qquad
r=d^{\mathsf T}B^2d.
\]
For every eigenvalue
\[
\lambda\in[m,M],
\]
the secant inequality
\[
\lambda^2
\le
(m+M)\lambda-mM
\]
holds. Averaging over the spectral weights of \(d\) yields
\[
r
\le
(m+M)q-mM.
\]
Therefore
\[
\|P_d\|_2^2
=
\frac rq^2
\le
\frac{(m+M)q-mM}{q^2}.
\]
The scalar right-hand side is maximized at
\[
q_*=\frac{2mM}{m+M},
\]
with value
\[
\frac{(m+M)^2}{4mM}.
\]
Thus
\[
\|P_d\|_2
\le
\frac{m+M}{2\sqrt{mM}}
=
\frac{\kappa^2+1}{2\kappa}.
\]

Equality in the spectral secant inequality requires support only on the two endpoint eigenspaces. The maximizing weights are
\[
\frac{M}{m+M}
\]
on the \(m\)-eigenspace and
\[
\frac{m}{m+M}
\]
on the \(M\)-eigenspace. Hence dimension two already attains the global bound.

After scaling the smallest eigenvalue to one, take
\[
A=\operatorname{diag}(1,\kappa)
\]
and
\[
d=(\kappa,1)^{\mathsf T}.
\]
Then
\[
P_d
=
\frac12
\begin{pmatrix}
1&-\kappa\\
-1/\kappa&1
\end{pmatrix}.
\]
This rank-one matrix has spectral norm
\[
\frac12
\sqrt{
2+\kappa^2+\kappa^{-2}
}
=
\frac{\kappa^2+1}{2\kappa}.
\]
Its right singular direction is
\[
e=(1,-\kappa)^{\mathsf T},
\]
which gives the displayed equality family.

Finally,
\[
\|Ae^+\|_2
\le
\|Ae\|_2
\]
holds by the defining residual minimization. In the equality family the ratio is explicitly
\[
\frac{\kappa^2+1}
{\sqrt{2(\kappa^4+1)}}.
\]
For \(\kappa>1\), squaring and subtracting shows strict decrease because
\[
2(\kappa^4+1)-(\kappa^2+1)^2
=
(\kappa^2-1)^2>0.
\]

In dimension one, any nonzero \(d\) spans the whole space, so the minimizer sets the residual to zero and reaches the exact solution. This proves minimality of dimension two.

## Verification
The embedded `verify.py` uses exact rational arithmetic. It reconstructs the projection matrix for several rational condition numbers, verifies idempotence, verifies the exact singular-value formula through the rank-one Frobenius norm, and replays the equality direction.

For the concrete case
\[
\kappa=3,
\]
it verifies
\[
\eta_*=\frac43,
\qquad
\frac{\|e^+\|_2}{\|e\|_2}=\frac53,
\]
and
\[
\frac{\|Ae^+\|_2^2}{\|Ae\|_2^2}
=
\frac{25}{41}.
\]

The dimension-free upper bound is analytic. Finite checks only replay exact identities.

## Relationship to prior work
Zhou and Walker formulate minimal residual smoothing as
\[
y_k=(1-\eta_k)y_{k-1}+\eta_kx_k
\]
with \(\eta_k\) chosen over the real line to minimize the Euclidean residual norm. Their full paper proves the resulting smoothed residual norms are monotone nonincreasing and develops equivalent stable implementations. That algorithmic definition and residual monotonicity are prior work.

Weiss emphasizes a broader and important distinction: residual decrease can coexist with solution-error increase, particularly for ill-conditioned systems, and motivates error-minimizing Krylov methods. That general warning is also prior work.

The result here quantifies the local price exactly for minimal residual smoothing on SPD systems. The smoothing step is an \(A^2\)-orthogonal projection, and its Euclidean operator norm has the sharp condition-number envelope
\[
\frac{\kappa^2+1}{2\kappa}.
\]
The equality family proves that the bound is not merely a norm-equivalence estimate and that two dimensions suffice.

Targeted searches under minimal residual smoothing, Euclidean solution error, oblique projection, condition number, and error amplification did not locate the displayed sharp factor or its equality construction.

## Limitations
The incoming candidate direction is unrestricted. Additional structure imposed by a specific primary iterative method can reduce the attainable amplification.

The theorem is for SPD \(A\). General nonsymmetric matrices involve singular-vector geometry rather than a single spectral condition number.

The full text of the closest general error-minimization paper was not available through the inspected publisher route. Its abstract explicitly states that residuals can decrease while errors increase, so an older differently phrased sharp local projection bound remains a residual originality risk.

The precise day of the original 1994 print appearance of the smoothing paper was not available in the inspected records. The machine-readable source date uses the earliest day-resolved public online date verified for the cited source rather than inventing a day for the print issue.

## References
1. L. Zhou and H. F. Walker, “Residual Smoothing Techniques for Iterative Methods,” SIAM Journal on Scientific Computing 15 (1994), 297–312. DOI 10.1137/0915021.
2. R. Weiss, “Error-Minimizing Krylov Subspace Methods,” SIAM Journal on Scientific Computing 15 (1994), 511–527. DOI 10.1137/0915034.
