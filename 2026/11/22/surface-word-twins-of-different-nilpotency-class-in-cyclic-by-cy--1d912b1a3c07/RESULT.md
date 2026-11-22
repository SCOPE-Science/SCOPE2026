# Surface-word twins of different nilpotency class in cyclic-by-cyclic prime-power groups

## Finding

Let \(p\) be a prime and \(c,k\ge1\), with \(c\ge2\) when \(p=2\). Set
\[
G_{p,c,k}=\langle a,b\mid a^{p^{c+k}}=b^{p^k}=1,\;bab^{-1}=a^{1+p^c}\rangle.
\]
The derived group is \(\langle a^{p^c}\rangle\cong C_{p^k}\). For every integer \(t\ge1\), define the genus-\(t\) surface word
\[
w_t(x_1,y_1,\ldots,x_t,y_t)=\prod_{i=1}^{t}[x_i,y_i],\qquad [x,y]=xyx^{-1}y^{-1}.
\]
Choose all \(2t\) inputs independently and uniformly in \(G_{p,c,k}\), and identify the derived-group value \(a^{p^cz}\) with \(z\in\mathbb Z/p^k\mathbb Z\). Then its complete output probability is
\[
\boxed{\Pr(w_t=a^{p^cz})=p^{-k}\sum_{s=0}^{k}p^{-2st}c_{p^s}(z).}
\]
Here \(c_1(z)=1\), and for \(s\ge1\), \(c_{p^s}(z)\) is \((p-1)p^{s-1}\) if \(z\equiv0\pmod{p^s}\), is \(-p^{s-1}\) if \(z\equiv0\pmod{p^{s-1}}\) but not modulo \(p^s\), and is zero otherwise. For targets outside the derived group the fiber is empty. Each displayed probability multiplied by \(|G_{p,c,k}|^{2t}=p^{(c+2k)2t}\) is the exact integer fiber cardinality.

Equivalently, for nonzero \(z\) of valuation \(h\in\{0,\ldots,k-1\}\),
\[
\Pr(w_t=a^{p^cz})=p^{-k}\left(1+(p-1)\sum_{s=1}^{h}p^{s-1-2st}-p^{h-2(h+1)t}\right),
\]
and at the identity,
\[
\Pr(w_t=1)=p^{-k}\left(1+(p-1)\sum_{s=1}^{k}p^{s-1-2st}\right).
\]
All derived-group elements occur, and the probabilities are independent of \(c\). More strongly they equal the full corresponding distributions for the class-two Heisenberg group \(H_k=\operatorname{UT}_3(\mathbb Z/p^k\mathbb Z)\), under the natural identification of cyclic derived groups.

Let \(U_k\) be uniform measure on \(C_{p^k}\). For all \(p,k,t\) in the stated domain,
\[
\left|\|\Pr(w_t\in\cdot)-U_k\|_{\rm TV}-(1-p^{-1})p^{-2t}\right|
\le\frac{(1-p^{-1})p^{-4t}}{1-p^{-2t}}.
\]
Consequently the leading decay of total-variation distance is uniform in \(k\) at fixed prime \(p\).

In particular, for any odd prime \(p\) and \(k\ge2\), the two groups
\[
X_{p,k}=G_{p,1,k}\times C_{p^{k-1}},\qquad H_k=\operatorname{UT}_3(\mathbb Z/p^k\mathbb Z)
\]
have equal order \(p^{3k}\) and cyclic derived groups of order \(p^k\), and have **the same exact fiber cardinality for every target of every \(w_t\)** under an identification of their derived groups; nevertheless their nilpotency classes are respectively \(k+1\) and \(2\). Thus this entire natural family of surface-word distributions, even with absolute fiber sizes and group order held fixed, does not detect nilpotency class.

## Assumptions and scope

The parameters \(p\) and \(k\) are arbitrary prime and positive integer, respectively. The action parameter is \(c\ge1\) for odd \(p\), or \(c\ge2\) for \(p=2\); the excluded binary case \(c=1\) is not asserted. The commutator orientation is as above; reversing it negates the target parameter but leaves the valuation-dependent distribution unchanged. The group is a split semidirect product. The product \(w_t\) uses disjoint variables, not iterated Engel commutators. The equal-order different-class examples are asserted for odd primes and \(k\ge2\).

## Proof

**1. Well-defined action and derived subgroup.** In the indicated parameter range the elementary lifting-the-exponent calculation gives
\[
\nu_p\big((1+p^c)^{p^j}-1\big)=c+j\qquad(j\ge0).
\]
For odd \(p\) this follows by expanding a \(p\)th power inductively starting at valuation \(c\ge1\); for \(p=2\) it holds from valuation \(c\ge2\) by the same binomial argument (the first term has valuation \(c+1\), all others strictly larger). Therefore \(\lambda=1+p^c\) has multiplicative order exactly \(p^k\) modulo \(p^{c+k}\), so the presentation defines the indicated semidirect product of order \(p^{c+2k}\). The commutator \([b,a]=a^{p^c}\), and all commutators lie in the normal cyclic subgroup; hence \(G' =\langle a^{p^c}\rangle\) has order \(p^k\).

**2. A bijective principal-unit coordinate.** In additive pair coordinates \((u,v)\in \mathbb Z/p^{c+k}\mathbb Z\times\mathbb Z/p^k\mathbb Z\), multiplication is
\[
(u,v)(s,t)=(u+\lambda^v s,v+t).
\]
The function
\[
L(v)=\frac{\lambda^v-1}{p^c}\pmod{p^k}
\]
is a bijection from \(\mathbb Z/p^k\mathbb Z\) to itself: the \(p^k\) powers of \(\lambda\) enumerate the complete group of principal units modulo \(p^{c+k}\), which has exactly \(p^k\) members. In particular \(L(v)\) is uniform when \(v\) is uniform.

**3. Distributional reduction to a determinant.** Comparing \((u,v)(s,t)\) and \((s,t)(u,v)\) gives
\[
[(u,v),(s,t)]=(p^c(L(v)s-L(t)u),0).
\]
As \(u,s\pmod{p^k}\) and \(v,t\pmod{p^k}\) are independent uniform variables, the resulting derived-group coordinate has exactly the distribution of the determinant of a uniform two-by-two matrix over \(R=\mathbb Z/p^k\mathbb Z\). For \(H_k\), multiplication of upper unitriangular matrices shows that the central commutator coordinate is \(uv'-u'v\), the same determinant. Independent commutators produce independent copies of this law, and their products add the central/derived coordinates. Thus \(w_t\) in either group is a sum of \(t\) independent determinants in \(R\).

**4. Exact Fourier inversion.** For an additive character \(\chi\) of \(R\) of exact order \(p^s\), let \(D=UV'-U'V\), with four independent uniform variables. Summing first in \(V'\) for fixed \(U\) gives \(\mathbb E\chi(UV')=p^{-s}\), since the character is trivial on \(UR\) exactly when \(U\equiv0\pmod{p^s}\). Independence then gives
\[
\mathbb E\chi(D)=p^{-2s},\qquad\mathbb E\chi(D_1+\cdots+D_t)=p^{-2st}.
\]
There are \((p-1)p^{s-1}\) characters of order \(p^s\), for \(s\ge1\); their sum at \(z\) is precisely the Ramanujan sum \(c_{p^s}(z)\). Fourier inversion yields the main formula and its zero/nonzero valuation specializations. Nonzero targets occur already at \(t=1\), because \(L(v)\) may be one and \(u\) may be zero; for general \(t\) the remaining commutators may be the identity.

**5. Sharp mixing estimate.** The \(s=1\) component of \(\Pr(w_t=\cdot)-U_k\) is \(p^{-k}p^{-2t}c_p(\cdot)\), and its total-variation norm is \((1-p^{-1})p^{-2t}\), because the average of \(|c_p|\) over \(R\) equals \(2(1-p^{-1})\). For each \(s\ge2\) the average of \(|c_{p^s}|\) is also \(2(1-p^{-1})\). The triangle and reverse triangle inequalities, followed by the geometric sum over \(s\ge2\), give the stated uniform error bound.

**6. Different classes at equal order.** The lower central series of \(G_{p,c,k}\) satisfies \(\gamma_j=\langle a^{p^{(j-1)c}}\rangle\) for \(j\ge2\), until this subgroup becomes trivial, so its nilpotency class is \(1+\lceil k/c\rceil\). For odd \(p\), \(X_{p,k}\) therefore has class \(k+1\); its central direct factor does not alter the derived group or normalized commutator-word law. Both \(X_{p,k}\) and \(H_k\) have order \(p^{3k}\), so equal normalized target probabilities imply equal absolute fiber cardinalities. Their different nilpotency classes prove they are nonisomorphic.

## Verification

A standalone standard-library checker named `verify.py` constructs the semidirect-product multiplication and inverses literally, enumerates every ordered pair, and compares each central fiber with the rational Ramanujan formula. It also verifies convolution formulas for \(t=2,3\) and independently counts determinant targets in small Heisenberg groups. The included `checks.txt` contains the actual output. Tests cover \((p,c,k)=(3,1,1),(3,1,2),(3,2,1),(2,2,1),(2,2,2),(5,1,1),(3,3,1)\) and Heisenberg pairs \((p,k)=(2,1),(2,2),(3,1),(3,2)\). All tests passed. Exhaustive finite tests supplement, but do not replace, the parameter-uniform proof.

For example, \((p,c,k)=(3,1,2)\) gives a group of order \(243\) and single-commutator fiber sizes \(8505\) at the identity, \(7776\) at the two nonzero targets divisible by \(3\), and \(5832\) at each of the six unit targets. These nine counts sum to \(243^2\).

## Relationship to prior work

Moradipour, Sarmin and Erfanian computed the conjugacy-class number and commuting probability of finite metacyclic prime-power groups in 2012; that is the identity-target, one-commutator specialization and is not claimed here as new. Levy's 2016 study supplies the classical character-theoretic framework for products of commutators and evaluates special families of exponent-\(p\) groups. The present family has exponent exceeding \(p\), with members of arbitrarily large nilpotency class. Camina, Iñiguez and Thillaisundaram (2020) give a general two-character-degree fiber theorem, while Camina, Cocke and Thillaisundaram (2023) establish a lower-bound theorem for broad metacyclic word maps; those results do not state the present all-genus exact, identified derived-target distribution or its same-order different-class construction. The determinant Fourier calculation uses standard finite character orthogonality; the claim is the explicit cross-family word-law identification and its consequences, not novelty of determinant counting or Ramanujan sums.

## Limitations

No assertion is made about arbitrary group words, iterated commutators, non-split metacyclic groups, or \(p=2,c=1\). The matched distributions are those of products of independent commutators, not a group isomorphism or an identification of all word maps. Literary priority remains subject to a possible broader unidentified theorem implying the full distributional equivalence. No independent mathematical audit has been carried out.

## References

1. M. Levy, *Enumerating fibres of commutator words over p-groups*, arXiv:1602.04093 (first posted 2016-02-12), https://arxiv.org/abs/1602.04093 .
2. K. Moradipour, N. H. Sarmin, A. Erfanian, *Conjugacy classes and commuting probability in finite metacyclic p-groups*, ScienceAsia 38 (2012), 113–117, doi:10.2306/scienceasia1513-1874.2012.38.113, https://people.utm.my/nizasarmin/wp-content/uploads/sites/980/2015/03/Conjugacy-classes-and-commuting-probability-in-finite.pdf .
3. R. D. Camina, A. Iñiguez, A. Thillaisundaram, *Word problems for finite nilpotent groups*, Arch. Math. 115 (2020), 599–609, https://doi.org/10.1007/s00013-020-01504-w .
4. R. D. Camina, W. L. Cocke, A. Thillaisundaram, *The Amit–Ashurst conjecture for finite metacyclic p-groups*, Eur. J. Math. 9 (2023), article 46, https://doi.org/10.1007/s40879-023-00644-x .
