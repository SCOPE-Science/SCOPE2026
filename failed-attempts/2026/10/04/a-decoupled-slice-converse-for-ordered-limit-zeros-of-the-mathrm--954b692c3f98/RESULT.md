# A decoupled-slice converse for ordered-limit zeros of the \(\mathrm{A}_2\) zeta function
## Finding
Let \(a,c\in\mathbb N_0\) and let \(\boldsymbol\ell=(a,0,c)\) denote the rank-two tuple with \(\ell_{11}=a\), \(\ell_{12}=0\), and \(\ell_{22}=c\). For \(\zeta_{\mathrm A_2}\) at \((-a,0,-c)\), the regular ordered limit and the ordered limit corresponding to the permutation \((23)\) vanish simultaneously if and only if \(a,c\ge1\) and \(a+c\) is odd. Consequently, on the slice \(\ell_{12}=0\), simultaneous vanishing of all six ordered limits forces the trivial-zero condition, proving the only-if direction of Rutard--Shinohara's Conjecture 2 on this entire slice.

Thus the natural decoupled slice \(\ell_{12}=0\) admits a two-limit detector for the conjectural necessary condition: no tuple outside the trivial-zero locus can make every rank-two ordered limit vanish.

## Assumptions and scope
For \(a,c\in\mathbb N_0\), write
\[
\boldsymbol\ell=\begin{pmatrix}a&0\\&c\end{pmatrix}.
\]
The ordered limits are those defined for \(\zeta_{\mathrm A_2}\) in arXiv:2609.28354v1. The claim concerns exactly the codimension-one slice \(\ell_{12}=0\). It proves the converse/only-if direction of the source conjecture on this slice; it does not prove that all six ordered limits vanish whenever the trivial-zero condition holds.

## Proof
Rutard--Shinohara's Example 11 gives, for the ordered limit labelled by the permutation \((23)\),
\[
P(a,c):=\zeta_{\mathrm A_2}\!\left(\overset{(23)}{\begin{smallmatrix}-a&0\\&-c\end{smallmatrix}}\right)=\zeta(-a)\zeta(-c).
\]
Their Example 19 gives, after setting \(\ell_{12}=0\), the regular value
\[
R(a,c):=\zeta_{\mathrm A_2}\!\left(\overset{\mathrm{reg}}{\begin{smallmatrix}-a&0\\&-c\end{smallmatrix}}\right)
=\zeta(-a)\zeta(-c)+\frac{(-1)^{c+1}}{c+1}\zeta(-a-c-1).
\]
Therefore \(P(a,c)=R(a,c)=0\) if and only if
\[
\zeta(-a)\zeta(-c)=0,\qquad \zeta(-a-c-1)=0.
\]
For every \(n\in\mathbb N_0\), the classical formula \(\zeta(-n)=(-1)^n B_{n+1}/(n+1)\) and the vanishing of odd Bernoulli numbers above degree one imply
\[
\zeta(-n)=0\quad\Longleftrightarrow\quad n\text{ is a positive even integer}.
\]
Hence the first equation says that at least one of \(a,c\) is positive even. The second says that \(a+c+1\) is positive even, equivalently \(a+c\) is odd. The other member of \(\{a,c\}\) is then positive odd, so necessarily \(a,c\ge1\) and \(a+c\) is odd.

Conversely, if \(a,c\ge1\) and \(a+c\) is odd, then one of \(a,c\) is positive even, so \(P(a,c)=0\). The tuple has positive diagonal entries and total weight \(a+c\equiv1\pmod2\); Rutard--Shinohara's Theorem 1, specialized to the regular value in rank \(r=2\), gives \(R(a,c)=0\). This proves the two-limit equivalence.

Finally, if all six ordered limits vanish, then in particular \(P(a,c)=R(a,c)=0\), so the condition \(a,c\ge1\) and odd \(a+c\) follows. This is exactly the only-if direction of Conjecture 2 on \(\ell_{12}=0\).

## Verification
The proof is exact and does not depend on finite computation. The accompanying `verify.py` independently evaluates the two detector formulas using exact rational Bernoulli numbers and checks the equivalence for every \(0\le a,c\le40\). Its output is stored in `verification_output.txt`. This finite replay is only a corroborative check of the formulas and boundary cases; the universal result is supplied by the proof above.

## Relationship to prior work
Rutard--Shinohara introduce all ordered limits and state Conjecture 2, whose only-if direction says that common vanishing of every ordered limit forces positive diagonal exponents and the required weight parity. Their Theorem 1 proves vanishing only for three distinguished types of ordered limit under the trivial-zero condition. Example 11 and Example 19 provide the two exact rank-two formulas used here. The source does not state the two-limit equivalence on \(\ell_{12}=0\), nor the resulting proof of the conjectural only-if direction on that full slice.

Targeted searches for the source title together with “ordered limit”, “common zeros”, “converse”, and the slice \(\ell_{12}=0\), together with searches of the published finding index, did not identify a result implying this classification. The closest retrieved material concerned unrelated zeta or zero-structure problems rather than ordered limits of \(\zeta_{\mathrm A_2}\).

## Limitations
This is an infinite but deliberately narrow structural result. It proves only the necessary/converse direction of Conjecture 2 on the decoupled slice \(\ell_{12}=0\). It does not prove common vanishing of all six ordered limits under the trivial-zero condition, does not treat \(\ell_{12}>0\), does not determine when individual ordered limits coincide, and does not address higher rank. Because the argument is a short consequence of newly published formulas, there remains a residual risk that the same observation appears in subsequent work not yet indexed.

## References
1. Simon Rutard and Takeshi Shinohara, “Trivial zeros of zeta functions of type \(\mathrm A_r\),” arXiv:2609.28354v1, submitted 2026-09-23. Relevant items: Theorem 1, Conjecture 2, Example 11, Example 19, and Remark 12.
