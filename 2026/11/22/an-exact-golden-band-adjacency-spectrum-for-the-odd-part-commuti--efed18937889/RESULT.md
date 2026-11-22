# An exact golden-band adjacency spectrum for the odd-part commuting graph of the four-generator exterior algebra

## Finding

Let \(q\) be an odd prime power, let \(V=\mathbb F_q^4\), and put \(E=\bigwedge_{\mathbb F_q}V\). Form the **simple odd-part commuting graph** \(G_q\): its vertices are *all* \(q^8\) elements of \(E_{\mathrm{odd}}=V\oplus\bigwedge^3V\), including zero, and distinct vertices are adjacent when their ordinary associative-algebra products commute. This is an induced commutation graph, not the usual convention of removing central vertices.

Define
\[
L=q^3+q^2+q+1,\quad K=q^2+q+1,\quad s=(q-1)q^3,
\]
and the integer matrix
\[
Q_q=\begin{pmatrix}
0&q^4-1&q^4(q^4-1)\\
1&q^4-2&(q-1)q^4K\\
1&q^3-1&s-1
\end{pmatrix}.
\]
The **complete adjacency spectrum**, with multiplicities and algebraic multiplicities for the last three entries, is the multiset union
\[
\boxed{\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
-1&L(qs-2)\\
s-1&L(q-1)\\
\frac{s-2+s\sqrt5}{2}&L-1\\
\frac{s-2-s\sqrt5}{2}&L-1\\
\text{the three roots of }\det(tI_3-Q_q)&\text{their root multiplicities}
\end{array}}
\]
(repeated values across rows are combined). In particular **the adjacency matrix is nonsingular for every odd prime power**. The two golden-ratio bands appear with uniform multiplicity \(L-1\), while the large \(-1\) eigenspace has dimension \(L(qs-2)\).

## Assumptions and scope

All fields are finite of odd characteristic, including extension fields. Exterior multiplication uses the alternating relations \(v\wedge v=0\). The graph includes zero and all other odd elements, but has no loops. Ordinary algebra commutation of two odd elements is equivalent to their product being zero because \(xy=-yx\) and two is invertible. Spectral multiplicities refer to the real symmetric \(q^8\)-by-\(q^8\) adjacency matrix, so its eigenvalues are real. The matrix \(Q_q\) is an equitable quotient and is similar to a real symmetric matrix, although it is not itself symmetric.

## Proof

**1. The complete edge criterion.** Fix an exterior volume form and identify \(\bigwedge^3V\) with \(V^*\) through the perfect pairing \(v\wedge\alpha=\langle v,\alpha\rangle\omega\). Write an odd element as \((v,\alpha)\). For two odd elements \((v,\alpha)\) and \((w,\beta)\), their product vanishes precisely when
\[
v\wedge w=0,\qquad \langle v,\beta\rangle-\langle w,\alpha\rangle=0.\tag{1}
\]
This follows by separating its degree-two and degree-four components. No larger-degree terms exist.

**2. Cliques and projective incidence.** There are \(q^4\) vertices \(A_\alpha=(0,\alpha)\), and they form a clique. For any nonzero \(v\), write \(v=\rho u\), where \(\rho\in\mathbb F_q^*\), \(u\) is the unique representative of a projective line \(\ell\in\mathrm{PG}(3,q)\) normalized with first nonzero coordinate one. Set \(t=\langle u,\alpha\rangle/\rho\). Equation (1) says that two vertices with nonzero first coordinate commute exactly when their labels \((\ell,t)\) agree. Each of the \(qL\) possible labels supports a clique of
\[
(q-1)q^3=s
\]
vertices, and different such cliques have no edges between them. An \(A_\alpha\) vertex is adjacent to every member of the clique \((\ell,t)\) if and only if \(\langle\ell,\alpha\rangle=0\), independently of \(t\). The zero vertex is universally adjacent. This gives an exact graph blow-up description, including all loop corrections.

**3. Projective design identity.** The nonzero \(\alpha\) fall into \(L\) projective classes, each of \(q-1\) scalar multiples. For nonzero normalized projective classes of \(\alpha\) and \(\ell\), let \(N\) be their \(L\)-by-\(L\) incidence matrix, \(N_{\bar\alpha,\ell}=1\) precisely when \(\langle\ell,\alpha\rangle=0\). Each column has \(K\) incident hyperplanes; two distinct columns meet in \(q+1\) hyperplanes. Thus
\[
N^TN=q^2I_L+(q+1)J_L.\tag{2}
\]
On the constants its singular value is \(K\), and on the orthogonal complement of constants all singular values are \(q\), each with multiplicity \(L-1\).

**4. The forced scalar blocks.** The \(s-1\)-dimensional sum-zero subspace of each nonzero-first-coordinate clique has adjacency eigenvalue \(-1\); this contributes \(qL(s-1)\). On each nonzero \(\alpha\) projective class, the \(q-2\) scalar contrasts have eigenvalue \(-1\), contributing \(L(q-2)\). Indeed, every such contrast is annihilated by the cross-incidence block and the complete-clique adjacency is \(J-I\). Contrasts between the \(q\) distinct \(t\)-cliques having the same \(\ell\) are annihilated by the cross-incidence block and have adjacency eigenvalue \(s-1\), contributing \(L(q-1)\). Therefore the full \(-1\) multiplicity contributed here is \(L(qs-2)\).

**5. The golden bands and three-dimensional remainder.** After removing the contrast blocks, normalized class indicators leave one dimension for zero, \(L\) dimensions for nonzero \(\alpha\) projective classes, and \(L\) dimensions for projective \(\ell\)-classes, totaling \(2L+1\). The three global constant directions form an invariant subspace, and direct edge counts from Step 2 give its quotient matrix exactly \(Q_q\): rows and columns are, respectively, zero; all nonzero \(A_\alpha\); and all \(B\) vertices. This subspace contributes the three eigenvalues of \(Q_q\).

The remaining \(2(L-1)\) dimensions split into orthogonal pairs indexed by a singular basis of \(N\) perpendicular to constants. The diagonal adjacency actions are \(-1\) (on the nonzero-\(\alpha\) side) and \(s-1\) (on the \(\ell\) side). Their normalized off-diagonal coupling is
\[
q\sqrt{(q-1)qs}=s,
\]
by (2) and \(s=(q-1)q^3\). Thus each pair has the real symmetric matrix
\[
\begin{pmatrix}-1&s\\s&s-1\end{pmatrix},
\]
whose eigenvalues are \((s-2\pm s\sqrt5)/2\), giving multiplicity \(L-1\) apiece. All listed dimensions sum to \(q^8\), so there are no omitted eigenvalues.

**6. Nonsingularity.** The scalar eigenvalues \(-1\) and \(s-1\) are nonzero since \(s\ge54\). The determinant of the two-by-two block equals \(1-s-s^2\ne0\). Direct expansion of the three-by-three quotient gives
\[
\det(Q_q)=-(q-1)(q+1)(q^2+1)\bigl(q^8-2q^7+q^4-q^3-1\bigr).
\]
The final factor is \(q^7(q-2)+q^3(q-1)-1>0\) for every \(q\ge3\). Hence \(0\) is not an eigenvalue anywhere in the complete decomposition, proving nonsingularity.

## Verification

A standalone checker `artifacts/check_odd_commuting_spectrum.py` verifies the exterior multiplication criterion using actual degree-two and degree-four products on 30,000 reproducible pseudorandom pairs over each of the prime fields \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). It verifies the exact projective Gram identity (2) over all projective points for these fields, and directly checks that the finite-field graph class partition has the predicted sizes by exhaustively enumerating all \(3^8=6561\) odd elements at \(q=3\). It forms the compressed symmetric 201-by-201 adjacency matrix with clique blow-up weights and numerically compares every eigenvalue with the claimed list, with maximum discrepancy below \(4\times10^{-13}\). The output is in `artifacts/verification_output.txt`. Run `python3 artifacts/check_odd_commuting_spectrum.py` from the extracted package root; Python 3 and NumPy are required. These finite checks corroborate Steps 1–6 and do not replace the proof for all odd prime powers.

## Relationship to prior work

Domokos and Zubor, *Commutative subalgebras of the Grassmann algebra* (2014, especially Section 2), prove the general parity-based zero-product characterization and classify maximal commutative subalgebras through maximal square-zero subspaces. Their Proposition 2.1 and symplectic pairing background are prior mathematics, not claimed here as new. Bavula's 2007 work addresses derivations and the graded structure of Grassmann algebras. Neither gives an adjacency eigenvalue decomposition of the finite-field odd-part commuting graph.

Published calculations titled *All-arity commuting geometry of the four-generator exterior algebra* study commuting tuple varieties, their singular loci, finite-field point counts, and element adjoint ranks. *The Plücker-cone commutator fibers of the four-generator exterior algebra* enumerates all commutator values and fibers. Both concern this same exterior algebra and are pertinent precedent; their published full results were compared. Neither reports the graph adjacency spectrum, its golden-ratio bands, nor the nonsingularity theorem. Knowing total commuting pairs or aggregate commutator fibers does not itself determine the adjacency spectrum. The exact projective incidence matrix identity used here is classical. A possible implicit consequence of a more general graph-blow-up or association-scheme theorem remains a historical-priority risk.

## Limitations

The theorem is about the simple commutation graph **on all odd elements including zero**, not about a graph on all algebra elements or the conventional commuting graph with central vertices removed. It assumes exactly four exterior generators and odd characteristic; in characteristic two every pair of exterior elements commutes and this distinct spectral formula does not apply. The finite checks cover three prime fields and one complete compressed spectrum; extension fields and all larger orders are covered by the proof, not by enumeration. Broader literature on spectral blow-ups and projective incidence graphs may contain an equivalent formula under different terminology. No independent mathematical audit has been performed.

## References

1. M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, first submitted 2014-03-12, Sections 2 and 7, https://arxiv.org/abs/1403.2916 .
2. V. V. Bavula, *Derivations and skew derivations of the Grassmann algebras*, arXiv:0704.3850, first submitted 2007-04-29, https://arxiv.org/abs/0704.3850 .
3. *All-arity commuting geometry of the four-generator exterior algebra*, published scientific finding, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-all-arity-commuting-geometry-of-the-four-generator-exterior-alge--cbf96911f4e2 .
4. *The Plücker-cone commutator fibers of the four-generator exterior algebra*, published scientific finding, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-pluecker-cone-commutator-fibers-of-the-four-generator-exteri--ba4d5eb87025 .
