# The half-power spectral transition and Coulomb edge law for Bergman Toeplitz perturbations

## Finding

Let \(A^2(\mathbb D)\) be the analytic Bergman space of the unit disk with normalized area measure. For \(s>0\) and \(C\in\mathbb C\), consider
\[
B_{s,C}=T_{z+C|z|^s}.
\]
Define the selfadjoint zero-diagonal Jacobi operator \(J_s\) on \(\ell^2(\mathbb N_0)\) by its strictly positive off-diagonal entries
\[
b_n(s)=\frac{s(n+1)\sqrt{(n+2)(n+3)}}{2(n+1+s/2)(n+2+s/2)},\qquad n\geq0.
\]
As in the established shift-plus-diagonal reduction [2,3], \(B_{s,C}\) is hyponormal exactly when \(|C|\,\|J_s\|\leq1\).

**Sharp phase and spectral edge.** For all real \(s\geq1/2\),
\[
\sigma(J_s)=[-s,s],\qquad \|J_s\|=s,\qquad
B_{s,C}\text{ hyponormal}\iff |C|\leq1/s.
\]
For every \(0<s<1/2\), \(J_s\) has infinitely many simple eigenvalues strictly above \(s\), with their negatives strictly below \(-s\); there are no other points of its spectrum outside \([-s,s]\). Write its positive exterior eigenvalues, in decreasing order, as \(\lambda_1(s)>\lambda_2(s)>\cdots>s\). Then
\[
\lambda_j(s)-s\sim \frac{s(1/2-s)^2}{2j^2}\qquad(j\to\infty).
\]
Equivalently, the positive-exterior counting function has the sharp law
\[
N_s(\varepsilon):=\#\{\lambda\in\sigma_{\rm p}(J_s):\lambda>s+\varepsilon\}
\sim (1/2-s)\sqrt{\frac{s}{2\varepsilon}}
\qquad(\varepsilon\downarrow0).
\]
The negative exterior spectrum has the identical counting function. Thus \(\|J_s\|>s\) and the sharp hyponormality window is strictly smaller than \(|C|\leq1/s\) throughout \(0<s<1/2\). No explicit elementary formula for \(\|J_s\|\) is claimed in that regime.

## Assumptions and scope

We use \(T_\phi f=P(\phi f)\), where \(P:L^2(\mathbb D,dA)\to A^2(\mathbb D)\) is orthogonal projection and \(dA\) is normalized area measure. All assertions are for \(s>0\), not for arbitrary radial weights or general weighted Bergman measures; the spectral and counting results concern the exact normalizing Jacobi operator \(J_s\) above. The parameter \(C\) is any complex number, including zero. Eigenvalues outside the essential spectral band are counted with multiplicity. The asymptotic symbols are for fixed \(s\), with no uniformity claimed as \(s\to0\) or \(s\to1/2\).

## Proof

**1. Exact operator reduction.** With \(e_n(z)=\sqrt{n+1}z^n\), direct Bergman integration gives
\[
T_z e_n=\sqrt{\frac{n+1}{n+2}}\,e_{n+1},\qquad
T_{|z|^s}e_n=\frac{n+1}{n+1+s/2}\,e_n.
\]
For the unilateral Bergman shift \(S=T_z\), its positive selfcommutator is diagonal:
\[
\Delta=[S^*,S],\qquad \Delta e_n=\frac{e_n}{(n+1)(n+2)}.
\]
The radial Toeplitz operator is selfadjoint and diagonal, hence has zero selfcommutator. The two cross terms in \([B_{s,C}^*,B_{s,C}]\), after normalization by \(\Delta^{-1/2}\) on finitely supported vectors, have off-diagonal absolute values \(|C|b_n(s)\). A diagonal unitary removes the constant phase of \(C\). Positivity of the commutator is therefore equivalent to positivity of \(I+|C|J_s\), with the harmless choice of sign absorbed into the alternating unitary. Since \(Ue_n=(-1)^ne_n\) satisfies \(UJ_sU=-J_s\), its spectrum is symmetric and this positivity condition is equivalent to \(|C|\|J_s\|\leq1\). Boundedness of \(J_s\) justifies extending from finitely supported vectors. The general reduction is also recorded in [2,3].

**2. Essential band and the exact no-outlier range.** Put \(a=s/2\). One obtains
\[
b_n(s)=a\left(1+\frac{1/2-s}{n}+O_s(n^{-2})\right)
\qquad(n\to\infty).
\]
Consequently, \(J_s\) is a compact perturbation of the free half-line Jacobi matrix with constant bonds \(a\), whose spectrum is \([-2a,2a]=[-s,s]\). Thus \(\sigma_{\rm ess}(J_s)=[-s,s]\) for every \(s>0\).

When \(s\geq1/2\), put \(t=s/2\geq1/4\). For each \(n\geq0\), the inequality \(b_n(s)\leq a\) is equivalent to
\[
(n+1+t)^2(n+2+t)^2\geq(n+1)^2(n+2)(n+3).
\]
The left side increases with \(t\). At \(t=1/4\), the difference is exactly
\[
\frac{224n^2+688n+489}{256}>0.
\]
Hence \(b_n(s)<a\) for every finite \(n\) whenever \(s\geq1/2\). The elementary estimate
\[
|\langle u,J_su\rangle|\leq 2\sup_n b_n(s)\,\|u\|^2\leq s\|u\|^2
\]
gives \(\|J_s\|\leq s\); the essential band gives the reverse inequality and proves the first assertion.

**3. Exact form of the attractive tail.** Suppose \(0<s<1/2\), and put \(c=1/2-s>0\), \(g=2ac=sc>0\). For finitely supported \(u\), the following identity holds exactly, with \(V_0=b_0-2a\) and \(V_n=b_{n-1}+b_n-2a\) for \(n\geq1\):
\[
\langle u,(J_s-sI)u\rangle
=-\sum_{n\geq0}b_n|u_{n+1}-u_n|^2
+\sum_{n\geq0}V_n|u_n|^2.
\]
The first-order bond asymptotics yield
\[
b_n=a+O_s(n^{-1}),\qquad
V_n=\frac gn+O_s(n^{-2}),\qquad n\to\infty.
\]
Thus the upper-band problem is a one-dimensional discrete kinetic energy with an attractive Coulomb-type positive potential \(g/n\). The boundary term at \(n=0\) and removing any fixed initial segment only change eigenvalue counts by a bounded amount.

**4. Counting for the discrete Coulomb comparison operator.** We prove the needed counting fact, rather than treating finite sections as a proof. On \(\ell^2\) over sufficiently large positive integers, let \(H_{a,g}\) have quadratic form
\[
\langle u,H_{a,g}u\rangle
=-a\sum_n|u_{n+1}-u_n|^2+\sum_n\frac gn|u_n|^2,
\qquad a,g>0.
\]
Its number \(N_{a,g}(\varepsilon)\) of eigenvalues greater than \(\varepsilon>0\) satisfies
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,N_{a,g}(\varepsilon)
=\frac{g}{2\sqrt a}.
\]
Indeed, for fixed \(\eta>0\), partition the integer half-line into geometric blocks whose endpoints grow by the factor \(1+\eta\), terminating at a constant multiple of \(g/\varepsilon\). Restricting or decoupling the bonds between blocks changes the eigenvalue count by at most twice the number of cuts, which is \(O_\eta(\log(1/\varepsilon))\). On each block, bound the potential \(g/n\) from above and below by its endpoint values. For a block of length \(L\) with constant potential \(V\), the discrete Dirichlet Laplacian has exactly
\[
\frac L\pi\arccos\left(1-\frac{(V-\varepsilon)_+}{2a}\right)+O(1)
\]
eigenvalues exceeding \(\varepsilon\), provided the initial index is large enough to ensure \(V<2a\). This follows from its exact eigenvalues \(-2a[1-\cos(\pi k/(L+1))]\). Uniformly in such blocks,
\[
\arccos(1-h)=\sqrt{2h}\,(1+O(h)),\qquad 0\leq h\ll1.
\]
The geometric upper and lower sums bound the integral
\[
\frac1{\pi\sqrt a}\int_0^{g/\varepsilon}\sqrt{\left(\frac gx-\varepsilon\right)_+}\,dx
=\frac g{2\sqrt{a\varepsilon}}.
\]
The omitted fixed initial segment contributes at most its finite dimension; the final tail with \(g/n\leq\varepsilon\) is nonpositive after shifting by \(\varepsilon\) and contributes no positive eigenvalues, except for a bounded cut error. After multiplying by \(\sqrt\varepsilon\), the boundary and cut errors vanish. Sending the initial index to infinity and \(\eta\) to zero squeezes the normalized upper and lower sums to the displayed constant. This establishes the comparison fact with all limiting operations specified.

**5. Transferring the sharp constant to \(J_s\).** For every \(\delta\in(0,1)\), take a sufficiently large fixed initial index so that on the remaining tail
\[
(1-\delta)a\leq b_n\leq(1+\delta)a,
\qquad
\frac{(1-\delta)g}{n}\leq V_n\leq\frac{(1+\delta)g}{n}.
\]
The min–max principle, using the form identity of Step 3, sandwiches the exterior eigenvalue counts between those of \(H_{(1+\delta)a,(1-\delta)g}\) and \(H_{(1-\delta)a,(1+\delta)g}\), up to a fixed finite-rank boundary correction. Applying Step 4 and then sending \(\delta\downarrow0\) yields
\[
\lim_{\varepsilon\downarrow0}\sqrt\varepsilon\,N_s(\varepsilon)
=\frac g{2\sqrt a}=c\sqrt a
=(1/2-s)\sqrt{s/2}.
\]
In particular, there are infinitely many eigenvalues above the essential band. All are simple: the three-term Jacobi recurrence uniquely determines an eigenvector from its initial component since every bond is nonzero. Symmetry under \(U\) yields the negative exterior eigenvalues. The eigenvalue law follows by inverting the monotone counting asymptotic, giving \(\lambda_j(s)-s\sim s(1/2-s)^2/(2j^2)\). Therefore \(\|J_s\|>s\), completing the hyponormality conclusion.

## Verification

The standalone standard-library script `checker.py` tests the exact algebraic polynomial identity, individual bond bounds at and above the threshold, the sign of finite-section exterior eigenvalue counts via Sturm inertia, and the first-order bond coefficient. It produces 4,631 successful checks on replay. Numerical finite sections are supplementary only; the counting theorem is proved by Steps 3–5, not inferred from a finite matrix.

## Relationship to prior work

Simanek [1] established the necessary constraint \(|C|\leq1/s\) for the exact symbols here and proved its sufficiency for \(s\geq2\). Simanek [2] and Le–Simanek [3] gave the **full implicit** Jacobi-norm criterion, which is used rather than claimed anew. This result identifies a sharp explicit transition at \(s=1/2\) and the detailed spectral accumulation above and below the essential band, including its leading constant. General Jacobi oscillation results such as Luef–Teschl [4] concern finiteness versus infiniteness of exterior eigenvalues, not this explicit Toeplitz classification and counting coefficient. Kim–Lee [5] study other nonharmonic monomial-symbol hyponormality conditions. The first-order bond correction is visible by expansion of the published exact formula, but does not by itself give the all-index norm cap or the sharp exterior eigenvalue count.

## Limitations

The small-exponent threshold for \(|C|\) is expressed as \(1/\|J_s\|\) and has no closed form here; its strict separation from \(1/s\) is proved. The counting and individual eigenvalue asymptotics hold at each fixed \(0<s<1/2\), not uniformly in the parameter. No claim about the spectral type inside \([-s,s]\), or the distribution at joint \(s\)-and-energy limits, is made. The result has undergone self-review only, not independent mathematical validation. Unindexed equivalent spectral results are a residual historical-priority risk.

## References

[1] Brian Simanek, *Hyponormal Toeplitz Operators with Non-Harmonic Algebraic Symbol*, arXiv:1807.00356v1, 1 July 2018. https://arxiv.org/abs/1807.00356.

[2] Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2001.07823v1, 22 January 2020. https://arxiv.org/abs/2001.07823.

[3] Trieu Le and Brian Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330v1, 16 March 2020. https://arxiv.org/abs/2003.07330.

[4] Franz Luef and Gerald Teschl, *On the Finiteness of the Number of Eigenvalues of Jacobi Operators Below the Essential Spectrum*, *J. Difference Equations and Applications* 10 (2004), 299–307. https://arxiv.org/abs/math/0109213.

[5] Sumin Kim and Jongrak Lee, *Remarks on Hyponormal Toeplitz Operators with Nonharmonic Symbols*, *Open Mathematics* 21 (2023), article 20230114. https://doi.org/10.1515/math-2023-0114.
