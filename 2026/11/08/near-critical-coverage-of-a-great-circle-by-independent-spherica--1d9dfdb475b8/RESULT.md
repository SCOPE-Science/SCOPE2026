# Near-critical coverage of a great circle by independent spherical caps: a sharp onset and a Beta–Dirichlet shape law

## Finding

Fix integers \(m\ge 2\) and \(n\ge 3\), a great circle \(E\subset S^m\), and independent, surface-uniform centers \(X_1,\ldots,X_n\in S^m\). Each center defines a closed geodesic cap of common angular radius \(w\). Write \(P_{m,n}(w)\) for the probability that the union covers **all of the fixed great circle** \(E\), not the whole sphere. Put \(w_0=\pi/n\). Then \(P_{m,n}(w)=0\) for \(0\le w\le w_0\), and as \(\varepsilon\downarrow 0\),

\[
P_{m,n}(w_0+\varepsilon)
=C_{m,n}\varepsilon^{n(m+1)/2-1}
+O_{m,n}\bigl(\varepsilon^{n(m+1)/2}\bigr),
\]

where the explicit, strictly positive coefficient is

\[
C_{m,n}=
\frac{\Gamma((m+1)/2)^n\,\Gamma(n)\,(2n)^{n(m+1)/2-1}
\tan(\pi/n)^{n(m-1)/2}}
{(2\pi)^{n-1}\Gamma(n(m+1)/2)}.
\]

In particular, for four caps on \(S^2\), \(P_{2,4}(\pi/4+\varepsilon)=\frac{64}{5\pi}\varepsilon^5+O(\varepsilon^6)\).

There is also a **conditional local-shape theorem**, giving more than the scalar probability. Let \(k=m-1\), \(N=nk\), and choose coordinates with \(E\) in the first two coordinate directions. Decompose each center as

\[
X_i=(\sqrt{1-\|U_i\|^2}\cos\theta_i,
\sqrt{1-\|U_i\|^2}\sin\theta_i,U_i),\qquad U_i\in B^k.
\]

Start the cyclic ordering at the **labeled center** \(X_1\), then list all centers counterclockwise; use the same order for the transverse coordinates \(U_i\). (Sorting instead from a fixed external zero-angle direction would size-bias the wraparound gap and is not intended.) On the covering event, let the induced cap's angular half-width on \(E\) be

\[
\alpha_i=\arccos\!\left(\frac{\cos w}{\sqrt{1-\|U_i\|^2}}\right),
\]

let \(G_i\) be its succeeding cyclic angular gap, and set

\[
S=2\sum_{i=1}^{n}\alpha_i-2\pi,
\qquad T_i=\alpha_i+\alpha_{i+1}-G_i,
\qquad Z_i=T_i/S,
\]

with cyclic indices. For all sufficiently small positive \(\varepsilon\), **conditional on coverage**, the random vector \((Z_1,\ldots,Z_n)\) has the exact \(\operatorname{Dirichlet}(1,\ldots,1)\) law and is independent of the transverse coordinates \((U_i)_i\).

Define \(Y_i=U_i/\sqrt\varepsilon\), \(Y=(Y_1,\ldots,Y_n)\in\mathbb R^N\), and \(Q=\cot(w_0)\|Y\|^2/(2n)\). As \(\varepsilon\downarrow0\), the conditional law of \(Y\) converges **in total variation** to the density proportional to \((2n-\cot(w_0)\|y\|^2)_+^{n-1}\). Equivalently, \(Q\) tends to \(\operatorname{Beta}(N/2,n)\); the direction \(Y/\|Y\|\) is uniform on \(S^{N-1}\) and independent of \(Q\) in the limit; and the exact independent Dirichlet slack vector \(Z\) is also independent of this limiting pair. This is a joint Beta–spherical-direction–Dirichlet limit, including its normalizations.

## Assumptions and scope

All angular distances are measured in radians. \(S^m\subset\mathbb R^{m+1}\) carries normalized rotation-invariant surface measure. The target \(E\) is fixed in advance, independently of the random centers. The integers \(m\) and \(n\) remain fixed while \(\varepsilon\to0^+\). A covered point may lie on the boundary of a cap. Probability-zero ties in sorting azimuths are immaterial. \(B^k\) is the Euclidean unit ball in \(\mathbb R^k\), with volume \(V_k=\pi^{k/2}/\Gamma(k/2+1)\). Beta and Dirichlet distributions use the usual probability-normalized densities, not unnormalized measures.

## Proof

**1. Exact transverse and azimuthal distributions.** Rotation invariance and the surface Jacobian show that the \(U_i\) are independent, uniformly distributed on \(B^k\), and independent of iid \(\operatorname{Uniform}[0,2\pi)\) azimuths \(\theta_i\). Indeed, in coordinates \(U\in B^k\) and \(\theta\in[0,2\pi)\), the induced metric has circular component \(g_{\theta\theta}=1-\|U\|^2\) and transverse block \(I+UU^\top/(1-\|U\|^2)\). The determinant of the transverse block is \((1-\|U\|^2)^{-1}\), exactly canceling the circular factor; hence surface measure is \(d\theta\,dU\) up to a constant. Equivalently, \(\|U_i\|^2\sim\operatorname{Beta}(k/2,1)\).

At radius \(w<\pi/2\), the intersection of a cap with \(E\) is either empty or an angular arc of half-width

\[
\alpha_i=\arccos\left(\cos w/\sqrt{1-\|U_i\|^2}\right)
\quad\text{if }\|U_i\|\le\sin w,
\]

and empty otherwise. Always \(0\le\alpha_i\le w\). The azimuths are independent of these widths, and, after using the labeled azimuth \(\theta_1\) as angular origin, the cyclic gaps \(G_1,\ldots,G_n\) are uniform on the simplex \(\{g_i>0,\sum_i g_i=2\pi\}\), with constant \((n-1)!/(2\pi)^{n-1}\) relative to the first \(n-1\) gap coordinates. Ordering simply permutes the iid transverse coordinates and preserves their joint law.

**2. Localization of coverage.** For \(w\le\pi/n\), the total induced arc length is at most \(2nw\le2\pi\); equality would require every \(U_i=0\) and perfectly evenly spaced azimuths, a probability-zero event. Thus the coverage probability is zero. Take \(w=w_0+\varepsilon\). On coverage, \(\sum_i2\alpha_i\ge2\pi\). Since all \(\alpha_j\le w\), each \(\alpha_i\ge w_0-(n-1)\varepsilon\). Consequently each deficit \(w-\alpha_i=O_n(\varepsilon)\), and the exact cosine formula implies \(\|U_i\|^2=O_{m,n}(\varepsilon)\), uniformly across all covered configurations.

Also every cyclic azimuthal gap is at most \(2w\): otherwise its midpoint is farther than \(w\) from every center's azimuth, so cannot be covered. Because gaps sum to \(2\pi\), every gap lies in \([2w_0-2(n-1)\varepsilon,2w_0+2\varepsilon]\). For sufficiently small \(\varepsilon\), each induced arc has half-width near \(w_0\) and cannot cross either of its neighboring centers' azimuths. Thus a gap can be covered only by the two arcs centered at its endpoints. Hence coverage is equivalent to \(G_i\le\alpha_i+\alpha_{i+1}\) for all \(i\).

**3. An exact simplex and a conditional Dirichlet law.** Write \(h_i=\alpha_i+\alpha_{i+1}\), \(S=\sum_i h_i-2\pi\), and \(T_i=h_i-G_i\). Feasible coverage requires \(T_i\ge0\) and \(\sum_i T_i=S\). On the covering event, \(0<S\le2n\varepsilon\), whereas \(h_i\to2w_0>0\). Conversely, for sufficiently small \(\varepsilon\), any such nonnegative simplex of \(T_i\) automatically has \(G_i=h_i-T_i>0\), and gives a covering configuration. Its volume in the first \(n-1\) gap coordinates is \(S^{n-1}/(n-1)!\). The constant gap density therefore gives the **exact** conditional formula

\[
\Pr(E\text{ is covered}\mid U_1,\ldots,U_n)
=\left(\frac{S_+}{2\pi}\right)^{n-1}
\]

for all sufficiently small \(\varepsilon\), with the convention that \(S_+=0\) if an intersection arc is empty. The normalized point \(Z=T/S\) is uniform on the standard \((n-1)\)-simplex and independent of every transverse coordinate; thus \(Z\sim\operatorname{Dirichlet}(1,\ldots,1)\) exactly. The statement remains true after averaging over the random transverse configuration on the covering event.

**4. Exact integral and sharp asymptotic.** The preceding formula yields

\[
P_{m,n}(w)=\frac{1}{(2\pi)^{n-1}V_k^n}
\int_{(B^k)^n}\left(2\sum_i\alpha_i-2\pi\right)_+^{n-1}\,dU_1\cdots dU_n.
\]

For the few transverse points capable of covering, write \(U_i=\sqrt\varepsilon\,y_i\). Taylor expansion at \((w_0,0)\), uniformly for bounded \(y\), gives

\[
\alpha_i=w_0+\varepsilon-\tfrac12\cot(w_0)\varepsilon\|y_i\|^2+O_{m,n}(\varepsilon^2),
\]

and hence \(S=\varepsilon(2n-\cot(w_0)\|y\|^2+O_{m,n}(\varepsilon))\). The localization argument supplies a fixed compact ball containing the support of the rescaled integrands. The positive-part power \(x\mapsto(x_+)^{n-1}\) is Lipschitz on this bounded range. The integrals therefore differ from their limiting integral by \(O_{m,n}(\varepsilon)\), giving the claimed absolute remainder after multiplication by \(\varepsilon^{N/2+n-1}\).

Set \(a=N/2\). Polar coordinates and the beta integral give

\[
\int_{\mathbb R^N}(2n-\cot(w_0)\|y\|^2)_+^{n-1}dy
=\pi^{a}(2n)^{a+n-1}\tan(w_0)^a
\frac{\Gamma(n)}{\Gamma(a+n)}.
\]

Dividing by \(V_k^n(2\pi)^{n-1}\), using \(V_k=\pi^{k/2}/\Gamma((k+2)/2)\), and noting \(a+n=n(m+1)/2\), proves the stated \(C_{m,n}\). In particular \(C_{2,4}=64/(5\pi)\) follows by the half-integer gamma identities.

**5. Conditional limit in total variation.** Conditional on coverage, the exact density of \(Y=U/\sqrt\varepsilon\) is proportional to its compactly supported, nonnegative rescaled integrand \((S(Y)/\varepsilon)_+^{n-1}\), with the support restriction \(\sqrt\varepsilon Y_i\in B^k\). Step 4 establishes \(L^1\) convergence to the strictly positive-integral limiting function. Normalizing therefore yields convergence in total variation. Polar coordinates identify the limiting squared scaled radius \(Q\) as \(\operatorname{Beta}(a,n)\) and its direction as independent uniform spherical measure. Step 3 provides the exact, jointly independent Dirichlet slack law. This completes the theorem.

## Verification

The accompanying `check_onset.py` independently samples isotropic Gaussian-normalized sphere points, tests actual arc coverage by cyclic gaps, and compares the empirical probability with the exact conditional-simplex integral (quasi-Monte Carlo). It also compares the exact integral with the derived gamma coefficient for several \((m,n)\) pairs and checks \(C_{2,4}=64/(5\pi)\). The final marker upon successful execution is `GREAT_CIRCLE_RANDOM_CAP_ONSET_CHECKS_OK`. The proof above, not Monte Carlo, establishes all infinite and conditional assertions. Run `python check_onset.py` with NumPy and SciPy installed.

## Relationship to prior work

Classic random-arc covering theory, notably Siegel–Holst (1982), already derives exact covering probabilities for random circle arcs of arbitrary iid length distribution; the integral expression above is **not** asserted novel as an abstract circle-arc probability formula. Huffer–Shepp (1987) prove Schur convexity and coordinate convexity for fixed random-arc lengths and explain the classical Stevens equal-length formula. Those results are relevant stronger general frameworks for scalar coverage probabilities, but do not in their inspected accessible material give this specific spherical transverse-coordinate asymptotic coefficient or the joint Beta–Dirichlet conditional configuration law. The full Siegel–Holst text could not be inspected, so any stronger implication of that paper remains a priority risk.

Finch (2015) studies four random caps covering the **entire** sphere \(S^2\), which has the different tetrahedral threshold \(\arccos(1/3)\), not the fixed-target-circle threshold \(\pi/4\). Maehara (1988) treats the many-cap whole-sphere threshold, not the present fixed-sample near-optimal circle event. The natural geometric contribution here is the dimension-dependent onset coefficient together with the detailed conditional transverse and gap-shape laws. No global novelty or independent audit is claimed.

## Limitations

The number of caps and ambient dimension are fixed: no uniformity in \(m\) or \(n\) is proved. Coverage means covering a predetermined great circle, never the whole sphere. Only the first nonzero probability coefficient and the leading conditional law are determined. The bounds have constants depending on \(m,n\). Conditioning on an event of asymptotically vanishing probability is mathematically well-defined for each small positive \(\varepsilon\). The exact law of gap slack does not imply the finite-\(\varepsilon\) transverse density is beta; that is a limit only. Historical priority is provisional, particularly because full text of the most closely related 1982 random-size arc paper was inaccessible.

## References

1. A. F. Siegel and L. Holst, *Covering the circle with random arcs of random sizes*, Journal of Applied Probability **19** (1982), 373–381. DOI: https://doi.org/10.2307/3213488 (abstract inspected; full text not accessible).
2. F. W. Huffer and L. A. Shepp, *On the probability of covering the circle by random arcs*, Journal of Applied Probability **24** (1987), 422–429. DOI: https://doi.org/10.2307/3214266 (full open-access text inspected).
3. S. R. Finch, *Covering a Sphere with Four Random Circular Caps*, arXiv:1502.06931v1, publicly posted 2015-02-24. https://arxiv.org/abs/1502.06931 (full text inspected).
4. H. Maehara, *A threshold for the size of random caps to cover a sphere*, Annals of the Institute of Statistical Mathematics **40** (1988), 665–670. DOI: https://doi.org/10.1007/BF00049424 (abstract and bibliographic details inspected; not the fixed-target problem).
