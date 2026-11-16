# Sharp norm and isolated amplification for squaring composition on a two-atom de Branges–Rovnyak space

## Finding

Let \(b_2(z)=(1+z^2)/2\). Equip the de Branges–Rovnyak space \(\mathcal H(b_2)\) with its **canonical reproducing-kernel norm**, defined by
\[
K_{b_2}(z,w)=\frac{1-b_2(z)\overline{b_2(w)}}{1-z\bar w},\qquad z,w\in\mathbb D.
\]
The self-composition operator \(C_2:\mathcal H(b_2)\to\mathcal H(b_2)\), \((C_2f)(z)=f(z^2)\), is bounded. Its exact operator and essential norms are
\[
\boxed{\ \|C_2\|=\sqrt{\lambda_*}=2.09355577138662\ldots,\qquad
\|C_2\|_{\mathrm{ess}}=2\ },
\]
where \(\lambda_*=4.38297576790623\ldots\) is the **unique real root greater than four** of
\[
\lambda^3-6\lambda^2+8\lambda-4=0.
\]
The operator norm is attained. Set \(r=(\lambda_*-1)^{-1}\) and \(\gamma=(1+r)/(\lambda_*-2)\). An explicit nonzero extremizer is
\[
 f_*(z)=u_*(z^2)+zv_*(z^2),
\]
with
\[
 u_*(\zeta)=\frac1{\lambda_*-2}+
 \frac{(1+\gamma)(\zeta-1)}{2(1-r\zeta)},\qquad
 v_*(\zeta)=\frac{\lambda_*-1}{\lambda_*-2}+
 \frac{(r+\gamma)(\zeta-1)}{2(1-r\zeta)}.
\]
Thus \(\|C_2f_*\|_{\mathcal H(b_2)}^2=\lambda_*\|f_*\|_{\mathcal H(b_2)}^2\). The strict gap between operator norm and essential norm is an isolated spectral amplification caused by the two boundary atoms being mapped to the same atom under squaring.

## Assumptions and scope

The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\); \(H^2\) is the classical coefficient-norm Hardy space. Both source and target are **the same** canonical \(\mathcal H(b_2)\). The assertion is not the known isometry from \(\mathcal H(b_1)\) into \(\mathcal H(b_1\circ z^2)\), where \(b_1(\zeta)=(1+\zeta)/2\). The essential norm is distance to compact linear maps on the given Hilbert space. All identities below hold for every function in these spaces, not only for polynomials.

## Proof

**1. Exact one-atom coordinate model.** Let \(b_1(\zeta)=(1+\zeta)/2\). The space of functions
\[
 h(\zeta)=x+(\zeta-1)g(\zeta),\qquad x\in\mathbb C,\quad g\in H^2,
\]
with squared norm \(2|x|^2+4\|g\|_{H^2}^2\), is an RKHS with kernel
\[
 \frac12+\frac{(\zeta-1)(\overline\eta-1)}{4(1-\zeta\overline\eta)}
 =\frac{1-b_1(\zeta)\overline{b_1(\eta)}}{1-\zeta\overline\eta}.
\]
Hence it is precisely canonical \(\mathcal H(b_1)\), isometrically. The representation is unique: if a nonzero constant were divisible by \(\zeta-1\) in \(H^2\), then \((1-\zeta)^{-1}\) would lie in \(H^2\), which it does not.

**2. Exact two-atom orthogonal splitting.** The kernel identity
\[
 K_{b_2}(z,w)=(1+z\overline w)K_{b_1}(z^2,w^2)
\]
gives an isometric, orthogonal decomposition
\[
 f(z)=u(z^2)+zv(z^2),\qquad
 \|f\|_{\mathcal H(b_2)}^2=\|u\|_{\mathcal H(b_1)}^2+\|v\|_{\mathcal H(b_1)}^2.
\]
Indeed the direct-sum RKHS on the right has exactly the kernel on the left; uniqueness follows from the even/odd Taylor coefficients. This is also the specialization of a known composition-splitting theorem, but here its exact kernel proof fixes the normalization.

**3. A four-block operator for squaring.** Write
\[
 u(\zeta)=x+(\zeta-1)g(\zeta),\quad
 v(\zeta)=y+(\zeta-1)h(\zeta).
\]
The new function \(C_2f(z)=t(z^2)\), where \(t(\xi)=u(\xi^2)+\xi v(\xi^2)\), satisfies \(t(1)=x+y\) and
\[
 \frac{t(\xi)-t(1)}{\xi-1}
 =(1+\xi)g(\xi^2)+\xi(1+\xi)h(\xi^2)+y.
\]
Splitting this quotient into its even and odd Hardy coefficients gives the squared target norm
\[
 2|x+y|^2+4\|g+Sh+y\mathbf1\|_{H^2}^2+4\|g+h\|_{H^2}^2,
\]
where \(S\) is multiplication by the coordinate and \(\mathbf1\) is the constant Hardy unit vector. With input coordinates \((a,b,p,q)=(\sqrt2x,\sqrt2y,2g,2h)\), the operator \(C_2\) is unitarily equivalent to the bounded operator (its target is a closed even subspace)
\[
 L:\mathbb C^2\oplus H^2\oplus H^2\to\mathbb C\oplus H^2\oplus H^2,
 \qquad L(a,b,p,q)=(a+b,\ p+Sq+\sqrt2b\mathbf1,\ p+q).
\]
The target identification preserves all nonzero singular values and the essential norm.

**4. Essential norm.** The difference between \(L\) and the operator \(B(p,q)=(p+Sq,p+q)\), after adding zero finite-dimensional components, has finite rank. The triangle and Cauchy–Schwarz inequalities give \(\|B\|\le2\). Equality is approached by \(p=q\) equal to unit Hardy polynomials supported on long consecutive blocks of large degrees: \(\|Sp-p\|\to0\) while the vectors tend weakly to zero. Thus \(\|B\|_{\mathrm{ess}}=2\) (compact maps send such weakly null sequences to norm-null sequences), hence \(\|L\|_{\mathrm{ess}}=2\).

**5. The unique spectral outlier.** Let \(P_0\) be the rank-one projection in \(H^2\) onto constants. Direct multiplication yields
\[
 LL^*=\begin{pmatrix}
 2&\sqrt2\langle\cdot,\mathbf1\rangle&0\\
 \sqrt2\mathbf1&2I+P_0&I+S\\
 0&I+S^*&2I
 \end{pmatrix}.
\]
The essential spectral supremum of \(LL^*\) is \(4\). Every spectral value strictly greater than \(4\) is an eigenvalue, since \(LL^*\) is a finite-rank perturbation of \(BB^*\) and \(\|BB^*\|\le4\). For an eigenvector \((c,v,w)\) and \(\lambda>4\), the first and third rows imply
\[
 c=\frac{\sqrt2\langle v,\mathbf1\rangle}{\lambda-2},\qquad
 w=\frac{(I+S^*)v}{\lambda-2}.
\]
Substitution into the middle row gives
\[
 \big((\lambda-2)^2-2\big)v=(S+S^*)v+(\lambda-1)P_0v.
\]
Writing \(v=\sum_{n\ge0}v_n\zeta^n\), let \(t=(\lambda-2)^2-2>2\). For \(n\ge1\), \(tv_n=v_{n-1}+v_{n+1}\). Every square-summable solution must be \(v_n=v_0r^n\) for a unique \(0<r<1\), with \(t=r+r^{-1}\). Since \(v_0=0\) would force the entire eigenvector to vanish, the zeroth equation \(tv_0=v_1+(\lambda-1)v_0\) forces \(r^{-1}=\lambda-1\). Equating the two expressions for \(t\) is equivalent to
\[
 \lambda^3-6\lambda^2+8\lambda-4=0.
\]
This polynomial is negative at \(4\), positive at \(5\), and strictly increasing on \([4,\infty)\), so it has exactly one root there. Conversely its root yields \(v(\zeta)=(1-r\zeta)^{-1}\), \(w=\gamma v\), \(c=\sqrt2/(\lambda-2)\), which satisfy all three eigen-equations. Therefore this \(\lambda_*\) is the sole spectral point above \(4\), and \(\|L\|^2=\lambda_*\).

**6. Attainment and the displayed function.** For the eigenvector \((c,v,w)\) in step 5, the nonzero source vector \(L^*(c,v,w)\) attains the norm of \(L\). Since \(S^*v=rv\), its source coordinates are
\[
 (a,b,p,q)=\left(\frac{\sqrt2}{\lambda_*-2},\frac{\sqrt2(\lambda_*-1)}{\lambda_*-2},\ (1+\gamma)v,\ (r+\gamma)v\right).
\]
Converting back to \((x,y,g,h)\) yields exactly \(f_*\) from the finding. Its poles lie strictly outside the closed unit disk, since \(0<r<1\).

## Verification

The accompanying `CHECK.py` (standard-library Python) evaluates the cubic root by bisection, tests the displayed source and target norm formulas using geometric-series coefficients, verifies the candidate eigen-equations on finite Taylor sections, and tests weakly-null block witnesses for the essential-norm mechanism. Run `python CHECK.py` from a directory containing the file. The checker is a finite consistency test; the unlimited-dimensional conclusions follow from the proof above. The kernel identity and \(LL^*\) matrix are exact algebraic identities and can be checked independently without numerical approximation.

## Relationship to prior work

Dellepiane and Seco, *Orthogonal polynomials in de Branges–Rovnyak spaces* (first posted March 3, 2026), establish an isometric monomial composition **between differently indexed spaces**, \(\mathcal H(b)\to\mathcal H(b\circ z^N)\), and an orthogonal decomposition (Theorem 3.9); they do not compute the canonical self-composition norm in the finding. Fricain, Hartmann, Ross and Timotin (2026) study analogous cross-space Littlewood subordination, not the isolated self-norm amplification here. Alhajj and Fricain (2022) characterize boundedness and compactness for rational symbols using an equivalent norm; their Example 4.3(c) has an unbounded squaring operator for a **different symbol with unequal boundary-zero multiplicities**, so it neither contradicts nor implies this result. Fricain, Karaki, Mashreghi and Ostermann (2025) also study qualitative weighted-composition criteria using a noncanonical equivalent norm. The exact cubic, essential-norm gap, and rational extremizer are the present claim, not the known decomposition, boundedness criteria, or general spectral technique.

## Limitations

This is an exact result for \(b_2(z)=(1+z^2)/2\) and the single map \(z\mapsto z^2\) on its own canonical Hilbert space. It does not give norm formulas for all power maps, higher atomic multiplicities, or arbitrary Schur symbols. The essential spectral set beyond its top endpoint is not classified. No claim is made about independence from all historical literature; a differently parameterized older norm computation remains a publication-priority risk. Independent external mathematical review has not been performed.

## References

- E. Dellepiane and D. Seco, *Orthogonal polynomials in de Branges–Rovnyak spaces*, arXiv:2603.03093 (first public version 2026-03-03), especially Section 3.3, Theorems 3.8–3.9. https://arxiv.org/abs/2603.03093
- E. Fricain, A. Hartmann, W. T. Ross and D. Timotin, *Littlewood subordination for de Branges–Rovnyak spaces*, arXiv:2609.10115 (first public version 2026-09-09). https://arxiv.org/abs/2609.10115
- R. Alhajj and E. Fricain, *Composition operators on de Branges–Rovnyak spaces associated to a rational (not inner) function*, arXiv:2211.04864 (2022), especially Sections 3–5 and Example 4.3. https://arxiv.org/abs/2211.04864
- E. Fricain, M. Karaki, J. Mashreghi and M. Ostermann, *Weighted composition operators on de Branges–Rovnyak spaces*, arXiv:2512.15287 (2025), especially Section 1 and its norm choice. https://arxiv.org/abs/2512.15287
