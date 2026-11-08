# Conductor and characteristic-dividing polar collapse for dual rational normal scrolls

## Finding
For every field \(k\) and every integer \(n\ge2\), consider the smooth rational normal scroll \(S(1,n)\subset\mathbb P^{n+2}_k\) and its projective dual hypersurface \(D\). In adapted dual homogeneous coordinates \([a:b:c_0:\cdots:c_n]\), put
\[
F(a,b,c)=\sum_{i=0}^n c_i a^{n-i}b^i,\qquad D=V(F),\qquad\Lambda=V(a,b)\cong\mathbb P^n.
\]
The normalization of \(D\) is the product \(\mathbb P^1\times\mathbb P^n\). More precisely, a point of the product is a linear form \(\ell\) up to scalar, together with \([u:R]\) where \(u\in k\) and \(R\) is a binary form of degree \(n-1\). The finite birational map is
\[
([\ell],[u:R])\longmapsto[L=u\ell,\ Q=\ell R].
\]
Here the coefficients of \(L\) are linearly reparametrized as \(a,b\), and the coefficients of \(Q\) are \(c_0,\dots,c_n\). The *conductor ideal sheaf*, the annihilator in \(\mathcal O_D\) of the normalization quotient, is exactly
\[
\boxed{\mathfrak c_D=\mathcal I_\Lambda^{n-1}.}
\]
The full Jacobian singular ideal is \((a,b)^n+(F_a,F_b)\), with reduced support \(\Lambda\). If \(\operatorname{char}k=p>0\) and \(p\mid n\), define
\[
G=\sum_{i=1}^{n-1} i c_i a^{n-i-1}b^{i-1}.
\]
Then \(F_a=-bG\), \(F_b=aG\), and
\[
\boxed{J_D=(a,b)^n+(aG,bG).}
\]
At the scheme-theoretic generic point of \(\Lambda\), the transverse Artin algebra has Hilbert function \((1,2,\ldots,n-1,n-2)\), length \(\binom{n+1}{2}-2\), with the convention that for \(n=2\) the last entry is zero. The reduced two-variable polar map \([a:b]\dashrightarrow[F_a:F_b]\), after canceling its maximal common factor, is \([a:b]\mapsto[-b:a]\), of degree one, for generic \(c_i\). If the characteristic does not divide \(n\), the generic polar map has degree \(n-1\); the two degrees coincide for \(n=2\), so strict collapse occurs only for \(n\ge3\).

For any finite field \(\mathbb F_q\), and for any positive integer \(r\),
\[
\#D(\mathbb F_{q^r})=\sum_{i=0}^{n-1}q^{ri}+2q^{rn}+q^{r(n+1)}.
\]
Equivalently, \([D]=[\mathbb P^n]+\mathbb L^n[\mathbb P^1]\) in the Grothendieck ring of varieties over \(k\).

## Assumptions and scope
All formulas are scheme-theoretic over an arbitrary ground field. The polar-degree comparison is generic in the coefficient parameters \(c_i\); it does **not** say that every specialization has that degree. The normalization statement is global, and the conductor formula is an equality of ideal sheaves on the whole projective hypersurface, including repeated-root strata. The Jacobian length is taken after localizing at the generic point of the linear singular stratum \(\Lambda\). The positive-characteristic polar collapse requires the divisibility hypothesis \(p\mid n\).

## Proof
**(1) The dual resultant.** On any local trivialization of the scroll bundle over \(\mathbb P^1\), write \([s:t]\) for the base coordinates and \([u:v]\) for the locally trivialized fiber coordinates. The local scroll parametrization is
\[
([s:t],[u:v])\longmapsto[u s:u t:v s^n:v s^{n-1}t:\cdots:v t^n].
\]
The fiber coordinates \([u:v]\) here do not define global coordinates on a product; they transform as the summands of \(\mathbb P(\mathcal O(1)\oplus\mathcal O(n))\).
A hyperplane pulls back to \(uL(s,t)+vQ(s,t)\) with \(L\) linear and \(Q\) homogeneous of degree \(n\). Tangency at some point requires \(L=Q=0\) at the base point, and conversely the remaining base derivative equation is one homogeneous linear condition in \([u:v]\) and has a nonzero solution. Therefore the dual is the resultant hypersurface. Choose \(L=b s-a t\), whose unique zero is \([a:b]\). Its resultant with \(Q(s,t)=\sum c_i s^{n-i}t^i\) is \(F=Q(a,b)\) up to an irrelevant nonzero scalar. Because \(F\) is primitive and linear in the algebraically independent \(c_i\), it is irreducible over \(k\).

**(2) Normalization.** The incidence variety parametrizing a common linear divisor is \(Z=\mathbb P^1\times\mathbb P^n\) with the displayed bilinear map. This product parametrization belongs to the normalization, not to the original scroll bundle. It is proper; its fiber over \((L,Q)\) is the finite set of linear common factors (if \(L\ne0\), exactly the factor \(L\), otherwise the at most \(n\) factors of nonzero \(Q\)). Thus the map is quasi-finite and proper, hence finite. It is an isomorphism above \(L\ne0\), and \(Z\) is smooth, so \(Z\to D\) is the normalization.

**(3) Exact conductor on every chart.** Work first where the coefficient of \(s^n\) in \(Q\) is nonzero, normalize it to \(1\), and write \(Q(x,1)=x^n+c_1x^{n-1}+\cdots+c_n\). Put \(A=k[b,c_1,\ldots,c_n]\). On the corresponding affine chart, the equation of \(D\) is monic in \(a\), and the normalization rings are
\[
R=A[a]/\bigl(a^n+c_1a^{n-1}b+\cdots+c_nb^n\bigr),\qquad
B=A[x]/\bigl(x^n+c_1x^{n-1}+\cdots+c_n\bigr),\quad a\mapsto bx.
\]
Each is free over \(A\) of rank \(n\), and inside \(B\) one has the **exact** decomposition
\[
B=\bigoplus_{i=0}^{n-1} A x^i,\quad
R=\bigoplus_{i=0}^{n-1} A b^i x^i,\quad
B/R=\bigoplus_{i=1}^{n-1}\bigl(A/(b^i)\bigr)x^i.
\]
The inclusion \(b^{n-1}B\subset R\) is immediate. To prove maximality, let \(K=k(c_1,\dots,c_n)\). The generic polynomial \(x^n+c_1x^{n-1}+\cdots+c_n\) is irreducible over \(K\); hence \(E=K[x]/(Q)\) is a field of dimension \(n\) over \(K\). If a conductor element had \(b\)-adic order \(e<n-1\), its nonzero leading class in \(E\) would, after multiplication by every element of \(E\), have to lie in the proper subspace \(\langle1,x,\ldots,x^e\rangle_K\), because of the explicit decomposition of \(R\). This is impossible: multiplication by a nonzero element of the field \(E\) is invertible. Thus the conductor inside \(B\) is exactly \(b^{n-1}B\). Under \(a=bx\), the same ideal as an ideal of \(R\) is generated by \(a^j b^{n-1-j}\) for \(0\le j\le n-1\), namely \((a,b)^{n-1}\). These calculations cover the points where \(Q(s,t)\) has nonzero leading coefficient; after a constant linear change of \(s,t\) they cover every nonzero binary form \(Q\) over an algebraic closure. Faithfully flat descent proves the conductor formula over the original field, including all of \(\Lambda\). Off \(\Lambda\) the finite birational map is already an isomorphism and both conductor and \(\mathcal I_\Lambda^{n-1}\) equal the unit ideal.

**(4) Singular scheme and polar behavior.** The derivatives with respect to \(c_i\) are the full set of degree-\(n\) monomials \(a^{n-i}b^i\), so the entire Jacobian ideal equals \((a,b)^n+(F_a,F_b)\), and its radical is \((a,b)\). If \(p\mid n\), differentiating termwise gives \(F_a=-bG\) and \(F_b=aG\). For generic \(c_i\), \(G\) is nonzero of degree \(n-2\). In the local polynomial algebra over the fraction field \(k(c_0,\ldots,c_n)\), all monomials of degree at most \(n-2\) survive modulo \(J_D\), exactly two independent combinations in degree \(n-1\) are killed by \(aG,bG\), and every degree at least \(n\) vanishes. The claimed Hilbert function and length follow. After canceling \(G\), the polar map is \([a:b]\mapsto[-b:a]\). If \(\operatorname{char}k\nmid n\), the specialization \(F=a^n+b^n\) has coprime derivatives \(n a^{n-1},n b^{n-1}\); coprimality is Zariski open, so the generic polar degree is \(n-1\).

**(5) Point counts and motives.** Split \(D=\Lambda\sqcup(D\setminus\Lambda)\). The first piece is \(\mathbb P^n\). On the second piece, the unique zero of \(L\) determines a point of \(\mathbb P^1\); after normalizing the nonzero scalar of \(L\), the forms \(Q=L R\) are parametrized by \(n\) free coefficients. Hence the second piece is a Zariski locally trivial affine-\(n\)-space bundle over \(\mathbb P^1\). This proves the motivic and finite-field formulas for all extensions.

## Verification
The included script `check_scroll_dual.py` checks the coefficient gradients and the characteristic-dividing factorization for \(2\le n\le8\) and \(p\in\{2,3,5,7}\), verifies the symbolic generic length calculation, checks irreducible specializations used to illustrate the normalization-module rank argument, and exhaustively enumerates projective points for five small prime-field cases. Run `python check_scroll_dual.py`; the accompanying `verification_output.txt` is the actual successful execution. All claims for arbitrary \(n\) are established by the algebraic argument above, not extrapolated from the script.

## Relationship to prior work
The geometry of scroll duality is classical. D'Andrea–Chipalkatti (2006) study Jacobian ideals of binary discriminants and two-form resultants, primarily in characteristic zero and with their §5 method formulated for two degrees at least two; their full-text §5 does not determine this linear-form resultant's conductor or the characteristic-dividing polar collapse. Dickenstein–Di Rocco–Piene (2011/2014) treat higher duals and degrees of rational normal scrolls in characteristic zero. Gondim–Russo–Staglianò (2018) write the resultant equation of \(S(1,n)^*\) explicitly (Theorem 3.1) and assume characteristic zero throughout, but do not calculate the normalization conductor or the characteristic-dividing polar geometry. The current claim is the global normalization–conductor computation together with the exact exceptional polar/Jacobian behavior; the resultant equation itself and the scroll construction are not claimed as new. Piene–Sacchiero (1984) is a particularly relevant earlier duality paper for which the full text was not obtained, so historical priority of the characteristic-independent normalization/conductor part remains subject to specialist comparison.

## Limitations
The normalization and conductor formulas concern these specific dual scroll hypersurfaces, not arbitrary resultants. Generic Hilbert functions do not describe all specialized embedded structures. The polar collapse is generic in \(c_i\) and requires characteristic dividing \(n\). Earlier work might contain equivalent conductor information under another formulation; the inaccessible Piene–Sacchiero (1984) full text is a residual novelty risk. Independent mathematical validation has not been performed.

## References
1. C. D'Andrea and J. Chipalkatti (with an appendix by A. Abdesselam), *On the Jacobian ideal of the binary discriminant*, first arXiv posting 2006-01-29, arXiv:math/0601705v1, especially §§1,5. https://arxiv.org/abs/math/0601705
2. A. Dickenstein, S. Di Rocco, and R. Piene, *Higher order duality and toric embeddings*, first arXiv posting 2011-11-20, arXiv:1111.4641, especially §§1,4. https://arxiv.org/abs/1111.4641
3. R. Gondim, F. Russo, and G. Staglianò, *Hypersurfaces with vanishing hessian via Dual Cayley Trick*, first arXiv posting 2018-02-05, arXiv:1802.01295, especially §3.2. https://arxiv.org/abs/1802.01295
4. R. Piene and G. Sacchiero, *Duality for rational normal scrolls*, Communications in Algebra 12 (1984), 1041–1066, DOI:10.1080/00927878408823038 (full text not verified).
