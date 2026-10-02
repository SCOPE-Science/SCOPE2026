# Finite-abelian Grothendieck obstructions to object cotorsion completeness

## Statement

Let $k$ be a field and let $S$ be a finite-dimensional semisimple $k$-algebra. Put
\[
\mathcal{D}=\operatorname{Ch}^{b}(\operatorname{mod}_{\mathrm{fd}}S),
\]
and let
\[
\varepsilon(X)=\sum_{n\in\mathbb Z}(-1)^n[H^n(X)]\in K_0(\operatorname{mod}_{\mathrm{fd}}S)
\]
be the Euler class. Let $\Lambda$ be a proper finite-index subgroup of
$K_0(\operatorname{mod}_{\mathrm{fd}}S)$, put
\[
G=K_0(\operatorname{mod}_{\mathrm{fd}}S)/\Lambda,
\]
and let $e$ be the exponent of the finite abelian group $G$. Define the full subcategory
\[
\mathcal A_\Lambda=\{X\in\mathcal D:\varepsilon(X)\in\Lambda\},
\]
with the degreewise split exact structure. Inside it define
\[
\mathcal F_\Lambda=\{X:H^n(X)=0\text{ for }n\ge1\},\qquad
\mathcal C_\Lambda=\{X:H^n(X)=0\text{ for }n\le1\}.
\]
For morphisms in $\mathcal A_\Lambda$, define
\[
\mathcal I_\Lambda=\{f:H^n(f)=0\text{ for every }n\ge1\},\qquad
\mathcal J_\Lambda=\{g:H^n(g)=0\text{ for every }n\le1\}.
\]

Then:

1. $\mathcal A_\Lambda$ is an essentially small, Hom-finite, weakly idempotent complete Frobenius exact category. It is not idempotent complete, and its idempotent completion is $\mathcal D$.
2. The projective-injective objects of $\mathcal A_\Lambda$ are exactly the contractible complexes.
3. The ideals are object ideals,
   \[
   \mathcal I_\Lambda=\langle\mathcal F_\Lambda\rangle,\qquad
   \mathcal J_\Lambda=\langle\mathcal C_\Lambda\rangle,
   \]
   and
   \[
   {}^\perp\mathcal J_\Lambda=\mathcal I_\Lambda,\qquad
   \mathcal I_\Lambda^\perp=\mathcal J_\Lambda.
   \]
   Hence $(\mathcal I_\Lambda,\mathcal J_\Lambda)$ is an ideal cotorsion pair.
4. This ideal cotorsion pair is complete.
5. Its associated object cotorsion pair $(\mathcal F_\Lambda,\mathcal C_\Lambda)$ is neither special precovering nor special preenveloping.
6. More precisely, for $A\in\mathcal A_\Lambda$, define the two defect classes
   \[
   \alpha(A)=\sum_{n\le0}(-1)^n[H^n(A)]+\Lambda\in G,
   \]
   \[
   \beta(A)=\sum_{n\ge2}(-1)^n[H^n(A)]+\Lambda\in G.
   \]
   Then a conflation
   \[
   0\to C\to F\to A\to0,
   \qquad C\in\mathcal C_\Lambda,\ F\in\mathcal F_\Lambda,
   \]
   exists if and only if $\alpha(A)=0$. Dually, a conflation
   \[
   0\to A\to C\to F\to0
   \]
   with $C\in\mathcal C_\Lambda$ and $F\in\mathcal F_\Lambda$ exists if and only if $\beta(A)=0$.
7. The exact direct-sum stabilization indices are
   \[
   \min\{r\ge1:A^{\oplus r}\text{ has a special }\mathcal F_\Lambda\text{-precover}\}
   =\operatorname{ord}_G(\alpha(A)),
   \]
   \[
   \min\{r\ge1:A^{\oplus r}\text{ has a special }\mathcal C_\Lambda\text{-preenvelope}\}
   =\operatorname{ord}_G(\beta(A)),
   \]
   with the order of $0$ taken to be $1$. Every element of $G$ occurs as such a defect class.

Consequently, every nontrivial finite abelian group occurs as an exact obstruction group for the descent of completeness from a complete ideal cotorsion pair of object ideals to its associated object cotorsion pair in a Hom-finite, weakly idempotent complete Frobenius exact category. The parity example of Ren--Wang is the special case $S=k$, $\Lambda=2\mathbb Z$, and $G\cong\mathbb Z/2\mathbb Z$.

## Proof

Because $S$ is semisimple, $K_0(\operatorname{mod}_{\mathrm{fd}}S)$ is free abelian on the simple $S$-modules. For every bounded complex,
\[
\varepsilon(X)=\sum_n(-1)^n[X^n]=\sum_n(-1)^n[H^n(X)].
\]
Thus Euler classes are additive on degreewise split short exact sequences.

### 1. Exact and Frobenius structure

The subcategory $\mathcal A_\Lambda$ is additive and extension closed because $\Lambda$ is a subgroup. If $Y\cong X\oplus Z$ with $X,Y\in\mathcal A_\Lambda$, then
\[
\varepsilon(Z)=\varepsilon(Y)-\varepsilon(X)\in\Lambda,
\]
so $Z\in\mathcal A_\Lambda$. Hence $\mathcal A_\Lambda$ is weakly idempotent complete.

Every bounded complex over a semisimple category decomposes as
\[
X\cong H(X)\oplus Q_X,
\]
where $Q_X$ is contractible. Contractible complexes have Euler class $0$. The standard degreewise split cone sequences
\[
0\to X\to K(X)\to X[1]\to0,
\qquad
0\to X[-1]\to P(X)\to X\to0
\]
remain inside $\mathcal A_\Lambda$, because shifts negate the Euler class and $K(X),P(X)$ are contractible. They give enough injectives and projectives. As in the ambient split exact category, contractible complexes are projective-injective; conversely, a projective (respectively injective) object is a retract of $P(X)$ (respectively $K(X)$), hence is contractible. Therefore $\mathcal A_\Lambda$ is Frobenius.

Since $\Lambda$ is proper, some simple module $T$ has $[T]\notin\Lambda$. But $e[T]\in\Lambda$, so $S^0(T^{\oplus e})\in\mathcal A_\Lambda$, while the idempotent projecting onto one copy of $S^0(T)$ cannot split in $\mathcal A_\Lambda$. Thus $\mathcal A_\Lambda$ is not idempotent complete.

Every $X\in\mathcal D$ is a direct summand of $X^{\oplus e}\in\mathcal A_\Lambda$, because $e\varepsilon(X)\in\Lambda$. Hence the idempotent completion of $\mathcal A_\Lambda$ is $\mathcal D$; the exact structures agree after completion because every degreewise split conflation in $\mathcal D$ is a direct summand of its $e$-fold direct sum in $\mathcal A_\Lambda$.

### 2. Extensions

For $X,Y\in\mathcal A_\Lambda$, every degreewise split extension in $\mathcal D$ has middle term of Euler class $\varepsilon(X)+\varepsilon(Y)\in\Lambda$. Therefore restriction does not remove any extension class, and the semisimple splitting gives
\[
\operatorname{Ext}^1_{\mathcal A_\Lambda}(X,Y)
\cong
\bigoplus_n\operatorname{Hom}_S(H^n(X),H^{n+1}(Y)).
\]
A chain map inducing zero on all cohomology groups is null-homotopic and factors through a contractible complex.

### 3. The object ideals

A morphism factoring through $\mathcal F_\Lambda$ lies in $\mathcal I_\Lambda$. Conversely, let $f:X\to Y$ lie in $\mathcal I_\Lambda$. Write
\[
X\cong L\oplus U\oplus Q,
\qquad
L=H^{\le0}(X),\quad U=H^{\ge1}(X),
\]
with $Q$ contractible. The map
\[
f_0=f\iota_L\pi_L
\]
has the same cohomology map as $f$, so $f-f_0$ is null-homotopic and factors through a contractible object of $\mathcal F_\Lambda$. The map $f_0$ factors through $L^{\oplus e}$, and
\[
\varepsilon(L^{\oplus e})=e\varepsilon(L)\in\Lambda.
\]
Thus $L^{\oplus e}\in\mathcal F_\Lambda$, proving
\[
\mathcal I_\Lambda=\langle\mathcal F_\Lambda\rangle.
\]
The dual argument with $H^{\ge2}$ gives
\[
\mathcal J_\Lambda=\langle\mathcal C_\Lambda\rangle.
\]

The displayed extension formula immediately gives
$\operatorname{Ext}^1(\mathcal I_\Lambda,\mathcal J_\Lambda)=0$.
For the reverse orthogonality, suppose $f$ has $H^n(f)\ne0$ for some $n\ge1$. Since the module category is semisimple, there is a simple module $T$ and a map from the codomain of $H^n(f)$ to $T$ whose composite with $H^n(f)$ is nonzero. Embed this map into the first coordinate of $T^{\oplus e}$ and use the stalk
\[
S^{n+1}(T^{\oplus e})\in\mathcal C_\Lambda.
\]
Its identity detects a nonzero component of $\operatorname{Ext}^1(f,-)$. Hence $f\notin{}^\perp\mathcal J_\Lambda$. This proves ${}^\perp\mathcal J_\Lambda=\mathcal I_\Lambda$. The dual simple-summand test proves $\mathcal I_\Lambda^\perp=\mathcal J_\Lambda$.

### 4. Completeness of the ideal cotorsion pair

Let
\[
A\cong L\oplus U\oplus Q,
\qquad
L=H^{\le0}(A),\quad U=H^{\ge1}(A),
\]
with $Q$ contractible. Define
\[
C_A=U[-1]^{\oplus e},
\]
\[
E_A=L\oplus P(U)\oplus U[-1]^{\oplus(e-1)}\oplus Q,
\]
and map $p_A:E_A\to A$ by the identity on $L,Q$, by the standard deflation $P(U)\to U$, and by zero on the extra $U[-1]$ summands. Its kernel is $C_A$. Moreover
\[
\varepsilon(C_A)=-e\varepsilon(U)\in\Lambda,
\qquad
\varepsilon(E_A)=\varepsilon(A)-e\varepsilon(U)\in\Lambda.
\]
The kernel lies in $\mathcal C_\Lambda$, while $p_A\in\mathcal I_\Lambda$. Thus this is an object-special $\mathcal I_\Lambda$-precover.

Dually, with
\[
A\cong V\oplus W\oplus Q,
\qquad
V=H^{\le1}(A),\quad W=H^{\ge2}(A),
\]
put
\[
D_A=K(V)\oplus W\oplus V[1]^{\oplus(e-1)}\oplus Q.
\]
The natural monomorphism $j_A:A\to D_A$ has cokernel $V[1]^{\oplus e}\in\mathcal F_\Lambda$, and
\[
\varepsilon(D_A)=\varepsilon(A)-e\varepsilon(V)\in\Lambda.
\]
Also $j_A\in\mathcal J_\Lambda$. Hence it is an object-special $\mathcal J_\Lambda$-preenvelope. The ideal cotorsion pair is complete.

### 5. Exact object obstruction

Suppose
\[
0\to C\to F\to A\to0
\]
is a conflation with $C\in\mathcal C_\Lambda$ and $F\in\mathcal F_\Lambda$. The long exact cohomology sequence forces
\[
H(F)\cong H^{\le0}(A).
\]
Therefore $\alpha(A)=0$.

Conversely, if $\alpha(A)=0$, then in the decomposition $A\cong L\oplus U\oplus Q$ above, both $\varepsilon(L)$ and $\varepsilon(U)=\varepsilon(A)-\varepsilon(L)$ lie in $\Lambda$. Hence the ordinary one-copy cone sequence
\[
0\to U[-1]\to L\oplus P(U)\oplus Q\to A\to0
\]
already lies in $\mathcal A_\Lambda$, with kernel in $\mathcal C_\Lambda$ and middle term in $\mathcal F_\Lambda$. Thus a special object precover exists exactly when $\alpha(A)=0$. The dual argument gives the criterion $\beta(A)=0$ for a special object preenvelope.

Since $\Lambda$ is proper, choose a simple $T$ with $[T]\notin\Lambda$. Then
\[
M=S^0(T)\oplus S^1(T),\qquad N=S^1(T)\oplus S^2(T)
\]
both have Euler class $0$, so they belong to $\mathcal A_\Lambda$, but $\alpha(M)=[T]+\Lambda\ne0$ and $\beta(N)=[T]+\Lambda\ne0$. Hence the object cotorsion pair is neither special precovering nor special preenveloping.

### 6. Stabilization and realization

For every $r\ge1$,
\[
\alpha(A^{\oplus r})=r\alpha(A),\qquad
\beta(A^{\oplus r})=r\beta(A).
\]
Applying the exact criterion above proves that the least direct-sum multiplicity that repairs the relevant object approximation is exactly the order of the corresponding element of $G$.

Every $g\in G$ occurs. Choose $\xi\in K_0(\operatorname{mod}_{\mathrm{fd}}S)$ representing $g$ and write $\xi=[P]-[Q]$. Let
\[
L=S^0(P)\oplus S^{-1}(Q),
\qquad
A=L\oplus L[-3].
\]
Then $L$ is supported in degrees $\le0$, $L[-3]$ is supported in degrees $\ge2$, and
\[
\varepsilon(A)=\xi-\xi=0.
\]
Thus $A\in\mathcal A_\Lambda$ and $\alpha(A)=g$ (while $\beta(A)=-g$). Hence all elements, and therefore all element orders, are realized as approximation defects and stabilization indices.

Finally, given any nontrivial finite abelian group $G$, choose a surjection $\mathbb Z^r\twoheadrightarrow G$ and let $S=k^r$. Since $K_0(\operatorname{mod}_{\mathrm{fd}}S)\cong\mathbb Z^r$, taking $\Lambda$ to be the kernel realizes exactly that $G$.

## Context and relation to prior work

Ren and Wang, arXiv:2609.18681v1, construct the case of bounded finite-dimensional $k$-complexes with even total cohomology dimension. Because total dimension and Euler characteristic have the same parity, their category is the case $K_0\cong\mathbb Z$ and $\Lambda=2\mathbb Z$. Their proof uses doubles to keep intermediate objects inside the category and obtains a parity criterion for special object approximations.

The result above identifies the mechanism as a finite quotient of the Grothendieck group rather than a phenomenon special to parity: the exponent of $G$ replaces doubling in ideal factorizations and ideal approximations, while the precise object-level obstruction is the truncated Euler class in $G$. The direct-sum stabilization index records the order of that class.

The earlier counterexample of Wang--Wang--Zhu, arXiv:2609.14382v1, uses an additive integer-valued function to build a non-weakly-idempotent-complete exact category; it does not give the finite-quotient Frobenius construction above. Sun--Tan--Wang--Zhu, arXiv:2502.11146v1, provide general positive criteria for ideal approximation theory in Frobenius categories; those results are treated as background rather than as originality claims here.

## Limitations and originality scope

The mathematical claim is elementary once the finite-index $K_0$ viewpoint is identified, and the construction deliberately abstracts the mechanism of the recent parity example. The originality claim is therefore narrow: to the best of our knowledge, the literature checked does not state the finite-abelian $K_0$ family, the exact $G$-valued obstruction criteria, or the element-order stabilization formula. An equivalent observation could exist in older ideal-approximation or exact-category literature under different terminology, and a later revision or concurrent follow-up to the recent parity preprint could independently contain the same generalization.

No independent, formal, or peer-reviewed validation is claimed.

## References

1. J. Ren and Y. Wang, *A parity obstruction to completeness of object cotorsion pairs*, arXiv:2609.18681v1 (2026).
2. Q. Wang, Y. Wang and H. Zhu, *A Counterexample to the Open Question on Object Ideals*, arXiv:2609.14382v1 (2026).
3. D. Sun, Z. Tan, Q. Wang and H. Zhu, *Ideal approximation theory in Frobenius categories*, arXiv:2502.11146v1 (2025).
4. X. H. Fu, P. A. Guil Asensio, I. Herzog and B. Torrecillas, *Ideal approximation theory*, Advances in Mathematics 244 (2013), 750--790.
