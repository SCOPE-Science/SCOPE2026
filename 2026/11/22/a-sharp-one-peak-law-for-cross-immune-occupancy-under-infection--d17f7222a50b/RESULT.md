# A sharp one-peak law for cross-immune occupancy under infection-driven immune escape

## Finding

In the prevalence-driven four-compartment SIRCm epidemic model, let the feedback strengths governing both stages of immune loss be equal to \(\varepsilon\ge0\), and suppose the intermediate cross-immune class cannot be reinfected (\(\sigma=0\)). Under the positive-rate and endemicity hypotheses stated below, the equilibrium cross-immune fraction \(C^*(\varepsilon)\) obeys a complete, sharp, two-regime classification:

\[
\begin{cases}
\mu\beta\le\delta\gamma &: C^*(\varepsilon)\text{ strictly decreases for }\varepsilon>0,\\
\mu\beta>\delta\gamma &: C^*\text{ strictly rises then strictly falls, with exactly one maximum.}
\end{cases}
\]

Define the dimensionless effective immune-escape factor \(k=1+\varepsilon I^*(\varepsilon)\). In the second regime the maximum is attained precisely at \(k_* = \sqrt{\mu\beta/(\delta\gamma)}\), or at \(\varepsilon_*=(k_*-1)/I(k_*)>0\), with \(I(k)\) and \(C(k)\) given explicitly below. The conclusion holds for **all** nonnegative feedback values, not just weak or strong feedback limits. It is compatible with strictly increasing endemic infection prevalence.

## Assumptions and scope

The normalized population state is \((S,I,R,C)\ge0\), \(S+I+R+C=1\), with susceptible, infected, fully recovered and intermediate cross-immune classes, respectively. Assume \(\mu,\alpha,\beta,\delta,\gamma>0\), \(\beta>\mu+\alpha\), \(\sigma=0\) and \(\varepsilon_1=\varepsilon_2=\varepsilon\ge0\). The autonomous prevalence-driven equations are

\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta SI+\gamma(1+\varepsilon I)C,\\
\dot I&=\beta SI-(\mu+\alpha)I,\\
\dot R&=\beta CI+\alpha I-[\mu+\delta(1+\varepsilon I)]R,\\
\dot C&=\delta(1+\varepsilon I)R-[\beta I+\mu+\gamma(1+\varepsilon I)]C.
\end{aligned}
\]

An *endemic equilibrium* means an equilibrium with \(I>0\). No claim is made about its dynamic stability. Let \(q=(\mu+\alpha)/\beta\in(0,1)\), \(P=1-q>0\), \(k=1+\varepsilon I\ge1\), and

\[
A=\beta\gamma,\quad B=\delta\gamma,\quad D=\mu\beta,\quad E=\delta\alpha P,\quad H(k)=Bk+(\delta+\gamma)(\mu+\alpha)+D/k.
\]

## Proof

**1. Exact scalar classification of the cross-immune fraction.** At every endemic equilibrium, \(\dot I=0\) gives \(S=q\). Substituting this into \(\dot S=0\) gives
\[
I(k)=\frac{\mu P+\gamma kC(k)}{\mu+\alpha},\qquad R(k)=P-I(k)-C(k).
\]
Eliminating \(R\) between the remaining stationary equations yields exactly
\[
F(C,k):=AC^2+H(k)C-E=0.\tag{1}
\]
For every \(k\ge1\), \(F(0,k)=-E<0\) and \(F(C,k)\) is strictly increasing for \(C\ge0\), so there is exactly one positive solution,
\[
C(k)=\frac{2E}{H(k)+\sqrt{H(k)^2+4AE}}>0.\tag{2}
\]
The formulas yield an admissible strictly positive state. Indeed, the stationary \(C\) equation gives \(\delta kR=C(\beta I+\mu+\gamma k)>0\); this equation is equivalent to (1) under the displayed expressions, hence \(R>0\). Mass conservation and \(S=q>0\) complete the stationary equations.

**2. The effective feedback parameter increases strictly.** For completeness, prove the specialized monotonicity rather than presupposing a parameterization. At a fixed candidate infected fraction \(z>0\), put \(G=1+\varepsilon z\), \(D(z)=(\mu+\delta G)(\mu+\gamma G)+\mu\beta z\), \(K(z)=\beta z+\mu+(\delta+\gamma)G\). Eliminating \(R,C\) as linear variables shows that the endemic infected fraction is the unique root of
\[
\Phi(z,\varepsilon)=z+\alpha zK(z)/D(z)=P.\tag{3}
\]
Write \(D(z)=d_0+d_1z+d_2z^2\) and \(K(z)=k_0+k_1z\), where
\[
\begin{aligned}
d_0&=(\mu+\delta)(\mu+\gamma),\\
d_1&=\varepsilon[\delta(\mu+\gamma)+\gamma(\mu+\delta)]+\mu\beta,\\
d_2&=\delta\gamma\varepsilon^2,\\
k_0&=\mu+\delta+\gamma,\\
k_1&=\beta+(\delta+\gamma)\varepsilon.
\end{aligned}
\]
Differentiation of (3) gives
\[
\partial_z\Phi=1+\alpha\frac{k_0d_0+2k_1d_0z+(k_1d_1-k_0d_2)z^2}{D(z)^2}>1.
\]
The last coefficient is strictly positive because it equals
\[
\mu\beta^2+2\beta\varepsilon[\mu(\delta+\gamma)+\delta\gamma]
+\varepsilon^2[\mu(\delta^2+\delta\gamma+\gamma^2)+\delta\gamma(\delta+\gamma)]>0.
\]
Also \(\Phi(0,\varepsilon)=0<P<\Phi(P,\varepsilon)\); hence there is exactly one infected root in \((0,P)\). At fixed \(z\),
\[
\frac{\partial(K/D)}{\partial G}=
-\frac{G\delta\gamma\,[G(\delta+\gamma)+2\beta z+2\mu]}{D^2}<0.
\]
Consequently \(\partial_\varepsilon\Phi<0\) for \(z>0\), and implicit differentiation with \(\partial_z\Phi>0\) yields \(dI^*/d\varepsilon>0\). Thus \(k(\varepsilon)=1+\varepsilon I^*(\varepsilon)\) is continuous and strictly increasing. Since \(I^*(\varepsilon)\ge I^*(0)>0\), \(k(\varepsilon)\to\infty\). Therefore \(\varepsilon\mapsto k\) is a bijection from \([0,\infty)\) to \([1,\infty)\).

**3. One-peak law and sharp boundary.** Differentiating (1) along its positive root gives
\[
\frac{dC}{dk}=-\frac{C(k)H'(k)}{2AC(k)+H(k)},\qquad H'(k)=B-D/k^2.
\]
Every factor outside \(-H'\) is strictly positive. If \(D\le B\), then \(H'(k)>0\) for \(k>1\) (at equality its derivative at \(k=1\) vanishes), and \(C(k)\) strictly decreases. If \(D>B\), \(H'\) has the unique zero \(k_*=\sqrt{D/B}>1\), is negative before it and positive after it. This proves strict rise then strict fall, unique global maximum and exact crossover. At the maximizer, put \(H_*=(\delta+\gamma)(\mu+\alpha)+2\sqrt{\mu\beta\delta\gamma}\); equations (1)-(2) give \(C_*=2E/[H_*+\sqrt{H_*^2+4AE}]\), \(I_*=(\mu P+\gamma k_*C_*)/(\mu+\alpha)\) and \(\varepsilon_*=(k_*-1)/I_*\). As \(k\to\infty\), \(C(k)\sim E/(Bk)\to0\), so the peak is global, not merely local. This completes the proof.

## Verification

The accompanying `verify.py` independently checks stationary elimination, conservation, the exact feedback-derivative numerator, positivity-coefficient identities, the closed-form rational/radical example, and 60 rational positive-rate configurations. Run `python verify.py` with Python 3 and SymPy. The all-parameter conclusion is the displayed algebraic proof, not finite testing.

As an exact witness, take \(\mu=\alpha=\delta=\gamma=1\), \(\beta=4\), \(\sigma=0\). Then \(P=1/2\), \(k_*=2\), \(\varepsilon_*=4(1+\sqrt2)/3\), \(C(0)=(\sqrt{89}-9)/8\), and \(C_*= (3\sqrt2-4)/4>C(0)\). Despite this nonmonotonic immune compartment, the endemic infection fraction increases strictly with feedback.

## Relationship to prior work

Ramírez-Gutiérrez, Lóczi, Muñoz-Moncayo and Ketcheson [1] introduce SIRCm, the prevalence-driven equations and endemic existence, including small- and large-feedback asymptotics. Their paper's full text (model, Sections 3–4 and appendices) does not state the sharp cross-immune occupancy classification (1)–(2). A published all-feedback theorem [2] already proves endemic uniqueness and infected-prevalence monotonicity for this system; the monotonicity mechanism is reproduced in specialized form above and **is not claimed as new**. The new claim is the exact all-feedback classification of the cross-immune state under matched immune-loss amplification, including its sharp threshold and finite-feedback optimum. Generic compartmental balance and inverse-square turning points alone do not imply the model-specific parameter condition without the elimination and positive-feedback correspondence.

## Limitations

The result applies to the prevalence-driven formulation with exactly equal feedback strengths and the allowed endpoint \(\sigma=0\). It is not a result for arbitrary \(\sigma\), unequal feedback strengths, transmission-driven feedback, seasonality, parameter estimation, or clinical immunity. Endemic uniqueness and rising infected prevalence are independently known in broader scope; only the cross-immune peak law is assessed here. Equilibrium stability is not asserted, and an equilibrium maximum need not describe transient immune response. Unindexed or inaccessible prior papers could contain equivalent statements.

## References

1. D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo and D. I. Ketcheson, *Compartmental epidemiological models with infection-driven immune escape*, arXiv:2610.01111v1, first publicly released October 1, 2026. https://arxiv.org/html/2610.01111v1
2. *All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system*, public mathematical result, October 11, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342
3. R. Casagrandi, L. Bolzoni, S. A. Levin and V. Andreasen, *The SIRC model and influenza A*, Mathematical Biosciences 200 (2006), 152–169. https://doi.org/10.1016/j.mbs.2005.12.029
