# Exact zero-fibre and parameter-regularity phase diagram for logarithmically weighted punctured disks

## Finding

Let \(\mathbb D^*=\{z\in\mathbb C:0<|z|<1\}\). For every integer \(q\ge1\) and real \(t>-1\), equip \(\mathbb D^*\) with the positive radial weight
\[
 d\mu_{t,q}(z)=|z|^{2t}\bigl(-\log|z|^2\bigr)^{q-1}\,dA(z),
\]
where \(dA\) is ordinary Euclidean area. Let \(K_{t,q}(z,w)\) be the reproducing kernel of the Hilbert space of holomorphic functions square-integrable for this measure. Set \(c=\lceil t\rceil\) and \(\alpha=t+1-c\in(0,1]\). There is a polynomial \(E_{q,\alpha}\) such that, with \(u=z\overline w\),
\[
 K_{t,q}(z,w)=\frac{u^{-c}}{\pi\Gamma(q)}\frac{E_{q,\alpha}(u)}{(1-u)^{q+1}},\qquad
 E_{0,\alpha}(u)=1,
\]
\[
 E_{q+1,\alpha}(u)=u(1-u)E'_{q,\alpha}(u)
 +\bigl(\alpha+(q+1-\alpha)u\bigr)E_{q,\alpha}(u).
\]
Every zero of \(E_{q,\alpha}\) is simple and negative real; for \(0<\alpha<1\) there are exactly \(q\) of them, and for \(\alpha=1\) exactly \(q-1\). The number \(Z_q(t)\) of distinct attainable scalar zero products \(u=z\bar w\) with \(z,w\in\mathbb D^*\) is **exactly**
\[
 Z_q(t)=\begin{cases}
 (q-1)/2+\mathbf1_{\{\alpha<1/2\}},&q\text{ odd},\\
 q/2-\mathbf1_{\{\alpha=1\}},&q\text{ even}.
 \end{cases}
\]
In particular, the kernel is zero-free exactly when either (i) \(q=1\) and \(\alpha\ge1/2\), or (ii) \(q=2\) and \(t\) is an integer. At half-integral \(t\), an odd-order polynomial has a boundary root \(u=-1\), not an attainable zero; for even \(q\), such a boundary root occurs precisely at integral \(t\).

The same family has a **sharp parameter-smoothness defect**. For each fixed \(z,w\in\mathbb D^*\), the map \(t\mapsto K_{t,q}(z,w)\) is real analytic on \((-1,0)\) and on each interval \((k,k+1)\) for integers \(k\ge0\), is \(C^{q-1}\) throughout \((-1,\infty)\), and fails to be \(C^q\) at every integer \(k\ge0\). Its \(q\)-th derivative has the exact right-minus-left jump
\[
 \bigl[\partial_t^q K_{t,q}(z,w)\bigr]_{k^+}
 -\bigl[\partial_t^q K_{t,q}(z,w)\bigr]_{k^-}
 =\frac{q!}{\pi\Gamma(q)}(z\bar w)^{-k-1}.
\]

## Assumptions and scope

The weight parameter satisfies \(t>-1\), the logarithmic exponent \(q-1\) is a nonnegative integer, and functions are holomorphic **on the punctured disk**, so integrable poles at the puncture are allowed. The measure is finite; evaluation is continuous at each nonzero point. All zeros discussed are off-diagonal kernel zeros, equivalently negative real values \(u\in(-1,0)\). An attainable scalar product means \(u=z\bar w\) for two nonzero disk points, which is equivalent to \(0<|u|<1\). The regularity assertion fixes \(z,w\) with \(u\ne0\); it does not claim continuity in a fixed Hilbert-space topology across changes of the admissible Laurent basis.

## Proof

**1. Monomial basis and exact numerator.** For any integer \(n\), polar integration gives
\[
 \|z^n\|_{t,q}^2=\pi\int_0^1 x^{n+t}(-\log x)^{q-1}\,dx
 =\frac{\pi\Gamma(q)}{(n+t+1)^q}
\]
if and only if \(n+t>-1\). If this fails the norm is infinite. Hence the allowable Laurent modes are exactly \(n\ge-c\), with \(c=\lceil t\rceil\). A holomorphic Laurent series is orthogonal mode by mode, and the monomials are complete, so
\[
 K_{t,q}(z,w)=\frac{u^{-c}}{\pi\Gamma(q)}
 \sum_{j\ge0}(j+\alpha)^q u^j,\quad \alpha=t+1-c.
\]
The identity \(\sum_{j\ge0}(j+\alpha)^q u^j=(\alpha+u\partial_u)^q(1-u)^{-1}\) proves the stated polynomial recurrence and rational kernel formula. For \(0<\alpha<1\) the polynomial has degree \(q\), positive constant \(\alpha^q\) and positive leading coefficient \((1-\alpha)^q\). At \(\alpha=1\) its degree is \(q-1\), with positive leading coefficient.

**2. Strict real-rootedness.** Assume \(0<\alpha<1\), and induct on \(q\). The first polynomial is \(\alpha+(1-\alpha)u\). If \(E_{q,\alpha}\) has \(q\) simple negative roots \(r_1<\cdots<r_q<0\), then
\[
 E_{q+1,\alpha}(r_j)=r_j(1-r_j)E'_{q,\alpha}(r_j).
\]
The derivative signs alternate, and the multiplier is negative. Together with the positive value at zero and the alternating sign at negative infinity determined by the positive leading coefficient, this gives one root in each of \((-\infty,r_1),(r_1,r_2),\ldots,(r_q,0)\). They are simple and exhaust the degree. For \(\alpha=1\), start instead from \(E_{1,1}=1\) and \(E_{2,1}=1+u\); the same sign argument then gives \(q-1\) simple negative roots for every \(q\ge2\).

**3. Crossings of the physical unit circle.** Directly from the generating series, or by induction in the displayed recurrence,
\[
 u^q E_{q,\alpha}(1/u)=E_{q,1-\alpha}(u).
\]
Consequently \(E_{q,1/2}\) is reciprocal: its negative simple roots occur in inverse pairs, with precisely one root at \(-1\) when \(q\) is odd. Also \(E_{q,0}(u)=u E_{q,1}(u)\), so \(E_{q,1}\) is a reciprocal polynomial of degree \(q-1\); it has a root \(-1\) precisely when \(q\) is even.

To exclude all other crossings, define the classical Euler polynomials \(\mathscr E_q\) by
\[
 \frac{2e^{\alpha v}}{e^v+1}=
 \sum_{q\ge0}\mathscr E_q(\alpha)\frac{v^q}{q!}.
\]
Abel evaluation of the generating series at \(u=-1\) gives the **exact polynomial identity**
\[
 E_{q,\alpha}(-1)=2^q\mathscr E_q(\alpha).
\]
Their elementary identities \(\mathscr E_q'(\alpha)=q\mathscr E_{q-1}(\alpha)\) and \(\mathscr E_q(1-\alpha)=(-1)^q\mathscr E_q(\alpha)\) show by induction that every even positive-order Euler polynomial has a fixed nonzero sign on \((0,1)\), whereas every odd-order one has its only root in \((0,1)\) at \(\alpha=1/2\). Indeed \(\mathscr E_1(\alpha)=\alpha-1/2\); integrating the alternating sign pattern of the preceding derivative, with even-order endpoint values zero and odd-order antisymmetry, gives the claimed signs and strictness. Hence there can be no other root crossings through \(u=-1\).

At \(\alpha=1/2\), reciprocal pairing gives \(q/2\) roots in \((-1,0)\) for even \(q\), and \((q-1)/2\) for odd \(q\). In the odd case, as \(\alpha\downarrow0\) the polynomial tends to \(uE_{q,1}(u)\); one negative root tends to zero and the other \(q-1\) roots split into reciprocal pairs, giving \((q+1)/2\) interior roots for \(\alpha<1/2\). At \(\alpha=1\) reciprocity of the \(q-1\) roots gives \((q-1)/2\) interior roots for odd \(q\), and \(q/2-1\) for even \(q\) (with the extra root at \(-1\)). This proves the exact counts, including every boundary convention. Since any \(u\in(-1,0)\) is realized by \(z=\sqrt{-u}\) and \(w=-\sqrt{-u}\), the scalar root count equals the actual zero-fibre count.

**4. Exact loss of parameter differentiability.** Fix an integer \(k\ge0\), and restrict \(t\) to a sufficiently small interval around \(k\). The terms \(n\ge-k\) constitute a common Laurent series, polynomial in \(t\) coefficientwise and locally uniformly convergent for each fixed \(0<|u|<1\); it is therefore real analytic in \(t\). For \(t>k\) one additional mode \(n=-k-1\) is allowed, while for \(t\le k\) it is forbidden. Its kernel contribution is exactly
\[
 \frac{\mathbf1_{\{t>k\}}(t-k)^q}{\pi\Gamma(q)}u^{-k-1}.
\]
The one-sided term is \(C^{q-1}\) and has the stated nonzero jump in its \(q\)-th derivative. No other term contributes a derivative jump. The same argument proves real analyticity within each interval between integers.

## Verification

Run \(\texttt{python CHECK.py}\) after installing the two packages in \(\texttt{requirements.txt}\). The checker independently rebuilds the rational numerator through the differential generating operator; verifies reciprocity, Euler-polynomial boundary values, simplicity and real negativity using exact polynomial operations; counts physical zeros by rational Sturm intervals for orders \(1\) through \(10\); tests radial norm integrals with high-precision quadrature; and checks the exact derivative jump symbolically. These are finite reproducibility checks, not substitutes for the all-order proof above.

## Relationship to prior work

Marinescu and Xing (arXiv:2609.24258, first submitted 21 September 2026) establish real-analytic parameter dependence for Euclidean-boundary-distance weights on smooth bounded pseudoconvex domains. The present puncture-power family lies outside those hypotheses and exhibits a precise failure of analyticity caused by the arrival of an integrable Laurent pole. Blaschke (2012) studies logarithmic **boundary** weights and their kernel asymptotics, rather than this exact interior-puncture zero count. Perälä (arXiv:1703.05976, Sections 1 and 3) develops a general radial mechanism for finitely many Bergman zeros but does not give this parameterized rational family or phase diagram. Auvray, Ma and Marinescu (arXiv:1604.06337, Section 3.1) compute the monomial model for a particular complete Poincaré cusp weight on a punctured disk; their results concern asymptotics as a tensor power grows and do not state the present fractional-residue zero counts or parameter differentiability threshold. The root arguments use classical Euler and Euler–Frobenius polynomial identities; those identities themselves are not claimed as new.

## Limitations

The exponent of the logarithmic factor is an integer; noninteger logarithmic powers lead to infinite series rather than the polynomial numerator used here. No stability of zeros under general perturbations of the radial weight is asserted. The novelty comparison is bounded by accessible literature; an equivalent specialized description could exist under Euler–Frobenius or spline terminology. No independent publication-priority or mathematical audit has been performed.

## References

- G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258 (first submitted 2026-09-21).
- A. Perälä, *Vanishing Bergman Kernels on the Disk*, arXiv:1703.05976 (2017), especially Section 3.
- H. Auvray, X. Ma and G. Marinescu, *Bergman kernels on punctured Riemann surfaces*, Math. Ann. 379 (2021), 951–1002; arXiv:1604.06337, especially Section 3.1.
- P. Blaschke, *Asymptotic behavior of Bergman kernels with logarithmic weight*, J. Math. Anal. Appl. 385 (2012), 293–302, doi:10.1016/j.jmaa.2011.06.044.
- W. Schempp, *A contour integral representation of Euler–Frobenius polynomials*, J. Approx. Theory (1981), doi:10.1016/0021-9045(81)90097-6 (historical terminology context; full text not inspected).
