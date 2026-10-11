# Exact factor two for the canonical \(C(K_L)\) representation of \(\operatorname{FBL}\langle L\rangle\)

## Finding
Let \(L\) be a nontrivial bounded distributive lattice with minimum \(m\) and maximum \(M\), and let \[K_L=\{x^*\in L^*: \max(|x^*(m)|,|x^*(M)|)=1\}.\] For the canonical restriction lattice isomorphism \(\Phi_L:\operatorname{FBL}\langle L\rangle\to C(K_L)\), \(\Phi_L(f)=f|_{K_L}\), one has \(\|\Phi_L\|=1\) and \(\|\Phi_L^{-1}\|=2\). Equivalently, \[\|f|_{K_L}\|_\infty\le \|f\|\le 2\|f|_{K_L}\|_\infty\] for every \(f\), and the constant \(2\) is attained by the canonical strong unit \(u=|\delta_m|\vee|\delta_M|\), for which \(\|u\|=2\) and \(\|u|_{K_L}\|_\infty=1\).

Thus the factor \(2\) in the known canonical \(C(K_L)\) representation is not merely a uniform upper estimate: it is the exact inverse norm of the canonical restriction map for every nontrivial bounded distributive lattice.

## Assumptions and scope
Let \(L\) be a distributive lattice with minimum \(m\), maximum \(M\), and at least two elements. Write \(L^*\) for the lattice homomorphisms from \(L\) to \([-1,1]\). The functional model of \(\operatorname{FBL}\langle L\rangle\) consists of positively homogeneous functions on \(L^*\) with norm
\[
 \|f\|=\sup\left\{\sum_{i=1}^n |f(x_i^*)|:
 \sup_{x\in L}\sum_{i=1}^n|x_i^*(x)|\le1\right\}.
\]
The compact set
\[
 K_L=\{x^*\in L^*: \max(|x^*(m)|,|x^*(M)|)=1\}
\]
is the canonical compactum used in the known lattice isomorphism with \(C(K_L)\). The result concerns this canonical restriction representation; it does not assert that the Banach--Mazur lattice distance to all possible \(C(K)\)-representations is exactly \(2\).

## Proof
For \(x^*\in L^*\), order preservation and \(m\le x\le M\) give
\[
 x^*(m)\le x^*(x)\le x^*(M)\qquad(x\in L).
\]
Hence
\[
 r(x^*):=\sup_{x\in L}|x^*(x)|
 =\max\{|x^*(m)|,|x^*(M)|\}.
\]

Take an admissible finite family \(x_1^*,\ldots,x_n^*\) in the defining norm, and put \(r_i=r(x_i^*)\). If \(r_i=0\), then \(x_i^*=0\). If \(r_i>0\), then
\[
 y_i^*=r_i^{-1}x_i^*\in K_L.
\]
Positive homogeneity therefore gives
\[
 |f(x_i^*)|=r_i|f(y_i^*)|\le r_i\|f|_{K_L}\|_\infty.
\]
Moreover,
\[
 r_i\le |x_i^*(m)|+|x_i^*(M)|.
\]
Admissibility, evaluated separately at \(m\) and \(M\), yields
\[
 \sum_i|x_i^*(m)|\le1,
 \qquad
 \sum_i|x_i^*(M)|\le1,
\]
so \(\sum_i r_i\le2\). Consequently
\[
 \|f\|\le2\|f|_{K_L}\|_\infty.
\]
Conversely, every \(y^*\in K_L\) is itself admissible as a one-element family because \(r(y^*)=1\). Thus
\[
 \|f|_{K_L}\|_\infty\le\|f\|.
\]
This proves \(\|\Phi_L\|\le1\) and \(\|\Phi_L^{-1}\|\le2\).

It remains to prove sharpness. Since \(L\) is nontrivial, \(M\nleq m\). The separation lemma for distributive lattices supplies a lattice homomorphism \(q\in L^*\) satisfying
\[
 q(m)=0,
 \qquad q(M)=1,
 \qquad 0\le q(x)\le1\quad(x\in L).
\]
Set \(p=q-1\). Because translation by \(-1\) is increasing and preserves minimum and maximum in the real chain, \(p\) is also a lattice homomorphism \(L\to[-1,1]\). For every \(x\in L\),
\[
 |q(x)|+|p(x)|=q(x)+1-q(x)=1,
\]
so the pair \((q,p)\) is admissible in the free norm.

Now let
\[
 u=|\delta_m|\vee|\delta_M|.
\]
Then \(u(q)=u(p)=1\), hence the defining norm gives \(\|u\|\ge2\). The upper estimate already proved gives \(\|u\|\le2\), because \(u=1\) on \(K_L\). Therefore
\[
 \|u\|=2,
 \qquad
 \|u|_{K_L}\|_\infty=1.
\]
Thus \(\|\Phi_L^{-1}\|=2\). Finally, \(p\in K_L\) and \(\delta_m(p)=-1\), while the free norm always has \(\|\delta_m\|\le1\); hence \(\|\delta_m\|=\|\delta_m|_{K_L}\|_\infty=1\), proving \(\|\Phi_L\|=1\).

## Verification
The upper inequality was reconstructed directly from the published defining norm rather than inferred from an abstract renorming theorem. The sharpness witness uses only the published lattice-separation lemma and the explicitly checked companion homomorphism \(p=q-1\). The admissibility identity \(|q(x)|+|p(x)|=1\) is exact for every \(x\in L\), so the lower bound \(2\) is not numerical or asymptotic.

The trivial one-point lattice is excluded: there \(m=M\), the canonical space is one-dimensional, and the corresponding factor is \(1\), so nontriviality is essential to the universal sharpness statement.

## Relationship to prior work
Avilés, Martínez-Cervantes, Rodríguez Abellán and Rueda Zoca proved that when a lattice has a minimum and maximum, \(\operatorname{FBL}\langle L\rangle\) is canonically lattice isomorphic to \(C(K_L)\) with distortion at most \(2\). Their proof obtains the upper bound from \(\|u\|\le2\), where \(u=|\delta_m|\vee|\delta_M|\).

Ben Rjeb and Tradacete's 2026 paper recalls the same compactum and strong unit, gives the exact functional norm formula, and proves a separation lemma producing a \([0,1]\)-valued lattice homomorphism that separates two ordered positions. Combining these ingredients with the companion homomorphism \(q-1\) yields an exact two-functional norm witness. In the inspected statements and proofs, neither source identifies the canonical inverse norm as exactly \(2\) for every nontrivial bounded distributive lattice.

## Limitations
The theorem is an optimality statement for the canonical restriction representation \(\Phi_L\). It does not rule out a different lattice isomorphism from \(\operatorname{FBL}\langle L\rangle\) to some other \(C(K)\)-space with smaller distortion. The closest 2022 theorem already gives the upper constant \(2\), so the originality lies specifically in the universal sharpness and exact strong-unit norm. Although targeted implication-level searches and inspection of the relevant theorem proof found no such sharpness statement, an equivalent observation could exist elsewhere under different terminology.

## References
1. A. Ben Rjeb and P. Tradacete, *On the free Banach lattice generated by a lattice*, arXiv:2604.27841, first posted 30 April 2026; Banach J. Math. Anal. 20 (2026), article 48, DOI 10.1007/s43037-026-00512-2.
2. A. Avilés, G. Martínez-Cervantes, J. D. Rodríguez Abellán, and A. Rueda Zoca, *Free Banach lattices generated by a lattice and projectivity*, arXiv:2103.08170; Proc. Amer. Math. Soc. 150 (2022), 2071--2082, DOI 10.1090/proc/15802.
