# Characteristic-three resonance in long adjoint Jordan chains of the \(5\times5\) nilradical

## Finding
Let \(k=\mathbb F_q\) be any finite field of characteristic \(p\) and let \(\mathfrak n_5(k)\) be the ten-dimensional Lie algebra of strictly upper-triangular \(5\times5\) matrices with bracket \([X,Y]=XY-YX\). For each \(X\in\mathfrak n_5(k)\), put \(N_X=\operatorname{ad}_X\), \(r_2(X)=\operatorname{rank}(N_X^2)\), and \(r_3(X)=\operatorname{rank}(N_X^3)\). Since \(N_X^4=0\), the number of Jordan blocks of sizes four and three are respectively
\[
 m_4(X)=r_3(X),\qquad m_3(X)=r_2(X)-2r_3(X).
\]
Thus the joint distribution of \((r_2,r_3)\) is exactly the joint distribution of **all Jordan blocks of lengths at least three**; it does *not* determine the blocks of lengths one and two.

The complete number of \(X\) in each stratum is given below. Unlisted rank pairs never occur. All counts are polynomials in \(q\), applicable to every prime power of the indicated characteristic:

| \((r_2,r_3)\) | \(p=2\) | \(p=3\) | \(p\ge5\) |
|---|---|---|---|
| \((0,0)\) | \(q^5(3q^2-q-1)\) | \(q^4(3q^2-2)\) | \(q^4(3q^2-2)\) |
| \((1,0)\) | \(q^5(q-1)^2(3q+1)\) | \(q^4(q-1)^2(q^2+6q+2)\) | \(q^4(q-1)^2(q^2+6q+2)\) |
| \((2,0)\) | \(3q^6(q-1)^2\) | \(q^5(q-1)^2(q+2)(2q-1)\) | \(q^5(q-1)^2(5q-2)\) |
| \((2,1)\) | \(2q^6(q-1)^3\) | \(0\) | \(2q^6(q-1)^3\) |
| \((3,1)\) | \(q^6(q-1)^3(q+1)\) | \(q^6(q-1)^3(q+1)\) | \(q^6(q-1)^3(q+1)\) |

Every column totals \(q^{10}\). In characteristic three, a size-four Jordan block **necessarily coexists with a size-three block**; in every other characteristic, size-four blocks without size-three blocks occur. The exact number of elements of adjoint nilpotency index four is
\[
\#\{X:N_X^3\ne0\}=\begin{cases}
q^6(q-1)^3(q+1),&p=3,\\
q^6(q-1)^3(q+3),&p\ne3.
\end{cases}
\]
The closed set \(\{X:N_X^3=0\}\) has six irreducible components of dimension eight when \(p\ne3\), whereas in characteristic three it has exactly three components of dimensions nine, nine and eight. These component assertions are over any algebraic closure of the base field.

## Assumptions and scope
Coordinates use one-based indices. Write \(A=x_{12},B=x_{23},C=x_{34},D=x_{45}\), \(E=x_{13},F=x_{24},G=x_{35}\) and \(H=x_{14},I=x_{25},J=x_{15}\). These are the ten independent entries of \(X\). All algebraic identities and rank reductions below work over any field, including characteristic two and three; finite-field counting uses only \(|k|=q\). The three coordinates \(H,I,J\) never enter \(N_X^2\) or \(N_X^3\).

## Proof
The bracket of strict matrix units is \([e_{ij},e_{kl}]=\delta_{jk}e_{il}-\delta_{li}e_{kj}\). Consequently \(N_X\) raises the superdiagonal degree by at least one, so \(N_X^4=0\). Matrix-unit multiplication gives exactly three possible nonzero rows of \(N_X^2\), corresponding to outputs \(e_{14},e_{25},e_{15}\). With column labels from the input \(Y\), these rows are:

| Output | Coefficients of the indicated input matrix units |
|---|---|
| \(e_{14}\) | \(y_{12}:BC,\quad y_{23}:-2AC,\quad y_{34}:AB\) |
| \(e_{25}\) | \(y_{23}:CD,\quad y_{34}:-2BD,\quad y_{45}:BC\) |
| \(e_{15}\) | \(y_{12}:BG+FD,\quad y_{13}:CD,\quad y_{23}:-2AG,\quad y_{24}:-2AD,\quad y_{34}:-2ED,\quad y_{35}:AB,\quad y_{45}:AF+EC\) |

Missing coefficients are zero. A third multiplication gives the sole possible nonzero row of \(N_X^3\):
\[
 (N_X^3Y)_{15}=-BCD\,y_{12}+3ACD\,y_{23}-3ABD\,y_{34}+ABC\,y_{45}.
\]
Thus \(r_3\in\{0,1\}\). For \(p\ne3\), it is one exactly when *at least three* of \(A,B,C,D\) are nonzero. For \(p=3\), it is one exactly when \(BC\ne0\) and at least one of \(A,D\) is nonzero.

For \(r_2\), the \(e_{14}\) and \(e_{25}\) rows have coefficients involving only \(A,B,C,D\). The \(e_{15}\) row has three private columns \(y_{13},y_{24},y_{35}\) with coefficients \(CD,-2AD,AB\). When one of these is nonzero, that row is independent of the other two. In the remaining cases, row reduction of the displayed three-by-ten matrix gives the following *exhaustive support table*. A mask \(abcd\) means \(A,B,C,D\), respectively, are nonzero precisely at the positions marked \(1\). With a fixed mask, any nonzero first-superdiagonal entries can be scaled to one by diagonal conjugation; hence the table applies uniformly to their actual values. Entries are multiplicities among the \(q^3\) choices of \((E,F,G)\); unused \((H,I,J)\) contribute another free factor \(q^3\). Set \(k\) equal to the number of ones in the mask. Each table entry must be multiplied by \(q^3(q-1)^k\) to obtain the number of matrices \(X\).

| Masks | \(p=2\) | \(p\ne2\) |
|---|---|---|
| \(0000\) | \((0,0):q^3\) | same |
| \(1000,0001\) | \((0,0):q^2,\ (1,0):q^3-q^2\) | \((0,0):q,\ (1,0):q^3-q\) |
| \(0100,0010\) | \((0,0):q^2,\ (1,0):q^3-q^2\) | same |
| \(1001\) | \((0,0):q^2,\ (1,0):q^3-q^2\) | \((1,0):q^3\) |
| \(1010,0101\) | \((0,0):q^2,\ (1,0):q^3-q^2\) | \((1,0):q^2,\ (2,0):q^3-q^2\) |
| \(1100,0110,0011\) | \((2,0):q^3\) | same |
| \(0111,1110\) | \((3,1):q^3\) | same |
| \(1011,1101\) | \((2,1):q^3\) | \((2,0):q^3\) if \(p=3\), otherwise \((2,1):q^3\) |
| \(1111\) | \((3,1):q^3\) | same |

Here \((s,t):m\) means there are \(m\) choices of \((E,F,G)\) giving \((r_2,r_3)=(s,t)\). To justify the only parameter-dependent lines explicitly: with only \(A\) nonzero, the \(e_{15}\) row is supported on \(-2AG\) and \(AF\), so it vanishes for \(F=G=0\) in odd characteristic and for \(F=0\) in characteristic two. With only \(D\) nonzero the symmetric conditions are \(E=F=0\) or \(F=0\). With only \(B\) or \(C\), vanishing requires respectively \(G=0\) or \(E=0\). For mask \(1010\), the \(e_{14}\) row is \(-2AC\,y_{23}\) and the \(e_{15}\) row has private entry \((AF+EC)y_{45}\); because \(A,C\ne0\), this is a nonzero linear form in \(E,F\). For mask \(0101\), exchange left/right: the decisive linear form is \(BG+FD\), giving the same counts. For mask \(1001\), \(-2AD\) is a private coefficient unless \(p=2\); then only the nonzero linear multiple of \(F\) remains. Masks with two adjacent ones have two distinct nonzero pivots in the three output rows. In each of \(1011,1101\), the first two output rows are dependent, but the third has a private nonzero column, giving rank two. For \(0111,1110,1111\), the first two output rows have independent end-column pivots and the third has a private nonzero column, giving rank three. All cases have been covered; summing the mask contributions yields exactly the five polynomial rows stated in the finding.

For the geometric conclusion, only the four variables \(A,B,C,D\) enter \(N_X^3\). For \(p\ne3\), \(N_X^3=0\) is the monomial variety given by vanishing of all four products of three distinct variables. Its reduced irreducible components are the six coordinate two-planes, times the affine six-space with coordinates \(E,F,G,H,I,J\); each has dimension eight. In characteristic three the equations become \(ABC=BCD=0\), whose reduced variety is \(\{B=0\}\cup\{C=0\}\cup\{A=D=0\}\), times the same affine six-space. These have respective dimensions nine, nine, eight. This proves the asserted modular geometric jump.

## Verification
The independent executable `verify_adpowers.py` constructs the full ten-by-ten bracket matrices directly from products of matrix units, composes them to the second and third powers, and computes the resulting exact ranks without using the displayed row formulas. Its finite-field arithmetic includes the nonprime field \(\mathbb F_4\) represented by a root of \(t^2+t+1\). It exhausts all \(q^7\) choices of \(A,B,C,D,E,F,G\) for \(q=2,3,4,5\); the remaining three free entries multiply all frequencies by \(q^3\). In each of the four fields it matched every predicted rank-pair frequency and the total \(q^{10}\). The captured replay is in `verify_output.txt`. Finite checks provide corroboration, not proof for all fields; the symbolic support reduction proves the general result.

## Relationship to prior work
Goodwin and Röhrle (2012, §3.4) classify the irreducible components of the **commuting-pair variety** of this type-\(A_4\) nilradical in characteristic zero. This is a different incidence problem: it gives neither the second/third adjoint-power ranks nor the characteristic-three jump. Soffer (2014) studies centralizers and bounds on unitriangular conjugacy classes; its linear commutation operator is only the first adjoint power. A later published fixed-flag theorem entitled *Uniform twisted-commutator rank spectrum in the \(5\times5\) nilradical* (2026) gives the complete distribution of \(\operatorname{rank}(Y\mapsto XY-\lambda YX)\), including \(\lambda=1\), but not its second or third powers. A first-power rank alone does not determine the counts of size-three or size-four Jordan blocks. Hu (2022) studies strongly ad-nilpotent elements over characteristic zero, not finite-field long-Jordan-chain counts. These comparisons bound, but do not conclusively establish, historical priority.

## Limitations
The result counts the long Jordan blocks of the nilpotent adjoint actions on \(\mathfrak n_5\), **not** their complete Jordan partitions: sizes one and two remain outside the counted invariant. It does not assert the same laws for larger triangular sizes or for arbitrary conjugates under the general linear group. The geometric components are reduced set-theoretic components, not a calculation of scheme-theoretic multiplicities. Historical priority remains subject to the possibility of an unlocated stronger theorem, particularly in classical orbit/canonical-form literature. No independent audit or external certification has been performed.

## References
1. S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289v1, publicly posted 2012-09-06, especially §3.4. https://arxiv.org/abs/1209.1289
2. A. Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389v1, publicly posted 2014-11-19, §§2–6. https://arxiv.org/abs/1411.5389
3. *Uniform twisted-commutator rank spectrum in the \(5\times5\) nilradical*, published-finding corpus (2026-10-26), particularly `RESULT.md`. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-uniform-twisted-commutator-rank-spectrum-in-the-5-times5-nilradi--7990fa0b63b3
4. Z. Hu, *Strongly Ad-Nilpotent Elements of the Lie Algebra of Upper Triangular Matrices*, 2022, doi:10.1155/2022/3484381. https://doi.org/10.1155/2022/3484381
