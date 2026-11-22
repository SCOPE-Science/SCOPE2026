# A sharp product threshold for total-variation stability of directed three-point bilateral filters

## Finding

Let \(n\geq 6\), \(a,b>0\), and let \(\rho:[0,\infty)\to(0,1]\) be continuous, nonincreasing, satisfy \(\rho(0)=1\), and obey \(t\rho(t)\to0\) as \(t\to\infty\). On a real finite path, the directed nearest-neighbor bilateral map with left weight \(a\), right weight \(b\), unit self-weight, and range affinity \(\rho\) is total-variation nonincreasing on **every** input if and only if

\[
 ab\le1.
\]

When \(ab\le1\), its sharp one-input total-variation gain is exactly \(1\), attained for every \(n\ge4\). If \(ab>1\), an explicit nondecreasing six-site input is mapped to a nonmonotone output and has strictly increased total variation. The nonexpansive side holds even for \(n\ge2\), without monotonicity or fast-tail assumptions on \(\rho\) beyond \(0\le\rho\le1\); the additional assumptions are required for the stated converse. An exact, nonnegative dissipation identity also holds on the nonexpansive side.

## Assumptions and scope

Index sites by \(i=0,\ldots,n-1\), use endpoint clamping \(x_{-1}=x_0\) and \(x_n=x_{n-1}\), and put \(d_i=x_{i+1}-x_i\) for \(0\le i\le n-2\), with the formal outside increments \(d_{-1}=d_{n-1}=0\). Define

\[
 (F_{a,b,\rho}x)_i=
 \frac{x_i+a\rho(|x_i-x_{i-1}|)x_{i-1}
       +b\rho(|x_{i+1}-x_i|)x_{i+1}}
 {1+a\rho(|x_i-x_{i-1}|)+b\rho(|x_{i+1}-x_i|)}.
\]

The unweighted adjacent total variation is \(V(x)=\sum_{i=0}^{n-2}|d_i|\). The statement \(V(Fx)\le V(x)\) refers to **one input**, not the generally different two-input Lipschitz property \(V(Fx-Fy)\le V(x-y)\). No invariance under cyclic, multidimensional, or wider-window boundaries is asserted. Gaussian affinity \(\rho(t)=\exp(-t^2/(2\sigma^2))\), for any \(\sigma>0\), satisfies the assumptions.

## Proof

Write

\[
 Z_i=1+a\rho(|d_{i-1}|)+b\rho(|d_i|),\qquad
 \ell_i=\frac{a\rho(|d_{i-1}|)}{Z_i},\qquad
 r_i=\frac{b\rho(|d_i|)}{Z_i},
\]

using \(\rho(0)\) on clamped outside edges. The identity \((Fx)_i=x_i-\ell_i d_{i-1}+r_i d_i\) is exact, hence for \(0\le i\le n-2\)

\[
 (Fx)_{i+1}-(Fx)_i
 =\ell_i d_{i-1}+(1-r_i-\ell_{i+1})d_i+r_{i+1}d_{i+1}.\tag{1}
\]

Let \(q_i=\rho(|d_i|)\in[0,1]\). Because the additional nonnegative weights in denominators only decrease the fractions,

\[
 r_i+\ell_{i+1}
 \le\frac{bq_i}{1+bq_i}+\frac{aq_i}{1+aq_i}\le1
 \quad\Longleftrightarrow\quad abq_i^2\le1.
\]

Thus if \(ab\le1\), each of the three coefficients in (1) is nonnegative. Summing the triangle inequality over all output edges yields

\[
 V(Fx)\le V(x)-r_0|d_0|-\ell_{n-1}|d_{n-2}|\le V(x).\tag{2}
\]

Indeed an interior \(|d_j|\) occurs in three consecutive output-edge estimates with total coefficient
\(r_j+(1-r_j-\ell_{j+1})+\ell_{j+1}=1\); on the first and last edges one of those terms lies outside the finite path.

For a more precise identity, denote by \(P_i\) and \(N_i\) the sums of, respectively, the positive and the absolute negative contributions among the at most three terms on the right of (1), omitting formal outside increments. Then

\[
 \boxed{V(x)-V(Fx)=r_0|d_0|+\ell_{n-1}|d_{n-2}|+
 2\sum_{i=0}^{n-2}\min\{P_i,N_i\}.}\tag{3}
\]

This follows from \(|P_i-N_i|=P_i+N_i-2\min(P_i,N_i)\) and the preceding column sums. It quantifies boundary leakage and cancellation of oppositely signed jumps, not just nonincrease.

Sharpness of coefficient \(1\) follows for any \(n\ge4\) using \(x=(0,0,1,\ldots,1)\): (1) shows the output is nondecreasing, while the first and last outputs are exactly \(0\) and \(1\), hence \(V(Fx)=V(x)=1\).

Conversely, assume \(ab>1\). Continuity at zero gives a sufficiently small \(\delta>0\) such that \(ab\rho(\delta)^2>1\). For \(T>0\), take the six entries

\[
 x^{(T)}=(-T,-T,0,\delta,T+\delta,T+\delta).
\]

The first and last output values remain \(-T\) and \(T+\delta\). By direct substitution, using \(T\rho(T)\to0\), their central output difference obeys

\[
 \lim_{T\to\infty}
 \bigl((Fx^{(T)})_3-(Fx^{(T)})_2\bigr)
 =\delta\left(1-\frac{bq}{1+bq}-\frac{aq}{1+aq}\right)<0,
 \quad q=\rho(\delta).
\]

The strict inequality is algebraically equivalent to \(abq^2>1\). Thus for all sufficiently large finite \(T\), the filtered output has a decreasing interior edge despite increasing input and unchanged global endpoints. Consequently \(V(Fx^{(T)})>V(x^{(T)})=2T+\delta\). Appending repeated endpoint values extends this counterexample to every \(n>6\). This proves both necessity and the stated sharpness.

## Verification

The included standalone `verify.py` uses exact rational arithmetic with \(\rho(t)=1/(1+t^2)\), which has the required fast decay. It checks the precise identity (3) and contraction on 6,000 generated rational datasets, verifies five distinct product-above-one counterexamples with an interior reversal, and checks attained unit gain on finite paths of sizes 4 through 14. These finite checks corroborate, but do not substitute for, the proof for all real inputs and admissible affinities.

## Relationship to prior work

Tomasi and Manduchi introduced edge-preserving bilateral averages; Pianykh studied their nonlinear response and parameter selection; Galiano and Velasco developed functional-rearrangement representations. Harten's classical incremental-form lemma already implies total-variation contraction when the adjacent positive coefficients sum to at most one. Accordingly, the **sufficiency mechanism itself is not new**. The specific exact product boundary \(ab=1\), its necessity uniformly across the stated rapidly decaying affinities, the explicit monotone failure witnesses, the sharp gain and the finite-path dissipation formula are the distinct assertion here. The reviewed sources do not state this combined classification, but broad prior literature leaves a residual historical-priority risk.

## Limitations

This is a one-input total-variation classification, not a claim of two-input contractivity. The converse uses continuity of \(\rho\) at zero and \(t\rho(t)\to0\); profiles with slower tails are not classified. The construction uses at least six sites. It does not treat windows wider than three samples, general graphs, or multidimensional image total variation. The archival source date in the metadata is the day-verified date on which the original 1998 bilateral-filter work entered IEEE Xplore, not a claim that the work first became public on that day.

## References

1. C. Tomasi and R. Manduchi, *Bilateral Filtering for Gray and Color Images*, ICCV 1998, DOI: 10.1109/ICCV.1998.710815; historical text: https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/MANDUCHI1/Bilateral_Filtering.html.
2. O. S. Pianykh, *Bilateral Filters: What They Can and Cannot Do*, arXiv:1007.1016v1 (2010-07-06), https://arxiv.org/abs/1007.1016.
3. G. Galiano and J. Velasco, *On a Fast Bilateral Filtering Formulation Using Functional Rearrangements*, arXiv:1505.00412v1 (2015-05-03), https://arxiv.org/abs/1505.00412.
4. A. Harten, *High Resolution Schemes for Hyperbolic Conservation Laws*, J. Comput. Phys. 49 (1983), 357–393, Lemma 2.2, DOI: 10.1016/0021-9991(83)90136-5.
