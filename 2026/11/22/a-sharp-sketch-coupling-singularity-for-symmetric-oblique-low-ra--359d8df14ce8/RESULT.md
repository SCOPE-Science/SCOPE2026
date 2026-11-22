# A sharp sketch-coupling singularity for symmetric oblique low-rank tangent projection

## Finding
Let \(d\ge\max\{2,\ell+1\}\), \(\ell\ge1\), and let \(Y=e_1e_1^{\mathsf T}\) and \(Z=e_2e_2^{\mathsf T}\) be matrices in \(\mathbb R^{d\times d}\). In particular, \(Y\) is positive semidefinite of rank one, \(Z\) is positive semidefinite, and the ordinary *orthogonal* tangent projector at \(Y\) annihilates \(Z\). For two correlated real Gaussian sketches with entrywise correlation \(\rho\in[-1,1]\), form the two-sided *oblique* tangent projector and then take its symmetric part. Denote the resulting spurious tangent force by \(S_\rho\). The theorem gives the exact all-order moment threshold:

\[
\boxed{\quad \mathbb E\|S_\rho\|_F^p<\infty\ \Longleftrightarrow\
\begin{cases}p<\ell,&|\rho|<1,\\p<\ell/2,&|\rho|=1,\end{cases}\qquad p>0.\quad}
\]

In particular, independent sketches followed by symmetrization have finite mean-square contamination from **three** rows onward, while perfectly shared sketches require **five** rows. With \(\ell=3\) or \(4\), the mean-square contamination is finite at every strictly imperfect coupling but diverges as \(|\rho|\uparrow1\). Writing \(s=1-\rho^2\), its *sharp divergence orders* are \(\Theta(s^{-1/2})\) at \(\ell=3\) and \(\Theta(\log(1/s))\) at \(\ell=4\). These are order statements, not assertions of an exact leading constant.

For independent sketches (\(\rho=0\)) and \(\ell>2\),
\[
\mathbb E\|S_0\|_F^2=\frac{1}{\ell-2}+\frac{1}{(\ell-2)^2}.
\]
For perfectly shared or sign-reversed sketches (\(|\rho|=1\)) and \(\ell>4\),
\[
\mathbb E\|S_{\pm1}\|_F^2=\frac{2}{\ell-2}+\frac{3}{(\ell-2)(\ell-4)},
\]
which is strictly larger than the independent-sketch value for every \(\ell\ge5\). At perfect sharing, the exact positive-tail law is
\[
\mathbb P(\|S_{\pm1}\|_F>R)\sim
\frac{2\Gamma((\ell+1)/2)}{\ell\sqrt\pi\,\Gamma(\ell/2)}R^{-\ell/2} \quad(R\to\infty).
\]
Thus *perfect* sketch reuse changes the moment-existence exponent discontinuously. All assertions concern the precisely stated rank-one benchmark and its symmetrized oblique projector, not the stability of an entire time integrator.

## Assumptions and scope
Fix integers \(d\ge\max\{2,\ell+1\}\) and \(\ell\ge1\), and a scalar \(\rho\in[-1,1]\). Let \(G_0,G_1\in\mathbb R^{\ell\times d}\) be independent matrices with independent standard normal entries. Set
\[
\Theta=G_0,\qquad \Omega=\rho G_0+\sqrt{1-\rho^2}\,G_1.
\]
Each sketch has standard Gaussian marginals. Their entries in matching positions have correlation \(\rho\), with independence across different positions. This is a *prescribed coupling*, not conditional sampling after inspecting the state. For any realization with \(\Theta e_1\ne0\), \(\Omega e_1\ne0\) (probability one), define
\[
L=e_1(\Theta e_1)^\dagger\Theta,\qquad
R=e_1(\Omega e_1)^\dagger\Omega,
\]
where the dagger is the Moore–Penrose pseudoinverse of the nonzero column. These are the rank-one oblique image projectors of the sketched-Galerkin tangent construction. Let
\[
\Pi_\rho(Z)=LZ+ZR^{\mathsf T}-LZR^{\mathsf T},\quad
S_\rho=\tfrac12\bigl(\Pi_\rho(Z)+\Pi_\rho(Z)^{\mathsf T}\bigr).
\]
Taking the symmetric part is an explicit postprocessing operation for the case \(|\rho|<1\); it is not asserted to coincide with the original unsymmetrized algorithm. For \(|\rho|=1\), the two projectors coincide and postprocessing is redundant. Norms and all probabilities refer to exact arithmetic. No assumption on further time steps or on general right-hand-side fields is made.

## Proof
**1. Exact oblique-tangent reduction.** Put
\[
a=\frac{\langle\Theta e_1,\Theta e_2\rangle}{\|\Theta e_1\|_2^2},\qquad
b=\frac{\langle\Omega e_1,\Omega e_2\rangle}{\|\Omega e_1\|_2^2}.
\]
On the span of \(e_1,e_2\), \(L=\begin{psmallmatrix}1&a\\0&0\end{psmallmatrix}\) and \(R=\begin{psmallmatrix}1&b\\0&0\end{psmallmatrix}\); all other entries of \(\Pi_\rho(Z)\) are zero. Exact multiplication yields
\[
\Pi_\rho(Z)=\begin{pmatrix}-ab&a\\b&0\end{pmatrix},\qquad
S_\rho=\begin{pmatrix}-ab&(a+b)/2\\(a+b)/2&0\end{pmatrix},
\]
and therefore
\[
W_\rho:=\|S_\rho\|_F^2=a^2b^2+\tfrac12(a+b)^2.
\]
The ordinary orthogonal tangent projector at \(Y\), \(PZ+ZP-PZP\) with \(P=e_1e_1^{\mathsf T}\), equals zero. Thus \(W_\rho\) is exactly squared *spurious* tangent-force magnitude for this positive normal input.

**2. Gaussian ratios.** Write \(g=\Theta e_1\), \(h=\Theta e_2\), \(g'=\Omega e_1\), \(h'=\Omega e_2\). Then \((g,g')\) and \((h,h')\) are independent identically distributed centered Gaussian vector pairs with individual covariance \(I_\ell\) and cross covariance \(\rho I_\ell\). Conditional on \((g,g')\), the pair \((a,b)\) is centered Gaussian, with
\[
\operatorname{Var}(a\mid g,g')=\|g\|^{-2},\quad
\operatorname{Var}(b\mid g,g')=\|g'\|^{-2},\quad
\operatorname{Corr}(a,b\mid g,g')=\rho\frac{g^{\mathsf T}g'}{\|g\|\|g'\|}.
\]
Each marginal separately has the standard normal/chi ratio law \(a\stackrel d=G/\chi_\ell\), with independent \(G\sim N(0,1)\) and \(\chi_\ell^2\sim\chi^2_\ell\). The density is
\[
f_\ell(x)=c_\ell(1+x^2)^{-(\ell+1)/2},\qquad
c_\ell=\frac{\Gamma((\ell+1)/2)}{\sqrt\pi\Gamma(\ell/2)}.
\]
In particular \(\mathbb E|a|^q<\infty\) exactly for \(0<q<\ell\).

**3. Sharp joint moments.** Suppose \(|\rho|<1\). The joint Gaussian vector \((g,g')\in\mathbb R^{2\ell}\) has a smooth everywhere-positive nondegenerate density. Conditional Gaussian absolute-product moments obey
\[
c_{p,\rho}\frac1{\|g\|^p\|g'\|^p}
\le\mathbb E[|ab|^p\mid g,g']\le
C_p\frac1{\|g\|^p\|g'\|^p}
\]
for every \(p>0\), where \(c_{p,\rho}>0\): the standardized conditional correlation is in the compact interval \([-|\rho|,|\rho|]\), and the absolute product moment of a nonsingular bivariate normal is continuous and positive there. Joint inverse powers are locally integrable at both coordinate singularities exactly when \(p<\ell\), by radial integration in each \(\ell\)-dimensional factor; Gaussian decay handles infinity. For \(p\ge\ell\), hold \(g'\) in a compact annulus and let \(g\to0\), obtaining divergence. Hence \(\mathbb E|ab|^p<\infty\) exactly when \(p<\ell\). Since \(\|S_\rho\|_F\ge|ab|\) and \(\|S_\rho\|_F\le|ab|+(|a|+|b|)/\sqrt2\), this is exactly the claimed threshold for \(\|S_\rho\|_F\).

For \(|\rho|=1\), \(\Omega=\pm\Theta\), which gives \(b=a\), so \(\|S_{\pm1}\|_F^2=a^4+2a^2\). Its positive \(p\)-moment is finite precisely when \(\mathbb E|a|^{2p}\) is finite, or \(p<\ell/2\). The density above implies \(\mathbb P(|a|>x)\sim(2c_\ell/\ell)x^{-\ell}\). The identity
\[
\|S_{\pm1}\|_F>R\ \Longleftrightarrow\
|a|>\sqrt{\sqrt{1+R^2}-1}
\]
proves the stated sharp tail constant and exponent.

**4. Exact squared-moment endpoints.** For \(\ell>2\), \(\mathbb E a^2=1/(\ell-2)\); for \(\ell>4\), \(\mathbb E a^4=3/[(\ell-2)(\ell-4)]\), by independence of the normal numerator and chi-square denominator. At \(\rho=0\), \(a,b\) are independent and centered, so \(\mathbb E W_0=(\ell-2)^{-2}+(\ell-2)^{-1}\). At \(|\rho|=1\), \(b=a\), yielding the other formula. For \(\ell\ge5\), their difference is
\[
\mathbb EW_{\pm1}-\mathbb EW_0
=\frac{\ell^2-4\ell+6}{(\ell-2)^2(\ell-4)}>0.
\]
For \(\ell=3\) or \(4\), the shared fourth moment diverges while the independent second moment is finite.

**5. Near-perfect coupling, with sharp rate.** For \(\ell>2\) and \(|\rho|<1\), set
\[
I_\ell(\rho)=\mathbb E\frac1{\|g\|^2\|g'\|^2}.
\]
Gaussian fourth-moment identities, conditional on \((g,g')\), give
\[
\mathbb E[a^2b^2\mid g,g']
=\frac{1+2\rho^2\cos^2\angle(g,g')}{\|g\|^2\|g'\|^2}.
\]
Consequently
\[
I_\ell(\rho)\le\mathbb E[a^2b^2]
\le(1+2\rho^2)I_\ell(\rho).
\]
The remaining term \(\tfrac12\mathbb E(a+b)^2\) lies between \(0\) and \(2/(\ell-2)\), by Cauchy–Schwarz. Using \(x^{-1}=\int_0^\infty e^{-tx}\,dt\) and the determinant formula for the Laplace transform of a correlated Gaussian pair yields, with \(s=1-\rho^2\),
\[
I_\ell(\rho)=\int_0^\infty\!\int_0^\infty
[1+2(t+u)+4stu]^{-\ell/2}\,dt\,du
=\frac1{\ell-2}\int_0^\infty
\frac{(1+2u)^{1-\ell/2}}{1+2su}\,du.
\]
At \(\ell=3\) and \(\ell=4\), respectively, this evaluates exactly to
\[
I_3(\rho)=\frac{\arcsin|\rho|}{|\rho|\sqrt{1-\rho^2}},\qquad
I_4(\rho)=\frac{-\log(1-\rho^2)}{4\rho^2},
\]
with continuous values \(I_3(0)=1\) and \(I_4(0)=1/4\). Thus \(I_3\sim\pi/(2\sqrt s)\) and \(I_4\sim\tfrac14\log(1/s)\). The two-sided bounds, together with the bounded additive term, prove the sharp \(\Theta\) orders of \(\mathbb E W_\rho\) claimed above. For \(\ell\ge5\), \(\mathbb E a^4<\infty\) and Cauchy–Schwarz bounds the cross-product moment uniformly over every \(\rho\), so no divergence is possible as \(|\rho|\uparrow1\).

## Verification
The standalone standard-library program `verify.py` checks the exact two-by-two oblique and symmetrized projector identities over rational coefficient grids, endpoint moment identities and their strict ordering, the exact Laplace-integral reductions for \(\ell=3,4\) against independent numerical quadrature, and seeded finite Gaussian realizations for the correlated sketch construction. Run `python3 verify.py` with no external dependencies. The proof above, not finite simulation, establishes all positive moment cutoffs, tail asymptotics, and near-correlation divergence orders.

## Relationship to prior work
Carrel and Grigori (2026, arXiv:2607.03402v1), Section 4 and Lemma 4.2, **already derive the two-sided oblique tangent projector** and establish that perpendicular forcing can create nonorthogonal dynamics; this geometric formula and warning are not claimed as new. Lam, Ceruti and Kressner (2024, arXiv:2409.06384v1), Section 2.3 and Theorem 2, establish moment bounds for a different, independently Gaussian generalized Nyström approximation, not for the coupled oblique tangent projector. The previously published *Residual-spectrum convex ordering and the exact Gaussian sketch failure law* gives a one-sided Gaussian inverse-Wishart/beta-prime law and moment thresholds, whereas *Sharp inverse-moment thresholds and logarithmic tails for two Gaussian tensor sketches* derives heavy tails of independent products of Gaussian/chi ratios in tensor regression. Those standard ratio ingredients and independently multiplied factors are credited and not presented as novel. The new assertion is the **specific correlated two-sided tangent-map moment phase, its sharp shared-sketch cutoff, exact endpoint comparison and near-perfect-coupling blow-up rates**. These do not follow as stated from the cited one-sided Nyström moment or tensor-regression results, because the shared/sketch-correlated ratio pair is not independent. Searches cannot establish complete worldwide priority; unindexed equivalent correlated-projection analyses remain possible.

## Limitations
The result is an exact-arithmetic benchmark at a single fixed rank-one matrix and a single perpendicular rank-one input; it is not a theorem for arbitrary states, higher-rank matrices, nonlinear flows, or repeated integration. The symmetric-part correction for independently drawn sketches is a defined modification and need not coincide with the dynamical tangent projector obtained from an independently sketched Galerkin equation. Sketch-size counts here measure risk for this test force, not total computational cost. The actual sampled oblique force at perfect sharing is symmetric but indefinite almost surely; its symmetric part does not guarantee positive-semidefiniteness of a forward Euler iterate. No optimality over all symmetry-preserving sketch constructions is asserted. Earlier equivalences might exist outside the inspected primary literature.

## References
1. B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1, first public July 3, 2026, especially Lemma 4.2; https://arxiv.org/abs/2607.03402.
2. H. Y. Lam, G. Ceruti, and D. Kressner, *Randomized low-rank Runge–Kutta methods*, arXiv:2409.06384v1, first public September 10, 2024, especially Section 2.3; https://arxiv.org/abs/2409.06384.
3. *Residual-spectrum convex ordering and the exact Gaussian sketch failure law* (published 2026), statement and proof; https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-residual-spectrum-convex-ordering-and-the-exact-gaussian-sketch--23a3fc6123ad.
4. *Sharp inverse-moment thresholds and logarithmic tails for two Gaussian tensor sketches* (published 2026), statement and proof; https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-sharp-inverse-moment-thresholds-and-logarithmic-tails-for-two-ga--d93c1b8eb1d0.
5. Standard multivariate Gaussian/Wick identities, chi-square inverse moments, and Laplace determinant transforms (classical mathematical tools).
