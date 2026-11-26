# Exact nullspace-risk laws for Gaussian and orthonormalized random-subspace least squares

## Finding

Fix integers \(1\le r\le \ell<d\), a real full-row-rank matrix \(J\in\mathbb R^{r\times d}\), and a nonzero residual \(e\in\mathbb R^r\). Draw \(G\in\mathbb R^{d\times\ell}\) with independent standard-normal entries. Let \(G=QR\) be its thin QR factorization, so \(Q^\mathsf TQ=I_\ell\), and let \(h_*=-J^\dagger e\) be the globally minimum-Euclidean-norm correction satisfying \(Jh=-e\).

Compare two exact solutions in the **same** random subspace \(U=\operatorname{range}(G)=\operatorname{range}(Q)\):

\[
 h_G=-G(JG)^\dagger e,\qquad
 h_Q=-Q(JQ)^\dagger e.
\]

The first minimizes the Gaussian sketch *coefficient* norm, whereas the second minimizes the physical Euclidean *correction* norm. Both solve \(Jh=-e\) almost surely and have the identical row-space component \(h_*\). Put

\[
 \nu=\ell-r+1,\quad m_G=d-r,\quad m_Q=d-\ell,
 \qquad Z_B=\frac{\|h_B-h_*\|_2^2}{\|h_*\|_2^2}
 \quad(B\in\{G,Q\}).
\]

Then the **complete marginal distributions** of their nullspace excess are

\[
 \boxed{Z_G\ \overset{\mathrm d}=\ \frac{\chi^2_{m_G}}{\chi^2_\nu},
 \qquad Z_Q\ \overset{\mathrm d}=\ \frac{\chi^2_{m_Q}}{\chi^2_\nu},}
\]

where the chi-squared variables in each displayed ratio are independent. The two ratios are statements about marginal laws, **not** a claim of a common independent denominator in their actual same-\(G\) coupling.

For either \(B\), with \(m=m_B\), and for every real \(p>0\),

\[
 \boxed{\mathbb E\!\left[\left(\frac{\|h_B-h_*\|_2}{\|h_*\|_2}\right)^p\right]
 =\frac{\Gamma((m+p)/2)\,\Gamma((\nu-p)/2)}
 {\Gamma(m/2)\,\Gamma(\nu/2)}\quad\text{if }0<p<\nu,}
\]

and that moment is infinite for \(p\ge\nu\). In particular, the expected squared correction is finite **if and only if** \(\ell\ge r+2\). In that finite regime,

\[
 \boxed{\frac{\mathbb E\|h_G\|_2^2}{\|h_*\|_2^2}
 =1+\frac{d-r}{\ell-r-1},\qquad
 \frac{\mathbb E\|h_Q\|_2^2}{\|h_*\|_2^2}
 =1+\frac{d-\ell}{\ell-r-1}.}
\]

For every individual full-rank sketch, \(\|h_Q\|_2\le\|h_G\|_2\), because \(h_Q\) has minimum physical norm among all exact corrections in \(U\). Thus, when \(\ell>r\), orthonormalization improves the *expected nullspace squared error* by the exact factor \((d-r)/(d-\ell)>1\) while keeping the span and zero residual unchanged. When \(\ell=r\), the exact correction in the sampled \(r\)-plane is unique and the two rules coincide samplewise.

A nonstatistical witness is

\[
 J=\begin{pmatrix}1&0&0\end{pmatrix},\quad e=-1,\quad
 G=\begin{pmatrix}1&1\\3&0\\0&1\end{pmatrix}.
\]

Here \(h_*=(1,0,0)^\mathsf T\), \(h_G=(1,3/2,1/2)^\mathsf T\), and \(h_Q=(1,3/10,9/10)^\mathsf T\), giving \(\|h_G\|_2^2=7/2\) and \(\|h_Q\|_2^2=19/10\). The two corrections satisfy exactly the same linear constraint and belong to exactly the same two-dimensional space.

## Assumptions and scope

The results concern **one unsafeguarded, exact** subspace least-squares correction. A linear least-squares objective \(x\mapsto\tfrac12\|Jx-b\|_2^2\) yields the setting by choosing \(e=Jx-b\). No noise, regularization, trust radius, rounding, or repeated iteration is included. The full-row-rank and nonzero-residual assumptions exclude respectively an ill-specified right-hand-side constraint and the trivial zero correction. Dimensions obey \(1\le r\le\ell<d\), so \(m_G,m_Q,\nu\) are positive integers. All statements are invariant under the singular values of \(J\) once normalized by \(\|h_*\|_2\).

The terms *Gaussian coefficient-minimal* and *orthonormalized physical-minimal* specify **different tie-breaking rules** for a reduced least-squares model with nonunique minimizers. QR orthonormalization is applied to the same Gaussian realization, not to a separately sampled subspace. A thin QR factorization with orthonormal columns suffices; sign conventions do not matter.

## Proof

**1. Feasibility, row-space component and deterministic ordering.** Since \(JG\) is an \(r\times\ell\) Gaussian linear image with full row rank almost surely, both reduced constraints are feasible. Any \(h\) satisfying \(Jh=-e\) has orthogonal decomposition \(h=h_*+w\) with \(w\in\ker J\), because \(h_*\in\operatorname{range}(J^\mathsf T)\). Thus \(\|h\|_2^2=\|h_*\|_2^2+\|w\|_2^2\). The minimum-norm \(Q\)-coefficient solution gives the physical minimum because \(Q\) is an isometry on its column space. Both corrections lie in \(U\), so \(\|h_Q\|_2\le\|h_G\|_2\). If \(\ell=r\), the restriction \(J|_U\) is invertible almost surely, giving equality of the corrections themselves.

**2. The Gaussian-coefficient rule.** Apply an ambient orthogonal transformation that identifies the row space of \(J\) with the first \(r\) coordinates. Its action on the Gaussian sketch retains independent standard-normal entries. Multiplying the full-row-rank constraint by the inverse of the deterministic row-space restriction of \(J\), write its target as a fixed vector \(a\in\mathbb R^r\) with \(\|a\|_2=\|h_*\|_2\). Partition the transformed sketch as

\[
 G=\begin{pmatrix}A\\B\end{pmatrix},\qquad
 A\in\mathbb R^{r\times\ell},\quad
 B\in\mathbb R^{(d-r)\times\ell}.
\]

The upper and lower blocks are independent standard Gaussian matrices. The coefficient-minimum solution is \(z=A^\mathsf T(AA^\mathsf T)^{-1}a\), and \(w_G=Bz\). Conditional on \(A\), \(w_G/\|z\|_2\) is standard Gaussian in \(\mathbb R^{d-r}\) with a conditional law independent of \(A\). Consequently,

\[
 \frac{\|w_G\|_2^2}{\|a\|_2^2}
 \overset{\mathrm d}=\chi^2_{d-r}\,
 \frac{a^\mathsf T(AA^\mathsf T)^{-1}a}{\|a\|_2^2},
\]

with independent factors. Rotate the rows of \(A\) to make \(a=\|a\|_2 e_1\). If \(u\) is its first Gaussian row and \(V\) contains the other \(r-1\) Gaussian rows, the Schur complement identity gives

\[
 e_1^\mathsf T(AA^\mathsf T)^{-1}e_1
 =\frac{1}{\|P_{\ker V}u\|_2^2}.
\]

Conditionally on \(V\), its denominator is chi-squared with \(\dim\ker V=\ell-r+1=\nu\) degrees of freedom. This proves the first ratio.

**3. The orthonormalized rule.** The sampled \(\ell\)-plane \(U\) is Haar-distributed. Its orthogonal complement is a Haar \((d-\ell)\)-plane, representable as the span of a fresh, standard Gaussian matrix \(N\in\mathbb R^{d\times s}\), \(s=d-\ell\). This fresh representation is used solely to calculate the **marginal** distribution, not to recouple a new subspace to the original \(G\). Partition \(N\) into \(N=(C^\mathsf T,D^\mathsf T)^\mathsf T\), with \(C\in\mathbb R^{r\times s}\) and \(D\in\mathbb R^{q\times s}\), where \(q=d-r\). A feasible correction \((a,w)\) belongs to \(U\) exactly when

\[
 D^\mathsf Tw=-C^\mathsf Ta.
\]

Since \(q\ge s\), \(D\) has full column rank almost surely. Its minimum-norm solution is

\[
 w_Q=-D(D^\mathsf TD)^{-1}C^\mathsf Ta.
\]

The vector \(g=C^\mathsf Ta/\|a\|_2\) is standard Gaussian in \(\mathbb R^s\) independent of \(D\). Hence

\[
 \frac{\|w_Q\|_2^2}{\|a\|_2^2}=g^\mathsf T(D^\mathsf TD)^{-1}g.
\]

Conditional on \(g\ne0\), rotate the \(s\) columns of \(D\) so that \(g\) points along its first coordinate; rotation preserves the standard Gaussian law of \(D\). The same Schur-complement calculation yields \(g^\mathsf T(D^\mathsf TD)^{-1}g\overset{\mathrm d}=\|g\|_2^2/\chi^2_{q-s+1}\), with the denominator independent of \(\|g\|_2\). As \(\|g\|_2^2\sim\chi_s^2\) and \(q-s+1=\ell-r+1\), this proves the second ratio.

**4. Exact moment boundary.** For independent \(X\sim\chi_m^2\) and \(Y\sim\chi_\nu^2\), the Gaussian gamma integrals give

\[
 \mathbb E(X/Y)^{p/2}
 =\frac{\Gamma((m+p)/2)\Gamma((\nu-p)/2)}
 {\Gamma(m/2)\Gamma(\nu/2)}
\]

for \(0<p<\nu\). The integral at \(Y=0\) diverges whenever \(p\ge\nu\). At \(p=2\), its value is \(m/(\nu-2)\) if \(\nu>2\), and infinite otherwise. Substitute \(m=d-r\) or \(m=d-\ell\), use the Pythagorean decomposition from step 1, and obtain the displayed expectations and comparison. All hypotheses and boundary equalities have now been covered.

## Verification

The standalone file `verification/check.py` uses exact rational arithmetic for the displayed deterministic example. It additionally checks both sketch solvers on arbitrary fixed full-row-rank test matrices, checks their shared range component and samplewise minimum-norm ordering, and compares Monte Carlo cumulative frequencies to the stated beta-prime laws with fixed numerical tolerances. It verifies finite gamma-moment identities when applicable. To reproduce, install packages in `verification/requirements.txt` and run `python verification/check.py`. In the recorded execution all **1,742** programmed assertions passed. Finite samples do not prove equality in distribution or divergence of moments; the preceding analytic argument is the proof.

## Relationship to prior work

Cartis and Otemissov (2020), Theorem 3.7 and Corollary 3.9, **already establish** the inverse-chi-squared law and squared expectation for the **minimum reduced coefficient norm** of a Gaussian random embedding. The coefficient part of proof step 2 is therefore an established input, not a newly claimed theorem. The additional result here concerns **physical nullspace displacement**, and, most importantly, the exact **paired Gaussian-basis versus orthonormalized-basis distribution and moment comparison for the same Haar subspace**. The second marginal law uses an independent orthogonal-complement construction and is not supplied by the prior coefficient-norm theorem alone.

Cartis, Fowkes, and Shao (2022) formulate randomized subspace Gauss–Newton, and their longer analysis develops global convergence for safeguarded trust-region and regularized methods. Those analyses do **not** assert that the unregularized pseudoinverse tie-breaking rule considered here is their implemented safeguard; this result neither contradicts nor replaces their guarantees. LeJeune et al. (2022/2024) analyze regularized sketched pseudoinverses, sketch-and-project, and orthogonal versus independent sketches in proportional asymptotics. Their displayed asymptotic operator equivalences are not the finite-dimensional distributions for the same-span pair of exact nullspace corrections.

These comparisons are about implications, not mere title similarity. Mathematical equivalence with an alternative exact inverse-Wishart/Grassmannian formulation remains a residual priority risk, so independent novelty certification is not asserted.

## Limitations

The theorem concerns exact one-step residual interpolation, not global convergence of nonlinear least squares, accumulated iterations, finite-precision QR cost, or any implementation with a trust region or regularization. Divergence of an expectation does not mean that a particular Gaussian draw has infinite length: every correction is finite almost surely. The theorem gives separate marginal laws and a samplewise norm ordering; it does not give a claimed closed form for the **joint** distribution of the two errors. Classical inverse-Wishart and random-embedding distribution lemmas underlie the new comparison, and the originality assessment is same-model rather than independent review.

## References

1. C. Cartis and A. Otemissov, *A dimensionality reduction technique for unconstrained global optimization of functions with low effective dimensionality*, Optimization Online, publicly posted 16 January 2020. https://optimization-online.org/2020/01/7575/ ; Theorem 3.7 and Corollary 3.9.
2. C. Cartis, J. Fowkes, and Z. Shao, *A Randomised Subspace Gauss–Newton Method for Nonlinear Least-Squares*, arXiv:2211.05727, initial arXiv version 10 November 2022. https://arxiv.org/abs/2211.05727
3. C. Cartis, J. Fowkes, and Z. Shao, *Randomised subspace methods for non-convex optimization, with applications to nonlinear least-squares*, arXiv:2211.09873, 2022. https://arxiv.org/abs/2211.09873
4. D. LeJeune, P. Patil, H. Javadi, R. G. Baraniuk, and R. J. Tibshirani, *Asymptotics of the Sketched Pseudoinverse*, arXiv:2211.03751 (2022), SIAM Journal on Mathematics of Data Science 6 (2024), 199–225. https://epubs.siam.org/doi/10.1137/22M1530264
