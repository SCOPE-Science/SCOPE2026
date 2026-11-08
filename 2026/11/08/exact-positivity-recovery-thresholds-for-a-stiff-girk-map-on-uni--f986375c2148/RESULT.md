# Exact positivity recovery thresholds for a stiff GIRK map on unit-rate birth chains

## Finding

The two-stage implicit Runge–Kutta coefficient set
\[
A=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad b=(0,1)
\]
has scalar stability function
\[
F(z)=\frac{1-z}{1-2z+2z^2}.
\]
For each integer \(n\in\{2,3,4,5\}\), let \(Q_n\) be the unit-rate pure-birth Markov generator with a single absorbing state. Define the exact one-update matrix \(P_n(h)=F(hQ_n)\) for every \(h\ge0\). Its **complete entrywise-nonnegativity classification** is
\[
\begin{array}{c|c}
n & P_n(h)\ge0\text{ entrywise if and only if}\\ \hline
2,3 & h\ge0\\
4 & h=0\text{ or }h\ge(\sqrt3-1)/2\\
5 & h=0\text{ or }h\ge1/\sqrt2.
\end{array}
\]
All these matrices have row sums one. In particular, on the normalized stiff window \(h\ge1/2\), all chains of at most four states are nonnegative, whereas the five-state chain has a negative transition entry exactly when \(1/2\le h<1/\sqrt2\). At the left endpoint,
\[
[P_5(1/2)]_{1,5}=-\frac7{625},\qquad F(-1/2)=\frac35,\quad F(0)=1.
\]
The appearance and disappearance of the negative entry are exact algebraic boundaries, not sampled numerical thresholds.

## Assumptions and scope

Fix \(n\in\{2,3,4,5\}\). The real \(n\times n\) generator is defined by \((Q_n)_{ii}=-1\) and \((Q_n)_{i,i+1}=1\) for \(1\le i<n\), with \((Q_n)_{nn}=0\) and all other entries zero. Row probability vectors evolve as \(p'(t)=p(t)Q_n\), so \(\exp(hQ_n)\) is stochastic for \(h\ge0\). We apply the constant-coefficient Runge–Kutta stability rational to this *separate linear Markov test system*, not the gas–dust coupling equations in the motivating papers. The independent variable \(h\) is the numerical step multiplied by the unit transition rate; if it denotes the authors' half-source-step parameter, their pure-drag stiff switch corresponds to \(h\ge1/2\). This numerical comparison does not identify the Markov chain with a physical drag–Lorentz operator.

The denominator is invertible on \(hQ_n\): the spectrum of \(Q_n\) consists of \(0\) and \(-1\), while \(1+2h+2h^2>0\). Therefore \(P_n(h)\) exists for every \(h\ge0\). Here entrywise nonnegativity, not a spectral norm bound, is the property tested.

## Proof

**1. RK rational and conservation.** The standard RK identity
\[
F(z)=1+z\,b(I-zA)^{-1}\mathbf1
\]
gives the stated rational function after substituting \(A\) and \(b\). Since \(Q_n\mathbf1=0\) and \(F(0)=1\), the rational functional calculus yields \(P_n(h)\mathbf1=\mathbf1\) for all \(h\ge0\).

**2. Exact matrix entries.** On the first \(n-1\) transient states, \(Q_n=-I+N\), where \(N\) is the nilpotent shift with ones on its first superdiagonal. Analytic matrix-function Taylor expansion terminates, giving, for \(1\le i\le j<n\),
\[
[P_n(h)]_{ij}=\frac{h^{j-i}}{(j-i)!}F^{(j-i)}(-h).
\]
Entries below the diagonal vanish. The final column is determined by the row sum. Writing
\[
B_m(h)=1-\sum_{k=0}^{m-2}\frac{h^k}{k!}F^{(k)}(-h),\qquad 2\le m\le5,
\]
we therefore have \([P_n(h)]_{i,n}=B_{n-i+1}(h)\) for \(1\le i<n\), and \([P_n(h)]_{nn}=1\). In particular the first-row absorbing entry is \(B_n(h)\).

**3. Rational derivative identities.** Set \(D=1+2h+2h^2\), always strictly positive. Direct differentiation gives
\[
\begin{aligned}
F(-h)&=\frac{1+h}{D},\\
F'(-h)&=\frac{1+4h+2h^2}{D^2},\\
F''(-h)&=\frac{4h(3+6h+2h^2)}{D^3},\\
F'''(-h)&=\frac{12(4h^4+16h^3+12h^2-1)}{D^4}.
\end{aligned}
\]
Inserting them in the finite row-tail sums and factoring yields
\[
\begin{aligned}
B_2(h)&=\frac{h(2h+1)}D,\\
B_3(h)&=\frac{4h^3(h+1)}{D^2},\\
B_4(h)&=\frac{2h^3(2h+1)(2h^2+2h-1)}{D^3},\\
B_5(h)&=\frac{4h^4(2h^2-1)(2h^2+4h+1)}{D^4}.
\end{aligned}
\]
These factorizations are exact identities for all real \(h\) for which \(D\ne0\).

**4. Necessity and sufficiency, including boundaries.** The transient entries in dimensions two and three use only \(F(-h)\) and \(F'(-h)\), both nonnegative for \(h\ge0\); their absorbing entries \(B_2,B_3\) are nonnegative too. In dimension four, all transient entries (derivative orders zero, one, two) are nonnegative for every \(h\ge0\). The only possible obstruction is \(B_4\), which is negative for \(0<h<(\sqrt3-1)/2\), zero at that positive boundary and positive thereafter. The other absorbing entries are \(B_2,B_3\), so this is an if-and-only-if.

In dimension five, \(B_5\) is negative for **every** \(0<h<1/\sqrt2\), establishing necessity regardless of any other entry. For \(h\ge1/\sqrt2\), all factors of \(B_2,B_3,B_4,B_5\) are nonnegative. Moreover, the numerator of \(F'''(-h)\) is then positive (already \(4h^4+12h^2-1\ge6\) there), while the derivatives of lower order are positive. Thus **all** transient and absorbing entries are nonnegative. Finally \(P_n(0)=I\), so zero is included as an isolated safe timestep for dimensions four and five. Substitution of \(h=1/2\) in \(B_5\) gives \(-7/625\). This completes the classification.

## Verification

The accompanying `verify.py` uses exact SymPy rational and polynomial arithmetic. It independently recomputes the two-stage RK rational function, all four derivative identities, all four \(B_m\) factorizations, and every entry of \(F(hQ_n)\) for \(2\le n\le5\) using an explicit matrix rational inverse; it confirms row sums, boundary zeros and the five-state witness. Execute `python3 verify.py` with SymPy installed. The independent conceptual proof is the terminating nilpotent Taylor expansion and the explicit sign analysis above; passing the checker alone is not asserted to prove statements for all real timesteps.

## Relationship to prior work

Tedeschi-Prades et al. (2025) introduced the stiff GIRK coefficient set, and Chen et al. (2026, Equation (25) and Appendix A) reused it for charged dust while proving spectral damping on their prescribed stiff modes. They did not assert the unit-rate pure-birth nonnegativity classification given here. Horváth (1998, 2005) gives general RK positivity and absolute-monotonicity criteria; these establish qualitative constraints for broad classes, but their inspected formulas do not state the exact four- and five-state recovery thresholds for this particular rational function. Previously published birth-chain computations for other RK rational functions, including the \([2/2]\) Padé method and SSP-SDIRK2, cannot be substituted: their stability functions and corresponding coefficient signs differ.

## Limitations

The theorem concerns only the specified equal-rate, absorbing pure-birth chains of size two through five and the single rational map \(F\). It does **not** assert positivity for every Markov generator of size four or less, nor for any gas–dust operator, nonconstant coefficient problem or complete operator-splitting method. Stability on eigenmodes does not imply positivity in an arbitrary basis. No claim is made for \(n\ge6\), and first public dates below refer to source preprints, not to this finding. No independent mathematical audit has been performed.

## References

1. G. Tedeschi-Prades, T. Birnstiel, K. Dolag, B. Ercolano and M. Hutchison, *General Implicit Runge-Kutta Integrators for Multifluid Gas-Dust Aerodynamic Drag*, arXiv:2511.07562v1, first public 2025-11-10, https://arxiv.org/html/2511.07562v1, Section II.7 and Appendix B.
2. M. Chen, H. Li, C.-C. He, B. D. Wibking, M. R. Krumholz and X.-N. Bai, *A Nonlinear General Implicit Runge-Kutta Integrator for Multifluid Charged Dust and Gas*, arXiv:2610.18979v1, first public 2026-10-13, https://arxiv.org/abs/2610.18979, Sections 2.4.1 and Appendix A.
3. Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, https://doi.org/10.1016/S0168-9274(98)00050-6.
4. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics 53 (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026.
