# Three-source Poisson attribution permits exactly three posterior ranking reversals

## Finding

An idealized downstream molecular-count observation can reverse the posterior ranking of two upstream source presences three times as the observed count increases, even though the first source contributes more molecules when present. This is the largest possible number of strict reversals with one additional independent Bernoulli nuisance source. Without that nuisance source, or whenever its contribution does not exceed the intensity difference of the two compared sources, at most one strict reversal occurs.

The exact three-reversal witness is
\[
\beta=0,\quad (u,v,c)=(1,1/10,5),\quad(p_1,p_2,p_3)=(1/11,1/2,1/1000).
\]
The signs of the posterior difference at counts \(1,2,5,6,19,20\) are respectively \(-,+,+,-,-,+\). Thus the exact sign switches lie between consecutive counts \(1,2\), \(5,6\), and \(19,20\), and there are no others.

## Assumptions and scope

Let \(X_1,X_2,X_3\) be mutually independent Bernoulli indicators of occupancy or emission at three upstream locations, with \(\Pr(X_i=1)=p_i\in(0,1)\). Let \(u>v>0\) be two source-specific expected contributions per sample, \(c>0\) the third source contribution, and \(\beta\ge0\) a *known fixed* background mean. A downstream count \(N\in\{0,1,\ldots\}\), conditional on these indicators, obeys
\[
N\mid X_1,X_2,X_3\sim\operatorname{Poisson}(\beta+uX_1+vX_2+cX_3).
\]
The comparisons concern posterior *marginal* occupancy probabilities \(\Pr(X_i=1\mid N=n)\), not the posterior probabilities that *exactly one* source is active. Assume source contributions are conditionally additive, emissions are constant during sampling, and there is no unknown extra source, non-Poisson clumping, or assay error. No real-world parameter calibration is inferred.

A **strict ranking reversal** occurs when the nonzero sign of \(\Delta_n=\Pr(X_1=1\mid N=n)-\Pr(X_2=1\mid N=n)\) differs at two successive nonzero-sign positions; zeros are treated as ties. Bounds apply to all integers \(n\ge0\), all allowed probabilities, and all allowed rates.

## Proof

Put \(q=p_3\) and, for \(t>0\), define
\[
L_t(n)=(1-q)e^{-(\beta+t)}(\beta+t)^n+qe^{-(\beta+t+c)}(\beta+t+c)^n.
\]
The common factor \(1/n!\) is suppressed. Denote the positive marginal observation probability by \(Z_n=\Pr(N=n)>0\). The contributions from configurations with \((X_1,X_2)=(0,0)\) or \((1,1)\) cancel when the two posterior probabilities are subtracted, yielding the exact identity
\[
n!Z_n\Delta_n=p_1(1-p_2)L_u(n)-p_2(1-p_1)L_v(n).\tag{1}
\]
This is valid even at \(\beta=0\), since all terms in \(L_u,L_v\) have positive means.

If \(c\le u-v\), every base in \(L_u(x)\), viewed as a positive sum of real powers of the corresponding rates, is at least every base in \(L_v(x)\). The logarithmic derivative of each positive sum is a positive-weight average of logarithms of its bases. Consequently
\[
\frac{d}{dx}\log\frac{L_u(x)}{L_v(x)}>0\qquad(x\in\mathbb R),
\]
because the smallest base of the first sum is at least the largest base of the second, while each nondegenerate two-atom mixture has strictly positive weights. The sign of (1) therefore changes at most once.

In general, the right side of (1), extended from integer \(n\) to real \(x\), is a linear combination of at most four exponential functions \(e^{x\log\lambda}\), with strictly positive distinct bases except when some rates coincide. Every nonzero sum of \(m\) distinct real exponentials has at most \(m-1\) distinct real roots: dividing by the exponential of the smallest rate leaves a constant plus \(m-1\) exponentials; Rolle's theorem and induction on \(m\) prove this bound. Hence (1) can change strict sign at most three times along increasing integer counts. If \(X_3\) is absent, the ratio is a single increasing exponential in \(n\), so at most one reversal is possible with two sources.

For the witness in the Finding, the sign of (1) equals that of
\[
H_n=999e^5-9990e^{59/10}10^{-n}+6^n-10e^{9/10}(51/10)^n.\tag{2}
\]
This follows by multiplying \(L_u(n)-10L_v(n)\) by the strictly positive factor \(1000e^6\). Exact rational Taylor enclosures of the three exponentials in (2) show
\[
H_1<0,\ H_2>0,\ H_5>0,\ H_6<0,\ H_{19}<0,\ H_{20}>0.
\]
The adjacent count pairs \((1,2),(5,6),(19,20)\) therefore each contain a strict reversal. The universal three-root bound excludes any others. The strict inequalities persist on an open neighborhood of the witness parameters, so the phenomenon is not a knife-edge tie. Three sources are minimal by the preceding two-source argument. This completes the proof.

## Verification

`verify.py` uses Python standard-library exact fractions to enclose every \(e^x\) needed in (2) by a positive rational Taylor sum and a rational geometric-tail upper bound. The strict signs are certified at all six stated counts. The script also independently enumerates all eight latent source configurations and checks the posterior differences directly; that floating-point diagnostic is supplementary, not the proof. Run `python3 verify.py` in the same directory as this document. No input data, package installation, or network access is required.

## Relationship to prior work

Van Driessche et al. (first public 26 October 2022) studied downstream eDNA concentrations and variability under source-biomass and flow changes and analyzed droplet digital PCR counts using Poisson statistics. The idealized latent-source inference problem here is not their empirical model. Carraro et al. (2018) modeled DNA transport and upstream source reconstruction in river networks; their spatial inverse problem differs from a single unlabelled Poisson count and posterior ranking reversals. Shanthikumar and Yao (1986) developed general likelihood-ratio ordering and closure results under convolution, highlighting that an arbitrary nuisance mixture does not necessarily preserve such order. Voorhoeve (1979) and classical exponential-polynomial theory supply broader zero-count machinery: the four-term upper bound itself is an application of known mathematics. The contribution assessed here is the sharp source-attribution interpretation, the one-reversal separation regime, and an exact three-reversal/minimal-source witness.

## Limitations

This is a theoretical conditional-Poisson model. eDNA is often clumped, source intensities are uncertain and spatially correlated, and real assays may have false positive or false negative responses. The result does not assert that three reversals have been seen in natural data, nor that the particular witness priors are typical. Known general exponential-sum theory covers the zero-count mechanism; broader historical priority for the specialized sharp attribution statement is not independently certified.

## References

1. Van Driessche, C., Everts, T., Neyrinck, S., and Brys, R. *Experimental assessment of downstream environmental DNA patterns under variable fish biomass and river discharge rates*. **Environmental DNA** (first public 2022-10-26). https://doi.org/10.1002/edn3.361
2. Carraro, L., Hartikainen, H., Jokela, J., Bertuzzo, E., and Rinaldo, A. *Estimating species distribution and abundance in river networks using environmental DNA*. **PNAS** 115, 11724–11729 (2018). https://doi.org/10.1073/pnas.1813843115
3. Shanthikumar, J. G., and Yao, D. D. *The preservation of likelihood ratio ordering under convolution*. **Stochastic Processes and their Applications** 23, 259–267 (1986). https://doi.org/10.1016/0304-4149(86)90039-6
4. Voorhoeve, M. *A Generalization of Descartes' Rule*. **Journal of the London Mathematical Society** s2-20, 446–456 (1979). https://doi.org/10.1112/jlms/s2-20.3.446
