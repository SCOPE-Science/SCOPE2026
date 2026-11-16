# Exact-degree double Fourier sphere energy has an elliptic azimuthal profile

## Finding

For a double Fourier sphere (DFS) coordinate pullback, the complete squared singular spectrum of the pullback **on each exact spherical-harmonic degree** has a natural azimuthal labeling. Its large-degree profile is an elliptic integral, with a sharp constant lower energy bound and a logarithmically divergent zonal sector.

Write \(d_{\ell,m}\) for squared singular energy at spherical degree \(\ell\) and azimuthal index \(-\ell\le m\le\ell\). For every sequence \(\ell\to\infty\) with \(|m|/\ell\to\alpha>0\),

\[
\lim d_{\ell,m}=\frac{4}{\pi^2}K\!\left(\sqrt{1-\alpha^2}\right),\quad K(k)=\int_0^{\pi/2}\frac{du}{\sqrt{1-k^2\sin^2u}}.
\]

When \(|m|/\ell\to0\), the squared energy instead diverges. At finite degrees \(d_{\ell,m}>2/\pi\), while the infimum over all degrees and orders is exactly \(2/\pi\). The specific zonal and sectoral energies obey

\[
 d_{\ell,0}=\frac4{\pi^2}\log\ell+O(1),\qquad
 d_{\ell,\ell}=(2\ell+1)\left[\frac{\binom{2\ell}{\ell}}{4^\ell}\right]^2\longrightarrow\frac2\pi.
\]

The result gives the sharp lower and logarithmically growing upper scales of the DFS energy distortion on high-degree spherical modes; no claim is made about the finite-degree ordering of all intermediate orders.

## Assumptions and scope

Equip the unit sphere \(\mathbb S^2\) with probability surface measure \(d\omega/(4\pi)\) and the parameter torus \(\mathbb T^2=(\mathbb R/2\pi\mathbb Z)^2\) with Haar probability measure \(d\lambda\,d\theta/(4\pi^2)\). The DFS map is

\[
\Phi(\lambda,\theta)=(\cos\lambda\sin\theta,\sin\lambda\sin\theta,\cos\theta),\quad (Tf)(\lambda,\theta)=f(\Phi(\lambda,\theta)).
\]

Here \(\theta\) runs through the full doubled interval \([0,2\pi)\). Let \(\mathcal H_\ell\) be the degree-\(\ell\) spherical-harmonic eigenspace, with its spherical probability-measure norm, and let \(Y_{\ell,m}\) be its orthonormal complex azimuthal basis. Define

\[
 p_{\ell,m}(x)=\left[\frac{2\ell+1}{2}\frac{(\ell-|m|)!}{(\ell+|m|)!}\right]^{1/2}P_\ell^{|m|}(x),
 \qquad \int_{-1}^1p_{\ell,m}(x)^2\,dx=1.
\]

All assertions concern \(\ell\in\mathbb N_0\) and \(|m|\le\ell\); no boundedness of \(T\) on the whole unweighted spherical \(L^2\) space is asserted.

## Proof

**Step 1 (exact singular diagonal).** In spherical polar coordinates \(Y_{\ell,m}\) is proportional to \(e^{im\lambda}P_\ell^{|m|}(\cos\theta)\), so distinct azimuthal orders remain orthogonal under torus integration. With the stated probability normalizations and the doubled latitude interval,

\[
 d_{\ell,m}=\|TY_{\ell,m}\|^2_{L^2(\mathbb T^2)}
 =\frac{2\ell+1}{\pi}\frac{(\ell-|m|)!}{(\ell+|m|)!}
 \int_0^\pi P_\ell^{|m|}(\cos\theta)^2\,d\theta
 =\frac2\pi\int_{-1}^1\frac{p_{\ell,m}(x)^2}{\sqrt{1-x^2}}\,dx.
\]

Since \((1-x^2)^{-1/2}>1\) except at one point, every finite \(d_{\ell,m}>2/\pi\). The sequence of sectoral harmonics in Step 4 tends to the bound, proving sharpness.

**Step 2 (weak semiclassical limit).** For fixed order \(m\), the normalized associated Legendre functions satisfy the symmetric Jacobi recurrence

\[
 x p_{\ell,m}=a_{\ell+1,m}p_{\ell+1,m}+a_{\ell,m}p_{\ell-1,m},
 \qquad a_{j,m}=\sqrt{\frac{j^2-m^2}{(2j-1)(2j+1)}}.
\]

At the lower endpoint \(p_{m-1,m}=0\). For any degree sequence \(\ell\to\infty\), \(|m|/\ell\to\alpha\in[0,1]\), the coefficients on each fixed finite window about \(\ell\) tend to \(c=\sqrt{1-\alpha^2}/2\), wherever the window exists. If \(\alpha<1\), the lower endpoint is eventually outside every fixed window, and the Jacobi path expansion gives

\[
\int_{-1}^1x^{2k}p_{\ell,m}(x)^2\,dx\to\binom{2k}{k}c^{2k},
\quad\int_{-1}^1x^{2k+1}p_{\ell,m}(x)^2\,dx=0.
\]

For \(\alpha=1\), every nonconstant even moment tends to zero by the same recurrence and the vanishing coefficient bound. The limiting probability law is the arcsine measure of radius \(b=\sqrt{1-\alpha^2}\):

\[
 p_{\ell,m}(x)^2dx\;\Longrightarrow\;
 \frac{\boldsymbol1_{|x|<b}\,dx}{\pi\sqrt{b^2-x^2}}
\]

for \(b>0\), and the point mass at zero for \(b=0\). Because all measures are supported on \([-1,1]\), polynomial moments determine weak convergence.

**Step 3 (the singular Jacobian).** The spherical eigenvalue identity and the nonnegative azimuthal part of the gradient energy yield

\[
 m^2\int_{-1}^1\frac{p_{\ell,m}(x)^2}{1-x^2}\,dx\le\ell(\ell+1).
\]

For \(\alpha>0\) this bounds the inverse-square-root weight in \(L^2(p_{\ell,m}^2dx)\). The arcsine support lies strictly inside \([-1,1]\), so the weak convergence and Cauchy--Schwarz imply that the weighted mass near the two endpoints tends to zero. The singular weight is therefore uniformly integrable and

\[
\lim d_{\ell,m}=\frac2\pi\int\frac{\mu_\alpha(dx)}{\sqrt{1-x^2}}
 =\frac4{\pi^2}\int_0^{\pi/2}\frac{du}{\sqrt{1-(1-\alpha^2)\sin^2u}}.
\]

For \(\alpha=0\), the limiting arcsine measure fills \([-1,1]\), and its integral against \((1-x^2)^{-1/2}\) diverges. Apply weak convergence first to each bounded continuous truncation of this weight, and then let the truncation increase, to obtain \(d_{\ell,m}\to+\infty\).

**Step 4 (exact endpoint sectors).** The formula \(P_\ell^\ell(x)=(-1)^\ell(2\ell-1)!!(1-x^2)^{\ell/2}\) and the beta integral give

\[
 d_{\ell,\ell}=(2\ell+1)\left[\binom{2\ell}{\ell}4^{-\ell}\right]^2.
\]

Stirling's formula gives its limit \(2/\pi\). For \(m=0\), use the Legendre generating function

\[
 (1-2t\cos\theta+t^2)^{-1/2}
 =(1-te^{i\theta})^{-1/2}(1-te^{-i\theta})^{-1/2}.
\]

Writing \(b_r=\binom{2r}{r}/4^r\), coefficient extraction yields

\[
 P_\ell(\cos\theta)=\sum_{r=0}^\ell b_r b_{\ell-r}\,e^{i(2r-\ell)\theta}.
\]

Parseval on a full period (equivalently twice the half period) gives the exact finite identity

\[
 d_{\ell,0}=(2\ell+1)\sum_{r=0}^\ell(b_r b_{\ell-r})^2.
\]

The estimate \(b_r^2=1/(\pi r)+O(r^{-2})\) as \(r\to\infty\), after separating the two endpoints, yields

\[
\sum_{r=0}^\ell b_r^2b_{\ell-r}^2=\frac{2\log\ell}{\pi^2\ell}+O(\ell^{-1}),
\qquad d_{\ell,0}=\frac4{\pi^2}\log\ell+O(1).
\]

All steps are identities or compactness/energy arguments for the stated full index range; no numerical extrapolation enters their proofs.

## Verification

The standalone program `verify_profile.py` independently evaluates normalized spherical harmonics by numerical integration and compares the zonal and sectoral energies against the exact formulas for all \(0\le\ell\le44\), testing all allowed orders. It also checks the elliptic scaling at multiple degree values and reports 1,149 successful comparisons. Run `python3 verify_profile.py` with Python 3, NumPy and SciPy. The finite evaluations check normalization and formulas; they do not certify the infinite-degree limits.

## Relationship to prior work

Mildenberger and Quellmalz (first public preprint, 12 August 2021; journal publication 2022) establish the DFS pullback, its weighted torus Fourier analysis and approximation properties. Their Theorem 5.4 explains the relevant Jacobian weight, while their Sobolev counterexample concerns a different whole-space regularity question. The present statement instead computes sharp exact-degree spherical-harmonic pullback energies, their fixed-azimuthal-ratio elliptic limit and their divergent zonal growth.

The Jacobi recurrence and its arcsine-limit mechanism are classical; general arcsine theorems such as Saigo--Sako are background, not claimed as new. Dunster's associated Legendre asymptotic theory is also prior background. A 1938 paper of Bailey on integrals of associated Legendre functions could contain related special-function identities, but its full content was inaccessible during this assessment and priority of the exact formulas is provisional.

## Limitations

The result is a **restricted exact-degree** singular-value theorem, not a global boundedness assertion for the DFS map. No classification of which intermediate azimuthal order maximizes the finite-degree energy, no finite-degree optimal condition number, and no new bound on full spherical Sobolev spaces is claimed. The computation is an independent finite corroboration, not an infinite proof. Equivalent formulas may be derivable from older special-function asymptotics or integrals and require independent priority checking. Independent mathematical audit has not been performed.

## References

- S. Mildenberger and M. Quellmalz, *Approximation Properties of the Double Fourier Sphere Method*, arXiv:2108.05662 (12 August 2021); *Journal of Fourier Analysis and Applications* **28**, 31 (2022), https://doi.org/10.1007/s00041-022-09928-4.
- H. Saigo and H. Sako, *The Arcsine Law and an Asymptotic Behavior of Orthogonal Polynomials*, arXiv:1407.0792 (2014), https://doi.org/10.4171/aihpd/34.
- T. M. Dunster, *Uniform asymptotic expansions for associated Legendre functions of large order*, *Proceedings of the Royal Society of Edinburgh A* **133** (2003), https://doi.org/10.1017/S0308210500002687.
- W. N. Bailey, *Some Integral Formulae Involving Associated Legendre Functions*, *Journal of the London Mathematical Society* **13** (1938), https://doi.org/10.1112/jlms/s1-13.3.167.
