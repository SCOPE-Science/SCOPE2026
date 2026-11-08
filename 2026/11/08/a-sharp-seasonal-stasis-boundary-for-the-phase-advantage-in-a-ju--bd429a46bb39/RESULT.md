# A sharp seasonal-stasis boundary for the phase advantage in a juvenile–adult population

## Finding

In a positive two-stage, two-season population projection, consider the choice between assigning the larger juvenile-to-adult maturation probability to the same season as the larger fertility or to the other season. The remaining juvenile and adult retention probabilities are fixed separately in each season. There is a sharp dichotomy determined entirely by the products of these retention probabilities.

Let \(0<a_i,d_i<1\) for seasons \(i=1,2\), \(0<s<S<1\), \(f>0\), and \(F>f\). The stage vector comprises juveniles and adults, and the season-\(i\) projection at fertility \(u\) and maturation probability \(v\) is
\[
M_i(u,v)=\begin{pmatrix}a_i&u\\v&d_i\end{pmatrix}.
\]
Define the aligned and opposite-phase two-season matrices by
\[
A(F)=M_2(f,s)M_1(F,S),\qquad
B(F)=M_2(f,S)M_1(F,s),
\]
and their positive Perron roots \(r_A(F)=\rho(A(F))\), \(r_B(F)=\rho(B(F))\). The asymptotic per-season abundance multipliers are the positive square roots of these two-season roots.

**Sharp phase law.** Put \(R_1=a_1d_1\) and \(R_2=a_2d_2\). If \(R_2\le R_1\), then \(r_B(F)>r_A(F)\) for *every* \(F>f\). If \(R_2>R_1\), there exists exactly one \(F_*\in(f,\infty)\) such that
\[
\begin{cases}
r_A(F)>r_B(F),&f<F<F_*,\\
r_A(F)=r_B(F),&F=F_*,\\
r_A(F)<r_B(F),&F>F_*.
\end{cases}
\]
In both cases the maturation contrast \(S-s\) is strictly positive; no infinitesimal or weak-seasonality approximation is used.

The crossover is characterized without a multi-parameter optimization. Define
\[
K(F)=\frac{R_2F-R_1f}{F-f}.
\]
For every \(F>f\),
\[
\operatorname{sign}\bigl(r_B(F)-r_A(F)\bigr)
=\operatorname{sign}\bigl(r_A(F)-K(F)\bigr).
\]
When \(R_2>R_1\), the unique crossing solves \(r_A(F_*)=K(F_*)\). This is an exact scalar characterization of the unique switch.

**Exact biologically feasible persistence-boundary witness.** Take
\[
(a_1,d_1)=\left(\frac15,\frac3{20}\right),\quad
(a_2,d_2)=\left(\frac25,\frac34\right),\quad
(f,F)=\left(\frac32,\frac{63}{40}\right),\quad
(s,S)=\left(\frac3{20},\frac25\right).
\]
Here \(a_i+S<1\) for both seasons, so staying juvenile and maturing can be modeled as mutually exclusive individual fates under either schedule. The two-season matrices are
\[
A=\begin{pmatrix}17/25&171/200\\33/100&279/800\end{pmatrix},\qquad
B=\begin{pmatrix}61/200&171/200\\77/400&297/400\end{pmatrix}.
\]
The exact characteristic values at one are
\[
\det(I-A)=-\frac{59}{800}<0,
\qquad
\det(I-B)=\frac{23}{1600}>0.
\]
All four diagonal entries of \(A,B\) are below one. Therefore \(r_A>1>r_B\). With identical within-season retention probabilities and the same fertility and maturation marginals, changing which season has higher maturation changes a linearly growing population into a declining one. This is a deterministic low-density projection statement, not an assertion about almost-sure survival of an individual-based stochastic process.

## Assumptions and scope

The stage equations are \((J_{t+1},A_{t+1})^\top=M_i(u,v)(J_t,A_t)^\top\), with the displayed two-season schedule repeating indefinitely. Fecundities count expected juvenile production per adult and may exceed one; juvenile maturation and juvenile/adult retention are positive probabilities strictly below one. The matrix is a nonnegative linear expected-abundance model, not a Markov transition matrix. For a biological model in which each juvenile must either remain juvenile or mature, impose additionally \(a_i+v_i\le1\) in the applicable season. The exact witness satisfies the stronger inequalities \(a_i+S<1\) for both seasons, so both compared schedules respect the exclusive juvenile fate constraint. The general theorem is algebraic even for positive demographic entries outside this more restrictive subdomain.

The year-two matrix products are ordered chronologically, with season 1 acting first. Because the matrices are strictly positive, each product has a simple positive Perron root. The comparison concerns asymptotic population growth and the linear extinction threshold at spectral radius one, not transient population counts or density-dependent coexistence.

## Proof

Write \(\Delta_F=F-f>0\), \(\Delta_S=S-s>0\). Direct multiplication gives
\[
A=\begin{pmatrix}
a_1a_2+fS & a_2F+fd_1\\
sa_1+d_2S & sF+d_1d_2
\end{pmatrix},\qquad
B=\begin{pmatrix}
a_1a_2+fs & a_2F+fd_1\\
Sa_1+d_2s & SF+d_1d_2
\end{pmatrix}.
\]
In particular,
\[
\operatorname{tr}(B)-\operatorname{tr}(A)=\Delta_F\Delta_S,
\]
and factorizing the two seasonal determinants gives
\[
\det(B)-\det(A)=\Delta_S(R_2F-R_1f).
\]
Thus for the monic characteristic polynomials \(\chi_A(z)=\det(zI-A)\) and \(\chi_B(z)=\det(zI-B)\),
\[
\chi_B(z)-\chi_A(z)=\Delta_F\Delta_S\bigl(K(F)-z\bigr).
\tag{1}
\]

Every entry of \(A,B\) is positive. Their two real eigenvalues are \(r_A,\ell_A\) and \(r_B,\ell_B\), with the Perron root strictly larger than each diagonal entry and the smaller eigenvalue strictly smaller than each diagonal entry. In particular
\[
\ell_B<B_{11}=a_1a_2+fs<A_{11}=a_1a_2+fS<r_A.
\]
Evaluate (1) at \(z=r_A\). Because \(\chi_A(r_A)=0\),
\[
(r_A-r_B)(r_A-\ell_B)
=\Delta_F\Delta_S\bigl(K(F)-r_A\bigr).
\]
The factor \(r_A-\ell_B\) is positive. It follows exactly that \(r_B>r_A\) if and only if \(r_A>K(F)\), and likewise for equality and the reversed inequality. This proves the stated sign criterion without relying on the sign of an isolated determinant for spectral ordering.

If \(R_2\le R_1\), then
\[
K(F)=R_2+\frac{(R_2-R_1)f}{F-f}\le R_2.
\]
On the other hand, positivity and the arithmetic–geometric mean bound show
\[
r_A>\max\{a_1a_2,d_1d_2\}\ge
\sqrt{(a_1d_1)(a_2d_2)}=\sqrt{R_1R_2}\ge R_2.
\]
Consequently \(r_A>K(F)\) and \(r_B>r_A\) for all \(F>f\).

If \(R_2>R_1\), the function \(K(F)=R_2+(R_2-R_1)f/(F-f)\) decreases continuously and strictly from \(+\infty\) as \(F\downarrow f\) to \(R_2\) as \(F\to\infty\). Meanwhile, \(A(F)\) is a positive matrix with entries \(A_{12}=a_2F+fd_1\) and \(A_{22}=sF+d_1d_2\) strictly increasing in \(F\), with the other entries fixed. Strict Perron monotonicity gives continuous, strictly increasing \(r_A(F)\), finite as \(F\downarrow f\). Moreover, \(r_A(F)>A_{22}\to\infty\) as \(F\to\infty\). Exactly one intersection \(r_A(F)=K(F)\) therefore exists, and the sign criterion gives the two strict inequalities on either side.

For the exact witness, multiply the stated rational matrices. The smaller eigenvalue of each positive two-by-two matrix lies below the smaller diagonal entry, hence below one. The displayed signs of \(\det(I-A)=(1-r_A)(1-\ell_A)\) and \(\det(I-B)=(1-r_B)(1-\ell_B)\) establish \(r_A>1>r_B\). This completes the proof.

## Verification

The standalone `verify_phase.py` uses rational arithmetic to check the trace, determinant, and characteristic-polynomial identities on 4,000 reproducibly selected parameter profiles. It separately checks the exact witness matrices, \(\det(I-A)\) and \(\det(I-B)\), and verifies with high-precision arithmetic that the opposite-phase arrangement eventually overtakes the aligned arrangement when fertility contrast increases. The general result is proved by the preceding algebra and Perron monotonicity, not by finite tests. Run `python verify_phase.py` from the directory containing this document and the script.

## Relationship to prior work

Cushing (2006) establishes a phase relationship for periodic juvenile–adult models with fertility, maturation and adult-survival variation, but its explicit projection has zero juvenile retention on the diagonal. In that setting \(R_1=R_2=0\) and the opposite-phase ordering of this theorem cannot reverse. The present theorem isolates the sharp new mechanism when positive juvenile retention and season-specific adult retention coexist: the retention products \(R_1\) and \(R_2\) determine whether and when the phase preference changes. The comparison is not a restatement of the original anti-phase preference.

Ackleh and Chiquet (2009) allow partial juvenile retention and compare seasonal versus continuous reproduction, but the investigated periodic breeding schedule is not the two competing, fixed-margin maturation placements here. Cushing and Ackleh (2011) develop general periodic matrix reproductive-number methods, rather than the present exact two-arrangement ordering and unique switching law. These papers give the matrix-model framework and important precursors; priority over every possible equivalent statement in broader matrix rearrangement literature is not established.

## Limitations

The result is limited to two stages and period two, a deterministic linear low-density projection, strictly positive rates, fixed season-specific diagonal retention entries, and exactly the two displayed maturation schedules. It is not a claim for arbitrary periods or arbitrary life-cycle matrices. Each juvenile's mutually exclusive staying and maturation events may require additional biological constraints, depending on how the rates are parameterized. Although the algebraic phase-order theorem holds for all parameter choices listed under Assumptions and scope, the exact persistence-boundary witness is a biologically admissible linear mean projection, not a calibrated individual-level stochastic demographic model. No empirical effect sizes or nonlinear long-term abundance predictions are asserted. Historical priority has not been independently audited.

## References

- J. M. Cushing, *A juvenile-adult model with periodic vital rates*, Journal of Mathematical Biology 53 (2006), 520–539. First public online date 2006-04-24. https://doi.org/10.1007/s00285-006-0382-6 ; lawful author copy https://math.arizona.edu/~cushing/AJuvenileAdultModelWithPeriodicVitalRates%20JMB06.pdf
- A. S. Ackleh and R. A. Chiquet, *The global dynamics of a discrete juvenile–adult model with continuous and seasonal reproduction*, Journal of Biological Dynamics 3 (2009), 101–115. https://doi.org/10.1080/17513750802379010
- J. M. Cushing and A. S. Ackleh, *A net reproductive number for periodic matrix models*, Journal of Biological Dynamics 6 (2012), 166–188; first online 2011-02-18. https://doi.org/10.1080/17513758.2010.544410
