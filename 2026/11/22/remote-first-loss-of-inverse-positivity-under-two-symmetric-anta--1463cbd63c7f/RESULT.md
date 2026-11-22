# Remote-first loss of inverse positivity under two symmetric antagonistic shortcuts on a path

## Finding
For every integer \(n\ge4\), let \(P_n\) be the unit-weight path on vertices \(1,\dots,n\), let \(L_n\) be its combinatorial Laplacian, and define the symmetric matrix
\[
A_n(t)=I+L_n-t\left[(e_1-e_{n-1})(e_1-e_{n-1})^{\mathsf T}+(e_2-e_n)(e_2-e_n)^{\mathsf T}\right],\qquad t\ge0.
\]
This models two equal antagonistic (negative-conductance) shortcuts. The endpoints \(1,n\) are not directly joined by either shortcut.

Put \(m=n-4\), define \(D_{-1}=0\), \(D_0=1\), and \(D_j=3D_{j-1}-D_{j-2}\) for \(j\ge1\), and set
\[
b=3-\frac{D_{m-1}}{D_m},\qquad d=\frac1{D_m},\qquad
\tau_n=\frac{d}{b+\sqrt{b^2-d(d+2)}},\qquad
\sigma_n=\frac{2(b+d)-1}{b+d+4}.
\]
Then \(0<\tau_n<\sigma_n<1\), and the following assertions hold **for every real \(t\ge0\)**:

1. \(A_n(t)\) is positive definite exactly when \(t<\sigma_n\).
2. In this entire positive-definite range, \(A_n(t)^{-1}\) is entrywise nonnegative exactly when \(t\le\tau_n\). It is entrywise strictly positive for \(0\le t<\tau_n\).
3. At \(t=\tau_n\), the **only zero entries** of the inverse are the two symmetric entries \((1,n)\) and \((n,1)\). For every \(\tau_n<t<\sigma_n\), those two entries are strictly negative.
4. With \(r=(3-\sqrt5)/2\) and \(\lambda=(3+\sqrt5)/2\), the two stability scales separate exponentially:
\[
\tau_n\sim\frac{\sqrt5}{2}r^{n-2},\qquad
\sigma_n\longrightarrow\frac{2\lambda-1}{\lambda+4}=0.6400795137\ldots .
\]
For example, \(n=4\) gives \(\tau_4=(3-\sqrt6)/3\) whereas \(\sigma_4=7/8\).

## Assumptions and scope
The path edges have conductance one, the positive screening shift is fixed at one, the two antagonistic shortcut strengths coincide, and \(n\ge4\). Entrywise inverse positivity is meant literally, for every matrix entry, and is asserted only while \(A_n(t)\) is positive definite. The result is **not** a statement about arbitrary edge weights, unequal shortcut strengths, or continuation through singularity.

## Proof
**Exact four-terminal reduction.** Retain vertices \(1,2,n-1,n\) in that order, and eliminate the \(m=n-4\) interior vertices (none when \(n=4\)). The interior block of \(A_n(t)\) is the fixed symmetric tridiagonal matrix \(H_m\) with diagonal three and neighboring entries minus one. It is a positive-definite irreducible \(M\)-matrix. Its determinant is \(D_m\), its endpoint inverse diagonal is \(D_{m-1}/D_m\), and its endpoint-to-endpoint inverse entry is \(1/D_m\); use the stated conventions when \(m=0\). Consequently the Schur complement is exactly
\[
S(t)=\begin{pmatrix}
2-t&-1&t&0\\
-1&b-t&-d&t\\
t&-d&b-t&-1\\
0&t&-1&2-t
\end{pmatrix}.
\]
The recurrence gives \(5/2<b\le3\) and \(0<d\le1\). Indeed, the ratios \(D_{j-1}/D_j\) increase from zero toward \(r=(3-\sqrt5)/2<1/2\).

**Exact positive-definiteness boundary.** Reflection into even and odd subspaces decomposes \(S(t)\) into the two symmetric \(2\times2\) matrices
\[
S_{\mathrm e}=\begin{pmatrix}2-t&t-1\\t-1&b-d-t\end{pmatrix},\qquad
S_{\mathrm o}=\begin{pmatrix}2-t&-1-t\\-1-t&b+d-t\end{pmatrix}.
\]
Their determinants simplify to
\[
\det S_{\mathrm e}=2(b-d)-1-(b-d)t,
\qquad
\det S_{\mathrm o}=2(b+d)-1-(b+d+4)t.
\]
The even block first becomes singular beyond \(t=1\), whereas the odd block first becomes singular at \(t=\sigma_n<1\). The positive leading diagonal \(2-t\) and the positive interior block complete the Schur-complement proof that \(A_n(t)\succ0\) if and only if \(0\le t<\sigma_n\). In particular, \(\sigma_n>1/2\).

**Every inverse entry, not only a witness.** Throughout \(t<\sigma_n\), the determinant of \(S(t)\) is positive. Its off-diagonal inverse entries have the signs of the corresponding adjugate numerators. Apart from reflection symmetry, these four numerators are
\[
\begin{aligned}
N_{12}&=2b-1-(2d+2+b)t+(d+2)t^2,\\
N_{13}&=2d-(2b+d+1)t+(b+2)t^2,\\
N_{23}&=(2-t)\bigl(2d-(d+2)t\bigr),\\
N_{14}&=d-2bt+(d+2)t^2.
\end{aligned}
\]
Here \(N_{24}=N_{13}\) and \(N_{34}=N_{12}\). The smaller zero of \(N_{14}\) is \(\tau_n\). Since
\[
N_{14}(d/4)/d=1-b/2+d(d+2)/16<0,
\]
it follows that \(0<\tau_n<d/4\le1/4<\sigma_n\). For \(0\le t\le d/4\), the inequalities \(5/2<b\le3\) and \(0<d\le1\) give
\[
N_{12}\ge 4-7/4>0,\quad
N_{13}\ge (b+2)t^2\quad(\text{strict at }t=0\text{ by its constant term}),\quad
N_{23}>0.
\]
Therefore \(S(t)^{-1}\) has positive diagonal and strictly positive off-diagonal entries except its \((1,4)\) and \((4,1)\) entries, which decrease to zero at \(t=\tau_n\). The larger zero of \(N_{14}\), by Vieta's formula, exceeds \(4/(d+2)\ge4/3>\sigma_n\), so this entry is strictly negative for every \(\tau_n<t<\sigma_n\).

To transfer positivity back to all vertices, write the original matrix in terminal/interior blocks with interior block \(H_m\) and terminal/interior block \(B\le0\). The full block inverse is
\[
\begin{pmatrix}
S^{-1}&-S^{-1}BH_m^{-1}\\
-H_m^{-1}B^{\mathsf T}S^{-1}&H_m^{-1}+H_m^{-1}B^{\mathsf T}S^{-1}BH_m^{-1}
\end{pmatrix}.
\]
Both \(H_m^{-1}\) and \(-B\) are nonnegative; \(H_m^{-1}\) is strictly positive whenever \(m>0\). All terminal-to-interior inverse entries are strictly positive because the second and third terminal columns of \(S^{-1}\) are strictly positive and connect to the ends of the interior chain. The interior-to-interior entries are strictly positive as well. Thus the first zeros are exactly the unperturbed, opposite-endpoint pair, and negativity of that pair immediately gives the converse.

**Asymptotics.** For \(\lambda=(3+\sqrt5)/2\) and \(r=\lambda^{-1}\), the continuants satisfy \(D_m=(\lambda^{m+1}-r^{m+1})/\sqrt5\). Hence \(d\sim\sqrt5\,r^{n-3}\), \(b\to\lambda\), and rationalization of the smaller root gives \(\tau_n\sim d/(2b)\sim(\sqrt5/2)r^{n-2}\); the formula for \(\sigma_n\) gives the stated positive limit.

## Verification
The standalone file `check.py` verifies all four symbolic cofactor identities; for each \(n=4,\ldots,12\), it checks the exact Schur complement, exact rational inverse positivity below the threshold, a strictly negative endpoint inverse entry above it but inside the positive-definite regime, and threshold inequalities. Execution of the embedded program produced 1,377 passed exact assertions. These finite tests verify algebraic specializations but do not replace the all-\(n\), all-real-parameter proof above.

## Relationship to prior work
Haynes, Trummer and Kennedy (2007) investigate persistence of nonnegative inverses for perturbations of tridiagonal \(M\)-matrices, including rank-one cases. Huang, Haynes and Huang (2012) give broad necessary-and-sufficient recursive tests for simultaneous nonnegative off-band perturbations of tridiagonal \(M\)-matrices. These results establish the pertinent framework but do not state the present *screened-Laplacian, two-equal-antichord, varying-diagonal* closed threshold, identify the first failing **unperturbed endpoint pair**, or quantify its exponential separation from definiteness. The general tests are closely related and could offer alternate ways to derive the specialized result; no general claim of a novel inverse-positivity framework is made. Zelazo and Bürger (2014) investigate signed-Laplacian definiteness and effective resistance, a different outcome from inverse entrywise nonnegativity.

## Limitations
The analytical classification is confined to the specified one-parameter path family. It does not optimize antagonistic edges, claim generality for all signed graphs, or control the signs once definiteness has failed. Earlier general inverse-positivity criteria might admit an unpublished or unindexed equivalent specialization; originality is accordingly a best-knowledge conclusion from the inspected primary material, not a priority certificate. Independent mathematical validation has not been carried out.

## References
- R. D. Haynes, M. R. Trummer, S. C. Kennedy, *Persistently positive inverses of perturbed M-matrices*, Linear Algebra and its Applications 422 (2007), 742–754. DOI: 10.1016/j.laa.2006.12.006. Public online February 1, 2007. https://www.math.mun.ca/~rhaynes/inversepos07.pdf
- J. Huang, R. D. Haynes, T.-Z. Huang, *Monotonicity of Perturbed Tridiagonal M-Matrices*, SIAM Journal on Matrix Analysis and Applications 33 (2012), 681–700. DOI: 10.1137/100812483. Public online June 28, 2012. https://www.math.mun.ca/rhaynes/haynesjiehuang.pdf
- D. Zelazo, M. Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance* (2014), arXiv:1408.2187v1, August 10, 2014. https://arxiv.org/abs/1408.2187
