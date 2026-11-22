# Exponential founding-time marks for Gumbel extremes in a singular birth–death excursion model

## Finding

Fix an excursion-immigration intensity \(\rho>0\) in the singular birth–death process constructed from Itô's symmetric Brownian excursion measure. At a deterministic observation time \(t\), each living particle has a position and its original birth time. This result identifies the **joint law of extreme positive positions and their birth-time marks**, not just the previously known unmarked maximum law.

Write \(A(y)=\int_y^\infty\operatorname{erfc}(w)\,dw\). For \(t>\pi/2\), let \(u_t>0\) solve \(\sqrt{2t}\,A(u_t)=1\), and define \(c_t=\sqrt{2t}\,u_t\) and \(v_t=\sqrt{t}/(\sqrt{2}u_t)\). For each positive particle \(i\) living at \(t\), let \(X_i(t)>0\) be its location and \(B_i\in(0,t)\) its birth time. Then, as \(t\to\infty\),
\[
\boxed{\ \sum_{i:X_i(t)>0}\delta_{\left((X_i(t)-c_t)/v_t,\;u_t^2 B_i/t\right)}
\ \Longrightarrow\ \operatorname{PPP}\bigl(\rho e^{-z-r}\,dz\,dr\bigr)\ }
\]
in the space of locally finite point measures on \(\mathbb R\times[0,\infty)\), with vague convergence. In particular, if \(M_t\) is the maximum positive location (zero if there is none), and \(B_t\) is the birth time of the unique maximizing particle whenever \(M_t>0\), then
\[
\left(\frac{M_t-c_t}{v_t},\frac{u_t^2 B_t}{t}\right)
\ \Longrightarrow\ (G_\rho,E),\qquad
\Pr(G_\rho\le z)=\exp(-\rho e^{-z}),\quad
\Pr(E>r)=e^{-r},
\]
where \(G_\rho\) and \(E\) are independent. This is equivalent to \(B_t/(2t/\log t)\Longrightarrow E\). The birth-time marks of any fixed number of the largest positive particles converge jointly to independent rate-one exponentials, independent of their ordered limiting heights.

There is also an **exact finite-time conditional birth-time law**: for every deterministic \(t>0\), \(x>0\), and \(0\le b<t\), a regular conditional version satisfies
\[
\boxed{\ \Pr(B_t>b\mid M_t=x)
=\frac{\operatorname{erfc}\bigl(x/\sqrt{2(t-b)}\bigr)}
{\operatorname{erfc}\bigl(x/\sqrt{2t}\bigr)}\ .\ }
\]
The conditioning is on \(M_t>0\); \(B_t=0\) may be used by convention on \(M_t=0\), an event whose probability tends to zero.

## Assumptions and scope

The process is precisely the Poisson system of independent excursions on the real line, \(\Theta=\sum_i\delta_{(B_i,e_i)}\), with intensity \(\rho\,db\otimes\mathbf n(de)\), as in Kou (2026). Every excursion starts at its own birth time at the origin, moves independently until first return to zero, and carries the real-valued position \(X_i(t)=e_i(t-B_i)\) when alive. The Brownian generator is \(\frac12\partial_{xx}\); the excursion entrance density is \(\mathbf n_a(dx)=|x|(2\pi a^3)^{-1/2}e^{-x^2/(2a)}dx\) for \(a>0\) and \(x\ne0\). No extra conditioning on total population size or on survival is imposed. The observation time tends to infinity through real values, with \(\rho\) held fixed. The marked limit concerns positive locations only; a symmetric statement holds separately for negative particles. All exponential distributions have unit rate.

For any fixed \(t>0\), the number of positive living particles is finite almost surely, their locations are distinct almost surely, and \(\Pr(M_t=0)=\exp(-\rho\sqrt{2t/\pi})\). The definitions involving positive \(u_t\) are used only for sufficiently large \(t\), as required for the limit.

## Proof

**Step 1: an exact time-marked Poisson intensity.** The mapping theorem for Poisson point processes, applied to the excursion atoms \((b,e)\mapsto(b,e(t-b))\) with \(b<t\) and excursion lifetime exceeding \(t-b\), gives an independent Poisson process on \((0,t)\times(0,\infty)\) with intensity
\[
\mu_t(db\,dx)
=\rho\frac{x}{\sqrt{2\pi(t-b)^3}}
\exp\left[-\frac{x^2}{2(t-b)}\right]db\,dx.
\]
The integral in birth time has the exact evaluation
\[
\int_{b_0}^{t}\frac{x}{\sqrt{2\pi(t-b)^3}}e^{-x^2/[2(t-b)]}\,db
=\operatorname{erfc}\left(\frac{x}{\sqrt{2(t-b_0)}}\right)
\quad(0\le b_0<t).
\]
In particular the unmarked positive-position intensity is \(\rho\operatorname{erfc}(x/\sqrt{2t})\,dx\), and the number of such points is Poisson with mean \(\rho\sqrt{2t/\pi}\). The same formula for \(b_0>0\) supplies the conditional birth-time tail at a specified positive location.

**Step 2: the exact conditional maximizing-point mark.** Almost surely there are no tied positive positions. Given the top positive position lies near \(x>0\), the no-higher-point event is independent of the birth time of its marked point, by independence of Poisson restrictions. Thus the conditional mark kernel at the maximizing positive point is the normalized intensity \(\mu_t(db\,dx)\) at \(x\), with normalizer \(\rho\operatorname{erfc}(x/\sqrt{2t})\,dx\). Applying the birth-time integral from Step 1 proves the boxed finite-time formula; this can equivalently be obtained from the Campbell–Mecke identity. No conditioning on a probability-zero event is used other than a regular conditional density.

**Step 3: exact transformed intensity and its local limit.** Put \(u=u_t\), \(q=u+z/(2u)\), \(r=u^2b/t\), and \(x=c_t+v_tz=\sqrt{2t}\,q\). The change of variables in Step 1 shows that the image of \(\mu_t\) on \(z>-2u^2\), \(0<r<u^2\) has density
\[
f_t(z,r)=\frac{\rho\sqrt{2t}}{2\sqrt\pi}\frac{q}{u^3}
\left(1-\frac{r}{u^2}\right)^{-3/2}
\exp\left[-\frac{q^2}{1-r/u^2}\right].
\]
As \(t\to\infty\), \(u_t\to\infty\), and elementary Gaussian-tail integration gives
\[
A(u)=\frac{e^{-u^2}}{2\sqrt\pi\,u^2}\bigl(1+O(u^{-2})\bigr),
\qquad
\frac{\sqrt{2t}\,e^{-u_t^2}}{2\sqrt\pi\,u_t^2}\to1.
\]
For every compact rectangle in \(\mathbb R\times[0,\infty)\), \(q/u\to1\), \((1-r/u^2)^{-3/2}\to1\), and
\[
\frac{q^2}{1-r/u^2}=u^2+z+r+o(1)
\]
uniformly. Hence \(f_t(z,r)\to\rho e^{-z-r}\) locally uniformly. Convergence of the Poisson Laplace functionals for every compactly supported nonnegative continuous test function proves the asserted vague marked-point-process convergence.

**Step 4: keeping extreme birth-time marks from escaping.** Vague convergence on its own does not justify selecting the largest point on an unbounded region. For any fixed \(z_0\in\mathbb R\) and \(R\ge0\), the exact expected number of marked particles with \(z>z_0\) and \(r>R\) (when \(R<u_t^2\)) equals
\[
\rho\sqrt{2t\left(1-R/u_t^2\right)}
\,A\left(\frac{u_t+z_0/(2u_t)}{\sqrt{1-R/u_t^2}}\right)
\ \longrightarrow\ \rho e^{-z_0-R}.
\]
Likewise the expected number above height \(z_0\), irrespective of mark, tends to \(\rho e^{-z_0}\). Therefore all points above any fixed height threshold have asymptotically tight birth-time marks. The limiting mean number above \(z_0\) tends to infinity as \(z_0\downarrow-\infty\), so for every fixed rank \(k\), choosing sufficiently negative \(z_0\) makes the probability of fewer than \(k\) points arbitrarily small. Choosing a sufficiently high upper threshold makes the probability of any point above it arbitrarily small. Tightness, truncation, and the continuous mapping theorem now give joint convergence for each fixed number of top ranked positions and marks. Because \(\rho e^{-z-r}\,dz\,dr=(\rho e^{-z}\,dz)(e^{-r}\,dr)\), the limiting rank marks are independent rate-one exponentials, independent of all ranked heights. The first height has CDF \(\exp(-\rho e^{-z})\).

**Step 5: birth-time scale.** The Gaussian-tail centering equation implies \(u_t^2/\log t\to1/2\). Hence \(u_t^2B_t/t\Rightarrow E\) is equivalent, by Slutsky's theorem, to \(B_t/(2t/\log t)\Rightarrow E\). This is a law for the original *birth time since the process began*, not the elapsed age \(t-B_t\); in particular the winning excursion has age \(t-O_{\Pr}(t/\log t)\).

## Verification

The standalone `checker.py` reproduces 104 finite integral, Gaussian-tail derivative, exact centering, transformed-intensity, and exponential-mark diagnostics with Python's standard library. Execute `python3 checker.py` in a directory containing that file; the corresponding output is in `verification_output.txt`. These numerical tests are supplemental and do not establish convergence. Steps 1–5 give the analytical argument, including the needed non-escape estimate for the ranked extremes.

## Relationship to prior work

Kou (2026, arXiv:2611.19362v1) establishes the construction, exact unmarked positive-position intensity, and the Gumbel law for the maximum positive position (Theorem 1.6 and Sections 2 and 5). Those results are credited, not presented as new. The cited sections derive no distribution for the winning particle's original birth time and no joint birth-time-marked extremal Poisson limit. The present claim adds the **exact conditional founder-time kernel**, the joint marked limit, the scale \(2t/\log t\), and independence of founder marks from the entire top-order height process. An unmarked Gumbel theorem alone cannot imply those marked conclusions.

A published study of polynomially immigrating critical geometric branching clans, *Gumbel extremes and Gamma founder-time localization for polynomially immigrating critical branching clans* (2026), proves a structurally analogous marked Gumbel theorem in a discrete genealogical setting with polynomial immigration and geometric clan-size tails. That result does not apply to Itô Brownian excursion immigration, whose continuous entrance density and Gaussian-tail centering produce different marks and scalings. *Multivariate Pareto excursions and a Gamma reset-age law in a first-passage-resetting Brownian gas* (2026) concerns a finite, jointly reset **stationary** diffusion population with Pareto remote tails; its clock and conditioning are unrelated to birth times in the growing Poisson excursion ensemble. Standard Poisson marking theory supplies a technique but does not determine this particular conditional birth-time kernel or asymptotic intensity. A 2026 study on maxima and their times within individual Brownian excursions treats a different temporal observable from the immigration birth time at fixed observation time.

## Limitations

This is an exact special-model result: no universality across other excursion entrance laws, interacting particles, finite-rate immigration mechanisms, or alternate time-dependent intensities is asserted. The conclusion is at one observation time tending to infinity; it is not a temporal point-process limit jointly over observation times. The finite-time conditional formula is a regular conditional distribution for positive maximum locations, not for the event \(M_t=0\). The unmarked maximum law and model construction are prior work. Finite diagnostic checks are not proofs of asymptotic claims. Publication priority is assessed only against the cited inspected sources and accessible mathematical records; older broad marked-excursion and point-process theorems may contain an implicit equivalent.

## References

1. R. Kou, *Singular Birth-Death model*, arXiv:2611.19362v1, first publicly posted 2026-11-14, https://arxiv.org/html/2611.19362v1 (model and entrance law, Section 1; unmarked point-process density, Proposition 2.5; maximum law, Theorem 1.6; proof, Section 5.3).
2. G. Last and M. Penrose, *Lectures on the Poisson Process*, Cambridge University Press, 2017, Chapter 5, mappings and markings, https://doi.org/10.1017/9781316104477.
3. *Gumbel extremes and Gamma founder-time localization for polynomially immigrating critical branching clans*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-gumbel-extremes-and-gamma-founder-time-localization-for-polynomi--710036798089.
4. *Multivariate Pareto excursions and a Gamma reset-age law in a first-passage-resetting Brownian gas*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-multivariate-pareto-excursions-and-a-gamma-reset-age-law-in-a-fi--c03a80e1262c.
5. K. Somnatha and R. Herbei, *Joint exact simulation of the maximum and its location for some constrained Brownian processes*, Journal of Statistical Computation and Simulation (2026), https://doi.org/10.1080/00949655.2026.2641543.
