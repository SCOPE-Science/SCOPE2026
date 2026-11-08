# Two-complete mappings of completely zero-simple semigroups

## Finding

A bijection \(f:S\to S\) of a semigroup is **two-complete** if \(\theta_f(x)=x(f(x))^2\) is also bijective. For every finite completely \(0\)-simple Rees matrix semigroup
\[
S=M^0(G;I,\Lambda;P),
\]
with no all-zero row or column, the following are equivalent:

1. \(S\) has a two-complete mapping.
2. Every sandwich entry \(p_{\lambda i}\) is nonzero.
3. \(S\) is completely regular (every element belongs to a subgroup).

In the positive case there is an explicit involutory mapping \(f\) satisfying \(\theta_f=f\). Indeed, groupwise inversion gives such a mapping on **every** completely regular semigroup, finite or infinite.

There is also a sharp necessary condition for higher powers: if \(k\ge2\) and \(S\) has a \(k\)-complete mapping, with \(x\mapsto x(f(x))^k\) bijective, then every sandwich entry is nonzero. Sufficiency for \(k>2\) is not asserted.

## Assumptions and scope

Let \(G\) be a group and \(I,\Lambda\) nonempty index sets; for the stated equivalence assume all are finite. Let \(P=(p_{\lambda i})\) be a \(\Lambda\)-by-\(I\) matrix over \(G\cup\{0\}\), with no zero rows or columns. The elements of \(S\) are a zero \(0\) and triples \((i,g,\lambda)\), with product
\[
(i,g,\lambda)(j,h,\mu)=
\begin{cases}
(i,gp_{\lambda j}h,\mu),&p_{\lambda j}\ne0,\\
0,&p_{\lambda j}=0.
\end{cases}
\]
A *completely regular* semigroup is a union of groups, not necessarily commutative. Its maximal group \(\mathcal H\)-classes partition its elements. In such a group class \(H_x\), the notation \(x^{-1}_{H_x}\) means the inverse computed with the identity of \(H_x\), not an inverse relative to an adjoined global identity.

## Proof

**Lemma 1 (power-zero obstruction).** Let \(S\) be any semigroup with absorbing zero and \(f\) a \(k\)-complete mapping for an integer \(k\ge1\). Since \(\theta_f(0)=0\), and \(\theta_f\) is injective, we have \(f^{-1}(0)=0\); hence \(f(0)=0\). If \(y\ne0\) and \(y^k=0\), choose \(x=f^{-1}(y)\ne0\). Then \(\theta_f(x)=xy^k=0=\theta_f(0)\), a contradiction. Consequently every nonzero \(y\) has \(y^k\ne0\).

**Lemma 2 (sandwich zeros).** In the specified Rees semigroup, if \(p_{\lambda i}=0\), then every \(y=(i,g,\lambda)\) has \(y^2=0\), hence \(y^k=0\) for each \(k\ge2\). By Lemma 1, none of these semigroups admits a \(k\)-complete mapping for any \(k\ge2\).

**Lemma 3 (groupwise inversion).** Let \(T\) be a completely regular semigroup. For each \(x\in T\), let \(H_x\) be the maximal subgroup containing \(x\). Define \(f(x)=x^{-1}_{H_x}\). Each \(H_x\) is stable under inversion; the group classes partition \(T\), so \(f\) is a bijection and \(f^2\) is the identity. Moreover all products below lie in \(H_x\), where ordinary group laws give
\[
\theta_f(x)=x\bigl(x^{-1}_{H_x}\bigr)^2=x^{-1}_{H_x}=f(x).
\]
Therefore \(f\) is two-complete. This argument is valid for infinite completely regular semigroups as well.

**Lemma 4 (full support is exactly complete regularity).** If every \(p_{\lambda i}\ne0\), then every \(\mathcal H\)-class
\[
H_{i\lambda}=\{(i,g,\lambda):g\in G\}
\]
is a group with identity \((i,p_{\lambda i}^{-1},\lambda)\), and inversion given explicitly by
\[
(i,g,\lambda)^{-1}_{H_{i\lambda}}
=(i,p_{\lambda i}^{-1}g^{-1}p_{\lambda i}^{-1},\lambda).
\]
The zero forms a singleton group with identity zero, so \(S\) is completely regular. Conversely, if any \(p_{\lambda i}=0\), the nonzero elements of that \(\mathcal H\)-class square to zero, and cannot belong to a subgroup. Thus complete regularity is equivalent to full support.

Lemmas 2–4 prove the complete equivalence and supply the explicit construction. There is no assumption that \(G\) be abelian, or that the nonzero entries of \(P\) be equal.

**Sharp change at the first exponent.** The Brandt semigroup \(B_n=M^0(1;[n],[n];\Delta_n)\) for \(n\ge2\) has off-diagonal zeros in its sandwich matrix, hence it has no two-complete mapping. It does admit ordinary one-complete mappings, as shown by the explicit Latin-square correspondence of Araújo et al. (Proposition 6.5). Thus the higher-power obstruction is not simply the obstruction to ordinary complete mappings.

## Verification

The included standalone \(\texttt{checker.py}\) builds Rees multiplication tables over the trivial group, a cyclic group of order two, and the nonabelian symmetric group on three symbols; it includes sparse, rectangular, and nonidentity sandwich patterns. For every full-support example it checks that the explicit local inversion is bijective and satisfies \(x(f(x))^2=f(x)\) for every element; for every sparse example it counts the nonzero square-zero elements. It also exhaustively checks all permutations fixing zero for two order-five examples, confirming that the combinatorial Brandt case has two one-complete and zero two-complete mappings. The test output is embedded as \(\texttt{verification_output.txt}\). These checks corroborate, but do not substitute for, the general proof.

## Relationship to prior work

Araújo, Bentz, Cameron, Hendrey and Kinyon (2026) introduced \(k\)-complete mappings in Definition 15.1 and explicitly posed their classification, including Rees \(0\)-matrix semigroups, in Problem 15.8. Their earlier sections determine ordinary \(k=1\) complete-mapping existence in important semigroup families; their Proposition 6.5 gives the Latin-square classification for Brandt semigroups. Those results are prior work. The present result addresses the first new power \(k=2\): it supplies a full if-and-only-if criterion for finite completely \(0\)-simple semigroups and an elementary, completely explicit construction in the positive case. The source's Problem 15.8 does not state this classification.

## Limitations

The finite zero-simple characterization assumes a regular sandwich matrix with no zero rows or columns. A higher-power necessary obstruction is proved, but no higher-power sufficiency statement for \(k>2\) is made. The existence of a two-complete mapping on arbitrary finite regular semigroups outside the completely regular and completely \(0\)-simple classes is not classified here. Historical priority beyond the sources inspected is not independently established.

## References

- J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1 (first public 2026-08-25), especially Proposition 1.4, Sections 5–7, Proposition 6.5, Definition 15.1 and Problem 15.8. https://arxiv.org/html/2608.25092v1
- Classical Rees theorem and the group \(\mathcal H\)-class structure of completely \(0\)-simple semigroups, as recalled in Section 4 of the same paper.
