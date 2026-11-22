# Exact two-or-four rational-bitangent distribution in a bielliptic Picard quartic family

## Finding
For every prime power \(q\) of characteristic at least five with \(q\equiv2\pmod3\), consider the smooth plane quartics
\[
C_r:\quad X^3Z+Y^4+rY^2Z^2+Z^4=0,
\qquad r\in\mathbb F_q\setminus\{2,-2\}.
\]
Let \(B_r\) be the reduced finite étale scheme of geometric bitangent lines, including hyperflex tangents, defined over \(\mathbb F_q\). Then
\[
\#B_r(\mathbb F_q)\in\{2,4\},\quad
\#\{r:\#B_r(\mathbb F_q)=2\}=\frac{q+1}{2},\quad
\#\{r:\#B_r(\mathbb F_q)=4\}=\frac{q-5}{2}.
\]
The frequencies count distinct coefficients \(r\), not isomorphism classes of curves. In addition, for arbitrary fields of characteristic other than two and three, each smooth \(C_r\) has the following explicit complete 28-bitangent description: the line \(Z=0\); three lines \(X=bZ\), with \(b^3=(r^2-4)/4\); and 24 lines \(X=a(Y+sZ)\), where
\[
3z^4+4rz^3+6z^2-1=0,\quad s^2=z,\quad a^3=9s-s^{-3}.
\]
These equations also determine the full Frobenius cycles and zeta function of \(B_r\) over every finite extension, by taking the corresponding algebraic roots and Frobenius permutations.

## Assumptions and scope
The geometric formula applies to any field \(k\) with characteristic not two or three and \(r^2\ne4\). The arithmetic distribution requires a finite \(k=\mathbb F_q\), \(q\equiv2\pmod3\); hence characteristic at least five, and the cube map on \(k\) is bijective. A bitangent means a line whose scheme-theoretic intersection with the smooth quartic is twice an effective degree-two divisor; a hyperflex line is included. The curve has genus three. The result concerns the 28-point *line scheme*, not the residue fields of tangency points, nor rational isomorphism classes of curves.

## Proof
**Smoothness and exhaustion.** On the affine chart \(Z=1\), the equation is \(x^3+y^4+ry^2+1=0\). Any finite singular point has \(x=0\) and \(y(2y^2+r)=0\); the equation and its \(y\)-derivative then share a root exactly when \(r^2=4\) (including the case \(y=0\) only if \(1=0\), which cannot happen). The unique point at infinity \([1:0:0]\) is smooth because the \(Z\)-derivative is nonzero there, and its tangent \(Z=0\) has contact order four.

Every projective line besides \(Z=0\) either has form \(X=ay+bZ\) in chart \(Z=1\) (equivalently \(X=a(Y+sZ)\) if \(a\ne0\)), or has form \(Y=cZ\). Every \(Y=cZ\) meets the unique point at infinity transversely and thus is not a bitangent. At \(a=0\), the restriction is \(y^4+ry^2+b^3+1\), which is a square precisely when \(b^3=(r^2-4)/4\). At \(a\ne0\), write \(b=as\). Restriction of the equation to the line gives
\[
y^4+a^3y^3+(3a^3s+r)y^2+3a^3s^2y+a^3s^3+1.
\]
Equality with \((y^2+uy+v)^2\) forces \(u=a^3/2\), \(v=3s^2\), \(a^3=9s-s^{-3}\), and \(3s^8+4rs^6+6s^4-1=0\). Conversely these conditions give the square factorization. The parameter \(s=0\) cannot work, since the constant equation would contradict \(1=0\). Separability follows directly: a common root of \(Q_r(z)\) and \(Q_r'(z)=12z(z^2+rz+1)\) is nonzero, so substitution \(r=-(z^2+1)/z\) gives \(Q_r(z)=-(z^2-1)^2\); then \(z=\pm1\) and \(r=\mp2\), which are excluded. Moreover, if \(a^3=9s-s^{-3}=0\), then \(z=s^2=\pm1/3\), and evaluating \(Q_r(z)\) again forces \(r=\pm2\). Equivalently, the discriminant of \(Q_r\) is \(-6912(r^2-4)^2\) and its resultant with \(9z^2-1\) is \(-144(r^2-4)\). Thus for characteristic not two or three and \(r^2\ne4\), it has four distinct nonzero roots, none producing \(a=0\). Each yields two choices of \(s\) and then three distinct nonzero values of \(a\). The 24 resulting lines, the three \(a=0\) lines and the unique line at infinity are distinct, and they exhaust all 28 geometric bitangents.

**Elliptic interpretation.** Now assume \(q\equiv2\pmod3\). Define \(E:\ v^2=u^3+1\) over \(\mathbb F_q\), with origin \(O\) and \(T=(-1,0)\). The cube map is bijective, so every \(v\in\mathbb F_q\) corresponds to a unique \(u\) and \(\#E(\mathbb F_q)=q+1\); \(T\) is its unique nontrivial rational two-torsion point. For nonzero \(v\), the standard elliptic duplication law gives
\[
v(2P)=\frac{v^4+18v^2-27}{8v^3}.
\]
Putting \(v=3z\), define
\[
R(z)=\frac{1-6z^2-3z^4}{4z^3}=-2v(2P).
\]
The condition \(Q_r(z)=0\) is precisely \(R(z)=r\). For fixed \(r\), multiplication by two has fibres of either zero or two points on \(E(\mathbb F_q)\); the unique \(u\)-coordinate for each rational \(v\) means that the equation \(R(z)=r\) likewise has zero or two rational nonzero roots, except that the finite nonzero restriction would remove the special fibres \(r=\pm2\). In fact \(z=0\) corresponds to \(T\) with \(2T=O\), and the only excluded value of \(v(2P)\) at the image \(O\) is at infinity, so for \(r\ne\pm2\) the rational roots have cardinality zero or two.

If \(P=(u,v)\) and \(P+T=(u',v')\), the addition law gives \(v'=-3v/(u+1)^2\) for \(v\ne0\). Because \(\mathbb F_q\) contains no primitive cube root of unity, \(-3\) is a nonsquare. Consequently the two roots \(z=v/3\) and \(z'=v'/3\) have *opposite quadratic character*. Exactly one is a square in \(\mathbb F_q\). For each square root \(z=s^2\), the two values \(s\) are rational, and the cube equation for \(a\) has exactly one rational solution for each. Hence the 24-line component contributes either zero or two rational bitangents. The line at infinity and exactly one \(X=bZ\) line are always rational. This proves the two-or-four dichotomy.

**Exact frequency.** There are \((q-1)/2\) nonzero squares \(z\in\mathbb F_q\). The map \(z\mapsto R(z)\) is injective on those squares: two distinct rational roots in the same fibre have opposite character, as just shown. The two omitted parameters \(r=\pm2\) each have exactly one square preimage. Indeed, the two preimages of \(r=-2\) are \(z=1,-1/3\), while those of \(r=2\) are \(z=-1,1/3\), and each pair has opposite quadratic character. Thus precisely \((q-1)/2-2=(q-5)/2\) allowable parameters have a square preimage and hence four rational bitangents. There are \(q-2\) smooth parameters in total, leaving \((q+1)/2\) parameters with two rational bitangents.

## Verification
Run the standalone `verify.py` with Python 3 and no third-party packages. It independently tests the square-of-quadratic coefficient conditions for every affine line against the quartic-tower formulas, for every allowable parameter over each prime field from \(5\) to \(101\). For all primes congruent to two modulo three it checks the exact 2/4 distribution, square-root uniqueness and counts. The supplied `examples.csv` is reproducible by `python3 verify.py --csv examples.csv`. This is finite verification; the universal prime-power theorem follows from the preceding algebraic proof, not from the sample. The polynomial discriminant and resultant identities can also be checked by elementary symbolic algebra or a computer algebra system.

## Relationship to prior work
Ohashi, Kudo and Harashita study this precise smooth cyclic-six genus-three family and its Hasse–Witt matrix and \(a\)-numbers. Liang explicitly studies bitangents for cyclic-three, -six, and -nine plane quartics, including three distinguished bitangents on the cyclic-six family. Bethea and Brazelton determine the geometric order-six action on its 28 bitangents, with the known decomposition \(24+3+1\). Laga and Shnidman describe related bitangent-based arithmetic of bielliptic Picard curves and a geometric four-line subsystem. These results are credited and are not asserted new. The present claim is the exact **finite-field rational-bitangent dichotomy and parameter frequencies for every \(q\equiv2\pmod3\)** and an explicit Frobenius-readable tower for this coefficient-marked family. Literature overlap checks have not established independent publication novelty conclusively; an equivalent hidden calculation is possible.

## Limitations
The two-or-four theorem assumes \(q\equiv2\pmod3\) and characteristic at least five; it makes no claim about the frequency distribution for \(q\equiv1\pmod3\), nor characteristic two or three. The parameter frequencies are coefficient-marked, not weighted moduli counts. The Frobenius-readable radical tower does not assert that all 28 bitangents are defined over a uniform low-degree extension, nor that the curve's zeta function is determined by the bitangent count. Computational checks use prime fields, while the proof covers all prime powers. Independent validation has not been performed.

## References
1. R. Ohashi, M. Kudo, S. Harashita, *The a-numbers of non-hyperelliptic curves of genus 3 with cyclic automorphism group of order 6*, arXiv:2111.09777 (first public 2021-11-18), https://arxiv.org/abs/2111.09777.
2. D. Liang, *Invariants, Bitangents and Matrix Representations of Plane Quartics with 3-Cyclic Automorphisms*, arXiv:1902.02914 (first public 2019-02-08), https://arxiv.org/html/1902.02914v2, §4.2.
3. C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242 (first public 2024-10-11), https://arxiv.org/html/2410.09242v1, Theorem 1.1 and §4.8.
4. J. Laga, A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, Journal of the London Mathematical Society, https://doi.org/10.1112/jlms.70347, §7.5 (later related literature; first published 2025-11-21).
