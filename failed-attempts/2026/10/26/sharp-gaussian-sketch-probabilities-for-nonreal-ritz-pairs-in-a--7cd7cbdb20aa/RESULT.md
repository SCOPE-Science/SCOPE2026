# Sharp Gaussian-sketch probabilities for nonreal Ritz pairs in a positive-definite Lanczos triple

## Finding

For any \(b,c>0\), \(d>\sqrt{b^2+c^2}\), and integer \(\ell\ge2\), apply an independent real Gaussian sketch with \(\ell\) rows to the two-dimensional Krylov subspace of \(e_1\) for the positive-definite tridiagonal matrix
\[
A=\begin{pmatrix}d&b&0\\ b&d&c\\0&c&d\end{pmatrix}.
\]
The sketched Rayleigh–Ritz (sRR) matrix has a nonreal conjugate eigenvalue pair with a strictly positive probability \(P_\ell(b,c)\) given by the exact one-dimensional integral below. Writing \(\nu=\ell-1\), the probability has the sharp large-sketch asymptotic
\[
\boxed{P_\ell(b,c)\sim\sqrt{\frac{b^2+c^2}{3\pi b^2\nu}}\left(1+\frac{b^2}{c^2}\right)^{-\nu/2}},\qquad\nu\to\infty.
\]
In particular, its exact exponential rate is \(-\tfrac12\log(1+b^2/c^2)\) per additional sketch row. The event probability is independent of \(d\), conditional on positive definiteness. This quantitatively sharpens the previously observed possibility of nonreal sRR eigenvalues for real symmetric inputs; it does not assert that the qualitative phenomenon is new.

## Assumptions and scope

All matrices and sketches are real and all calculations are in exact arithmetic. Fix \(b,c>0\), \(d>\sqrt{b^2+c^2}\), and integer \(\ell\ge2\). Let \(S\in\mathbb R^{\ell\times3}\) have independent standard normal entries, and \(V=[e_1,e_2]\in\mathbb R^{3\times2}\). Since \(Ae_1=de_1+be_2\), this is precisely the orthonormal two-vector Lanczos basis starting at \(e_1\). Define
\[
\widehat H=(SV)^\dagger SAV,
\]
using the Moore–Penrose pseudoinverse. The Gaussian sketch has full rank on this basis almost surely. Scaling every entry of \(S\) by \(\ell^{-1/2}\) leaves \(\widehat H\) unchanged.

Put \(\nu=\ell-1\) and define the angular fraction
\[
\psi_b(r)=\begin{cases}0,&0\le r\le b,\\
\displaystyle\frac1\pi\arccos\!\left(\frac{\sqrt{r^2+8b^2}-2b}{r}\right),&r>b.\end{cases}
\]
The exact finite-row probability is
\[
\boxed{P_\ell(b,c)=\int_b^\infty \frac{\nu r}{c^2}\left(1+\frac{r^2}{c^2}\right)^{-(\nu+2)/2}\psi_b(r)\,dr.}
\]
It may also be evaluated by the bounded integral
\[
P_\ell(b,c)=\left(1+\frac{b^2}{c^2}\right)^{-\nu/2}\int_0^1\psi_b\!\left(\sqrt{(b^2+c^2)u^{-2/\nu}-c^2}\right)du.
\]
The integrand at \(u=0\) is defined by its limiting value \(0\), which does not affect the integral. No zero-probability conditioning or selection of successful sketches is assumed.

## Proof

**Step 1 (exact random projection).** Write the first two columns of \(S\) as \(G=[g_1,g_2]\in\mathbb R^{\ell\times2}\), and its last column as \(h\). These are independent standard Gaussian arrays. Since
\[
AV=V\begin{pmatrix}d&b\\b&d\end{pmatrix}+c e_3e_2^{\mathsf T},
\]
we have, almost surely,
\[
\widehat H=\begin{pmatrix}d&b+cw_1\\b&d+cw_2\end{pmatrix},\quad
w=(G^{\mathsf T}G)^{-1}G^{\mathsf T}h.
\]
Conditionally on \(M=G^{\mathsf T}G\), \(w\) is centered Gaussian with covariance \(M^{-1}\). The Gram matrix has real Wishart density proportional to \((\det M)^{(\ell-3)/2}\exp[-\operatorname{tr}(M)/2]\) for positive-definite \(M\). Multiplying by the conditional normal density and integrating over positive-definite \(M\), or equivalently applying the two-variable matrix-gamma change \(M\mapsto(I+ww^{\mathsf T})^{-1/2}M(I+ww^{\mathsf T})^{-1/2}\), shows that the unconditional density of \(w\) is proportional to
\[
\det(I+ww^{\mathsf T})^{-(\ell+1)/2}=(1+\|w\|_2^2)^{-(\nu+2)/2}.
\]
Polar normalization yields the exact density \(\nu(1+\|w\|_2^2)^{-(\nu+2)/2}/(2\pi)\). Equivalently, \(w\stackrel{\rm d}=Z/\sqrt U\) with independent \(Z\sim N(0,I_2)\) and \(U\sim\chi^2_\nu\). In particular, \((x,y)=c(w_1,w_2)\) has density
\[
f(x,y)=\frac{\nu}{2\pi c^2}\left(1+\frac{x^2+y^2}{c^2}\right)^{-(\nu+2)/2}.
\]

**Step 2 (discriminant and angular geometry).** The discriminant of the real two-by-two matrix \(\widehat H\) is
\[
\Delta=(cw_2)^2+4b(b+cw_1)=y^2+4b(b+x).
\]
Thus its eigenvalues form a nonreal pair exactly when \(x<-b-y^2/(4b)\). In polar coordinates \(x=r\cos\theta\), \(y=r\sin\theta\), this event is empty for \(r\le b\). For \(r>b\), its angular fraction is \(\psi_b(r)\): on the circle \(x^2+y^2=r^2\), the boundary negative \(x\)-coordinate is \(x=2b-\sqrt{r^2+8b^2}\). Rotational symmetry and radial integration prove the stated exact formula. Its integrand is positive for every \(r>b\), so \(P_\ell>0\) for every finite \(\ell\). The bounded-integral version follows by the survival substitution \(u=[(1+r^2/c^2)/(1+b^2/c^2)]^{-\nu/2}\).

**Step 3 (sharp Laplace boundary asymptotic).** Let \(r=b+z\), \(z\downarrow0\). Differentiating the angular threshold gives
\[
\psi_b(b+z)=\frac{2}{\pi\sqrt{3b}}\sqrt z\,[1+O(z)],
\]
while
\[
\log(1+(b+z)^2/c^2)=\log(1+b^2/c^2)+\frac{2b}{b^2+c^2}z+O(z^2).
\]
Set \(D=1+b^2/c^2\) and \(\lambda=b/(b^2+c^2)>0\). A standard one-sided Laplace argument (split the integral at fixed small \(z>0\), substitute \(z=v/\nu\) in the local integral, dominate by a decaying exponential and use \(\int_0^\infty v^{1/2}e^{-\lambda v}dv=\sqrt\pi/(2\lambda^{3/2})\)) yields
\[
P_\ell(b,c)\sim D^{-\nu/2}\frac{\nu b}{c^2D}\frac{2}{\pi\sqrt{3b}}\frac{\sqrt\pi}{2(\nu\lambda)^{3/2}}.
\]
Simplification is exactly the displayed prefactor. For the tail above a fixed local neighborhood, the positive logarithmic rate is bounded strictly away from its minimum at \(r=b\), so that tail is exponentially smaller. The normalization \(D^{-\nu/2}\) gives the asserted logarithmic rate.

**Step 4 (minimal dimension).** A full two-dimensional orthonormal basis in ambient dimension two is invariant under any two-by-two matrix. Whenever the Gaussian sketch is full column rank, \((SV)^\dagger(SAV)=V^{\mathsf T}AV\), which is real symmetric for a real symmetric \(A\). Hence three ambient dimensions are minimal for a nonreal sketched pair with a two-vector Lanczos basis. The assumptions \(b,c>0\) ensure the two Lanczos steps are nonterminal, and \(d>\sqrt{b^2+c^2}\) makes \(A\) strictly positive definite.

## Verification

Execute `python3 verify.py` from a folder containing the supplied standalone verifier; only the Python standard library is needed. Its deterministic exact-rational witness sets \(b=1\), \(c=2\), \(d=5\) and \(S\) with rows \((1,0,-1)\), \((0,1,0)\), \((0,0,1)\). It computes
\[
\widehat H=\begin{pmatrix}5&-1\\1&5\end{pmatrix}
\]
with eigenvalues \(5\pm i\), although \(A\) has strictly positive eigenvalues \(5\) and \(5\pm\sqrt5\). The verifier also checks exact regression identities, numerical Gaussian frequencies, exact integral evaluation, and the asymptotic prefactor. Its finite tests validate algebra and implementation consistency but are not proofs of a universal probability law or an infinite limit; those are established above.

## Relationship to prior work

Nakatsukasa and Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems* (arXiv:2111.00113, first posted 2021-10-29), develop sketched Rayleigh–Ritz and explicitly state in Section 6.8 that even symmetric eigenproblems can yield nonreal sketched eigenvalues. They further note practical real-part postprocessing. This qualitative phenomenon is established prior art. Their Section 6.7 discusses the final-column perturbation for Krylov bases; the present theorem specializes that structure and quantifies exactly the Gaussian probability and its sharp rate on the minimal nonterminal Lanczos triple. Burke, Güttel, and Soodhalter (arXiv:2311.14206) analyze related sketched Krylov projections, while Palitta, Schweitzer, and Simoncini (arXiv:2306.06481, especially Section 7) discuss spectral outliers in sketched polynomial Krylov matrix-function evaluation. Their statements do not by themselves give this event probability or the boundary-Laplace asymptotic. Exact multivariate Student regression and one-sided Laplace integration are classical ingredients, not presented as new general results.

## Limitations

The probability formula concerns real independent Gaussian sketches, a fixed three-dimensional symmetric positive-definite tridiagonal family, a two-vector Lanczos basis, and unconditioned exact arithmetic. It does not quantify convergence of Ritz vectors, residual quality, errors after taking real parts, larger-dimensional or block-Krylov configurations, structured sketches such as SRFT, or the effects of regularization, finite precision, or sketch-dependent safeguards. A rare nonreal pair is not necessarily a failure of downstream use. Novelty is assessed against the specifically inspected literature and may be affected by equivalent unlocated formulations.

## References

1. Yuji Nakatsukasa and Joel A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v1 (2021-10-29), Sections 6.3, 6.7, and 6.8. https://arxiv.org/abs/2111.00113
2. Liam Burke, Stefan Güttel, and Kirk Soodhalter, *GMRES with randomized sketching and deflated restarting*, arXiv:2311.14206v1 (2023-11-23). https://arxiv.org/abs/2311.14206
3. Davide Palitta, Marcel Schweitzer, and Valeria Simoncini, *Sketched and truncated polynomial Krylov methods: Evaluation of matrix functions*, arXiv:2306.06481v1 (2023-06-10), especially Section 7. https://arxiv.org/abs/2306.06481
