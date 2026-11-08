# One-chord odd cycles: every singleton controls except the triangle midpoint

## Finding

For every odd integer \(n=2q+1\ge5\), form \(G_n\) by adding the edge \(\{0,2\}\) to the ordinary unweighted cycle \(C_n\) on \(\mathbb Z/n\mathbb Z\). Write \(L_n\) for the combinatorial Laplacian, and \(e_j\) for the standard coordinate vector. Then

\[
(-L_n,e_j)\text{ is controllable}\quad\Longleftrightarrow\quad j\ne1.
\]

The minimum dedicated-leader budget is one, and **exactly \(n-1\)** singleton leader sets attain it. The unique forbidden leader is the midpoint vertex \(1\) of the triangle created by the chord. Although adding one edge reduces the minimum dedicated-leader budget of the odd cycle from two to one, the graph has no one-vertex zero-forcing set.

## Assumptions and scope

The cycle vertices are labeled modulo an odd \(n\ge5\). Every present edge, including the new chord, has weight exactly one. The diagonal entries of \(L_n\) are unweighted degrees, the off-diagonal entries are negative one at adjacent vertices, and the dynamical convention is \(\dot x=-L_nx+e_ju\) with a real unconstrained scalar input. Controllability is Kalman controllability over \(\mathbb R\), equivalently the Popov--Belevitch--Hautus (PBH) eigenvector condition for this symmetric matrix. The claim is not a statement about arbitrary weights, even cycles, different chord lengths, or robust controllability.

## Proof

**1. Reflection sectors.** Reflection through the triangle midpoint is \(\sigma(j)=2-j\pmod n\). It fixes precisely the vertex \(1\), since \(n\) is odd, and commutes with \(L_n\). Put \(q=(n-1)/2\). The even reflection subspace has dimension \(q+1\), and the odd subspace has dimension \(q\). The chord adds the rank-one Laplacian \((e_0-e_2)(e_0-e_2)^\mathsf T\), supported entirely in the odd reflection sector.

**2. Unmodified even eigenmodes are visible at every vertex.** With origin at the fixed vertex \(1\), a basis of even-sector Laplacian eigenvectors is

\[
f_k(j)=\cos\!\left(\frac{2\pi k(j-1)}{n}\right),\quad
\lambda_k=2-2\cos\!\left(\frac{2\pi k}{n}\right),\quad k=0,\ldots,q.
\]

The eigenvalues are pairwise distinct. Moreover, \(f_k(j)\ne0\) for every integer \(j\): equality would force \(4k(j-1)=n(2s+1)\) for some integer \(s\), impossible because the left side is even and the right side odd.

**3. Odd Jacobi block and spectral separation.** In the orthonormal odd-sector basis \(v_r=(e_{1-r}-e_{1+r})/\sqrt2\), \(r=1,\ldots,q\), the Laplacian is the real symmetric Jacobi matrix

\[
J_q=\begin{pmatrix}
4&-1&&\\[-2pt]
-1&2&\ddots&\\
&\ddots&\ddots&-1\\
&&-1&3
\end{pmatrix},
\]

where for \(q=2\) the matrix has diagonal \((4,3)\) and one off-diagonal \(-1\). Without the chord this block is \(J_q^{(0)}=J_q-2e_1e_1^\mathsf T\). Its eigenvalues are exactly \(\lambda_1,\ldots,\lambda_q\). Since every eigenvector of an irreducible Jacobi matrix has a nonzero first coordinate, the positive rank-one update strictly interlaces them: if \(\mu_1<\cdots<\mu_q\) denote the eigenvalues of \(J_q\), then

\[
\lambda_1<\mu_1<\lambda_2<\mu_2<\cdots<\lambda_q<\mu_q.
\]

Thus the even and odd spectra are disjoint; the full Laplacian has simple spectrum.

**4. An odd eigenvector has no zero coordinate.** Nonzero eigenvectors of \(J_q\) have nonzero first and last entries by the tridiagonal recurrence. Suppose an interior entry \(y_r\) vanished with \(1<r<q\). The entries on both sides must be nontrivial, and the same eigenvalue \(\mu\) must occur in the leading block of size \(a=r-1\) and trailing block of size \(b=q-r\). Both \(a,b\) are positive. Let \(t=(2-\mu)/2\), with \(U_s\) the Chebyshev polynomial of the second kind, and \(U_{-1}=0\). Determinant recurrence gives

\[
P_a(\mu)=U_a(t)+2U_{a-1}(t),\qquad
R_b(\mu)=U_b(t)+U_{b-1}(t).
\]

A root of \(R_b\) has \(t=\cos(2\pi\ell/(2b+1))\), \(1\le\ell\le b\). Set \(z=\exp(2\pi i\ell/(2b+1))\), a root of unity of odd order \(d>1\). The equality \(P_a(\mu)=0\) implies

\[
F(z)=z^{2a+2}+2z^{2a+1}-2z-1=0.
\]

The integer cyclotomic polynomial \(\Phi_d\) would therefore divide \(F\). Reducing modulo two gives \(F(z)\equiv z^{2a+2}-1\). Because \(d\) is odd, its cyclotomic factors remain separable modulo two and their roots retain exact multiplicative order \(d\). Consequently \(d\mid(2a+2)\), whence \(d\mid(a+1)\). Substituting \(z^{a+1}=1\) into the original equation yields \(2(z^{-1}-z)=0\), so \(z^2=1\), contradicting odd \(d>1\). The shared eigenvalue is impossible, and every coordinate of every odd Jacobi eigenvector is nonzero.

**5. PBH and optimality.** At vertex \(j\ne1\), all even modes are nonzero by Step 2, and every odd mode has a nonzero value because \(j=1\pm r\) for a unique \(r\in\{1,\ldots,q\}\), so Step 4 applies. By PBH, \((-L_n,e_j)\) is controllable. At \(j=1\), all odd eigenvectors vanish by reflection, giving uncontrollability. Since every vertex degree in \(G_n\) is at least two, an initial single black vertex has at least two white neighbors, so no one-vertex set can be zero forcing. Finally, a nonempty dedicated-leader set is necessary for control; the controllable singletons attain the minimum.

## Verification

The standalone standard-library Python program `verify.py` constructs the exact integer Laplacian of each \(G_n\) and calculates modular ranks of each single-input Krylov matrix over the prime field with modulus \(1000000007\). For every odd \(n\) from \(5\) through \(35\), every \(j\ne1\) has full rank, and the forbidden midpoint has rank \((n+1)/2\), totaling **320** leader-position checks. These finite checks corroborate but do not replace the proof for all odd \(n\ge5\).

Reproduce with `python3 verify.py`; no third-party Python packages are needed. Exact integer-rank confirmations for sizes \(5,7,9,11,13,15\) were also carried out separately, but are not dependencies of the proof.

## Relationship to prior work

Monshizadeh, Zhang and Camlibel (2014) establish a zero-forcing characterisation for a qualitative family of graph-patterned matrices and examine paths, cycles and complete graphs. Their cycle comparison explains why an unchanged undirected cycle cannot be controlled from one vertex, but does not imply the present classification for the fixed Laplacian of a cycle with one added chord. In fact, our successful one-leader placements are not zero forcing. Hsu and Yang (2019) study controllability via interconnected path and antiregular graph structures rather than the present odd cycle with a chord; its construction does not directly imply this sharp forbidden-vertex rule. The result uses a Jacobi zero-free lemma and spectral interlacing to classify all the possible single-coordinate inputs.

## Limitations

The theorem applies only to the exact unweighted one-distance-two-chord family with odd order. It does not establish generic or robust controllability under arbitrary edge perturbations, nor quantify numerical conditioning or Gramian magnitudes. Published results not present in available searchable literature might already imply the theorem; this work has not received independent mathematical or publication-priority validation. Finite-rank experiments do not establish the all-order statement by themselves.

## References

1. N. Monshizadeh, S. Zhang and M. K. Camlibel, "Zero forcing sets and controllability of dynamical systems defined on graphs", arXiv:1403.4868v1, first publicly posted 19 March 2014, https://arxiv.org/abs/1403.4868 .
2. S.-P. Hsu and C.-J. Yang, "Generalising Laplacian controllability of paths", *IET Control Theory & Applications* (2019), https://doi.org/10.1049/iet-cta.2018.6214 .
