# Sharp co-location threshold for two distance-decaying ecological detectors

## Finding
Consider an animal whose unknown location is uniform on a finite transect. Two independent detectors observe it with an exponentially decaying distance response and the same on-site detection probability. **The optimal pair is exactly co-located at the midpoint below a sharp detection-quality threshold, and separates symmetrically above it.** The transition is global, unique up to exchanging the detector labels, and has a linear separation onset. A singular perfect-detection limit produces quarter-point rather than midpoint placement on a short transect.

Specifically, let \(L,\lambda>0\), \(0<p\leq1\), and \(\ell=\lambda L\). With detector coordinates \(z_1,z_2\in[0,L]\), write \(P(z_1,z_2)\) for the probability of detecting the animal at least once. If
\[
p\leq e^{-\ell/2},
\]
then the unique unordered maximizing pair is \(\{L/2,L/2\}\). If \(p>e^{-\ell/2}\), the unique maximizing unordered pair is
\[
\left\{\frac{L-d_*/\lambda}{2},\frac{L+d_*/\lambda}{2}\right\},
\]
where \(d_*\in(0,\ell)\) is uniquely determined by
\[
p e^{\ell/2}=H(d_*),\qquad H(d)=\frac{2e^d\sinh(d/2)}{d},\quad H(0)=1.
\]
For \(0<p<1\), the critical dimensionless transect length is exactly \(\ell_c=2\log(1/p)\). On entering the separated phase, the dimensionless optimal gap obeys
\[
d_* = p e^{\ell/2}-1+O\bigl((p e^{\ell/2}-1)^2\bigr).
\]
For every fixed \(0<p<1\), sufficiently short dimensionless transects have two co-located midpoint detectors. At exactly \(p=1\), however, as \(\ell\downarrow0\) the normalized detector positions tend to \(1/4\) and \(3/4\). Thus the long-detection-range and perfect-on-site-detection limits do not commute. For fixed \(p>0\) as \(\ell\to\infty\), the optimal dimensionless gap satisfies
\[
d_*=\frac{\ell}{3}+\frac23\log\ell+\frac23\log(p/3)+o(1),
\]
so the two detector positions approach the one-third and two-thirds points.

## Assumptions and scope
A single animal has one fixed unknown location \(X\sim\operatorname{Uniform}[0,L]\). Conditional on \(X=x\), detector \(i\) at \(z_i\in[0,L]\) produces an independent binary detection with probability \(p e^{-\lambda|x-z_i|}\). Both probabilities have the same calibrated parameters \(0<p\leq1\) and \(\lambda>0\); distinct physical devices may occupy the same coordinate, and their detections remain conditionally independent. Detection occurs when either device responds. There are no false positives, inter-device interference, environmental heterogeneity, movement during the exposure, abundance-estimation requirements, or installation costs. The optimization is over **all** ordered pairs on the interval, not only symmetric pairs.

## Proof
Scale coordinates by \(\lambda\), so the habitat is \([0,\ell]\). By symmetry write sorted detector locations as \(a\leq b\), their center \(c=(a+b)/2\), and their gap \(d=b-a\). The feasible domain is \(0\leq d\leq\ell\) and \(d/2\leq c\leq\ell-d/2\). Integrating the conditional union probability over the uniform animal location gives the exact identity
\[
\begin{aligned}
\ell P(a,b)={}&4p-2p\cosh(d/2)\bigl(e^{-c}+e^{-(\ell-c)}\bigr)\\
 &-p^2e^{-d}(1+d)+\tfrac{p^2}{2}\bigl(e^{-2c}+e^{-2(\ell-c)}\bigr).
\end{aligned}
\tag{1}
\]
Indeed, each one-detector integral is \(2-e^{-a}-e^{-(\ell-a)}\). The product of the two distance kernels integrates exactly to
\[
e^{-d}(d+1)-\tfrac12\bigl(e^{-(a+b)}+e^{-(2\ell-a-b)}\bigr).
\]
This also establishes (1) when \(a=b\), including the boundary.

For fixed \(d\), differentiating (1) with respect to the center gives
\[
\partial_c(\ell P)=\bigl(e^{-c}-e^{-(\ell-c)}\bigr)
\left[2p\cosh(d/2)-p^2\bigl(e^{-c}+e^{-(\ell-c)}\bigr)\right].
\tag{2}
\]
The bracket is **strictly positive** for every feasible center: \(\cosh(d/2)\geq1\), \(p\leq1\), and \(e^{-c}+e^{-(\ell-c)}<2\) because \(\ell>0\). Hence (2) has the sign of \(\ell/2-c\). The sole center maximizing the probability for each fixed gap is therefore \(c=\ell/2\), including boundary gaps. This proves global centering, without a prior symmetry assumption.

Substituting \(c=\ell/2\) reduces (1) to the one-variable objective
\[
F(d)=4p-4p e^{-\ell/2}\cosh(d/2)-p^2e^{-d}(1+d)+p^2e^{-\ell},\quad 0\leq d\leq\ell.
\tag{3}
\]
Its derivative factors as
\[
F'(d)=p d e^{-d}\bigl[p-e^{-\ell/2}H(d)\bigr],\qquad
H(d)=e^d\frac{\sinh(d/2)}{d/2}.
\tag{4}
\]
The function \(H\) is strictly increasing on \((0,\infty)\), because \(e^d\) and \(\sinh(d/2)/(d/2)\) are strictly increasing and positive. Continuously, \(H(0)=1\). Also
\[
e^{-\ell/2}H(\ell)=\frac{e^\ell-1}{\ell}>1\geq p,
\]
so \(F'(\ell)<0\) for all admissible parameters. If \(p\leq e^{-\ell/2}\), (4) is negative on \((0,\ell]\): \(d=0\) is the unique optimum. Otherwise (4) changes sign exactly once from positive to negative, because \(H\) is strictly increasing from 1 past \(p e^{\ell/2}\) before \(\ell\). Thus the root \(d_*\) is the unique global maximizer, proving the complete classification.

For the transition law, \(H(d)=1+d+13d^2/24+O(d^3)\) near zero. Inverting at \(p e^{\ell/2}=1+\varepsilon\) yields \(d_*=\varepsilon+O(\varepsilon^2)\) for \(\varepsilon\downarrow0\). For \(0<p<1\), the co-location condition is equivalent to \(\ell\leq2\log(1/p)\). At \(p=1\), \(H(d_*)=e^{\ell/2}\), so the same small-argument expansion implies \(d_*/\ell\to1/2\) as \(\ell\downarrow0\), placing the devices asymptotically at quarters; for each fixed \(p<1\), \(\ell\downarrow0\) instead forces exact midpoint co-location.

Finally, for fixed \(p>0\) and \(\ell\to\infty\), the root must satisfy \(d_*\to\infty\). Using \(H(d)=e^{3d/2}(1-e^{-d})/d\), taking logarithms in \(H(d_*)=p e^{\ell/2}\), and first obtaining \(d_*/\ell\to1/3\), then substituting \(\log d_* = \log\ell-\log3+o(1)\), yields the stated expansion. This proves every asserted quantifier and asymptotic regime.

## Verification
The standalone `verify.py` reproduces the closed integral by independent midpoint quadrature, tests randomly generated unconstrained placements against the analytical optimum, checks the centering reduction, tests the exact root/phase classification, probes both noncommuting limits, and verifies benchmark calculations. Run `python verify.py > verification_output.json` in the extracted package. The provided `verification_output.json` is the actual replayed output. The verifier uses only the Python standard library. Its **13,036 finite assertions** are diagnostics, not substitutes for the analytical global theorem and limiting proofs above.

For a transect with \(\lambda L=2\) and \(p=0.7\), the optimal dimensionless gap is \(d_*\approx0.626998110087\), giving detector coordinates \(\lambda z_1\approx0.686500945\) and \(\lambda z_2\approx1.313499055\). The predicted detection probability is \(0.679671811520\); exact midpoint co-location instead gives \(0.673125926753\).

## Relationship to prior work
The primary biological motivation is Sun, Fuller and Royle (2014), who examine spatial animal capture–recapture detection and clustered versus regular arrays with different baseline detection probabilities. Their complete accessible article analyzes parameter-estimation accuracy by simulation under a different, half-normal distance kernel; its conclusions neither optimize the probability of a **single encounter** for two freely placed devices on a uniform transect nor supply the present threshold and limiting classification. Michaelides and Panayiotou (2011) study collaborative pairs of sensors with space-correlated received signals and false-alarm-controlled fusion decisions. They compare pair separation, but neither use the independent Bernoulli exponential-absolute-distance response nor derive this exact global placement theorem.

Litvak and coauthors, *Increasing Detection Performance of Surveillance Sensor Networks*, Section 5.2.1, prove a no-overlap principle for uniform object locations and two fixed-radius, constant-within-footprint sensors; those fixed-range discontinuous kernels do not imply a phase in which the optimal continuous-decay devices coincide. Frasca and coauthors (2014) minimize expected worst-case distance to the closest active sensor under complete device failures, not the expected binary detection probability of an unknown uniformly placed animal. A closely related published discrete-path two-trap optimization theorem with response \(q^{|i-a|}\) assumes certain on-site detection, disallows co-location, and places detectors at discrete sites; its fixed-range one-third and long-range quarter limits are acknowledged here. It does not imply a strictly imperfect on-site response, global continuous co-location, or the sharp continuous \(p=e^{-\ell/2}\) transition. Related unpublished Gaussian/half-normal detector calculations similarly concern a different location law and squared-distance response and do not imply the exact compact-uniform exponential-absolute-distance result. These are mathematical implication comparisons, not proof of absolute bibliographic novelty.

## Limitations
The model assumes conditional independence even for co-located devices. Common disturbances, correlated false negatives, camera occlusion, target movement, heterogeneous habitats, abundance-estimation objectives and restrictions forbidding co-location can change the optimal design. The result is an idealized probability-of-at-least-one-encounter benchmark, not an empirical recommendation for specific wildlife species or a statement about capture–recapture estimator precision. The sharp threshold is kernel-specific. Historical priority remains provisional for alternative formulations in probabilistic coverage and facility location, and no independent scientific audit has been performed.

## References
1. M. Michaelides and C. G. Panayiotou, *Improved coverage in WSNs by exploiting spatial correlation: the two sensor case*, EURASIP Journal on Advances in Signal Processing (2011), article 11; online 2011-06-10, https://doi.org/10.1186/1687-6180-2011-11 (complete open primary text inspected).
2. C. C. Sun, A. K. Fuller, and J. A. Royle, *Trap Configuration and Spacing Influences Parameter Estimates in Spatial Capture-Recapture Models*, PLOS ONE 9 (2014), e88025; online 2014-02-05, https://doi.org/10.1371/journal.pone.0088025 (complete open primary text inspected, including methods and discussion).
3. P. Frasca, F. Garin, B. Gerencsér, and J. M. Hendrickx, *Optimal One-Dimensional Coverage by Unreliable Sensors*, https://arxiv.org/abs/1404.7711, first submitted 2014-04-30 (accessible primary preprint inspected).
4. N. Litvak and collaborators, *Increasing Detection Performance of Surveillance Sensor Networks*, in Mathematics with Industry report, Section 5.2.1, https://miis.maths.ox.ac.uk/268/2/thales-report.pdf (primary PDF text and page image inspected; precise original public release date not established).
5. *Noncommuting detection-range and landscape-size limits for two ecological traps* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-noncommuting-detection-range-and-landscape-size-limits-for-two-e--4b47353a8a35 (complete publicly accessible scientific result inspected; different discrete, certain-on-site, distinct-trap model).
