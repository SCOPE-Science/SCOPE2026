# Three–five resonances and dyadic transient clocks in generalized Petersen parity dynamics

## Finding

For every integer \(n\ge5\), let \(G_n=GP(n,2)\). The synchronous binary neighbor-sum map \(F_n:\mathbb F_2^{2n}\to\mathbb F_2^{2n}\) has precisely the following zero-primary Jordan blocks:

\[
J_{2h}(0)^{\oplus 2\mathbf1_{3\mid n}}\oplus J_h(0)^{\oplus 4\mathbf1_{5\mid n}},\qquad h=2^{\nu_2(n)}.
\]

The remaining \(R=2n-4h(\mathbf1_{3\mid n}+\mathbf1_{5\mid n})\) dimensions form an invertible invariant subspace. Set

\[
d_t=2\mathbf1_{3\mid n}\min(t,2h)+4\mathbf1_{5\mid n}\min(t,h),\quad t\in\mathbb Z_{\ge0}.\]

Then \(\dim\ker F_n^t=d_t\). The number of configurations with first-periodic-entry time zero is \(2^R\), and for each \(t\ge1\) the number with first-periodic-entry time exactly \(t\) is

\[
2^R\bigl(2^{d_t}-2^{d_{t-1}}\bigr).
\]

In particular the sharp maximum first-entry time equals \(2h\) when \(3\mid n\), equals \(h\) when \(3\nmid n\) and \(5\mid n\), and equals zero otherwise. Equivalently, the map is reversible exactly when \(\gcd(n,15)=1\). These threshold conditions concern *transient* dynamics, not the temporal periods on the eventual recurrent subspace.

## Assumptions and scope

Vertices are \(u_i,v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). The three neighbors of \(u_i\) are \(u_{i-1},u_{i+1},v_i\), and the three neighbors of \(v_i\) are \(v_{i-2},v_{i+2},u_i\). Every site is updated simultaneously to the sum of its three neighbors in \(\mathbb F_2\). All states are labelled, and a state first enters a periodic orbit at time \(t\) when \(t\) is the least nonnegative time for which its image is periodic. The hypothesis \(n\ge5\) avoids degeneracies of the graph definition. The indicator \(\mathbf1_P\) equals one when the property \(P\) holds and zero otherwise.

## Proof

1. Put \(\mathcal R_n=\mathbb F_2[x,x^{-1}]/(x^n-1)\). Grouping outer and inner configurations as a column in \(\mathcal R_n^2\), the update is multiplication by

\[
A(x)=\begin{pmatrix}z&1\1&z^2\end{pmatrix},\qquad z=x+x^{-1}.
\]

2. In characteristic two, \(\det A=z^3+1\) and

\[
x^3\det A=x^6+x^4+x^3+x^2+1=(x^2+x+1)(x^4+x^3+x^2+x+1).
\]

The displayed factors are distinct irreducible polynomials over \(\mathbb F_2\), with roots of orders three and five, respectively. Writing \(n=hm\) with \(m\) odd, \(x^n-1=(x^m-1)^h\). Thus a singular root occurs precisely when its order divides \(n\), and its local multiplicity is \(h\). At all other roots \(A\) is invertible.

3. Work after scalar extension to an algebraic closure, near a primitive third root \(\alpha\), in the local length-\(h\) ring \(K[s]/(s^h)\) where \(s=x-\alpha\). There \(z(\alpha)=1\), so \(\operatorname{tr} A=z+z^2\) is divisible by \(s\), and \(\det A\) has \(s\)-valuation exactly one: the factorization in step 2 has simple roots before truncation. Cayley–Hamilton gives \(A^2=(\operatorname{tr}A)A+(\det A)I\), hence \(A^{2h}=0\) on this full \(2h\)-dimensional local module. Moreover an off-diagonal entry is the unit \(1\), while the determinant is \(s\) times a unit. Elementary row-column reduction over the local principal ideal ring therefore gives Smith factors \(1,s\). The kernel of multiplication by \(A\) has dimension one over \(K\). A nilpotent operator on a \(2h\)-dimensional vector space with one-dimensional kernel has a single Jordan block \(J_{2h}(0)\). There are exactly two primitive third roots.

4. Near a primitive fifth root \(\beta\), the equation \(\beta^4+\beta^3+\beta^2+\beta+1=0\) implies \(z(\beta)^2+z(\beta)+1=0\). Thus \(\operatorname{tr} A(\beta)=z+z^2=1\) and \(\det A(\beta)=0\): the two residue-field eigenvalues are the distinct values zero and one. Since their difference is a unit, Hensel factorization of the degree-two characteristic polynomial and the Chinese remainder decomposition split the rank-two module over \(K[s]/(s^h)\) into two free invariant rank-one summands. The invertible eigenvalue is a unit, and the other eigenvalue has \(s\)-valuation one because their product is \(\det A\). Multiplication by \(s\) times a unit on a length-\(h\) local ring is exactly \(J_h(0)\). There are exactly four primitive fifth roots.

5. Since the calculated Jordan blocks are defined by kernel dimensions of powers, scalar extension preserves their multiplicities. Descending to \(\mathbb F_2\) yields exactly the claimed zero-primary partition. The Fitting decomposition separates the nilpotent part and the invertible recurrent part. A state first reaches the recurrent subspace at time at most \(t\) exactly when its nilpotent coordinate lies in \(\ker F_n^t\); there are \(2^{R+d_t}\) such states. Differencing successive counts proves the exact first-entry population formula. The maximum block length gives the asserted sharp entry time, and \(\ker F_n=0\) characterizes bijectivity.

## Verification

`checks/verify_petersen_powers.py` computes the actual binary adjacency matrix and independently tests the kernel dimension of every power through \(2h+2\) for each \(5\le n\le65\). `checks/verify_gcd_and_census.py` checks the determinant polynomial gcd condition for each \(5\le n\le500\) and explicitly follows all labelled states for \(5\le n\le8\), comparing each first-entry population with the closed formula. Both scripts use only Python's standard library and are included with captured outputs. These finite checks corroborate, but do not replace, the algebraic argument for arbitrary \(n\).

## Relationship to prior work

Martin–Odlyzko–Wolfram (1984) develop algebraic descriptions of additive cellular automata on periodic lattices, including transient and periodic structure. The polynomial representation and Fitting-type viewpoint are pre-existing methods; novelty is not claimed for them. Gera–Stănică, *The Spectrum of Generalized Petersen Graphs*, Theorem 2.4 and Section 3, gives the ordinary real adjacency spectrum for all generalized Petersen graphs, including \(GP(n,2)\). This does **not** determine the zero-primary Jordan partition over characteristic two, particularly when the circumference is even and the shift polynomial is inseparable. Frucht–Graver–Watkins (1971) introduced and studied the symmetry groups of this graph family, not parity dynamics. The results above isolate a three/five divisibility threshold and the exact dyadic lengths of nilpotent Jordan blocks for every circumference, rather than reporting a characteristic-zero spectrum. The possibility of an uncatalogued equivalent modular specialization remains.

## Limitations

The finding determines only the zero-primary Jordan blocks, recurrent-space dimension, and the distribution of first-periodic-entry times; it does not classify the nonzero-primary Jordan blocks or temporal primitive periods. The general methodology of spectral/local-ring reduction is established, and a later or inaccessible publication could contain an equivalent graph-specific specialization. Independence of review has not been established.

## References

- O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics 93 (1984), 219–258, DOI 10.1007/BF01223745. Accessible full text: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf.
- R. Gera and P. Stănică, *The Spectrum of Generalized Petersen Graphs*, manuscript dated September 5, 2010, particularly Lemma 2.1, Theorem 2.4 and Section 3. https://faculty.nps.edu/pstanica/research/SpectraGPG_AJC_r3.pdf.
- R. Frucht, J. E. Graver and M. E. Watkins, *The Groups of the Generalized Petersen Graphs*, Mathematical Proceedings of the Cambridge Philosophical Society 70 (1971), 211–218, DOI 10.1017/S0305004100049811 (accessible extract).
- S. Wolfram, *Cellular automata as models of complexity*, Nature 311 (October 4, 1984), 419–424, DOI 10.1038/311419a0 (public source-date anchor; accessible abstract).
