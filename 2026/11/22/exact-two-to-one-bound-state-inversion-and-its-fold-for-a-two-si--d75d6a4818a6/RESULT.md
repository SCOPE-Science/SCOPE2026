# Exact two-to-one bound-state inversion and its fold for a two-site Jacobi potential

## Finding

Consider the half-line discrete Schrödinger (Jacobi) operator \(J_{a,b}\) on \(\ell^2(\mathbb N_0)\), with unit nearest-neighbor hopping, Dirichlet boundary \(u_{-1}=0\), and nonzero diagonal entries \(a>0\) and \(b>0\) only at sites zero and one. In the open region
\[
a>2,\qquad b>\frac{a-1}{a-2},
\]
it has precisely two simple eigenvalues strictly above \(2\), no other point spectrum, and essential spectrum \([-2,2]\).

Write the two eigenvalues in decreasing order as \(\lambda_r=r+r^{-1}\) and \(\lambda_s=s+s^{-1}\), where \(0<r<s<1\). The *entire inverse fiber* of the unordered pair of bound-state energies among positive two-site potentials is obtained from the roots \(t>1\) of
\[
Q_{r,s}(t)=rs\,t^2-(r+s)(1-rs)t+(1-rs)=0,
\]
by setting
\[
 a=r+s+t,\qquad b=\frac1{rst}.
\]
Both quadratic roots are real and larger than one for every attainable pair, counting multiplicities. Thus there are precisely two distinct positive potentials with the same *full spectral set* except on the discriminant-zero locus, where there is exactly one. The discriminant is
\[
\Delta=(1-rs)\bigl((r+s)^2(1-rs)-4rs\bigr),
\]
and the separation of the two parameter branches is exactly
\[
|a_+-a_-|=\frac{\sqrt\Delta}{rs},\qquad
|b_+-b_-|=\frac{\sqrt\Delta}{rs(1-rs)}.
\]
At the fold, the parameter pair has the one-parameter form
\[
(a,b)=\left(t+\frac2t,\ t+\frac1t\right),\quad t>t_*,
\]
where \(t_*\) is the unique root above one of \(t^3-2t^2+2t-2=0\), approximately \(1.5436890127\).

For instance, the distinct positive pairs
\[
(a_\pm,b_\pm)=\left(\frac{13}{2}\pm2\sqrt3,\ \frac{25}{4}\mp\frac{25\sqrt3}{12}\right)
\]
have *exactly* the same spectrum \([-2,2]\cup\{29/10,101/10\}\).

## Assumptions and scope

The fixed underlying free operator is \((J_0u)_n=u_{n-1}+u_{n+1}\) for \(n\ge0\), with \(u_{-1}=0\). Only real strictly positive diagonal perturbations at sites zero and one are admitted; the hopping coefficients remain one. By *spectral set* we mean the support of the self-adjoint spectrum, not its spectral measure, norming constants, scattering data, or resonances. The two-fold statement concerns only the two-bound-state region above; no classification of zero- or one-bound-state fibers is asserted. The main classification uses the standard primary spectral-theory classification of Jacobi operators (MSC2020 47B36).

## Proof

**1. Number and location of bound states.** The free half-line resolvent has boundary values at energy \(2\) equal to the two-by-two matrix \(G(2)_{ij}=\min(i,j)+1\), for \(i,j\in\{0,1\}\). Hence its Birman–Schwinger compression for the positive perturbation has the monotone limit
\[
 B(2)=\begin{pmatrix}a&\sqrt{ab}\\\sqrt{ab}&2b\end{pmatrix}.
\]
For energies above two, its two positive eigenvalues are strictly decreasing and tend to zero at infinity. There are exactly two bound states above two precisely if both eigenvalues of \(B(2)\) exceed one. Positivity of \(B(2)-I\) is equivalent to \(a>2\) and \(b(a-2)>a-1\). Since \(J_{a,b}\ge J_0\), there are no eigenvalues below \(-2\); the free recurrence outside the support precludes square-summable solutions at and inside the band. Simplicity follows from uniqueness of a square-summable tail and backward propagation. Finite-rank perturbation preserves the essential band.

**2. The exact Jost cubic.** At \(\lambda>2\), write \(\lambda=z+z^{-1}\) for \(0<z<1\). The square-summable tail is proportional to \(z^{n-1}\) at sites \(n\ge1\). The site-one equation gives \(u_0=(z^{-1}-b)u_1\); the site-zero equation gives \(u_1=(\lambda-a)u_0\). Eliminating these values gives
\[
 F_{a,b}(z)=1-(a+b)z+abz^2-bz^3=0.
\]
Its two roots in \((0,1)\) correspond bijectively to the two simple eigenvalues. The cubic has exactly one remaining real root, and it lies strictly above one: indeed, \(F_{a,b}(1)=ab-a-2b+1=b(a-2)-(a-1)>0\) in the two-bound-state region, while the leading cubic coefficient is negative. Consequently the intermediate value theorem supplies a root \(t>1\), distinct from both interior roots; these are all three roots counting multiplicity.

**3. Exact inverse equation and completeness.** Vieta's identities for \(F_{a,b}(z)=-b(z-r)(z-s)(z-t)\) give \(a=r+s+t\), \(b=(rst)^{-1}\), and, from the linear coefficient, precisely \(Q_{r,s}(t)=0\). Conversely, any positive real \(t\) solving this equation reproduces all four coefficients of the same cubic, hence the two prescribed eigenvalues. A previously existing pair guarantees a root \(t_0>1\), so the quadratic discriminant is nonnegative. Its two roots are positive, and
\[
Q_{r,s}(1)=(1-rs)(1-r-s)+rs\ge (rs)^2>0,
\]
using \(r+s\le1+rs\) for \(r,s<1\). Since one root is greater than one and \(Q(1)>0\), the other is also greater than one. This proves the exact two-preimage-or-one-preimage classification; no solutions are lost by reconstruction.

**4. Fold and instability.** The quadratic discriminant equals \(\Delta\) above, so its root separation is \(\sqrt\Delta/(rs)\). By the product-of-roots identity, the difference of reciprocal roots is \(\sqrt\Delta/(1-rs)\), giving both exact parameter separations. At \(\Delta=0\), the inverse quadratic has a double root \(t\) (the Jost cubic still has three distinct roots), yielding \(a=t+2/t\), \(b=t+1/t\). The two-bound-state inequality becomes
\[
b(a-2)-(a-1)=\frac{(t-1)(t^3-2t^2+2t-2)}{t^2}>0.
\]
The cubic on the right is strictly increasing for real \(t\), since its derivative \(3t^2-4t+2\) has negative discriminant; it has one zero \(t_*>1\). For \(t>t_*\), the unique inverse root \(t>1\) and two distinct interior Jost roots are admissible. The square-root vanishing of branch separation is exact, rather than merely asymptotic.

**5. Algebraic example.** Put \(r=1/10\), \(s=2/5\). Then \(Q_{r,s}(t)=(t^2-12t+24)/25\), with roots \(t=6\pm2\sqrt3\), both exceeding one. The reconstruction yields the displayed parameter pairs and the eigenvalues \(101/10\) and \(29/10\). Because the perturbation is positive and supported on two sites, there are no other eigenvalues.

## Verification

The standalone `check.py` checks the exact symbolic cubic factorization and algebraic example, the fold equation, and several hundred two-bound-state parameter pairs, as well as finite-section eigenvalues for the explicit pair. It requires Python with NumPy and SymPy and can be run with `python check.py` in a directory containing this file. These computations are diagnostic: no finite section or numerical enumeration is used to prove the infinite-dimensional result. The analytic Birman–Schwinger and Vieta arguments above provide that proof.

## Relationship to prior work

Webb and Olver [1] give a general direct spectral theory for finite-rank perturbations of free Jacobi operators and identify eigenvalues using zeros of a finite polynomial. Iantchenko and Korotyaev [2] study finite-support half-line Jacobi inverse resonance problems and prove uniqueness when sufficiently rich Jost/resonance information is supplied. The present narrower observation retains only the continuous spectral support and *both* bound energies, discarding the nonphysical third Jost root and all norming/scattering data. The newly assessed part is the exact two-fold inverse fiber, its fold and parameter-instability constants, not the classical direct Jost-root method. A full-data uniqueness theorem does not imply uniqueness for this partial data.

## Limitations

No classification is provided when there are fewer than two bound states, for mixed-sign perturbations, or for more than two perturbed sites. The spectral *measures* of the two inverse solutions generally differ. Other prior literature might encode this algebraic two-site inverse fiber in equivalent variables; originality is therefore a best-knowledge claim pending independent specialist examination. The verification checks are not independent mathematical validation.

## References

[1] M. Webb and S. Olver, *Spectra of Jacobi operators via connection coefficient matrices*, arXiv:1702.03095 (first publicly submitted 10 February 2017), https://arxiv.org/abs/1702.03095 ; especially Sections 4.2–4.3 and Theorem 4.22.

[2] A. Iantchenko and E. Korotyaev, *Periodic Jacobi operator with finitely supported perturbation on the half-lattice*, arXiv:1004.2664 (first publicly submitted 15 April 2010), https://arxiv.org/abs/1004.2664 ; especially Section 3.3 and Theorems 1.3–1.5.
