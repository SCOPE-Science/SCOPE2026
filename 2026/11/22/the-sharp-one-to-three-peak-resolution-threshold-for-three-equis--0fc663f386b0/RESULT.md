# The sharp one-to-three-peak resolution threshold for three equispaced logistic adoption waves

## Finding

Suppose three equally sized populations independently follow shifted logistic adoption profiles with a common positive scale and three equally spaced onset centers. Their aggregate adoption *rate* has exactly one strict local maximum if the separation, divided by common scale, does not exceed

\[
d_* = \operatorname{arcosh}(4+3\sqrt{3}) = 2.908963008819674894\ldots.
\]

Above this threshold it has exactly three strict local maxima, separated by two strict local minima. At the threshold the center remains a strict maximum and two noncentral stationary shoulders are born, but those shoulders are not local extrema. Thus two separate neighboring waves can individually exhibit two peaks without the combined three-wave rate being trimodal.

## Assumptions and scope

Let the calendar time \(t\in\mathbb R\), common scale \(b>0\), center \(\mu\in\mathbb R\), and normalized positive separation \(d>0\). Define the logistic CDF and its density by

\[
L(x)=\frac1{1+e^{-x}},\qquad \ell(x)=L'(x)=\frac1{2+2\cosh x}.
\]

Each cohort's cumulative fraction is \(L((t-\mu-jbd)/b)\), where \(j\in\{-1,0,1\}\). Their combined instantaneous adoption rate is

\[
R(t)=\frac1{3b}\sum_{j=-1}^{1}\ell\!\left(\frac{t-\mu}{b}-jd\right).
\]

This is a deterministic, independent-cohort model with equal final cohort sizes and common rate scale, not a network-coupled Bass model. Modes refer to strict local maxima of \(R\) on all of \(\mathbb R\); observations restricted to a truncated time window may omit modes. Positive proportional changes of \(R\) do not affect their locations or number.

## Proof

Write \(y=(t-\mu)/b\), \(c=2\cosh d>2\), and \(u=2\cosh y\ge2\). The hyperbolic addition identities yield the exact rational reduction

\[
3bR(t)=J_c(u):=\frac1{u+2}+\frac{cu+4}{(u+c)^2}.
\]

Direct differentiation gives

\[
J_c'(u)=\frac{H_c(u)}{(u+2)^2(u+c)^3},\qquad
H_c(u)=(c^2-8-cu)(u+2)^2-(u+c)^3.
\]

The denominator is strictly positive for \(u\ge2\). The cubic's discriminant factors as

\[
\operatorname{disc}_u H_c=4(c-2)^6(c+1)(c^2-16c-44).
\]

Its only parameter transition in \(c>2\) is \(c_*=8+6\sqrt3\). For all \(c>2\),

\[
H_c(2)=-(c+2)[(c-6)^2+32]<0,\qquad
H_c(-c)=2(c-2)^3(c+2)>0,
\]

and \(H_c(0)=-c^3+4c^2-32<0\): the polynomial \(c^3-4c^2+32\) is positive for all \(c\ge2\) (its minimum on that interval occurs at \(c=8/3\), where it equals \(608/27>0\)). Consequently one negative root always lies in \((-c,0)\).

If \(2<c<c_*\), the discriminant is negative, so there is exactly one real root, which is negative. Hence \(J_c'(u)<0\) throughout \(u\ge2\). Since \(u=2\cosh y\) increases strictly as \(|y|\) increases, the central point \(y=0\) is the sole strict maximum.

At \(c=c_*\), exact factorization gives

\[
H_{c_*}(u)=-(9+6\sqrt3)(u-4-2\sqrt3)^2(u+8-2\sqrt3).
\]

Its noncentral zero is double, at \(u_*=4+2\sqrt3>2\). The sign of \(J'_{c_*}\) remains negative on either side, so these points are stationary shoulders (not extrema), whereas the center remains a strict maximum.

For \(c>c_*\), the discriminant is positive and all three roots are simple and real. Immediately above \(c_*\), the positive double root splits into two roots greater than \(2\), because \(\partial_c H_c(u_*)|_{c=c_*}=288+192\sqrt3>0\), while the neighboring values of \(H_{c_*}\) are negative. They cannot merge again since the discriminant never vanishes in \((c_*,\infty)\), and cannot cross \(u=2\) because \(H_c(2)<0\). Thus there are precisely two positive admissible roots \(2<u_1<u_2\). The cubic's sign on \(u>2\) is negative, then positive, then negative. Therefore \(J_c\) decreases, increases, then decreases as \(|y|\) increases, yielding a strict maximum at \(y=0\), minima at \(y=\pm\operatorname{arcosh}(u_1/2)\), and outer maxima at \(y=\pm\operatorname{arcosh}(u_2/2)\). No other stationary points occur.

The unique transition \(c=c_*\) is equivalent to \(d=d_*\), since \(c=2\cosh d\) increases strictly for \(d>0\). The conclusion holds for every \(b>0\) and \(\mu\in\mathbb R\).

## Verification

The independent algebraic identities, derivative numerator, discriminant, parameter-boundary factorization, critical double-root factorization, and representative mode counts are reproduced by the standalone `check.py`. Run `python check.py` with SymPy installed. This confirms algebraic and finite-sample conditions; the all-parameter mode classification is proved by the sign, discriminant, and continuity argument above, not by finite numerical enumeration.

For \(d=3\), numerical roots of \(H_{2\cosh3}\) are approximately \(-4.7255551803\), \(6.1384669645\), and \(10.7224122073\), giving the predicted three strict maxima. For \(d=2\), the sole real cubic root is negative and the response is unimodal.

## Relationship to prior work

Došlá (2009), Proposition 3, establishes an explicit criterion for *two* equal-scale logistic densities. In the equal-weight case the two-component bimodality threshold is \(2\log(2+\sqrt3)=2.6339157938\ldots\), strictly smaller than the three-component trimodality threshold obtained here. In particular, neighboring pairs may be bimodal while their full equal-weight three-component sum remains unimodal. The theorem concerns a distinct three-component claim and does not follow directly from Došlá's two-component condition.

Bertotti, Brunner, and Modanese (2016) discuss heterogeneous adoption timing in a network Bass model, but their investigated adoption processes are governed by a different interaction model and do not yield the rational cubic threshold above. The 2024 three-logistic numerical mixture example of Skarżyńska and Romaniuk has unequal component parameters and is used for sampler diagnostics, rather than to classify symmetric three-component modality. General mixture-mode literature remains a historical-priority risk.

## Limitations

The mode count applies to independent logistic cohorts of *equal weight, equal scale and equispaced centers*. It does not classify arbitrary cohort weights, unequal adoption scales, network feedback, time-dependent interventions, or data with sampling noise. The result is an exact idealized resolution benchmark rather than a claim about detectability from finite noisy sales data. The sampled checker is supplementary and is not a proof of all real-parameter cases. Publication priority has not been independently audited; broader general mixture theory may contain an implicit form.

## References

1. Š. Došlá, *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, Kybernetika 45 (2009), 279–292, https://dml.cz/dmlcz/140075 ; full text: https://dml.cz/bitstream/handle/10338.dmlcz/140075/Kybernetika_45-2009-2_6.pdf .
2. M. L. Bertotti, J. Brunner, G. Modanese, *The Bass diffusion model on networks with correlations and inhomogeneous advertising*, arXiv:1605.06308v1, public 2016-05-19, https://arxiv.org/abs/1605.06308 .
3. A. Skarżyńska, M. Romaniuk, *On Improvement of the DE-MC_z Algorithm with Modes Identification*, IPMU 2024, https://ipmu2024.inesc-id.pt/files/paper_1001.pdf .
