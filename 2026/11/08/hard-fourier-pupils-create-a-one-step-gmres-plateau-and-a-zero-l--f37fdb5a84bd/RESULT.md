# Hard Fourier pupils create a one-step GMRES plateau and a zero-leakage phase transition

## Finding

For an exactly Fourier-diagonalizable Tikhonov inverse problem, a hard binary pupil in the Schur inverse turns the Type-2 right-preconditioned saddle operator into an **idempotent**. On a natural nonzero right-hand side, ordinary exact-arithmetic GMRES then has a nonzero, explicitly calculable residual after its first step and can never reduce it further in its Krylov spaces. Flexible right preconditioning with *any sequence of masks that permanently erases the same frequencies* also faces an exact positive geometric residual floor. By contrast, giving every erased frequency any strictly positive transmission restores a two-step minimal polynomial, hence exact-arithmetic GMRES termination in at most two steps, but with a modewise condition number diverging inversely in transmission.

Specifically, for the objects in the next section, put
\[
E=\|(I-\Pi)A^*b\|_2^2,\qquad N=\|b\|_2^2.
\]
For \(b\ne0\), the optimal GMRES residual over **every** Krylov space of positive order for the hard-pupil transformed equation is
\[
\boxed{\|r_k\|_2^2=\frac{NE}{N+E}\quad(k\ge1).}
\]
This is strictly positive precisely when some omitted Fourier mode has \(a_j\widehat b_j\ne0\). In the same situation, every zero-start, mask-restricted flexible-right-preconditioning iterate \(s\) satisfies
\[
\boxed{\|Ks-(b,0)\|_2^2\ge
\sum_{j:\,\chi_j=0}\frac{|a_j|^2|\widehat b_j|^2}{1+|a_j|^2}>0.}
\]
The lower bound is the **exact minimum over the entire mask-restricted physical trial space**; it need not be attained by a particular flexible GMRES run.

For any positive leakage \(0<\varepsilon\le1\), the corresponding transformed operator has annihilating polynomial \((z-1)(z-\varepsilon)\), so exact GMRES solves its nonsingular equation in at most two steps, independently of dimension. For any omitted frequency \(j\), its associated two-dimensional block has condition number
\[
\boxed{\kappa_j(\varepsilon)=
\frac{t_j+\sqrt{t_j^2-4\varepsilon^2}}{2\varepsilon},\qquad
 t_j=1+\varepsilon^2+(1-\varepsilon)^2|a_j|^2,}
\]
and thus \(\varepsilon\kappa_j(\varepsilon)\to1+|a_j|^2\) as \(\varepsilon\downarrow0\).

## Assumptions and scope

Fix an integer \(n\ge2\), a unitary \(n\times n\) discrete Fourier matrix \(F\), a real regularization parameter \(\alpha>0\), and a (possibly complex) circulant matrix
\[
A=F^*\operatorname{diag}(a_0,\ldots,a_{n-1})F.
\]
Let \(P=A^*A+\alpha^2I\succ0\) and consider the invertible Tikhonov saddle matrix and initial right-hand side
\[
K=\begin{bmatrix}I&A\\A^*&-\alpha^2I\end{bmatrix},
\qquad c=\begin{bmatrix}b\\0\end{bmatrix},\qquad b\in\mathbb C^n\setminus\{0\}.
\]
Choose a nonempty proper binary Fourier pupil \(\chi_j\in\{0,1\}\) and its orthogonal projector
\[
\Pi=F^*\operatorname{diag}(\chi_0,\ldots,\chi_{n-1})F.
\]
Define the hard-cutoff Schur inverse \(B_0=P^{-1}\Pi\). More generally, for \(0\le\varepsilon\le1\), define
\[
B_\varepsilon=P^{-1}\bigl[\Pi+\varepsilon(I-\Pi)\bigr].
\]
For any linear Schur inverse approximation \(B\), the Type-2 *right preconditioning map* is
\[
R_B\begin{bmatrix}u\\v\end{bmatrix}
=\begin{bmatrix}u-Aw\\w\end{bmatrix},\qquad w=B(A^*u-v).
\]
When \(\varepsilon=0\), this map is singular and is **not claimed to be the inverse of an invertible preconditioner**. Standard right-preconditioned GMRES means minimizing \(\|c-KR_B y\|_2\) over \(y\in\mathcal K_k(KR_B,c)\) from zero; \(s=R_B y\) is the physical iterate. A flexible variant uses possibly varying maps \(R_{B_\ell}\) at its right-preconditioning calls. Such a variant is mask-restricted when \(\operatorname{ran}(B_\ell)\subseteq\operatorname{ran}(\Pi)\) for all calls, irrespective of the operators' other properties. All statements are for exact arithmetic and exact linear optical filters.

## Proof

**1. Factorization and the hard projector.** The usual triangular Schur factors give, by direct block multiplication,
\[
T_B:=KR_B
=\begin{bmatrix}I&0\\(I-PB)A^*&PB\end{bmatrix}.
\]
Since \(P\) commutes with \(\Pi\) and \(PB_0=\Pi\),
\[
T_0=\begin{bmatrix}I&0\\(I-\Pi)A^*&\Pi\end{bmatrix}.
\]
Its square is itself: the lower-left block of \(T_0^2\) equals \((I-\Pi)A^*+\Pi(I-\Pi)A^*=(I-\Pi)A^*\), while the lower-right block is \(\Pi^2=\Pi\). Thus \(T_0^k=T_0\) for every integer \(k\ge1\).

**2. Exact all-order GMRES plateau.** Let \(v=(I-\Pi)A^*b\). Then \(T_0c=(b,v)\) and every transformed Krylov image \(T_0\mathcal K_k(T_0,c)\) is contained in \(\operatorname{span}\{(b,v)\}\). It contains that line already for \(k=1\). Therefore the residual problem at every positive order is the one-variable least-squares minimization
\[
\min_{t\in\mathbb C}\left(\|(1-t)b\|_2^2+|t|^2\|v\|_2^2\right).
\]
Its unique minimizing scalar is \(t=N/(N+E)\) and its exact squared minimum is \(NE/(N+E)\). If \(E>0\) the Arnoldi process may terminate at a singular breakdown; “every positive order” refers to the mathematically defined Krylov spaces, not to extra executable steps after a breakdown. Since \(F\) is unitary,
\[
E=\sum_{j:\chi_j=0}|a_j|^2|\widehat b_j|^2,
\qquad \widehat b=Fb,
\]
which proves the positive-versus-zero characterization.

**3. A bound for every fixed-mask flexible sequence.** If \(\operatorname{ran}(B_\ell)\subseteq\operatorname{ran}(\Pi)\), the second block of \(R_{B_\ell}(u,v)\) always belongs to \(\operatorname{ran}(\Pi)\). Hence every zero-start iterate assembled from any number of such right-preconditioned search directions lies in
\[
\mathcal S=\{(r,x):r\in\mathbb C^n,\ x\in\operatorname{ran}(\Pi)\}.
\]
The minimization of \(\|K(r,x)-c\|_2^2\) over \(\mathcal S\) decouples exactly in Fourier coordinates. For \(\chi_j=1\), the invertible \(2\times2\) saddle block admits zero residual. For \(\chi_j=0\), \(\widehat x_j=0\) is enforced, and one minimizes
\[
|\widehat r_j-\widehat b_j|^2+|a_j|^2|\widehat r_j|^2.
\]
The minimizer is \(\widehat r_j=\widehat b_j/(1+|a_j|^2)\), with minimum \(|a_j|^2|\widehat b_j|^2/(1+|a_j|^2)\). Summing gives the asserted *attained geometric minimum* over \(\mathcal S\), hence the bound for all mask-restricted flexible updates. The bound does not depend on \(\alpha\), although \(K\) itself is invertible for every \(\alpha>0\).

**4. Exact positive-leakage transition and conditioning.** Write \(\Lambda_\varepsilon=\Pi+\varepsilon(I-\Pi)\), so that
\[
T_\varepsilon
=\begin{bmatrix}I&0\\(1-\varepsilon)(I-\Pi)A^*&\Lambda_\varepsilon\end{bmatrix}.
\]
Direct multiplication gives
\[
(T_\varepsilon-I)(T_\varepsilon-\varepsilon I)=0.
\]
For \(\varepsilon>0\) both \(T_\varepsilon\) and \(R_{B_\varepsilon}\) are invertible. The polynomial \(p(z)=(1-z)(1-z/\varepsilon)\) has \(p(0)=1\) and \(p(T_\varepsilon)=0\); hence zero-start GMRES has an exact zero residual by order two. The case \(\varepsilon=1\) has \(T_1=I\) and needs one step.

On each omitted Fourier mode, the transformed operator is unitarily represented by
\[
J_j(\varepsilon)=\begin{bmatrix}1&0\\(1-\varepsilon)\overline{a_j}&\varepsilon\end{bmatrix}.
\]
The squared singular values of this block have sum \(t_j\) and product \(\varepsilon^2\). Solving their quadratic yields the displayed condition number and asymptotic coefficient. The polynomial identity ensures exact termination, not numerical stability: a transformed solve can require intermediate coordinates of size \(1/\varepsilon\) while the corresponding physical correction is bounded.

## Verification

The standalone script `verify.py` uses SymPy to verify the block identities exactly for symbolic scalar parameters and a two-mode rational/diagonal instance. It then exercises 160 independently seeded, nontrivially masked, complex-circulant Fourier instances in dimensions 3, 4, 5, 7, and 9, checking the hard-pupil idempotence, all-order GMRES minimization, exact mask-restricted least-squares minimum, and the leakage polynomial and modewise condition numbers at three positive leakage levels (480 further cases). It returned `VERIFY_OK`. Computations corroborate but are not substituted for the quantified proof above.

For a simple explicit witness, choose a nonzero Fourier mode that the mask discards, take \(A=I\) and let \(b\) be that mode with \(\|b\|_2=1\). Then the hard-pupil GMRES residual is exactly \(1/\sqrt2\) after every positive Krylov order, and the mask-restricted flexible lower bound is also \(1/\sqrt2\), for every \(\alpha>0\). With any \(\varepsilon>0\), exact-arithmetic GMRES solves the transformed equation by the second order.

## Relationship to prior work

Drum, Onisk, Brown, and Nagy (2026) introduce the Type-2 approximate Schur inverse (their equations (10), (11), and Section 4.2), the hard optical pupil (Section 3.1.1), and the noisy/quantized optical model. Those definitions and the general FGMRES strategy are prior work. The present assertion is restricted to their deterministic exactly Fourier-diagonalizable special case, and claims the derived **idempotence, exact data-dependent nonzero GMRES plateau, all-sequence fixed-mask flexible floor, and singular-versus-positive-leakage two-step/conditioning dichotomy**; it does not claim the existence of Fourier truncation or singular-preconditioner breakdown as new ideas.

Gazzola, Noschese, Novati, and Reichel (2018/2019) already discuss singular/low-rank GMRES preconditioning and possible Krylov breakdown for ill-posed problems, but their studied preconditioners do not give this optical Type-2 hard-pupil saddle structure or its frequency-resolved residual formulas. Di Serafino and Orban (2019) address constraint-preconditioned Krylov solvers for regularized saddle matrices under different preconditioner construction. Dollar et al. (2006) study implicit-factorization preconditioners for regularized saddles; only abstract-level material was available in this comparison. These papers are not claimed to be new. Historical priority beyond the located literature is not fully resolved.

## Limitations

The theorem is exact-arithmetic, fixed-frequency-mask, and circulant; arbitrary noncirculant forward operators need not commute with a Fourier pupil. It does not assert failure of the full experimental optical preconditioner with noise, random aberrations, nonideal transformations, or ADC/DAC quantization; those effects can inject frequencies outside the fixed-mask range, invalidating the flexible-floor hypothesis. It does not assert that a particular flexible solver attains the geometric floor. Ordinary GMRES with a singular right map solves a singular transformed system and may terminate at breakdown rather than numerically continue stagnating. The two-step positive-leakage result does not imply favorable finite-precision conditioning. No claims are made for arbitrary nonzero initial guesses, adaptive projector changes, or modified iterations that add unpreconditioned corrections.

## References

1. C. Drum, L. Onisk, A. N. Brown, J. G. Nagy, “Optical Fourier Transform-Based Preconditioning for Large-Scale Inverse Problems,” arXiv:2610.17275v1, publicly posted 12 October 2026. https://arxiv.org/html/2610.17275v1
2. S. Gazzola, S. Noschese, P. Novati, L. Reichel, “Arnoldi decomposition, GMRES, and preconditioning for linear discrete ill-posed problems,” arXiv:1806.06599, 2018; Applied Numerical Mathematics 142 (2019), 102–121. https://arxiv.org/abs/1806.06599
3. D. di Serafino, D. Orban, “Constraint-Preconditioned Krylov Solvers for Regularized Saddle-Point Systems,” arXiv:1910.02552, 2019. https://arxiv.org/abs/1910.02552
4. H. S. Dollar, N. I. M. Gould, W. H. A. Schilders, A. J. Wathen, “Implicit-Factorization Preconditioning and Iterative Solvers for Regularized Saddle-Point Systems,” SIAM J. Matrix Anal. Appl. 28 (2006), 170–189. https://doi.org/10.1137/05063427X
