# Two-versus-three monitor identifiability and calibrated-mass aliasing for an impulsive river tracer

## Finding

Consider the ideal free-line, one-dimensional advective–dispersive–reactive response to one instantaneous tracer release:

\[
C(x,t)=\begin{cases}
0,&t\le\tau,\\[2pt]
\displaystyle\frac{M}{\sqrt{4\pi D(t-\tau)}}
\exp\!\left[-\frac{(x-\xi-v(t-\tau))^2}{4D(t-\tau)}-k(t-\tau)\right],&t>\tau.
\end{cases}
\]

The release location \(\xi\in\mathbb R\), release time \(\tau\in\mathbb R\), dispersion \(D>0\), downstream velocity \(v>0\), decay \(k\ge0\), and released mass \(M>0\) are all unknown. Sensor coordinates and gains are known; continuous noiseless time traces are available, and the source does not coincide with a sensor.

**Sharp sensor-count and alias classification.** Let \(x_0<x_1\) be distinct sensors.

1. If the source is known a priori to lie strictly upstream, \(\xi<x_0\), the two entire breakthrough traces uniquely identify *all six* parameters. Once the onset \(\tau\) has been observed, only three distinct positive post-onset sampling times at each sensor are needed. One sensor cannot be sufficient, even with the upstream restriction.
2. Without any source-side restriction, the two traces cannot universally identify the six parameters: **every** admissible release upstream of \(x_0\) has an explicit, physically admissible, distinct twin source *between* the two sensors, with different dispersion, velocity, and decay but exactly the same two continuous histories. Three distinct sensors, anywhere on the line, do universally determine all six parameters.
3. Even knowing the released mass in advance does not universally resolve the two-sensor ambiguity. An explicit exact pair of distinct, same-mass releases has identical histories at both sensors.

These assertions are for the stated model and exact data, not numerical or statistical identifiability in the presence of noise.

## Assumptions and scope

The spatial domain is all of \(\mathbb R\), with homogeneous constant coefficients, one instantaneous point release, first-order irreversible decay, positive downstream drift, and no physical boundaries. In particular, no reservoir, dead zone, finite-volume injection, variable cross section, background tracer, turbulent non-Fickian mixing, or multiple release is included. Parameters are constant throughout observation; time is measured on a calibrated clock. At a sensor not coincident with \(\xi\), concentrations vanish exactly through \(\tau\) and are strictly positive at every later time. Observing the complete trace therefore determines the release onset as the boundary of its positive-time support. The three-post-onset-time statement assumes that this onset has been independently determined.

A calibrated-mass alias means both distinct parameter sets obey the *same prescribed positive* \(M\); neither release is allowed to change its mass to fit the data.

## Proof

**1. Canonical invariants of a breakthrough trace.** Set \(s=t-\tau>0\). Expanding the square gives, for each observation coordinate \(x_j\),

\[
\log(C(x_j,\tau+s)\sqrt{s})=\ell_j-\frac{A_j}{s}-Bs,
\]

where

\[
A_j=\frac{(x_j-\xi)^2}{4D},\qquad
B=k+\frac{v^2}{4D},\qquad
\ell_j=\log\frac{M}{\sqrt{4\pi D}}+\frac{v(x_j-\xi)}{2D}.
\]

Thus a full trace uniquely determines \(A_j,B,\ell_j\). In fact, after multiplying the displayed logarithm by \(s\), it becomes a quadratic polynomial in \(s\). Its values at any three distinct positive \(s\) determine all three coefficients by polynomial interpolation. The two sensors necessarily return the same \(B\). No asymptotic fitting or infinite-time extrapolation is needed in the ideal data model.

**2. Explicit two-sensor inverse for upstream sources.** Let \(L=x_1-x_0>0\). For \(\xi<x_0\), both distances are positive and

\[
r=\sqrt{A_1/A_0}=\frac{x_1-\xi}{x_0-\xi}>1,
\quad \xi=\frac{r x_0-x_1}{r-1},
\quad D=\frac{(x_0-\xi)^2}{4A_0}.
\]

The spatial log-amplitude slope \(\rho=2(\ell_1-\ell_0)/L\) equals \(v/D\). The remaining parameters follow uniquely:

\[
v=\rho D,\qquad
k=B-\frac{\rho^2D}{4},\qquad
M=\sqrt{4\pi D}\exp\!\left(\ell_0-\frac{\rho(x_0-\xi)}2\right).
\]

Every true admissible upstream release gives \(r>1\), \(\rho>0\), and \(k\ge0\); the inverse is therefore global on that admissible region. To show that one sensor does *not* suffice, write \(p=x_0-\xi>0\) and replace, for any \(c>0\),

\[
p\mapsto cp,\quad \xi\mapsto x_0-cp,\quad D\mapsto c^2D,
\quad v\mapsto cv,\quad k\mapsto k,\quad M\mapsto cM.
\]

Each of its one-sensor invariants \(A_0,B,\ell_0\) stays unchanged, while \(c\ne1\) changes the parameters. One monitor cannot identify the release even with its upstream location known.

**3. Exact two-sensor involutive ambiguity without source-side knowledge.** For any upstream release put \(p=x_0-\xi>0\), \(L=x_1-x_0>0\), and

\[
q=\frac{L}{2p+L}\in(0,1),\qquad \eta=x_0+pq\in(x_0,x_1).
\]

Define the second release by

\[
\boxed{\begin{aligned}
\xi'&=\eta, &D'&=q^2D, &v'&=q^2v,\\
k'&=k+\frac{(1-q^2)v^2}{4D},
&&M'=qM\exp\!\left(\frac{v(\eta-\xi)}{2D}\right),
&\tau'&=\tau.
\end{aligned}}
\]

Every primed parameter is admissible; notably \(k'\ge k\ge0\). At the two sensors,

\[
|x_j-\eta|=q|x_j-\xi|\quad(j=0,1).
\]

It follows that \(A_j'=A_j\). Since \(v'/D'=v/D\), both spatial log-amplitude differences agree; the stated positive \(M'\) makes the entire log amplitude at the first sensor agree, hence also at the second. Finally,

\[
k'+\frac{(v')^2}{4D'}=k+\frac{v^2}{4D}=B.
\]

All three invariants agree at each sensor, so \(C'(x_j,t)=C(x_j,t)\) for **every real time** and for \(j=0,1\). This is a strict alias because \(\xi'\ne\xi\) and \(D'\ne D\), not a time-discretization accident. It is the complete alternate *geometric branch*: any fit with \(A_0,A_1>0\) must satisfy \(|x_1-\xi'|/|x_0-\xi'|=\sqrt{A_1/A_0}\); fixing whether the two signed sensor-source differences have equal or opposite signs gives at most one source location and corresponding dispersion per branch. The invariants then determine \(v,k,M\) uniquely on each admissible branch. Some data sets have only one physically feasible branch, but every upstream release has both.

**4. A third sensor resolves all global aliases.** For any three distinct sensors, the three identifiable numbers \(A_j\) are the samples of

\[
A(x)=\frac{(x-\xi)^2}{4D}=\alpha x^2+\beta x+\gamma.
\]

A quadratic is uniquely determined by three distinct samples. Consequently \(D=1/(4\alpha)\) and \(\xi=-\beta/(2\alpha)\) are unique; the invariant \(\rho=2(\ell_1-\ell_0)/(x_1-x_0)\) then yields \(v\), and \(B,\ell_0\) yield \(k,M\). The pre-release trace identifies \(\tau\). This proves universal sufficiency of three spatial stations, including cases where no prior source-side information is available. Since the explicit two-sensor alias exists for every upstream release, three is also the sharp universal sensor count within this model.

**5. Exact alias despite known released mass.** In the upstream-to-interior construction,

\[
\frac{M'}M=q\exp\!\left(\frac{v p(p+L)}{D(2p+L)}\right).
\]

The equality \(M'=M\) holds at the *unique* positive drift

\[
\boxed{v_{\mathrm{mass}}=\frac{D(2p+L)}{p(p+L)}\log\frac{2p+L}{L}.}
\]

For example, place stations at \(0\) and \(1\). The release

\[
(\xi,D,v,k,M,\tau)=(-1,1,\tfrac32\log3,1,1,0)
\]

and the distinct release

\[
(\xi',D',v',k',M',\tau')=
(\tfrac13,\tfrac19,\tfrac16\log3,1+\tfrac12(\log3)^2,1,0)
\]

have *identical concentrations at both stations at all times*, despite both releasing exactly unit mass and obeying strictly positive downstream velocity and nonnegative decay. This proves that mass calibration alone does not give universal two-station identification.

## Verification

The standalone standard-library Python checker `checker.py` evaluates 150 deterministic parameter sets with varying station positions and all positive physical coefficients, constructs their exact algebraic twins, checks the two-site concentration identity at six post-onset times at each station, and reconstructs all five post-onset unknowns from three sample times in both the two-site upstream and three-site unrestricted inverses. It also tests the exact same-mass logarithmic example. Replay with `python3 checker.py`. The script reports 4,215 successful assertions. The proof of universal and all-time statements is the algebra above, not finite numerical testing.

## Relationship to prior work

El Badia, Ha-Duong and Hamdi (2005) proved identifiability of an unknown time-dependent point pollutant source in a finite river with **prescribed** transport coefficients, from suitable two-sided measurements. The full accessible manuscript's model in section 2 and parameter statement in section 3 treat velocity, dispersion and reaction as coefficients of the given operator, not three additional unknowns to be inferred jointly. That result does not imply the present six-parameter inverse or the mass-calibrated drift-induced alias. Hamdi (2009) and Andrle, Ben Belgacem and El Badia (2011) extend source reconstruction and moving-source problems but involve different source functions and observation geometries; the latter full text was not accessible for a decisive entire-document exclusion.

The publicly accessible published result *An exact hypersphere obstruction and minimal two-snapshot sensor theorem for an unknown-diffusivity pollutant puff* establishes a sharp three-sensor condition in one-dimensional **advection-free, reaction-free** Gaussian diffusion with unknown mass, diffusivity, onset and location. Its geometric inversion is the important closest prior mechanism. Here it is acknowledged rather than claimed as new. The present claim instead gives the **two-sensor** globally identifying side-prior with both drift and decay unknown, the complete physically admissible cross-side alias transformation, and a mass-calibrated positive-drift collision, none of which follows from that theorem's zero-drift assumptions. The three-station corollary is included to close the comparison, not independently asserted as a new sensor-count principle for Gaussian diffusion.

The empirical monitoring-design study *Influence of the spatial and temporal monitoring design on the identification of an instantaneous pollutant release in a river* (2020) studies identifiability of source parameters under prescribed hydrodynamic scenarios, including numerical sensitivity to flow and dispersion; it is not treated as a proof of the present simultaneous all-parameter classification. Full-text priority risks from broader inverse-problem theory remain.

## Limitations

The exact pairwise identity does not imply good numerical conditioning or identifiability under background pollution, noisy finite detection thresholds, unknown sensor gain, uncertain timing, multiple sources, or finite-domain boundary conditions. The three-post-onset-time reconstruction requires a separately known onset. The source-side assumption is substantial and must be justified independently; outside it, two spatial stations can genuinely be ambiguous despite perfect records. A fitted negative decay coefficient would mark an inadmissible alias rather than a second physical solution. General historical priority cannot be certified from a finite set of accessible sources.

## References

1. A. El Badia, T. Ha-Duong, A. Hamdi, *Identification of a point source in a linear advection–dispersion–reaction equation: application to a pollution source problem*, Inverse Problems 21 (2005), 1121–1136; first online publication 2005-05-09. DOI: https://doi.org/10.1088/0266-5611/21/3/020. Accessible author manuscript text: https://www.researchgate.net/publication/230901733_Identification_of_a_point_source_in_a_linear_advection-dispersion-reaction_equation_Application_to_a_pollution_source_problem.
2. A. Hamdi, *The recovery of a time-dependent point source in a linear transport equation: application to surface water pollution*, Inverse Problems 25 (2009), 075006. DOI: https://doi.org/10.1088/0266-5611/25/7/075006.
3. M. Andrle, F. Ben Belgacem, A. El Badia, *Identification of moving pointwise sources in an advection–dispersion–reaction equation*, Inverse Problems 27 (2011), 025007. DOI: https://doi.org/10.1088/0266-5611/27/2/025007.
4. *An exact hypersphere obstruction and minimal two-snapshot sensor theorem for an unknown-diffusivity pollutant puff* (2026), publicly archived theorem and proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-an-exact-hypersphere-obstruction-and-minimal-two-snapshot-sensor--a9167f8e630b/RESULT.md.
5. *Influence of the spatial and temporal monitoring design on the identification of an instantaneous pollutant release in a river*, Advances in Water Resources (2020), article 103788. DOI: https://doi.org/10.1016/j.advwatres.2020.103788.
