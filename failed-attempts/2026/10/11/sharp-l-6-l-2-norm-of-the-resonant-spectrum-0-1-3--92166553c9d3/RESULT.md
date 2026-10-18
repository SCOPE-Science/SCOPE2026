# Sharp \(L^6/L^2\) norm of the resonant spectrum \(\{0,1,3\}\)
## Finding
For
\[
F(t)=a+b e^{2\pi i t}+c e^{6\pi i t},\qquad t\in\mathbb T,
\]
with normalized Haar measure, the sharp inequality
\[
\|F\|_6\le K_{013}\bigl(|a|^2+|b|^2+|c|^2\bigr)^{1/2}
\]
has the following exact algebraic constant. Define
\[
\begin{aligned}
P(r)={}&32r^{10}+36r^9+81r^8+120r^7-148r^6-207r^5\\
&+6r^4+42r^3+44r^2+13r+1,\\
A(r)={}&-8r^7-3r^6+28r^5+25r^4-22r^3-19r^2+6r+1,\\
B(r)={}&-8r^9-3r^8-16r^7-14r^6-3r^5-6r^4+14r^3+6r^2+9r+1.
\end{aligned}
\]
Let \(r_*\) be the unique root of \(P\) in \((91/100,23/25)\), put \(u_*=-B(r_*)/A(r_*)\), and put \(S_*=u_*+1+r_*^2\). Then
\[
K_{013}^6=
\frac{6S_*^3-9S_*(u_*^2+1+r_*^4)+4(u_*^3+1+r_*^6)+6u_*r_*}{S_*^3}.
\]
Numerically,
\[
r_*=0.9137999806544519\ldots,\qquad
u_*=0.9211830216862\ldots,
\]
where the symbol in the second display is \(u_*\), and
\[
K_{013}^6=3.676690884789\ldots,\qquad K_{013}=1.242346821125\ldots .
\]
All nonzero extremizers are exactly those for which
\[
|a|:|b|:|c|=\sqrt{u_*}:1:r_*
\]
and
\[
2\arg a+\arg c-3\arg b\equiv0\pmod{2\pi}.
\]

## Assumptions and scope
The domain is the circle \(\mathbb T=\mathbb R/\mathbb Z\) with normalized Haar measure. The frequency set is exactly \(\{0,1,3\}\). Coefficients are arbitrary complex numbers; the inequality is homogeneous, so the zero triple is trivial and every nonzero triple may be normalized by its \(\ell^2\) norm.

The frequency relation responsible for the new term is
\[
0+0+3=1+1+1.
\]
This is the first resonance of the normalized three-frequency support \(\{0,1,3\}\). The theorem optimizes both coefficient magnitudes and phases; it is not restricted to unimodular coefficients.

## Proof
Write \(x=|a|^2\), \(y=|b|^2\), and \(z=|c|^2\). Parseval applied to \(F^3\) shows that all triple-sum fibers are single multisets except the frequency \(3\), where \((0,0,3)\) collides with \((1,1,1)\). Hence, with \(S=x+y+z\), \(Q=x^2+y^2+z^2\), and \(R=x^3+y^3+z^3\),
\[
\|F\|_6^6
=6S^3-9SQ+4R+6\operatorname{Re}(a^2c\overline{b}^{\,3}).
\]
For fixed magnitudes the last term is at most \(6x\sqrt z\,y^{3/2}\), and equality holds exactly when
\[
2\arg a+\arg c-3\arg b\equiv0\pmod{2\pi}.
\]
Thus every global maximizer can be phase-aligned, and an extremizer with all three magnitudes positive must satisfy this phase condition.

On a boundary face one coefficient vanishes. After normalizing the two surviving squared magnitudes to \(s\) and \(1-s\), the sixth-moment ratio is
\[
-6s^2+6s+1\le\frac52.
\]
At equal positive magnitudes with aligned phase the ratio is \(11/3\), so a global maximizer lies in the interior.

Normalize \(|b|=1\), put
\[
u=\left(\frac{|a|}{|b|}\right)^2,
\qquad
r=\frac{|c|}{|b|},
\qquad
S=u+1+r^2.
\]
The aligned sixth-moment ratio is
\[
\Phi(u,r)=
\frac{6S^3-9S(u^2+1+r^4)+4(u^3+1+r^6)+6ur}{S^3}.
\]
At an interior critical point, clearing the positive denominators in \(\partial_u\Phi=0\) and \(\partial_r\Phi=0\) gives
\[
\begin{aligned}
E_1={}&u^2r^2+u^2+6ur^2+2ur-r^6-3r^4-r^3-3r^2-r-1=0,\\
E_2={}&2u^3r+6u^2r+u^2-2ur^5-12ur^3-5ur^2+6ur+u-2r^5+2r=0.
\end{aligned}
\]
Exact polynomial division in \(u\) gives
\[
(r^2+1)^2E_2=Q(u,r)E_1+A(r)u+B(r)
\]
for an explicit polynomial \(Q\). Moreover,
\[
\left|\operatorname{Res}_r(A,B)\right|=309678550548480000\ne0,
\]
so a common zero of \(E_1,E_2\) has \(A(r)\ne0\) and therefore \(u=-B(r)/A(r)\). Direct substitution gives the exact identity
\[
A(r)^2E_1\!\left(-\frac{B(r)}{A(r)},r\right)
=3r(2r+1)(r^2+1)^3P(r).
\]
Thus every interior critical point has \(P(r)=0\).

An exact Sturm calculation shows that \(P\) has precisely two positive roots: one lies in \((17/20,43/50)\), and one lies in \((91/100,23/25)\). On the first interval both \(A\) and \(B\) are positive and have no zero, so \(-B/A<0\), which is inadmissible because \(u>0\). On the second interval \(A>0\), \(B<0\), and neither has a zero, so \(u=-B/A>0\). Hence there is exactly one interior critical point, namely \((u_*,r_*)\).

The compact normalized coefficient simplex has a global maximizer; it is interior because \(11/3>5/2\); and the interior critical point is unique. Therefore \((u_*,r_*)\) is the unique maximizing magnitude ratio. The phase-alignment condition above gives exactly the stated full extremizer family and the displayed sharp constant.

## Verification
The standalone checker `artifacts/verify.py` uses exact rational and integer arithmetic. It verifies the polynomial-division identity, computes the exact nonzero resultant of \(A\) and \(B\), verifies the substitution factorization, performs a rational Sturm count for all positive roots of \(P\) and for the two isolating intervals, verifies that \(A\) and \(B\) have no zeros on those intervals, and then bisects the admissible root only for the displayed decimals. The finite algebraic computation certifies the elimination and root isolation; the global-maximizer argument is the analytic compactness and boundary argument in the proof.

A replay from the serialized package must end with a line beginning `VERIFY_OK` and reports the isolated root, \(u_*\), \(K_{013}^6\), and \(K_{013}\).

## Relationship to prior work
Michels formulates \(\Lambda(p)\)-sets and their constants for characters on compact abelian groups, providing the archive-era harmonic-analysis setting for the finite \(L^p/L^2\) question, but does not evaluate this resonant three-frequency \(\Lambda(6)\) constant.

Krenedits studies the classical trinomials \(1+e_1\pm e_3\) in the Hardy--Littlewood majorant problem. His result concerns fixed unimodular coefficients at non-even exponents; the full text explicitly recalls that even exponents are governed by Parseval and does not optimize arbitrary coefficient magnitudes at \(p=6\).

A published exact phase-moment analysis of three-frequency spectra determines all even moments for unimodular coefficients and, for \(\{0,1,3\}\), identifies the sixth moment as the first phase-sensitive one. Its stated limitation is that it makes no claim for non-unimodular magnitudes or for the corresponding amplitude optimization. The finding here addresses exactly that remaining optimization: the sharp \(L^6/L^2\) constant, the unique magnitude ratio, and the complete phase condition.

Peskir proves Schur concavity for moments of independent complex Steinhaus sums. That comparison does not dominate the present problem: independence removes the deterministic resonance \(0+0+3=1+1+1\), while the extra resonant term is precisely what shifts the extremal magnitude ratio away from equality.

## Limitations
The theorem concerns only the first resonant normalized three-point spectrum \(\{0,1,3\}\). It does not give a closed formula for arbitrary \(\{0,A,B\}\) when several amplitude variables interact at the first resonant moment, nor for higher even moments where multiple harmonics of the phase invariant can occur.

The exact constant is algebraic but is presented through an isolated root and a rational expression rather than a radical expression. Targeted database and web searches did not locate an implication-equivalent amplitude-optimized theorem, but absence from search is not treated as a proof of global novelty; older trinomial or thin-set literature under different notation remains a residual risk.

## References
1. C. Michels, *Λ(p)-sets and the limit order of operator ideals*, arXiv:math/9904176v1, first public version 1999-04-30; primary MSC classes include 43A46.
2. S. Krenedits, *Three-term idempotent counterexamples in the Hardy-Littlewood majorant problem*, arXiv:1006.0409v1, first public version 2010-06-02.
3. *Even phase moments recover the normalized geometry of a three-frequency spectrum*, public research record `2026/10/4/SCOPE-even-phase-moments-recover-the-normalized-geometry-of-a-three-fr--7849dda51c79`.
4. G. Peskir, *Best constants in Kahane--Khintchine inequalities for complex Steinhaus functions*, Proc. Amer. Math. Soc. 123 (1995), 3101--3111, DOI 10.2307/2160667.
