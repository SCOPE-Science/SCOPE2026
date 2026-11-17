# A mortality-response sign reversal under active-population SIRD normalization

## Finding

Consider two identical, fully interacting deterministic SIRD groups as defined below. Let \(t=\mu/\gamma\), \(r=\beta/\gamma\), and let \(d_a(t)\), \(d_f(t)\) be the eventual deceased fractions under two otherwise identical choices of transmission normalization. The sharp high-mortality expansions are
\[
 d_a(t)=1-s+\frac{sr\log(1/s)-(1-s)}{t}+O(t^{-2}),
 \qquad d_f(t)=1-s+\frac{(1-s)(sr-1)}{t}+O(t^{-2}).
\]
At the active-denominator threshold \(r_a=(1-s)/(s\log(1/s))\), the first active correction vanishes, and
\[
 d_a(t)=1-s-\frac{(1-s)^2}{2s\,t^2}+O(t^{-3}).
\]
Since \(\log(1/s)>1-s\) for \(0<s<1\), the interval
\[
 \frac{1-s}{s\log(1/s)}<r<\frac1s
\]
is nonempty. Throughout this interval, \(d_a(t)>1-s>d_f(t)\) for all sufficiently large finite \(t\), with \(d_a\) eventually strictly decreasing and \(d_f\) eventually strictly increasing. Thus active-population feedback reverses the sign of the late mortality response, although the parameters and initial states otherwise match. Moreover \(d_a(0)=0\) continuously in the zero-mortality limit, so the active model attains a global maximum at some finite positive mortality rate, strictly above its large-mortality limiting level \(1-s\).

## Assumptions and scope

Take two identical groups indexed by \(i=1,2\), initial data \(S_i(0)=s\), \(I_i(0)=1-s\), \(R_i(0)=D_i(0)=0\), where \(0<s<1\). Let \(\beta,\gamma,\mu>0\) and \(\beta_{ij}=\beta/2\) for all \(i,j\). Define living population \(N_i=S_i+I_i+R_i\). The active-normalized model is
\[
 \dot S_i=-S_i\sum_{j=1}^2\frac{\beta}{2}\frac{I_j}{N_j},\quad
 \dot I_i=-\dot S_i-(\gamma+\mu)I_i,\quad
 \dot R_i=\gamma I_i,\quad \dot D_i=\mu I_i.
\]
The fixed-denominator comparator replaces each \(N_j(t)\) in the force of infection by \(N_j(0)=1\), without changing any other equation or initial state. Identical initial conditions and positive uniform mixing preserve the equal-group invariant manifold, so each model reduces exactly to a single homogeneous population. The quantity \(d\) denotes the final deceased fraction of one initial unit-sized group; it is also the total two-group deceased fraction divided by two. The first publicly available motivating article describes the active-population normalization; the fixed-denominator comparator is a deliberately matched control.

## Proof

**1. Exact scalar final-size identities.** In either model, write \(x=S_i(\infty)\), \(u=\log(s/x)\) and \(t=\mu/\gamma\), \(r=\beta/\gamma\). Because \(S+I+R+D=1\), \(I(\infty)=0\), and \(R(\infty)=\gamma D(\infty)/\mu\), mass balance yields
\[
 d=\frac{t}{1+t}(1-x),\qquad N_\infty=\frac{1+t x}{1+t}.
\]
For the active force of infection, integrate \(\dot S/S=-\beta I/N\) with \(\dot N=-\mu I\):
\[
 u=\frac r t\log\frac{1+t}{1+t x},\qquad x=s e^{-u}.
\]
For fixed initial-population normalization, integrate \(\dot S/S=-\beta I\) and use \(\int_0^\infty I\,dt=(1-x)/(\gamma+\mu)\):
\[
 u=\frac r{1+t}(1-x),\qquad x=s e^{-u}.
\]
For each \(t>0\), each right-hand side is an increasing, strictly concave function of \(u\ge0\), positive at zero and bounded above. Hence it has a unique positive fixed point: the function minus \(u\) begins positive, is strictly concave and tends to negative infinity. These uniquely describe the physical final sizes. For the fixed-denominator equation, its right-hand side is at most \(r/(1+t)\), so \(u=O(t^{-1})\). For the active equation, \(0\le u\le (r/t)\log(1+t)\to0\); consequently \(x=s e^{-u}\to s\), so \(x\ge s/2\) for all large \(t\). On that range \(\log[(1+t)/(1+t x)]\) stays bounded, hence also \(u=O(t^{-1})\).

**2. Active denominator expansion.** Put \(\varepsilon=1/t\), \(L=\log(1/s)\). The identity becomes
\[
 u=r\varepsilon\left[L+u+\log(1+\varepsilon)-\log(1+\varepsilon e^u/s)\right].
\]
The analytic implicit function theorem at \((u,\varepsilon)=(0,0)\) applies because the derivative of the equation \(u-\text{RHS}=0\) in \(u\) equals 1 there. Expanding uniquely gives
\[
 u=rL\varepsilon+\left[r^2L+r(1-1/s)\right]\varepsilon^2+O(\varepsilon^3).
\]
Substitute \(x=s e^{-u}\) and \(d=(1-x)/(1+\varepsilon)\). The coefficient of \(\varepsilon\) is \(srL-(1-s)\), proving the first expansion. The second coefficient is
\[
 (1-s)-srL+sr^2L+sr(1-1/s)-\tfrac12 sr^2L^2.
\]
At \(r=(1-s)/(sL)\) this simplifies exactly to \(-(1-s)^2/(2s)\), yielding the equality boundary formula.

**3. Fixed denominator expansion.** Its implicit equation is \(u=r\varepsilon(1+\varepsilon)^{-1}(1-s e^{-u})\), hence \(u=r(1-s)\varepsilon+O(\varepsilon^2)\). Substituting into \(d=(1-x)/(1+\varepsilon)\) gives first correction \((1-s)(sr-1)\). The analytic expansions imply the asserted eventual strict signs of the differences and derivatives.

**4. Sharp wedge and attained active peak.** For \(0<s<1\), \(\log(1/s)>1-s\) shows \(r_a<1/s\). In that open interval, \(srL-(1-s)>0\) but \((1-s)(sr-1)<0\). The equality calculation shows the active boundary is approached from below, proving sharpness of the leading-correction threshold including its equality case. Finally \(0\le d_a(t)\le t/(1+t)\to0\) as \(t\downarrow0\), and the final-size solution is continuous for positive \(t\) by the scalar fixed-point characterization. Since some finite large \(t\) has \(d_a(t)>1-s\) while \(d_a(t)\to1-s\) as \(t\to\infty\), the positive global maximum occurs at a finite interior value.

## Verification

The standalone file `checker.py` symbolically verifies the first- and second-order coefficients (including the sharp equality threshold) using SymPy and tests the defining scalar fixed-point equations with 55-digit mpmath arithmetic. At \(s=1/2\) and \(r=3/2\), the active threshold is \(1/\log2\approx1.442695\), while the fixed threshold is 2. This ratio lies strictly in the wedge. The active first-order coefficient is \(\tfrac34\log 2-\tfrac12\approx0.0198604\); the fixed coefficient is \(-1/8\). Computed signs at \(t=100,1000,10000,100000\) agree with the theorem. Finite tests are auxiliary, not a replacement for the analytic proof.

## Relationship to prior work

Melo and Santos (2026) develop the active-population SIRD equations and its final-size analysis, including numerical sensitivity to disease mortality. A later exact analysis, *Parameter-unrestricted final-size uniqueness and certified geometric bracketing in active-population SIRD networks*, establishes existence and uniqueness of fully interacting multi-group active-normalized final sizes, and is not claimed as new here. Neither inspected statement supplies the matched-model sign-reversal wedge, its sharp mortality expansion, or its equality boundary. Standard fixed-population SIRD final-size theory also supplies one of the underlying equations, but the comparison at the same initial data and rates is the additional content. The closest published-record searches described in the accompanying review found no explicit implication covering this result; absence from a search index does not certify historical novelty.

## Limitations

The assertion is restricted to a homogeneously initialized, exactly invariant two-community sector and to large mortality, not arbitrary heterogeneous populations or all mortality rates. The final active maximum is known to exist but is not claimed unique or located exactly. There is no implication about finite-time death-count monotonicity. Direct full-text retrieval of the motivating manuscript and some older related literature was unavailable; this leaves an originality risk, and no independent mathematical audit has been performed.

## References

1. A. M. V. D. L. Melo and M. C. Santos, *Final size of a structured SIRD Model with active-population force of infection*, arXiv:2601.15388, first public version January 21, 2026. https://arxiv.org/abs/2601.15388
2. A. M. V. D. L. Melo and M. C. Santos, same work, *Communications in Nonlinear Science and Numerical Simulation*, DOI:10.1016/j.cnsns.2026.110430. https://doi.org/10.1016/j.cnsns.2026.110430
3. *Parameter-unrestricted final-size uniqueness and certified geometric bracketing in active-population SIRD networks*, full result available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parameter-unrestricted-final-size-uniqueness-and-certified-geome--86fd5f29697c.
