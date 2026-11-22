# Sharp single-snapshot sensor geometry for an anisotropic Gaussian contaminant puff

## Finding
Let \(d\ge1\), and put \(q=(d+1)(d+2)/2\). For a single ideal, instantaneous, zero-advection, freely diffusing contaminant release with *known age* \(\tau>0\), unknown center \(\mu\in\mathbb R^d\), unknown mass \(M>0\), and unknown arbitrary constant symmetric positive-definite diffusion tensor \(D\), concentration measurements at fixed positions \(x_1,\ldots,x_N\) uniquely determine all three unknowns **for every permissible release** if and only if the only real polynomial of total degree at most two vanishing on all sensors is the zero polynomial. Therefore \(N\ge q\) is necessary, and \(q\) suitably placed sensors suffice. For \(d=2\) this means six sensors; they must not all lie on a real conic (including degenerate conics).

With \(q\) such sensors at two different known clock times, the unknown release time can also be reconstructed uniquely, provided both readings follow the release. In contrast, when the release time is unknown, even an entire noiseless spatial concentration field at one clock time cannot determine the diffusion tensor and release time separately. These statements are exact within the stated model and do not imply statistical stability under noise.

## Assumptions and scope
The instantaneous release occurs at clock time \(t_0\). For \(t>t_0\), write \(\tau=t-t_0\), and define
\[
 C(x,t)=\frac{M}{(4\pi\tau)^{d/2}\sqrt{\det D}}\exp\left[-\frac{(x-\mu)^TD^{-1}(x-\mu)}{4\tau}\right].
\]
The ambient space is \(\mathbb R^d\), with no walls, ambient background, reaction, finite sensor footprint, advection or model error. Sensors record exact positive point concentrations, with calibrated common units. Diffusion tensor \(D\) is arbitrary symmetric positive definite, and \(M>0\) and \(\mu\) are unrestricted. The geometric necessity and sufficiency statement concerns a **single snapshot of known age**. The two-snapshot statement concerns a known clock at which the release time is unknown, and does not assert minimal sensor count for that different problem.

A set of locations is *quadratically unisolvent* if its evaluation map on polynomials \(P(x)=a+b^Tx+x^TGx\), \(G=G^T\), has zero kernel. The dimension of that polynomial space is \(q\).

## Proof
**1. Linearization and admissible coefficient cone.** The logarithm of one snapshot is
\[
 \log C(x,t)=a+b^Tx-\frac12x^THx,
 \quad H=(2\tau D)^{-1}\succ0,\quad b=H\mu,
\]
where \(a=\log M-\frac d2\log(2\pi)-\frac12\log\det(H^{-1})-\frac12\mu^TH\mu\). Conversely, every real \(a,b\) and positive-definite symmetric \(H\) come from exactly one permissible \((\mu,D,M)\) at fixed \(\tau\), namely
\[
 \mu=H^{-1}b,\qquad D=\frac{H^{-1}}{2\tau},\qquad
 M=\exp(a+\tfrac12b^TH^{-1}b)(2\pi)^{d/2}\sqrt{\det(H^{-1})}.
\]
In particular, permissible polynomial coefficients form a nonempty open subset of the \(q\)-dimensional coefficient space.

**2. Exact spatial criterion and sharp count.** At any \(N\) locations, the vector of log concentrations is the linear evaluation of the quadratic polynomial above. If evaluation is injective on all quadratics, the coefficients, hence \(\mu,D,M\), are unique. Conversely, if a nonzero quadratic \(P\) vanishes on all sensors, add \(\varepsilon P\) to an admissible log profile. For all sufficiently small nonzero real \(\varepsilon\), the new quadratic term remains negative definite, so the modified log profile corresponds to distinct admissible physical parameters while giving precisely the same sensor data. Thus lack of unisolvency is actual nonidentifiability, not merely failure of a particular algorithm. Since the polynomial space has dimension \(q\), \(N<q\) always has a nonzero evaluation kernel.

**3. Constructive sharpness.** For every \(d\), take the \(q\) points \(0\), each coordinate unit point \(e_i\), each doubled point \(2e_i\), and each pair-sum \(e_i+e_j\) with \(i<j\). If a quadratic \(P\) vanishes there, the origin gives its constant term zero. Evaluation at \(e_i,2e_i\) forces the linear and pure-square coefficients in coordinate \(i\) to zero; then each \(e_i+e_j\) forces the mixed coefficient to zero. Hence \(P=0\) and \(q\) suffices. For \(d=2\), \(q=6\), and the failed-unisolvency condition means that a nonzero real quadratic curve passes through all the sites, with degenerate curves included.

**4. Unknown release time and the temporal distinction.** Let \(t_1<t_2\) be known clock times later than the unknown \(t_0\), and reconstruct \(H_1,H_2\) independently from the same quadratically unisolvent sensor array. Then
\[
 H_1=\frac{D^{-1}}{2(t_1-t_0)},\qquad
 H_2=\frac{D^{-1}}{2(t_2-t_0)},\qquad
 H_1=\rho H_2,
\]
with the uniquely observed \(\rho=(t_2-t_0)/(t_1-t_0)>1\). Therefore
\[
 t_0=\frac{\rho t_1-t_2}{\rho-1},\qquad
 D=\frac{H_1^{-1}}{2(t_1-t_0)}.
\]
The spatial formulas then uniquely determine \(\mu,M\). Conversely, at a single clock time \(t\), for any new positive age \(\tau'\), the changed release time \(t-\tau'\) and diffusion tensor \(D'=\tau D/\tau'\) give the same entire spatial field with the same \(M,\mu\), since \(\tau'D'=\tau D\). This proves impossibility of identifying release time from one snapshot even with infinitely many perfectly measured locations.

## Verification
The standalone `checker.py` (Python 3, NumPy, SymPy) tests explicit exact nonzero interpolation determinants in dimensions \(1\)–\(4\), numerical parameter recovery over random positive-definite tensors, release-time formulas, one-snapshot time-diffusion ambiguity, and a rational planar six-sensor conic with an exact quadratic null vector. Running `python checker.py` produced `PASS: 1509 checks, 4 exact full-rank constructions, conic nullspace, inversion, release-time alias`. These finite diagnostics supplement but are not substitutes for the proof, which covers every integer \(d\ge1\) and every admissible parameter value.

## Relationship to prior work
Lushi and Stockie (public arXiv version 11 August 2009) solve a Gaussian-plume inverse emission-rate problem with known source locations and prescribed dispersion; its linear systems in emission rates do not imply a universal, exact sensor-rank characterization for a single unknown full diffusion tensor and source center. Korsakissok and Mallet (2010) study Gaussian-puff coupling and parameterization, not this exact finite-sensor identification question. Konda et al. (2010) analyze uncertainty propagation in Gaussian puff models rather than exact identification. A related indexed mathematical finding on *isotropic* unknown-diffusivity puffs identifies a different two-time sensor count and a sphere/hyperplane obstruction: the present full-anisotropic, **one-known-age-snapshot** rank characterization is not a corollary of its isotropic result, and no minimality claim is made here for the two-time anisotropic problem. The logarithmic polynomial reduction is classical; novelty is asserted narrowly for the combined sharp physical inverse-design statement, subject to further literature verification.

## Limitations
This is a noiseless ideal-Gaussian model without drift, boundaries, mixtures, attenuation or evolving tensor. Rank does not guarantee good numerical conditioning. The two-snapshot result supplies a sufficient design, not a sharp minimum number of sites. Closely related general multivariate-normal interpolation methods may yield the same mathematical criterion; no exhaustive historical priority claim is made. There is no independent scientific audit.

## References
1. E. Lushi and J. M. Stockie, *An inverse Gaussian plume approach for estimating atmospheric pollutant emissions from multiple point sources*, public arXiv preprint dated 2009-08-11, https://arxiv.org/abs/0908.1589, DOI: 10.1016/j.atmosenv.2009.11.039.
2. I. Korsakissok and V. Mallet, *Subgrid-scale treatment for major point sources in an Eulerian model*, first published 2010-02-11, https://doi.org/10.1029/2009JD012734.
3. U. Konda, T. Singh, P. Singla, and P. Scott, *Uncertainty propagation in puff-based dispersion models using polynomial chaos*, *Environmental Modelling & Software* (2010), https://doi.org/10.1016/j.envsoft.2010.04.005.
