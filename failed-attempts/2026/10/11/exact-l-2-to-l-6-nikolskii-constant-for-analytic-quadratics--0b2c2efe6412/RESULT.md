# Exact \(L^2\)-to-\(L^6\) Nikolskii constant for analytic quadratics
## Finding
For \(P(t)=a+b e^{2\pi i t}+c e^{4\pi i t}\) on \(\mathbb T\) with normalized Haar measure, the sharp constant in \[\|P\|_6\le \mathsf C_6\bigl(|a|^2+|b|^2+|c|^2\bigr)^{1/2}\] is determined by \[\mathsf C_6^6=\frac{35(\sqrt{105}-3)}{48}.\] Writing \(\rho=\frac12\sqrt{\sqrt{105}-5}\), every nonzero extremizer, and only those extremizers, has the form \[(a,b,c)=\lambda\bigl(1,\rho e^{i\beta},e^{2i\beta}\bigr),\qquad \lambda\in\mathbb C\setminus\{0\},\ \beta\in\mathbb R.\]

Equivalently, \(\mathsf C_6^6\) is the unique positive root of
\[
24X^2+105X-1225=0,
\]
and numerically
\[
\mathsf C_6^6=5.284234933512207\ldots,\qquad
\mathsf C_6=1.319766254722393\ldots .
\]
The equal-modulus point has sixth-power ratio \(47/9=5.222\ldots\), so the sharp inequality genuinely requires amplitude redistribution.

## Assumptions and scope
The circle is \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar measure. The coefficient norm is Euclidean. The theorem concerns precisely the three-dimensional analytic polynomial space \(\operatorname{{span}}\{1,z,z^2\}\), equivalently any translated and dilated three-term arithmetic progression of integer frequencies. The result is homogeneous in the coefficients and invariant under a common scalar and modulation. No assertion is made here for degree at least three, for non-arithmetic three-frequency supports, or for exponents other than \(6\).

## Proof
Put \(z=e^{2\pi i t}\). Parseval applied to \(P^3\) gives \(\|P\|_6^6=\|P^3\|_2^2\). The coefficient expansion is
\[
P^3=a^3+3a^2bz+3a(ac+b^2)z^2+b(6ac+b^2)z^3+3c(ac+b^2)z^4+3bc^2z^5+c^3z^6.
\]
Write \(x=|a|\), \(y=|b|\), and \(z_0=|c|\). Replacing each mixed sum by its triangle-inequality maximum gives an upper envelope \(F(x,y,z_0)\). Set
\[
u=x^2+z_0^2,\qquad v=xz_0,\qquad t=y^2.
\]
A direct expansion yields
\[
F=t^3+9t^2u+12t^2v+9tu^2+18tuv+18tv^2+u^3+6uv^2.
\]
For fixed \(u,t\),
\[
\frac{\partial F}{\partial v}=12t^2+18tu+12v(3t+u)\ge0.
\]
Since \(0\le v\le u/2\), the upper envelope is maximized at \(v=u/2\), hence at \(x=z_0\). At the global maximizer all three magnitudes are nonzero, so this step is strict unless \(x=z_0\).

Now put \(r=y/x\). Homogeneity reduces the sharp sixth-power ratio to
\[
h(r)=\frac{r^6+30r^4+90r^2+20}{(r^2+2)^3},\qquad r\ge0.
\]
Its derivative factors as
\[
h'(r)=-\frac{24r(2r^4+5r^2-10)}{(r^2+2)^4}.
\]
The polynomial \(2s^2+5s-10\) has exactly one positive root
\[
s=\frac{\sqrt{105}-5}{4}.
\]
Thus \(h\) increases up to \(r=\rho=\sqrt{s}\) and decreases thereafter. The endpoint values are \(h(0)=5/2\) and \(\lim_{r\to\infty}h(r)=1\), so this critical point is the unique global maximum. Substitution gives
\[
h(\rho)=\frac{35(\sqrt{105}-3)}{48}.
\]

It remains to identify equality. Equality in the triangle steps requires \(ac\) and \(b^2\) to have the same argument. Equality in \(v\le u/2\) requires \(|a|=|c|\), and the scalar optimization requires \(|b|/|a|=\rho\). Because \(|b|^2=\rho^2|a|^2\), the phase condition is equivalent to \(b^2=\rho^2ac\). Taking \(\lambda=a\) and \(e^{i\beta}=b/(\rho a)\) gives \(c=\lambda e^{2i\beta}\), which is exactly the stated extremal family. Conversely that family has equality in every step.

## Verification
The accompanying `artifacts/verify.py` independently expands the cubic convolution, checks the algebraic constant and extremal ratio, and stress-tests both the triangle-envelope bound and the final sharp inequality on deterministic pseudorandom complex coefficients. Its terminal line begins `VERIFY_OK`. These finite numerical checks corroborate the algebraic proof; they are not used to infer the universal inequality.

## Relationship to prior work
Krenedits' three-term Hardy--Littlewood majorant paper, first public as arXiv:1006.0409v1 on 2010-06-02 and classified primarily under 42A05, treats three-term idempotent exponential polynomials and explicitly recalls that even exponents have the majorant property by Parseval. Its coefficients have prescribed equal magnitudes and its problem is a signed-versus-positive comparison; it does not optimize the Euclidean-normalized \(L^6\) norm over arbitrary amplitudes.

Neuwirth's arXiv:math/0703236v1 studies arbitrary trigonometric trinomials in the maximum-modulus/Sidon setting, not the \(L^2\)-to-\(L^6\) norm. His earlier arXiv:math/9707211v1 explains the special arithmetic role of even \(L^p\) norms through polynomial/Parseval structure, but does not state this finite-dimensional sharp constant. Arestov's 1980 work on inequalities of different metrics is part of the natural Nikolskii background; the accessible bibliographic record is general and did not expose the degree-two analytic \(L^2\)-to-\(L^6\) value above.

A directly relevant published published-finding corpus finding, *Even phase moments recover the normalized geometry of a three-frequency spectrum*, gives the all-even-moment phase polynomial for **unimodular** three-frequency coefficients. It explicitly excludes optimization over non-unimodular magnitudes. The present extremizer has \(\rho\ne1\), so that result cannot imply the sharp constant here.

## Limitations
The proof is elementary after the cubic self-convolution is written down, so the originality claim is intentionally narrow: the exact degree-two analytic Nikolskii constant and all extremizers. General Nikolskii inequalities and even-moment Parseval identities are prior work. The full text of Arestov's 1980 article was not available in the inspected lawful sources; an equivalent low-degree special case hidden there or in older approximation-theory literature remains the principal residual originality risk.

## References
1. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy--Littlewood majorant problem*, arXiv:1006.0409v1, first public 2010-06-02, primary MSC 42A05.
2. Stefan Neuwirth, *The maximum modulus of a trigonometric trinomial*, arXiv:math/0703236v1, first public 2007-03-08.
3. Stefan Neuwirth, *Metric unconditionality and Fourier analysis*, arXiv:math/9707211v1, first public 1997-07-28.
4. V. V. Arestov, *Inequality of different metrics for trigonometric polynomials*, Mathematical Notes 27 (1980), 265--269, DOI 10.1007/BF01140526.
