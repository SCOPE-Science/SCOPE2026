# Parity-obstructed lifting of depth-one involutions in truncated Nottingham groups

## Finding
Let \(k\) be any field of characteristic \(2\), and let \(N\geq2\). In the group \(G_N(k)\) of series \(f(t)=t+\sum_{j=2}^N a_jt^j\) under composition modulo \(t^{N+1}\), define \(I_N\) to be the **reduced** subvariety cut out by \(f\circ f=t\) and \(a_2\ne0\). Then
\[
 I_N\simeq\mathbb G_m\times\mathbb A^{\lfloor(N-1)/2\rfloor}
\]
over \(k\). The open condition \(a_2\ne0\) is the depth-one ramification stratum.

Let \(L_N\subseteq I_N\) consist of truncations of genuine order-two elements of the full substitution group \(G(k)=\{t+\sum_{j\ge2}a_jt^j\}\). If \(N\) is even, \(L_N=I_N\). If \(N=2m+1\) is odd, \(L_N\) is a smooth codimension-one closed subvariety of \(I_N\), isomorphic to \(\mathbb G_m\times\mathbb A^{m-1}\). It is given by the single condition that the coefficient \([t^{N+1}](f\circ f-t)\) vanishes; the condition is independent of the omitted coefficient \(a_{N+1}\).

In particular, for every finite field \(\mathbb F_q\) of characteristic \(2\),
\[
 |I_N(\mathbb F_q)|=(q-1)q^{\lfloor(N-1)/2\rfloor},\qquad
 |L_N(\mathbb F_q)|=(q-1)q^{\lfloor(N-2)/2\rfloor}.
\]
Thus every depth-one involution at an even truncation level lifts to an honest involution, while precisely a proportion \(1/q\) does so at each odd level. This is a theorem about this depth-one stratum, not about all involutions in \(G_N(k)\).

## Assumptions and scope
The integer \(N\) ranges over all \(N\ge2\); the field \(k\) is arbitrary of characteristic \(2\), not necessarily finite, perfect, or algebraically closed. Composition is always taken modulo \(t^{N+1}\) in \(G_N(k)\), and the full group uses formal power series without truncation. A point of \(I_N\) is an element whose square is the identity in \(G_N(k)\), not necessarily the truncation of a formal involution. The identity itself does not occur in the depth-one stratum.

All geometric statements concern reduced varieties. No assertion is made about nonreduced structure of the full involution equation scheme.

## Proof
For a formal series \(f=t+a t^2+\cdots\) with \(a\ne0\), write
\[
 f\circ f=t+\sum_{j\ge4} E_j t^j.
\]
The coefficients in degrees \(2\) and \(3\) vanish identically in characteristic \(2\). We prove two facts.

**(1) A nontrivial square cannot begin in an odd degree.** Suppose \(g=f\circ f\ne t\), and \(g=t+b t^r+O(t^{r+1})\) with \(b\ne0\) and \(r\ge4\). The two series \(f\) and \(g\) commute. A direct substitution, using \(f=t+a t^2+O(t^3)\), gives
\[
 [t^{r+1}](f\circ g-g\circ f)=r a b
\]
in characteristic \(2\). If \(r\) were odd, this coefficient would equal \(ab\ne0\), contradicting commutativity. Hence \(r\) is even. Consequently, after making \(E_4,E_6,\ldots,E_{2j-2}\) vanish, the intervening odd coefficients through \(E_{2j-1}\) vanish automatically.

**(2) Each even obstruction determines exactly one odd-indexed coefficient.** For every \(j\ge2\), the coefficient \(E_{2j}\) depends on \(a_{2j-1}\) affinely, with coefficient \(a=a_2\), and is independent of all \(a_i\) with \(i\ge2j\):
\[
 E_{2j}=a\,a_{2j-1}+P_j(a_2,\ldots,a_{2j-2}).
\]
To see the coefficient of \(a_{2j-1}\), compare substitution of the perturbation \(a_{2j-1}t^{2j-1}\): its direct occurrence cancels, while expanding its outer term around \(f=t+a t^2+\cdots\) contributes \((2j-1)a a_{2j-1}t^{2j}=a a_{2j-1}t^{2j}\); terms of smaller outer degree cannot contribute a new linear term at this degree in characteristic \(2\). Thus \(E_{2j}=0\) has exactly one solution for \(a_{2j-1}\), namely \(a_{2j-1}=a^{-1}P_j\).

Begin with arbitrary \(a=a_2\in k^\times\), and choose all even-indexed coefficients \(a_4,a_6,\ldots\) freely. Recursively solve \(E_4=0\) for \(a_3\), then \(E_6=0\) for \(a_5\), and so on; fact (1) removes all intervening odd-degree equations. This constructs a unique full formal involution for every sequence of even-indexed coefficients and nonzero \(a_2\).

At level \(N=2m\), the determining equations are \(E_4=\cdots=E_{2m}=0\): there are \(m-1\) free coefficients \(a_4,a_6,\ldots,a_{2m}\), in addition to nonzero \(a_2\). The formal recursion extends every such jet. At level \(N=2m+1\), the last coefficient \(a_{2m+1}\) is unconstrained by equations through degree \(N\) and contributes one more affine coordinate. Extension requires \(E_{2m+2}=0\), which uniquely determines that last odd coefficient, without involving any new coefficient \(a_{2m+2}\). Once it holds, all subsequent equations can again be solved recursively.

These formulas and their inverses are polynomial in the free variables and \(a_2^{-1}\). In particular, after taking reduced structures they give the claimed isomorphisms of varieties over arbitrary characteristic-two fields. Counting their rational points yields the stated formulas.

## Verification
Run `python check.py` using Python 3 (standard library only) in the folder containing this document. The program constructs actual truncated compositions over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), and exhaustively enumerates every series with \(a_2\ne0\) for the degrees listed in `checked_output.txt`. It tests the involution equations through degree \(N\) and the first possible lifting obstruction at degree \(N+1\). The two predicted counts agree in every tested case. The program is a finite check, not the proof of the statements for all \(N\) or all fields.

For a hand-checkable example, at \(N=3\) every series \(t+a_2t^2+a_3t^3\) with \(a_2\ne0\) is an involution modulo \(t^4\); it lifts precisely when \(a_3=a_2^2\), the coefficient equation in degree four. At \(N=4\), that equation is already part of the truncated involution condition, and every solution lifts.

## Relationship to prior work
The Nottingham group and its ramification filtration are classical. Lubin (2011, building on Klopsch) classifies **genuine** finite-order Nottingham elements up to conjugacy, with depth and leading coefficient as invariants; the depth-one formal involutions are conjugate to fractional-linear series. This does not directly count the elements of order two in **finite truncations that fail to lift**, nor give the odd-even affine geometry of the depth-one quotient stratum. The present theorem explicitly separates finite order-two jets from jets of true order-two elements.

Szechtman's 2026 preprint studies the power-commutator presentation of truncated substitution groups, including all levels through \(N=15\) over prime fields. Its results can support finite-level calculations but do not themselves state the all-level, all-characteristic-two-field lifting and counting theorem above. The earlier conjugacy-class count of Pálfy (1998) likewise concerns conjugacy classes in selected finite quotients, a different invariant. The result may be derivable from general unpublished or unlocated torsion-lifting theorems; historical priority is not independently certified.

## Limitations
This treats only the depth-one stratum (nonzero quadratic coefficient), not all involutions at greater depth. All schemes are reduced. Characteristic different from two and non-field coefficient rings are excluded. The affine-parameter theorem is proved internally; external validation and an exhaustive priority determination have not been performed.

## References
1. Jonathan Lubin, *Torsion in the Nottingham group*, Bulletin of the London Mathematical Society 43 (2011), 547–560, DOI 10.1112/blms/bdq120; author's accessible manuscript: https://www.math.brown.edu/jlubin/TorsInNott.pdf (publicly dated journal version 2011-01-28).
2. Fernando Szechtman, *A power-commutator presentation for the group of truncated polynomials under substitution*, arXiv:2610.01469 (first posted 2026-10-01), https://arxiv.org/abs/2610.01469.
3. P. P. Pálfy, *The number of conjugacy classes in some quotients of the Nottingham group*, Proceedings of the Edinburgh Mathematical Society 41 (1998), 369–384, DOI 10.1017/S0013091500019714 (full text not inspected here).
