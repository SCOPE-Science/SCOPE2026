# A sharp first-update positivity optimum for error-optimal two-step stiff solvers

## Finding
Consider the error-optimal, second-order, two-step, A-stable \(L(\kappa)\)-family from Jensen, Lóczi and Ketcheson, with \(0\le\kappa<1\). On the scalar decay equation \(y'=-\lambda y\), start with the **exact** positive pair \(y_0=1\), \(y_1=e^{-z}\), where \(z=\lambda h\ge0\). Let \(y_2\) denote the first output of this two-step formula. There is a unique positive zero \(z_1(\kappa)\) of \(y_2(z,\kappa)\), and
\[
 y_2>0\ (0\le z<z_1(\kappa)),\qquad y_2=0\ (z=z_1(\kappa)),\qquad y_2<0\ (z>z_1(\kappa)).
\]
The sharp global first-update positivity frontier over this published coefficient family is
\[
 \max_{0\le\kappa<1} z_1(\kappa)=z_*=1.517214740336255583\ldots,
\]
uniquely attained at \(\kappa_*=0.366871635162403894\ldots\). These constants are specified without numerical fitting: set
\[
 A(z)=4e^{-z}-1,\quad B(z)=2-4ze^{-z},\quad C(z)=3-2z-4e^{-z},\quad D(z)=B(z)^2-4A(z)C(z).
\]
Then \(z_*\) is the unique zero of \(D(z)\) in \((\log4,2)\) and \(\kappa_*=-B(z_*)/[2C(z_*)]\).

A further sharp comparison with classical BDF2, the \(\kappa=0\) endpoint, is
\[
 z_1(\kappa)>\log4\quad\Longleftrightarrow\quad 0<\kappa<\kappa_c,
 \qquad \kappa_c=\frac{2-\log4}{2(\log4-1)}=0.794349724781044915\ldots.
\]
Equality holds also at \(\kappa=\kappa_c\) (and at \(\kappa=0\)); for larger \(\kappa<1\) the first-update positivity ceiling is below BDF2's ceiling. This is specifically a **one-completed-update** theorem, not an assertion of indefinitely positive iterates.

## Assumptions and scope
The scalar initial-value problem has \(\lambda>0\) and a constant step \(h=z/\lambda\), with exactly initialized first two values. The published coefficient family is in the usual convention
\[
 \sum_{j=0}^2 \alpha_j y_{n+j}=h\sum_{j=0}^2 \beta_j f(y_{n+j}),\quad
 (\alpha_0,\alpha_1,\alpha_2)=\left(\frac{3\kappa-1}{\kappa-3},\frac{4(1-\kappa)}{\kappa-3},1\right),
\]
\[
 (\beta_0,\beta_1,\beta_2)=\frac1{3+2\kappa-\kappa^2}(2\kappa^2,4\kappa,2).
\]
Here \(\kappa\in[0,1)\) is the source's asymptotic stiff-damping parameter, not a condition number. No claim is made about nonlinear equations, arbitrary starting data, other two-step formulas, or future outputs \(y_n\) for \(n\ge3\).

## Proof
Substitute \(f(y)=-\lambda y\) into the recurrence and solve for the first completed output. Since \(3+2\kappa-\kappa^2+2z>0\), direct cancellation gives
\[
 y_2(z,\kappa)=\frac{F(z,\kappa)}{3+2\kappa-\kappa^2+2z},\quad
 F(z,\kappa)=4(1-\kappa^2-\kappa z)e^{-z}-(1-2\kappa-3\kappa^2+2\kappa^2z).
\]
Its value at zero is \(F(0,\kappa)=3+2\kappa-\kappa^2>0\). For \(\kappa=0\), \(F(z,0)=4e^{-z}-1\), strictly decreasing to \(-1\). For \(0<\kappa<1\),
\[
 \partial_zF=4e^{-z}\bigl(\kappa z-1-\kappa+\kappa^2\bigr)-2\kappa^2.
\]
The maximum over \(z\ge0\) of the first product \(e^{-z}(\kappa z-1-\kappa+\kappa^2)\) occurs at \(z=2+\kappa^{-1}-\kappa\) and is \(\kappa e^{-2-\kappa^{-1}+\kappa}\). Thus \(\partial_zF<0\) because
\[
 \log(2/\kappa)-2-\kappa^{-1}+\kappa<0\quad(0<\kappa\le1).
\]
Indeed the left side has derivative \((1-\kappa+\kappa^2)/\kappa^2>0\) and its endpoint value at \(\kappa=1\) is \(\log2-2<0\). For positive \(\kappa\), \(F\to-\infty\) as \(z\to\infty\). This proves one and only one positive zero for each \(\kappa\).

Write \(F=A+B\kappa+C\kappa^2\) with the functions in the finding. We have \(B(z)>0\) from \(ze^{-z}\le1/e\), and \(C(z)<0\) because its maximum on \([0,\infty)\), attained at \(z=\log2\), is \(1-2\log2<0\). For \(z>0\),
\[
 B(z)+2C(z)=4\bigl[2-z-(2+z)e^{-z}\bigr]<0,
\]
where the inequality is equivalent to \(2\tanh(z/2)<z\). Therefore the strictly concave quadratic \(F(z,\cdot)\) has its unique maximizer within \((0,1)\) at \(\kappa_z=-B(z)/[2C(z)]\). Its maximum is
\[
 M(z)=A(z)-\frac{B(z)^2}{4C(z)}=-\frac{D(z)}{4C(z)}.
\]
Because \(F(z,\kappa)\) strictly decreases in \(z\) for every \(\kappa\in[0,1]\), the maximum \(M(z)\) strictly decreases. At \(z=\log4\), \(A=0\) and \(B>0\), so \(M>0\). At \(z=2\), substitution \(q=e^{-2}<1/4\) gives \(D(2)=32q(4q-1)<0\), whence \(M(2)<0\) as \(C(2)<0\). Consequently there is exactly one \(z_*\in(\log4,2)\) for which \(M(z_*)=0\), equivalently \(D(z_*)=0\). At this unique ceiling \(F(z_*,\kappa)\le0\) for all \(\kappa\), with equality only at \(\kappa_*=-B(z_*)/[2C(z_*)]\). Strict decrease in \(z\) then proves the unique global maximizer of \(z_1(\kappa)\).

Finally, putting \(z=\log4\) into \(F=A+B\kappa+C\kappa^2\) gives
\[
 F(\log4,\kappa)=\kappa\bigl[(2-\log4)-2(\log4-1)\kappa\bigr].
\]
Its sign and the strict decrease of \(F\) in \(z\) prove the BDF2 crossover exactly.

## Verification
The accompanying `check.py` uses rational coefficient identities, separately evaluates the recurrence, brackets the unique maximum and checks its defining equations, checks the BDF2 crossover and randomly samples both sides of the sign frontier. Run `python check.py` using Python 3.10 or newer; it uses only the standard library. Numerical tests only check the formulas; the inequalities and uniqueness conclusions are proved above.

## Relationship to prior work
Jensen, Lóczi and Ketcheson establish the A-stable, second-order, optimal-error family and its \(L(\kappa)\)-damping law (their Corollary 4.2). Those coefficients and their optimization objective are **not** newly derived here. Hundsdorfer, Ruuth and Spiteri provide the classical positivity/starting-procedure framework for multistep formulas. Published mathematical records already analyze all-iterate positivity for this same family, including a maximal *robust* timestep at \(\kappa=1/2\); these are different statements. The new claim determines instead the full exact-start **first completed output** sign frontier, its unique global optimizing damping parameter, and its crossover against BDF2. All-iterate positivity does not imply the sharp one-output failure boundary or optimal parameter; conversely, first-output positivity does not imply all-iterate positivity.

## Limitations
The quantity being optimized is one first-update sign margin from exact data, not total error, long-run positivity, SSP monotonicity, nonlinear stability, or practical performance. It must not be used as a safe timestep for subsequent outputs. Generic equivalent formulas may exist outside the indexed sources and published records compared; one relevant historical record of all-iterate positivity was available only by summary, not complete text. No independent verification has been performed.

## References
1. T. Jensen, L. Lóczi and D. I. Ketcheson, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, publicly submitted 2026-10-15, Corollary 4.2. https://arxiv.org/abs/2610.22685
2. W. Hundsdorfer, S. J. Ruuth and R. J. Spiteri, *Monotonicity-preserving linear multistep methods*, CWI Report MAS-R0210 (2002), sections 2–3. https://ir.cwi.nl/pub/4231/04231D.pdf
3. *Complete positive-start phase diagram for optimized two-step stiff integrators*, published-finding corpus publication record dated 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-positive-start-phase-diagram-for-optimized-two-step-sti--89235ce0d52d (summary available; full text not inspected).
4. *A sharp positivity phase boundary for error-optimal two-step stiff multistep methods*, published-finding corpus publication record dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-positivity-phase-boundary-for-error-optimal-two-step-sti--d8e0bc3614f5 (summary available; full text not inspected).
