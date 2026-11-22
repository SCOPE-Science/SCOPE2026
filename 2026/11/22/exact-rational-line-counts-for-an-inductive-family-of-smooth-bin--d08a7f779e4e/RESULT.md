# Exact rational-line counts for a smooth binary space-filling quartic family

## Finding

For each integer \(n\ge3\), a distinguished inductive family of geometrically smooth, space-filling quartics \(Y_n\subset\mathbb P^n_{\mathbb F_2}\) has exactly

\[
L_n=\#\{\mathbb F_2\text{-rational projective lines }\ell\subset Y_n\}
=\frac{2\cdot 4^n-9\cdot 2^n+4}{12}.
\]

Its ordinary line-count generating function is

\[
\sum_{m\ge0}L_{m+3}t^m=\frac{5-4t}{(1-t)(1-2t)(1-4t)}.
\]

The values for \(n=3,4,5,6,7,8,9,10\) are \(5,31,147,635,2635,10731,43307,173995\). The fraction of all ambient \(\mathbb F_2\)-rational projective lines that are contained in \(Y_n\) tends to exactly \(1/4\) as \(n\to\infty\).

## Assumptions and scope

Work over \(\mathbb F_2\). In the homogeneous coordinate ring on \(\mathbb P^n\), set

\[
\phi_{ij}=X_i^2X_j+X_iX_j^2,\qquad
B=X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(X_0+X_3)\phi_{30}.
\]

The base quartic must be the *coordinate-transformed* polynomial

\[
H(X_0,X_1,X_2,X_3)=B(X_0,X_1,X_2+X_3,X_2),\quad F_3=H,
\]

and the recursion is, for every integer \(n\ge3\),

\[
F_{n+1}=F_n+(X_n+X_{n+1})\phi_{n,n+1},\qquad Y_n=V(F_n).
\]

The original source's Lemmas 9.2 and 9.4, with \(b=c=\lambda=1\) in \(\mathbb F_2\), show that \(H\) and its section \(H|_{X_3=0}\) are geometrically smooth. Its Proposition 9.1 propagates both smoothness and the smooth-section hypothesis inductively. These established premises apply specifically to the transformed base \(H\), not merely to \(B\). Every \(Y_n\) is therefore a smooth (and hence geometrically integral) space-filling quartic. A *rational line* means a projective line defined over the base field, not an arbitrary geometric line over \(\overline{\mathbb F}_2\).

## Proof

**Step 1: Restrict to a rational line.** Identify the vector space of binary linear forms in parameters \((s,t)\) with \(V=\mathbb F_2^2\), and write its elements as \(u\). Every rational projective line is given by a rank-two word \((u_0,\ldots,u_n)\in V^{n+1}\), modulo the free action of \(\operatorname{GL}_2(\mathbb F_2)\), which has order six. Put \(h(s,t)=st(s+t)\) and let \(\det(u,v)\in\mathbb F_2\) denote the two-by-two determinant. Direct substitution into the cubic Frobenius form gives the exact polynomial identity

\[
\phi(u,v)=u^2v+uv^2=\det(u,v)\,h(s,t).
\]

Both sides vanish for dependent vectors. For independent vectors, \((u,v)\) is a basis of \(V\) and \(u^2v+uv^2\) is the product of the three nonzero linear forms; over \(\mathbb F_2\) the determinant is one. Thus the restriction of any \(F_n\) is \(h(s,t)\) times a binary linear form. Because the polynomial ring is a domain, restriction is identically zero precisely when that residual linear form vanishes.

**Step 2: Explicit residual state.** Represent \(u\in V\) as the two-bit integer \(0,1,2,3\). Define

\[
T(u,v)=\det(u,v)(u+v).
\]

For a four-symbol word \((a,b,c,d)\), first define the residual vector for the untransformed base:

\[
Q_B(a,b,c,d)=\det(a,b)b+\det(b,c)c+\det(c,d)d+\det(d,a)(d+a).
\]

All vector arithmetic in this formula is in \(V\). For the actual transformed base,

\[
Q_H(a,b,c,d)=Q_B(a,b,c+d,c).
\]

On adjoining each new coordinate with last vector \(d\) and new vector \(e\), the state \((d,z)\in V^2\), where \(z\) is the residual obstruction, evolves exactly by

\[
(d,z)\longmapsto(e,z+T(d,e)).
\]

Consequently, the sixteen states form a finite, exact transfer system for *all* integers \(n\ge3\), not a numerical extrapolation.

**Step 3: Symmetry reduction to five states.** Simultaneous \(\operatorname{GL}_2(\mathbb F_2)\) changes of coordinates partition the sixteen pairs into the five types

\[
A:(d,z)=(0,0),\quad B:d=0,\ z\ne0,\quad
C:d\ne0,\ z=0,\quad D:d=z\ne0,\quad E:d,z\ne0,\ d\ne z.
\]

Their numbers of states are \(1,3,3,3,6\) respectively. For each type retain its **per-individual-state** count, forming the column vector \(v_n=(A_n,B_n,C_n,D_n,E_n)^\mathsf T\). Enumerating the 256 four-symbol words according to the displayed formula \(Q_H\) gives the complete base vector

\[
v_3=(22,14,18,18,14)^\mathsf T.
\]

The transition rule in Step 2 gives, by considering the four possible newly appended symbols for each representative state,

\[
v_{n+1}=Mv_n,\qquad
M=\begin{pmatrix}
1&0&3&0&0\\
0&1&0&1&2\\
1&0&1&0&2\\
0&1&0&3&0\\
0&1&1&0&2
\end{pmatrix}.
\]

This is a complete state partition; each entry is the exact number of predecessor states of the indicated type for an individual successor state. The characteristic polynomial is

\[
\det(xI-M)=x(x-2)(x-4)(x^2-2x-4).
\]

**Step 4: Count line words and remove rank deficiency.** A word has zero residual obstruction precisely in types \(A\) and \(C\). The number of words, including rank-deficient ones, is therefore \(K_n=A_n+3C_n\). Since \(K_n=(1,0,3,0,0)M^{n-3}v_3\), multiplying the finite matrices gives the *exact rational-function identity*

\[
\sum_{m\ge0}K_{m+3}t^m
=(1,0,3,0,0)(I-tM)^{-1}v_3
=\frac{76-176t}{(1-2t)(1-4t)}
=\frac{64}{1-4t}+\frac{12}{1-2t}.
\]

In particular \(K_n=4^n+3\cdot2^{n-1}\) for all \(n\ge3\). Every rank-zero or rank-one word has identically vanishing quartic restriction. There are exactly \(3\cdot2^{n+1}-2\) such words: each of the three one-dimensional subspaces of \(V\) supports \(2^{n+1}\) words, and their only common word is zero. Each rank-two word has exactly six parameter bases. Hence

\[
L_n=\frac{K_n-(3\cdot2^{n+1}-2)}6
=\frac{2\cdot4^n-9\cdot2^n+4}{12}.
\]

Summation gives the stated generating function, completing the count without geometric-line or multiplicity assumptions.

**Step 5: Asymptotic density.** The ambient number of rational projective lines is

\[
\#\operatorname{Gr}(2,n+1)(\mathbb F_2)
=\frac{(2^{n+1}-1)(2^{n+1}-2)}6.
\]

Its leading term is \(4\cdot4^n/6\), compared with \(4^n/6\) for \(L_n\), establishing the limit \(1/4\).

## Verification

The bundled standard-library checker `verify_lines.py` computes restrictions by polynomial multiplication in \(\mathbb F_2[s,t]\), independently of the vector transfer formula. It exhaustively enumerates the rational-line parameter words for dimensions \(3\le n\le7\) and obtains \(5,31,147,635,2635\); it separately verifies all 256 base words, all sixteen state transitions, and the first 32 coefficients of the exact generating function and closed form. The infinite theorem follows from the algebraic restriction identity and finite transfer matrix in Steps 1–4; no extrapolation from those tests is used. To reproduce: `python3 verify_lines.py`.

## Relationship to prior work

Bourgeois-Conti, Moon, Perez and Warren, *Space-Filling Hypersurfaces* (arXiv:2611.15768v1, 2026), §9, provide the original transformed quartic and smooth induction. They establish smoothness and space-filling, not the exact counts of contained \(\mathbb F_2\)-rational lines, the generating function or the limiting line density. General work on transverse or tangent lines over finite fields, such as Asgarli–Duan–Lai (2021) and Bruggemann–Choi–Freidin–Whyte (2025), concerns different line-incidence conditions and does not by itself imply this enumeration. The base surface's other known cohomological or line information is not a counting theorem for the higher-dimensional induction.

## Limitations

Only the explicit transformed-base induction, the binary field, and \(\mathbb F_2\)-rational projective lines are covered. The entire scheme of lines over an algebraic closure, nonreduced Fano-scheme structure, extension-field counts, and alternative quartic families are not determined. The starting paper supplies smoothness and space-filling; the proof here establishes the new incidence count conditional on the explicit, independently inspected source construction. Historical publication priority cannot be proved from finite searches or incomplete archival access.

## References

- V. Bourgeois-Conti, H.-B. Moon, E. Perez, A. Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1 (first public 2026-11-11), especially Proposition 9.1, Lemmas 9.2 and 9.4, Theorem 9.5. https://arxiv.org/abs/2611.15768
- S. Asgarli, L. Duan, K.-W. Lai, *Transverse lines to surfaces over finite fields*, Manuscripta Math. **165** (2021), 135–157; arXiv:1903.08845.
- C. Bruggemann, J. Choi, G. Freidin, N. Whyte, *Transverse-freeness in finite geometries*, Finite Fields Appl. **108** (2025), 102663; arXiv:2409.05248.
- N. M. Katz, *Space filling curves over finite fields*, Math. Res. Lett. **6** (1999), 613–624.
