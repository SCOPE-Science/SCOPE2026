# Arithmetic descent of the two genus-two factors of the Accola–Maclachlan curve at eleven

## Finding

For the smooth genus-four hyperelliptic curve over \(\mathbb F_{11}\)
\[
C:\quad y^2=x^{10}-1,
\]
the two canonically distinguished genus-two quotient Jacobians are **not isogenous over \(\mathbb F_{11}\)**, although they become isomorphic as principally polarized abelian surfaces over the quadratic extension \(\mathbb F_{121}\). Their exact Frobenius numerators are
\[
P_+(T)=1+4T+6T^2+44T^3+121T^4,
\qquad P_-(T)=P_+(-T).
\]
Both quartics are irreducible over \(\mathbb Q\). Therefore
\[
\begin{aligned}
L_C(T)&=P_+(T)P_-(T)\\
&=1-4T^2-74T^4-484T^6+14641T^8,
\end{aligned}
\]
and \(\#\operatorname{Jac}(C)(\mathbb F_{11})=14080=176\cdot80\). The genus-four Jacobian is ordinary, isogenous over \(\mathbb F_{11}\) to a product of **two nonisogenous simple ordinary abelian surfaces**, and becomes isogenous to a square of a genus-two Jacobian over \(\mathbb F_{121}\). This is an arithmetic descent distinction from the geometric decomposition of the same curve.

## Assumptions and scope

The base is \(k=\mathbb F_{11}\), and \(K=\mathbb F_{121}=k(i)\) with \(i^2=-1\). Throughout, \(L_X(T)=\det(1-T\operatorname{Frob}\mid H^1_{\mathrm{\acute et}}(X_{\overline{k}},\mathbb Q_\ell))\), for any \(\ell\ne11\), and the point-count convention is \(\#X(\mathbb F_{11^n})=11^n+1-\sum_j\alpha_j^n\). We claim an isogeny of unpolarized Jacobians, not an isomorphism of the genus-four Jacobian to a polarized product. Simplicity refers to the base field \(\mathbb F_{11}\), not absolute simplicity.

The two smooth quotient curves are
\[
Y_+:\quad v^2=u^5-1,\qquad
Y_-:\quad w^2=u(u^5-1).
\]
Their genera are both two, and the genus of \(C\) is four because all defining branch polynomials are squarefree in characteristic eleven.

## Proof

**1. Distinct quotient summands.** The commuting involutions \(\sigma(x,y)=(-x,y)\) and \(\tau(x,y)=(-x,-y)\) on \(C\) yield the quotient maps
\[
\pi_+(x,y)=(x^2,y),\qquad \pi_-(x,y)=(x^2,xy).
\]
The pullbacks of bases \(\{du/v,u\,du/v\}\) and \(\{du/w,u\,du/w\}\) for regular differentials on the respective genus-two curves are
\[
\{2x\,dx/y,2x^3\,dx/y\},\qquad
\{2\,dx/y,2x^2\,dx/y\}.
\]
Together they form a basis of \(H^0(C,\Omega_C^1)\). Thus the dual map on differential spaces for the Jacobian norm homomorphism \(\pi_{+*}\times\pi_{-*}:J(C)\to J(Y_+)\times J(Y_-)\) is an isomorphism. Both sides have dimension four, so the norm homomorphism is a separable isogeny over \(k\); its dual is the sum of the two pullback homomorphisms and is also an isogeny. Therefore \(L_C=L_{Y_+}L_{Y_-}\).

**2. Exact twisting and first descent field.** In \(k(Y_-)\), set \(t=1/u\), \(z=w/u^3\). The equation becomes \(z^2=1-t^5=-(t^5-1)\). Hence \(Y_-\) is the quadratic twist of \(Y_+\) by \(-1\); the smooth completions are isomorphic over \(K\) since \(i^2=-1\). Over \(k\), \(-1\) is nonsquare. On the Tate module of the twist, Frobenius is multiplied by \(-1\), so \(L_{Y_-}(T)=L_{Y_+}(-T)\).

**3. Exhaustive finite-field counts and the genus-two functional equation.** Direct enumeration of all points on \(v^2=u^5-1\), including its one rational point at infinity, gives
\[
\#Y_+(\mathbb F_{11})=16,\qquad
\#Y_+(\mathbb F_{121})=118.
\]
For the second field use the explicit representation \(\mathbb F_{121}=\mathbb F_{11}[i]/(i^2+1)\); its \(121\) elements are all enumerated by the attached exact verifier, with neither statistical sampling nor unverified external dependencies. The Frobenius power sums are \(s_1=12-16=-4\), \(s_2=122-118=4\). Newton's identity yields \(a_2=(s_1^2-s_2)/2=6\), and the genus-two functional equation then yields
\[
L_{Y_+}(T)=1-s_1T+a_2T^2-11s_1T^3+11^2T^4=P_+(T).
\]
Twisting yields \(P_-(T)\) and multiplication gives the displayed genus-four numerator and Jacobian order. Independently, direct enumeration of \(C\) returns \(12\) points over \(\mathbb F_{11}\) and \(114\) over \(\mathbb F_{121}\), agreeing with these factors.

**4. Rational simplicity, nonisogeny, and ordinarity.** The reduction of \(P_+\) modulo \(3\) is \(T^4-T^3+T+1\). It has no monic factor of degree one or two over \(\mathbb F_3\), as exhaustively checked in `verify.py`; thus \(P_+\), and therefore \(P_-(T)=P_+(-T)\), is irreducible in \(\mathbb Q[T]\). Tate's finite-field isogeny theorem implies that each \(J(Y_\pm)\) is simple over \(k\), and their unequal characteristic polynomials imply that they are not isogenous over \(k\). The middle coefficient \(6\) is nonzero modulo \(11\), so both genus-two factors are ordinary, and so is their isogenous product. The curve isomorphism over \(K\) from Step 2 shows that their principally polarized Jacobians become isomorphic over \(K\).

## Verification

Run `python3 verify.py` with standard Python. The program constructs the field of order \(121\) as ordered pairs with multiplication \((a+bi)(c+di)=(ac-bd)+(ad+bc)i\), enumerates every field element and every square, independently counts both genus-two curves and the genus-four curve over the two fields, checks the Frobenius coefficients and group order, and tests irreducibility of the quartic modulo three by every monic linear/quadratic divisor. Its final success line is `ACCOLA_MACLACHLAN_F11_DESCENT_OK`. Finite enumeration proves these finite-field counts exactly; the quotient and isogeny identities are proved symbolically above.

## Relationship to prior work

Auffarth, Reyes-Carocca and Rojas (2024) give the complex Jacobian decomposition of the Accola–Maclachlan curve of genus four into two isomorphic simple abelian surfaces; that geometric decomposition is **not claimed as new**. Bruin and Kulkarni (2023) give a broader theory of \((2,2)\)-decomposable genus-four Jacobians, including hyperelliptic examples isogenous to genus-two squares; neither their general framework nor a bare geometric product decomposition identifies the two distinct \(\mathbb F_{11}\)-Frobenius factors here. The assessed arithmetic contribution is the exact nonisogenous/simple/ordinary Frobenius descent and the minimal quadratic field where those factors become isomorphic, with a complete zeta numerator as its numerical witness.

## Limitations

No statement is made about the absolute simplicity of the factors or a polarization-preserving decomposition of \(J(C)\) over \(\mathbb F_{11}\). The result is specific to characteristic eleven, although the double-quotient and twisting identities hold over all odd characteristics other than five. A preexisting local Euler-factor table for \(Y_+\), or an equivalent unpublished arithmetic computation, could reduce historical novelty; the combination with the quotient descent must be distinguished from such a table. The independent mathematical audit of this result has not been performed.

## References

1. R. Auffarth, S. Reyes-Carocca, A. M. Rojas, *On the Jacobian variety of the Accola-Maclachlan curve of genus four*, arXiv:2401.13277, first posted 2024-01-24. https://arxiv.org/abs/2401.13277
2. N. Bruin, A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959, first posted 2023-09-05, especially Section 7.1. https://arxiv.org/html/2309.01959v1
