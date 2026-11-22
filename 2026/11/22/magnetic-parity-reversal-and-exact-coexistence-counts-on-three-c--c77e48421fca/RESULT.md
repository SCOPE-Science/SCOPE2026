# Magnetic parity reversal and exact coexistence counts on three-colour Möbius ladders

## Finding

Let \(n\ge3\) and let \(M_{2n}\) be the Möbius ladder on vertices \(\mathbb Z/(2n)\mathbb Z\), with edges \(\{i,i+1\}\) and \(\{i,i+n\}\), indices modulo \(2n\). For three named spin colours \(\sigma_i\in\{0,1,2\}\), equal antiferromagnetic coupling \(J>0\), and a field \(H\ge0\) favouring colour zero, consider
\[
\mathcal H(\sigma)=J\sum_{\{i,j\}\in E(M_{2n})}\mathbf1_{\sigma_i=\sigma_j}-H\sum_i\mathbf1_{\sigma_i=0}.
\]
Write \(x=H/J\). The exact ground energy divided by \(J\) is
\[
\begin{aligned}
 n\text{ odd}:\quad &\min\{-nx,\,3n-2nx\},\\
 n\text{ even}:\quad &\min\{-(n-1)x,\,1-nx,\,3-(n+1)x,\,3n-2nx\}.
\end{aligned}
\]
Thus odd \(n\) has only the positive-field crossing \(x=3\), whereas even \(n\) has precisely three crossings \(x=1,2,3\). For odd \(n\), the unique positive-field ground sector for \(0<x<3\) has \(n\) vertices of colour zero and degeneracy \(2^{n+1}\). For even \(n\), the respective open plateaux \((0,1),(1,2),(2,3)\) have zero-colour populations \(n-1,n,n+1\) and degeneracies \(n2^{n-1},n2^n,n2^n\). At \(x=1,2\) (even \(n\)) the degeneracies are \(3n2^{n-1}\) and \(n2^{n+1}\), respectively. For every \(n\), the saturated phase \(x>3\) has one ground state.

At zero field the exact labelled degeneracy is
\[
 D_0(n)=3^n-1-2(-2)^n.
\]
At the saturation crossing \(x=3\), for both parities,
\[
 D_3(n)=\left(\frac{3+\sqrt{17}}2\right)^n+\left(\frac{3-\sqrt{17}}2\right)^n-(-2)^n.
\]
In particular, the critical residual entropy per site tends to \(\tfrac12\log((3+\sqrt{17})/2)\). The \(-(-2)^n\) term is the exact finite-size twisted-seam contribution in the hard-core critical manifold.

## Assumptions and scope

The graph is simple and cubic for every integer \(n\ge3\). All edges have identical positive exchange \(J\), colours are distinguished and labelled, and the external field is nonnegative, favouring exactly colour zero. The result concerns finite-graph zero-temperature energy minimizers and all their degeneracies. At \(H=0\) all proper three-colourings are included. The crossing values are exact, not thermodynamic phase-transition points.

## Proof

Write \(A=\{i:\sigma_i=0\}\), \(B=V\setminus A\), \(k=|A|\), and \(e(U)\) for the number of edges induced by \(U\). Let \(b(B)\) be the number of edges of \(B\) whose endpoints carry the same nonzero colour. The monochromatic-edge cost is \(c=e(A)+b(B)\). Cubic regularity gives
\[
 e(A)-e(B)=3(k-n),\qquad c=3(k-n)+e(B)+b(B).
\]
Consequently \(c\ge0\) and \(c\ge3(k-n)\), with equality in the second bound precisely when \(B\) is independent (because then \(b(B)=0\)).

View the ladder as \(n\) rungs, each containing two vertices. An independent set contains at most one vertex per rung. On consecutive nonempty rungs the chosen sides must alternate, while the Möbius closing bond reverses the side requirement. Therefore the independence number is \(n\) when \(n\) is odd (exactly two maximizers), and \(n-1\) when \(n\) is even (exactly \(2n\) maximizers: choose the sole empty rung and either of two alternating patterns). In the latter case no \(n\)-vertex subset is independent, so at \(k=n\) the monochromatic-edge cost is at least one. The lower bounds are attained as follows.

For odd \(n\), take \(A\) to be one of the two size-\(n\) independent sides and colour \(B\) arbitrarily with colours one or two. This yields cost zero and count \(2\cdot2^n\). For larger \(k\), take an independent \(B\) with \(2n-k\) vertices; this gives cost \(3(k-n)\), including saturation at \(k=2n\). The resulting energy envelope has the sole positive-field crossing \(x=3\).

For even \(n\), a size-\(n-1\) independent set \(A\) has a complement \(B\) inducing precisely three edges, by cubicity. The graph is triangle-free, so these three edges form a forest; its \(n+1\) vertices have \(n-2\) components and hence \(2^{n-2}\) proper assignments of the two remaining colours. There are \(2n\) choices of \(A\), giving \(n2^{n-1}\) cost-zero states at \(k=n-1\). At \(k=n\), cost one requires \(e(A)=e(B)=1\). Each of \(A,B\) then occupies exactly one vertex per rung: a double-occupied rung would force at least one more edge incident to its pair, since there is only one empty rung. Exactly one longitudinal constraint must fail; the defect can occupy any of \(n\) edges and has two side patterns, giving \(2n\) choices of \(A\). Each such \(B\) has exactly one induced edge and \(2^{n-1}\) proper two-colour assignments, hence \(n2^n\) states. For \(k=n+1\), choose the independent set \(B\) of size \(n-1\) in \(2n\) ways and assign its vertices either nonzero colour freely, giving \(n2^n\) states of cost three. For \(k\ge n+1\), independent \(B\) attains the bound \(c=3(k-n)\). These facts and \(c\ge0\) exclude any other lower-envelope segment and give crossings at \(1,2,3\); adding the counts of the coincident sectors yields the stated coexistence counts.

For \(x=3\), the identity for \(c\) shows that the energy differs from \(-3nJ\) by \(J(e(B)+b(B))\). Thus ground states are exactly arbitrary independent sets \(B\), with two choices of nonzero colour per vertex. Their number is the independence polynomial \(I(M_{2n};2)\). The three allowed rung states (empty, top occupied, bottom occupied) have transfer matrix
\[
 T=\begin{pmatrix}1&2&2\\1&0&2\\1&2&0\end{pmatrix}.
\]
The twisted seam exchanges the last two states, hence \(I(M_{2n};2)=\operatorname{tr}(T^nP)\), where \(P\) swaps top and bottom. The eigenvalues of \(T\) are \((3\pm\sqrt{17})/2\), both symmetric under the swap, and \(-2\), antisymmetric; the critical formula follows.

At \(x=0\), use the six rung states \((a,b)\) with \(a\ne b\) in \(\{0,1,2\}^2\), and the zero-one transfer \(Q_{(a,b),(c,d)}=\mathbf1_{a\ne c}\mathbf1_{b\ne d}\). In the simultaneous eigendecomposition with row-swap \(P\), the nonzero eigenvalues of \(Q\) are \(3\) (swap-even), \(1\) (swap-odd), and two copies of \(-2\) (swap-odd). Thus \(\operatorname{tr}(Q^nP)=3^n-1-2(-2)^n\), establishing the zero-field count.

## Verification

Run `python verify.py` with Python 3.10 or newer. The independent routine explicitly enumerates all \(3^{2n}\) labelled spin configurations for \(3\le n\le6\), and compares their minimum energies, populations and counts across eight rational field values. A separate nine-rung-state min-plus transfer independently checks the formula through \(n=17\). Independent-set counts are checked directly by subset enumeration at small size and by a signed transfer recurrence at larger size. The packaged execution returned `ALL_EXACT_CHECKS_PASSED 124`. These finite checks supplement the analytic all-size proof.

## Relationship to prior work

Shrock (1999) calculated zero-field chromatic polynomials of Möbius lattice strips and compared them with cyclic strips; the special case here at \(H=0\) is established prior work and is included only to close the finite-field census. Chang and Shrock (2015) calculated a generalized-field Potts partition function for **untwisted cyclic** square and triangular ladders, which is stronger than the corresponding cyclic-ladder field statement and is not claimed as new here. The Möbius-specific finite positive-field plateau classification and the signed critical finite-size count are the present statements. Classical Ising (two-state) Möbius-ladder field classifications, and generic independence-polynomial transfer methods, likewise do not give the three-state population split at \(H=J,2J\). The critical count is an evaluation of a hard-core independence polynomial; no novelty is claimed for the general independence-polynomial technique.

## Limitations

This theorem assumes uniform positive bonds, exactly three Potts colours and a single favoured colour. It does not treat negative fields, anisotropic couplings, finite-temperature singularities or the two-dimensional thermodynamic limit. The zero-field count and transfer mechanisms have predecessors. A historical equivalent computation of the twisted positive-field specialisation cannot be excluded without independent bibliographic audit.

## References

- R. Shrock, *T=0 Partition Functions for Potts Antiferromagnets on Moebius Strips and Effects of Graph Topology*, arXiv:cond-mat/9908323, first posted 1999-08-24. https://arxiv.org/abs/cond-mat/9908323
- S.-C. Chang and R. Shrock, *Exact Partition Functions for the q-State Potts Model with a Generalized Magnetic Field on Lattice Strip Graphs*, arXiv:1506.07392, first posted 2015-06-24. https://arxiv.org/abs/1506.07392
- S.-C. Chang and R. Shrock, *Transfer matrices for the zero-temperature Potts antiferromagnet on cyclic and Möbius lattice strips*, Physica A 346 (2005), 400–450. https://doi.org/10.1016/j.physa.2004.08.010
