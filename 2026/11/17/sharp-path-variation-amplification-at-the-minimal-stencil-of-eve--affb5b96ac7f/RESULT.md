# Sharp path-variation amplification at the minimal stencil of every Whittaker–Henderson order

## Finding
For every integer \(p\ge1\) and every \(\lambda>0\), let \(n=p+1\) and let \(D_p\) be the unique length-\(n\) forward difference of order \(p\), with entries \((-1)^{p-j}\binom{p}{j}\) for \(0\le j\le p\). The unweighted quadratic smoothing operator is
\[
S_{p,\lambda}=(I+\lambda D_p^{\mathsf T}D_p)^{-1}.
\]
Write \(V(y)=\sum_{i=0}^{p-1}|y_{i+1}-y_i|\). Define the sharp two-input variation Lipschitz coefficient
\[
\mathcal L_p(\lambda)=\sup_{V(a-b)>0}\frac{V(S_{p,\lambda}a-S_{p,\lambda}b)}{V(a-b)}.
\]
It has the exact finite binomial formula
\[
\boxed{\mathcal L_p(\lambda)=1+\frac{\lambda M_p}{1+\lambda\binom{2p}{p}},\qquad
M_p=\max_{0\le j<p}\binom{p-1}{j}\left(2^{p+1}-2-2\binom{p+1}{j+1}\right).}
\]
A monotone binary single-jump vector \(a-b=(0,\ldots,0,1,\ldots,1)\), with its jump positioned at any maximizer \(j\), attains this exact sharp coefficient. In particular,
\[
\mathcal L_1(\lambda)=\frac1{1+2\lambda}<1,\quad
\mathcal L_2(\lambda)=1,\quad
\mathcal L_p(\lambda)>1\quad(p\ge3).
\]
For every fixed \(\lambda>0\), the amplification has a universal, strictly greater-than-two high-order limit:
\[
\boxed{\lim_{p\to\infty}\mathcal L_p(\lambda)=1+\sqrt2.}
\]
The same limit holds for the strong-penalty coefficients \(\lim_{p\to\infty}\lim_{\lambda\to\infty}\mathcal L_p(\lambda)\).

## Assumptions and scope
The integer difference order is \(p\ge1\), the observation length is exactly the minimal admissible \(n=p+1\), the sample grid is equally spaced and the data-fidelity weights are one. The tuning parameter is arbitrary \(\lambda>0\). Variation is the unweighted sum of absolute *adjacent* first differences, not the complete-pair Gini seminorm. All inputs are real; the operator is linear and translation equivariant. The norm is taken on the quotient by constants, and its denominator excludes zero-variation input differences.

## Proof
Put \(d_j=(-1)^{p-j}\binom{p}{j}\), \(0\le j\le p\). Since \(D_p=d\) is a single row, Vandermonde's identity and Sherman–Morrison give
\[
C_p=dd^{\mathsf T}=\binom{2p}{p},\quad
S_{p,\lambda}=I-\alpha d^{\mathsf T}d,\quad
\alpha=\frac{\lambda}{1+\lambda C_p}.
\]
Let \(D\) be the first-difference operator, so \((Dy)_j=y_{j+1}-y_j\), \(0\le j<p\). The order-\(p\) difference factors as \(d=v^{\mathsf T}D\), with
\[
v_j=(-1)^{p-1-j}\binom{p-1}{j},\qquad
u_j=(Dd^{\mathsf T})_j=(-1)^{p-1-j}\binom{p+1}{j+1}.
\]
Consequently
\[
DS_{p,\lambda}=(I_p-\alpha u v^{\mathsf T})D.
\]
The first-difference map \(D:\mathbb R^{p+1}\to\mathbb R^p\) is onto; hence the required variation norm equals the induced \(\ell^1\)-matrix norm of \(B=I_p-\alpha u v^{\mathsf T}\), namely its maximum absolute column sum.

For each \(j\), \(u_jv_j=\binom{p+1}{j+1}\binom{p-1}{j}>0\). The identity \(v^{\mathsf T}u=C_p\) and positivity of the other terms when \(p\ge2\) show \(\alpha u_jv_j<1\). For \(p=1\), the same inequality follows from \(\alpha C_1<1\). Thus diagonal entries of \(B\) are positive. Its \(j\)-th absolute column sum is exactly
\[
1-\alpha u_jv_j+\alpha|v_j|\sum_{i\ne j}|u_i|
=1+\alpha\binom{p-1}{j}\left(2^{p+1}-2-2\binom{p+1}{j+1}\right),
\]
using \(\sum_{i=0}^{p-1}|u_i|=\sum_{k=1}^p\binom{p+1}{k}=2^{p+1}-2\). Taking the maximum proves the exact formula. The vector whose first differences are the \(j\)-th coordinate vector is a nondecreasing zero-one step; it proves actual attainment rather than just infinitesimal sharpness.

For \(p=1\), direct substitution gives \(M_1=-2\) and \(C_1=2\); for \(p=2\), \(M_2=0\). If \(p\ge3\), choosing \(j=0\) gives
\[
M_p\ge2^{p+1}-2p-4>0.
\]
The strict positivity starts at \(p=3\), completing the sharp trichotomy.

For the asymptotics, set \(b_p=\max_{0\le j<p}\binom{p-1}{j}=\binom{p-1}{\lfloor(p-1)/2\rfloor}\). The exact formula implies the upper bound
\[
M_p\le(2^{p+1}-2)b_p.
\]
Choosing a maximizing central index \(j_p\) in the definition gives
\[
M_p\ge b_p\left(2^{p+1}-2-2\binom{p+1}{j_p+1}\right).
\]
The central binomial upper estimate \(\binom{p+1}{j_p+1}=O(2^p/\sqrt p)\) makes the upper and lower expressions asymptotic to \(2^{p+1}b_p\). Stirling's formula yields
\[
\frac{2^{p+1}b_p}{\binom{2p}{p}}\longrightarrow\sqrt2.
\]
Therefore \(M_p/C_p\to\sqrt2\). For each fixed \(\lambda>0\), \(\lambda C_p/(1+\lambda C_p)\to1\), proving the stated limit; sending \(\lambda\to\infty\) first has exactly the same binomial ratio limit.

## Verification
The standalone `verify.py` builds \(I+\lambda d^{\mathsf T}d\) and inverts it by exact rational elimination, independently of the rank-one formula. It then evaluates all \(p\) binary single-jump vectors, for every \(1\le p\le12\) and three positive rational parameter choices, comparing the maximal measured variation to the predicted binomial coefficient. It tests the first five values of \(M_p\) and prints larger-order ratios for inspection. All checks are finite corroboration: the assertions for all dimensions and the limit are established by the preceding analytical proof.

To reproduce, run `python3 verify.py` using the standard Python library.

## Relationship to prior work
Whittaker–Henderson smoothing and its rank-one minimum-length matrix formula are established constructions. Existing work on generalized Hodrick–Prescott filters provides matrix and ridge formulations, while finite-sample HP papers derive second-order filter coefficients. A published cross-order result establishes range preservation only for first differences and exhibits a rank-one negative-weight witness for every higher order. That range-preservation classification is not a claim about the *exact induced adjacent-variation norm* or its high-order limit. In particular, range-preservation failure alone neither implies variation expansion nor fixes the sharp \(1+\sqrt2\) factor.

The present result computes this different natural stability invariant at each minimal stencil, proves actual binary-step extremizers, and establishes a universal large-order limit independent of the fixed smoothing strength. Earlier explicit matrix formulas make the finite rank-one reduction accessible; the remaining originality risk is an unindexed treatment of BV norms of general-order graduation filters.

## Limitations
The precise formula concerns only the minimal \(p+1\)-point stencil; larger sample lengths have multiple difference rows and do not follow by the same rank-one calculation. The sharp bound is a two-input Lipschitz coefficient; it does not imply that all outputs increase variation. The high-order limit is taken along growing dimension \(p+1\), not at a fixed number of observations. Weighted fidelity, unequal grids, periodic boundaries, and other norms are not covered. Complete historical priority is not asserted.

## References
1. Eilers, P. H. C., “A Perfect Smoother,” *Analytical Chemistry* **75** (2003), 3631–3636, doi:10.1021/ac034173t. First online: 2003-05-30.
2. Yamada, H., “Ridge Regression Representations of the Generalized Hodrick–Prescott Filter,” *Journal of the Japan Statistical Society* **45** (2016), doi:10.14490/jjss.45.121.
3. Cornea-Madeira, A., “The Explicit Formula for the Hodrick-Prescott Filter in Finite Sample,” institutional open manuscript deposited 2016-04-06, https://eprints.whiterose.ac.uk/id/eprint/97954/1/HP_ACM.pdf.
4. “Only first-difference Whittaker–Henderson smoothing is universally range-preserving,” online mathematical result, 2026-10-04 (publicly accessible comparison).
