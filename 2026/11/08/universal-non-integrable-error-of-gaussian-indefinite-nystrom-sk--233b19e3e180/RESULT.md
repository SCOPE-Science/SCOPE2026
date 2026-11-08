# Universal non-integrable error of Gaussian indefinite Nyström sketches

## Finding

**Theorem (all nontrivial Gaussian sketch sizes).** Let \(A\in\mathbb R^{n\times n}\) be real, symmetric, invertible and indefinite, with \(n\ge2\). For every integer \(1\le k<n\), let \(G\in\mathbb R^{n\times k}\) have independent standard real Gaussian entries and define the *unmodified* symmetric Nyström approximation

\[
\widehat A=AG(G^{\mathsf T}AG)^{-1}G^{\mathsf T}A.
\]

The inverse exists almost surely. Although \(\widehat A\) and its residual are finite almost surely, for every real \(p\ge1\) and each of the spectral, Frobenius, and nuclear norms,

\[
\mathbb E\lVert A-\widehat A\rVert^p=+\infty.
\]

**Theorem (exact near-full law).** When \(k=n-1\), choose a Haar-uniform unit vector \(u\) perpendicular to the columns of \(G\). Almost surely,

\[
A-\widehat A=\frac{uu^{\mathsf T}}{u^{\mathsf T}A^{-1}u},\qquad
R:=\lVert A-\widehat A\rVert_2=\lVert A-\widehat A\rVert_{\mathrm F}=\lVert A-\widehat A\rVert_*=
\left|u^{\mathsf T}A^{-1}u\right|^{-1}.
\]

Let \(f_A\) be the density near zero of the spherical quadratic form \(q=u^{\mathsf T}A^{-1}u\). It is continuous and strictly positive at zero, with the exact surface-integral coefficient

\[
f_A(0)=\frac{1}{|\mathbb S^{n-1}|}\int_{\{u\in\mathbb S^{n-1}:u^{\mathsf T}A^{-1}u=0\}}
\frac{d\mathcal H^{n-2}(u)}{2\lVert A^{-1}u\rVert_2}>0.
\]

Consequently

\[
\Pr(R>t)\sim\frac{2f_A(0)}{t}\quad(t\to\infty),\qquad
\mathbb E R^p<\infty\ \Longleftrightarrow\ 0<p<1,
\]

and \(\mathbb E\min(R,T)\sim2f_A(0)\log T\) as \(T\to\infty\).

**Exact two-level spectrum.** If \(A\) has positive eigenvalue \(a>0\) of multiplicity \(r\ge1\) and negative eigenvalue \(-b<0\) of multiplicity \(s\ge1\), where \(r+s=n\), then for \(U\sim\operatorname{Beta}(r/2,s/2)\),

\[
R\stackrel{d}{=}\frac{ab}{|(a+b)U-a|}.
\]

For \(t>\max(a,b)\), writing \(F_{r/2,s/2}\) for the beta distribution function,

\[
\Pr(R>t)=F_{r/2,s/2}\!\left(\frac{a+ab/t}{a+b}\right)
-F_{r/2,s/2}\!\left(\frac{a-ab/t}{a+b}\right).
\]

Its sharp tail constant is

\[
\lim_{t\to\infty}t\Pr(R>t)=
\frac{2ab}{(a+b)\operatorname B(r/2,s/2)}
\left(\frac a{a+b}\right)^{r/2-1}
\left(\frac b{a+b}\right)^{s/2-1}.
\]

For \(a=b=1\), \(r=s=1\), this becomes the particularly transparent exact survival function \(\Pr(R>t)=2\arcsin(1/t)/\pi\) for \(t>1\). For fixed \(a,b\), letting \(r=1\), \(s=n-1\) and \(n\to\infty\) gives \(R\to b\) in probability even though \(\mathbb E R=+\infty\) at every dimension.

## Assumptions and scope

Everything concerns the real Gaussian, unregularized core-inverse method in exact arithmetic. No distributional assumption is made on the eigenvectors, and all nonzero positive and negative eigenvalues may have arbitrary multiplicity and magnitude. The sketch has exactly \(k\) columns with \(1\le k<n\). The almost-sure inverse uses the ordinary inverse; the Moore–Penrose pseudoinverse agrees on its full-measure domain. Spectral, Frobenius and nuclear norms are the usual unitarily invariant norms. The exact beta law assumes the additional two-eigenvalue form and the near-full sketch size.

## Proof

**1. Almost-sure invertibility.** The polynomial \(G\mapsto\det(G^{\mathsf T}AG)\) is not identically zero. Indeed choose the columns as \(k\) distinct eigenvectors of the invertible \(A\), for which the core is diagonal with nonzero diagonal entries. Its zero set has Lebesgue measure zero, hence Gaussian probability zero.

**2. The one-column singularity lemma.** Let \(B\) be any real symmetric indefinite matrix, possibly singular, and let \(z\) have a full-dimensional density positive on every nonempty open set (in particular a standard Gaussian). Then, for every \(p\ge1\),

\[
\mathbb E\left\|B-\frac{(Bz)(Bz)^{\mathsf T}}{z^{\mathsf T}Bz}\right\|_2^p=\infty.
\]

Choose unit positive and negative eigenvectors of \(B\) with eigenvalues \(\lambda_+>0\) and \(\lambda_-<0\). A nonzero linear combination \(z_0\) can be chosen such that \(z_0^{\mathsf T}Bz_0=0\), while \(Bz_0\neq0\). The gradient of the scalar denominator \(\phi(z)=z^{\mathsf T}Bz\) at \(z_0\) is \(2Bz_0\neq0\). The inverse function theorem therefore supplies smooth local coordinates \((t,w)\) about \(z_0\) with \(t=\phi(z)\), Jacobian bounded above and below, a positive density bound and \(\|Bz\|_2^2\ge c>0\). The rank-one term has spectral norm \(\|Bz\|_2^2/|t|\). By the reverse triangle inequality its difference from \(B\) has norm at least \(c/|t|-\|B\|_2\), which is at least \(c/(2|t|)\) on a small punctured neighborhood. Integration in \(t\) contains \(\int_{-\delta}^{\delta}|t|^{-p}\,dt=\infty\). The zero-denominator event itself has measure zero by the nonzero-polynomial argument.

**3. Every sketch dimension.** The case \(k=1\) is Step 2 applied to \(B=A\). For \(2\le k<n\), write \(G=[Y,z]\), where \(Y\) contains \(k-1\) independent Gaussian columns and \(z\) is independent standard Gaussian. On the event that \(W=Y^{\mathsf T}AY\) is invertible, define

\[
B=A-AYW^{-1}Y^{\mathsf T}A.
\]

Block Gaussian elimination (the scalar Schur complement is \(z^{\mathsf T}Bz\)) yields the **exact** residual identity

\[
A-AG(G^{\mathsf T}AG)^{-1}G^{\mathsf T}A
=B-\frac{(Bz)(Bz)^{\mathsf T}}{z^{\mathsf T}Bz}.
\]

There is an open set of \(Y\) with positive Gaussian probability for which \(B\) is indefinite. To see this, take the columns of a reference \(Y_0\) to be \(k-1\) distinct orthonormal eigenvectors of \(A\), **omitting at least one positive and one negative eigenvector**; this is possible because \(k-1\le n-2\). At \(Y_0\), the core is nonsingular and \(B\) acts as \(A\) on the span of the omitted eigenvectors and as zero on the selected ones. Thus \(B\) has eigenvalues of both signs. Core invertibility and both strict signs persist in a neighborhood by continuity. Conditional on every \(Y\) in that neighborhood, Step 2 makes the \(p\)-th spectral-error moment infinite. Tonelli's theorem then gives an infinite unconditional moment. Since \(\|E\|_{\mathrm F}\ge\|E\|_2\) and \(\|E\|_*\ge\|E\|_2\), the same holds for the other stated norms.

**4. Near-full residual identity.** When \(k=n-1\), the sketch columns span a hyperplane almost surely. Let \(u\) be a unit normal. The symmetric residual \(E=A-\widehat A\) annihilates \(G\), so necessarily \(E=\gamma uu^{\mathsf T}\) for some real scalar \(\gamma\). Independently, \(EA^{-1}u=u\), because the factor containing \(G^{\mathsf T}u\) vanishes. Hence \(\gamma(u^{\mathsf T}A^{-1}u)=1\), proving \(\gamma=1/q(u)\) whenever the core is invertible. Rotational invariance of the Gaussian sketch makes the unoriented unit normal Haar-uniform. This proves the residual and norm formulas.

**5. Sharp tail and moments.** For \(q(u)=u^{\mathsf T}A^{-1}u\), indefiniteness guarantees that its zero set \(Z\) on the unit sphere is nonempty. At every point of \(Z\), the spherical gradient is \(\nabla_{\mathbb S}q=2(A^{-1}u-q(u)u)=2A^{-1}u\neq0\) because \(A\) is invertible. Thus zero is a regular value. For \(n\ge2\), \(Z\) is a compact nonempty smooth manifold of dimension \(n-2\) (a finite collection of points when \(n=2\)). The spherical coarea formula yields a continuous density at zero with the stated strictly positive integral. Consequently \(\Pr(|q|<\epsilon)=2f_A(0)\epsilon+o(\epsilon)\). Substituting \(\epsilon=1/t\) gives the tail. The layer-cake moment formula \(\mathbb E R^p=p\int_0^\infty t^{p-1}\Pr(R>t)\,dt\) gives the exact moment threshold; \(R\) is also bounded below away from zero because \(|q|\le\|A^{-1}\|_2\). The truncated-first-moment asymptotic follows from \(\mathbb E\min(R,T)=\int_0^T\Pr(R>t)\,dt\).

**6. Two-eigenvalue law.** The squared projection of a Haar unit vector onto an \(r\)-dimensional eigenspace is \(U\sim\operatorname{Beta}(r/2,s/2)\). Substituting \(q=U/a-(1-U)/b\) proves the exact transformation and survival law. The strictly positive beta density at the interior zero \(U=a/(a+b)\) gives the displayed constant by a symmetric interval of half-width \(ab/[(a+b)t]\). For \(r=1,s=n-1\), \(\mathbb E U=1/n\), hence \(U\to0\) in probability, yielding \(R\to b\) in probability; infinite expectations in each fixed dimension still follow from the moment theorem.

## Verification

The standalone script `verify.py` checks random test matrices and sketch ranks by direct core inversion and the near-full hyperplane identity, algebraic block-Schur formulas, the beta survival probabilities at high precision, the exact two-dimensional arcsine law, and tail constants. `verify_output.txt` records the observed result. These finite calculations support but do not replace the proofs of the infinite-moment assertions, the positive-probability open event, or the coarea expansion.

To reproduce from these files, install compatible versions of Python, NumPy, SymPy and mpmath, then run `python verify.py` in the same directory.

## Relationship to prior work

Park and Nakatsukasa [1] already show by an explicit \(2\times2\) indefinite matrix that *unmodified* Nyström approximation can be arbitrarily unstable; that deterministic phenomenon is **not new here**. Their analysis and stability results concern truncated/projected-core variants and bounds on suitably restricted events. The claim assessed here is stronger and distributional for the unmodified Gaussian method: a universal non-integrable expected error **at every sketch size**, its exact near-full rank-one residual law, and a sharp reciprocal tail. Hillier [2] studies the density of a spherical quadratic form, so the existence and possible computation of its density are **not claimed as new**; the Nyström identity and algorithmic all-sketch consequences are what is assessed. Schur-complement identities have a long history [3], and the algebraic identity alone does not imply the Gaussian heavy-tail/moment classification without the indefinite isotropic-cone argument.

## Limitations

The result concerns only unregularized, untruncated, Gaussian sketches and exact arithmetic; it does not characterize finite-precision implementations, regularized cores, shifted sketches, other sketch distributions, or singular input matrices. The exact reciprocal-tail coefficient is established for the near-full sketch; the proof for general smaller sketches establishes non-integrability, not an exact leading tail coefficient. The classical spherical quadratic-form density literature may give an alternative route to the near-full distribution. Independent mathematical validation and a specialist precedence review have not been performed.

## References

1. Taejun Park and Yuji Nakatsukasa, *Randomized low-rank approximation for symmetric indefinite matrices*, arXiv:2212.01127 (first public version 2 December 2022). https://arxiv.org/abs/2212.01127 .
2. Grant Hillier, *The Density of a Quadratic Form in a Vector Uniformly Distributed on the n-Sphere*, *Econometric Theory* 17 (2001), 1–28, https://doi.org/10.1017/S026646660117101X .
3. Diane Valérie Ouellette, *Schur Complements and Statistics*, *Linear Algebra and its Applications* 36 (1981), 187–295, https://doi.org/10.1016/0024-3795(81)90232-9 .
