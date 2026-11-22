# Binary-entropy crossover and asymmetric rare-chord localization on near-circular Lamé ovals

## Finding
Let \(C_p=\{(u,v)\in\mathbb R^2:|u|^p+|v|^p=1\}\), with \(p>1\), and take \(X_p,Y_p\) independently uniformly with respect to **Euclidean arclength** on \(C_p\). All distances below are Euclidean. Write \(L_p=\|X_p-Y_p\|_2\) and let \(D_p=\operatorname{diam}(C_p)\). For any fixed \(\lambda\in\mathbb R\), any fixed \(x>0\), and \(p_\varepsilon=2+\lambda\varepsilon\), define the continuous binary entropy
\[
H(\alpha)=-\cos^2\alpha\log(\cos^2\alpha)-\sin^2\alpha\log(\sin^2\alpha),\qquad 0\log0:=0,
\]
and the nonnegative angular penalty
\[
G_\lambda(\alpha)=\frac{\max(\lambda,0)\log2-\lambda H(\alpha)}2.
\]
Then the exact **near-Euclidean crossover** is
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr\{D_{p_\varepsilon}-L_{p_\varepsilon}\le x\varepsilon\}}{\sqrt\varepsilon}
=F_\lambda(x):=\frac1{\pi^2}\int_0^{2\pi}\sqrt{(x-G_\lambda(\alpha))_+}\,d\alpha.}
\]
Here \(y_+=\max(y,0)\). The normalization at the circle is \(F_0(x)=2\sqrt{x}/\pi\). The angular localization and tail amplitudes of this crossover are sharply asymmetric:
\[
\boxed{F_\lambda(x)\sim\frac{2x}{\pi\sqrt\lambda}\quad(\lambda\to+\infty),\qquad
F_{-L}(x)\sim\frac{2\sqrt2\,x}{\pi\sqrt{L\log L}}\quad(L\to+\infty).}
\]
These two limits are limits of the **crossover profile**, not assertions of a uniform asymptotic with diverging \(\lambda\) and \(\varepsilon\) simultaneously.

There is also a joint marked limit. Write the polar arguments of the ordered pair as \(\alpha\in[0,2\pi)\) and \(\alpha+\pi+\beta\) modulo \(2\pi\), with \(\beta\in(-\pi,\pi]\). Conditional on \(D_{p_\varepsilon}-L_{p_\varepsilon}\le x\varepsilon\), the pair \((\alpha,\beta/\sqrt\varepsilon)\) converges to the constant-density probability law on
\[
\mathcal A_{\lambda,x}=\{(a,z):0\le a<2\pi,\ z^2/4+G_\lambda(a)\le x\}.
\]
In particular, the limiting first-point direction has density proportional to \(\sqrt{(x-G_\lambda(a))_+}\); given that direction, the rescaled antipodal mismatch is uniform on the corresponding interval \([-2\sqrt{x-G_\lambda(a)},\,2\sqrt{x-G_\lambda(a)}]\) whenever that interval has positive length. Thus large positive \(\lambda\) localizes at four diagonal directions, while large negative \(\lambda\) localizes at four coordinate axes on the smaller logarithmic scale.

## Assumptions and scope
This is a fixed-dimensional planar result. \(\varepsilon\to0\) with \(x>0\) and \(\lambda\in\mathbb R\) held fixed; eventually \(p_\varepsilon>1\). Sampling is independent and normalized by the full **Euclidean** perimeter, not cone measure, polar-angle measure, or invariant random-line measure. The angular parameters in the marked law are defined modulo \(2\pi\); the event localizes near antipodal points, so the signed \(\beta\) is unambiguous for sufficiently small deficits. The diameters have exact values
\[
D_p=\begin{cases}2,&1<p\le2,\\ 2^{3/2-1/p},&p\ge2.\end{cases}
\]
Both expressions equal two at \(p=2\). Natural logarithms are used. No uniformity is claimed when the crossover parameter diverges together with the small deficit.

## Proof
**1. Radial parametrization and exact diameter.** Write \(e_\alpha=(\cos\alpha,\sin\alpha)\) and
\[
r_p(\alpha)=(|\cos\alpha|^p+|\sin\alpha|^p)^{-1/p},\qquad R_p(\alpha)=r_p(\alpha)e_\alpha.
\]
The Euclidean norm of a point on \(C_p\) is the radial function. By the power-mean comparison (or a one-variable Lagrange multiplier calculation), \(\max_\alpha r_p(\alpha)=1\) when \(p\le2\), attained on the four axes for \(p<2\); for \(p\ge2\) it equals \(2^{1/2-1/p}\), attained at the four diagonal directions for \(p>2\). Since \(C_p\) is centrally symmetric, its Euclidean diameter is twice its maximum Euclidean radius, proving the displayed formula.

**2. Uniform first variations.** Put \(p=2+\delta\) and \(c=|\cos\alpha|\), \(s=|\sin\alpha|\). The functions \(t^p\log^k t\) with \(k\le2\), extended by zero at \(t=0\), are uniformly bounded on \([0,1]\) for \(p\) near two. Taylor expansion in \(\delta\), uniformly in \(\alpha\), gives
\[
c^{2+\delta}+s^{2+\delta}=1+\delta(c^2\log c+s^2\log s)+O(\delta^2)
=1-\frac\delta2 H(\alpha)+O(\delta^2),
\]
so
\[
r_{2+\delta}(\alpha)=1+\frac\delta4 H(\alpha)+O(\delta^2).
\]
Differentiating the exact radial expression with respect to \(\alpha\) and using the same uniform boundedness of \(t^p\log t\) proves \(\sup_\alpha|r'_{2+\delta}(\alpha)|=O(|\delta|)\). Consequently, the arclength density \(s_p(\alpha)=\sqrt{r_p(\alpha)^2+r'_p(\alpha)^2}\) satisfies \(\sup_\alpha|s_{2+\delta}(\alpha)-1|\to0\), and the total perimeter \(P_{2+\delta}=\int_0^{2\pi}s_{2+\delta}(\alpha)d\alpha\to2\pi\). No second angular derivative of the entropy is used: it is singular at the axes.

**3. Uniform antipodal chord deficit and localization.** Write the two polar arguments as \(\alpha\) and \(\alpha+\pi+\beta\). Central symmetry gives \(r_p(\alpha+\pi+\beta)=r_p(\alpha+\beta)\). From the cosine rule,
\[
\|R_p(\alpha)-R_p(\alpha+\pi+\beta)\|_2
=\sqrt{r_p(\alpha)^2+r_p(\alpha+\beta)^2+2r_p(\alpha)r_p(\alpha+\beta)\cos\beta}.
\]
For bounded \(z=\beta/\sqrt\varepsilon\) and \(\delta=\lambda\varepsilon\), the radial first variation and uniform continuity of \(H\) yield, uniformly in \(\alpha,z\),
\[
\|R_{p_\varepsilon}(\alpha)-R_{p_\varepsilon}(\alpha+\pi+\sqrt\varepsilon z)\|_2
=2+\frac{\lambda\varepsilon}2H(\alpha)-\frac{\varepsilon z^2}4+o(\varepsilon).
\]
The exact diameter satisfies \(D_{p_\varepsilon}=2+(\max(\lambda,0)\log2)\varepsilon/2+O(\varepsilon^2)\). Subtracting yields
\[
D_{p_\varepsilon}-L_{p_\varepsilon}
=\varepsilon\{z^2/4+G_\lambda(\alpha)\}+o(\varepsilon)
\]
uniformly on bounded \(z\). To justify restriction to that window, note that \(r_{p_\varepsilon}\to1\) uniformly, and the chord distance of the unit circle at angle difference \(\pi+\beta\) is \(2|\cos(\beta/2)|\). Away from \(\beta=0\) it is uniformly less than two; near zero, because \(r_{p_\varepsilon}=1+O(\varepsilon)\), a deficit at most \(x\varepsilon\) forces \(1-\cos(\beta/2)=O(\varepsilon)\), hence \(|\beta|\le C_{x,\lambda}\sqrt\varepsilon\). This establishes localization with no missed contact pairs.

**4. Probability and marked convergence.** The joint density in polar angles is
\(s_{p_\varepsilon}(\alpha)s_{p_\varepsilon}(\alpha+\pi+\beta)/P_{p_\varepsilon}^2\), uniformly converging to \((2\pi)^{-2}\). Set \(\beta=\sqrt\varepsilon z\); step 3 restricts integration to a fixed bounded region, and the indicator converges almost everywhere to \(\mathbf1\{z^2/4+G_\lambda(\alpha)\le x\}\). The boundary has two-dimensional Lebesgue measure zero because for each \(\alpha\) it contains at most two \(z\)-values. Dominated convergence gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-1/2}\Pr(D-L\le x\varepsilon)
=\frac1{4\pi^2}\int_0^{2\pi}\int_{\mathbb R}\mathbf1\{z^2/4+G_\lambda(\alpha)\le x\}\,dz\,d\alpha
=\frac1{\pi^2}\int_0^{2\pi}\sqrt{(x-G_\lambda(\alpha))_+}\,d\alpha.
\]
For every bounded continuous test function of \((\alpha,z)\), inserting it into the same integral proves the marked convergence. The normalizing integral is positive for every \(x>0\), since the angular penalty has zeros. When \(\lambda=0\), the integral is \(2\sqrt{x}/\pi\), consistent with the exact circle law \(\Pr(L\ge2-\varepsilon)=\frac2\pi\arccos(1-\varepsilon/2)\).

**5. Distinct far-localization mechanisms.** Binary entropy has exactly four maxima at diagonal angles and four minima at axes on a full turn. At each diagonal \(a_0\),
\[
H(a_0+u)=\log2-2u^2+O(u^4),
\]
so for positive \(\lambda\), the penalty is \(\lambda u^2+O(\lambda u^4)\). With the substitution \(u=\sqrt{x/\lambda}\,v\), each diagonal contributes \(\pi x/(2\sqrt\lambda)\) to the unnormalized angular integral. Four diagonals give the first far-profile asymptotic.

At each axis \(a_0\),
\[
H(a_0+u)=u^2\log(1/u^2)+O(u^2).
\]
For \(\lambda=-L<0\), the penalty equals \(Lu^2\log(1/u^2)/2+O(Lu^2)\). Substitute \(u=\sqrt{2x/(L\log L)}\,v\). On compact \(v\)-sets the penalty converges to \(xv^2\), while elementary monotonicity of binary entropy on \([0,\pi/4]\) bounds the support to compact \(v\)-sets in this scale. Each axis contributes \(\pi x/\sqrt{2L\log L}\) to the angular integral; summing four axes and dividing by \(\pi^2\) yields \(2\sqrt2 x/(\pi\sqrt{L\log L})\). These rescalings also prove the asserted respective angular localization of the marked laws when the profile parameter subsequently tends to the indicated infinities.

## Verification
The standalone executable `verify_entropy_chords.py` independently computes the profile by split quadrature, and the actual finite-deficit near-antipodal event from the exact Lamé radial parametrization and exact Euclidean arclength density. It checks \(\lambda=-4,0,+4\), two deficit scales, finite and asymptotic profile constants, and symmetry/entropy identities. The packaged checker runs with Python 3, NumPy and SciPy and terminates with `ALL_CHECKS_PASSED 20`. The finite computations are diagnostics only; the infinite limit and sharp coefficients are consequences of the proof.

## Relationship to prior work
Mayer and Molchanov (2006, arXiv:math/0605289) analyze extremal interpoint distances for random samples in the **Euclidean unit ball**, including isotropic boundary distributions; their symmetry assumption does not supply the present changing Lamé-oval angular entropy penalty. Matsuura (2014) determines differential-geometric curvature properties of Lamé curves, not near-diametral two-point probability crossovers. Bäsel (2012) treats invariant-line chords and independent **area-uniform interior points of regular polygons**, which is a distinct body and sampling law.

Related indexed geometric studies establish the near-circle long-chord crossover for **Euclidean-motion-invariant random lines** on smooth support-function perturbations and the near-circle random-**boundary-endpoint** law for **ellipses**. Their generic leading angular integral and normalization motivated a precise comparison. The present deformation is a Lamé exponent perturbation rather than elliptic semiaxis perturbation: its first variation is binary entropy, whose second angular derivative diverges at the coordinate axes. The logarithmically corrected \(\lambda\to-\infty\) profile and the two-sided localized mark law are not statements of those works, nor does the fixed-exponent invariant-line \(\ell_p\) chord theorem imply them. A separate known random-width entropy transition for \(\ell_p\) balls concerns one direction, not a pair of arclength-sampled boundary points.

The originality assessment is based on statement-level comparisons of accessible published results and primary sources. Broader unsurveyed work on variable-geometry random distances may contain an equivalent formulation; lack of a matching indexed title is not proof of novelty.

## Limitations
The claimed limit keeps \(\lambda\) and \(x\) fixed before \(\varepsilon\downarrow0\), and its far-profile asymptotics subsequently send \(\lambda\) to infinity. This does not establish one uniform double limit with arbitrarily diverging \(\lambda(\varepsilon)\), fixed-non-Euclidean-exponent tail coefficients, or a full chord-length distribution. The marked limit uses ordered boundary points; interchange symmetry is automatic. The angular density is Euclidean arclength, not the cone measure, and no interior-point or invariant-line interpretation is asserted. Historical priority and independent mathematical validation remain open.

## References
1. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:math/0605289, first submitted 2006-05-11, https://arxiv.org/abs/math/0605289 .
2. M. Matsuura, *Asymptotic Behaviour of the Maximum Curvature of Lamé Curves*, Journal for Geometry and Graphics 18 (2014), 45–59, https://www.heldermann-verlag.de/jgg/jgg18/j18h1mats.pdf .
3. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first submitted 2012-04-12, https://arxiv.org/abs/1204.2707 .
4. *A universal near-circle crossover for long invariant-line chords*, related published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-universal-near-circle-crossover-for-long-invariant-line-chords--c14c19482cd1 .
5. *A logarithmic near-circle crossover for nearly diametral chords of ellipse boundaries*, related published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-logarithmic-near-circle-crossover-for-nearly-diametral-chords--4a4af7408362 .
6. *Singular-curvature extreme-chord tails and Dirichlet endpoint limits for Euclidean \(\ell_p\) balls*, related published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-singular-curvature-extreme-chord-tails-and-dirichlet-endpoint-li--5bac0f506ab7 .
