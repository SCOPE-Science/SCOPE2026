# Exact noncentral bracket fibers in a free class-four Lie algebra

## Finding

Let \(K=\mathbb F_q\) for any prime power \(q\), and let \(L\) be the ordinary free class-four nilpotent Lie algebra on \(x,y\). Write its homogeneous Hall basis as \(x,y,z,u,v,a,b,c\), where
\[
z=[x,y],\quad u=[x,z],\quad v=[y,z],\quad a=[x,u],\quad b=[x,v]=[y,u],\quad c=[y,v].
\]
For a derived target write \(T=wz+U_1u+U_2v+V_1a+V_2b+V_3c\), encoded by \(w\in K\), \(U=U_1X+U_2Y\), and \(V=V_1X^2+V_2XY+V_3Y^2\). Define \(N_q(T)\) as the number of **ordered** pairs \((r,s)\in L^2\) with \([r,s]=T\). The noncentral fibers are
\[
N_q(T)=\begin{cases}
q^8(q^2-1),&w\ne0,\\
q^9(q^2-1),&w=0,\ U\ne0,\ U\mid V,\\
0,&w=0,\ U\ne0,\ U\nmid V.
\end{cases}
\]
In particular, when the degree-two coefficient vanishes but the degree-three part does not, the latter determines a line, and the degree-four part must be divisible by that same line. Zero counts as divisible. There is no restriction on the characteristic. Central fibers and width are included below as comparisons with known results, not as originality claims.

## Proof

The dimensions in degrees 1–4 are \(2,1,2,3\). One way to check the basis in all characteristics is to use alternation and Jacobi to span each homogeneous piece by the displayed brackets, including the identity \([x,v]=[y,u]\). Their nonzero associative word expansions in the tensor algebra certify independence in each degree. In degrees 3 and 4 the displayed brackets within each degree have distinct numbers of occurrences of \(x,y\); each has a word with coefficient \(1\) or \(-1\), including \(-x^2y^2\) in the noncommutative expansion of \(b\). Only the uppercase variables encoding coordinates are commutative. The degree-four span is central. A degree-one part commuting with both generators must be zero by the degree-two bracket, a degree-two part then vanishes by its brackets in degree three, and the degree-three part must vanish by its degree-four brackets. Thus a derived target is noncentral exactly when \((w,U)\ne(0,0)\).

Write
\[
r=\alpha x+\beta y+\gamma z+\delta u+\epsilon v+r_4,\qquad
s=\alpha' x+\beta' y+\gamma' z+\delta' u+\epsilon' v+s_4.
\]
In commutative binary coordinates let \(f=\alpha X+\beta Y\), \(g=\alpha'X+\beta'Y\), \(d=\delta X+\epsilon Y\), and \(e=\delta'X+\epsilon'Y\). The bracket coordinates are
\[
(w,U,V)=(\alpha\beta'-\alpha'\beta,\ f\gamma'-g\gamma,\ fe-gd).
\]
Indeed, \([z,z]=0\) by alternation, \([x,v]=[y,u]\) produces the mixed coefficient, and every term involving \(r_4,s_4\) vanishes. This is valid in characteristic two. The independent central coordinates account for a common factor \(q^6\).

If \(w\ne0\), the \((f,g)\) with determinant \(w\) number \(q(q^2-1)\): there are \(q^2-1\) choices of \(f\ne0\) and \(q\) solutions for \(g\) in an affine line. The map \((\gamma,\gamma')\mapsto U\) is bijective. Since \(f,g\) form a basis of the linear forms, the map \((d,e)\mapsto fe-gd\) surjects onto binary quadratics and has a one-dimensional kernel. This gives \(q^8(q^2-1)\) lifts per target.

If \(w=0\) and \(U\ne0\), the nonzero dependent pair \((f,g)\) must span a line \([\ell]\), where \(\ell\) divides \(U\) and \(V\). There is just one candidate, the line of \(U\) itself. Fix a representative \(\ell\) and write \((f,g)=(s_0\ell,t_0\ell)\) with \((s_0,t_0)\ne(0,0)\). For each of the \(q^2-1\) scalar pairs, the equation \(s_0\gamma'-t_0\gamma=U/\ell\) has \(q\) lifts, and the equation \(s_0e-t_0d=V/\ell\) on two linear forms has \(q^2\) lifts. With the central coordinates this gives exactly the stated mixed-degree fiber.

## Comparison with central quotients and width

The central fibers are recoverable from the central quotient census [1]. For a nonzero central target \(C\) encoded by the binary quadratic \(V\), let \(J=KC\). Its quotient commuting probability is
\[
P_{\nu}=\frac{2q^3+q^2-q-1+\nu(q-1)^2(q+1)}{q^7},
\]
where \(\nu\) is the number of rational projective roots of \(V(t,-s)\), equivalently the number of distinct rational projective linear factors of \(V\). Central lifts give \(q^{16}P_\nu=\sum_{C'\in J}N_q(C')=N_q(0)+(q-1)N_q(C)\), using invariance of the count under scaling one input. For an irreducible quadratic (available over every finite field), no nonzero element of \(J\) is a bracket: any dependent nonzero pair \((f,g)\) of linear parts forces \(V\) to be divisible by their line, and if both vanish the bracket is zero. This also follows from the degree-four image planes and their normal vectors in [1]. Thus \(N_q(0)=q^{16}P_0=q^{12}+(q+1)q^9(q^2-1)\), and subtraction yields \(N_q(C)=q^9(q^2-1)\nu\). In particular the zero-target commuting probability for \(L\) is \(q^{-4}+(q+1)(q^2-1)q^{-7}\).

Combining the noncentral and recovered central counts, the number of distinct single brackets is
\[
(q-1)q^5+(q^2-1)q^2+\frac{(q^2-1)(q+2)}2+1.
\]
The first term counts the arbitrary other coordinates when \(w\ne0\). When \(w=0\), \(U\ne0\), the allowed quadratics are its \(q^2\) multiples. For nonzero central targets the attainable quadratic is a product of two rational linear forms: choose an unordered pair with repetitions from the \(q+1\) lines, then a nonzero scalar. The last term is zero. The exact width two also follows from the central comparison and the Hall basis, since \([L,L]=[x,L]+[y,L]\) and an irreducible central quadratic is not a single bracket. The width of rank-two free nilpotent Lie algebras belongs to the broader arbitrary-field setting of [2]; the width is not part of the originality claim.

## Reproducibility and scope

The supplied script `verification/bracket_fibers.py` checks all target fibers over \(\mathbb F_2\) and selected targets over \(\mathbb F_3\), as recorded in the associated output. The algebraic argument proves the noncentral formulas over every finite field; the script is a finite check. The earlier census [1] gives line aggregates at the zero quotient target; such aggregates recover the original central fibers but do not count prescribed noncentral targets in \(L\). Structural Hall-basis context is in [3]. This result is for the free rank-two class-four algebra, not arbitrary central quotients or higher classes. No universal priority claim is made.

## References

1. *A binary-quadratic census of central quotients of the rank-two free class-four Lie algebra*, Resultary 10559960a3e4 (2026-10-25), Finding, assumptions and adjoint-rank proof.
2. V. A. Roman'kov, *The commutator width of some relatively free Lie algebras and nilpotent groups*, Siberian Mathematical Journal 57 (2016), 679–695, DOI 10.1134/S0037446616040108.
3. P. Benito and D. de-la-Concepción, *A note on extensions of nilpotent Lie algebras of type 2*, arXiv:1307.8419, §2 (characteristic-zero context).
