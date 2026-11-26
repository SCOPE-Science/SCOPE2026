# Central-shear automorphism group and order-four rigidity for \(Q_8\) cellular automata

## Finding

Consider continuous, shift-commuting group endomorphisms of the full two-sided shift \(Q_8^{\mathbb Z}\) with pointwise multiplication. Write \(S(x)_n=x_{n+1}\), let \(\mathcal C=\operatorname{Hom}(Q_8,\{\pm1\})\cong\mathbb F_2^2\), and use \(0\) for the constant identity-configuration map. All character families below have finite support.

The reversible group is explicitly
\[
\mathbb Z\times\left[\left(\bigoplus_{j\in\mathbb Z\setminus\{0\}}\mathcal C\right)\rtimes S_4\right].
\]
Here \(S\) generates the first factor, and \(S_4\cong\operatorname{Aut}(Q_8)\) acts on each copy of \(\mathcal C\) by precomposition with the inverse, through the quotient \(S_4\twoheadrightarrow\operatorname{GL}_2(2)\). Each reversible map has unique data \(F=S^k A_\alpha H_c\), where \(A_\alpha(x)_n=\alpha(x_n)\) and \(H_c(x)_n=x_n\prod_{j\ne0}c_j(x_{n+j})\). Its normalized map \(S^{-k}F\) has order in \(\{1,2,3,4\}\), and each order occurs. In particular every normalized map satisfies the twelfth-power identity, and the sharp bound on any individual order is four. No other drift makes the map have finite order.

The nonreversible maps are precisely the maps \(C_d(x)_n=\prod_{j\in\mathbb Z} d_j(x_{n+j})\). Any product of two such maps is \(0\). Their composition with the reversible part is given below; this yields the full composition monoid.

For context, the reversible normal form as a local rule, the reversible rule count, and the reversible entropy formula are covered by the more general order-\(p^3\) surjective classification [2]. The refinements here are the explicit quaternion composition structure, including the nonreversible part, and the sharper normalized order theorem.

## Proof

**Local rules.** The proper subgroups of \(Q_8\) are cyclic, and its commutator subgroup is its centre \(Z=\{\pm1\}\). A nonsurjective endomorphism kills the commutator because its image is abelian. Every square of \(Q_8\) lies in \(Z\); the image therefore has exponent at most two and lies in \(Z\). The possibilities are the four characters in \(\mathcal C\), all of which kill \(Z\). The surjective endomorphisms are the 24 automorphisms: the images of \(i,j\) can be any two nonparallel signed quaternion units, giving six and four choices. Equivalently the automorphisms act on the three imaginary axes as the signed permutations preserving orientation. This rotation group acts faithfully on the four unoriented cube diagonals and so is isomorphic to \(S_4\). The induced action on \(Q_8/Z\cong\mathbb F_2^2\) is the full \(\operatorname{GL}_2(2)\), with kernel the four diagonal sign changes preserving orientation.

The finite-memory local rule \(f:Q_8^E\to Q_8\) of a group endomorphism of the shift is a homomorphism. Its coordinate restrictions have pairwise commuting images and multiply to give \(f\). If none is an automorphism, the rule is of the form \(C_d\). Otherwise exactly one is an automorphism (two images equal to \(Q_8\) would not commute), and writing its site as \(k\) gives the displayed form \(S^k A_\alpha H_c\), since \(\alpha\) fixes \(Z\) pointwise. Restricting to each coordinate separately proves uniqueness.

**Composition.** A character is unchanged by multiplying its argument by an element of \(Z\). Hence \(H_c H_b=H_{c+b}\) and \(H_c^2=\mathrm{id}\), and \(C_dC_e=0\) since \(C_e\) takes values in \(Z^{\mathbb Z}\). Each shear is invertible; no \(C_d\) is invertible. Conjugation gives \(A_\alpha H_c A_\alpha^{-1}=H_{\alpha\cdot c}\), with \((\alpha\cdot c)_j=c_j\circ\alpha^{-1}\). The shift commutes with both types of reversible factor. The site-automorphism subgroup and the shear subgroup have trivial intersection by uniqueness of the coordinate restrictions. The same uniqueness separates shifts from the other factors. This proves the group isomorphism. For \(F=S^k A_\alpha H_c\) and every \(C_d\),
\[
F\circ C_d=S^k C_d,\qquad C_d\circ F=S^k C_{d\circ\alpha},\quad (d\circ\alpha)_j=d_j\circ\alpha.
\]
The first formula holds since the shears and alphabet automorphisms fix central configurations; in the second formula the characters ignore every central twist. These formulas together with the group law and \(C_dC_e=0\) exhaust composition.

**Sharp normalized orders.** Put \(B=A_\alpha H_c\), \(t=\operatorname{ord}(\alpha)\), and let \(\rho\) be the character action of \(\alpha\). The power \(B^m\) has alphabet part \(\alpha^m\) and shear part given, in the convention of writing the shear to the left of the alphabet part, by the sum \(\rho c+\rho^2 c+\cdots+\rho^m c\). If \(t=1\), \(B^2=\mathrm{id}\). If \(t=2\) or \(4\), \(\rho^2=1\), so the sum for \(m=4\) vanishes in characteristic two and \(B^4=\mathrm{id}\). If \(t=3\), \(\rho\) has order three since the action kernel has order four. On \(\mathbb F_2^2\) this action has no nonzero fixed vector and \(1+\rho+\rho^2=0\) (multiply by \(1-\rho\), which is invertible). Hence \(B^3=\mathrm{id}\). Since the order of \(B\) is a multiple of \(t\), these are precisely the claimed possibilities, and taking \(c=0\) realizes every order using \(S_4\). A wrong drift leaves a nonzero shift on the full central subshift, where \(B\) is the identity; hence it cannot yield finite order.

**Consequences.** On any fixed set of \(r\ge1\) distinct sites, there are \(4^r\) central rules and \(24r4^{r-1}\) reversible rules, counted by their coordinate restrictions. For a reversible map, if \(B\) has order \(m\) then \(F^m=S^{km}\). Entropy of the \(m\)th iterate is \(m\) times that of \(F\), while \(h_{\rm top}(S^a)=|a|\log8\); thus \(h_{\rm top}(F)=|k|\log8\). The central maps have entropy zero because their squares are constant. All values in the spectrum \(\{k\log8:k\ge0,\ k\in\mathbb Z\}\) are already realized by shifts. The only idempotents are \(0\) and \(\mathrm{id}\), by the square-zero and group cases.

## Verification and scope

The proof applies to the full two-sided shift with a group-homomorphic rule, not to arbitrary eight-symbol cellular automata. It does not enumerate conjugacy classes. The accompanying \(\texttt{verify\_q8.py}\) is a standard-library finite checker of the alphabet endomorphism census, small local-rule counts, shear laws and normalized orders for two offsite positions. It supports but does not prove the all-neighborhood results.

## Relationship to prior work

Dennunzio, Formenti and Margara [1, Section IX, Theorem 11] treat quaternion group cellular automata and provide the four-versus-24 alphabet split and the surjective/reversible criterion; those are background here. The order-\(p^3\) theorem [2, Finding and Proof §3] covers the reversible local normal form, reversible rule count and exact entropy by specializing \(p=2,G=Q_8\). It also gives \(F^{2t}=S^{2kt}\), which on its own allows normalized order six for \(t=3\) and eight for \(t=4\). The character-action calculation above excludes both, gives the explicit split group, and combines it with the square-zero ideal and the cross-composition laws. No publication ordering between the two records dated 22 November 2026 is asserted. General structural methods and entropy computability results [3,4] are separate. Historical priority for the refinements is qualified by the available literature.

## References

1. A. Dennunzio, E. Formenti and L. Margara, *On the Dynamical Behavior of Cellular Automata on Finite Groups*, IEEE Access 12 (2024), 122061–122077. https://doi.org/10.1109/ACCESS.2024.3452199
2. *Shift-power rigidity for surjective cellular automata on nonabelian groups of order \(p^3\)*, Resultary, 22 November 2026. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-shift-power-rigidity-for-surjective-cellular-automata-on-nonabel--8fa80cdab7a1
3. N. Castronuovo, A. Dennunzio and L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics*. https://arxiv.org/abs/2507.09761
4. N. Castronuovo, A. Dennunzio, J. Kari and L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*. https://arxiv.org/abs/2611.16746
