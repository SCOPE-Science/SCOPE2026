# Three elliptic traces for the inverse-cube graph's additive energy

## Finding
Let \(q=p^m\), where \(p\ge7\) is prime and \(m\ge1\), and write \(\mathbb F_q\) for the finite field of order \(q\). Consider the graph
\[
H_q=\{(x,x^{-3}):x\in\mathbb F_q^\times\}\subset\mathbb F_q^2.
\]
Its ordered additive energy \(\mathcal E_q\) counts quadruples \((x,y,z,w)\in(\mathbb F_q^\times)^4\) for which \(x+y=z+w\) and \(x^{-3}+y^{-3}=z^{-3}+w^{-3}\).

Define the three nonsingular elliptic curves over \(\mathbb F_p\), each with its usual point at infinity, by
\[
\begin{aligned}
E_0 &: Y^2=(1+X)(1+X+4X^2),\\
E_+ &: Y^2=(X+2)(4X^2+5X+10),\\
E_- &: Y^2=(X-2)(4X^2+5X+10).
\end{aligned}
\]
Write \(a_j(q)=q+1-\#E_j(\mathbb F_q)\), \(\epsilon_q=\chi_q(-3)\) and \(\eta_q=\chi_q(-1)\), where \(\chi_q\) is the quadratic character with \(\chi_q(0)=0\). Then
\[
\boxed{\mathcal E_q=(q-1)\bigl(4q-14-6\epsilon_q-3\eta_q-2\epsilon_q a_0(q)-a_+(q)-a_-(q)\bigr).}
\]
In particular, all extension-field energies are determined by three prime-field point counts: for each \(j\in\{0,+,-\}\), put \(a_j(p^0)=2\) and use
\[
a_j(p^m)=a_j(p)a_j(p^{m-1})-p\,a_j(p^{m-2})\qquad(m\ge2).
\]
For every nontrivial additive character \(\psi\) of \(\mathbb F_q\), the exact constant-coefficient fourth moment is
\[
\sum_{A,B\in\mathbb F_q}\left|\sum_{x\in\mathbb F_q^\times}\psi(Ax+Bx^{-3})\right|^4=q^2\mathcal E_q.
\]

## Assumptions and scope
All counts are ordered; repetitions are allowed in energy quadruples. The characteristic hypothesis excludes \(2,3,5\), where a parametrization requires division by \(3\) or one of the displayed elliptic cubics degenerates. This is an identity for every extension exponent, not a fixed-field numerical observation. The curves are nonsingular because their cubic factors have nonzero discriminant in characteristic at least seven.

## Proof
Write \(s=x+y\). When \(s=0\), every pair is \((x,-x)\), and oddness of the inverse cube gives second-coordinate sum zero, yielding \((q-1)^2\) contributions to the energy. For \(s\ne0\), rescale \((x,y)=(su,s(1-u))\) with \(u\notin\{0,1\}\). Setting \(v=u(1-u)\ne0\) gives
\[
u^{-3}+(1-u)^{-3}=\frac{1-3v}{v^3},\qquad r(v)=\#\{u:u(1-u)=v\}=1+\chi_q(1-4v).
\]
Let \(J\) be the number of pairs \((u,u')\) for which this rational expression agrees. Then \(\mathcal E_q=(q-1)^2+(q-1)J\). The contribution \(v=w\) is
\[
J_{\mathrm{diag}}=\sum_{v\ne0}r(v)^2=2q-5.
\]
Indeed \(\sum_{v\ne0}\chi_q(1-4v)=-1\), and precisely one nonzero \(v\) makes \(1-4v=0\).

For distinct \(v,w\), equality of the rational expressions factors as
\[
(v-w)\bigl(3v^2w-v^2+3vw^2-vw-w^2\bigr)=0.
\]
Put \(t=w/v\). Every off-diagonal solution corresponds uniquely to
\[
v=\frac{t^2+t+1}{3t(t+1)},\qquad w=tv,
\]
with \(t\) outside \(\{0,-1,1\}\) and outside the roots of \(t^2+t+1\). There are \(N_\omega=1+\epsilon_q\) such excluded roots. For allowed \(t\), write \(A=1-4v\) and \(B=1-4w\). Define
\[
F(t)=t(t+1)(t^2+t+4),\qquad G(t)=t(t^2+t+4)(4t^2+t+1).
\]
The quadratic-character relations are
\[
\chi_q(A)=\epsilon_q\chi_q(F(t)),\quad
\chi_q(AB)=\chi_q(G(t)).
\]
The substitution \(t\mapsto t^{-1}\) interchanges \(v\) and \(w\), so the sum of \(\chi_q(B)\) over the allowed set equals that of \(\chi_q(A)\). At \(t=1\) the corresponding character is \(\eta_q\); at each excluded root of \(t^2+t+1\), both individual characters equal one. Also \(\chi_q(G(-1))=\eta_q\) and \(\chi_q(G(1))=1\). Subtracting all excluded values from the complete character sums, and adding the diagonal contribution, gives
\[
J=3q-13-4\epsilon_q-3\eta_q
+2\epsilon_q\sum_{t\in\mathbb F_q}\chi_q(F(t))
+\sum_{t\in\mathbb F_q}\chi_q(G(t)).
\]

The quartic sum is elliptic. The substitution \(z=t^{-1}\) for \(t\ne0\) and the identity
\[
F(t)/t^4=(1+z)(1+z+4z^2)
\]
give
\[
\sum_t\chi_q(F(t))=-1-a_0(q),
\]
where the correction \(-1\) is the omitted \(z=0\) term.

The quintic sum splits into two elliptic sums by a reciprocal symmetry, without requiring a general curve-isogeny theorem. For \(t\ne0\), put \(h=t+t^{-1}\), and define \(R(h)=4h^2+5h+10\). Then \(G(t)=t^3R(h)\). For each \(h\in\mathbb F_q\), the roots of \(t^2-ht+1=0\) satisfy
\[
\sum_{t\ne0:\,t+t^{-1}=h}\chi_q(t)=\chi_q(h+2)+\chi_q(h-2).
\]
If the discriminant is nonsquare both sides vanish; if there are two distinct roots, \(h\pm2=(t\pm1)^2/t\) give the equality; the repeated-root cases \(h=\pm2\) give the same identity directly. Hence
\[
\sum_t\chi_q(G(t))=\sum_h\chi_q((h+2)R(h))
+\sum_h\chi_q((h-2)R(h))=-a_+(q)-a_-(q).
\]
Substitution into the expression for \(J\), followed by \(\mathcal E_q=(q-1)^2+(q-1)J\), proves the displayed energy identity.

Each cubic curve is smooth with one rational point at infinity. The standard elliptic Frobenius characteristic polynomial \(T^2-a_j(p)T+p\) yields the extension trace recurrence. Finally, expand the fourth powers of the exponential sums and sum over \(A,B\). Orthogonality of nontrivial additive characters imposes exactly the two equal-sum equations, producing the factor \(q^2\).

## Verification
Execute \(\texttt{python3 VERIFY.py}\) in a directory containing the accompanying standalone Python file. The verifier constructs prime fields directly and quadratic extensions by an irreducible quadratic, independently enumerates all ordered two-sums, and counts all three cubic-curve points by quadratic characters. It compares the two energy calculations in 23 prime fields of characteristic at least seven through 101, and in the four quadratic extensions with prime bases 7, 11, 13, and 17. It also checks \(a_j(p^2)=a_j(p)^2-2p\) on each cubic. The expected terminal marker is \(\texttt{VERIFY_OK}\).

## Relationship to prior work
The standard inverse graph has an elementary rational fourth moment; the classical two-sum argument appears in Kowalski's February 2010 exposition. Work of Guo, Geng, and Pan (2014) evaluates a fourth moment for character-averaged generalized Kloosterman sums with matched direct/inverse exponents. Neither formula yields this unweighted *mixed-exponent* family or its three fixed elliptic traces. Earlier inverse-square graph energy calculations involve a different rational collision equation and do not imply the inverse-cube formula. Related fourth-moment papers with additional character or Gauss-sum weights have different parameter averages; complete texts for some of these were unavailable and historical priority remains qualified.

## Limitations
No assertion is made for characteristics 2, 3, or 5. The exact formula is expressed through elliptic Frobenius traces, not elementary polynomials in \(q\) alone. The finite-field checks are corroboration, not a proof of the infinitely many extension cases. Historical absence of an equivalent result cannot be certified by search alone. No independent mathematical audit has been performed.

## References
1. E. Kowalski, “The fourth moment of Kloosterman sums,” public exposition, February 26, 2010, https://blogs.ethz.ch/kowalski/2010/02/26/the-fourth-moment-of-kloosterman-sums/ .
2. X. Guo, G. Geng, X. Pan, “On the fourth power mean of the general \(k\)-th Kloosterman sums,” *Advances in Difference Equations* 2014, article 103, doi:10.1186/1687-1847-2014-103 .
3. C. Calderón, M. J. de Velasco, M. J. Zárate, “An explicit formula for the fourth moment of certain exponential sums,” *Acta Mathematica Hungarica* 130 (2011), 203–222, doi:10.1007/s10474-010-0043-5 .
4. H. Chen, J. Chen, G. Cai, X. Ai, “Explicit formulas for the fourth moment of mixed exponential sums,” *Journal of Number Theory* 133 (2013), 1484–1491, doi:10.1016/j.jnt.2012.10.004 .
