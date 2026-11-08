# An exact positive three-factor split for two-state Markov generators

## Finding

Let \(Q_A,Q_B\) be any two conservative two-state continuous-time Markov generators, written with column probability vectors as
\[
Q_A=\begin{pmatrix}-u_A&v_A\\u_A&-v_A\end{pmatrix},\qquad
Q_B=\begin{pmatrix}-u_B&v_B\\u_B&-v_B\end{pmatrix},
\]
where all four off-diagonal rates are nonnegative and \(a=u_A+v_A>0\), \(b=u_B+v_B>0\). For every \(h>0\), set
\[
\boxed{\vartheta(h)=\frac{1}{ah}\log\!\left(\frac{(a+b)(1-e^{-bh})}{b(1-e^{-(a+b)h})}\right).}
\]
Then the following **exact matrix identity** holds, without a commutativity assumption:
\[
\boxed{e^{h(Q_A+Q_B)}=e^{\vartheta(h)hQ_A}\,e^{hQ_B}\,e^{(1-\vartheta(h))hQ_A}.}
\]
Every factor is a nonnegative, column-stochastic Markov transition matrix. The splitting coefficients use precisely total time \(h\) for each generator and strictly positive substep times. More precisely, \(\vartheta\) is strictly decreasing, \(0<\vartheta(h)<1/2\), and
\[
\begin{aligned}
\vartheta(h)&=\tfrac12-\frac{a+2b}{24}h+O(h^3)&& (h\downarrow0),\\
\vartheta(h)&\sim\frac{\log((a+b)/b)}{ah}&&(h\to\infty).
\end{aligned}
\]
If \([Q_A,Q_B]\ne0\), this is the **unique real allocation** in the three-factor family with the stated total substep times that gives equality. In that case, neither of the two-factor endpoint splittings is exact at any \(h>0\); no constant allocation can be exact at all step sizes. If the generators commute, all allocations give the exact propagator.

Furthermore, for \([Q_A,Q_B]\ne0\), the ordinary symmetric Strang allocation \(\vartheta=1/2\) has a genuinely nonzero cubic local error. For a unit-mass input \(p=(x,1-x)^\mathsf T\), writing \(\pi_A=v_A/a\) and \(\pi_B=v_B/b\),
\[
\left(e^{hQ_A/2}e^{hQ_B}e^{hQ_A/2}-e^{h(Q_A+Q_B)}\right)p
=-\frac{ab(a+2b)}{24}(\pi_B-\pi_A)h^3
\begin{pmatrix}1\\-1\end{pmatrix}+O(h^4).
\]
This coefficient does not depend on the initial unit-mass input.

## Assumptions and scope

The matrices are finite-dimensional real conservative generators under the **column** convention; \(h>0\), \(a>0\), and \(b>0\). Zero individual transition rates are permitted. The formula is for autonomous generators and the probability evolution \(p'= (Q_A+Q_B)p\), without an additional source or nonlinear forcing. Matrix equalities extend to signed vectors by linearity; positivity and probability preservation concern probability vectors.

## Proof

**1. Reduction to affine scalar flows.** The first-state probability \(x\) obeys under generator \(Q_i\) the scalar ODE
\[
\dot x=-\lambda_i(x-\pi_i),\qquad
\lambda_A=a,\quad\lambda_B=b,\quad
\pi_A=v_A/a,\quad\pi_B=v_B/b.
\]
Its exact flow is \(F_i(t)x=\pi_i+e^{-\lambda_i t}(x-\pi_i)\). The exact joint flow contracts by \(r=e^{-(a+b)h}\) around \(\pi_*=(a\pi_A+b\pi_B)/(a+b)\).

**2. Exact composition and uniqueness.** Multiplying the three affine maps in the matrix order asserted gives
\[
F_A(\theta h)F_B(h)F_A((1-\theta)h)x
=rx+(1-r)\big((1-w_B(\theta))\pi_A+w_B(\theta)\pi_B\big),
\]
with
\[
w_B(\theta)=\frac{e^{-a\theta h}(1-e^{-bh})}{1-e^{-(a+b)h}}.
\]
Both sides have the same linear coefficient \(r\). If \(\pi_A\ne\pi_B\), the two maps agree precisely when \(w_B(\theta)=b/(a+b)\), whose unique real solution is the displayed \(\vartheta(h)\). Since both maps conserve total mass, equality for the first coordinate of every probability input is equality of the two full \(2\times2\) matrices. If \(\pi_A=\pi_B\), both generators contract about the same point, hence every allocation works. Direct multiplication gives \([Q_A,Q_B]=0\) if and only if \(\pi_A=\pi_B\).

**3. Sharp positive allocation and monotonicity.** Let \(S=a+b\) and
\[
F(h)=\log\frac{S(1-e^{-bh})}{b(1-e^{-Sh})}.
\]
We have \(F(0+)=0\) and
\[
F'(h)=\frac{b}{e^{bh}-1}-\frac{S}{e^{Sh}-1}>0.
\]
The strict inequality holds because \(z/(e^{zh}-1)\) decreases with \(z>0\). Moreover,
\[
F''(h)=-\left(\frac{b}{2\sinh(bh/2)}\right)^2
+\left(\frac{S}{2\sinh(Sh/2)}\right)^2<0,
\]
using the strict decrease of \(z/\sinh(zh/2)\). Thus \(F\) is strictly increasing and strictly concave, so \(F(h)/(ah)=\vartheta(h)\) is positive and strictly decreasing. Its limit at zero is \(F'(0+)/a=1/2\), proving \(0<\vartheta(h)<1/2\). The representation
\[
\vartheta(h)=\frac12+\frac{1}{ah}\log\!\left(\frac{S\sinh(bh/2)}{b\sinh(Sh/2)}\right)
\]
and the Taylor series of \(\log(\sinh z/z)\) yield the stated small-step expansion. The finite limit \(F(\infty)=\log(S/b)\) gives the large-step law. Consequently the two substeps of \(Q_A\) are strictly positive, as is the middle \(Q_B\) step, and every matrix exponential is stochastic and entrywise nonnegative.

**4. Minimality and Strang error.** A two-factor splitting with the prescribed total times is an endpoint \(\theta=0\) or \(\theta=1\); strict uniqueness and \(0<\vartheta<1/2\) exclude both when \(\pi_A\ne\pi_B\). The small-step expansion of \(\vartheta\) also rules out any fixed \(\theta\) being exact for all \(h>0\). Finally, at \(\theta=1/2\), use
\[
\frac{\partial w_B}{\partial\theta}=-ahw_B,
\qquad \vartheta(h)=\frac12-\frac{a+2b}{24}h+O(h^3)
\]
together with \(w_B(\vartheta)=b/S\) and \(1-r=Sh+O(h^2)\). This gives
\[
(1-r)(\pi_B-\pi_A)\big(w_B(1/2)-b/S\big)
=-\frac{ab(a+2b)}{24}(\pi_B-\pi_A)h^3+O(h^4),
\]
which is precisely the first component of the stated vector error; the second component is its negative. For noncommuting generators, \(\pi_B-\pi_A\ne0\), so the cubic coefficient is nonzero.

## Verification

The self-contained standard-library program `verify.py` evaluates each generator exponential from \(e^{tQ}=I+(1-e^{-\lambda t})Q/\lambda\), checks the three-factor identity on a reproducible positive-rate grid, checks column sums and nonnegative entries, tests strictly decreasing positive coefficients for representative rate ratios, and checks the nonzero Strang cubic coefficient. Running `python verify.py` produces its actual test summary. These floating-point checks supplement the full analytic proof and are not used as proof of an all-parameter statement.

## Relationship to prior work

Battestini, Caliari, and Cassini (2026) analyze Lie–Trotter and Strang splitting errors and split exponential integrators for general noncommuting operators; their general error estimates do not assert the present exact positive two-state three-factor allocation. Sumner (2012) describes the Lie geometry and a different factorization of all \(2\times2\) Markov matrices, rather than a prescribed-generator, exact, positivity-preserving splitting with total substep-time constraints. Van-Brunt and Visser (2015) provide exact Baker–Campbell–Hausdorff identities for certain solvable Lie algebras, a broader algebraic framework from which related special formulas may be derived; the constrained positive allocation, strict monotonicity, and uniqueness above are the specific claim evaluated here. Chin (2005) studies positive exponential decompositions for general operators; its fixed-coefficient discussion is not an exact formula for this special two-state, step-dependent case.

## Limitations

The identity depends on the one-dimensional nonconserved mode of a two-state Markov chain and is not claimed for three or more states, general noncommuting matrices, inhomogeneous problems, or nonlinear forcing. It does not improve the asymptotic operation count over using a directly available \(2\times2\) exponential. Scientific priority remains uncertain if an older general factorization theorem explicitly specializes to the same constrained positive substeps; no independent literature-wide priority certification is claimed. The numerical checker cannot establish infinite-precision reliability of floating-point implementations, especially for extreme rate ratios.

## References

1. L. Battestini, M. Caliari, F. Cassini, *Analysis of split exponential integrators for semilinear problems with noncommuting operators*, arXiv:2610.07989 (first public 2026-10-06), https://arxiv.org/abs/2610.07989.
2. J. G. Sumner, *Lie geometry of 2x2 Markov matrices*, arXiv:1212.5311 (2012), https://arxiv.org/abs/1212.5311.
3. A. Van-Brunt, M. Visser, *Explicit Baker–Campbell–Hausdorff formulae for some specific Lie algebras*, arXiv:1505.04505 (2015), https://arxiv.org/abs/1505.04505.
4. S. A. Chin, *Structure of positive decompositions of exponential operators*, Physical Review E 71, 016703 (2005), https://doi.org/10.1103/PhysRevE.71.016703.
