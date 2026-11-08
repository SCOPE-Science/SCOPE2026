# D-optimal angular separation for four phaseless samples of a damped two-mode flow

## Finding

Fix a relative mode modulus \(r>0\) and an angular increment \(\theta\in\mathbb R\), and set \(z=re^{i\theta}\). For arbitrary unknown \(u,v\in\mathbb C\), consider four consecutive squared-intensity measurements
\[
y_k=|u+z^k v|^2,\qquad k=0,1,2,3.
\]
Write their real linear lifting as \(y=M_{r,\theta}U\), with
\[
U=\left(|u|^2,|v|^2,2\operatorname{Re}(\overline u v),-2\operatorname{Im}(\overline u v)\right)^T,
\quad
M_{r,\theta}=\left(1,r^{2k},r^k\cos(k\theta),r^k\sin(k\theta)\right)_{k=0}^3.
\]
The exact determinant is
\[
\det M_{r,\theta}=r^3(r^2-1)(1+r^2-2r\cos\theta)^2\sin\theta.\tag{1}
\]
In particular the lifting is invertible exactly when \(r\ne1\) and \(\theta\notin\pi\mathbb Z\). In that case the four intensities uniquely determine **every** pair \((u,v)\), including zero components, up to a common unit-modulus factor.

For each **fixed** \(r>0\) with \(r\ne1\), the determinant magnitude \(|\det M_{r,\theta}|\) has precisely two global angular maximizers modulo \(2\pi\): \(\theta=\pm\theta_*(r)\), where
\[
\boxed{\cos\theta_*(r)=\frac{r+r^{-1}-\sqrt{(r+r^{-1})^2+96}}{12}
=-\frac8{r+r^{-1}+\sqrt{(r+r^{-1})^2+96}}.}\tag{2}
\]
These optimizers are nondegenerate, and their principal representatives satisfy
\[
\frac\pi2<\theta_*(r)<\arccos(-2/3).
\]
The design is invariant under replacing \(r\) by \(r^{-1}\). As \(r\to1\) through unequal values, \(\theta_*(r)\to\arccos(-2/3)\); as \(r\to0\) or \(r\to\infty\), \(\theta_*(r)\to\pi/2\).

With additive, independent, equal-variance perturbations of the **squared intensities**, this is exactly the D-optimal angular design for estimating the four *lifted real coordinates*: it maximizes the determinant of the normal matrix, equivalently minimizes the generalized covariance volume of the unrestricted linear lifted estimator. This is not a claim of optimality for nonlinear rank-one estimation, for other noise models, or when the four observation times may vary.

## Assumptions and scope

The relative modulus \(r\) is fixed before optimizing \(\theta\); all four observation indices are exactly \(k=0,1,2,3\), with equal observation weights and an unnormalized fixed first mode. A general diagonal two-mode evolution with eigenvalues \(\lambda_0\ne0,\lambda_1\) reduces to this model after dividing each known observation by \(|\lambda_0|^{2k}\), with \(z=\lambda_1/\lambda_0\). Such rescaling changes a physical noise distribution, so the D-optimality assertion refers specifically to the normalized \(y_k\) above. All data are complex amplitudes, with real, nonnegative measured intensities. The complex signal is not assumed componentwise nonvanishing.

## Proof

**1. Linear lifting and determinant.** Put \(w=\overline u v\). Expanding gives
\[
|u+z^k v|^2=|u|^2+|z|^{2k}|v|^2+2\operatorname{Re}(wz^k),
\]
which is exactly the stated four-column real matrix. Let \(V\) denote the complex Vandermonde matrix whose four columns have bases \(1,r^2,z,\bar z\), each evaluated at exponents \(0,1,2,3\). The last two real columns of \(M\) are the sum and difference of the last two complex columns, divided by \(2\) and \(2i\) respectively. Their change-of-basis matrix has determinant of absolute value \(1/2\). Therefore
\[
|\det M|=\tfrac12|(r^2-1)(z-1)(\bar z-1)(z-r^2)(\bar z-r^2)(\bar z-z)|.
\]
Since \(|z-1|^2=1+r^2-2r\cos\theta\), \(|z-r^2|^2=r^2|z-1|^2\), and \(|z-\bar z|=2r|\sin\theta|\), this yields the absolute value of (1). Keeping track of the column order and the real/imaginary change-of-basis gives the **signed** identity (1). This also proves the exact invertibility criterion. If \(M\) is invertible, the four squared intensities recover \(U\), hence the Hermitian rank-one matrix \((u,v)(u,v)^*\). Such a matrix determines the vector up to one global phase, including the zero vector.

**2. All angular maximizers.** For fixed \(r\ne1\), the positive factors of (1) independent of \(\theta\) may be discarded. Put \(a=1+r^2\), \(x=\cos\theta\), and maximize
\[
F_r(x)=(a-2rx)^2\sqrt{1-x^2},\qquad -1\le x\le1.
\]
The factor \(a-2rx\) is strictly positive for \(-1<x<1\). At the endpoints \(F_r=0\), while the interior values are positive. On the interior, the logarithmic derivative has the sign of
\[
Q_r(x)=6rx^2-a x-4r.\tag{3}
\]
Indeed, multiplication by the positive denominator \((a-2rx)(1-x^2)\) transforms \(F_r'/F_r\) into \(Q_r(x)\). We have \(Q_r(-1)=(r+1)^2>0\), \(Q_r(0)=-4r<0\), and \(Q_r(1)=-(r-1)^2<0\) when \(r\ne1\). As \(Q_r\) is an upward-opening quadratic, exactly one root lies in \((-1,0)\), and the other lies in \((1,\infty)\). Thus \(F_r\) strictly increases then strictly decreases, giving the unique maximizer in \(x\) and the two angular representatives. The negative root of (3) is precisely (2). More precisely, \(Q_r'(x_*)=12rx_*-(1+r^2)<0\), so the second derivative of \(\log F_r\) at the critical cosine is strictly negative. Since \(\sin\theta_*\ne0\), the two angular maxima are nondegenerate.

**3. Range, reciprocity and limits.** Set \(s=r+r^{-1}\ge2\). Formula (2) becomes \(x_*(s)=(s-\sqrt{s^2+96})/12\). Its derivative is \((1-s/\sqrt{s^2+96})/12>0\), with \(x_*(2)=-2/3\) and \(x_*(s)\uparrow0\) as \(s\to\infty\). For \(r\ne1\), \(s>2\), proving the strict angular range and both limiting statements. Dependence only on \(s\) proves the symmetry under reciprocation.

**4. D-optimality and exact boundaries.** If the additive noise in \(y\) has covariance \(\sigma^2 I_4\), unrestricted linear least squares for \(U\) has covariance \(\sigma^2(M^TM)^{-1}\) when invertible. Consequently \(\det\operatorname{Cov}=\sigma^8/|\det M|^2\). The angular maximizers above uniquely minimize this generalized variance. At \(r=1\), the two modulus columns coincide, and for instance \((u,v)=(1,2)\) and \((2,1)\) have identical intensities at all times but are not phase equivalent. When \(\sin\theta=0\), all \(z^k\) are real, and \((1,i)\) and \((1,-i)\) have identical intensities. Thus the noninvertible boundaries genuinely fail universal phase retrieval, not merely this particular lifting certificate.

## Verification

The standalone standard-library script `check_doptimal.py` computes the determinant independently by real Gaussian elimination, compares it with (1), checks the stationary quadratic and reciprocal formula, samples each full angular interval at a grid of 1001 cosines for twelve widely separated moduli, and tests singular boundaries. The script uses a fixed random seed and on execution reported `DAMPED_TWO_MODE_DOPT_CHECKS_PASS 12473`. These finite and floating-point checks are **not** proofs of the universal assertions; the preceding algebra and calculus supply those proofs.

## Relationship to prior work

Beinert and Hasannasab's 2021 work on dynamical phase retrieval by polarization develops dynamical frames, Vandermonde structure, and additional polarization measurements. Their 2021 preprint *Phase Retrieval and System Identification in Dynamical Sampling via Prony's Method* (journal version 2023) already proves generic squared-intensity recovery via collision-free spectral products (Theorem 5 of the 2023 full text), which includes the generic injectivity mechanism here. Neither of the inspected relevant sections gives the sharp D-optimal **angular** design at fixed relative modulus for four consecutive time observations. The present claim of contribution is specifically the global exact phase optimizer and complete equality/boundary classification for the normalized four-by-four lifted design, **not** the Vandermonde determinant technique or generic injectivity. The paper's approximate-Prony stability estimates concern separation and perturbation, not the stated angular determinant optimum. The resulting one-variable design problem is elementary once the model is reduced, but its sharp solution specifies a natural experiment-design invariant not supplied by those general results.

## Limitations

This is exact for a restricted one-parameter design and the determinant (D-) criterion only. It is not a theorem about maximum smallest singular value, about arbitrary temporal schedules, about more than two modes, about unknown evolution eigenvalues, or about phase-retrieval optimality under signal-dependent shot noise. Generic injectivity is established background; the independent historical priority of the explicit angle remains provisional because synonymous classical experimental-design formulations cannot be ruled out by finite searches. Numerical checks do not certify the full theorem independently.

## References

1. R. Beinert and M. Hasannasab, *Phase Retrieval via Polarization in Dynamical Sampling*, arXiv:2102.00536v1 (first public 2021-01-31), especially Sections 3–5. https://arxiv.org/abs/2102.00536
2. R. Beinert and M. Hasannasab, *Phase Retrieval and System Identification in Dynamical Sampling via Prony's Method*, arXiv:2103.10086v1 (first public 2021-03-18); open-access journal version, *Advances in Computational Mathematics* 49, article 56 (2023), Theorem 5, Section 8 and Appendix A. https://doi.org/10.1007/s10444-023-10059-7
