# Regulus-rigid tight affine tomography on the finite-field determinant cone

## Finding

Let \(q\ge2\) be any prime power, \(F=\mathbb F_q\), and \(V=M_2(F)\). Equip \(V\) with \(Q(X)=\det X\) and its nondegenerate polar pairing
\[
 B(X,Y)=Q(X+Y)-Q(X)-Q(Y).
\]
There are exactly two families of maximal totally singular two-dimensional linear subspaces, parametrized by \(i,j\in\mathbb P^1(F)\):
\[
 L_i=\{u_i z^{\mathsf T}:z\in F^2\},\qquad
 R_j=\{zv_j^{\mathsf T}:z\in F^2\},
\]
where \(u_i,v_j\ne0\) represent the corresponding projective points. For each selected direction \(D\), the **unnormalized affine plane-sum** \(T_Df\) consists of the \(q^2\) values \(\sum_{y\in x+D}f(y)\), one per coset \(x+D\). Weights are scalars \(w_i,v_j\ge0\), not all zero, attached to complete direction views, and the weighted transform stacks \(\sqrt{w_i}T_{L_i}\) and \(\sqrt{v_j}T_{R_j}\). Write zero for every unselected weight.

**Complete spectrum.** With standard counting \(\ell^2\)-inner products on functions and the direct sum of view data, the normal operator \(T^*T\) has Fourier eigenvalues
\[
\begin{array}{ll}
q^2\left(\sum_i w_i+\sum_jv_j\right) &\text{at zero frequency, multiplicity }1;\\[2pt]
q^2(w_i+v_j)&\text{at each nonzero frequency in }L_i\cap R_j,\text{ multiplicity }q-1\text{ per pair }(i,j);\\[2pt]
0&\text{on the invertible-matrix frequencies, multiplicity }(q^2-1)(q^2-q).
\end{array}
\]
Coincident values are combined by adding multiplicities. This is a statement for *arbitrary nonnegative view weights*, including zero-weight directions and even characteristic.

Let \(\mathcal H\) be the \((q-1)(q+1)^2\)-dimensional space of complex functions on \(V\) with vanishing mean and Fourier transform supported on the nonzero determinant-zero cone. If \(A\) and \(C\) are the sets of positively weighted left and right directions respectively, and \(a=|A|\), \(c=|C|\), then
\[
 \dim\ker(T|_{\mathcal H})=(q-1)(q+1-a)(q+1-c).
\]
Thus the restricted transform is injective **if and only if** one full ruling is present. Exactly \(q+1\) directions suffice, and the only injective designs using exactly that number are the two full rulings.

**Tightness rigidity and a nonmonotone conditioning effect.** Among all injective designs with strictly positive weights on their selected views, \(T|_{\mathcal H}\) is a tight frame exactly when the selected directions are (i) the complete left ruling with constant weights, (ii) the complete right ruling with constant weights, or (iii) both complete rulings, with weights constant separately in each ruling. For unit weights on a complete left ruling, every singular value on \(\mathcal H\) equals \(q\). Adding any proper, nonempty subset of right-ruling directions changes the sharp condition number from \(1\) to \(\sqrt2\); adding the entire right ruling restores it to \(1\). The same holds with left and right exchanged.

**Reconstruction.** A full ruling \(A=\mathbb P^1(F)\) with unit weights obeys \(T_A^*T_A=q^2 I\) on \(\mathcal H\), so \(f=q^{-2}T_A^*T_Af\) there. More generally, every \(f\) whose Fourier support lies in the complete determinant-zero cone (including zero) satisfies
\[
 f=q^{-2}T_A^*T_A f-q\,\overline f\,\mathbf1,
 \qquad \overline f=q^{-4}\sum_{X\in V}f(X).
\]
The mean \(\overline f\) is itself determined from any one selected complete direction view.

## Assumptions and scope

The field \(F\) is any finite field, including characteristic two and nonprime extension fields. Signals are complex-valued; \(\mathcal H\) is defined using the additive characters \(\chi_\xi(X)=\psi(B(\xi,X))\) for a fixed nontrivial additive character \(\psi:F\to\mathbb C\). The input and output norms are ordinary unnormalized counting norms. Every direction view contains *all affine cosets* of its linear plane, with a single nonnegative weight for the whole view; arbitrary erasures of individual cosets are not covered. The theorem concerns recovery on the intrinsic recoverable frequency cone \(\{\det\xi=0\}\), not recovery of arbitrary functions on \(F^4\); invertible-frequency functions are invisible to all of these views.

## Proof

**1. Two generator families and their incidence.** Every nonzero singular \(2\)-by-\(2\) matrix \(X\) has rank one and admits an outer-product decomposition \(X=uv^{\mathsf T}\) with nonzero \(u,v\in F^2\). Its column line \([u]\) and row line \([v]\) are determined uniquely. Hence \(X\in L_i\) if and only if \(i=[u]\), and \(X\in R_j\) if and only if \(j=[v]\). The intersection \(L_i\cap R_j=\{tuv^{\mathsf T}:t\in F\}\) has \(q\) elements, while distinct planes in the same family intersect only at zero. Every two-dimensional linear subspace on which the determinant vanishes is one of these planes: if it contains independent rank-one matrices \(uv^{\mathsf T}\) and \(ab^{\mathsf T}\), then the determinant of their sum is zero exactly when either \(u,a\) are proportional or \(v,b\) are proportional. Thus its generators share a column line or a row line. There are \(q+1\) choices in each family, and the nonzero determinant-zero frequencies number \((q-1)(q+1)^2\).

**2. Self-orthogonality, in every characteristic.** Since \(Q|_D=0\) on each generator plane \(D\), polarization gives \(B(D,D)=0\). In coordinates \(X=(a,b;c,d)\), \(B(X,Y)=ad'+a'd-bc'-b'c\), which is nondegenerate for every characteristic. As \(\dim D=2=\frac12\dim V\), each generator satisfies \(D^{\perp_B}=D\).

**3. Fourier diagonalization.** For a plane \(D\), let \(T_D f(x+D)=\sum_{z\in D}f(x+z)\). Its adjoint satisfies
\[
 (T_D^*T_D f)(x)=\sum_{z\in D}f(x+z).
\]
Character orthogonality gives \(T_D^*T_D\chi_\xi=q^2\chi_\xi\) if \(\xi\in D^{\perp_B}=D\), and zero otherwise. Summing the weighted views yields the displayed complete spectrum. Each pair \((i,j)\) contributes the \(q-1\) nonzero elements of \(L_i\cap R_j\); there are \((q^2-1)(q^2-q)\) invertible frequencies. This checks the total eigenvalue multiplicity \(q^4\).

**4. Kernel, uniqueness, and minimum number of views.** A pair frequency \((i,j)\) has eigenvalue zero exactly when \(w_i=v_j=0\). Thus the restricted kernel is spanned by the \(q-1\) characters at each pair outside the chosen row set \(A\) and chosen column set \(C\); the kernel dimension is \((q-1)(q+1-a)(q+1-c)\). Zero kernel requires \(a=q+1\) or \(c=q+1\). Therefore any injective design uses at least \(q+1\) views and at equality it must consist of one complete ruling, providing both minimality and uniqueness.

**5. Tightness and condition numbers.** The squared singular values on \(\mathcal H\) are \(q^2(w_i+v_j)\), so tightness is equivalent to all \(w_i+v_j\) being equal and positive over the full \((q+1)\)-by-\((q+1)\) grid. An injective design contains a full ruling. If the other ruling is partly but not entirely present, comparing columns with a zero and with a positive weight precludes equality. If the other ruling is absent, all weights in the full ruling must coincide. If both are full, subtracting two grid entries along one row/column forces constancy of the weights within each ruling. Conversely all listed patterns yield a positive constant sum. For unit weights and exactly \(1\) through \(q\) opposite directions, the attained positive squared singular values are \(q^2\) and \(2q^2\), giving \(\sqrt2\); they coincide for zero or \(q+1\) opposite directions.

**6. Inversion.** For one complete ruling the normal operator acts as \(q^2(q+1)\) on constants, as \(q^2\) on the nonzero determinant cone, and as zero on invertible frequencies. The reconstruction statements follow by Fourier expansion. For any fixed plane \(D\), summing \(T_D f\) over its \(q^2\) cosets recovers \(\sum_X f(X)\), so the mean is observable.

## Verification

The standalone checker `null_regulus_checker.py` builds the two families of affine planes directly, constructs the complete incidence matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the last via polynomial-basis extension-field arithmetic), and diagonalizes the exact integer normal matrices. It checks four unweighted selection designs and three irregular positive-weight selections for each field. Every computed eigenvalue is within \(10^{-7}\) of an integer and its complete multiplicity agrees with the displayed formula. It also checks rank-one geometry and total isotropy directly. Run with `python null_regulus_checker.py`; the successful final marker is `NULL_REGULUS_INCIDENCE_SPECTRUM_CHECKS_PASS`. These finite tests corroborate, but do not replace, the proof for arbitrary prime powers.

## Relationship to prior work

Fourier slicing for finite affine \(k\)-plane sums and the classical geometry of a doubly ruled determinant quadric are established ingredients. Koh (2012) studies sharp \(L^p\)-mapping estimates for the **full** affine X-ray and Radon transforms, not weighted arbitrary-subset generator-plane tomography. Carbery–Stones–Wright (2008) study finite-field averages and maximal estimates rather than the determinant-cone partial-view spectrum. Feldman–Grinberg (2017) study projective point-to-line transforms and projective admissible line complexes; they use doubly ruled quadrics but neither their signal space nor their data geometry is the present affine function-to-two-plane problem. Scarabotti (2003) develops finite Radon harmonic analysis in multiplicity-free permutation modules; only its abstract was accessible, so implicit broader coverage was not excluded. The present claim is the combined complete weighted spectrum, exact partial-view kernel, unique minimal full-ruling designs, tightness rigidity, and the nonmonotone unweighted condition number. It is not a claim to have invented Fourier slicing or the two-regulus geometry.

## Limitations

No independent audit or external originality certification has been performed. This result neither provides information about arbitrary erasures of cosets nor reconstructs the invertible-frequency part of an unrestricted signal. It does not claim the weighted condition-number optimum under extra constraints on positive weights; strictly positive but arbitrarily small added-view weights may make the condition number approach one without attaining tightness. An uninspected broad finite Radon paper or earlier treatment of this exact determinant-cone sampling model could affect historical priority. The computations cover only three field sizes; the universal theorem rests on the explicit proof.

## References

1. Doowon Koh, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields*, first arXiv posting 6 September 2012, arXiv:1209.1215, https://arxiv.org/abs/1209.1215.
2. A. Carbery, B. Stones, J. Wright, *Averages in vector spaces over finite fields*, Math. Proc. Cambridge Philos. Soc. 144 (2008), 13–27, DOI:10.1017/S0305004107000680.
3. D. V. Feldman and E. L. Grinberg, *Admissible Complexes for the Projective X-Ray Transform over a Finite Field*, first arXiv posting 20 July 2017, arXiv:1707.06695, https://arxiv.org/abs/1707.06695.
4. F. Scarabotti, *Fourier Analysis of a Class of Finite Radon Transforms*, SIAM J. Discrete Math. 16 (2003), 545–554, DOI:10.1137/S0895480102416398 (abstract accessible; full text not inspected).
5. E. D. Bolker, *The finite Radon transform*, Contemporary Mathematics 63 (1987), 27–50 (classical background; full text not inspected).
