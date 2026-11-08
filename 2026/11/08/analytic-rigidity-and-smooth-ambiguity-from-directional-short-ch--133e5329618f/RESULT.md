# Analytic rigidity and smooth ambiguity from directional short-chord tails

## Finding
Consider a planar compact convex body \(K\) with nonempty interior, a strictly convex \(C^2\) boundary, and everywhere positive curvature. A random unoriented line is sampled from translation- and rotation-invariant line measure \(d\theta\,dp\), with normal angle \(\theta\in[0,\pi)\) and signed normal offset \(p\), conditioned on intersecting \(K\). Let \(\Theta\) be the normal angle and \(L\) the length of the intersection chord. Let \(P\) be the known perimeter. Define the following two **direction-resolved** data functions, which can be obtained from the line experiment:
\[
g_K(\theta)=\frac{d\Pr(\Theta\in d\theta)}{d\theta},\qquad
b_K(\theta)=\lim_{t\downarrow0}\frac{1}{t^2}
\frac{d\Pr(\Theta\in d\theta,\ L\le t)}{d\theta}.
\]
Here probabilities are for the conditionally sampled line. Write \(h(\theta)\) for the support function, \(\rho(\theta)=h(\theta)+h''(\theta)>0\) for its radius of curvature in the outward normal direction, and \(w(\theta)=h(\theta)+h(\theta+\pi)\) for width. Then, with \(\kappa=1/\rho\),
\[
\boxed{g_K(\theta)=\frac{w(\theta)}{P},\qquad
b_K(\theta)=\frac{1}{8P}
\left(\frac{1}{\rho(\theta)}+\frac{1}{\rho(\theta+\pi)}\right).}
\tag{1}
\]

**Theorem (analytic rigidity and a sharp smooth-class obstruction).** If two such bodies have the **same known perimeter** and real-analytic support functions, equality of the two directional data functions \(g,b\) for all normal directions implies that the bodies differ by a translation or a point reflection followed by a translation. No full chord-length distribution is needed. In contrast, there exist two strictly positively curved \(C^\infty\) **constant-width** bodies of the same perimeter, not related by translation or point reflection, which have identical \(g\) and \(b\). Hence the assertion fails in the unrestricted smooth class.

These statements are about labelled normal directions, not the scalar chord-length distribution after forgetting directions. They do not assert rigidity from a single scalar probability.

## Assumptions and scope
The line measure is parametrized by \(n_\theta=(\cos\theta,\sin\theta)\) and \(\ell_{\theta,p}=\{x:\langle x,n_\theta\rangle=p\}\); opposite normal parametrizations represent the same line. Conditioning on intersection gives a total line measure \(P=\int_0^\pi w(\theta)\,d\theta\) (Cauchy's perimeter identity). Angle labels are fixed in the ambient coordinate system. The perimeter is assumed known in physical units: a conditional distribution alone does not supply its value. The analytic assertion compares bodies both having analytic positive-curvature support functions. Point reflection means \(K\mapsto -K\), up to translation, rather than arbitrary mirror reflection across an axis.

## Proof
**1. Short-chord limit.** Fix \(\theta\). Almost all intersecting offsets form the interval \((-h(\theta+\pi),h(\theta))\), whose length is \(w(\theta)\). Near the upper supporting line, choose tangent/normal coordinates with inward support-line displacement \(\delta>0\). A positive-curvature \(C^2\) boundary has the local parabolic expansion \(y=x^2/(2\rho(\theta))+o(x^2)\); the chord at displacement \(\delta\) therefore has length
\[
L=2\sqrt{2\rho(\theta)\delta}\,(1+o(1)),\qquad
\delta=\frac{L^2}{8\rho(\theta)}(1+o(1)).
\]
The lower supporting line contributes the same expression with \(\theta+\pi\). Away from these two endpoints the chord length has a positive minimum for fixed \(\theta\), so no other offset contributes when \(t\downarrow0\). Consequently the offset measure of chords of length at most \(t\) is
\[
\frac{t^2}{8}\left(\frac1{\rho(\theta)}+\frac1{\rho(\theta+\pi)}\right)+o(t^2).
\]
The curvature bounds and compactness give uniformity in \(\theta\). Divide by total conditioned Crofton measure \(P\) to prove (1).

**2. Recover the unordered antipodal radii.** Since \(P\) is known, \(g\) gives \(w=Pg\). The support equation gives
\[
S(\theta):=w(\theta)+w''(\theta)=\rho(\theta)+\rho(\theta+\pi),\qquad
H(\theta):=8P b(\theta)=\rho(\theta)^{-1}+\rho(\theta+\pi)^{-1}.
\]
Both are strictly positive. The product of the antipodal radii is \(S/H\), so these radii are precisely the two positive roots, counted with multiplicity, of
\[
\boxed{z^2-S(\theta)z+\frac{S(\theta)}{H(\theta)}=0.}\tag{2}
\]
Thus \(g,b,P\) recover the unordered pair at every angle, but not its labelling a priori.

**3. Analytic labelling rigidity.** Suppose \(\rho_1,\rho_2\) correspond to two real-analytic candidate bodies with identical data. By (2), their antipodal sums coincide and their unordered pairs coincide at every \(\theta\). Put \(d_j(\theta)=\rho_j(\theta)-\rho_j(\theta+\pi)\). Then \(d_1^2=d_2^2\), hence
\[
(d_1-d_2)(d_1+d_2)\equiv0.
\]
On the connected analytic circle, the product of two real-analytic functions vanishes identically only if one factor does. Therefore \(d_2=d_1\) globally or \(d_2=-d_1\) globally; this also covers the identically zero case. Together with equality of sums, \(\rho_2=\rho_1\) or \(\rho_2(\theta)=\rho_1(\theta+\pi)\) for every \(\theta\). In the first case the support-function difference solves \(q''+q=0\), giving \(q=A\cos\theta+B\sin\theta\), which represents translation. In the second case \(h_2(\theta)-h_1(\theta+\pi)\) solves the same equation, giving point reflection plus translation. This proves analytic uniqueness.

**4. Two smooth, inequivalent constant-width bodies with identical data.** Choose two disjoint intervals \(I_1,I_2\) compactly contained in \((0,\pi)\), and choose nonzero \(\psi_j\in C_c^\infty(I_j)\). Set \(\phi_j=\psi_j''+\psi_j\) on \([0,\pi]\). Integration by parts shows, for each \(j\),
\[
\int_0^\pi\phi_j(\theta)\cos\theta\,d\theta=
\int_0^\pi\phi_j(\theta)\sin\theta\,d\theta=0.
\]
Define \(f_+=\phi_1+\phi_2\) and \(f_-=\phi_1-\phi_2\) on \([0,\pi]\), and extend both smoothly to \([0,2\pi]\) by \(f_\pm(\theta+\pi)=-f_\pm(\theta)\). The compact supports make the extensions smooth; their first Fourier harmonics vanish. Thus, for any fixed \(R>0\) and all sufficiently small \(\varepsilon>0\), the two positive \(C^\infty\) functions
\[
\rho_\pm(\theta)=R+\varepsilon f_\pm(\theta)
\]
are radii of curvature of strictly convex closed curves: the periodic support equations \(h_\pm''+h_\pm=\rho_\pm\) are solvable because the two first-harmonic compatibility integrals vanish. These curves have perimeter \(2\pi R\) and width \(2R\), since the antipodal radius sums are \(2R\) and the \(\pi\)-periodic width equation has only the constant solution \(w=2R\).

The disjoint supports imply \(f_+^2=f_-^2\) pointwise. Hence
\[
\frac1{\rho_+(\theta)}+\frac1{\rho_+(\theta+\pi)}
=\frac{2R}{R^2-\varepsilon^2f_+(\theta)^2}
=\frac{2R}{R^2-\varepsilon^2f_-(\theta)^2}
=\frac1{\rho_-(\theta)}+\frac1{\rho_-(\theta+\pi)}.
\]
Equation (1) now shows both bodies have identical directional data. They cannot be translates (their radius functions differ on \(I_2\)) or point reflections (the radii differ from antipodal ones on \(I_1\)). This proves the smooth obstruction. \(\square\)

## Verification
The standalone Python 3 program `verify_short_chord.py` checks the exact small-chord offset formula for three ellipses against the curvature expression, checks the quadratic recovery formula for 2,049 normal directions of a noncircular analytic body, and checks first-Fourier compatibility, positivity, the squared-perturbation identity, and identical inverse-curvature sums for a constructed compact-bump smooth pair. The observed output was `SHORT_CHORD_VERIFY_OK ellipses=3 analytic_pairing=2049 smooth_counterexample=5001`. The analytic uniqueness and infinite family construction are proved symbolically above; finite sampled checks are not substituted for infinite proofs.

## Relationship to prior work
Bianchi, Segala and Volčič [1] prove reconstruction of strictly positively curved planar bodies from the **entire two-dimensional covariogram** and show that it determines unordered antipodal curvatures. Averkov and Bianchi [2] show certain **neighborhood restrictions** of the covariogram are sufficient in specified classes; their hypotheses retain function values over open sets, not merely the angular marginal and one short-chord coefficient. Averkov and Bianchi [3] settle the full planar covariogram inverse problem. Full direction-dependent chord distributions are known to encode this full covariogram. All of those stronger-data theorems and the standard support-width identities are acknowledged, not claimed as new. The new claim here is an exact, minimal **two-function short-chord truncation** sufficient for real-analytic shape reconstruction, coupled to an explicit strictly positively curved smooth ambiguity showing the regularity boundary. In particular, full covariogram uniqueness is compatible with our smooth counterexample: the examples share only the specified truncated data, not the complete covariogram.

## Limitations
The perimeter is provided externally; recovery of an unknown perimeter from the two normalized functions alone is not asserted. Both compared bodies are assumed real analytic for uniqueness. For arbitrary \(C^\infty\) bodies, nonuniqueness is established, but the complete smooth equivalence-class classification is not claimed. The construction is not a counterexample to full covariogram or full orientation-resolved chord-distribution uniqueness. Existing historical priority of this exact truncated-data theorem remains subject to independent literature review.

## References
1. G. Bianchi, F. Segala and A. Volčič, *The solution of the covariogram problem for plane \(C_+^2\) convex bodies*, Journal of Differential Geometry **60** (2002), 177–198, DOI:10.4310/jdg/1090351101; original PDF: https://www.maths.tcd.ie/EMIS/journals/NYJM/jdg/p/2002/60-2-1.pdf.
2. G. Averkov and G. Bianchi, *Retrieving Convex Bodies from Restricted Covariogram Functions*, first arXiv release 28 February 2007, arXiv:math/0702892v1, https://arxiv.org/abs/math/0702892; Advances in Applied Probability **39** (2007), 613–629.
3. G. Averkov and G. Bianchi, *Confirmation of Matheron's conjecture on the covariogram of a planar convex body*, Journal of the European Mathematical Society **11** (2009), 1187–1202, DOI:10.4171/JEMS/179, https://ems.press/journals/jems/articles/1922.
