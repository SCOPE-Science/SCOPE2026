# Modular non-smoothness and sharp arithmetic thresholds for maximal-index evolution-algebra automorphisms

## Finding

Fix any field \(K\) and integer \(n\ge4\). Consider the nonassociative, commutative evolution algebra \(E_{\mathbf b}\) with natural basis \(e_1,\ldots,e_n\), products \(e_i e_j=0\) for distinct indices, and
\[
e_i^2=e_{i+1}+\sum_{j=i+2}^{n-1}b_{ij}e_j\quad(1\le i\le n-2),\qquad e_{n-1}^2=e_n,\qquad e_n^2=0.
\]
Let \(S=\{(i,j): b_{ij}\ne0\}\). If \(S\ne\varnothing\), define the positive integer
\[
g=\gcd_{(i,j)\in S}(2^{j-1}-2^i).
\]
The full automorphism **group scheme** (not merely its field-valued points) is
\[
\operatorname{Aut}(E_{\mathbf b})\simeq
\begin{cases}
\mathbb G_a\rtimes\mu_g,&S\ne\varnothing,\\
\mathbb G_a\rtimes\mathbb G_m,&S=\varnothing,
\end{cases}
\]
where the multiplicative factor acts on the additive factor by the character \(t\mapsto t^{2^{n-1}-1}\). In particular, for \(S\ne\varnothing\), the representing coordinate ring is \(K[t,t^{-1},z]/(t^g-1)\). This identification holds functorially on commutative \(K\)-algebras, including nonreduced coefficient algebras.

If \(\operatorname{char}K=p>0\), the group scheme is non-smooth precisely when \(S\ne\varnothing\) and \(p\mid g\), with
\[
\dim_K\operatorname{Der}(E_{\mathbf b})=
\begin{cases}
2,&S=\varnothing,\\
1+\mathbf 1_{p\mid g},&S\ne\varnothing.
\end{cases}
\]
Thus in characteristic \(2\), every non-chain member of this normalized family is non-smooth, with one-dimensional reduced automorphism group and two-dimensional derivation space. For odd \(p\), set \(r=\operatorname{ord}_p(2)\). No such non-smooth member occurs in dimension \(n<r+3\), and one occurs in every dimension \(n\ge r+3\). This dimension threshold is sharp.

Over \(K=\mathbb F_q\), the number of ordinary automorphisms is \(q(q-1)\) if \(S\) is empty and \(q\gcd(g,q-1)\) otherwise. These point counts do not detect the infinitesimal defect when \(p\mid g\).

## Assumptions and scope

The field \(K\) has arbitrary characteristic; the assertions concern only the explicitly displayed normalized family. This family has codimension-one square \(E_{\mathbf b}^2\) and maximal nilpotency index \(2^{n-1}+1\). No classification of all evolution algebras up to changes of natural basis is asserted. The group scheme means the functor taking each commutative unital \(K\)-algebra \(R\) to the \(R\)-algebra automorphisms of \(E_{\mathbf b}\otimes_KR\). The group dimension is the Krull dimension of that representing group scheme; derivation dimension is the tangent-space dimension at its identity.

## Proof

**Intrinsic flag.** Put \(V_i=\operatorname{span}_R(e_i,\ldots,e_n)\) after any extension from \(K\) to a commutative \(K\)-algebra \(R\). The products \(V_i V_i\) generate exactly \(V_{i+1}\) for \(1\le i<n\), since the leading coefficients in the displayed multiplication table are units and all additional terms are farther along the flag. Therefore each \(V_i\) is characteristic and every automorphism is upper triangular relative to this basis, with diagonal entries \(t_i\in R^\times\).

**Orthogonality and terminal coordinate.** Write \(\phi(e_i)=\sum_{j\ge i}a_{ji}e_j\). For \(i<j<n\), the coefficient of \(e_{j+1}\) in \(\phi(e_i)\phi(e_j)=0\) is \(a_{ji}t_j\), because \(\phi(e_j)\) has no terms below \(e_j\), and higher-index squares cannot yield \(e_{j+1}\). Hence \(a_{ji}=0\). Consequently \(\phi(e_i)=t_i e_i+u_i e_n\) for \(i<n\) and \(\phi(e_n)=t_n e_n\). Compare the \(e_{i+1}\)-coefficients of \(\phi(e_i^2)=\phi(e_i)^2\): \(t_{i+1}=t_i^2\) for every \(1\le i<n\). Thus \(t_i=t^{2^{i-1}}\) with \(t=t_1\). Comparing the \(e_n\)-coefficients successively from \(i=n-2\) downward shows \(u_{n-1}=u_{n-2}=\cdots=u_2=0\). Only \(u_1\) is free, because \(e_n\) annihilates the entire algebra.

**All coefficient equations.** The \(e_j\)-coefficient with \(i+2\le j\le n-1\) is \(b_{ij}(t_i^2-t_j)\), so the remaining conditions are exactly \(t^{2^{j-1}-2^i}=1\) for \((i,j)\in S\). Because \(t\) is a unit, these conditions are equivalent, over every commutative \(R\), to \(t^g=1\) by Bézout's identity. If \(S\) is empty, there is no restriction beyond invertibility.

Thus all automorphisms and only automorphisms have
\[
\phi_{t,u}(e_1)=t e_1+u e_n,\qquad
\phi_{t,u}(e_i)=t^{2^{i-1}}e_i\quad(2\le i\le n),
\]
where \(u\in R\), \(t\in R^\times\), with \(t^g=1\) when applicable. The matrix is triangular with unit diagonal, so each such algebra endomorphism is an automorphism. Set \(z=u/t\). Composition becomes
\[
(t,z)\cdot(s,y)=(ts,\,z+t^{2^{n-1}-1}y),
\]
which proves the claimed semidirect product functorially and therefore the coordinate rings.

**Smoothness and arithmetic onset.** The multiplicative factor \(\mu_g\) is smooth in characteristic \(p\) exactly when \(p\nmid g\); in characteristic \(p\), its tangent equation at \(t=1+\varepsilon h\) is \(gh=0\) in \(K[\varepsilon]/(\varepsilon^2)\). This yields precisely the displayed derivation dimensions. In characteristic \(2\), every weight is \(2^i(2^{j-1-i}-1)\), hence even. For odd \(p\), a weight is divisible by \(p\) exactly when \(r=\operatorname{ord}_p(2)\) divides \(j-1-i\). This positive integer is at most \(n-3\). Accordingly no nonempty support can have \(p\mid g\) below \(r+3\); at \(n=r+3\) and higher the single nonzero coefficient \(b_{1,r+2}=1\) gives \(g=2(2^r-1)\) divisible by \(p\). The asserted threshold follows. Finally, in \(\mathbb F_q^\times\) the equation \(t^g=1\) has \(\gcd(g,q-1)\) solutions, and \(u\) is arbitrary, giving the point-count formula.

## Verification

The standalone `check.py` constructs the multiplication laws and all derivation linear equations independently and compares their finite-field solution dimensions with the theorem. It checks the proposed maps by direct multiplication in ten field/dimension/support configurations; it also enumerates every one of the \(2^{16}\) linear transformations in dimension four over \(\mathbb F_2\) for the chain and first non-chain cases. Dual-number checks over \(\mathbb F_p[\varepsilon]/(\varepsilon^2)\) exhibit the predicted infinitesimal automorphisms in the first examples at primes \(2,3,5\), and their absence in the tested characteristic-three nonresonant case. Reproduce with `python3 check.py`; `check_output.txt` records the successful replay. These finite checks corroborate, but do not replace, the functorial proof.

## Relationship to prior work

Casas, Ladra, Omirov, and Rozikov established the maximal-index criterion and upper-triangular evolution-algebra models (first public version 8 August 2012). Mukhamedov, Khakimov, Omirov, and Qaralleh's characteristic-zero analysis already established the **ordinary automorphism normal form and gcd-of-weights constraint**, notably Theorem 5.2 (2018 preprint, 2019 journal). Those results are prerequisites, not new claims here. The present result concerns the entire automorphism *group scheme* for this normalized class in arbitrary characteristic, including nonreduced test rings, and its sharp characteristic-dependent smoothness cutoff. In particular, extending a characteristic-zero automorphism count alone does not give the non-smoothness or the derivation-dimension jump. Related work on perfect evolution algebras assumes a nondegenerate square and does not imply these nilpotent cases.

## Limitations

The normalization restricts the multiplication-table coefficients of \(e_n\) to zero except \(e_{n-1}^2=e_n\); a more general maximal-index algebra need not already have this displayed presentation without further basis changes. The result does not classify isomorphism classes or automorphism schemes of every unnormalized maximum-index evolution algebra. A distinct historical treatment of positive-characteristic group schemes could imply the theorem; the comparison below is limited to the named inspected sources and available indexed results. Smoothness is a statement about the group scheme, not the finite group of \(K\)-rational points. Only the functorial algebraic argument establishes the infinite-family theorem.

## References

1. J. M. Casas, M. Ladra, B. A. Omirov, U. A. Rozikov, *On nilpotent index and dibaricity of evolution algebras*, arXiv:1208.1709, version 1 posted 8 August 2012. https://arxiv.org/abs/1208.1709
2. F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285, version 1 posted 25 May 2018; Journal of Algebra and Its Applications 18 (2019), 1950233, Theorem 5.2. https://arxiv.org/abs/1805.10285
3. American Mathematical Society, *Mathematics Subject Classification 2020*, 17A36, automorphisms and derivations of nonassociative algebras. https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=17Axx
