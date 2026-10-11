# Gaussian-binomial tuple-orbit profile of the universal homogeneous cubic space

## Finding
Let \(q=p^e\) with prime \(p>3\), and let \((V,\omega)\) be the countable universal ultrahomogeneous cubic space over \(\mathbb F_q\), where \(\omega\colon V^3\to\mathbb F_q\) is symmetric trilinear. For an ordered \(n\)-tuple \(v=(v_1,\ldots,v_n)\), let \(L_v\colon\mathbb F_q^n\to V\) send the \(i\)-th standard basis vector to \(v_i\), set \(K_v=\ker L_v\), and let \(t_v=L_v^*\omega\). Then two ordered \(n\)-tuples lie in the same automorphism orbit if and only if they have the same kernel \(K_v\) and the same pullback tensor \(t_v\). Equivalently, the orbit set is naturally in bijection with pairs \((K,\bar t)\), where \(K\le\mathbb F_q^n\) and \(\bar t\) is a symmetric trilinear form on \(\mathbb F_q^n/K\). Consequently the number of ordered \(n\)-tuple orbits is \[ b_n(q)=\sum_{r=0}^n {n\brack r}_q\,q^{\binom{r+2}{3}}, \] where \({n\brack r}_q\) is the Gaussian binomial coefficient. In particular, the number of orbits of linearly independent ordered \(n\)-tuples is exactly \(q^{\binom{n+2}{3}}\).

For example, at \(q=5\) the full ordered-tuple orbit counts for \(n=0,1,2,3,4,5\) are
\[
1,\ 6,\ 656,\ 9785156,\ 95368955582656,\ 2910383120155532786132656.
\]

## Assumptions and scope
A cubic space here means a vector space equipped with a symmetric trilinear form. The field is \(\mathbb F_q\) with \(q=p^e\) and \(p>3\). This restriction places the claim directly under the positive-characteristic form of the universal-homogeneous tensor-space theorem of Harman and Snowden. The automorphism group consists of linear bijections preserving \(\omega\).

The theorem counts orbits of all ordered tuples, including repeated coordinates and arbitrary linear dependencies. The rank parameter \(r\) is the dimension of their linear span, not the number of distinct coordinates.

## Proof
Fix an ordered tuple \(v=(v_1,\ldots,v_n)\) and define \(L_v\) as in the finding. Since \(K_v=\ker L_v\), the map \(L_v\) induces a linear isomorphism
\[
\bar L_v\colon \mathbb F_q^n/K_v\longrightarrow \langle v_1,\ldots,v_n\rangle.
\]
The pullback \(t_v=L_v^*\omega\) vanishes whenever one argument lies in \(K_v\), so it descends uniquely to a symmetric trilinear form \(\bar t_v\) on \(\mathbb F_q^n/K_v\).

Suppose tuples \(v\) and \(w\) have the same kernel \(K\) and the same pullback tensor. The coordinate-preserving map
\[
\phi\colon\langle v_1,\ldots,v_n\rangle\longrightarrow\langle w_1,\ldots,w_n\rangle,
\qquad \phi(v_i)=w_i,
\]
is well defined because the linear relations among the coordinates are exactly \(K\). Equality of the pullback tensors says precisely that \(\phi\) preserves the symmetric trilinear form. Thus \(\phi\) is an isomorphism of finite-dimensional cubic subspaces. Ultrahomogeneity of \(V\) extends \(\phi\) to an automorphism of \(V\), so \(v\) and \(w\) are in the same orbit.

Conversely, any automorphism carrying \(v\) to \(w\) preserves all linear relations and preserves \(\omega\), hence preserves both \(K_v\) and \(t_v\). Therefore \((K_v,\bar t_v)\) is a complete orbit invariant.

Every admissible pair \((K,\bar t)\) occurs. Indeed, equip the quotient \(Q=\mathbb F_q^n/K\) with \(\bar t\). By universality, the finite-dimensional cubic space \((Q,\bar t)\) embeds into \(V\). Applying such an embedding to the standard-basis cosets yields an ordered tuple with kernel \(K\) and pullback \(\bar t\).

It remains to count. If \(\dim Q=r\), then kernels \(K\) with \(\dim(\mathbb F_q^n/K)=r\) are the codimension-\(r\) subspaces of \(\mathbb F_q^n\), of which there are \({n\brack r}_q\). A symmetric trilinear form on an \(r\)-dimensional space has one freely chosen field value for each multiset of three basis indices, so the vector space of such forms has dimension
\[
\binom{r+2}{3}.
\]
Hence there are \(q^{\binom{r+2}{3}}\) such forms. Summing over \(r\) proves the formula. For linearly independent tuples, \(K=0\) and \(r=n\), giving \(q^{\binom{n+2}{3}}\).

## Verification
The bundled script `artifacts/verify.py` checks the Gaussian-binomial arithmetic in two independent ways: a product formula and explicit enumeration of reduced-row-echelon subspaces of \(\mathbb F_5^n\) for \(n\le4\). It also verifies the dimension \(\binom{r+2}{3}\) by enumerating multisets of three basis positions and reproduces the displayed \(q=5\) orbit counts. It prints `VERIFY_OK` on success.

The finite computation is only a replay of the counting step. The all-arity orbit classification is proved structurally from universality and ultrahomogeneity.

## Relationship to prior work
Harman and Snowden construct the universal ultrahomogeneous countable cubic space and prove the needed positive-characteristic version when the characteristic exceeds the tensor arity; their paper is classified primarily under MSC 03C35. Neretin independently treats universal ultrahomogeneous cubic spaces over finite fields and proves oligomorphicity of their automorphism groups. These sources provide the structural premises used above.

The inspected primary text and targeted searches did not locate the kernel-plus-pullback classification of ordered tuple orbits or the resulting Gaussian-binomial formula. Nearby indexed work gives exact orbit profiles for other homogeneous structures, but those statements concern different Fraïssé limits and do not imply this formula.

## Limitations
The originality check is necessarily literature-based rather than a proof of historical priority. Because the argument is short once universality and ultrahomogeneity are available, an equivalent formula could exist as unindexed folklore, lecture notes, or under different terminology.

The statement is deliberately restricted to characteristic \(p>3\), matching the directly inspected positive-characteristic theorem used as the primary source. Neretin's finite-field construction is broader, but no broader characteristic claim is needed here.

## References
1. Nate Harman and Andrew Snowden, “Ultrahomogeneous tensor spaces,” *Advances in Mathematics* 443 (2024), 109599; arXiv:2207.09626. First public arXiv version: 2022-07-20. DOI: 10.1016/j.aim.2024.109599.
2. Yury A. Neretin, “Oligomorphic groups, categories of partial bijections, and ultrahomogeneous cubic spaces over finite fields,” arXiv:2308.13247. First public arXiv version: 2023-08-25.
