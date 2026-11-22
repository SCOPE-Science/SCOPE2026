# The first nonsynchronous radial minima of weighted Bergman numerator zeros

## Finding

The root trajectories in the open question of Ghiloufi--Snoun (2020) do **not** attain their minimum moduli simultaneously. Already for the quartic numerator family, corresponding to their integer parameter \(\alpha=3\), the distinguished positive real root has a unique minimum at \(a=2-\sqrt3\) with value \(2+\sqrt3\), whereas the modulus of the nonreal conjugate pair has nonzero derivative at that parameter. The positive root and conjugate pair consequently have different minimum parameters. In degrees below four, there cannot be two distinct non-distinguished root moduli, so quartic degree is the first possible and actual failure.

The claim is about roots in the complex plane of the *auxiliary polynomial* defining the weighted Bergman kernel, not about zeros necessarily attainable as products of two points in the unit disk.

## Assumptions and scope

Let \(0<a<1\), set \(\beta=-a\), and define
\[
 G_a(z)=\sum_{j=0}^4\frac{(-1)^j\binom4j}{j-a}z^j,
 \qquad H(a,z)=\prod_{j=0}^4(j-a)\,G_a(z).
\]
This is \(G_{3,\beta}=T_\beta(1-z)^4\) in the notation of the cited paper, with \(T_\beta(\sum c_jz^j)=\sum c_jz^j/(j+\beta)\). All assertions hold for every real \(a\in(0,1)\). The four roots of \(G_a\), equivalently of \(H(a,\cdot)\), are denoted \(u(a)<0\), \(v(a)>0\), and \(w(a),\overline{w(a)}\) with \(\operatorname{Im} w(a)>0\).

The conclusions are:

1. The four roots are simple for every \(a\in(0,1)\) and have the indicated reality types.
2. \(v\) has exactly one stationary point on \((0,1)\). It is its unique global minimum, with \(a_*=2-\sqrt3\) and \(v(a_*)=2+\sqrt3\).
3. \(\left.\frac{d}{da}|w(a)|^2\right|_{a=a_*}\ne0\). The continuous function \(|w(a)|\) has at least one minimum in \((0,1)\), but none at \(a_*\).
4. For the same family with powers \((1-z)^d\), \(d\le3\), at most one modulus among the root branches other than the distinguished negative real root is present; hence simultaneous-minimum failure first becomes possible at \(d=4\), where it occurs.

## Proof

**Reality, simplicity, and endpoint behavior.** Clearing denominators and expanding yields the polynomial
\[
\begin{aligned}
 H(a,z)={}&a^4z^4-4a^4z^3+6a^4z^2-4a^4z+a^4
 -6a^3z^4+28a^3z^3-48a^3z^2+36a^3z-10a^3\\
 &+11a^2z^4-56a^2z^3+114a^2z^2-104a^2z+35a^2\\
 &-6az^4+32az^3-72az^2+96az-50a+24.
\end{aligned}
\]
Its leading coefficient \(a(a-1)(a-2)(a-3)\) is negative, while its constant coefficient \(\prod_{j=1}^4(j-a)\) is positive. Its discriminant is exactly
\[
 \operatorname{disc}_z H=331776a^3(a-4)^3(a-3)^2(a-2)^2(a-1)^2<0.
\]
Thus the real quartic has precisely two distinct real roots of opposite sign and one simple nonreal conjugate pair. At \(a=0\), \(H(0,z)=24\); at \(a=1\), \(H(1,z)=24z\). Polynomial-root continuity (or Rouché's theorem on every fixed compact disk) shows that all four roots escape every bounded set as \(a\downarrow0\), and exactly three escape as \(a\uparrow1\), while one tends to zero. Since the negative real root remains the unique root with negative real part on the negative real axis and since \(H(a,0)>0\), the root tending to zero as \(a\uparrow1\) is \(u\). In particular, both \(v(a)\) and \(|w(a)|\) tend to infinity at both parameter endpoints.

**Unique stationary parameter for the positive root.** Write
\[
\begin{aligned}
 P(a)={}&18a^{10}-360a^9+3114a^8-15264a^7+46647a^6
 -92052a^5+117335a^4\\
 &-93688a^3+43664a^2-10368a+972.
\end{aligned}
\]
Exact resultant elimination gives
\[
\operatorname{Res}_z(H,\partial_a H)
=442368(a^2-4a+1)P(a).
\]
Here \(P(a)>0\) on \([0,1]\): for each of \([l,r]=[0,1/3],[1/3,2/3],[2/3,1]\), substitute \(a=(l+rt)/(1+t)\). In all three cases the degree-ten polynomial
\[
 (1+t)^{10}P\left(\frac{l+rt}{1+t}\right)
\]
has eleven strictly positive rational coefficients; the minima of those eleven coefficients for the three intervals in order are \(163106/6561\), \(163106/6561\), and \(18\). This is an exact finite algebraic positivity certificate, fully reproduced by `CHECK.py`. Because \(H_z\ne0\) at a root, \(v'(a)=-H_a(a,v(a))/H_z(a,v(a))\), so every stationary positive root parameter belongs to the zero set of \(a^2-4a+1\). Its only zero in \((0,1)\) is \(a_*=2-\sqrt3\). Put \(x_*=2+\sqrt3\). Direct substitution gives
\[
 H(a_*,x_*)=H_a(a_*,x_*)=0,
 \quad H_z(a_*,x_*)=-24-16\sqrt3\ne0,
\]
and the exact factorization
\[
 H(a_*,z)=(6-4\sqrt3)(z-x_*)
 \bigl(z^3-\sqrt3z^2+(3+2\sqrt3)z+(2+\sqrt3)\bigr).
\]
The cubic factor is positive for all \(z\ge0\), because
\(z^2-\sqrt3z+3+2\sqrt3>0\) for all real \(z\). Thus \(x_*\) is precisely \(v(a_*)\), and this is its only stationary point. Together with the endpoint divergence, it is its unique global minimum.

**The conjugate modulus is not stationary there.** Vieta's formula yields the exact identity
\[
 u(a)v(a)|w(a)|^2=-\frac{4-a}{a}.
\]
Differentiate logarithmically at \(a=a_*\), using \(v'(a_*)=0\) and \(u'=-H_a/H_z\). This gives
\[
 \left.\frac{d}{da}\log|w(a)|^2\right|_{a_*}
 =\frac{a_*(4-a_*)H_a(a_*,u(a_*))-4u(a_*)H_z(a_*,u(a_*))}
 {a_*(4-a_*)u(a_*)H_z(a_*,u(a_*))}.
\]
Let \(C(z)=z^3-\sqrt3z^2+(3+2\sqrt3)z+2+\sqrt3\) and
\(J(a,z)=a(4-a)H_a(a,z)-4zH_z(a,z)\). The negative root \(u(a_*)\) is a root of \(C\), but direct elimination gives
\[
 \operatorname{Res}_z(C(z),J(a_*,z))=847872+494592\sqrt3\ne0.
\]
Hence the displayed logarithmic derivative is nonzero (numerically about \(-0.34847825\); this decimal is illustrative and not used to certify the sign). Since \(|w(a)|\to\infty\) at both endpoints, it attains an interior global minimum, where its derivative must vanish; its minimizer cannot be \(a_*\). This proves the nonsynchrony.

**Minimal polynomial degree.** For \(d=2\), the corresponding degree-two polynomial has discriminant \(-4a(a-2)>0\), so there is just one non-distinguished positive root. For \(d=3\), the discriminant is \(-216a^2(a-3)^2(a-2)(a-1)<0\) for \(0<a<1\): there is one real negative root and a conjugate pair, whose moduli agree identically. In degree one there are no two non-distinguished root-modulus trajectories. Thus the quartic is the smallest degree for which the nontrivial simultaneous-minimum question can fail.

## Verification

`CHECK.py` uses exact symbolic arithmetic (Python 3.10+ and SymPy 1.12+). Running `python CHECK.py` reconstructs \(H\) from the defining sum; verifies its discriminant and stationary resultant; verifies all thirty-three strictly positive coefficient entries on three rational subintervals; verifies the critical radical identities, cubic factorization, and nonvanishing conjugate-modulus resultant; and checks the two lower-degree discriminants. Its successful replay corroborates the finite elimination steps. The inequalities and root-classification arguments in the proof provide the mathematical passage from exact identities to the claims over the entire parameter interval; the checker alone is not an infinite proof.

## Relationship to prior work

Ghiloufi and Snoun (2020), *Zeros of new Bergman kernels*, introduce the family \(G_{\alpha,\beta}\), establish its root trajectory properties, and explicitly ask whether all non-distinguished root-modulus functions attain their minima at the same parameter. The present calculation gives a **negative answer** to that precise question at the first polynomial degree where it is nontrivial. General parameter-dependent zero counts or boundary-entry results for other radial Bergman weights do not imply the simultaneous-minimum statement or its failure. No claim is made to a complete classification of minima across all degrees or all parameters.

## Limitations

The nonreal pair's minimizing parameter is not explicitly classified or asserted unique; only its existence and separation from \(a_*\) are proved. The theorem concerns the zero set of an auxiliary polynomial in the entire plane, not necessarily kernel zeros with \(|z\overline w|<1\). Priority is based on inspected primary literature and searches, not an exhaustive survey of all possible equivalent resultant or special-function identities. No independent mathematical review has been performed.

## References

- N. Ghiloufi and S. Snoun, *Zeros of new Bergman kernels*, arXiv:2009.04307v1, publicly posted 9 September 2020, https://arxiv.org/abs/2009.04307 . In particular its definition of \(G_{\alpha,\beta}\), discussion of root trajectories and open simultaneous-minimum question.
- N. Ghiloufi and S. Snoun, *Zeros of new Bergman kernels*, Journal of the Korean Mathematical Society, DOI:10.4134/JKMS.j200373, https://doi.org/10.4134/JKMS.j200373 .
