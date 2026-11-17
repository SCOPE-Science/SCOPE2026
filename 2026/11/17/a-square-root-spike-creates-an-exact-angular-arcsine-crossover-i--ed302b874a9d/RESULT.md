# A square-root spike creates an exact angular-arcsine crossover in lecture-hall simplices

## Finding
Consider the one-spike \(s\)-lecture-hall simplex
\[
P_n(a)=\{x\in\mathbb R^n:0\le x_1\le x_2\le\cdots\le x_{n-1}\le x_n/a\le1\},\quad a\in\mathbb Z_{\ge1},\ n\ge2.
\]
The vertices are \(0\) and \(v^{(k)}=\sum_{i=k}^{n-1}e_i+ae_n\) for \(1\le k\le n\) (empty sums are zero). For an independent standard Gaussian objective \(G\), let \(V_n\) be the almost-surely unique exposed vertex, and let its location be \(L_n=\dagger\) if \(V_n=0\), or \(L_n=(n-k)/n\) if \(V_n=v^{(k)}\). The symbol \(\dagger\) is isolated from \([0,1]\).

**Theorem.** For any positive integer sequence \(a_n\) with \(a_n/\sqrt n\to\tau\in[0,\infty)\), the law of \(L_n\) converges weakly to \(\mu_\tau\) on \(\{\dagger\}\sqcup[0,1]\), where
\[
\mu_\tau(\{\dagger\})=\frac{\arctan\tau}{\pi},\qquad
\mu_\tau(dt)=g_\tau(t)\,dt,
\]
\[
g_\tau(t)=\frac1{2\pi\sqrt{t(1-t)}}\left(1+\sqrt{\frac{t}{t+\tau^2}}\right),\quad 0<t<1.
\]
At \(\tau=0\), the fraction under the second square root is \(1\). There are no endpoint atoms in the \([0,1]\) component. Equivalently, for \(0\le u\le1\),
\[
\mu_\tau([0,u])=\frac1\pi\left[\arcsin\sqrt u+\arcsin\sqrt{\frac{u+\tau^2}{1+\tau^2}}-\arctan\tau\right].
\]
For each \(0<\tau<\infty\), conditional on nonzero exposure, the limiting location strictly dominates the standard arcsine law in the usual stochastic order. At \(\tau=0\), the entire limiting mass is arcsine; as \(\tau\to\infty\), the origin mass tends to \(1/2\) and the nonzero component tends to half the arcsine law.

With \(\overline w(K)=\int_{S^{n-1}}(h_K(u)+h_K(-u))\,d\sigma(u)\) for the normalized Haar probability \(\sigma\), the same scale has the exact limiting width
\[
\lim_{n\to\infty}\overline w(P_n(a_n))=\sqrt{\frac2\pi}\left(1+\sqrt{1+\tau^2}\right).
\]

## Assumptions and scope
The metric is the standard Euclidean coordinate metric in \(\mathbb R^n\), not an affine-invariant or intrinsic lattice metric. The Gaussian objective is isotropic and independent of the simplex. Each \(a_n\) is a positive integer; no regularity other than the stated ratio convergence is assumed. The weak convergence treats \(\dagger\) as a separate isolated point, and it describes macroscopic vertex indices, not uniform local probability asymptotics for a specific vertex. A Gaussian objective is equivalent for vertex exposure to a Haar-uniform direction because scaling an objective by a positive factor preserves its maximizer.

## Proof
**Step 1 (exact vertex reduction).** Put \(Z_i=G_{n-i}\) for \(1\le i\le n-1\), define \(S_0=0\), \(S_j=\sum_{i=1}^j Z_i\) and \(M_{n-1}=\max_{0\le j\le n-1}S_j\). Let \(J_{n-1}\) be the almost surely unique maximizing index. The final Gaussian coordinate \(Z=G_n\) is independent of the walk. By direct vertex evaluation,
\[
\langle G,v^{(n-j)}\rangle=a_n Z+S_j,\qquad
h_{P_n(a_n)}(G)=(a_n Z+M_{n-1})_+.
\]
Therefore \(V_n=0\) precisely when \(a_nZ+M_{n-1}<0\); otherwise \(L_n=J_{n-1}/n\). This finite-dimensional identity also proves that ties have probability zero.

**Step 2 (joint Brownian scaling).** Donsker's invariance principle gives convergence of the linearly interpolated process \(S_{\lfloor nt\rfloor}/\sqrt n\) to standard Brownian motion \(B(t)\) on \([0,1]\). Brownian motion has an almost surely unique maximizer, so continuity of the maximum and argmax functionals at such paths gives
\[
(M_{n-1}/\sqrt n,J_{n-1}/n)\ \Longrightarrow\ (M,T),\quad M=\max_{0\le t\le1}B(t),\quad T=\operatorname*{argmax}_{0\le t\le1}B(t).
\]
Joint convergence with independent \(a_nZ/\sqrt n\to\tau Z\) follows from independence. The boundary event \(M+\tau Z=0\) has probability zero, including at \(\tau=0\), since \(M>0\) almost surely. Consequently, the limiting origin mass is \(\Pr(M+\tau Z<0)\), and the nonzero-location measure satisfies \(\mu_\tau(dt)=\mathbb E[\mathbf 1_{\{T\in dt\}}\Phi(M/\tau)]\) for \(\tau>0\); at \(\tau=0\) the weight is one.

**Step 3 (the needed Brownian joint density).** The classical reflection principle implies \(M\overset d=|Y|\) for a standard normal \(Y\). The joint maximum-time law has density
\[
f_{M,T}(m,t)=\frac{m}{\pi t^{3/2}\sqrt{1-t}}\exp\left(-\frac{m^2}{2t}\right),\quad m>0,\quad 0<t<1.
\]
For completeness, the first-passage density at level \(m\) and time \(t\) is \(m\exp(-m^2/(2t))/\sqrt{2\pi t^3}\). After first passage, Brownian survival below an additional height \(\varepsilon\) during the remaining interval \(1-t\) is \(\sqrt{2/\pi}\,\varepsilon/\sqrt{1-t}+o(\varepsilon)\). Their product, after division by \(\varepsilon\) and boundary passage \(\varepsilon\downarrow0\), gives the displayed joint density; this is the standard first-passage/maximum-time factorization. It integrates to the arcsine density \(1/(\pi\sqrt{t(1-t)})\) in \(t\). Thus the only stochastic input beyond Donsker is an established Brownian law, not a new probabilistic assertion.

**Step 4 (explicit angular law).** For \(\tau>0\), integrate the joint density against \(\Phi(m/\tau)\):
\[
g_\tau(t)=\frac1{\pi t^{3/2}\sqrt{1-t}}\int_0^\infty m e^{-m^2/(2t)}\Phi(m/\tau)\,dm.
\]
Integration by parts and an elementary half-Gaussian integral give
\[
\int_0^\infty m e^{-m^2/(2t)}\Phi(m/\tau)\,dm=\frac t2\left(1+\sqrt{\frac t{t+\tau^2}}\right).
\]
This proves the density, and elementary antiderivatives give the asserted cumulative formula. The Gaussian pair \((M,Z)\) has the same distribution as \((|Y|,Z)\); by isotropic planar angle,
\[\Pr(M+\tau Z<0)=\frac{\arctan\tau}{\pi}.\]
The atom and density integrate to one, leaving no endpoint atoms. The ratio \(g_\tau(t)/(1/[\pi\sqrt{t(1-t)}])\) is \(\tfrac12(1+\sqrt{t/(t+\tau^2)})\), strictly increasing in \(t\) for finite positive \(\tau\). Normalizing the nonzero measure therefore gives strict monotone-likelihood-ratio, hence strict first-order stochastic, domination of arcsine.

**Step 5 (Euclidean mean width).** From Step 1 and Doob's \(L^2\) maximal inequality, \(\sup_n\mathbb E[(M_{n-1}/\sqrt n)^2]<\infty\). Since \(a_n/\sqrt n\) stays bounded, the normalized support variables are uniformly integrable and
\[
\frac{\mathbb E h_{P_n(a_n)}(G)}{\sqrt n}\to\mathbb E(\tau Z+M)_+.
\]
The reflection principle yields \(M\overset d=|Y|\). By symmetry, \(\mathbb E|\tau Z+|Y||=\mathbb E|\tau Z+Y|=\sqrt{2/\pi}\sqrt{1+\tau^2}\) and \(\mathbb E(\tau Z+|Y|)=\sqrt{2/\pi}\). Consequently
\[
\mathbb E(\tau Z+M)_+=\frac{1+\sqrt{1+\tau^2}}{\sqrt{2\pi}}.
\]
Writing \(G=RU\), the Gaussian radius \(R\) is independent of the Haar direction \(U\), with \(\mathbb ER/\sqrt n\to1\). Positive homogeneity and symmetry give \(\overline w(P_n)=2\mathbb E h_{P_n}(G)/\mathbb ER\). Combining these identities gives the claimed limit.

## Verification
The standalone file `verification/check_spiked_angles.py` checks the exact vertex-support identity against explicit coordinate vertices for \(n=3,\ldots,14\) and several integer spike lengths; integrates the limiting density for seven spike ratios; and independently simulates four finite-size exposure laws. It uses a reproducible random seed and reports `SPIKED_LECTURE_HALL_PASS analytic_norms=7 finite_vertex_tests=720 stochastic=240000`. The numerical checks are finite and do not establish convergence or prove the Brownian maximum-time identity; all infinite-dimensional inferences are analytically justified above.

## Relationship to prior work
Brändén and Solus introduced the general \(s\)-lecture-hall polytope framework and studied integer decomposition, Gröbner bases, and triangulations; the present one-coordinate terminal spike lies inside that framework but asks a distinct Euclidean normal-cone question. Vysotsky and Zaporozhets discuss the canonical (unspiked) orthoscheme and its intrinsic volumes, crediting Gao and Vitale's earlier formulas; in particular, the unspiked mean-width endpoint is already classically accessible and is **not independently claimed as original**. The joint Brownian maximum/argmax distribution is also classical (Imhof); the asserted contribution is the complete explicitly tilted angular law, including the added vertex atom, for the spiked simplices and the linked sharp width crossover. Neither the unspiked orthoscheme formulas nor the cited lecture-hall algebraic results state this deformation law. Earlier equivalent formulations may exist in unindexed work.

## Limitations
This is an asymptotic macroscopic angular distribution, not an exact finite-dimensional full solid-angle census. The theorem requires one terminal spike and does not treat arbitrary nonconstant lecture-hall weights or different Euclidean coordinate scalings. Known Brownian laws are used, not re-proved from first principles. Bibliographic priority is provisional pending independent full-literature review, and there has been no independent mathematical audit.

## References
1. P. Brändén and L. Solus, *Some Algebraic Properties of Lecture Hall Polytopes*, preprint first posted 2019-11-27, arXiv:1911.12459; https://arxiv.org/abs/1911.12459. Full proceedings manuscript: https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2020/32-Solus.pdf.
2. V. Vysotsky and D. Zaporozhets, *Convex Hulls of Multidimensional Random Walks*, first posted 2015, arXiv:1506.07827, especially Section 4.1 on canonical orthoschemes and Section 4.2 on spherical intrinsic volumes; https://arxiv.org/pdf/1506.07827.
3. J.-P. Imhof, *Density factorizations for Brownian motion, meander and the three-dimensional Bessel process, and applications*, *Journal of Applied Probability* 21 (1984), 500–510, doi:10.2307/3213612; https://doi.org/10.2307/3213612.
