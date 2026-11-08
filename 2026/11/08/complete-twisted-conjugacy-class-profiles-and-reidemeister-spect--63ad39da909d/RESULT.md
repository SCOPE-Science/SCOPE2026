# Complete twisted-conjugacy class profiles and Reidemeister spectra of elementary generalized dihedral groups

## Finding
For every odd prime \(p\) and \(d\ge2\), the generalized dihedral group \(G=\mathbb F_p^d\rtimes C_2\) has the complete automorphism-wise twisted-conjugacy class-size distribution and Reidemeister spectrum described below. In particular,
\[
\operatorname{Spec}_R(G)=\left\{1+\frac{p^a+p^c}{2}:a,c\ge0,\ a+c\le d\right\},
\qquad
\left|\operatorname{Spec}_R(G)\right|=\left\lfloor\frac{(d+2)^2}{4}\right\rfloor.
\]
Each numerically allowed pair \((a,c)\) is realized. This is a full parametrized spectrum for a noncyclic odd abelian kernel, not merely a numerical bound.

## Assumptions and scope
Fix an odd prime \(p\), integer \(d\ge2\), and \(V=\mathbb F_p^d\). In additive notation let \(G=V\rtimes C_2\), with multiplication
\[
(v,\epsilon)(w,\delta)=(v+(-1)^\epsilon w,\epsilon+\delta\pmod 2).
\]
For any automorphism \(\varphi\) of \(G\), elements \(x,y\) are \(\varphi\)-twisted conjugate when \(y=gx\varphi(g)^{-1}\) for some \(g\in G\). Define \(R(\varphi)\) as the number of classes and \(\operatorname{Spec}_R(G)=\{R(\varphi):\varphi\in\operatorname{Aut}(G)\}\). Every element of \(V\) has odd order; every element outside \(V\) has order two. Therefore \(V\) is characteristic, and every automorphism uniquely satisfies
\[
\varphi(v,0)=(Lv,0),\qquad \varphi(0,1)=(b,1)
\]
for \(L\in\operatorname{GL}_d(\mathbb F_p)\) and \(b\in V\). Conversely, all such pairs give automorphisms. Set \(a=\dim_{\mathbb F_p}\ker(I-L)\), \(c=\dim_{\mathbb F_p}\ker(I+L)\), so \(a+c\le d\), since the two eigenspaces intersect trivially in odd characteristic.

## Proof
**1. Two invariant cosets.** Both the quotient map to \(C_2\) and the induced map of \(\varphi\) on that quotient are the identity. Hence a twisted-conjugacy orbit stays entirely within one of the rotation and reflection cosets.

**2. Translation orbits.** Twisted conjugation by \((u,0)\), for \(u\in V\), sends \((v,0)\) to \((v+(I-L)u,0)\) and \((v,1)\) to \((v+(I+L)u,1)\). Thus translation-suborbits are precisely the cosets of \(W_-=\operatorname{im}(I-L)\) and \(W_+=\operatorname{im}(I+L)\), each having sizes \(p^{d-a}\) and \(p^{d-c}\), respectively.

**3. The remaining involution.** Twisted conjugation by \((0,1)\) acts on the rotation labels by \(v\mapsto-v-b\), and on reflection labels by \(v\mapsto-v+b\). These induce affine involutions on \(V/W_-\) and \(V/W_+\), of cardinalities \(p^a\) and \(p^c\). An affine involution \(z\mapsto-z+\beta\) of any odd-order abelian group has exactly one fixed point, since multiplication by two is invertible. Every other point belongs to a two-element orbit. Consequently, for the rotations, there is exactly one whole-group orbit of \(p^{d-a}\) elements and \((p^a-1)/2\) whole-group orbits of \(2p^{d-a}\) elements. For reflections the corresponding profile is one orbit of \(p^{d-c}\) and \((p^c-1)/2\) orbits of \(2p^{d-c}\). Their total cardinality is \(2p^d\); all classes are accounted for. Summing their numbers gives
\[
R(\varphi)=\frac{p^a+1}{2}+\frac{p^c+1}{2}=1+\frac{p^a+p^c}{2}.
\]
The translation parameter \(b\) affects the unique fixed coset but not this profile.

**4. Realization of every allowed pair.** Fix \(a,c\ge0\) with \(a+c\le d\); put \(m=d-a-c\). We construct invertible \(L\) with geometric multiplicities \(a,c\) for eigenvalues \(1,-1\). If \(m=0\), take the diagonal matrix \(\operatorname{diag}(I_a,-I_c)\). If \(m\ge2\), append an \(m\times m\) companion matrix of any monic irreducible polynomial of degree \(m\) over \(\mathbb F_p\). Such a polynomial exists for every degree, and its constant coefficient is nonzero; its eigenvalues include neither \(1\) nor \(-1\) because its degree is at least two. If \(m=1\) and \(p\ge5\), append a scalar \(\lambda\in\mathbb F_p\setminus\{0,1,-1\}\). If \(m=1\) and \(p=3\), then \(a+c=d-1\ge1\). Start with the diagonal blocks for \(a\) copies of \(1\) and \(c\) copies of \(-1\), and replace one one-dimensional diagonal block for an eigenvalue \(\eta\in\{1,-1\}\) by the two-dimensional Jordan block \(\begin{pmatrix}\eta&1\\0&\eta\end{pmatrix}\). The dimension increases by one, whereas its \(\eta\)-eigenspace remains one-dimensional, preserving the desired kernel dimensions. This covers every \(p,d,a,c\) specified and every resulting automorphism can take \(b=0\).

**5. Number of distinct spectrum values.** Since \(p\ge3\), the base-\(p\) numeral of \(p^a+p^c\) determines the unordered exponent pair \(\{a,c\}\): if the two exponents coincide, one digit is two, and otherwise two digits are one. There is no carry. Thus different unordered admissible pairs give different Reidemeister numbers. Count pairs with \(0\le c\le a\), \(a+c\le d\):
\[
\sum_{c=0}^{\lfloor d/2\rfloor}(d-2c+1)
=\left\lfloor\frac{(d+2)^2}{4}\right\rfloor.
\]
This proves the exact spectrum and its cardinality.

## Verification
The accompanying standalone `verify_reidemeister.py` independently enumerates all invertible matrices for \((d,p)=(1,3),(1,5),(2,3),(2,5),(3,3)\), together with two inequivalent translation parameters in dimension two. It constructs actual twisted-conjugation orbits via group generators (rather than using the proof's quotient-orbit formula), compares all orbit-size multiplicities with the claimed formula, and compares all observed spectra with the predicted sets. It reports `VERIFY_OK` after 12,294 direct orbit-profile checks on 11,766 matrices. Its rank-one cases are boundary diagnostics; the stated unrestricted theorem begins at \(d=2\). This finite test is corroboration, not a substitute for the preceding proof.

## Relationship to prior work
Marius Tărnăuceanu, *The Reidemeister spectrum of ZM-groups*, arXiv:2511.09982v1 (first public November 13, 2025), classifies finite groups whose Sylow subgroups are cyclic; the groups here have noncyclic Sylow \(p\)-subgroups for \(d\ge2\), so are not covered by that statement. Pieter Senden, *The Reidemeister spectrum of split metacyclic groups*, arXiv:2109.12892v2, treats split metacyclic groups with cyclic kernel; these groups again lie outside that family. Sam Tertooy, *Algorithms for twisted conjugacy classes of polycyclic-by-finite groups II*, arXiv:2504.03596, gives a general effective method for obtaining class representatives, not this closed formula and full attainable spectrum. Senden and Tertooy, *Bi-twisted conjugacy in finite groups*, arXiv:2603.01679v2, proves general character and conjugacy-class counting identities; these give a framework for every finite group but do not state an explicit automorphism-by-automorphism class-size profile or attainable spectrum for this noncyclic family. Tărnăuceanu, *On a generalization of the Reidemeister spectrum of a finite group*, arXiv:2609.38366v1, extends ZM-group calculations to bi-twisted conjugacy, again retaining the cyclic-Sylow restriction. General finite-group character/fixed-class methods and odd-order inversion orbit counting are standard; the claimed contribution is the complete class-size profile, all attainable pairs, and the exact number of distinct values for the noncyclic elementary generalized dihedral family.

## Limitations
Only odd prime fields and kernel dimension at least two are asserted. In particular, the excluded group with \(p=3,d=1\) has spectrum \(\{3\}\), whereas the generic pair set would incorrectly include \(2\). There is no assertion about arbitrary finite abelian kernels with higher prime powers, even prime characteristic two, infinite groups, or independent validation. An older equivalent theorem under a character-theoretic or generalized-dihedral terminology may exist beyond the searched record.

## References
1. M. Tărnăuceanu, *The Reidemeister spectrum of ZM-groups*, arXiv:2511.09982v1 (2025-11-13), https://arxiv.org/abs/2511.09982.
2. P. Senden, *The Reidemeister spectrum of split metacyclic groups*, arXiv:2109.12892v2 (2022-02-11), https://arxiv.org/abs/2109.12892.
3. S. Tertooy, *Algorithms for twisted conjugacy classes of polycyclic-by-finite groups II*, arXiv:2504.03596v1 (2025-04-04), https://arxiv.org/abs/2504.03596.
4. P. Senden and S. Tertooy, *Bi-twisted conjugacy in finite groups*, arXiv:2603.01679v2 (2026-07-06), https://arxiv.org/abs/2603.01679.
5. M. Tărnăuceanu, *On a generalization of the Reidemeister spectrum of a finite group*, arXiv:2609.38366v1 (2026-09-29), https://arxiv.org/abs/2609.38366.
