# Unique optimal two-region Gaussian photometry under a fixed readout budget

## Finding

Fix a circular field of radius \(R>0\), a known point-spread width \(\sigma>0\), and a uniform positive sky-background photon intensity \(b>0\). Suppose the instrument keeps **only two photon totals**, from a measurable partition of this disk into two regions of positive area. The unknown scientific parameters are the source's total expected photon flux \(F\geq0\) and the background intensity \(b\). In the local background-dominated Fisher-information limit \(F\downarrow0\), the unique D-optimal **unordered** two-region partition, among **all measurable partitions**, consists of a central disk and its complementary annulus, up to area-zero changes.

Write
\[
 c=\frac{R^2}{2\sigma^2},\quad x=\frac{a^2}{R^2},\quad
 h_c(x)=1-e^{-cx}-x(1-e^{-c}),\quad
 Q_c(x)=\frac{h_c(x)^2}{x(1-x)}.
\]
For each \(c>0\), the optimal central area fraction \(x_*(c)\) exists, is unique, and obeys \(0<x_*(c)<1/2\). It is the unique solution in \((0,1/2)\) to
\[
 2x(1-x)\bigl(ce^{-cx}-(1-e^{-c})\bigr)
 -(1-2x)\bigl(1-e^{-cx}-x(1-e^{-c})\bigr)=0.
\]
The maximal determinant of the two-parameter Fisher information is exactly \(b^{-2}Q_c(x_*(c))\). The asymptotic laws are
\[
 x_*(c)=\frac12-\frac{c}{12}+O(c^2)\quad(c\downarrow0),
 \qquad
 cx_*(c)\longrightarrow y_*=1.2564312086261696\ldots\quad(c\to\infty),
\]
where \(y_*>0\) is the unique positive solution of \(e^{y_*}=1+2y_*\). Thus the large-field optimal inner radius approaches \(\sqrt{2y_*}\,\sigma=1.5852010652445131\ldots\,\sigma\).

## Assumptions and scope

The observation field is \(D_R=\{z\in\mathbb R^2:|z|\leq R\}\). The point source is centered at the known origin, with known circular Gaussian point-spread probability density
\[
 p_\sigma(z)=\frac{1}{2\pi\sigma^2}\exp\!\left(-\frac{|z|^2}{2\sigma^2}\right).
\]
Photons form a spatial Poisson process of intensity \(F p_\sigma(z)+b\). There are no other sources, detector read-noise effects, saturation, point-spread uncertainty, centroid uncertainty, or spatial background gradients. A designer chooses any measurable region \(E\subset D_R\) with \(0<|E|<\pi R^2\); the instrument records only the counts in \(E\) and \(D_R\setminus E\), not the positions of individual photons. Given the independent Poisson totals, local D-optimality maximizes the determinant of the Fisher information matrix for \((F,b)\) as \(F\downarrow0\), with \(b>0\) held fixed. The field radius and two-channel readout budget are fixed: this is **not** optimization over the outer radius, and it is **not** a claim that two counts match the full-pixel Fisher information.

## Proof

**1. Exact Fisher reduction.** Let \(A_1=|E|\), \(A_2=\pi R^2-A_1\), \(P_1=\int_Ep_\sigma\), and \(P_2=\int_{D_R\setminus E}p_\sigma\). The independent counts have means \(\lambda_i=FP_i+bA_i\). Since their score-gradient vectors are \((P_i,A_i)\), their Fisher matrix is
\[
 \mathcal I(F,b)=\sum_{i=1}^2\frac{1}{\lambda_i}
 \begin{pmatrix}P_i^2&P_iA_i\\P_iA_i&A_i^2\end{pmatrix},\qquad
 \det\mathcal I(F,b)=\frac{(P_1A_2-P_2A_1)^2}{\lambda_1\lambda_2}.
\]
The limit at \(F=0\) exists with both means positive and equals
\[
 \det\mathcal I(0,b)=\frac{(P_1-xP)^2}{b^2x(1-x)},
 \quad x=\frac{A_1}{\pi R^2},\quad P=1-e^{-c}.
\]
This formula also defines the \(F\downarrow0\) local design from the interior parameter domain \(F>0\).

**2. Global geometric reduction, not merely a radial ansatz.** The Gaussian density is strictly decreasing in radius. At any prescribed area fraction \(x\in(0,1)\), the layer-cake/rearrangement principle makes \(P_1\) uniquely largest (up to null sets) for the centered disk with radius \(R\sqrt{x}\), and uniquely smallest for the outermost annulus of area fraction \(x\). One can verify the maximality directly: for the centered disk \(C\) with \(|C|=|E|\), integrate \((1_C-1_E)(p_\sigma-p_\sigma(R\sqrt x))\geq0\); strict radial decrease gives equality only when \(E=C\) almost everywhere. The corresponding minimum follows by complementation.

For the central disk of area fraction \(x\), its photon fraction is \(1-e^{-cx}\), and \(P_1-xP=h_c(x)>0\), strictly by concavity of \(u\mapsto1-e^{-cu}\). For arbitrary \(E\), its signed contrast \(P_1-xP\) lies between \(-h_c(1-x)\) and \(h_c(x)\). Consequently
\[
 \det\mathcal I(0,b)
 \leq b^{-2}\max\{Q_c(x),Q_c(1-x)\}.
\]
Therefore global optimization over all measurable two-region partitions reduces exactly to maximizing \(Q_c\) on \((0,1)\). Equality requires a central disk or its annular complement, with no hidden nonradial optima.

**3. Strict uniqueness of the radial fraction.** Since \(h_c(x)>0\), \(Q_c'\) has the sign of
\[
 N_c(x)=2x(1-x)h_c'(x)-(1-2x)h_c(x)
 =(1+e^{-c})x-1+e^{-cx}\bigl(1-2x+2cx(1-x)\bigr).
\]
Direct differentiation gives
\[
 N_c''(x)=-c^2e^{-cx}\,[2cx^2-(2c+6)x+3].
\]
The quadratic in brackets has exactly one zero in \((0,1)\): it has positive value \(3\) at zero, negative value \(-3\) at one, and positive leading coefficient (hence its second zero is beyond one). Thus \(N_c'\) first strictly decreases, then strictly increases. The endpoint identities are
\[
 N_c(0)=N_c(1)=0,\quad N_c'(0)=c-1+e^{-c}>0,\quad
 N_c'(1)=1-(1+c)e^{-c}>0.
\]
Finally
\[
 N_c(1/2)=\frac{e^{-c/2}}{2}\bigl(c-2\sinh(c/2)\bigr)<0.
\]
The derivative \(N_c'\) must therefore be negative somewhere. Since it decreases then increases and is positive at both endpoints, it has precisely two interior zeros. Hence \(N_c\) rises from zero to a positive local maximum, falls through zero exactly once to a negative local minimum, and rises to zero at one. Its unique interior zero lies in \((0,1/2)\); \(Q_c\) increases then decreases across this zero. As \(Q_c(x)\to0\) at either endpoint, this is the unique global maximum. Combining this with the strict rearrangement equality cases proves uniqueness of the unordered optimal partition.

**4. Limiting geometry.** Uniformly for \(x\) in compact subsets of \((0,1)\), Taylor expansion yields
\[
 h_c(x)=\frac{c^2}{2}x(1-x)\left[1-\frac c3(1+x)+O(c^2)\right].
\]
The convergence of the optimizer to \(1/2\) is global: the interpolation error for the concave function \(1-e^{-ct}\) has a nonnegative Green-kernel representation, and its second derivative \(-c^2e^{-ct}\) lies between \(-c^2\) and \(-c^2e^{-c}\). Consequently \(\frac{c^2e^{-c}}2x(1-x)\leq h_c(x)\leq\frac{c^2}2x(1-x)\) for every \(x\in[0,1]\). Thus \(4Q_c(x)/c^4\to x(1-x)\) uniformly on \([0,1]\), and the sole optimizer tends to \(1/2\). Expanding the stationary equation then gives \(x_*=1/2-c/12+O(c^2)\).

For \(c\to\infty\), put \(y=cx\). The normalized objective square root obeys
\[
 \frac{h_c(y/c)}{\sqrt{c(y/c)(1-y/c)}}
 \longrightarrow \frac{1-e^{-y}}{\sqrt y}
\]
locally uniformly for positive fixed \(y\). Maximizers do not escape to \(y=0\) or \(y=\infty\): for \(x\leq1/2\), the normalized expression is bounded by \(\min\{\sqrt{2y},\sqrt{2/y}\}\), using \(h_c(x)\leq\min\{cx,1\}\). The limit function vanishes at both ends and has one positive maximizer, since differentiation gives \(e^y=1+2y\), with exactly one positive root by strict convexity of the exponential. Thus \(cx_*(c)\to y_*\) and the radius limit follows.

## Verification

`CHECK.py` is an executable Python-standard-library diagnostic, run as `python CHECK.py`. It compares both expressions for \(N_c\), tests the stated second-derivative formula by finite differences, compares Fisher-matrix and reduced determinant formulas, brackets and locates the unique maximizing root over varied field scales, checks thousands of deterministic discretized two-region partitions against the analytic bound, and tests both asymptotic regimes. These finite diagnostics do not prove uniqueness or the all-measurable-partition statement; Steps 2–4 above provide those proofs.

For example, at \(c=2\), the optimal central area fraction is \(0.34619465700758033\ldots\), giving inner radius \(0.588383086948954\ldots\,R\). Its Fisher determinant is \(0.17721494562743806\ldots/b^2\), compared with \(0.15966130015118526\ldots/b^2\) for an equal-area split, a gain of about \(10.99\%\) in determinant within the constrained two-count design.

## Relationship to prior work

Classical aperture-photometry studies optimize source signal-to-noise or analyze the use of background sky annuli, including Fischer and Kochanski (first public preprint 1993-10-14). Masci (2008) already derives the large-field Gaussian optimum radius \(1.5852\sigma\) for **single-aperture signal-to-noise**; neither this constant nor its defining scalar equation is asserted to be new. The distinct finite-field and arbitrary-partition two-parameter classification is the result here. Chandra Source Catalog documentation (2012-12-14) explicitly models two aperture photon totals and encircled-source fractions. Vicuña et al. (arXiv 2023) derive joint source/background Poisson Fisher bounds using **individual pixel counts** and compare their inference with staged masked-aperture practice; the inspected manuscript uses a different decision problem and does not establish an all-measurable-two-bin partition optimum. Espinosa et al. (2025) consider how much pixel-level Fisher information is retained as a fitting radius changes, again with a different design space. The present result specifically optimizes the **partition of a fixed outer disk when only two aggregated Poisson totals survive**, and proves a unique geometric optimum plus two sharp limiting laws. It does not claim the underlying Poisson Fisher formula, the Gaussian profile, or the general rearrangement principle as new; the exact constrained optimal-partition classification is the subject of this result. Historical priority remains provisional, particularly against general information-optimal quantization literature and any inaccessible prior proofs.

## Limitations

The result is strictly about local Fisher D-optimality at vanishing source flux, not finite-flux global design, actual unbiased-estimator performance at the parameter boundary, or a recommendation to discard recorded pixels. Both the circular Gaussian point-spread function and uniform background are known; positional errors, read noise, crowding, correlated pixels, imperfect detector response, and robust multiobjective design are excluded. Optimizing over three or more retained counts or over the outer field radius is outside scope. The large-field limiting radius equals an explicitly published Gaussian SNR scale (Masci, 2008), but the finite-field two-parameter global-partition proof is distinct. Mathematical correctness is supported by an analytic proof and diagnostics, not independently audited.

## References

1. P. Fischer and G. P. Kochanski, *Optimal Addition of Images for Detection and Photometry*, arXiv:astro-ph/9310031 (first public preprint 1993-10-14), https://arxiv.org/abs/astro-ph/9310031.
2. Chandra X-ray Center, *Aperture Photometry Values and Errors* (2012-12-14), https://asc.harvard.edu/csc1/why/ap_vals_errs.html.
3. V. Dhillon, *Extracting photometric data* (2012-11-26), https://vikdhillon.staff.shef.ac.uk/teaching/phy217/instruments/phy217_inst_photred.html.
4. M. L. Vicuña et al., *Optimal photometry of point sources: Joint source flux and background determination on array detectors*, arXiv:2311.12142 (first preprint 2023-11-20), https://arxiv.org/pdf/2311.12142.
5. F. Masci, *Optimum Aperture Radius for a Gaussian Profile* (2008-10-08), https://web.ipac.caltech.edu/staff/fmasci/home/mystats/GaussApRadius.pdf.
6. S. Espinosa et al., *The impact of the point spread function fitting radius on photometric uncertainty based on the Fisher information matrix*, arXiv:2509.20613 (2025), https://arxiv.org/abs/2509.20613.
