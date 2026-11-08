# Elliptic three-step convolution and exact diameter exceptions for inverse-graph Cayley walks

## Finding

Let \(F=\mathbb F_q\) have odd prime-power order \(q\), and let \(S=\{(t,t^{-1}):t\in F^\times\}\) inside the additive group \(G=F^2\). For an integer \(j\geq 0\), define \(R_j(a,b)\) as the number of ordered \(j\)-tuples from \(S\) with sum \((a,b)\); in particular \(R_0\) is the point mass at the origin. Write \(\chi:F\to\{-1,0,1\}\) for the quadratic character, with \(\chi(0)=0\).

The following formula determines the entire three-step convolution \(R_3\). If \(a=b=0\),
\[
R_3(0,0)=(q-1)(1+\chi(-3)).
\]
If precisely one coordinate vanishes,
\[
R_3(a,b)=q-3-\chi(-3).
\]
For \(ab\ne0\) put \(c=ab\), and define
\[
P_c(T)=(1-T)(-cT^2+(c-3)T-1)(cT-1).
\]
Then
\[
R_3(a,b)=\begin{cases}
3q-6,&c=1,\\
q-5-\chi(-3),&c=9\ne0,1,\\
q-4+\displaystyle\sum_{t\in F}\chi(P_c(t)),&c\notin\{0,1,9\}.
\end{cases}
\]
The second line is used only when the field element \(9\) is distinct from \(0\) and \(1\); characteristic three and characteristic two are thereby excluded from that case, and characteristic odd is assumed throughout. For \(c\notin\{0,1,9\}\), the smooth projective genus-one curve \(E_c\) defined by \(Y^2=P_c(T)\) has two rational points at infinity, and
\[
R_3(a,b)=\#E_c(F)-6.
\]

The undirected additive Cayley graph \(\operatorname{Cay}(G,S)\) is disconnected for \(q=3\). For \(q\in\{5,7,9\}\) its diameter is exactly \(4\); for **every** odd prime power \(q\ge11\), its diameter is exactly \(3\). The full exceptional support of the three-step measure is explicit: at \(q=5\), its nonzero-coordinate omissions have \(ab\in\{2,3\}\) and the origin is omitted; at \(q=7\), the omissions have \(ab\in\{5,6\}\) and the origin is present; at \(q=9\), they have \(ab\) a root of \(c^2+c+2=0\) over \(\mathbb F_3\) and the origin is present; at \(q=11\), they have \(ab=6\) and the origin is omitted. For all \(q\ge13\) every nonzero target is reached in exactly three steps, while the origin is reached in exactly three steps precisely when \(\chi(-3)\ne-1\). At \(q=3\), the generator set is contained in the proper diagonal subgroup \(\{(u,u):u\in\mathbb F_3\}\).

## Assumptions and scope

All summation, polynomial coefficients, and displayed finite-field equalities are interpreted inside \(F\). The integer \(q\) is any odd prime power, including nonprime orders. The notation \(9\) inside a set of field elements means the image of the integer \(9\) in \(F\), not a distinct symbol. Graph distance uses at most \(j\) increments, unlike the exact-\(j\) convolution support. This distinction is necessary for the \(q=11\) conclusion, since the nonzero-coordinate targets omitted from three steps are reached in two steps. The claims do not concern even characteristic.

## Proof

**The two-step identity.** First,
\[
R_2(0,0)=q-1,\qquad R_2(a,0)=R_2(0,b)=0\quad(a,b\ne0).
\]
Indeed, two nonzero elements with vanishing first coordinate sum must be opposite, making their reciprocal sum vanish too. For \(ab\ne0\), the two first coordinates are the roots of a quadratic with sum \(a\) and product \(a/b\). Its discriminant is \(a^2(1-4/(ab))\), hence
\[
R_2(a,b)=1+\chi(1-4/(ab)).
\]
This holds in odd characteristic, counting repeated roots once.

**Scaling and the generic third step.** The invertible additive map \((u,v)\mapsto(a^{-1}u,av)\) preserves \(S\) and sends \((a,b)\) to \((1,c)\), where \(c=ab\). Fixing the first increment as \((t,t^{-1})\), the remaining two increments sum to \((1-t,c-t^{-1})\). If \(c\ne1\), the three values \(t=0\), \(t=1\), and \(t=1/c\) contribute zero or are forbidden. For all other \(t\), the discriminant in the two-step formula is
\[
D_t=(1-t)^2-\frac{4t(1-t)}{ct-1}
=\frac{(1-t)(-ct^2+(c-3)t-1)}{ct-1}.
\]
Since division and multiplication by a nonzero square have the same quadratic character, \(\chi(D_t)=\chi(P_c(t))\). The excluded polynomial character values satisfy \(\chi(P_c(1))=\chi(P_c(1/c))=0\) and \(\chi(P_c(0))=1\). The \(q-3\) admissible values of \(t\) contribute their constant term \(1\), and summing the characters yields
\[
R_3(1,c)=q-3+\left(\sum_{t\in F}\chi(P_c(t))-1\right).
\]
This proves the third line of the stated formula, including the singular \(c=9\) before specialization.

**The two exceptional products.** For \(c=1\), the residual target at \(t=1\) is \((0,0)\), contributing \(q-1\), and every other nonzero \(t\) contributes \(1+\chi(D_t)\). A direct cancellation gives \(P_1(T)=(T^2-1)^2\), so \(\sum_t\chi(P_1(t))=q-2\). The standard counting, now accounting for the exceptional \(t=1\), gives \(R_3(1,1)=3q-6\). For \(c=9\ne0,1\), the quadratic factor becomes \(-(3T-1)^2\), so
\[
P_9(T)=(T-1)(9T-1)(3T-1)^2.
\]
For the nondegenerate quadratic \((T-1)(9T-1)\), its character sum is \(-1\). Removing the one zero contribution at \(T=1/3\), where the quadratic has character \(\chi(-3)\), gives \(\sum_t\chi(P_9(t))=-1-\chi(-3)\), yielding \(q-5-\chi(-3)\).

**Axes and origin.** When \(a=0\) but \(b\ne0\), scale the inverse-coordinate component to \(b=1\). Writing \(z=-x-y\) for the first coordinates, the reciprocal constraint yields \(x^2+xy+y^2=-bxyz\) after the nonzero-product condition. Equivalently, fix the first summand and apply the two-step discriminant, then scale to a target \((1,0)\). For \(t\notin\{0,1\}\), the two-step character is \(\chi((1+3t)(1-t))\). Its complete sum over \(t\in F\) equals \(-\chi(-3)\): if the characteristic is not three, this is the standard quadratic-character sum for a separable quadratic with discriminant \(16\); in characteristic three the polynomial becomes linear and its character sum is zero. Removing the \(t=0\) contribution \(1\), and noting the \(t=1\) value is zero, gives \(q-3-\chi(-3)\). The case \((0,b)\) follows by interchanging the two coordinates, which preserves the generator set. For the origin, the relation \(x+y+z=0\) forces \(z=-x-y\); the reciprocal relation is equivalent to \(x^2+xy+y^2=0\). For each nonzero \(x\), the ratio \(y/x\) is a root of \(u^2+u+1\), whose root count is \(1+\chi(-3)\), and the three coordinates are nonzero. This gives the origin formula.

**The elliptic point-count and uniform large-field coverage.** For \(c\notin\{0,1,9\}\), the quadratic factor of \(P_c\) has discriminant \((c-1)(c-9)\), and at \(T=1\) and \(T=1/c\) it is, respectively, \(-4\) and \(-4/c\). These are nonzero; thus the quartic has no repeated root. Its leading coefficient is \(c^2\), a square, giving exactly two rational points at infinity. Counting \(1+\chi(P_c(t))\) affine points proves \(\#E_c(F)=q+2+\sum_t\chi(P_c(t))\). Hasse's bound yields
\[
R_3(a,b)\ge q-5-2\sqrt q>0\qquad(q\ge13).
\]
The exceptional \(c=9\) likewise has \(q-5-\chi(-3)>0\) for \(q\ge13\), and \(c=1\) has \(3q-6>0\). For axis targets, \(q-3-\chi(-3)>0\) when \(q\ge5\). The origin lies in \(2S\) for all \(q\ge3\), and every nonzero axis target lies in neither \(S\) nor \(2S\). Therefore every graph with \(q\ge13\) has diameter exactly three; likewise \(q=11\) follows from the separately enumerated cases.

**The finite exceptions.** For \(q=3\), the generators are \((1,1)\) and \((-1,-1)\), hence generate a proper subgroup. For \(q=5,7,9,11\), the exact arithmetic checker `check_hyperbola.py` exhausts all ordered two- and three-step representations, matches them independently to the formulas above, and searches graph distances by iterative sumsets. Its resulting exceptional products and diameter values are those in the Finding section; for \(q=5,7,9\) the missing targets have no representation with at most three generators but do have four-step representations, and for \(q=11\), the missing three-step product \(6\) has a two-step representation. The fields with orders \(q=9\) and \(q=25\) are modeled by explicit irreducible polynomials, not inferred from prime-field tests. These are exhaustive finite verifications for those fields, not an extrapolation to other field orders.

## Verification

Execute `python3 check_hyperbola.py` in the directory containing the provided standalone script, with no third-party packages. The script uses finite-field polynomial arithmetic and independent explicit convolution enumeration; it checks the exact formulas and graph diameters for \(q\in\{3,5,7,9,11,13,17,19,25,27\}\), including extension fields. Its expected terminal marker is `SPLIT_HYPERBOLA_THREE_STEP_CHECKS_PASS`. The infinite family conclusion rests on the displayed algebraic proof and Hasse's theorem, not on these finite tests.

## Relationship to prior work

The finite-field modular hyperbola and its Kloosterman Fourier spectrum are classical subjects, surveyed in Shparlinski's *Modular Hyperbolas* (first made public March 15, 2011). Forey, Fresán, Kowalski, and Wigderson study the same hyperbola generating set through Kloosterman spectral pseudorandomness in *Spectrally indistinguishable pseudorandom graphs* (2025, arXiv:2511.21351); their ordinary Cayley-graph variant is explicitly mentioned. Their inspected spectral results do not state this full pointwise three-step convolution, its elliptic curves, or its complete small-field diameter exceptions. The formal Fourier transform of the third power of their adjacency symbol can recover the convolution in principle, but evaluating its pointwise support is a separate argument. Earlier results on norm-one tori over quadratic field extensions address anisotropic rather than split norm forms and do not give the asserted split-hyperbola cases.

## Limitations

Historical priority has not been established absolutely; an unindexed direct additive decomposition or a stronger general three-sum theorem might imply the same conclusion. The elliptical formulas depend on Hasse's bound for smooth projective genus-one curves. The exact graph-diameter exception table has been independently enumerated only for the finite fields explicitly named; all other odd orders are treated by the proof. No statement about even-characteristic fields or about independent mathematical certification is made.

## References

1. I. E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879 (public version of March 15, 2011), https://arxiv.org/abs/1103.2879.
2. A. Forey, J. Fresán, E. Kowalski, and Y. Wigderson, *Spectrally indistinguishable pseudorandom graphs*, arXiv:2511.21351 (first public November 26, 2025), https://arxiv.org/abs/2511.21351.
3. Hasse's theorem on point counts of smooth genus-one curves over finite fields (classical bound \(\lvert\#E(F)-(q+1)\rvert\le2\sqrt q\)).
