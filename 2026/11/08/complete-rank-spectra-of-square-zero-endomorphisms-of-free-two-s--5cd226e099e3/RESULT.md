# Complete rank spectra of square-zero endomorphisms of free two-step nilpotent associative algebras

## Finding
Let \(k\) be a field, \(m\ge2\), \(V=k^m\), and \(N_m=V\oplus(V\otimes_k V)\), with multiplication \(uv=u\otimes v\) for \(u,v\in V\) and zero whenever an argument lies in \(V\otimes V\). We count **all labeled algebra endomorphisms** \(\Phi:N_m\to N_m\) satisfying \(\Phi\circ\Phi=0\), sorted by their ordinary \(k\)-linear rank. This is the free **nonunital** associative algebra on \(m\) generators truncated after word length two. The equation is composition-square-zero, not the square-zero property of an individual algebra element.

For \(k=\mathbb F_q\), write \[{n\brack j}_q=\prod_{i=0}^{j-1}\frac{q^{n-i}-1}{q^{j-i}-1},\quad G_j(q)=\prod_{i=0}^{j-1}(q^j-q^i),\] with empty products equal to one. For each \(0\le r\le\lfloor m/2\rfloor\), set \[a=m-2r,\quad b=m^2-2r^2,\quad Q_{m,r}(q)={m\brack r}_q{m-r\brack r}_qG_r(q).\]

The full rank polynomial is
\[\boxed{\mathcal R_{m,q}(z)=\sum_{r=0}^{\lfloor m/2\rfloor}Q_{m,r}(q)q^{2r^3+rb+ar^2}\sum_{s=0}^{a}{a\brack s}_q\left(\prod_{i=0}^{s-1}(q^b-q^i)\right)z^{r(r+1)+s}.}\]
Every coefficient counts actual distinct algebra endomorphisms. Summing coefficients gives the closed formula
\[\#\{\Phi:\Phi^2=0\}=\sum_{r=0}^{\lfloor m/2\rfloor} Q_{m,r}(q)\,q^{m^3-m^2r-mr^2+2r^3}.\]
Over **any** field, the attainable linear ranks are exactly
\[\bigcup_{r=0}^{\lfloor m/2\rfloor}\{r(r+1)+s:0\le s\le m-2r\}.\]
In particular, the maximum rank is \(m+h(h-1)\), where \(h=\lfloor m/2\rfloor\). The spectrum can be disconnected: for \(m=6\), it is \(\{0,1,2,3,4,5,6,7,8,12\}\), with the three consecutive ranks \(9,10,11\) forbidden.

## Assumptions and scope
The algebra is nonunital. The base field is arbitrary for the structural criterion and rank support; the coefficient formula assumes a finite field of cardinality \(q\), an arbitrary prime power. The count is for labeled endomorphisms, not automorphism-conjugacy classes, and the rank is on the full vector space of dimension \(m+m^2\).

## Proof
**Step 1 (unique endomorphism blocks).** The product ideal \(N_m^2=V\otimes V\) is characteristic under every endomorphism. The image of any degree-one generator has a uniquely determined linear part \(T:V\to V\) and quadratic part \(S:V\to V\otimes V\). Multiplicativity on every product of generators forces its value on the quadratic ideal to be exactly \(U=T\otimes T\). Conversely arbitrary \(T,S\) with this formula give an algebra endomorphism, because all triple products vanish. Relative to the ordered decomposition \(V\oplus(V\otimes V)\), the full operator matrix is
\[\Phi=\begin{pmatrix}T&0\\S&U\end{pmatrix}.\]

**Step 2 (composition equation).** Direct block multiplication gives
\[\Phi^2=\begin{pmatrix}T^2&0\\ST+US&U^2\end{pmatrix}.\]
If \(T^2=0\) then \(U^2=T^2\otimes T^2=0\). Consequently \(\Phi^2=0\) if and only if \(T^2=0\) and \(ST+US=0\), without any characteristic restriction.

**Step 3 (exact intertwiner dimension).** Fix a square-zero \(T\) of rank \(r\), and let \(K=\ker T\), \(I=\operatorname{im}T\). Necessarily \(I\subseteq K\), with \(\dim(K/I)=a=m-2r\). Since \(U=T\otimes T\) has rank \(r^2\), \(\dim(\ker U/\operatorname{im}U)=b=m^2-2r^2\). Regard \(V\) and \(V\otimes V\) as modules over \(k[\epsilon]/(\epsilon^2)\) with \(\epsilon\) acting as \(T\) and \(-U\), respectively. Their Jordan decompositions are \(J_2^{\oplus r}\oplus J_1^{\oplus a}\) and \(J_2^{\oplus r^2}\oplus J_1^{\oplus b}\). The relation \(ST+US=0\) is precisely a module-homomorphism relation. The dimensions of the Hom spaces \(J_2\to J_2\), \(J_2\to J_1\), \(J_1\to J_2\), \(J_1\to J_1\) are respectively \(2,1,1,1\), so the full vector space of allowable \(S\) has dimension
\[H=2r^3+rb+ar^2+ab=m^3-m^2r-mr^2+2r^3.\]

**Step 4 (rank refinement and uniform fibers).** For \(v\in K\), the defining equation implies \(Sv\in\ker U\). If \(v\in I\), write \(v=Tw\) and obtain \(Sv=-USw\in\operatorname{im}U\). Thus each allowable \(S\) induces a well-defined linear map
\[\overline S: K/I\longrightarrow\ker U/\operatorname{im}U.\]
This induced-map construction is surjective: choose complements of \(I\) in \(K\) and \(\operatorname{im}U\) in \(\ker U\), lift any desired map on the two complements, set \(S=0\) on the other Jordan summands, and extend linearly. Its kernel therefore has dimension \(H-ab=2r^3+rb+ar^2\). Over \(\mathbb F_q\), every prescribed \(\overline S\) has exactly \(q^{H-ab}\) lifts.

The projection of \(\operatorname{im}\Phi\) onto \(V\) is \(I\) of dimension \(r\); its intersection with the quadratic summand is \(S(K)+\operatorname{im}U\). Since \(S(K)\subseteq\ker U\), this intersection has dimension \(r^2+\operatorname{rank}\overline S\). Hence
\[\operatorname{rank}\Phi=r+r^2+\operatorname{rank}\overline S.\]
The number of maps from an \(a\)-space to a \(b\)-space with rank \(s\) is \({a\brack s}_q\prod_{i=0}^{s-1}(q^b-q^i)\).

**Step 5 (number of possible quotient matrices).** A square-zero \(m\times m\) matrix \(T\) of rank \(r\) is determined by choosing an image \(I\) of dimension \(r\), a kernel \(K\) of dimension \(m-r\) containing \(I\), and an isomorphism \(V/K\to I\). The respective counts are \({m\brack r}_q\), \({m-r\brack r}_q\), and \(G_r(q)\). Multiplying these with the Step 4 fiber count proves the displayed rank polynomial. Summing over all \(S\) proves the total-count formula. For arbitrary fields, every rank \(s\in\{0,\ldots,a\}\) is attainable because \(0\le a\le b\); conversely Steps 2–4 exclude all other ranks. Maximization over \(r\) gives \(m+r(r-1)\), which is nondecreasing in \(r\), proving the maximum. \(m=6\) gives the explicit gap example.

## Verification
The accompanying dependency-free `check.py` directly enumerates every \(T\) and \(S\) over \(\mathbb F_2\) and \(\mathbb F_3\) when \(m=2\); for every candidate it evaluates the original composition-square equation and computes the linear rank of the full algebra endomorphism. It checks multiplication on every ordered pair of word generators. It independently builds and row-reduces the linear constraints on \(S\) for every square-zero \(T\) over \(\mathbb F_2\) and \(\mathbb F_3\) when \(m=2,3\). The outputs agree with the symbolic formula in all cases. Execute `python check.py`; expected output is included as `verification_output.txt`. Example full rank distributions are \(1+45z+258z^2\) for \(m=2,q=2\) and \(1+320z+6888z^2\) for \(m=2,q=3\). These finite checks are independent corroboration; arbitrary \(m,q\) follow from the preceding proof, not extrapolation.

## Relationship to prior work
Lipyanski (2005), arXiv:math/0511654, studies **automorphisms of the semigroup of endomorphisms** of free nilpotent associative algebras. His Theorem B and Example 7.2 explicitly cover the same type of free three-nilpotent nonunital algebra, but identify symmetries of the whole endomorphism semigroup; they do not give cardinalities or linear ranks of its composition-square-zero elements. De Graaf (2010), arXiv:1009.5339, classifies underlying nilpotent associative algebras of small dimension, rather than the endomorphism rank distribution on a fixed algebra. Lopatin–Shestakov (2013), arXiv:1303.0898, studies the nilpotency degree of **different relatively free algebras satisfying an elementwise polynomial identity**; its results neither count these endomorphisms nor imply the rank polynomial. The basic Gaussian count of square-zero matrices alone does not imply the theorem: for nonzero \(T\), the required lifting parameter \(S\) is constrained by \(ST+(T\otimes T)S=0\) and changes the possible full ranks. The main unresolved priority risk is an unlocated endomorphism-monoid enumeration or more general module-intertwiner formula already specialized to this setting.

## Limitations
The theorem treats nonunital free algebras truncated at word length two. It neither covers the unital augmentation algebra without additional conditions on unital maps, nor all endomorphism nilpotency orders, nor other nilpotent-algebra varieties. It counts labeled maps, not isomorphism orbits or the nonreduced parameter scheme. Full external priority verification and independent mathematical audit remain outstanding.

## References
- R. Lipyanski, *Automorphisms of the semigroup of endomorphisms of free algebras of homogeneous varieties*, arXiv:math/0511654, first posted 2005-11-27. https://arxiv.org/abs/math/0511654
- W. A. de Graaf, *Classification of nilpotent associative algebras of small dimension*, arXiv:1009.5339, first posted 2010-09-27. https://arxiv.org/abs/1009.5339
- A. A. Lopatin and I. P. Shestakov, *Associative nil-algebras over finite fields*, arXiv:1303.0898, first posted 2013-03-05. https://arxiv.org/abs/1303.0898
