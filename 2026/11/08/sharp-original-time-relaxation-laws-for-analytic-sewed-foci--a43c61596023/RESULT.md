# Sharp original-time relaxation laws for analytic sewed foci

## Finding

Let a planar piecewise-analytic crossing field have switching line \(y=0\), with local vector fields
\[
(\dot x,\dot y)=(P^+(x,y),Q^+(x,y))\quad (y>0),\qquad
(\dot x,\dot y)=(P^-(x,y),Q^-(x,y))\quad (y<0).
\]
Assume the origin is a stable sewed focus with \(b_+=P^+(0,0)>0\), \(b_-=P^-(0,0)<0\), and \(xQ^\pm(x,0)<0\) for all sufficiently small nonzero \(x\). Denote the analytic half-flight involutions on the switching line by \(\sigma^+\) and \(\sigma^-\), and let \(\chi=\sigma^+-\sigma^-\). Suppose its first nonzero Taylor term is
\[
\chi(x)=-c x^{2p}+O(x^{2p+1}),\qquad c>0,\quad p\in\{1,2,3,\ldots\}.
\]
For any sufficiently small positive-section starting amplitude, write \(r_n>0\) for the successive positive \(x\)-axis crossings, \(t_n\) for their actual elapsed times (\(t_0=0\)), and
\[
K=2\left(\frac1{b_+}+\frac1{|b_-|}\right).
\]
Then the following limits hold, with all constants in original, unrescaled physical time:
\[
\lim_{n\to\infty}n r_n^{2p-1}=\frac1{c(2p-1)},\qquad
\lim_{n\to\infty}\frac{t_{n+1}-t_n}{r_n}=K.
\]
For \(p=1\), there is a finite, strictly positive constant \(C\), dependent on the initial crossing, such that
\[
\boxed{\lim_{n\to\infty}r_n\exp\!\left(\frac{c}{K}t_n\right)=C\in(0,\infty).}
\]
For every \(p\ge2\), the sharp universal law is
\[
\boxed{\lim_{n\to\infty}t_n r_n^{2p-2}=\frac{K}{c(2p-2)}.}
\]
Consequently, the section-based physical-time contraction exponent exists and satisfies
\[
\lim_{n\to\infty}\frac{\log r_n}{t_n}=
\begin{cases}-c/K,&p=1,\\0,&p\ge2.\end{cases}
\]
Every listed exponent is realized by an explicit planar system with polynomial vector fields on the two sides of the switching line.

The mathematical distinction is between decay \(r_n\asymp n^{-1}\) with *exponential decay in physical time* at the first nonzero mismatch order, and decay \(r_n\asymp n^{-1/(2p-1)}\) with *algebraic decay in physical time* at all higher mismatch orders. The transition is not visible from the statement that arrival takes infinite time.

## Assumptions and scope

The side vector fields are real analytic in a common neighborhood of the origin, although they need not agree across \(y=0\). Their horizontal components have the opposite nonzero signs stated above. The transverse sign condition excludes sliding and gives an unambiguous crossing flow away from the singular point. The standard local sewed-focus half-flight maps are analytic decreasing involutions with \(\sigma^\pm(0)=0\), \((\sigma^\pm)'(0)=-1\); see the cited source and the local flow-box construction there. The Taylor assumption specifies the stable, finite-order mismatch branch. It excludes the center, the infinitely flat non-analytic mismatch, and the unstable time-reversed branch. The theorem does not assert that arbitrary non-analytic sewed foci have these rates.

The times are evaluated at successive *positive* switching-line crossings, one completed lower-plus-upper circuit apart. For the stable branch, all sufficiently small positive amplitudes remain in the local crossing neighborhood and decrease to zero. Positive initial crossings need not lie on the same physical orbit as one another; the strong exponential prefactor may vary with the initial condition. The limits do not prescribe an oscillatory pointwise formula for the signed coordinate \(x(t)\) between crossings.

## Proof

**1. Return equation.** The lower half-flight takes a positive section point \(r_n\) to \(s_n=\sigma^-(r_n)<0\). The upper half-flight then returns it to \(r_{n+1}=\sigma^+(s_n)>0\). Since \(\sigma^-\) is an involution,
\[
r_{n+1}-r_n=\sigma^+(s_n)-\sigma^-(s_n)=\chi(s_n).
\]
Analyticity and the derivative \((\sigma^-)'(0)=-1\) give \(s_n=-r_n+O(r_n^2)\). The even leading exponent in \(\chi\) therefore gives the precise local recurrence
\[
 r_{n+1}=r_n-c r_n^{2p}+O(r_n^{2p+1}).\tag{1}
\]
For sufficiently small \(r_n\), the right side is positive and strictly smaller than \(r_n\). Iteration remains local, and the limit is zero because a positive limiting radius would contradict (1) after the neighborhood is chosen sufficiently small. Consequently the origin is not reached at any finite crossing index.

**2. Asymptotics in crossing index.** Put \(q=2p-1\), an odd positive integer. From (1),
\[
r_{n+1}=r_n(1-c r_n^q+O(r_n^{q+1})).
\]
Using the binomial expansion for the reciprocal gives
\[
 r_{n+1}^{-q}-r_n^{-q}=qc+O(r_n).
\]
The error tends to zero; Cesàro averaging yields
\[
\lim_{n\to\infty}\frac{r_n^{-q}}n=qc,
\]
which proves the first displayed limit. This is an infinite-iteration argument, not an inference from finite numerical sampling.

**3. Clock for one crossing circuit.** A lower half-flight traverses horizontal distance \(r_n-s_n=2r_n+O(r_n^2)\), and an upper one traverses \(r_{n+1}-s_n=2r_n+O(r_n^2)\). Uniformly on each small half-flight, \(x=O(r_n)\), \(y=O(r_n^2)\), because the vertical components vanish at the singularity and the horizontal speeds stay bounded away from zero: along either flight, the inequality \(|dy/dx|\le C(|x|+|y|)\) and a Gronwall estimate over a horizontal interval of length \(O(r_n)\) give the stated height bound. Hence analyticity gives \(P^\pm(x,y)=b_\pm+O(r_n)\). Integrating \(dt=dx/P^\pm\), using the correct sign for the lower flight, yields
\[
 t_{n+1}-t_n=K r_n+O(r_n^2),\qquad K=2(b_+^{-1}+|b_-|^{-1}).\tag{2}
\]
This step is essential: the number of returns is not physical time; the duration of each return tends to zero with the crossing radius.

**4. Higher-order mismatch.** For \(p\ge2\), the value \(q=2p-1\) satisfies \(q>1\). Step 2 gives \(r_n\sim(cqn)^{-1/q}\). From (2), the sum of crossing times obeys the standard integral comparison (or Stolz–Cesàro)
\[
 t_n\sim K(cq)^{-1/q}\frac{q}{q-1}n^{1-1/q}.
\]
Multiplication by \(r_n^{q-1}\sim(cqn)^{-(q-1)/q}\) leaves \(K/[c(q-1)]\), exactly the announced \(K/[c(2p-2)]\).

**5. The quadratic mismatch.** When \(p=1\), recurrence (1) reads \(r_{n+1}=r_n-c r_n^2+O(r_n^3)\). Hence
\[
\frac1{r_{n+1}}-\frac1{r_n}=c+O(r_n).
\]
Step 2 gives \(r_n=O(1/n)\), and summation improves the reciprocal estimate to \(r_n^{-1}=cn+O(\log n)\). Accordingly,
\[
 r_n=\frac1{cn}+O\!\left(\frac{\log n}{n^2}\right).
\]
Both error sequences \(r_n-(cn)^{-1}\) and \(r_n^2\) are absolutely summable. From (2), the series of differences between \(t_{n+1}-t_n\) and \(K/(cn)\) therefore converges. Thus \(t_n-(K/c)\log n\) tends to a finite number \(\tau\), accounting for the harmonic-sum constant. The exact prefactor follows:
\[
 r_n e^{(c/K)t_n}\longrightarrow c^{-1}e^{(c/K)\tau}\in(0,\infty).
\]
In particular, the physical-time exponent is \(-c/K\) although the return-index decay is only \(n^{-1}\).

**6. Realization and sharpness.** For any integer \(p\ge1\) and \(c>0\), take the polynomial crossing field
\[
(\dot x,\dot y)=
\begin{cases}
(1,-2x-(2p+1)c x^{2p}),& y>0,\\
(-1,-2x),& y<0.
\end{cases}\tag{3}
\]
Its side fields are analytic, \(b_+=1\), \(b_-=-1\), and near the origin \(xQ^\pm(x,0)<0\), since the linear term controls the higher even-degree perturbation. The lower half-flight maps \(r\mapsto-r\). The upper trajectory from \((-r,0)\) has integral
\[
 y=-x^2-cx^{2p+1}+r^2-cr^{2p+1}.
\]
Its positive return \(u=R(r)\) is the unique small positive solution of
\[
 u^2+c u^{2p+1}=r^2-c r^{2p+1}.
\]
Substitution of \(u=r+s r^{2p}+o(r^{2p})\) equates the coefficient of \(r^{2p+1}\) and gives \(2s+c=-c\), hence \(s=-c\). Therefore \(R(r)=r-c r^{2p}+O(r^{2p+1})\) and \(\chi(x)=-c x^{2p}+O(x^{2p+1})\). All required orders occur in analytic polynomial crossing systems, and \(K=4\) there. This completes the proof.

## Verification

The self-contained `checker.py` verifies the polynomial side-field antiderivatives and return mismatch coefficients exactly for several integers \(p\), and checks independently with high-precision arithmetic that the unique positive return solves the stated implicit equation with the predicted normalization. The checker is supplementary: Steps 1–6 constitute the proof for *all* analytic fields satisfying the hypotheses and every integer \(p\ge1\).

Run `python checker.py` with Python 3, SymPy and mpmath installed. The script uses only the files included here and prints its own finite test counts. The limits themselves are justified by the recurrence and convergent-series arguments, not by the numerical tests.

## Relationship to prior work

Glendinning, Hogan, Homer, Jeffrey and Szalai (arXiv:2306.09743v1, Theorem 1 and Section 2) prove the analytic sewed-focus center-or-infinite-time-focus alternative. Their Section 2 derives the involutions, the even-order first nonzero discrepancy, the local crossing recurrence and divergence of the total flight time. These ingredients are **prior results**, and this finding does not reassert them as new. The new contribution is the *sharp physical-time dependence on the order and coefficient of that discrepancy*, including the positive finite exponential prefactor at the quadratic mismatch, the exact constants for all higher orders, and a polynomial family realizing every case.

Classical parabolic-iteration asymptotics underlie Step 2 and the quadratic refinement. However, a parabolic return-index rate does not alone give physical-time decay, since the return duration vanishes. The universal conversion in Steps 3–5 uses the two physical crossing speeds and is the scientific distinction. Prior studies of finite-time collapse in non-analytic sewed foci concern a different asymptotic regime and do not imply these infinite-time laws.

## Limitations

The theorem concerns crossing radii at positive section times and does not give a uniform signed-coordinate asymptotic between zero crossings. It requires real-analytic side fields and a finite-order mismatch; infinitely flat smooth examples lie outside scope. The positive prefactor in the quadratic case depends on the initial orbit and is not claimed to have a universal closed form. Time-reversed unstable foci are not treated. The corresponding leading rate may be derivable through classical normal-form or Fatou-coordinate literature not indexed in the searched sources; publication priority therefore remains subject to further literature verification. 

## References

1. P. Glendinning, S. J. Hogan, M. Homer, M. R. Jeffrey, R. Szalai, *Uncountably many cases of Filippov's sewed focus*, arXiv:2306.09743v1 (first posted 2023-06-16), Section 2 and Theorems 1–2. Open full text: https://arxiv.org/html/2306.09743v1 . Journal of Nonlinear Science 33 (2023), article 52, https://doi.org/10.1007/s00332-023-09910-4 .
2. A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer, 1988, Section 19.4, cited and discussed in Reference 1. Original text not independently inspected for this report.
