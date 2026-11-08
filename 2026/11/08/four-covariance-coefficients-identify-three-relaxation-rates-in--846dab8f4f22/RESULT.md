# Four covariance coefficients identify three relaxation rates in an actively reset harmonic particle

## Finding

Consider the two-dimensional active Brownian particle whose position and orientation are jointly reset at Poisson rate \(r\) to \((0,0,0)\), with a harmonic trap, propulsion speed \(v\), translational diffusivity \(D\), and rotational diffusivity \(d\). Suppose \(v>0\) and \(D>0\) are known, while the trap relaxation rate \(\beta>0\), rotational diffusivity \(d>0\), and resetting rate \(r>0\) are unknown.

**Theorem.** The four right derivatives \(c_j=C^{(j)}(0+)\), \(j=0,1,2,3\), of the *stationary transverse positional autocovariance* \(C(t)=\operatorname{Cov}(Y_0,Y_t)\) determine the ordered triple \((r,\beta,d)\) uniquely. The reconstruction is explicit and works without excluding equal rates or cancellation of a relaxation mode.

In particular,
\[
r=-\frac{2(c_1+D)}{c_0}.
\]
If \(\Delta=c_0c_2-c_1^2\ne0\), put
\[
S=\frac{c_1c_2-c_0c_3}{\Delta},\qquad
P=\frac{c_1c_3-c_2^2}{\Delta}.
\]
The roots of \(z^2-Sz+P\) are precisely \(r+\beta\) and \(r+d\), counted with multiplicity. The known propulsion and thermal parameters, together with \(c_0\), uniquely assign the roots to their physical meanings. If \(\Delta=0\), there is exactly one visible exponential, but the hidden trap rate is still uniquely recoverable by a positive quadratic root (shown below).

An exact cancellation example is \((r,\beta,d,v,D)=(1,3,1,5,3/2)\): the transverse covariance is simply \(C(t)=e^{-2t}\), yet all three rates are uniquely determined under the calibration assumptions. Thus ordinary pole counting alone would incorrectly treat the trap rate as unrecoverable.

## Assumptions and scope

The position \((X_t,Y_t)\in\mathbb R^2\) and orientation \(\theta_t\in\mathbb R/(2\pi\mathbb Z)\) evolve between resets as
\[
\begin{aligned}
dX_t&=(-\beta X_t+v\cos\theta_t)\,dt+\sqrt{2D}\,dB_t^{(1)},\\
dY_t&=(-\beta Y_t+v\sin\theta_t)\,dt+\sqrt{2D}\,dB_t^{(2)},\\
d\theta_t&=\sqrt{2d}\,dW_t\pmod{2\pi},
\end{aligned}
\]
where the three Brownian motions and the rate-\(r\) reset clock are independent. At each reset the entire state becomes \((X,Y,\theta)=(0,0,0)\). Time is physical time. All five parameters are finite; \(r,\beta,d,v,D>0\). The observation \(Y\) is transverse to the fixed reset orientation. The covariances and their right derivatives refer to the unique stationary law.

For concise formulas define
\[
\begin{aligned}
q&=\mathbb E[\sin^2\theta]=\frac{2d}{r+4d},\\
h&=\mathbb E[Y\sin\theta]=\frac{vq}{\beta+d+r}>0,\\
V&=\mathbb E[Y^2]=\frac{2D+2vh}{2\beta+r}>0.
\end{aligned}
\]
Here \(\mathbb E[Y]=\mathbb E[\sin\theta]=0\), so \(V=C(0)\). The covariance has the explicit representation, valid for every \(t\ge0\),
\[
C(t)=Ve^{-(r+\beta)t}+vh\int_0^t e^{-(r+\beta)(t-s)}e^{-(r+d)s}\,ds.
\]
For unequal rates the integral is \((e^{-(r+d)t}-e^{-(r+\beta)t})/(\beta-d)\); for equal rates it is \(t e^{-(r+\beta)t}\). No use is made of long-time asymptotic fitting or of observations of the orientation itself.

## Proof

**1. Stationarity and moments.** The full process restarts independently from its fixed state at every exponential reset. Its renewal construction gives a unique stationary law by mixing an independent between-reset trajectory over an exponential age. All moments used below are finite because \(\beta>0\), \(v<\infty\), \(D<\infty\), and the orientation is bounded. Symmetry under \((Y,\theta)\mapsto(-Y,-\theta)\) gives zero transverse mean.

The generator acting on a smooth observable \(f\) is
\[
\mathcal Lf=(-\beta X+v\cos\theta)\partial_X f+(-\beta Y+v\sin\theta)\partial_Yf+D(\partial_{XX}+\partial_{YY})f+d\partial_{\theta\theta}f+r\bigl(f(0,0,0)-f\bigr).
\]
Applying the stationarity equation \(\mathbb E[\mathcal Lf]=0\) to \(\cos2\theta\), \(Y\sin\theta\), and \(Y^2\) gives respectively
\[
(r+4d)\mathbb E[\cos2\theta]=r,\quad
(\beta+d+r)h=vq,\quad
(2\beta+r)V=2D+2vh.
\]
They prove the formulas above, including strict positivity of \(h,V\).

**2. Closed lag evolution and reset-rate recovery.** Let \(H(t)=\mathbb E[Y_0\sin\theta_t]\) under stationarity. The Markov property and the reset generator give
\[
H'(t)=-(r+d)H(t),\qquad
C'(t)=-(r+\beta)C(t)+vH(t),
\]
with \(H(0)=h\) and \(C(0)=V\). Their solution is the stated convolution formula and satisfies
\[
C''+(\beta+d+2r)C'+(\beta+r)(d+r)C=0.
\]
At the right endpoint, stationarity of \(Y^2\) yields the universal slope
\[
c_1=-(\beta+r)V+vh=-D-\frac r2V.
\]
Since \(V=c_0>0\), the displayed formula determines \(r\) uniquely, independently of \(\beta,d,v\).

**3. Two visible modes, including the repeated-root case.** When \(\Delta\ne0\), evaluate the second-order lag equation and its derivative at \(t=0+\). The resulting nonsingular two-by-two system determines the sum and product of its characteristic rates. Elementary elimination gives exactly \(S,P\) displayed in the theorem. The two roots are therefore \(\lambda_1=r+\beta\) and \(\lambda_2=r+d\). In case of a double root, \(\beta=d\) and both are recovered. Indeed, for \(\beta=d\), the covariance is \((V+vh\,t)e^{-(r+\beta)t}\), whose determinant satisfies \(\Delta=-(vh)^2<0\), so it is not confused with a single exponential.

For distinct roots, only their assignment remains. The stationary variance calculated in step 1 is the known-parameter function
\[
\mathcal V(\beta,d)=\frac{2D+\dfrac{4v^2d}{(r+4d)(r+\beta+d)}}{2\beta+r}.
\]
For fixed \(r,v,D\) and a fixed unordered pair \(\{\beta,d\}\), if \(\beta>d\) then
\[
\mathcal V(\beta,d)<\mathcal V(d,\beta).
\]
This follows because \(z/(r+4z)\) is strictly increasing on \(z>0\), the factor \(r+\beta+d\) is unchanged by swapping, and the denominator \(2\beta+r\) is larger for the first ordering. Thus the two candidate orderings predict *different* variances. Exactly one agrees with the observed \(V=c_0\), proving their unique physical assignment.

**4. Hidden-pole cancellation.** If \(\Delta=0\), write the unequal-rate covariance as \(Ae^{-(r+\beta)t}+Be^{-(r+d)t}\), where
\[
B=\frac{vh}{\beta-d}\ne0,\qquad A=V-B.
\]
Then \(\Delta=AB(\beta-d)^2\). The equal-rate case has already been excluded because its determinant is negative. Hence \(A=0\) and \(C(t)=Ve^{-(r+d)t}\). Its visible decay is \(\lambda=-c_1/c_0=r+d\), so \(d=\lambda-r\) is known. The equality \(A=0\) becomes \(V(\beta-d)=vh\). Substituting \(h\) from step 1 yields
\[
(\beta-d)(\beta+d+r)=\frac{2v^2d}{V(r+4d)}=:K>0.
\]
There is a unique root \(\beta>d\), given by
\[
\beta=\frac{-r+\sqrt{(r+2d)^2+4K}}2.
\]
Thus even an exactly cancelled pole cannot conceal its trap rate. Steps 2–4 exhaust all positive parameters and prove injectivity of the four-jet parameter map.

**5. Rational cancellation witness.** At \((r,\beta,d,v,D)=(1,3,1,5,3/2)\), the formulas give \(q=2/5\), \(h=2/5\), \(V=1\), and \(vh=2\). Consequently
\[
C(t)=e^{-4t}+\frac{2}{2}(e^{-2t}-e^{-4t})=e^{-2t}.
\]
The apparent single mode has \(\lambda=2\). The slope yields \(r=1\), hence \(d=1\), and the positive quadratic root above yields \(\beta=3\).

## Verification

The standalone script `check.py` uses exact rational arithmetic for generator identities, the fourth-order derivative reconstruction and special-rate cases. It also constructs independently the finite-dimensional stationary moment generator and the conditional correlation semigroup, comparing them with the closed formulas through matrix exponentials. Executing `python check.py` in an environment with Python 3, NumPy and SciPy printed `PASS: 1409 exact/rational/numerical checks`. The script includes both a pole-cancellation case and a repeated-pole case. These diagnostics are finite consistency checks, not substitutes for steps 1–4 of the proof.

## Relationship to prior work

Shee (arXiv:2409.06920, first submitted September 11, 2024) analyzes the same jointly reset active Brownian particle in a harmonic trap and provides its fixed-time position moments, orientation correlations and kurtosis. The current theorem credits that model and its basic moment framework; its new object is the *stationary transverse two-time positional autocovariance* used for complete inverse recovery of the three hidden rates from a four-jet, including mode cancellation. Caraglio and Franosch (arXiv:2210.04205, 2022) give an exact positional autocorrelation for a harmonically trapped active Brownian particle **without resetting**, and Kumar, Sadekar and Basu (arXiv:2008.03294, 2020) study complete resetting **without harmonic trapping**. The analyzed texts do not state the reset-plus-trap three-rate inverse classification through these four derivatives. Their forward generators and moment identities motivate the reconstruction but do not themselves prove parameter injectivity or resolve its hidden-mode case. The algebraic spectral reconstruction is related to classical Prony-type identification; that generic method is not claimed as new. Originality priority would require independent broader verification.

## Limitations

The result assumes exact stationary ensemble covariances and exact right derivatives up to order three, with *known positive* \(v,D\). It provides structural identifiability, **not** stable recovery from discretely sampled or noisy trajectories: near merged poles or vanishing modal amplitudes the inversion can be poorly conditioned. It does not address resetting only position, resetting to a random orientation, unknown propulsion/diffusivity, imperfect time resolution, or general confining potentials. The exact claims are proved analytically; numerical diagnostics cannot certify novelty or infinite-parameter correctness independently.

## References

- Amir Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1, September 11, 2024. https://arxiv.org/abs/2409.06920
- Michele Caraglio and Thomas Franosch, *Analytic Solution of an Active Brownian Particle in a Harmonic Well*, arXiv:2210.04205v1, October 9, 2022. https://arxiv.org/abs/2210.04205
- Vijay Kumar, Onkar Sadekar and Urna Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294v1, August 7, 2020. https://arxiv.org/abs/2008.03294
