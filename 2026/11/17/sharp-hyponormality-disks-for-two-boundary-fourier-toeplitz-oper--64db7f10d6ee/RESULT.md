# Sharp hyponormality disks for two-boundary Fourier Toeplitz operators on a Hardy annulus

## Finding
Fix an annulus \(\mathcal A_R=\{z\in\mathbb C:R<|z|<1\}\) with \(0<R<1\) and a nonzero integer \(k\). For \(A,B\in\mathbb C\), let the bounded boundary symbol be
\[
\phi(e^{i\theta})=Ae^{ik\theta},\qquad
\phi(Re^{i\theta})=Be^{ik\theta}.
\]
Write \(q=R^{|k|}\in(0,1)\), \(d=q+q^{-1}>2\), and \(c=\operatorname{Re}(\overline A B)\). The annular Hardy Toeplitz operator \(T_\phi\) is hyponormal, meaning \(T_\phi^*T_\phi-T_\phi T_\phi^*\succeq0\), exactly under the following conditions:

* For \(k>0\), \(2c\ge d|B|^2\), equivalently \(\big|B-A/d\big|\le |A|/d\).
* For \(k<0\), \(2c\ge d|A|^2\), equivalently \(\big|A-B/d\big|\le |B|/d\).

For every choice of the parameters and either sign of \(k\), the self-commutator \(C_\phi=T_\phi^*T_\phi-T_\phi T_\phi^*\) is in every Schatten class \(S_p\) for \(p>0\), and its exact trace is
\[
\operatorname{tr}(C_\phi)=k\big(|A|^2-|B|^2\big).
\]
In this family, \(T_\phi\) is normal if and only if \(A=B=0\). Every nonzero point of the hyponormality disks gives a nonnormal hyponormal operator, including nonanalytic symbols (where \(B\ne R^k A\)).

## Assumptions and scope
Use the Hardy space \(H^2(\partial\mathcal A_R)\) with angular Lebesgue measure normalized separately to total mass one on **each** boundary circle. The squared norm is
\[
\|h\|^2=\frac1{2\pi}\int_0^{2\pi}|h(e^{i\theta})|^2\,d\theta+
\frac1{2\pi}\int_0^{2\pi}|h(Re^{i\theta})|^2\,d\theta.
\]
The Laurent monomials \(e_n(z)=z^n/(1+R^{2n})^{1/2}\) for \(n\in\mathbb Z\) are an orthonormal basis. The Toeplitz operator is compression \(T_\phi=P_{H^2}M_\phi|_{H^2}\). The symbol has exactly one prescribed angular Fourier mode; the two complex boundary coefficients are independent. No claim is made for sums of modes, matrix symbols, or Bergman spaces. All quantifiers include zero coefficients and every real \(R\in(0,1)\).

## Proof
**1. Weighted bilateral shift.** First take \(k>0\). Directly integrating the two circles gives
\[
T_\phi e_n=w_ne_{n+k},\qquad
w_n=\frac{A+B R^{2n+k}}{\sqrt{(1+R^{2n})(1+R^{2n+2k})}}.
\]
Hence the self-commutator is diagonal in the stated basis:
\[
C_\phi e_n=(|w_n|^2-|w_{n-k}|^2)e_n.
\]
Put \(q=R^k\), \(a=|A|^2\), \(b=|B|^2\), \(c=\operatorname{Re}(\overline A B)\), \(d=q+q^{-1}\), and
\[
D(t)=1+dt+t^2,\qquad f(t)=\frac{a+2ct+bt^2}{D(t)}.
\]
Then \(|w_n|^2=f(R^{2n+k})\), with \(f(0)=a\) and \(\lim_{t\to\infty}f(t)=b\). For each \(n\), set \(s=R^{2(n-k)+k}>0\); thus \(|w_n|^2-|w_{n-k}|^2=f(q^2s)-f(s)\).

**2. Exact sign factorization.** Expanding the two rational functions, collecting powers of \(s\), and cancelling common factors gives
\[
 f(q^2s)-f(s)=
 \frac{(1-q^2)s(1+qs)}{qD(s)D(q^2s)}
 \left[(1+q^2)a-2qc+s\big(2q^2c-q(1+q^2)b\big)\right].\tag{1}
\]
All factors outside the square brackets are strictly positive for \(q\in(0,1)\) and \(s>0\). The admissible geometric sequence \(s=R^{2n-k}\), \(n\in\mathbb Z\), has \(s\to0\) as \(n\to+\infty\), and \(s\to+\infty\) as \(n\to-\infty\). A linear function of \(s\) is nonnegative on that entire sequence if and only if both its constant and linear coefficients are nonnegative. Equation (1) therefore proves hyponormality if and only if
\[
 da\ge 2c,\qquad 2c\ge db.\tag{2}
\]
**3. One inequality is redundant.** By Cauchy–Schwarz, \(c\le\sqrt{ab}\). If \(b>0\) and \(2c\ge db\), then \(db\le2\sqrt{ab}\), so \(b\le4a/d^2\). Consequently \(2c\le2\sqrt{ab}\le4a/d\le da\), since \(d>2\). If \(b=0\), then \(c=0\) and \(da\ge2c\) is automatic. Thus the second inequality in (2) implies the first, giving exactly \(2\operatorname{Re}(\overline A B)\ge d|B|^2\). Completing the square yields \(|B-A/d|\le |A|/d\), with equality and the zero case included.

**4. Negative Fourier modes.** If \(k=-m<0\), the adjoint is \(T_\phi^*=T_{\overline\phi}\), with positive frequency \(m\) and boundary amplitudes \(\overline A,\overline B\). The condition that \(T_\phi\) is hyponormal is that \(T_\phi^*\) is cohyponormal. In the positive-frequency calculation, cohyponormality reverses both inequalities in (2), and the restriction \(2c\le db\) is implied by \(2c\ge da\). Interchanging \(a\) and \(b\) in the Cauchy argument proves the assertion \(2c\ge d|A|^2\) and the corresponding disk.

**5. Schatten regularity and trace.** Since the rational function \(f\) is analytic near \(0\) and has an analytic expansion in \(1/t\) near \(\infty\), the diagonal entries \(f(R^{2n+k})-f(R^{2(n-k)+k})\) decay at least geometrically as \(n\to+\infty\) and as \(n\to-\infty\). Therefore \(\sum_{n\in\mathbb Z}|\langle C_\phi e_n,e_n\rangle|^p<\infty\) for every \(p>0\); in particular the operator is trace class. For \(k>0\), telescope:
\[
\sum_{n=-N}^{N}(|w_n|^2-|w_{n-k}|^2)
=\sum_{n=N-k+1}^{N}|w_n|^2
-\sum_{n=-N-k}^{-N-1}|w_n|^2.
\]
As \(N\to\infty\), the first sum tends to \(ka\), and the second to \(kb\). Thus the trace is \(k(a-b)\). For negative \(k\), use the adjoint relation \([T_\phi^*,T_\phi]=-[T_{\overline\phi}^*,T_{\overline\phi}]\) to obtain the same signed formula \(k(a-b)\).

**6. Normality and sharpness.** If \(C_\phi=0\), both directions of (2) must hold with equality for positive \(k\) (the bracket in (1) vanishes on an unbounded two-sided sequence). Thus \(da=2c=db\), hence \(a=b\). But \(2c\le2a<da\) whenever \(a>0\), a contradiction. Therefore \(A=B=0\). The negative-frequency case reduces by adjoint. Conditions (1) and (2) show necessity by the actual diagonal entries at the two Laurent tails; hence the disk boundary is sharp, not a numerical approximation.

## Verification
The standalone standard-library Python script `check.py` performs 41,815 exact-rational diagnostic identities and inequalities on various annuli, positive frequency indices, complex rational coefficients, and Laurent indices. It checks equation (1) directly against the matrix coefficient formula and the redundant-inequality assertion, exercises the sharp disk boundary and outside points at \(R=1/2\), and tests finite trace telescoping. Running `python check.py` reports `PASSED 41815 exact rational diagnostic identities and inequalities`. These are finite diagnostics only; the proof above establishes all infinite statements.

For illustration, with \(R=1/2\), \(k=1\) and \(A=1\), the disk is \(|B-2/5|\le2/5\). Both \(B=4/5\) and \(B=2/5+2i/5\) lie on its boundary and are nonanalytic, while \(B=9/10\) lies outside it. Here the analytic multiplication symbol \(z\) corresponds to \(B=1/2\), strictly inside the disk.

## Relationship to prior work
Adhikari and Das (2026) formulate algebraic characterizations and zero-product results for annular Hardy Toeplitz operators, with the same two-boundary normalization; they do not state this exact hyponormality region. Jain and Sarkar (2026) establish a Brown–Halmos-type characterization and compact perturbation tests, not a condition on hyponormality for the nonanalytic two-boundary single-mode family. Das and Narayanan (2025) prove zero-product results and give the two-boundary matrix-entry formula that the present calculation specializes. Existing annular Hardy self-commutator results for coordinate or Laurent monomial **multipliers** concern the analytic subfamily with linked boundary coefficients \(B=R^k A\), so they do not determine the entire complex phase disk of independent pairs \((A,B)\). Published Bergman-annulus hyponormality papers concern a different Hilbert space and symbols.

## Limitations
The result concerns a single angular Fourier mode on a Hardy annulus with fixed equal boundary masses, not general symbols, weighted boundary masses, matrix-valued symbols, or Bergman Toeplitz operators. No claim of absolute publication priority is made: a possible equivalent older classification under bilateral-weighted-shift language, or an implication from an uninspected monograph, is an outstanding literature risk. The finite checker does not certify universal inequalities; those follow from the rational identity and tail argument. Independent mathematical assessment has not been performed.

## References
1. S. Adhikari and S. Das, *Algebraic properties of Toeplitz operators on annulus and multiply connected domains*, arXiv:2611.01717, version publicly submitted 2026-11-01; https://arxiv.org/abs/2611.01717 .
2. S. Jain and J. Sarkar, *Characterizations of Toeplitz operators on the annulus*, arXiv:2610.40118 (2026); https://arxiv.org/abs/2610.40118 .
3. S. Das and E. K. Narayanan, *Zero Products of Toeplitz operators on the Hardy and Bergman spaces over an annulus*, New York Journal of Mathematics 31 (2025), 984–1001; https://nyjm.albany.edu/j/2025/31-37v.pdf .
4. J. M. Tattersall, *Toeplitz and Hankel operators on Hardy spaces of complex domains*, University of Leeds PhD thesis (2015); https://etheses.whiterose.ac.uk/id/eprint/11498/ .
5. N. Sadraoui and H. Guediri, *Hyponormality of Toeplitz operators on the Bergman space of an annulus* (2020); a related result in a different Hilbert-space setting.

