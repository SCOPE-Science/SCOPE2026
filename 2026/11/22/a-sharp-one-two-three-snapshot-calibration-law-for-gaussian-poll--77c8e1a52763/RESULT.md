# A sharp one–two–three snapshot calibration law for Gaussian pollutant-source localization

## Finding

**Complete minimal spatiotemporal sampling classification.** Fix an integer spatial dimension \(d\ge 1\), a known positive diffusivity \(D\), and distinct known observation times \(t_1<\cdots<t_m\). At finitely many fixed sensor positions \(s_1,\ldots,s_N\in\mathbb R^d\), observe noiseless, positive, absolutely calibrated values of the free-space instantaneous-release field

\[
C(s,t)=\frac{M}{[4\pi D(t-t_0)]^{d/2}}\exp\!\left(-\frac{\|s-z\|^2}{4D(t-t_0)}\right),\qquad t>t_0.
\]

The unknowns are the source center \(z\in\mathbb R^d\), release time \(t_0<t_1\), and either a positive unknown release mass \(M\) or a specified positive calibrated mass \(M=M_0\). Write

\[
A=\begin{pmatrix}1&s_1^\top\\ \vdots&\vdots\\1&s_N^\top\end{pmatrix},\qquad
H=\begin{pmatrix}1&s_1^\top&\|s_1\|^2\\ \vdots&\vdots&\vdots\\1&s_N^\top&\|s_N\|^2\end{pmatrix}.
\]

The following table states the **exact minimum number of distinct temporal snapshots for global injectivity over every admissible parameter set**, with \(\infty\) meaning that not even complete postrelease time traces ensure injectivity:

| Fixed sensor geometry | Calibrated known mass | Unknown mass |
|---|---:|---:|
| \(\operatorname{rank}A<d+1\) | \(\infty\) | \(\infty\) |
| \(\operatorname{rank}A=d+1\) and \(\operatorname{rank}H=d+1\) | **2** | **3** |
| \(\operatorname{rank}H=d+2\) | **1** | **1** |

All rows apply for arbitrary distinct specified observation times, with no generic-position caveat on the source. In the middle row, all sensor positions lie on a single positive-radius sphere while their affine span is full. Thus mass calibration saves **exactly one entire observation round** on every such minimal spatial array. In the plane, a three-sensor noncollinear circular array needs precisely two temporal rounds when mass is known but three when mass is unknown; a fourth nonspherical sensor can reduce either requirement to one.

## Assumptions and scope

An impulsive passive tracer diffuses in unbounded, homogeneous, isotropic space, with a known scalar transport coefficient \(D>0\), without advection, reaction, decay, sensor background, or boundaries. All sensor positions and observation times are known, and observations are positive real concentrations with known gain. The release occurs strictly before the first observation. The two mass-calibration settings are separate inverse problems: in the known-mass setting its positive numerical value is supplied externally; in the unknown-mass setting it is unrestricted in \((0,\infty)\). The theorem concerns *global structural identifiability* from raw concentration values, not statistical estimation or conditioning. It treats any finite array, including repeated sensor coordinates, and any number of observation times.

A sensor set has full affine span precisely when \(\operatorname{rank}A=d+1\). If this holds and \(\operatorname{rank}H=d+1\), there are unique \(o\in\mathbb R^d\) and \(R>0\) with \(\|s_i-o\|=R\) at every sensor: this is the cospherical case. With full affine span and \(\operatorname{rank}H=d+2\), no sphere contains all sensors.

## Proof

**1. Exhaustion of spatial geometries.** When \(\operatorname{rank}A<d+1\), all sensors lie in a proper affine hyperplane. Reflecting a source strictly off that hyperplane across it yields a distinct source center at precisely the same distance from *every* sensor. Keeping its release time, mass and diffusivity fixed gives identical complete positive-time concentration traces. No temporal oversampling can make the map globally injective in either mass setting.

Now suppose \(\operatorname{rank}A=d+1\). An equality \(\operatorname{rank}H=d+1\) means the final column of \(H\) is a linear combination of the columns of \(A\). Hence for some real \(b\) and vector \(v\), all sensors satisfy \(\|s_i\|^2=b+v\cdot s_i\). Completing the square gives \(\|s_i-o\|^2=R^2\) with \(o=v/2\). Because the affine span is full, the sphere radius is positive, and its center and radius are unique. Conversely, sensors on a sphere make \(H\) rank deficient. The only remaining full-affine-span possibility is \(\operatorname{rank}H=d+2\).

**2. One snapshot in the nonspherical case.** Fix any single postrelease observation time \(t\) and put \(u=t-t_0>0\). Its logarithmic concentration is the quadratic-affine polynomial

\[
\log C(s,t)=\alpha+\beta\cdot s+\gamma\|s\|^2,
\quad \gamma=-\frac1{4Du},\quad \beta=\frac{z}{2Du},
\]

\[
\alpha=\log M-\frac d2\log(4\pi Du)-\frac{\|z\|^2}{4Du}.
\]

If \(\operatorname{rank}H=d+2\), the exact sensor readings uniquely determine \((\alpha,\beta,\gamma)\). Thus \(u=-1/(4D\gamma)\), \(z=-\beta/(2\gamma)\), \(t_0=t-u\), and

\[
M=(4\pi Du)^{d/2}\exp\!\left(\alpha+\frac{\|z\|^2}{4Du}\right).
\]

This reconstructs even unknown mass. No positive number of rounds below one is possible, proving sharpness of the last row. This logarithmic-polynomial part of the argument is elementary and is not asserted as a separate novelty claim.

**3. All noncentral sources on a spanning sphere recover from two rounds.** Assume the sensors span \(\mathbb R^d\) affinely and lie on the sphere centered at \(o\) of radius \(R>0\). Let \(u=t_1-t_0>0\), \(\Delta=t_2-t_1>0\), and form exact spatial log differences

\[
\delta_i(t)=\log C(s_i,t)-\log C(s_1,t)
=\frac{(s_i-s_1)\cdot(z-o)}{2D(t-t_0)}.
\]

Because the difference vectors \(s_i-s_1\) span \(\mathbb R^d\), all differences vanish if and only if \(z=o\). If at least one \(\delta_i(t_1)\ne0\), then

\[
\frac{\delta_i(t_1)}{\delta_i(t_2)}=\frac{u+\Delta}{u},\qquad
u=\frac{\Delta}{\delta_i(t_1)/\delta_i(t_2)-1}.
\]

The same spatial differences then determine \(z-o\) from a full-rank linear system. One absolute reading determines \(M\) if it was not already known. Thus *both* mass settings are globally injective after two rounds at every off-center source. The sole possible two-round ambiguity is at the circumcenter \(z=o\).

**4. The circumcenter with known mass: two and only two rounds.** For \(z=o\), every sensor sees the same temporal profile

\[
C(s_i,t)=\frac{M}{(4\pi D)^{p}}g(t-t_0),\quad
p=\frac d2>0,\quad a=\frac{R^2}{4D}>0,\quad
 g(u)=u^{-p}e^{-a/u},\quad u>0.
\]

Suppose \(0<u<v\) gave equal *known-mass* profiles at the first time. Taking logarithms of \(g(u)=g(v)\) forces

\[
a=p\,Q(u,v),\qquad Q(u,v)=\frac{uv}{v-u}\log\frac vu
=\int_0^1\frac{uv}{(1-\theta)u+\theta v}\,d\theta.
\]

For every \(\theta\in[0,1]\), the integrand is the weighted harmonic mean \(\big((1-\theta)/v+\theta/u\big)^{-1}\), strictly increasing when a common \(\Delta>0\) is added to \(u\) and \(v\). Consequently \(Q(u+\Delta,v+\Delta)>Q(u,v)\), contradicting the second-time equality \(g(u+\Delta)=g(v+\Delta)\). Two rounds thus identify the central age and therefore the entire source at *every* center, including \(o\).

One round cannot suffice uniformly: \(g\) is continuous, rises strictly from zero to its unique maximum at \(u=a/p\), then falls strictly back to zero. Every response strictly between zero and its maximum occurs at two distinct positive ages, with the same known mass and central source, so a one-round exact ambiguity exists.

**5. The circumcenter with unknown mass: three and only three rounds.** If masses are unrestricted, two distinct ages \(u<v\) and two positive masses produce identical readings at each time offset \(h\) precisely when their ratio \(g(u+h)/g(v+h)\) is constant for all observed offsets. Differentiate:

\[
\frac{d}{dh}\log\frac{g(u+h)}{g(v+h)}
=\frac{v-u}{(u+h)(v+h)}
\left[-p+a\left(\frac1{u+h}+\frac1{v+h}\right)\right].
\]

The bracket strictly decreases with \(h\), so this logarithmic ratio is strictly monotone or else first rises then falls: it has **at most one turning point**. Therefore one horizontal level can be attained at most twice. Readings at *three distinct time offsets* cannot arise from two distinct ages, and once the age is determined the mass follows from any absolute reading. This proves three-round global sufficiency.

To show two-round *failure*, fix the gap \(\Delta>0\), and consider

\[
r(u)=\frac{g(u+\Delta)}{g(u)},\qquad
\frac{d}{du}\log r(u)=\frac{\Delta}{u(u+\Delta)}\left[p-a\left(\frac1u+\frac1{u+\Delta}\right)\right].
\]

The bracket increases strictly from \(-\infty\) to \(p>0\), so \(r\) first strictly decreases and then strictly increases; \(r(0+)=+\infty\), while \(r(u)\to1\) **from below** as \(u\to\infty\). Every level strictly between its minimum and \(1\) has two distinct positive preimages. Choose two ages realizing such a level, then rescale the unknown positive masses to equalize first-time amplitudes. The second-time amplitudes match automatically at every sensor, giving exact two-round nonidentifiability. The result holds for *every* positive gap \(\Delta\).

**6. Exact planar witness.** Set \(d=2\), \(D=1/4\), with three sensors \((1,0),(-1,0),(0,1)\) and central source \(z=(0,0)\). Here \(p=a=1\), and with observation gap \(\Delta=1\),

\[
\frac{g(u+1)}{g(u)}=\frac u{u+1}\exp\!\left(\frac1{u(u+1)}\right).
\]

The exact inequalities \(r(2)<r(1)<r(4)\) follow respectively from \(e^{1/3}>4/3\) and \(\log(8/5)>9/20\). The first follows from \(e^x>1+x\) for positive \(x\); the latter follows from four terms of the alternating expansion of \(\log(1+3/5)\), whose lower bound is \(0.4596>0.45\). Thus there is an exact \(v\in(2,4)\) with \(r(v)=r(1)\). Taking one source with age \(1\), mass \(1\), and another central source with age \(v\), mass \(g(1)/g(v)>0\), produces *identical readings at both times*. Their third readings differ by the injectivity just proved. In contrast, knowing mass \(1\) resolves the ages from two readings. Adding the noncospherical fourth site \((0,0)\) makes one time sufficient.

## Verification

The standalone standard-library \(\texttt{checker.py}\) performs exact rational rank and reflection checks in dimensions \(1\) through \(5\); reconstructs separately Gaussian-source location, age, and uncalibrated mass from one snapshot of full-rank quadratic sensor arrays; and reconstructs noncentral sources using two rounds on co-spherical arrays. It also checks a strict numerical witness for a two-round ambiguity with unknown mass, the known-mass one-round ambiguity, and the log-ratio derivative signs underlying the sharp thresholds. All pseudo-random cases use an explicit fixed seed. Run in the same folder as \(\texttt{RESULT.md}\) with \(\texttt{python3 checker.py}\). Its finite tests supplement, and do not replace, the all-dimensional global proof in the previous section.

## Relationship to prior work

Lu, Dragotti and Vetterli (SampTA 2011, Sections 2–3; Allerton 2011, Section 3) already use the exact free-space diffusion kernel and recover unknown instantaneous sources from spatially distributed sensors, including \(d+1\)-sensor strategies. Their algorithms rely on multiple temporal samples and derivative, integral, or moment constraints; the inspected results do not give the **minimal numbers of raw concentration snapshots for every full-affine-span array**, including the central-source obstruction and a one-round saving from known mass. The new result does *not* claim that \(d+1\)-sensor localization or the Gaussian field equation is new.

Murray-Bruce and Dragotti (ICASSP 2014, Sections 3.1–3.3; IEEE TSP 2015; and the accessible dissertation treatment, Chapters 3–4) use reciprocity-gap and Prony-type reconstruction with aggregate spatiotemporal measurements, not this source-centered scalar three-versus-two-round boundary. Their broad source recovery makes novelty of general reconstructibility impossible to claim; only the exact minimal finite raw-snapshot classification is assessed.

A relevant published theorem on unknown-diffusivity pollutant puffs derives a sharper *spatial* obstruction: with both diffusivity and mass unknown, a cospherical array has an all-time source/diffusivity inversion symmetry. That theorem does **not** cover the present fixed, externally known \(D\) setting, where cospherical arrays become identifiable with exactly two or three finite rounds. A separate existing Gaussian-sensor result with known puff age and unknown anisotropic diffusion tensor treats quadratic interpolation with a different parameter regime, not the two-versus-three central-source threshold. These mathematical comparisons are comparisons of hypotheses and implications rather than titles. Historical priority over all possible inverse-heat-theory results cannot be established solely from this literature search.

## Limitations

The theorem is an exact, **noiseless and highly idealized** identifiability result; near-degenerate geometries, small spatial differences, or nearby central ages can be extremely ill-conditioned in realistic sensors. It does not provide finite-noise error bounds or a statistical optimal design, nor does it include unknown diffusivity, source mixtures, finite-duration releases, nonuniform transport, wind, boundaries, chemical decay, sensor calibration errors, or environmental background. The known-mass result specifically assumes an independent true mass calibration rather than merely an informative prior. The three-time guarantee requires distinct postrelease observation times and cannot be read as an instruction for actual atmospheric-monitoring deployment. Priority relative to broader inverse-source and parameter-identification theory is provisional and warrants independent literature assessment.

## References

1. Y. M. Lu, P. L. Dragotti, M. Vetterli, *Localizing Point Sources in Diffusion Fields from Spatiotemporal Samples*, SampTA 2011, May 2011. Full author-hosted text: https://www.commsp.ee.ic.ac.uk/~pld/publications/LuDV_SampTA2011.pdf . The meeting took place May 2–6, 2011: https://www.global-sci.com/cam/article/view/18944 .
2. Y. M. Lu, P. L. Dragotti, M. Vetterli, *Localization of Diffusive Sources Using Spatiotemporal Measurements*, Allerton 2011, DOI: 10.1109/ALLERTON.2011.6120286. Full author-hosted text: https://www.commsp.ee.ic.ac.uk/~pld/publications/AllertonPaper.pdf .
3. J. Murray-Bruce, P. L. Dragotti, *Spatio-Temporal Sampling and Reconstruction of Diffusion Fields Induced by Point Sources*, ICASSP 2014, DOI: 10.1109/ICASSP.2014.6853552. Full author-hosted text: https://www.commsp.ee.ic.ac.uk/~pld/publications/Murray-BruceD_ICASSP2014.pdf .
4. J. Murray-Bruce, P. L. Dragotti, *Estimating Localized Sources of Diffusion Fields Using Spatiotemporal Sensor Measurements*, IEEE Transactions on Signal Processing 63 (2015), 3018–3031, DOI: 10.1109/TSP.2015.2419187. Closely related dissertation chapters are available at https://theses.eurasip.org/wp-content/uploads/murray-bruce-john-sensing-physical-fields-inverse-problems-for-the-diffusion-equation-and-beyond.pdf .
5. *An Exact Hypersphere Obstruction and Minimal Two-Snapshot Sensor Theorem for an Unknown-Diffusivity Pollutant Puff* (2026), public research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-hypersphere-obstruction-and-minimal-two-snapshot-sensor--a9167f8e630b .
