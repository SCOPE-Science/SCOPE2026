# Complete skew-derivation cohomology spectrum for finite crown incidence algebras

## Finding
Fix an integer \(m\ge3\) and a finite field \(K=\mathbb F_q\). Define the **crown poset** \(P_m\) with minimal elements \(a_i\), maximal elements \(b_i\), and exactly the strict relations
\[
a_i<b_i,\qquad a_i<b_{i-1}\qquad(i\in\mathbb Z/m\mathbb Z).
\]
Let \(A=I(P_m,K)\), the incidence algebra. For an automorphism \(\varphi\) of \(A\), a \(\varphi\)-derivation means a \(K\)-linear map satisfying
\[
D(xy)=D(x)y+\varphi(x)D(y)
\]
for every \(x,y\in A\); inner \(\varphi\)-derivations have the form \(D_u(x)=ux-\varphi(x)u\). Put
\[
d(\varphi)=\dim_K\bigl(\operatorname{Der}^{\varphi}(A)/\operatorname{IDer}^{\varphi}(A)\bigr).
\]
Every automorphism has a factorization \(\varphi=\xi_u\circ M_\sigma\circ\widehat\lambda\), where \(\xi_u\) is conjugation by a unit, \(M_\sigma\) multiplies each comparable basis element \(e_{xy}\) by the nonzero scalar \(\sigma(x,y)\), and \(\lambda\) is a poset automorphism. The poset automorphism belongs to the dihedral group of order \(2m\). If \(\lambda\) is the identity, define its scalar holonomy
\[
H(\sigma)=\prod_{i\in\mathbb Z/m\mathbb Z}
\frac{\sigma(a_i,b_i)}{\sigma(a_i,b_{i-1})}\in K^\times.
\]
Then the **complete cohomology spectrum**, valid in every characteristic, is
\[
\boxed{
d(\varphi)=\begin{cases}
1,&\lambda=\mathrm{id}\text{ and }H(\sigma)=1,\\
0,&\lambda=\mathrm{id}\text{ and }H(\sigma)\ne1,\\
m,&\lambda\text{ is a rotation by }+1\text{ or }-1,\\
0,&\lambda\text{ is any other nonidentity rotation},\\
2,&\lambda\text{ is a reflection}.
\end{cases}}
\]
The condition \(H(\sigma)=1\) is independent of the chosen factorization when \(\lambda=\mathrm{id}\).

Furthermore,
\[
|\operatorname{Aut}_K(A)|=2m\,q^{2m}(q-1)^{2m}.
\]
For uniformly chosen \(\varphi\in\operatorname{Aut}_K(A)\), the full probability distribution of \(d(\varphi)\) is
\[
\begin{aligned}
\Pr[d=m]&=\frac1m,\\
\Pr[d=2]&=\frac12,\\
\Pr[d=1]&=\frac{1}{2m(q-1)},\\
\Pr[d=0]&=\frac12-\frac1m-\frac{1}{2m(q-1)}.
\end{aligned}
\]
For fixed \(q\), as \(m\to\infty\), the distribution converges to equal point masses at \(0\) and \(2\), whereas
\[
\mathbb E[d]=2+\frac1{2m(q-1)}\longrightarrow 2,
\qquad
\mathbb E[d^2]=m+2+\frac1{2m(q-1)}.
\]
The limiting distribution has mean \(1\), so this family exhibits a specific failure of uniform integrability: one-step rotations have probability \(1/m\) yet carry cohomology dimension \(m\).

## Assumptions and scope
All indices are modulo \(m\); there are \(2m\) vertices and \(2m\) strict comparable pairs, so \(\dim_K A=4m\). The poset has height one and is connected. A rotation by \(k\) sends \(a_i\mapsto a_{i+k}\) and \(b_i\mapsto b_{i+k}\); a reflection indexed by \(r\) sends \(a_i\mapsto a_{r-i}\) and \(b_i\mapsto b_{r-i-1}\). These exhaust its poset automorphisms for \(m\ge3\). All derivations and automorphisms are \(K\)-linear; the theorem does not concern field-semilinear maps. The value \(d(\varphi)\) is the dimension of a quotient vector space, not the total number of derivations.

## Proof
**1. Passage to cochains.** The structural decomposition of incidence-algebra automorphisms and the twisted-cohomology isomorphism are established in Fornaroli–Khrypchenko [1, Theorem 1.3, Corollary 3.8]. Thus conjugating by \(u\) does not affect \(d(\varphi)\), and
\[
\operatorname{Der}^{\varphi}(A)/\operatorname{IDer}^{\varphi}(A)
\cong H^1_{(\sigma,\lambda)}(P_m,K).
\]
For this height-one poset, the normalized degree-one cocycle space consists of arbitrary scalars \(t_{ij}\) on the strict edges \(a_i<b_j\) **for which** \(\lambda(a_i)\le b_j\), and zero on all other strict edges. There are no strict chains of length two, so there are no further cocycle constraints. Define the allowed-edge set
\[
E_\lambda=\{(i,j):j\in\{i,i-1\}\cap\{\lambda_a(i),\lambda_a(i)-1\}\}.
\]
It follows that \(\dim Z^1_{(\sigma,\lambda)}=|E_\lambda|\). Here \(\lambda_a\) is the induced permutation of minimal indices.

A degree-zero cochain has a coordinate \(\epsilon(x)\) only at vertices fixed by \(\lambda\), because an automorphism preserves the minimal and maximal levels and \(\lambda(x)\le x\) then means \(\lambda(x)=x\). The degree-zero coboundary on an allowed edge is
\[
(\delta\epsilon)(a_i,b_j)=
\epsilon(a_i)-\sigma(\lambda(a_i),\lambda(b_j))\epsilon(b_j),
\]
where \(\epsilon(x)=0\) for a nonfixed vertex. Consequently \(d(\varphi)=|E_\lambda|-\operatorname{rank}\delta\).

**2. Rotations.** If \(\lambda\) rotates by \(k\ne0\), no vertex is fixed; hence \(\operatorname{rank}\delta=0\). The neighbor sets \(\{b_i,b_{i-1}\}\) and \(\{b_{i+k},b_{i+k-1}\}\) have one common member precisely for \(k=1\) or \(k=-1\) modulo \(m\), and no common member otherwise. Therefore \(|E_\lambda|=m\) for adjacent rotations and \(0\) for other nonidentity rotations.

**3. Reflections.** If \(\lambda_a(i)=r-i\), an allowed edge arises precisely when \(r-i\equiv i\), \(i+1\), or \(i-1\) modulo \(m\). A fixed minimum yields two edges, while each adjacent (but nonfixed) minimum yields one. For odd \(m\), there is exactly one solution to each of these three congruences and hence four allowed edges. For even \(m\), either there are two fixed minima and no adjacent solutions, or there are no fixed minima and two solutions to each of the two adjacent equations. Again \(|E_\lambda|=4\). Every reflection fixes exactly two vertices: one minimum and one maximum if \(m\) is odd, or two vertices from the same level if \(m\) is even. Each fixed vertex contributes a nonzero degree-zero coboundary supported on incident edges; no edge joins two fixed vertices. (For odd \(m\), if fixed indices are \(i,j\), then \(2(i-j)\equiv1\pmod m\), which is neither an edge offset of \(0\) nor \(1\) for \(m\ge3\).) The two coboundary vectors have disjoint nonempty supports, regardless of \(\sigma\). Therefore \(\operatorname{rank}\delta=2\), and \(d(\varphi)=4-2=2\).

**4. Identity and holonomy.** If \(\lambda=\mathrm{id}\), then \(|E_\lambda|=2m\). The coboundary is a weighted incidence matrix on the connected cycle graph with \(2m\) vertices and \(2m\) edges. A kernel vector is a vertex potential obeying
\[
\epsilon(a_i)=\sigma(a_i,b_i)\epsilon(b_i)
=\sigma(a_i,b_{i-1})\epsilon(b_{i-1}).
\]
Nonzero potentials exist if and only if the product of edge ratios around the cycle is \(H(\sigma)=1\). In that event all potentials are scalar multiples of one, giving kernel dimension one. Otherwise the kernel vanishes. By rank-nullity, \(\operatorname{rank}\delta=2m-1\) or \(2m\), respectively, and the two identity cases follow. Multiplying \(\sigma\) by a fractional edge weighting \(\eta(a_i)/\eta(b_j)\) does not change \(H(\sigma)\), proving factorization independence.

**5. Automorphisms and probabilities.** The unit group of \(A\) consists of \(2m\) independent nonzero diagonal entries and \(2m\) arbitrary radical entries, hence has size \((q-1)^{2m}q^{2m}\). Because the poset is connected, its algebra center consists of scalars, so its inner automorphism group has size \(q^{2m}(q-1)^{2m-1}\). Multiplicative automorphisms are specified by \(2m\) nonzero edge weights; the fractional ones account for a subgroup of size \((q-1)^{2m-1}\), leaving exactly \(q-1\) multiplicative classes, distinguished by holonomy. Finally \(|\operatorname{Aut}(P_m)|=2m\), giving the group order above. Each poset symmetry has exactly \(q-1\) equally sized holonomy classes. Among the \(2m(q-1)\) quotient classes there are \(2(q-1)\) adjacent rotations, \(m(q-1)\) reflections, one identity class of trivial holonomy, and the remaining classes have vanishing \(d\). This gives the distribution. The moment identities follow by direct summation. Since \(1/m\to0\), the limiting distribution has equal masses at \(0\) and \(2\), but the contribution \((1/m)m=1\) from adjacent rotations persists in the mean. This proves the final assertion.

## Verification
The accompanying dependency-free `verify.py` independently constructs each incidence algebra's multiplication table, imposes every coefficient of the skew Leibniz identity on an arbitrary linear operator, and computes the dimension of inner skew derivations from the map \(u\mapsto D_u\). It does **not** infer the final dimensions from the cochain classification. It compares these dimensions with the theorem for \(m=3,4,5\), prime fields of orders \(2,3,5\), every rotation and reflection, and two choices of edge weights when available. It separately checks \(900\) finite cochain complexes over those prime fields through \(m=12\), including nontrivial holonomy, and \(51\) exact finite probability/moment identities. The checks complete with `VERIFY_OK`. Finite checks are not a proof for arbitrary \(m\) or nonprime finite fields; the five mathematical steps above supply that proof.

## Relationship to prior work
Fornaroli and Khrypchenko [1] establish the general twisted-cohomology mechanism and explicitly treat a two-crown for certain automorphisms (Examples 3.14–3.15) and one particular symmetry of a four-crown (Example 3.22). These examples already give individual dimensions and are *not* claimed as discoveries here. The present contribution computes, for every \(m\ge3\), every dihedral symmetry and every multiplicative twist, the entire exact dimension spectrum, and then the distribution under the full automorphism group. The rare-large-dimension effect and the consequent mismatch of limiting and expected dimensions are additional consequences of that complete spectrum. The broader cochain framework is an essential ingredient but does not itself state these explicit formulas.

Fornaroli, Khrypchenko and Santulo [2] study Lie automorphisms of incidence algebras and crowns, a different symmetry problem. Krylov and Tuganbaev [3] describe ordinary derivations of incidence algebras; they do not enumerate automorphism-twisted outer derivations of crowns. Fornaroli and Pezzott [4] provide ordinary additive-derivation background. Other results under alternative Hochschild-cohomology terminology might provide broader implicit coverage; publication priority is not independently established.

## Limitations
The result is for \(m\ge3\), finite fields, \(K\)-linear algebra automorphisms, and skew derivations with the stated Leibniz convention. The two-crown is exceptional in its poset-symmetry and overlap pattern and is excluded. The theorem computes quotient **dimensions**, not a basis-free canonical identification of the resulting vector spaces, nor full multiplication in a skew-derivation operator algebra. The asymptotics keep \(q\) fixed while \(m\) grows. The proof uses an established cohomology isomorphism; computations only check finite instances. Priority against all possible equivalent formulations remains subject to independent literature review.

## References
1. É. Z. Fornaroli and M. Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439, first public version 2023-07-17. https://arxiv.org/abs/2307.08439 (Sections 1–3; Theorem 1.3, Corollary 3.8, Examples 3.14, 3.15, 3.22).
2. É. Z. Fornaroli, M. Khrypchenko and E. A. Santulo Jr., *Proper Lie automorphisms of incidence algebras*, arXiv:2108.03765, first public 2021-08-09. https://arxiv.org/abs/2108.03765 (Section 4.3 on crowns).
3. P. Krylov and A. Tuganbaev, *Derivations of Incidence Algebras*, Mathematics 12 (2024), 999, published 2024-03-27. https://www.mdpi.com/2227-7390/12/7/999.
4. É. Z. Fornaroli and R. E. M. Pezzott, *Additive derivations of incidence algebras*, Communications in Algebra 49 (2021), 1816–1828, first public 2020-12-09. https://doi.org/10.1080/00927872.2020.1854775.
