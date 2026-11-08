# Sharp conditioning and the ternary threshold for balanced finite Fourier slices

## Finding

For integers \(k\ge1\) and \(M\ge3\), let \(\zeta=\exp(2\pi i/M)\), and index the complex matrix \(F_{k,M}\) by the \(k\)-subsets of \([2k]\):
\[
F_{k,M}(A,B)=\zeta^{|A\cap B|}.
\]
Write \(c=\cot(\pi/M)\), and define the positive polynomials \(U_0(c)=1\), \(U_1(c)=c\), and
\[
(m+1)U_{m+1}(c)=(2m+1)cU_m(c)+mU_{m-1}(c).
\]
Every \(F_{k,M}\) is invertible. Its singular values, including multiplicities, are
\[
(2\sin(\pi/M))^k U_m(c),\quad m=0,\ldots,k,\qquad
\operatorname{mult}(m)=\binom{2k}{k-m}-\binom{2k}{k-m-1}.
\]
For \(M\ge4\), the sharp spectral condition number is
\[
\boxed{\kappa_2(F_{k,M})=U_k(\cot(\pi/M)).}
\]
The largest singular mode is the constant-vector sector \(m=k\), while the smallest is the top Johnson harmonic \(m=0\); when \(M=4\) an additional \(m=1\) mode ties for the smallest.

At the exceptional **ternary phase** \(M=3\), define \(T_m\) by
\[
\sum_{m\ge0}T_m t^m=(1-2t-3t^2)^{-1/2}.
\]
These are the generalized central trinomial coefficients \(T_m=\sum_{a=0}^{\lfloor m/2\rfloor}\binom{m}{2a}\binom{2a}{a}\). For \(k\ge2\),
\[
\boxed{\kappa_2(F_{k,3})=T_k/3^{(k-1)/2}.}
\]
The smallest mode is now \(m=1\), **not** the top harmonic \(m=0\); the largest remains \(m=k\). At \(k=2\), \(m=0\) and \(m=k\) tie for the largest. At \(k=1\), the condition number is \(\sqrt3\), with largest mode \(m=0\) and smallest mode \(m=1\). In particular, a discrete phase threshold swaps the least-stable harmonic sector.

For fixed \(M\ge4\), write \(s=\sqrt{1+c^2}\) and \(\rho=c+s\). Then
\[
\boxed{\kappa_2(F_{k,M})\sim \sqrt{\frac{\rho}{2\pi s}}\,\frac{\rho^k}{\sqrt{k}}}\qquad (k\to\infty).
\]
For the ternary phase,
\[
\boxed{\kappa_2(F_{k,3})\sim\frac3{2\sqrt\pi}\frac{(\sqrt3)^k}{\sqrt{k}}}.
\]
The constants and exponential bases are sharp.

## Assumptions and scope

All matrices are unnormalized complex Fourier principal minors of \((\mathbb Z/M\mathbb Z)^{2k}\) at the binary constant-weight slice, with their ordinary Euclidean spectral condition number. Every integer \(M\ge3\) and \(k\ge1\) is covered; the limit keeps \(M\) fixed. No phase- or dimension-uniform asymptotic error term is claimed. The Johnson harmonic multiplicities are given explicitly above; binomial coefficients with lower argument \(-1\) vanish.

## Proof

**1. Known spectral decomposition, independently specialized.** The intersection-matrix eigenvalue theorem of Ghareghani–Ghorbani–Mohammad-Noori, Theorem 9, applied to the kernel \((1+u)^{|A\cap B|}\) with \(u=\zeta-1\), gives on the \(j\)-th Johnson harmonic sector
\[
\lambda_j=(\zeta-1)^j\sum_{\ell=0}^{k-j}\binom{k-j}{\ell}^2\zeta^\ell,
\qquad \dim V_j=\binom{2k}j-\binom{2k}{j-1}.
\]
These real mutually orthogonal harmonic subspaces are independent of \(\zeta\), so the complex matrix is unitarily diagonalizable, and its singular values are \(|\lambda_j|\). **This general eigenvalue theorem is prior work and is not claimed here.**

**2. Legendre reduction and invertibility.** Set \(m=k-j\). The classical identity
\[
\sum_{\ell=0}^m\binom m\ell^2 z^\ell=(1-z)^mP_m\left(\frac{1+z}{1-z}\right)
\]
with \(z=\zeta\) and \((1+\zeta)/(1-\zeta)=i\cot(\pi/M)=ic\) yields
\[
|\lambda_j|=|1-\zeta|^k|P_m(ic)|=(2\sin(\pi/M))^k U_m(c),
\quad U_m(c)=(-i)^mP_m(ic).
\]
The generating function is \((1-2ct-t^2)^{-1/2}\). For \(c>0\), the recurrence and \(U_0=1\), \(U_1=c\) imply \(U_m>0\), proving invertibility for every permitted modulus and dimension.

**3. The endpoint problem for \(M\ge4\).** Since \(c\ge1\), the recurrence shows \(U_1\ge U_0\) and, inductively, \(U_{m+1}>U_m\) for \(m\ge1\): indeed
\[
(m+1)U_{m+1}\ge(3m+1)U_m>(m+1)U_m,
\]
where the first inequality uses positivity of \(U_{m-1}\), and the last inequality uses \(c\ge1\) and \(m\ge1\). Thus the exact extremal sectors and \(\kappa_2=U_k(c)\) follow.

**4. The ternary outlier.** Put \(T_m=3^{m/2}U_m(1/\sqrt3)\). Substitution into the recurrence gives
\[
(m+1)T_{m+1}=(2m+1)T_m+3mT_{m-1},\quad T_0=T_1=1.
\]
In particular \(T_2=3\). For \(r_m=T_m/T_{m-1}\), an induction from \(r_2=3\) proves
\[
3-\frac2m\le r_m\le3\quad(m\ge2).
\]
The lower bound at the next step follows from \(r_m\le3\); the upper bound follows from \(r_m\ge 3-2/m\ge 3m/(m+2)\). Hence \(r_m>\sqrt3\) for \(m\ge2\). The sequence \(T_m/3^{m/2}\) decreases from \(m=0\) to \(m=1\) and thereafter strictly increases; it equals its initial value at \(m=2\). This supplies all stated endpoint sectors, the small-\(k\) exceptions, and the ternary exact formula.

**5. Sharp limits.** The Legendre integral representation gives
\[
U_k(c)=\pi^{-1}\int_0^\pi(c+\sqrt{1+c^2}\cos\theta)^k\,d\theta.
\]
For fixed \(c\ge1\), the unique absolute-modulus maximum is \(\rho=c+s\) at \(\theta=0\). Laplace's method, using \(c+s\cos\theta=\rho-s\theta^2/2+O(\theta^4)\), gives \(U_k\sim\rho^k\sqrt{\rho/(2\pi sk)}\). The ternary generating function factors as \((1-3t)^{-1/2}(1+t)^{-1/2}\); its dominant singularity at \(t=1/3\) gives \(T_k\sim (\sqrt3/2)3^k/(\sqrt{\pi k})\), from which the stated limit follows.

## Verification

The standalone `check.py` uses exact Eisenstein-integer arithmetic. It independently evaluates the original slice matrices and verifies the eigenvector identities for \(1\le k\le5\) in both balanced and one-extra-coordinate cases, checking 2770 matrix rows. It checks the integer trinomial recurrence and the sharp squared spectral endpoints through \(k=499\). A separate numerical singular-value reconstruction verified the stated endpoints for \(M\in\{3,4,5,6,8\}\) and \(k\le3\). These computations are finite corroboration and do not replace the full proof.

## Relationship to prior work

The general intersection-kernel eigenvalue formula and its harmonic multiplicities were proved by Ghareghani–Ghorbani–Mohammad-Noori (2009 preprint, 2011 revision), Theorem 9. Filmus (2014) treats the slice harmonic basis. The new precise assertion here is **which sector realizes the smallest singular value at each permitted primitive root of unity**, including the exceptional ternary switch, and the closed-form **sharp condition numbers and exponential-scale asymptotics**. The result is thus a sharp spectral-optimization refinement of known eigenvalue theory, rather than a claim to discover the spectrum itself. The classical Legendre identities and trinomial generating function are standard inputs.

## Limitations

This theorem does not provide uniform asymptotics when the modulus grows with dimension, nor a classification of all complex phases outside roots of unity. The generic eigenvalues and classical polynomial identities are established prior mathematics. Although no literature statement explicitly giving this phase-threshold conditioning law was located in the bounded search, wider historical coverage may exist. Independent validation has not been performed.

## References

- N. Ghareghani, E. Ghorbani and M. Mohammad-Noori, *Intersection matrices revisited*, arXiv:0902.4367, first public 2009-02-25, particularly Theorem 9; https://arxiv.org/abs/0902.4367.
- Y. Filmus, *An orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, first public 2014-06-01; https://arxiv.org/abs/1406.0142.
- Z.-W. Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887, first public 2010-08-23; https://arxiv.org/abs/1008.3887.
- NIST Digital Library of Mathematical Functions, Chapter 14 (Legendre functions), https://dlmf.nist.gov/14.
