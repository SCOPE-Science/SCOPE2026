# Characteristic-three Jordan blocks in Pappus independence homology

## Finding
Let \(P\) be the 18-vertex Pappus graph with vertices \(0,\ldots,17\), Hamiltonian edges \(\{i,i+1\}\) (indices modulo \(18\)), and LCF chords \(\{i,i+d_i\}\), where \((d_0,\ldots,d_{17})=(5,7,-7,7,-7,-5)^3\). Let \(X=\operatorname{Ind}(P)\). The automorphism \(r(i)=i+6\pmod{18}\) generates a cyclic group \(C_3\) of order three. Over \(\mathbb F_3\), define the indecomposable cyclic modules \(J_j=\mathbb F_3[t]/((t-1)^j)\), with \(r\) acting as multiplication by \(t\).

**Theorem.** The exact homology module is
\[
\widetilde H_4(X;\mathbb F_3)\cong J_3^{\oplus2}\oplus J_2^{\oplus2}.
\]
In particular, the \(r\)-fixed subspace is four-dimensional:
\[
\dim_{\mathbb F_3}\widetilde H_4(X;\mathbb F_3)^{\langle r\rangle}=4.
\]
This is strictly finer than the known characteristic-zero character \((10,-2,-2)\), which has only two invariant dimensions. Since \(\widetilde H_4(X;\mathbb Z)\) is free of rank ten and \(\widetilde H_3(X;\mathbb Z)=0\), this also gives the characteristic-three reduction of the integral homology action.

## Assumptions and scope
All simplicial faces are subsets of the stated eighteen labeled vertices spanning no graph edge; a face with \(k\) vertices has simplicial dimension \(k-1\). Coefficients for the new classification are **exactly** \(\mathbb F_3\), and the acting group is the specified \(C_3\), not the entire graph automorphism group. An oriented face is always written in increasing vertex order. The action on oriented chains includes the sign of the permutation necessary to sort its transformed vertices. The cyclic modules are modules over \(\mathbb F_3[C_3]\), where \((r-1)^3=0\).

## Proof
**1. Exact chain dimensions and homology concentration.** There are \(2597\) nonempty independent faces, whose counts by cardinality \(1,\ldots,9\) are
\[
(18,126,438,801,756,348,90,18,2).
\]
For the boundary \(d_4:C_4\to C_3\), the exact rank over \(\mathbb F_3\) is \(472\), and for \(d_5:C_5\to C_4\) it is \(274\), where \(C_4\) has \(756\) basis simplices. Hence
\[
\dim_{\mathbb F_3}H_4(X;\mathbb F_3)=756-472-274=10.
\]
The attached independent integral check constructs an acyclic Morse matching with \(1292\) matched face pairs and critical cells comprising one vertex, eleven four-cells and one five-cell. It computes the integral five-cell attaching vector in the critical four-cell coordinates to be \((0,0,0,0,0,0,-1,0,0,1,1)\), whose entries have greatest common divisor one. Thus \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{10}\), all other reduced integral homology groups vanish, and the universal coefficient theorem identifies the mod-three group with the integral reduction. Homotopy and rank are included to verify premises, not claimed as new.

**2. The finite-field action is computed on actual homology, not inferred from traces.** Let \(d_4\) and \(d_5\) be the oriented simplicial boundary matrices over \(\mathbb F_3\). Column elimination with accompanying change-of-basis vectors produces \(284\) independent vectors spanning \(\ker d_4\) (dimension \(756-472\)). The \(348\) columns of \(d_5\) span a \(274\)-dimensional subspace. Quotienting the cycle basis by that image leaves ten explicit homology classes. Both elimination stages are included as executable, exact arithmetic in `verify_mod3.py`, with no randomization or floating-point calculation.

For a sorted face \(\sigma=[v_0,\ldots,v_k]\), the chain map sends it to the face sorted from \((r(v_0),\ldots,r(v_k))\), multiplied by its sorting sign. The separate `verify_chain_signs.py` checks that this signed action commutes with each applicable boundary on **every** face of cardinalities four, five and six for \(r\) and \(r^2\). Transporting the ten homology basis classes through this chain map and reducing modulo boundaries yields an exact ten-by-ten matrix \(R\) over \(\mathbb F_3\). The verifier calculates
\[
\operatorname{rank}(R-I)=6,\qquad
\operatorname{rank}((R-I)^2)=2,\qquad
(R-I)^3=0.
\]
It independently calculates the matrix for \(r^2\), verifying that it equals \(R^2\), and verifies \(R^3=I\).

**3. Jordan multiplicities.** Write \(a_j\) for the number of size-\(j\) Jordan blocks for the eigenvalue one. Because \(R^3=I\) in characteristic three, no block exceeds size three. The ranks from the previous step give
\[
 a_3=\operatorname{rank}((R-I)^2)=2,\quad
 a_2=\operatorname{rank}(R-I)-2a_3=2,
\]
and
\[
 a_1=10-2\operatorname{rank}(R-I)+a_3=0.
\]
This proves the claimed decomposition, and \(a_1+a_2+a_3=4\) is the fixed-space dimension.

**4. Why the characteristic-zero result does not force the conclusion.** Over \(\mathbb Q\), the previously calculated module is \(2\mathbf1\oplus4\mathbb Q(\zeta_3)\), with character \((10,-2,-2)\). Both integral lattices
\[
L_A=\mathbb Z^{2}\oplus\mathbb Z[\zeta_3]^{4},\qquad
L_B=\mathbb Z[C_3]^{2}\oplus\mathbb Z[\zeta_3]^{2}
\]
have that *same rationalization*, but their mod-three Jordan types are respectively \(J_1^{\oplus2}\oplus J_2^{\oplus4}\) and \(J_3^{\oplus2}\oplus J_2^{\oplus2}\). Thus rational character data plus freeness and rank are insufficient to infer this theorem. The present result concerns the actual Pappus chain complex. It does **not** assert that its integral lattice is isomorphic to \(L_B\).

## Verification
Run `python3 verify_mod3.py`, `python3 verify_integral.py`, and `python3 verify_chain_signs.py` in the same directory. All use only Python 3's standard library. `verify_mod3.py` produces the exact 10-by-10 matrices for both nontrivial cyclic elements, verifies their multiplication, ranks, and Jordan multiplicities. `verify_integral.py` independently checks acyclicity of the full face-poset matching, its integral attaching-degree vector and torsion-free homology. `verify_chain_signs.py` checks signed cellular naturality by independently enumerating faces. Their actual stdout is recorded in `verification_output.txt`.

Finite enumeration is exhaustive **for this labeled 18-vertex graph** and proves no statement about arbitrary finite graphs. Calculations of modular ranks are performed over the prime field with no rational-to-modular rank assumption.

## Relationship to prior work
Taylan's January 27, 2015 archival work gives matching-tree and discrete-Morse techniques for graph independence complexes. Tsukuda's complete 2017 article gives nonequivariant homotopy descriptions for incidence-graph independence complexes. The previously indexed Pappus-specific calculation “Order-three symmetry on Pappus independence homology” proves the rational cyclic character \((10,-2,-2)\) and the known sphere-wedge homotopy type. A separate earlier complete rational graph-automorphism character is also known. Neither supplies a characteristic-three homology action or the nilpotent extension ranks. The explicit comparison of \(L_A\) and \(L_B\) above shows that the new modular statement is not a corollary of those characters or of the ordinary homotopy type. The present result specifically identifies the modular isomorphism class for the canonical period-six symmetry.

## Limitations
The claim is a one-graph, one-subgroup modular classification. It does not determine the integral \(\mathbb Z[C_3]\)-lattice, the modular action of all 216 graph automorphisms, or modular higher-degree homology of other graphs. Literature searches cannot eliminate unindexed equivalent results. There is no independent audit or external mathematical certification.

## References
- Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754, first submitted January 27, 2015, `https://arxiv.org/html/1501.06754v1`.
- Shuichi Tsukuda, *Independence Complexes and Incidence Graphs*, Contributions to Discrete Mathematics **12** (2017), 28–46, DOI `10.55016/ojs/cdm.v12i1.62277`.
- *Order-three symmetry on Pappus independence homology*, prior public research calculation, `https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31/RESULT.md`.
- A. E. Brouwer, *Pappus graph*, `https://aeb.win.tue.nl/graphs/Pappus.html` (graph identification and group order).
