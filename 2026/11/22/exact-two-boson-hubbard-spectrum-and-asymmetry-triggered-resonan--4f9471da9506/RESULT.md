# Exact two-boson Hubbard spectrum and asymmetry-triggered resonances on complete bipartite networks

## Finding

Let \(K_{m,n}\) be the complete bipartite graph, with \(m,n\ge2\), and let two identical bosons hop along each graph edge with amplitude \(-1\), subject only to a uniform repulsive onsite Hubbard interaction \(U>0\). The *entire* two-particle characteristic polynomial factors into explicit cubic, quadratic and linear factors. Moreover, a symmetry-trivial energy and a nontrivial permutation multiplet coincide at positive energy for a positive interaction strength **if and only if one shore is strictly more than three times as large as the other**. If \(m>3n\), the unique such crossing is

\[
E_*=\sqrt{n(m-3n)},\qquad U_*=\frac{3n}{3n-2}\sqrt{n(m-3n)};
\]

its eigenspace has dimension exactly \(m\), and the two crossing positive interior eigenvalues exchange order. If \(n>3m\), exchange \(m\) and \(n\); otherwise no symmetry-trivial versus nontrivial-sector crossing occurs at any \(U>0\). This concerns interaction-tuned extra coincidences, not the ordinary symmetry-enforced multiplicities when the shore sizes agree.

## Assumptions and scope

The one-particle vertices are the disjoint union \(A\sqcup B\), with \(|A|=m\) and \(|B|=n\). The Hamiltonian acts on the exactly-two-boson Fock subspace and has the normalization

\[
H=-\sum_{a\in A,\,b\in B}(c_a^\dagger c_b+c_b^\dagger c_a)
+\frac U2\sum_{v\in A\sqcup B}N_v(N_v-1),\qquad U>0.
\]

There are no intersite density interactions, site energies, magnetic phases or hopping inside a shore. All eigenvalues are counted with their actual bosonic multiplicity. Put

\[
\begin{aligned}
F_0(x)&=x^3-Ux^2-4mnx+2U(2mn-m-n),\\
F_A(x)&=x^3-Ux^2-mnx+n(m-2)U\quad (m\ge3),\\
F_B(x)&=x^3-Ux^2-mnx+m(n-2)U\quad (n\ge3).
\end{aligned}
\]

For a size-two shore, define \(F_A(x)=x^2-Ux-2n\) when \(m=2\), and \(F_B(x)=x^2-Ux-2m\) when \(n=2\). Define

\[
z=1+(m-1)(n-1)+\mathbf1_{m\ge4}\frac{m(m-3)}2+\mathbf1_{n\ge4}\frac{n(n-3)}2.
\]

The exact characteristic polynomial, including every boundary size, is

\[
\boxed{\det(xI-H)=(x-U)x^z F_0(x)F_A(x)^{m-1}F_B(x)^{n-1}.}
\]

In particular, \(0\) has multiplicity exactly \(z\), and \(U\) has multiplicity exactly one unless other factors happen to vanish at the same value (which they do not for \(U>0\)).

## Proof

**Orthogonal decomposition.** The commuting shore-permutation group \(S_m\times S_n\) splits the two-boson space into states with both bosons in \(A\), both in \(B\), or one in each. Within same-shore states, separate doublons \(|aa\rangle\), unordered distinct pairs \(|ab\rangle\), and similarly on the other shore. The hopping sends a doublon to an opposite-shore pair with amplitude \(-\sqrt2\) in normalized Fock coordinates and a distinct same-shore pair to opposite-shore pairs with amplitude \(-1\) per moved endpoint.

The invariant fully symmetric block, in the ordered basis of uniform \(A\)-doublons, uniform \(B\)-doublons, uniform distinct \(A\)-pairs, uniform distinct \(B\)-pairs, and uniform cross-shore pairs, is the real symmetric arrowhead matrix whose four diagonal leaf entries are \(U,U,0,0\), central entry is \(0\), and leaf-to-central couplings are respectively

\[
-\sqrt{2n},\quad-\sqrt{2m},\quad-\sqrt{2n(m-1)},\quad-\sqrt{2m(n-1)}.
\]

Its characteristic polynomial, by the determinant of an arrowhead matrix, is \((x-U)xF_0(x)\). The common minus sign of each hopping can be changed by conjugating the cross-shore basis vector and has no spectral effect.

On the standard (sum-zero) representation of \(S_m\), repeated \(m-1\) times, the active block is the three-component arrowhead with leaf energies \(U,0\), central energy \(0\), and coupling magnitudes \(\sqrt{2n}\) and \(\sqrt{n(m-2)}\). Its determinant is \(F_A(x)\). For \(m=2\) the standard component of unordered distinct same-shore pairs does not exist, so the block is exactly two-by-two with characteristic polynomial \(x^2-Ux-2n\). The corresponding standard \(S_n\) blocks give \(F_B\). These statements follow directly from the incidence matrix \(R_m\) sending an unordered distinct \(A\)-pair to the sum of its two endpoint basis vectors. Its Gram matrix is

\[
R_mR_m^{\mathsf T}=(m-2)I_m+J_m,
\]

with eigenvalues \(2(m-1)\) on constants and \(m-2\) on the standard subspace; the cross-shore hopping contributes the opposite shore multiplicity \(n\) to squared couplings.

The remaining cross-shore \(S_m\)-standard tensor \(S_n\)-standard space has dimension \((m-1)(n-1)\) and is killed by hopping. For each shore of size at least four, the kernel of its unordered-pair incidence map contributes \(m(m-3)/2\) or \(n(n-3)/2\) zero modes: full row rank follows from the positive eigenvalues of the displayed Gram matrix for sizes at least three. One additional zero mode lies inside the symmetric block. Therefore the displayed factorization includes precisely \(z\) zeros. Counting the symmetric block, both standard families and these kernels gives the full \((m+n)(m+n+1)/2\)-dimensional Hilbert space; thus no spectral factors have been omitted.

**Root localization.** For \(m,n\ge2\), the three relevant cubics satisfy \(F(0)>0\), \(F(U)<0\), and have positive leading coefficient. Thus each cubic has exactly three distinct real roots, one in \(( -\infty,0)\), one in \((0,U)\), and one in \((U,\infty)\). The size-two quadratic has one root below zero and one strictly above \(U\), because \(x^2-Ux-2q\) has one negative root and one root greater than \(U\). The simple factor \(x-U\) shares no root with the cubics or quadratics; none of these factors vanishes at zero. Hence the only possible *new* symmetry-trivial versus standard coincidence is among the positive middle cubic roots.

**Crossing equation.** When \(m\ge3\), direct subtraction yields

\[
F_0(x)-F_A(x)=m\bigl[(3n-2)U-3nx\bigr].
\]

Any common root must consequently have \(x=c_nU\) where \(c_n=(3n-2)/(3n)\in(0,1)\). Substitution into \(F_A(x)=0\) reduces exactly to

\[
x^2=n(m-3n).
\]

Since \(x=c_nU>0\), this is possible precisely when \(m>3n\), yielding the unique pair \((U_*,E_*)\) above. Reversing shores proves the second case. The size-two definition is compatible with the *formal* identity \(xF_A(x)=x^3-Ux^2-mnx+n(m-2)U\) when \(m=2\); its quadratic roots are never in \((0,U)\), so cannot cause additional crossings. The analogous statement holds for \(n=2\).

The two standard cubics cannot have a common root when \(m\ne n\), since \(F_A(x)-F_B(x)=2U(m-n)\); the argument with the formal cubic also covers size-two boundaries. If \(m=n\), the standard factors coincide identically, a symmetry-enforced degeneracy, while neither can coincide with the symmetric cubic because the strict inequality \(m>3n\) fails. At \(m>3n\), the crossing is between one simple root of \(F_0\) and the \(m-1\) copies of one simple root of \(F_A\). All other blocks are separated there by their root ranges and polynomial identities, so the eigenspace dimension is precisely \(m\).

Finally, the symmetric middle eigenvalue behaves as \(U[1-(m+n)/(2mn)]+o(U)\), and the \(A\)-standard middle eigenvalue behaves as \(U[1-2/m]+o(U)\) as \(U\downarrow0\). The first lies below the second when \(m>3n\). As \(U\to\infty\), their respective limits are \(\sqrt{4mn-2(m+n)}\) and \(\sqrt{n(m-2)}\), the former strictly larger. Since their positive middle branches have exactly one intersection, the ordering reverses at \(U_*\).

## Verification

Two standalone Python 3 scripts use only the standard library. Run `python3 verify_characteristic.py` to reconstruct the exact full two-boson hopping matrices and independently compute their characteristic polynomials by Newton's trace identities for six small asymmetric and symmetric systems. Run `python3 verify_resonance.py` to check six threshold identities using exact rational arithmetic, and two exact modular ranks of the 55-state \(K_{8,2}\) Hamiltonian at \(U=3,E=2\), whose nullity is eight. These finite checks test the formula and normalizations but do not replace the all-size decomposition and algebraic proof.

## Relationship to prior work

Valiente and Petrosyan treat exact interacting two-boson states on one-dimensional periodic lattices [1]. Childs, Gosset and Webb analyze the general graph Bose-Hubbard Hamiltonian, proving a computational-complexity theorem [2]. Ymai and colleagues study an integrable tunneling Hamiltonian on complete bipartite networks [3], but their interaction is proportional to the *square of total shore-occupation imbalance*, not the sum of individual onsite pair penalties. In the two-particle sector their interaction assigns the same energy to two bosons on distinct same-shore sites and to a doublon, whereas the present Hamiltonian distinguishes them. Santos Filho's fragmented model [4] similarly couples onsite and nonlocal density interactions, and does not reduce to this onsite-only repulsive family with both shores nontrivial. None of these inspected statements entails the present factorization or its strict \(3:1\) resonance threshold. This is a comparison with identified sources, not a proof of absolute historical uniqueness.

## Limitations

Only the two-particle sector, real uniform cross-shore hopping, exactly onsite repulsion and \(m,n\ge2\) are covered. Particle-number extensions, graph perturbations, site disorder, attractive interactions, finite-temperature consequences and avoided crossings after symmetry breaking are not established. Previous exact results on quantum stars address a one-vertex shore; the present claim requires two nontrivial shores and is not inferred by simply identifying those models. Unindexed or inaccessible prior computations might have determined an equivalent spectrum; the literature comparison is bounded. The proof and checks have not been independently audited.

## References

[1] M. Valiente and D. Petrosyan, *Two-particle states in the Hubbard model*, arXiv:0805.1812, first public 2008-05-13, https://arxiv.org/abs/0805.1812.

[2] A. M. Childs, D. Gosset and Z. Webb, *The Bose-Hubbard model is QMA-complete*, arXiv:1311.3297, first public 2013-11-13, https://arxiv.org/abs/1311.3297.

[3] L. H. Ymai, A. P. Tonel, A. Foerster and J. Links, *Quantum integrable multi-well tunneling models*, arXiv:1606.00816, first public 2016-06-02, https://arxiv.org/abs/1606.00816.

[4] G. N. Santos Filho, *The exact solution of a fragmented Bose-Hubbard model and twisted models*, arXiv:2105.13447, first public 2021-05-27, https://arxiv.org/abs/2105.13447.
