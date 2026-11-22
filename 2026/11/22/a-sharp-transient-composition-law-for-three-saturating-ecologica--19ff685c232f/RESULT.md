# A sharp transient-composition law for three saturating ecological markers

## Finding

Consider three taxonomic marker classes with different saturating accumulation rates. Although the absolute detected amount in **each** class increases strictly with sampling duration, the intermediate-rate class can have a unique transient maximum in its share of a fixed-depth sequencing library. The exact criterion holds for **all** three ordered positive rates; an equal-endpoint regime permits a sharp amplification factor approaching the ratio of the two slower rates.

Precisely, let \(0<\lambda_1<\lambda_2<\lambda_3\), \(a,b,c>0\), \(t>0\), and
\[
M_1(t)=a(1-e^{-\lambda_1t}),\qquad M_2(t)=b(1-e^{-\lambda_2t}),\qquad M_3(t)=c(1-e^{-\lambda_3t}).
\]
Define the middle-class library share and its detection probability under exactly \(n\ge1\) independent reads by
\[
p(t)=\frac{M_2(t)}{M_1(t)+M_2(t)+M_3(t)},\qquad P_n(t)=1-(1-p(t))^n.
\]
Write \(m=\lambda_2/\lambda_1\), \(r=\lambda_3/\lambda_1\), so \(1<m<r\), and set
\[
\Theta=\frac{r(r-m)}{m-1}=\frac{\lambda_3(\lambda_3-\lambda_2)}{\lambda_1(\lambda_2-\lambda_1)}.
\]
Then:

1. **Unique transient optimum exactly under a sharp condition.** If \(a/c<\Theta\), \(p(t)\) and every \(P_n(t)\) increase strictly up to one common finite \(t_*>0\) and decrease strictly thereafter. If \(a/c\ge\Theta\), they are strictly decreasing for every \(t>0\), with no positive-time optimizer. The finite optimum depends on \(a/c\) and the three rates, but **not** on \(b\) or sequencing depth \(n\).
2. **Identical endpoint compositions can hide a peak.** The short-time limit \(p(0+)\) equals the long-time limit \(p(\infty)\) if and only if
\[
\frac ac=\frac{r-m}{m-1}=\frac{\lambda_3-\lambda_2}{\lambda_2-\lambda_1}.
\]
Under this condition the unique interior peak always exists and its amplification factor satisfies
\[
1<\frac{p(t_*)}{p(0+)}<m=\frac{\lambda_2}{\lambda_1}.
\]
For every fixed \(m>1\), the constant \(m\) is sharp over all \(r>m\), even with fixed positive \(b,c\) and the matching \(a\). For every fixed integer \(n\ge1\), the corresponding detection-probability ratio obeys the same strict bound and approaches \(m\) in that sharpness family.
3. **Minimality.** With only two positive classes of the same independent-saturation form, either normalized class share is monotone in duration (or constant for equal rates). Thus three distinct capture rates are necessary for a strict interior composition peak within this model.

## Assumptions and scope

The three classes have fixed positive saturation plateaus \(a,b,c\) and independent monotone accumulation responses. The biological population and its ambient marker supply do not change during sampling. Sequencing is idealized as \(n\) independent draws, conditional on exactly \(n\) usable reads, with each class's read probability proportional to its captured marker amount. Any fixed class-specific amplification factor can be absorbed into its plateau coefficient. The model does not describe coupled substrate competition, fluctuating read depth, taxonomic misassignment, degradation after capture, or time-varying field abundance.

At exact zero duration all three amounts vanish, so \(p(0+)\) and \(P_n(0+)\) denote mathematical limits for a conditional fixed-depth sequencing experiment, **not** actual read recovery at zero duration. All inequalities and the unique optimizer concern \(t>0\). Time units are set by the \(\lambda_i\).

## Proof

For \(q=e^{-\lambda_1t}\in(0,1)\), set
\[
S_v(q)=\frac{1-q^v}{1-q},\qquad v>1.
\]
Canceling the common factor \(1-q\) in all three captured amounts gives
\[
p(t)=\frac{bS_m(q)}{a+bS_m(q)+cS_r(q)}.
\]
Each \(S_v\) increases strictly from \(S_v(0)=1\) to \(S_v(1)=v\). The derivative \(S_v'(q)\) is positive, as follows from the integral identity
\[
S_v(q)=v\int_0^1[q+(1-q)u]^{v-1}\,du.
\]
For \(v>1\), differentiating under the integral yields
\[
S_v'(q)=\frac{v(v-1)}{(1-q)^2}\int_q^1(1-y)y^{v-2}\,dy.
\]
For \(r>m>1\), the ratio
\[
R(q)=\frac{S_r'(q)}{S_m'(q)}=\frac{r(r-1)}{m(m-1)}\frac{\int_q^1(1-y)y^{m-2}y^{r-m}\,dy}{\int_q^1(1-y)y^{m-2}\,dy}
\]
is **strictly increasing** in \(q\). Indeed it is a positive constant times the mean of the strictly increasing function \(y^{r-m}\) under a positive weight, conditional on \(y\ge q\); differentiating this truncated mean gives a positive multiple of its excess over the boundary value \(q^{r-m}\).

Define
\[
H(q)=S_m(q)R(q)-S_r(q).
\]
Because \(S_m'=S_r'/R\), exact differentiation gives \(H'(q)=S_m(q)R'(q)>0\). Using \(S_v(0)=S_v'(0)=1\) and \(S_v(1)=v\), \(S_v'(1)=v(v-1)/2\) (one-sided values),
\[
H(0)=0,\qquad H(1)=\frac{r(r-m)}{m-1}=\Theta.
\]
Now differentiating the quotient with respect to \(q\) gives the exact factorization
\[
\frac{dp}{dq}=\frac{bS_m'(q)\bigl(a-cH(q)\bigr)}{\bigl(a+bS_m(q)+cS_r(q)\bigr)^2}.
\]
Since \(dq/dt=-\lambda_1q<0\), the time derivative has sign \(cH(q)-a\). The strict monotonicity and endpoint range of \(H\) imply precisely one sign change if \(0<a/c<\Theta\), and a strictly negative derivative for all positive times otherwise. Hence the unique finite maximum is at
\[
t_*=-\frac{\log q_*}{\lambda_1},\qquad H(q_*)=a/c,\quad 0<q_*<1.
\]
Because \(x\mapsto1-(1-x)^n\) is strictly increasing on \((0,1)\), \(P_n\) has exactly the same optimum and monotonicity.

For the endpoint comparison, the limits of the uncanceled saturation expressions are
\[
p(0+)=\frac{bm}{a+bm+cr},\qquad p(\infty)=\frac b{a+b+c}.
\]
Cross multiplication proves endpoint equality exactly when \((m-1)a=(r-m)c\). This positive ratio is strictly below \(\Theta\), since \(r>1\), so there is a unique strict interior peak. For any \(0<q<1\), \(S_m(q)<m\) and \(a+bS_m(q)+cS_r(q)>a+b+c\), giving \(p(t)/p(\infty)<m\). Equality of endpoint shares gives the claimed strict two-sided amplification bound.

To show sharpness, fix \(m>1\) and fixed \(b,c>0\); let \(r\to\infty\) and \(a=c(r-m)/(m-1)\), and evaluate at \(q_r=1-r^{-1/2}\). Then \(S_m(q_r)\to m\), \(S_r(q_r)\le\sqrt r\), and \(a\sim cr/(m-1)\); therefore \(p(q_r)/p(\infty)\to m\). Since the optimal ratio is larger than this evaluated ratio but strictly less than \(m\), its limit is \(m\). For the read-detection ratio, \(p(0+)\to0\) and \(p(q_r)\to0\), so \(1-(1-x)^n\sim nx\) for every fixed \(n\), giving the same limiting factor. Concavity of \(1-(1-x)^n\) and its zero intercept imply its ratio between two positive arguments is no greater than the arguments' ratio, proving the strict upper bound for every finite \(r\).

Finally, for two classes with rates \(\alpha\ne\beta\), the derivative of the logarithm of their captured-mass ratio is
\[
\frac\alpha{e^{\alpha t}-1}-\frac\beta{e^{\beta t}-1},
\]
which has a constant strict sign because \(z/(e^z-1)\) is strictly decreasing for \(z>0\). Therefore two-class shares cannot have interior strict extrema. This proves minimality.

## Verification

For the exact three-rate example \((\lambda_1,\lambda_2,\lambda_3)=(1,2,3)\), \(a=b=c=1\), the endpoints are both \(1/3\), while \(H(q)=2q+q^2\). Thus
\[
q_*=\sqrt2-1,\quad t_*=\log(1+\sqrt2),\quad p(t_*)=\frac{\sqrt2}{4},\quad \frac{p(t_*)}{p(0+)}=\frac{3\sqrt2}{4}>1.
\]
A more separated example, \((m,r,a,b,c)=(5,50,45/4,1,1)\), has both endpoint shares equal to \(4/53\), with a unique maximum near \(t=0.189572\) when \(\lambda_1=1\), of approximately \(0.172269\) (about \(2.283\) times its endpoint level).

Run `python3 check.py` using only the Python standard library. It checks the exact derivative factorization numerically, strict monotonicity of the scalar threshold, the unique-maximum regimes, endpoint matching, the strict bound, and sharpness examples. Numerical tests supplement, but do not replace, the preceding analytic proof.

## Relationship to prior work

Ledger et al. (2024) use three fish species to validate proportional metabarcoding estimates and show how a qPCR reference can recover absolute marker concentrations. Their investigation concerns abundance calibration, PCR bias and controlled mixed-species trials; it does not introduce the present time-varying three-saturation model or derive its threshold and sharp amplification.

Courtaillac et al. (2024) study spatial/temporal replication and pooled-versus-individual eDNA sample detection. Gloor et al. (2017) explain the established compositional-data problem. Those concepts motivate the model, but their inspected results do not imply the unique peak criterion or its optimal-ratio bound. Published work on passive samplers has observed changing relative frequencies with deployment time; the present assertion is a model-specific exact theorem, not a claim of first discovery of compositional bias or transient compositional changes.

## Limitations

The mathematical result holds for independent simple exponential saturation classes and fixed, conditional sequencing depth. No empirical rate fitting or substrate-competition model is supplied. For real field sampling, zero-duration library recovery is not feasible, and availability of enough reads is itself duration-dependent. Nonlinear cross-species capture competition, loss of captured material and changes in surrounding biomass can alter the optimum, its uniqueness and its bound. Neither a universal real-world optimal sampling duration nor a general theorem for arbitrary uptake kernels is claimed. Independent external scientific validation has not been performed.

## References

- Ledger, K. J., et al. (2024). *Validation of Environmental DNA for Estimating Proportional and Absolute Biomass*. Environmental DNA. First published 2024-10-26. https://doi.org/10.1002/edn3.70030
- Courtaillac, K.-L., et al. (2024). *The Effect of Spatio-Temporal Sampling and Biological Replication on the Detection of Kelp Forest Fish Communities Using eDNA Metabarcoding*. Environmental DNA. First published 2024-10-14. https://doi.org/10.1002/edn3.70023
- Gloor, G. B., et al. (2017). *Microbiome Datasets Are Compositional: And This Is Not Optional*. Frontiers in Microbiology 8:2224. https://doi.org/10.3389/fmicb.2017.02224
- von Ammon, U., et al. (2025). *Investigating passive eDNA samplers and submergence times for marine surveillance*. PeerJ 13:e19043. https://doi.org/10.7717/peerj.19043
- Araki, H., and Sakata, M. K. (2026). *Optimising passive eDNA sampling: A theoretical framework for time-dependent eDNA accumulation*. bioRxiv preprint, abstract indexed at https://www.lifescience.net/preprints/26627/optimising-passive-edna-sampling-a-theoretical-fra/
