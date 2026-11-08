# Sharp quasi-Schatten phase transition for Fock Volterra self-commutators

## Finding

On the standard one-variable Gaussian Fock Hilbert space, let
\[
(V_gf)(z)=\int_0^z f(w)g'(w)\,dw,\qquad g(z)=az^2+bz+c,
\]
with arbitrary complex coefficients \(a,b,c\), and let \(C_g=V_g^*V_g-V_gV_g^*\). Every such \(C_g\) is trace class, with the **exact trace invariant**
\[
\operatorname{Tr}(C_g)=8|a|^2.
\]
If \(a=b=0\), then \(C_g=0\). For a nonzero self-commutator its decreasing singular values satisfy the sharp two-sided estimates
\[
s_j(C_g)\asymp
\begin{cases}
j^{-2},&ab=0,\quad (a,b)\ne(0,0),\\
j^{-3/2},&ab\ne0,
\end{cases}\qquad j\to\infty.
\]
Consequently, for **every real \(p>0\)**, including the quasi-Banach range,
\[
C_g\in\mathcal S_p\quad\Longleftrightarrow\quad
\begin{cases}
\text{always},&a=b=0,\\
p>1/2,&ab=0,\ (a,b)\ne(0,0),\\
p>2/3,&ab\ne0.
\end{cases}
\]
At the relevant critical exponent \(p_*=1/2\) or \(2/3\), the nonzero operator belongs to the weak ideal \(\mathcal S_{p_*,\infty}\), but not \(\mathcal S_{p_*}\); no smaller weak exponent is possible.

There is also a complete qualitative sign classification: when \(a\ne0,b=0\), \(C_g\) is strictly positive and has infinitely many positive eigenvalues; when \(a=0,b\ne0\), it has exactly one positive eigenvalue and infinitely many negative eigenvalues; when \(ab\ne0\), it has infinitely many eigenvalues of **each** sign. In particular, adding a nonzero linear term to a nonzero quadratic symbol worsens the commutator's sharp singular-value decay exponent from \(2\) to \(3/2\), without changing its trace.

## Assumptions and scope

The normalized Fock space is
\[
\mathcal F^2=\left\{f\text{ entire}:\ \|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\},
\]
with orthonormal monomials \(e_n(z)=z^n/\sqrt{n!}\), for integers \(n\ge0\). The integral from \(0\) to \(z\) is path independent. The class \(\mathcal S_p\) is defined by summability of the \(p\)-th powers of singular values even when \(0<p<1\). The weak class \(\mathcal S_{p,\infty}\) means \(s_j=O(j^{-1/p})\). The symbol constant \(c\) does not affect \(V_g\). There are no restrictions on the phases or magnitudes of \(a\) and \(b\).

## Proof

**1. Exact band coefficients.** Direct integration against the Fock monomials yields
\[
V_ge_n=\alpha_ne_{n+2}+\beta_ne_{n+1},\qquad
\alpha_n=2a\sqrt{\frac{n+1}{n+2}},\quad
\beta_n=\frac{b}{\sqrt{n+1}}.
\]
This bounded two-diagonal formula is also given in Mengestie's 2026 work. Set \(t_{-1}=0\). The self-adjoint self-commutator has the tridiagonal expansion
\[
C_ge_n=\overline{t_{n-1}}e_{n-1}+d_ne_n+t_ne_{n+1},
\]
where the missing negative-index term is suppressed and
\[
\begin{aligned}
d_0&=2|a|^2+|b|^2,\\
d_n&=\frac{8|a|^2}{n(n+2)}-\frac{|b|^2}{n(n+1)}\quad(n\ge1),\\
t_0&=a\overline b,\\
t_n&=-\frac{2a\overline b}{(n+2)\sqrt{n+1}}\quad(n\ge1).
\end{aligned}
\]
For example, the forward coefficient of \(V_g^*V_g\) is \(\alpha_n\overline{\beta_{n+1}}=2a\overline b\sqrt{n+1}/(n+2)\); that of \(V_gV_g^*\), for \(n\ge1\), is \(\alpha_{n-1}\overline{\beta_{n-1}}=2a\overline b/\sqrt{n+1}\). Their difference is the claimed \(t_n\); at \(n=0\) the latter coefficient vanishes. The diagonal follows similarly from the two squared weights and their backward shifts. These formulas include the boundary indices \(n=0,1\).

**2. Trace-class membership and trace.** Write \(C_g=D+U+U^*\), where \(De_n=d_ne_n\) and \(Ue_n=t_ne_{n+1}\). For \(n\ge1\), \(|d_n|=O(n^{-2})\) and \(|t_n|=O(n^{-3/2})\). Both coefficient sequences are absolutely summable; hence \(D\), \(U\), and \(U^*\) are trace class. Since \(U\) is strictly upper triangular its trace is zero. For every integer \(N\ge1\), telescoping the differences of squared weights gives the **exact finite identity**
\[
\sum_{n=0}^{N}d_n
=4|a|^2\frac{N+1}{N+2}
+4|a|^2\frac{N}{N+1}
+\frac{|b|^2}{N+1}.
\]
Letting \(N\to\infty\) proves \(\operatorname{Tr}(C_g)=8|a|^2\).

**3. Singular-value upper bounds.** A diagonal operator has singular values equal to the decreasing rearrangement of its absolute diagonal coefficients; a unilateral weighted shift has singular values equal to the decreasing rearrangement of the moduli of its weights. Thus \(s_j(D)=O(j^{-2})\) and \(s_j(U)=s_j(U^*)=O(j^{-3/2})\). The three-term singular-value inequality
\[
s_{3j-2}(D+U+U^*)\le s_j(D)+s_j(U)+s_j(U^*)
\]
shows \(s_j(C_g)=O(j^{-3/2})\). If \(ab=0\) then \(U=0\), so the sharper \(O(j^{-2})\) holds.

**4. Matching singular-value lower bounds.** If \(ab\ne0\), let \(Q\) project onto the closed span of \(e_{3k}\), for integers \(k\ge1\), and \(P\) project onto the closed span of \(e_{3k+1}\) for the same indices. Because \(C_g\) has bandwidth one,
\[
PC_gQe_{3k}=t_{3k}e_{3k+1}.
\]
These are pairwise independent diagonal transfer coefficients. Their moduli decrease in \(k\) and satisfy
\[
|t_{3k}|=\frac{2|ab|}{(3k+2)\sqrt{3k+1}}\asymp k^{-3/2}.
\]
Consequently \(s_j(PC_gQ)\asymp j^{-3/2}\). Singular values are contractive under compression, so \(s_j(C_g)\ge s_j(PC_gQ)\), proving the matching lower bound. If \(ab=0\) and the operator is nonzero, it is diagonal, and its tail coefficients satisfy \(|d_n|\sim8|a|^2n^{-2}\) if \(b=0\), or \(|d_n|\sim |b|^2n^{-2}\) if \(a=0\). This proves the other two-sided estimate. The ideal and critical weak-ideal conclusions follow by the elementary summability criterion for \(j^{-\gamma p}\).

**5. Positive/negative spectral multiplicities.** For \(a\ne0,b=0\), all \(d_n>0\). For \(a=0,b\ne0\), the exceptional coefficient \(d_0=|b|^2\) is positive whereas every \(d_n\) with \(n\ge1\) is negative. When \(ab\ne0\), take large disjoint adjacent pairs \(\{e_{4k},e_{4k+1}\}\). The two normalized vectors on each pair having their relative phases aligned or opposed to \(t_{4k}\) have quadratic-form values
\[
\frac{d_{4k}+d_{4k+1}}2\pm|t_{4k}|.
\]
The diagonal average is \(O(k^{-2})\), while \(|t_{4k}|\asymp k^{-3/2}\); hence these values are respectively positive and negative for all sufficiently large \(k\). Distinct pairs are separated by at least two unused indices, and the bandwidth-one form has no cross terms between them. Thus each sign has an infinite-dimensional definite subspace. Compact self-adjoint spectral theory gives infinitely many eigenvalues of both signs. This concludes the proof.

## Verification

A standalone standard-library Python program, `checker.py`, independently constructs finite sections of \(V_g^*V_g-V_gV_g^*\) from the two nonzero monomial coefficients. It compares its diagonal and first off-diagonal entries against the displayed formulas, including \(n=0\); also tests the finite trace identity in exact rational arithmetic and checks squared off-diagonal magnitudes. The program returned `EXACT_FOCK_VOLTERRA_COMMUTATOR_OK 21010` (21,010 finite assertions) when run from the completed artifact. The infinite spectral estimates, ideal nonmembership, trace limit, and inertia rely on the analytical arguments above, not on this finite computation.

## Relationship to prior work

Mengestie, *Normality properties of Volterra-type integral operators on the Fock space* (first public October 21, 2026), classifies several normality properties and proves that **every** bounded \(V_g\) is essentially normal, i.e. that its self-commutator is compact (Proposition 2.6). The paper supplies the monomial action and a diagonal calculation for the pure quadratic shift. It does not state a trace formula, the mixed-coefficient off-diagonal cancellation, a Schatten or weak-Schatten classification of the self-commutator, or the two-sided singular-value and inertia classifications. These are the present claims, not the previously known compactness statement.

Mengestie's 2017 paper addresses Schatten membership of the **Volterra operator itself**, rather than of its self-commutator. The related October 23, 2026 article on Berezin range and norm concerns a different invariant. Standard weighted-shift and singular-value inequalities are used as established tools, not proposed as new lemmas.

## Limitations

The claim is for classical one-variable Gaussian Fock space and polynomial symbols of degree at most two, exactly the bounded-symbol regime. It does not classify analogous commutators on Fock--Sobolev or multivariable spaces; it gives a two-sided singular-value **order**, not an exact asymptotic leading constant in the mixed regime; it does not determine individual nonzero eigenvalues or the possible kernel dimension. Priority remains a best-knowledge assessment rather than an independently certified literature classification. The finite checker cannot establish infinite-dimensional statements. No independent mathematical audit has been performed.

## References

1. T. Mengestie, *Normality properties of Volterra-type integral operators on the Fock space*, Advances in Operator Theory **12**, article 1 (2027), published online October 21, 2026, DOI: https://doi.org/10.1007/s43036-026-00541-6 (especially equations (2.1)--(2.3) and Proposition 2.6).
2. T. Mengestie, *Spectral properties of Volterra-type integral operators on Fock--Sobolev spaces*, 2017, https://arxiv.org/abs/1702.08157 (the Schatten class of \(V_g\) itself).
3. T. Mengestie, *Berezin range and norm of Volterra-type integral operators on the Fock space*, Canadian Mathematical Bulletin, published online October 23, 2026, https://doi.org/10.4153/S0008439526102616 (abstract and bibliographic metadata inspected).
