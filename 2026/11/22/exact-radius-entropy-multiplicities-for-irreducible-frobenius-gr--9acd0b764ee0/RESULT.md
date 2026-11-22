# Exact radius-entropy multiplicities for irreducible Frobenius group cellular automata

## Finding

Fix distinct primes \(p,q\) and an integer \(d\ge1\). Let \(A\in\mathrm{GL}_d(\mathbf F_p)\) have prime order \(q\) and act irreducibly and nontrivially on \(V=\mathbf F_p^d\), and put \(G=V\rtimes_A C_q\). Then \(d=\operatorname{ord}_q(p)\), and \(G\) has order \(p^dq\). Every continuous, shift-commuting *group endomorphism* \(F:G^{\mathbf Z}\to G^{\mathbf Z}\) is exactly one of the following disjoint types (the zero map belongs to type (B)):

(A) A coordinate shift composed with a coordinatewise group automorphism: \(F(x)_n=\gamma(x_{n+j})\), \(\gamma\in\operatorname{Aut}(G)\), \(j\in\mathbf Z\). Its topological entropy is \(|j|\log(p^dq)\).

(B) A quotient-field linear rule with a common output complement: \(F(x)_n=\iota(\sum_j a_j\pi(x_{n+j}))\), where \(\pi:G\to C_q\cong\mathbf F_q\) is the canonical quotient, \(\iota:C_q\hookrightarrow G\) embeds one complement, and \(P(z)=\sum_j a_jz^j\in\mathbf F_q[z,z^{-1}]\) has finite support. For \(P\ne0\), its entropy equals \(w(P)\log q\), where \(w(P)=\max(0,\max\operatorname{supp}P)-\min(0,\min\operatorname{supp}P)\); for \(P=0\), entropy is zero. The complement is uniquely determined by a nonzero map.

For centered radius \(R\ge1\), consider the group endomorphism cellular automata whose outputs at \(n\) depend only on \(x_{n-R},\ldots,x_{n+R}\). Set \(v=p^d\) and \(a=v d(v-1)=|\operatorname{Aut}(G)|\). Their **complete entropy spectrum** is

\[
\{k\log q:0\le k\le2R\}\ \cup\ \{k\log(vq):0\le k\le R\}.
\]

The **number of distinct cellular automata at each entropy** is exactly

\[
N(0)=1+v(q-1)+a,\qquad N(k\log(vq))=2a\quad(1\le k\le R),
\]
\[
N(k\log q)=v\left[2\mathbf1_{k\le R}(q-1)q^k+c_R(k)(q-1)^2q^{k-1}\right],\quad 1\le k\le2R,
\]

where \(c_R(k)=\max(0,\min(R,k-1)-\max(1,k-R)+1)\). The two sets of positive entropy levels are disjoint. Summing all levels yields exactly

\[
1+v(q^{2R+1}-1)+(2R+1)a.
\]

More generally, with any prescribed \(r\ge1\) distinct input sites, the number of group-homomorphic local rules is \(1+v(q^r-1)+ra\).

## Assumptions and scope

All shifts are two-sided, over \(\mathbf Z\), with the product topology. Entropy is topological entropy of the **time-iteration map** \(F\), not entropy of its image as a spatial subshift. The rule is required to be a group homomorphism with respect to pointwise multiplication; arbitrary nonlinear cellular automata are excluded. The irreducible, faithful cyclic prime-complement hypothesis is essential for the stated normal-subgroup and commuting-image classification. The centered radius bound allows coefficients at any subset of \([-R,R]\), and no representation is double-counted by padding a local rule with unused coordinates.

## Proof

**1. Group structure and normal subgroups.** Irreducibility of the cyclic prime-order action gives \(\mathbf F_p[A]\cong\mathbf F_{p^d}\), so \(d=\operatorname{ord}_q(p)\). Every nonidentity power of \(A\) is fixed-point-free on \(V\). The centralizer \(C_G(V)=V\), and \(Z(G)=\{1\}\). If \(N\triangleleft G\) is nontrivial, then either \(N\cap V\ne0\), hence \(V\le N\) by irreducibility, or \(N\cap V=0\), hence \([N,V]\le N\cap V=0\), forcing \(N\le C_G(V)=V\), a contradiction. Thus the normal-subgroup lattice is exactly \(\{1\},V,G\).

Every group endomorphism \(e:G\to G\) is consequently trivial, an automorphism, or factors through \(\pi:G\to C_q\) with image a subgroup of order \(q\). The latter subgroups are the \(v\) conjugate complements, each self-centralizing; each complement supports \(q-1\) nontrivial quotient maps. The normalizer of \(\langle A\rangle\) in \(\mathrm{GL}_d(\mathbf F_p)\) consists of semilinear multipliers of order \(d(v-1)\): the image exponent in \(A\mapsto A^k\) must be one of the \(d\) Frobenius conjugates, and for each exponent there are \(v-1\) field multipliers. A complement generator can additionally be sent to any of \(v\) conjugate complement representatives. Therefore \(|\operatorname{Aut}(G)|=vd(v-1)\).

**2. Local-rule dichotomy.** By locality and the group-homomorphism property, the local map \(G^S\to G\) is the product, in any fixed order, of homomorphisms \(e_j:G\to G\) having pairwise commuting image subgroups. Since \(Z(G)=1\), if one \(e_j\) is an automorphism, every other one is trivial, giving (A). Otherwise all nontrivial image subgroups are order-\(q\) complements. Since each such subgroup is self-centralizing, their images must coincide, giving one common complement and (B). Conversely both constructions are group cellular automata. Different nonzero coefficient polynomials give different maps, and distinct complements have disjoint nonidentity elements, so there is no hidden multiplicity. This also gives \(1+v(q^r-1)+ra\) local rules on \(r\) prescribed sites.

**3. Entropy.** Since every group automorphism has finite order, for case (A) a positive power of \(F\) is a pure coordinate shift. Entropy scales under positive powers and \(h(\sigma^j)=|j|\log|G|\), giving (A). In (B), the first iterate lands in the common-complement full shift, and for \(P\ne0\) its restriction is the scalar linear cellular automaton \(L_P\) on \(\mathbf F_q^{\mathbf Z}\). The scalar map is surjective for nonzero \(P\): multiplication by \(P\) is injective on the finitely supported dual Laurent-polynomial module, so its compact dual is surjective. Removing one initial time step does not change topological entropy, hence \(h(F)=h(L_P)\). The one-dimensional scalar Laurent entropy identity gives \(h(L_P)=w(P)\log q\); it also follows from the one-dimensional linear-group formula in Castronuovo--Dennunzio--Kari--Margara, Theorem 4 (2026). The zero polynomial gives a constant map.

**4. Exact multiplicities.** For \(0<k\le R\), a polynomial with width \(k\) and support on one side of zero has a nonzero extreme coefficient (\(q-1\) choices), \(k\) other freely chosen coefficients (\(q^k\) choices), and two choices of side. For any \(1\le k\le2R\), a polynomial meeting both strict sides has outermost support indices \(-u<0<v\), with \(u+v=k\), \(1\le u,v\le R\). There are exactly \(c_R(k)\) such pairs, each allowing \((q-1)^2q^{k-1}\) coefficient choices. This proves the positive quotient multiplicities. At width zero the only nonzero polynomials are nonzero constants, \(q-1\) per complement; the zero map is common to all complements. At automorphism entropy \(k\log(vq)\), there are exactly \(2a\) shifts at offsets \(\pm k\); at zero there are \(a\) sitewise automorphisms. Prime support makes \(k\log q\ne\ell\log(vq)\) for positive integers \(k,\ell\), so these counts do not overlap. Summing the classification gives the displayed total and realizes every listed level.

## Verification

The accompanying standalone `check.py` independently enumerates all group homomorphisms of the groups \(S_3\), \(A_4\), and the nonabelian group of order \(21\) from their generator images, checks the homomorphism equation on all pairs, and counts commuting-image pairs and triples. It obtains, respectively, \((|\operatorname{End}|,|\operatorname{Aut}|,N_2,N_3)=(10,6,22,40),(33,24,81,177),(57,42,141,309)\). It also enumerates all Laurent coefficient vectors at radius one, two and three for \(q=2,3,5\), verifying the exact width multiplicities. These finite tests are not proofs for arbitrary groups or radii; the general proof is in the preceding sections.

## Relationship to prior work

Castronuovo, Dennunzio, Kari and Margara (2026) prove effective entropy computability for all finite-group cellular automata and supply the scalar Laurent entropy formula, but not the parameter-uniform list and multiplicities for this Frobenius family. Dennunzio, Formenti and Margara (2024), Theorems 7, 9 and 10, classify injectivity and transitivity for the alternating group \(A_4\) and odd dihedral groups; these are covered special families, but their statements do not provide the entropy-level multiplicity formulas above. The present statement adds the irreducible prime-complement family, a structural quotient/automorphism dichotomy, and complete radius-level counts. General entropy algorithms do apply to each individual example, and no claim is made that the scalar entropy identity or the special-case dynamical criteria are new.

## Limitations

The classification is restricted to irreducible elementary-abelian kernels with faithful *prime-order* complements. Reducible actions, composite complements, direct products and arbitrary local maps can have more commuting image types. The claim concerns mathematically distinct cellular automata on specified labeled spatial sites; it does not count conjugacy classes or spatial-shift equivalence classes. Historical equivalences under different group-theoretic terminology remain possible; the cited general methods may furnish alternative derivations. No independent audit has been performed.

## References

- N. Castronuovo, A. Dennunzio, J. Kari, L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1 (first posted 2026-11-12), https://arxiv.org/html/2611.16746v1, especially Theorem 4.
- A. Dennunzio, E. Formenti, L. Margara, *On the Dynamical Behavior of Cellular Automata on Finite Groups*, IEEE Access **12** (2024), https://doi.org/10.1109/ACCESS.2024.3452199, especially Theorems 7, 9, 10.
- N. Castronuovo, A. Dennunzio, L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics*, arXiv:2507.09761 (2025), https://arxiv.org/abs/2507.09761 (related general decomposition; abstract consulted).
