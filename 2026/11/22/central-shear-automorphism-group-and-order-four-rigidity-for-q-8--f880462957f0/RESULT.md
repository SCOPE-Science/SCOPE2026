# Central-shear automorphism group and order-four rigidity for \(Q_8\) cellular automata

## Finding
Let \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), and consider every continuous shift-commuting group endomorphism \(F:Q_8^{\mathbb Z}\to Q_8^{\mathbb Z}\), with the pointwise quaternion-group structure. Let \(S(x)_n=x_{n+1}\) and let \(\mathcal C=\operatorname{Hom}(Q_8,\{\pm1\})\cong\mathbb F_2^2\).

**Complete classification.** Every such \(F\) is exactly one of the following, with all character families finitely supported:

* A central map \(C_c(x)_n=\prod_{j\in\mathbb Z}c_j(x_{n+j})\), where \(c_j\in\mathcal C\). Every central map satisfies \(C_c^2=0\), with \(0\) the constant identity-configuration map.
* A reversible map \(F=S^k A_\alpha H_c\), where \(k\in\mathbb Z\), \(A_\alpha(x)_n=\alpha(x_n)\), \(\alpha\in\operatorname{Aut}(Q_8)\cong S_4\), and
  \[
  H_c(x)_n=x_n\prod_{j\ne0}c_j(x_{n+j}),\qquad c_j\in\mathcal C.
  \]
  The triple \((k,\alpha,c)\) is unique.

The complete group of reversible group cellular automata is
\[
\operatorname{Aut}_{\rm GCA}(Q_8^{\mathbb Z})\cong
\mathbb Z\times\left[
\left(\bigoplus_{j\in\mathbb Z\setminus\{0\}}\mathbb F_2^2\right)
\rtimes S_4\right],
\]
where \(S_4\) acts on each \(\mathbb F_2^2\) through its natural quotient \(S_4\twoheadrightarrow S_3\cong\operatorname{GL}_2(2)\). The shift \(S\) generates the central \(\mathbb Z\)-factor.

**Sharp normalized order bound.** For every reversible \(F\), there is a unique drift \(k\) such that \(S^{-k}F\) has order one, two, three, or four. All four orders occur. Thus \((S^{-k}F)^4\) need not be the identity when the order is three; the precise universal relation is \((S^{-k}F)^{12}=\mathrm{id}\), and every individual normalized order is at most four.

**Complete entropy and finite-window counts.** The topological entropy is
\[
h_{\rm top}(F)=\begin{cases}|k|\log8,&F=S^kA_\alpha H_c,\\0,&F=C_c.\end{cases}
\]
Consequently its spectrum is precisely \(\{m\log8:m=0,1,2,\ldots\}\). On any fixed neighborhood of \(r\ge1\) distinct sites there are exactly \(4^r+24r4^{r-1}\) distinct group-homomorphism local rules; exactly \(24r4^{r-1}\) yield reversible global maps. The endomorphism monoid has precisely two idempotents: \(0\) and \(\mathrm{id}\).

## Assumptions and scope
The configuration space is the full two-sided shift over the *nonabelian group alphabet* \(Q_8\), not the vector space \(\mathbb F_2^3\). A cellular automaton is required to preserve pointwise group multiplication, as well as to be continuous and spatially shift commuting. No restriction on finite memory, radius, or neighborhood symmetry is imposed. All products of characters land in the central group \(Z(Q_8)=\{\pm1\}\). All entropies use the natural logarithm.

## Proof
**1. Endomorphisms of the alphabet.** Every proper subgroup of \(Q_8\) is cyclic. A non-surjective endomorphism \(\phi:Q_8\to Q_8\) has abelian image and kills the commutator subgroup \([Q_8,Q_8]=\{\pm1\}\). Every element of \(Q_8\) has square in this commutator subgroup, so every element in the image of \(\phi\) has square \(1\). The only elements of \(Q_8\) of order dividing two are \(\pm1\). Hence all non-surjective endomorphisms are exactly the four central characters \(\mathcal C\). The other endomorphisms are the 24 automorphisms: the images of \(i,j\) are an ordered pair of nonparallel signed quaternion units (six choices for the first, four for the second). The induced action on \(Q_8/Z(Q_8)\cong\mathbb F_2^2\) realizes \(\operatorname{GL}_2(2)\), with inner automorphism kernel of order four. This is the standard \(\operatorname{Aut}(Q_8)\cong S_4\) extension.

**2. Local rule exhaustion.** By the finite-memory characterization of shift-commuting continuous maps, the local rule is a homomorphism \(f:Q_8^E\to Q_8\) for some finite set \(E\subset\mathbb Z\). Its coordinate restrictions \(f_j\in\operatorname{End}(Q_8)\) have pairwise commuting images, and \(f((x_j))=\prod_{j\in E}f_j(x_j)\). At most one coordinate restriction can be an automorphism, because two full \(Q_8\) images do not commute. If none is an automorphism, all are central characters, yielding exactly \(C_c\). If one is an automorphism \(\alpha\) at a unique site \(k\), all others are central characters, yielding uniquely \(S^kA_\alpha H_c\) with \(c\) supported away from zero. This also proves the rule count: among \(r\) sites there are \(4^r\) character-only rules and \(r\cdot24\cdot4^{r-1}\) automorphism-bearing rules. No two different choices coincide since they have different coordinate restrictions.

**3. Involutive shears and group structure.** For every \(\chi\in\mathcal C\), \(\chi(-1)=1\). Hence central twists do not change the value of any character at any coordinate: \(\chi(H_c(x)_n)=\chi(x_n)\). It follows directly that \(H_cH_d=H_{c+d}\), so \(H_c^2=\mathrm{id}\). The shears form \(\bigoplus_{j\ne0}\mathcal C\). All shears commute with \(S\), and \(A_\alpha H_c A_\alpha^{-1}=H_{\alpha\cdot c}\), with \((\alpha\cdot c)_j=c_j\circ\alpha^{-1}\). Their intersection with \(\{S^kA_\alpha\}\) is the identity. Step 2 gives unique factorization, hence the asserted semidirect/direct product. A central map lands entirely in \(Z(Q_8)^{\mathbb Z}\), and each character annihilates that subgroup, proving \(C_cC_d=0\) for every two central maps. Thus every map in the classified first case is noninvertible and square-zero, while every map in the second case is explicitly invertible.

**4. The uniform four-step bound.** Put \(B=A_\alpha H_c\). The action of \(\operatorname{Aut}(Q_8)\cong S_4\) on the shear group factors through \(\operatorname{GL}_2(2)\cong S_3\). An element \(\alpha\) of \(S_4\) has order \(1,2,3,\) or \(4\). If the order is \(1\), \(B^2=1\). If the order is \(2\) or \(4\), its action on \(\mathcal C\) has order at most two, so the sum of the conjugate shears over four factors vanishes in characteristic two; hence \(B^4=1\). If the order is \(3\), the action is the fixed-point-free order-three element of \(\operatorname{GL}_2(2)\), satisfying \(1+\rho+\rho^2=0\), so \(B^3=1\). The order of \(B\) therefore belongs to \(\{1,2,3,4\}\). These are all realized by coordinatewise automorphisms of the corresponding orders.

**5. Entropy and idempotents.** The shear \(H_c\) commutes with the shift, as does \(A_\alpha\). If \(B\) has order \(d\), then \((S^kB)^d=S^{kd}\). Standard entropy identities for continuous maps on compact spaces give \(d h_{\rm top}(S^kB)=h_{\rm top}(S^{kd})=|kd|\log8\), proving the claimed formula. A square-zero central map has entropy zero. Among reversible maps only the identity is idempotent, and among central maps \(C_c^2=0\) forces idempotency only for \(C_c=0\).

## Verification
The accompanying standalone `verify_q8.py` enumerates all \(8^2\) pairs of images of the standard generators, independently checks the quaternion group relations and all endomorphism tables, and confirms 28 endomorphisms: 24 automorphisms and four central characters. Exhaustive compatible-coordinate counts for one, two, and three prescribed sites give exactly 28, 208 and 1,216. It also tests shear involution and addition identities on every configuration of a three-site cyclic ring and checks the algebraic normalized-order bound for all 384 choices of an automorphism and two offsite characters. These finite checks are auxiliary; the proof handles arbitrary finite neighborhoods and bilateral infinite configurations.

## Relationship to prior work
Dennunzio, Formenti, and Margara (2024), especially Section IX and Theorem 11, already give the four-versus-24 split in quaternion alphabet endomorphisms and the equivalence between reversible and surjective group cellular automata; these underlying observations are explicitly *not* claimed as new. Castronuovo, Dennunzio, and Margara (2025) provide general decomposition and decidability methods. Castronuovo, Dennunzio, Kari, and Margara (2026) prove entropy computability and logarithmic-integrality for arbitrary one-dimensional group cellular automata. The present statement goes further in this concrete case: it describes the entire composition monoid and infinite reversible group, proves the sharp order-four rigidity of every drift-normalized automaton, enumerates all local homomorphism rules, and determines the entire entropy spectrum. It is a classification specific to \(Q_8\), not a general theorem for all nonabelian alphabets.

## Limitations
The finding concerns the two-sided full shift and **group-homomorphic** rules; arbitrary set-theoretic cellular automata on eight symbols are not classified. It does not identify conjugacy classes or orbit counts of individual reversible automata. The finite checker cannot establish infinite-neighborhood completeness; completeness rests on the endomorphism and commuting-image arguments in the proof. No independent mathematical audit has been performed. Earlier specialized classifications of quaternionic algebraic cellular automata might provide equivalent descriptions, so historical priority warrants further checking.

## References
1. N. Castronuovo, A. Dennunzio, J. Kari, L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1, first posted 12 November 2026. https://arxiv.org/pdf/2611.16746
2. A. Dennunzio, E. Formenti, L. Margara, *On the Dynamical Behavior of Cellular Automata on Finite Groups*, IEEE Access 12 (2024), 122061–122077, DOI:10.1109/ACCESS.2024.3452199. https://boa.unimib.it/retrieve/1a7d2f2e-c021-4c18-8a2a-1705d58b6118/Dennunzio-2024-IEEE%20Access-VoR.pdf
3. N. Castronuovo, A. Dennunzio, L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics*, arXiv:2507.09761v1, 13 July 2025. https://arxiv.org/pdf/2507.09761
