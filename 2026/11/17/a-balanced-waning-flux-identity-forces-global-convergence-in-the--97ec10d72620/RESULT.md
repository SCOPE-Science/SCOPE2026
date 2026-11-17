# A balanced waning-flux identity forces global convergence in the prevalence-driven SIRCm model

## Finding

For the four-compartment, autonomous **prevalence-driven** SIRCm epidemic model, equal immune-escape feedback strengths and the balanced rate condition \(\gamma=\sigma\delta\) create an exact planar dynamical factor. At every nonnegative feedback strength, the complete epidemic behavior on the population simplex is determined by the familiar threshold \(\mathcal R_0=\beta/(\mu+\alpha)\): extinction is global at and below one, and a single strictly positive endemic state attracts **every** initially infected trajectory above one. In particular, this balanced family permits no nonconstant periodic solutions and no unstable endemic equilibrium, no matter how strongly prevalence drives immune escape.

The result is a global dynamical assertion, not merely an equilibrium-uniqueness or a weak-/strong-feedback local-stability statement. Its essential certificate is an explicit strict entropy--quadratic Lyapunov identity. For \(0<\sigma<1\), exact planar closure by the specified immunity aggregate occurs precisely at the balanced rate condition.

## Assumptions and scope

Let \(\mu,\alpha,\beta,\delta,\gamma>0\), \(0<\sigma\le1\) and \(\varepsilon\ge0\). We work on the forward-invariant simplex \(\Omega=\{(S,I,R,C)\in[0,1]^4:S+I+R+C=1\}\). Consider

\[
\begin{aligned}
\dot S&=\mu(1-S)-\beta SI+\gamma(1+\varepsilon I)C,\
\dot I&=\beta SI+\sigma\beta CI-(\mu+\alpha)I,\
\dot R&=(1-\sigma)\beta CI+\alpha I-\mu R-\delta(1+\varepsilon I)R,\
\dot C&=\delta(1+\varepsilon I)R-\beta CI-\mu C-\gamma(1+\varepsilon I)C.
\end{aligned}
\]

Assume the **flux-balance identity** \(\gamma=\sigma\delta\). Define \(k=1-\sigma\), \(U=R+kC\), \(h=\mu+\alpha\), \(a=\mu+\gamma>0\), and \(b=\gamma\varepsilon\ge0\). For \(\beta>h\) also define \(v=1-h/\beta\in(0,1)\).

The theorem concerns unforced, fixed-rate, prevalence-driven feedback, not the transmission-driven feedback choice \(g=SI\), seasonally varying contact rates, or unequal feedback coefficients. At \(\sigma=1\), the aggregate is simply \(U=R\); the necessity statement below is restricted to \(0<\sigma<1\).

## Proof

**1. Exact aggregation and its structural boundary.** Combining the infectious equation with conservation yields

\[
\dot I=I[\beta-h-\beta(I+U)].
\]

A direct combination of the recovered and cross-immune equations, before imposing balance, gives

\[
\dot U=\alpha I-[\mu+\sigma\delta(1+\varepsilon I)]U
 +(1-\sigma)(\sigma\delta-\gamma)(1+\varepsilon I)C.
\]

At \(\gamma=\sigma\delta\), the cross-immune term cancels identically. Therefore the planar factor is

\[
\boxed{\quad\dot I=I[\beta-h-\beta(I+U)],\qquad
\dot U=\alpha I-(a+bI)U.\quad}
\tag{1}
\]

Moreover, the remaining coordinate is a stable nonautonomous scalar equation,

\[
\dot C=\delta(1+\varepsilon I)U-
 [\beta I+\mu+(\gamma+k\delta)(1+\varepsilon I)]C.
\tag{2}
\]

For any physical initial condition \(I\ge0\), \(U\ge0\) and \(I+U\le1\), since \(I+U=1-S-\sigma C\). When \(0<\sigma<1\), states in the interior with the same \((I,U)\) but different \(C\) exist. The displayed coefficient of \(C\) in \(\dot U\) vanishes for all such states if and only if \(\gamma=\sigma\delta\). This establishes the exact boundary for this aggregate's planar closure.

**2. Disease extinction at and below threshold.** If \(\beta<h\), equation (1) gives \(0\le I(t)\le I(0)e^{-(h-\beta)t}\). At equality it gives \(\dot I\le-\beta I^2\), hence for initially infected states \(I(t)\le[\beta t+I(0)^{-1}]^{-1}\). The stable linear equation \(\dot U=\alpha I-(a+bI)U\) implies \(U(t)\to0\). The coefficient multiplying \(-C\) in (2) is at least \(\mu>0\) and the forcing tends to zero; hence \(C(t)\to0\). Then \(R=U-kC\to0\) and \(S=1-I-R-C\to1\). The same conclusion holds for \(I(0)=0\) by direct exponential decay of \(U\) and \(C\).

**3. Existence, uniqueness, and physicality above threshold.** Let \(\beta>h\) and \(v=1-h/\beta\). At a positive equilibrium of (1), the first equation requires \(U=v-I\), whereas the second requires \(U=\alpha I/(a+bI)\). The former is strictly decreasing from \(v\) to zero on \((0,v)\), while the latter is strictly increasing from zero. They have one intersection \((I_*,U_*)\) with both coordinates positive. Equivalently,

\[
 b I_*^2+(a+\alpha-bv)I_*-av=0,
 \qquad U_*=v-I_*.
\tag{3}
\]

For \(b=0\), this gives \(I_*=av/(a+\alpha)\). For \(b>0\), the unique positive root is specified by (3), or the quadratic formula. The original system then has a unique steady cross-immune coordinate

\[
C_*=\frac{\delta(1+\varepsilon I_*)U_*}
{\beta I_*+\mu+(\gamma+k\delta)(1+\varepsilon I_*)},
\quad R_*=U_*-kC_*,\quad S_*=1-I_*-R_*-C_*.
\tag{4}
\]

These coordinates are physically positive: \(C_*>0\), \(R_*=U_*[\beta I_*+\mu+\gamma(1+\varepsilon I_*)]/[\beta I_*+\mu+(\gamma+k\delta)(1+\varepsilon I_*)]>0\); the susceptible equation at equilibrium then yields \(S_*=[\mu+\gamma(1+\varepsilon I_*)C_*]/[\mu+\beta I_*]>0\). Conservation gives their total mass one.

**4. A global strict Lyapunov identity.** The equilibrium relation \(\alpha I_*=(a+bI_*)U_*\) implies

\[
q=\alpha-bU_*=\frac{aU_*}{I_*}>0.
\]

For \(I>0\) in the simplex, set

\[
\boxed{\quad V(I,U)=I-I_*-I_*\log(I/I_*)
+\frac{\beta}{2q}(U-U_*)^2.\quad}
\tag{5}
\]

Writing \(x=I-I_*\), \(y=U-U_*\), equation (1) has the exact translated form

\[
\dot I=-\beta I(x+y),\qquad
\dot U=qx-(a+bI)y.
\]

Consequently the cross terms cancel and

\[
\boxed{\quad\dot V=-\beta(I-I_*)^2
-\frac{\beta}{q}(a+bI)(U-U_*)^2.\quad}
\tag{6}
\]

This is strictly negative away from the endemic factor equilibrium. Moreover, \(V\to\infty\) as \(I\downarrow0\), so every initially infected trajectory is trapped in a compact sublevel set bounded away from the extinction face. LaSalle's invariance principle applied to (6) gives \((I(t),U(t))\to(I_*,U_*)\). The scalar forced linear equation (2) has a damping coefficient bounded below by \(\mu>0\), and its coefficients and forcing converge to constants, so \(C(t)\to C_*\). The definitions then yield \((S,I,R,C)(t)\to(S_*,I_*,R_*,C_*)\). The planar linearization is Hurwitz by the strict quadratic local form of (6), while the third scalar mode has a negative coefficient; hence this equilibrium is also locally exponentially attracting within the simplex.

When \(I(0)=0\), infection remains absent and the solution converges to the disease-free equilibrium. Thus the basins are precisely separated by the invariant extinction face, and no nonconstant periodic orbit can occur in the population simplex. \(\square\)

## Verification

The bundled standard-library Python program `check.py` tests exact vector-field conservation, exact aggregate reduction, and the exact scalar remainder equation on 2,400 rational parameter/state samples; it additionally tests the endemic relation and the mixed entropy derivative on these same samples. Run `python check.py` using Python 3. A successful run prints `PASS: 2400 independent rational vector-field and floating entropy-identity trials`. This is supplementary arithmetic consistency evidence; the universal claim rests on the displayed algebra and Lyapunov argument, not finite sampling.

## Relationship to prior work

Ramírez-Gutiérrez, Lóczi, Muñoz-Moncayo, and Ketcheson [1] introduced both SIRCm feedback models. For equal prevalence feedback, they found numerical stability along the feedback diagonal, while proving existence generally and uniqueness/local stability in the weak and strong feedback regimes. Their model equations and those bounds are prior work; their manuscript does not supply the balanced-flux planar closure or the all-feedback global Lyapunov conclusion.

A separately published exact prevalence-driven SIRCm theorem [2] already establishes unconditional endemic **uniqueness** and separate parameter monotonicity for arbitrary feedback coefficients. Those facts are prior, and are not claimed here as new. Its statement explicitly excludes local/global stability. The present result is the *global convergence and exclusion of oscillatory behavior* for the flux-balanced subfamily, with an explicit dynamical certificate, not the equilibrium census of [2]. The classical SIRC model of Casagrandi et al. [3] has no infection-dependent escape feedback; its analysis does not, from the inspected summary, imply a global theorem for the present positive-feedback family. Related SIRS models with immunity delays [4] have different dynamics and allow stability switches.

## Limitations

The exact balance condition \(\gamma=\sigma\delta\) is a restrictive but structurally singled-out rate relation; no global convergence is claimed for unbalanced feedback models, for \(g=SI\), or for unequal feedback strengths. In particular, the motivating paper reports numerical Hopf transitions for a transmission-driven model, which this theorem does not contradict. The theorem is deterministic and unforced; it is not an inference about real-world epidemic policy or measured mutation dynamics. The result has undergone only self-review; independent mathematical validation has not been performed. Broad historical priority cannot be proven solely from finite indexed searches.

## References

1. D. R. Ramírez-Gutiérrez, L. Lóczi, C. Muñoz-Moncayo, D. I. Ketcheson, *Compartmental epidemiological models with infection-driven immune escape*, arXiv:2610.01111v1, first posted 2026-10-01. https://arxiv.org/html/2610.01111v1
2. *All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system*, published-finding corpus (published 2026-10-11), repository record `2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342`, full RESULT.md inspected. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342
3. R. Casagrandi, L. Bolzoni, S. A. Levin, V. Andreasen, *The SIRC model and influenza A*, Mathematical Biosciences 200 (2006), 152–169. https://doi.org/10.1016/j.mbs.2005.12.029
4. M. V. Barbarossa, M. Polner, G. Röst, *Stability switches induced by immune system boosting in an SIRS model with discrete and distributed delays*, SIAM Journal on Applied Mathematics 77 (2017), 905–923. https://doi.org/10.1137/16M1077234
