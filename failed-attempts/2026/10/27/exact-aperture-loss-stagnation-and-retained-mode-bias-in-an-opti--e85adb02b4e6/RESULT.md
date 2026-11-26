# Exact aperture-loss stagnation and retained-mode bias in an optical Type-II Tikhonov preconditioner

## Finding
For a symmetric circulant forward operator and a fixed exact binary Fourier pupil, a Type-II optical Schur-inverse preconditioner can turn an *invertible* Tikhonov saddle system into an idempotent, singular right-preconditioned matrix. With nonzero data and a zero initial guess, every un-restarted fixed-preconditioner GMRES iterate beyond the first has exactly the same minimum residual. If an omitted frequency contributes a nonzero transformed residual, even retained reconstruction frequencies are attenuated by a common scalar smaller than one. All formulas are exact for any finite dimension and any strictly positive regularization parameter.

Write \(E=\|b\|_2^2>0\), \(R^2=\|A(I-\Pi)b\|_2^2\), and \(t=E/(E+R^2)\). The sharp first-step and eventual GMRES squared residual is
\[
\|r_G\|_2^2=\frac{E R^2}{E+R^2},
\qquad x_G=t\Pi x_*,\qquad x_*=(A^2+\alpha^2I)^{-1}Ab.
\]
The exact squared reconstruction error is
\[
\|x_G-x_*\|_2^2=(1-t)^2\|\Pi x_*\|_2^2+\|(I-\Pi)x_*\|_2^2.
\]
In contrast, minimization over the **whole range** of the right-preconditioned matrix permits the smaller floor
\[
 d_{\mathrm{range}}^2=\sum_{j:p_j=0}\frac{a_j^2}{1+a_j^2}|\widehat b_j|^2.
\]
Thus missing frequencies can cause both an unavoidable range restriction and an additional Krylov subspace restriction, while producing a global bias even in transmitted modes.

## Assumptions and scope
Let \(n\ge2\), \(A\in\mathbb R^{n\times n}\) be real symmetric circulant, and let \(F\) denote the *unitarily normalized* discrete Fourier transform, so \(A=F^*\operatorname{diag}(a_0,\ldots,a_{n-1})F\) with real eigenvalues. A binary aperture \(p_j\in\{0,1\}\) is conjugate symmetric, ensuring that \(\Pi=F^*\operatorname{diag}(p_j)F\) is a real orthogonal projection that commutes with \(A\). Put \(\alpha>0\) and \(S=A^2+\alpha^2I\), which is positive definite irrespective of whether \(A\) is singular. Consider the Tikhonov saddle-point system
\[
K\binom{r}{x}=\binom b0,\qquad K=\begin{pmatrix}I&A\\A&-\alpha^2I\end{pmatrix},\qquad b\ne0.
\]
The minus sign in its lower-right block follows from the normal equations \(A^T(b-Ax)=\alpha^2x\). Let the exact *fixed* hard-aperture inverse of the Type-II central Schur factor be \(W=\Pi S^{-1}\). Define the (possibly singular) inverse-application operator
\[
\widetilde M^{-1}=\begin{pmatrix}I&-A\\0&I\end{pmatrix}
\begin{pmatrix}I&0\\0&-W\end{pmatrix}
\begin{pmatrix}I&0\\-A&I\end{pmatrix}.
\]
This is a precise, noiseless, unquantized idealization of frequency truncation in the source's Type-II optical Fourier preconditioner; it is **not** a claim about arbitrary noisy optical transforms or variable-preconditioner FGMRES. GMRES uses \(B=K\widetilde M^{-1}\), starts from zero, and minimizes Euclidean residuals over its ordinary unrestarted Krylov spaces. All statements are in exact arithmetic.

## Proof
Because \(A\), \(S\) and \(\Pi\) commute, \(WS=SW=\Pi\). Direct block multiplication gives
\[
\widetilde M^{-1}=\begin{pmatrix}I-AWA&AW\\WA&-W\end{pmatrix},
\qquad B=K\widetilde M^{-1}=\begin{pmatrix}I&0\\A(I-\Pi)&\Pi\end{pmatrix}.
\]
The two projections \(\Pi\) and \(I-\Pi\) are complementary and commute with \(A\). Thus
\[
B^2=\begin{pmatrix}I&0\\A(I-\Pi)+\Pi A(I-\Pi)&\Pi^2\end{pmatrix}=B.
\]
In particular, \(B\) does not depend on \(\alpha\), although the original matrix \(K\) is invertible for every \(\alpha>0\).

Write \(c=(b,0)\) and \(q=Bc=(b,A(I-\Pi)b)\). Since \(Bq=q\), for every positive integer \(k\) the image of the ordinary Krylov space under \(B\) equals \(\operatorname{span}\{q\}\): higher powers supply no new image direction. A zero-start GMRES residual is therefore minimized over \(c-sq\) with real scalar \(s\). Orthogonal projection gives the unique minimizer
\[
s=t=\frac{\langle c,q\rangle}{\|q\|_2^2}=\frac{E}{E+R^2},
\quad \min_s\|c-sq\|_2^2=E-\frac{E^2}{E+R^2}=\frac{ER^2}{E+R^2}.
\]
No later Krylov vector can decrease this norm. If \(R=0\), the first GMRES step solves the preconditioned system exactly. If \(R>0\), the residual is strictly positive at every step, and Arnoldi encounters degeneracy no later than the second step. The claim concerns the mathematical least-residual Krylov iterate, not a hypothetical continued finite-precision Arnoldi run.

The second block of \(\widetilde M^{-1}c\) is \(WAb=\Pi S^{-1}Ab=\Pi x_*\), so \(x_G=t\Pi x_*\). The error identity follows by the orthogonality of the range and kernel of \(\Pi\). Fourier diagonalization yields \(R^2=\sum_{j:p_j=0}a_j^2|\widehat b_j|^2\).

For comparison, the Fourier-mode block of \(B\) on retained frequencies is the identity. On each omitted frequency it maps \((u,v)\mapsto(u,a_j u)\), whose range is the line \(\operatorname{span}\{(1,a_j)\}\). The squared distance from the local right-hand side \((\widehat b_j,0)\) to this line equals \(a_j^2|\widehat b_j|^2/(1+a_j^2)\). Summing over the omitted frequencies proves the exact full-range least-squares floor above, and by inclusion of Krylov images into the range, \(d_{\mathrm{range}}^2\le\|r_G\|^2\).

For an exact strict witness, take the two-point unitary Fourier transform, \(A=\tfrac12\begin{psmallmatrix}3&-1\\-1&3\end{psmallmatrix}\), and \(\Pi=\tfrac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\); their Fourier multipliers are respectively \((1,2)\) and \((1,0)\). Put \(\widehat b=(1,1)\), hence \(b=(\sqrt2,0)\), and \(\alpha=1\). The forward matrix is symmetric positive definite with condition number \(2\). Direct substitution gives \(E=2\), \(R^2=4\), \(t=1/3\) and \(\|r_G\|_2^2=4/3\), whereas \(d_{\mathrm{range}}^2=4/5\). The exact Tikhonov solution has Fourier coefficients \((1/2,2/5)\), while the computed reconstruction has \((1/6,0)\), with squared error \(61/225\). This proves strict range-to-Krylov loss and transmitted-mode attenuation even for a condition-two SPD forward operator.

## Verification
Run `python verify_pupil.py` with Python, NumPy and SymPy. The standalone checker independently verifies the per-mode block identity and projection algebra symbolically, the condition-two example using exact rational arithmetic in Fourier coordinates, and 480 seeded real symmetric circulant systems of sizes \(2,4,6,8\). Those tests check the idempotence identity, GMRES projection residual, retained-mode reconstruction, and full-range lower bound. The infinite families are proved above and are not certified by finite sampling.

## Relationship to prior work
Drum, Onisk, Brown and Nagy (2026), arXiv:2610.17275v1, introduce the Type-II block factorization for Fourier-optical Tikhonov preconditioning, explicitly describe binary finite-pupil frequency truncation and analyze numerical optical imperfections. The present classification specializes their construction to a symmetric circulant exact binary-pupil regime and derives a closed-form stagnation and reconstruction law rather than a numerical performance claim. Brown and Walker (1997) and Sugihara and Hayami (2023) provide general foundational results on singular and range-asymmetric GMRES and breakdown, so singular-GMRES failure or idempotent projector algebra is **not** asserted to be new. The contribution assessed here is the sharp physical-aperture-to-Tikhonov matrix reduction, the all-data residual/error formulas, and the strict, well-conditioned witness separating Krylov stagnation from range-optimal residuals.

## Limitations
No theorem is claimed for noncirculant forward operators, non-binary pupils, aberrations, additive noise, quantization, finite precision, flexible/variable-preconditioner GMRES, restarts, or modified preconditioning. A mathematical minimum over a Krylov space need not equal a computed iterate after numerical breakdown. The source paper's broader optical simulations do not satisfy this exact idealization. The novelty assessment is based on inspected relevant sources, and older specialized statements not encountered remain a bibliographic risk. Independent validation has not been performed.

## References
1. C. Drum, L. Onisk, A. Brown, J. G. Nagy, *Optical Fourier Transform-Based Preconditioning for Large-Scale Inverse Problems*, arXiv:2610.17275v1 (first public 2026-10-12), Sections 2.1–2.2, 3.1.1, 4.2. https://arxiv.org/html/2610.17275v1
2. P. N. Brown and H. F. Walker, *GMRES on (Nearly) Singular Systems*, SIAM J. Matrix Anal. Appl. 18 (1997), 37–51, DOI:10.1137/S0895479894262339.
3. K. Sugihara and K. Hayami, *Right preconditioned GMRES for arbitrary singular systems*, arXiv:2310.16442 (2023), Sections 1–4. https://arxiv.org/html/2310.16442
