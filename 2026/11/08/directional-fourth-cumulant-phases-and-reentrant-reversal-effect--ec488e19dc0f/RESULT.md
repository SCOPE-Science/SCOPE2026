# Directional fourth-cumulant phases and reentrant reversal effects in a chiral four-state walker

## Finding

Consider a planar particle of speed \(v>0\) whose velocity successively points in one of the four cardinal directions. Its orientation changes by a left quarter-turn at rate \(a\geq0\), a right quarter-turn at rate \(b\geq0\), and a half-turn at rate \(h\geq0\), with \(M=a+b>0\). Start with uniform orientation and position zero. For each angle \(\theta\in\mathbb R\), denote the projected displacement by
\[
Z_t(\theta)=X_t\cos\theta+Y_t\sin\theta.
\]
Put \(L=M+2h\), \(\Omega=a-b\), \(Q=L^2+\Omega^2\), and
\[
F=L\bigl[(2M-L)L^2-(L+2M)\Omega^2\bigr].
\]
Then the second and fourth cumulant growth rates exist and satisfy
\[
\lim_{t\to\infty}\frac{\kappa_2(Z_t(\theta))}{t}=\frac{v^2L}{Q},
\qquad
\boxed{\lim_{t\to\infty}\frac{\kappa_4(Z_t(\theta))}{t}=
-\frac{3v^4}{MQ^3}\left[F+Q^2\sin^2(2\theta)\right].}
\]
Thus the diffusive variance rate does not depend on projection angle, whereas the fourth-cumulant rate does. Every diagonal projection \(\theta=\pi/4\pmod{\pi/2}\) has strictly negative fourth-cumulant rate. For any \(F<0\), the positive fourth-cumulant directions are precisely those obeying
\[
\sin^2(2\theta)<-F/Q^2.
\]
The sector half-width around every cardinal axis is \(\tfrac12\arcsin\sqrt{-F/Q^2}\), strictly between zero and \(\pi/4\). If \(F=0\) the rate vanishes at cardinal axes and is negative at all other angles; if \(F>0\) it is negative everywhere.

There is a sharp and nonmonotone phase threshold. Write \(q=h/M\) and \(\chi=\Omega/M\), so \(|\chi|\le1\). For \(0\le q<1/2\), the axial fourth-cumulant rate is positive exactly when
\[
\chi^2>f(q):=\frac{(1+2q)^2(1-2q)}{3+2q}.
\]
For \(q=1/2\), it is positive exactly when \(\chi\ne0\) (and zero when \(\chi=0\)); for \(q>1/2\), it is positive for every admissible \(\chi\). The threshold \(f(q)\) increases and then decreases on \([0,1/2]\), attaining its unique maximum
\[
q_* = \frac{\sqrt5}{2}-1,\qquad f(q_*)=10\sqrt5-22.
\]
Hence changing only the half-turn rate can cause a positive-negative-positive *reentrant sign sequence* at a fixed quarter-turn chirality. For example, fix \(M=v=1\) and \(\chi^2=7/20\). The axial fourth-cumulant rate is positive at \(q=0\), negative at \(q=1/8\), and positive again at \(q=1/2\).

## Assumptions and scope

The four-state orientation \(J_t\in\{0,1,2,3\}\) is a continuous-time Markov chain with jumps \(j\to j+1\pmod4\) at rate \(a\), \(j\to j-1\pmod4\) at rate \(b\), and \(j\to j+2\pmod4\) at rate \(h\). The position evolves as \(d(X_t,Y_t)/dt=v(\cos(\pi J_t/2),\sin(\pi J_t/2))\). The chain starts in its uniform stationary distribution. The hypotheses \(a,b,h\ge0\) and \(a+b>0\) guarantee irreducibility, including unidirectional turning cases. There is no translational Brownian noise, confining potential, or interparticle interaction. The fourth cumulant is \(\kappa_4(Z)=\mathbb E[Z^4]-3\mathbb E[Z^2]^2\) because all projected odd moments vanish by inversion symmetry. The result concerns the coefficient of linear growth at long times; it is not a finite-time sign claim.

## Proof

**1. Tilted generator.** In state order \(0,1,2,3\), let \(G\) be the row generator with off-diagonal entries \(G_{j,j+1}=a\), \(G_{j,j-1}=b\), \(G_{j,j+2}=h\), and \(G_{j,j}=-(a+b+h)\). Put \(u=v\cos\theta\) and \(w=v\sin\theta\). The real moment-generating tilted generator is
\[
G_k=G+k\operatorname{diag}(u,w,-u,-w).
\]
A direct determinant expansion, using \(L=M+2h\) and \(\Omega=a-b\), gives exactly
\[
\det(\lambda I-G_k)=
\lambda(\lambda+2M)\bigl[(\lambda+L)^2+\Omega^2\bigr]
-k^2(u^2+w^2)(\lambda+M)(\lambda+L)
+k^4u^2w^2.
\]
This identity includes the parameter boundaries \(a=0\), \(b=0\), and \(h=0\).

**2. Long-time cumulants.** Since \(M>0\), \(G\) is irreducible and zero is its simple dominant eigenvalue. For real \(k\) sufficiently near zero, its simple analytic continuation \(\psi(k)\) dominates the remaining spectrum. Finite-state spectral perturbation therefore gives \(\log\mathbb E[e^{kZ_t}]=t\psi(k)+O(1)\), with the error and derivatives through order four locally bounded in \(k\). Fourfold symmetry makes \(\psi\) even. Write \(\psi(k)=A k^2+B k^4+O(k^6)\). Substituting into the determinant yields, with \(U=u^2+w^2=v^2\),
\[
2MQ A=UML,
\quad
2MQ B+(Q+4ML)A^2-U(M+L)A+u^2w^2=0.
\]
Consequently \(A=UL/(2Q)\), and algebraic simplification gives
\[
2A=\frac{UL}{Q},\quad
24B=-\frac{3}{MQ^3}\bigl[U^2F+4u^2w^2Q^2\bigr].
\]
Since \(4u^2w^2=v^4\sin^2(2\theta)\), these are the announced limits of \(\kappa_2/t\) and \(\kappa_4/t\).

**3. Negative diagonal rate and all angular sectors.** The strict identity
\[
F+Q^2=2ML^3+L(L-2M)\Omega^2+\Omega^4>0
\]
holds for all parameters: if \(L\ge2M\), all displayed terms are nonnegative and the first is positive; if \(M\le L<2M\), then \(|\Omega|\le M\) implies \(L(L-2M)\Omega^2\ge-LM^3\) and the sum is at least \(LM(2L^2-M^2)>0\). At diagonal angles \(\sin^2(2\theta)=1\), hence strict negativity. If \(F<0\), this also proves \(0<-F/Q^2<1\), so the positive angular sectors and their half-width follow by solving the strict trigonometric inequality. The cases \(F=0\) and \(F>0\) follow directly.

**4. Sharp chirality-reversal phase.** After substituting \(L=M(1+2q)\) and \(\Omega=M\chi\), the sign of \(F\) is the sign of
\[
(1-2q)(1+2q)^2-(3+2q)\chi^2.
\]
For \(0\le q<1/2\), this proves the displayed threshold and its strict/equality cases. At \(q=1/2\), only the chirality-dependent negative term remains; for \(q>1/2\), both terms are strictly negative. Differentiating the threshold gives
\[
f'(q)=-\frac{4(2q+1)(4q^2+8q-1)}{(2q+3)^2}.
\]
Its unique interior zero is \(q_* =\sqrt5/2-1\), at which \(f=10\sqrt5-22\); derivative signs yield the unique maximum. To verify reentrance, note \(f(0)=1/3<7/20\), \(f(1/8)=75/208>7/20\), and at \(q=1/2\) every nonzero \(\chi\) gives a positive rate.

**5. An exact angular contrast.** For \(a=5\), \(b=1\), \(h=0\), and \(v=1\), one gets \(M=L=6\), \(\Omega=4\), \(Q=52\), and \(F=-432\). Hence the axial rate is exactly \(27/17576>0\) and the diagonal rate is exactly \(-71/8788<0\), although both second-cumulant rates equal \(3/26\).

## Verification

The standalone script `verify_cumulant.py` checks the full tilted characteristic polynomial against the direct four-by-four generator symbolically, substitutes the perturbative eigenvalue series to obtain the cumulant coefficient, checks the exact rational angular-contrast example, and performs five independent finite-time matrix-exponential moment-chain comparisons. Its output also displays the positive-negative-positive reentrant example. The finite-time comparisons are diagnostics, not proofs of infinite-time limits; the analytic spectral argument and sign inequalities provide those proofs. Execute with Python 3, SymPy, NumPy, and SciPy installed: `python verify_cumulant.py`.

## Relationship to prior work

Mallikarjun and Pal (arXiv:2209.05912, first publicly available 2022-09-13) analyze exactly this four-cardinal-direction velocity model with independent left-turn, right-turn, and reversal rates. Their Sections II.1–II.3 and Appendices A–B give its forward spatial moments, Fourier-Laplace representation, and velocity correlations. In particular, the published large-time fourth *raw* moment is the leading Gaussian \(t^2\) term, whereas its Appendix A provides an implicit generating-function representation rather than the explicit subleading fourth-cumulant slope and its global angular sign classification. The present result does not claim the underlying model, leading diffusion coefficient, or forward propagator as new. It isolates and proves an explicit long-time cumulant phase structure and a nonmonotone reversal-driven boundary. Loewe, Kozhukhov, and Shendruk (arXiv:2305.03663) study 90-degree tumble-turn anisotropy in a different dynamics; their published abstract does not establish this three-rate chiral fourth-cumulant sign theorem, but the full text was not independently available in this assessment.

## Limitations

This is an asymptotic cumulant statement for a single four-state constant-speed particle. For any fixed finite time, the fourth cumulant can have different signs due to transients. No uncertainty bounds are provided for inferring cumulants from finite observations. The complete forward generating function of the same model is already available in the 2022 source, so independent publication-priority assessment should evaluate whether the derived sharp angular/reentrant classification has appeared elsewhere or is implicit in a stronger published asymptotic theorem. Numerical checks confirm examples but do not certify arbitrary real parameters.

## References

1. R. Mallikarjun and A. Pal, *Chiral run-and-tumble walker: transport and optimizing search*, arXiv:2209.05912 (first version 2022-09-13), https://arxiv.org/abs/2209.05912. Sections II.1–II.3 and Appendices A–B.
2. B. Loewe, T. Kozhukhov, and T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, arXiv:2305.03663 (first version 2023-05-05), https://arxiv.org/abs/2305.03663; *Soft Matter* 20 (2024), 1133–1150.
