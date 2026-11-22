# Every subgroup of an odd-exponent extraspecial group is an automorphism fixed subgroup

## Finding

**Theorem.** Let \(p\) be any odd prime, \(n\ge 1\), and \(G\) any extraspecial group of order \(p^{2n+1}\) and exponent \(p\). For every subgroup \(H\le G\) there is a group automorphism \(\alpha\in\operatorname{Aut}(G)\) whose **entire fixed subgroup** is exactly
\[
\operatorname{Fix}(\alpha)=\{g\in G:\alpha(g)=g\}=H.
\]
In particular, the set of all automorphism fixed subgroups equals the whole subgroup lattice \(L(G)\), for every \(n\ge1\) and every odd prime \(p\).

The proof is constructive and distinguishes subgroups that contain the center from those disjoint from it. It does not require any counting hypothesis or genericity assumption.

## Assumptions and scope

Set \(F=\mathbb F_p\). Let \(V\) be a nondegenerate alternating vector space of dimension \(2n\) over \(F\), with form \(\omega\). Since \(p\) is odd, the group
\[
G(V)=V\times F,\qquad (v,z)(w,t)=\bigl(v+w,z+t+\tfrac12\omega(v,w)\bigr)
\]
models every extraspecial group of this order and exponent: its center and derived subgroup are \(Z=\{(0,z):z\in F\}\), and its commutator pairing is \(\omega\). The standard classification of exponent-\(p\) extraspecial groups identifies each such \(G\) with one of these models. We prove the claim for \(G(V)\), whence it holds under group isomorphism.

For \(\lambda\in F^\times\), a linear map \(M:V\to V\) is a symplectic similitude of multiplier \(\lambda\) when
\[\omega(Mv,Mw)=\lambda\omega(v,w)\quad\text{for all }v,w\in V.\]
Any such \(M\) and any linear functional \(\varphi\in V^*\) define an automorphism
\[
\alpha_{M,\lambda,\varphi}(v,z)=\bigl(Mv,\lambda z+\varphi(v)\bigr).
\]
The group law verifies multiplicativity, and invertibility of \(M\) and \(\lambda\) verifies bijectivity.

## Proof

**Subgroup dichotomy.** Let \(\pi:G(V)\to V\) be the natural quotient map.

If \(Z\le H\), then \(H=\pi^{-1}(U)=U\times F\) for a (not necessarily isotropic) subspace \(U=\pi(H)\le V\). Conversely every such inverse image is a subgroup.

If \(H\cap Z=1\), then \(\pi|_H\) is injective. Since \([H,H]\le H\cap Z=1\), the projection \(U=\pi(H)\) is totally isotropic: \(\omega|_{U\times U}=0\). The group law restricted to \(U\times F\) is then addition, so \(H\) is the graph of an \(F\)-linear functional \(\ell:U\to F\):
\[H=\{(u,\ell(u)):u\in U\}.\]
The trivial subgroup corresponds to \(U=0\). These two cases exhaust all subgroups because \(|Z|=p\).

**Case A: \(Z\le H\).** We build a symplectic transformation \(M\) with \(\ker(M-I)=U\). Let \(R=U\cap U^\perp\). The restriction of \(\omega\) to \(U\) has radical \(R\), so choose a complementary subspace \(W\subseteq U\) on which \(\omega\) is nondegenerate, giving \(U=W\oplus R\). Since \(W\) is nondegenerate, we work in \(W^\perp\), where \(R\) is totally isotropic. Choose an isotropic dual \(R^*\subseteq W^\perp\) paired perfectly with \(R\), and let \(E=(W\oplus R\oplus R^*)^\perp\). Standard symplectic Gram–Schmidt gives
\[
V=W\perp(R\oplus R^*)\perp E.
\]
On \(W\) and \(R\), set \(M=I\). For mutually dual bases \(r_1,\dots,r_s\) of \(R\) and \(r_1^*,\dots,r_s^*\) of \(R^*\), set
\[
M(r_j^*)=r_j^*+r_j\quad(1\le j\le s).
\]
On \(E\), set \(M=-I\). The hyperbolic-plane shears preserve \(\omega\); \(-I\) is symplectic; hence \(M\in\operatorname{Sp}(V,\omega)\). A vector fixed by the shears has no \(R^*\)-component, and, because \(p\ne2\), \(-I\) fixes no nonzero vector of \(E\). Therefore \(\ker(M-I)=W\oplus R=U\). Taking \(\alpha=\alpha_{M,1,0}\) fixes precisely \(U\times F=H\). Empty blocks are permitted, including \(U=V\), in which case \(\alpha=I\).

**Case B: \(H\cap Z=1\).** Write \(H\) as the graph of \(\ell\) over a totally isotropic \(U\). Choose a hyperbolic extension
\[
V=(U\oplus U^*)\perp E,
\]
where \(U^*\) is a totally isotropic dual to \(U\), and \(E\) is nondegenerate. On \(U\), let \(M=I\); on \(U^*\), let \(M=-I\). Relative to a symplectic basis on each hyperbolic plane of \(E\), use the matrix
\[
B=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]
In dimension two, \(B\) has symplectic multiplier \(\det B=-1\), and \(\det(B-I)=-1\ne0\). Thus the orthogonal block sum defines a similitude \(M\) of multiplier \(-1\), with \(\ker(M-I)=U\): the \(U^*\) block has no fixed vector because \(-1\ne1\), and neither does any \(B\)-block. Extend the linear functional \(2\ell\) from \(U\) to \(\varphi\in V^*\), and put
\[
\alpha(v,z)=\bigl(Mv,-z+\varphi(v)\bigr).
\]
Fixed points have \(v\in U\) and satisfy \(2z=\varphi(v)=2\ell(v)\), hence \(z=\ell(v)\). Therefore \(\operatorname{Fix}(\alpha)=H\), as required. This includes \(H=1\) by choosing \(U=0\). \(\square\)

## Verification

A standalone finite-field checker `CHECK.py` is supplied. It enumerates all linear similitudes and central translations for the rank-one model at \(p=3\) and \(p=5\), obtaining respectively 19 and 39 distinct subgroups and the same 19 and 39 distinct fixed-subgroup sets. It tests all subgroup closures at \(p=3\) and verifies six representative four-dimensional symplectic/similitude constructions at both primes. Its success marker is `EXTRASPECIAL_FIXED_SUBGROUP_REALIZATION_OK`.

The proof above, not those finite computations, establishes the theorem for all odd primes and all ranks. The checks separately test the exceptional smallest prime and higher-rank decomposition boundaries.

## Relationship to prior work

Obreja and Tărnăuceanu, *Extending a property of vector spaces to abelian groups* (arXiv:2611.07224v1, first posted 2026-11-04), formulate the finite-group fixed-subgroup realization problem and solve the abelian case. In the introduction they mention the order-27 exponent-3 Heisenberg group as a nonabelian example and leave the arbitrary nonabelian question open. The present theorem establishes the property for the entire infinite family of odd-prime extraspecial exponent-\(p\) groups, strictly beyond that example. The original problem is attributed there to Deaconescu and Walls, *Automotives* (2011).

Related results on images of idempotent endomorphisms of extraspecial groups or Reidemeister-number distributions of Heisenberg automorphisms concern different questions: an idempotent image is a retract and need not represent all automorphism fixed subgroups; a Reidemeister-number count does not determine which individual subgroups arise as fixed subgroups. No exhaustive historical-priority claim is made.

## Limitations

The theorem is restricted to odd primes and extraspecial groups of exponent \(p\); it does not assert the same property for groups of exponent \(p^2\), extraspecial \(2\)-groups, or arbitrary finite nilpotent groups. The 2011 source *Automotives* was not fully accessible for direct theorem comparison; its public summary and bibliographic record were examined, and its potential historical priority remains a residual risk. The separate literature search cannot establish uniqueness or historical priority.

## References

1. A.-N. Obreja and M. Tărnăuceanu, *Extending a property of vector spaces to abelian groups*, arXiv:2611.07224v1 (2026-11-04), https://arxiv.org/html/2611.07224v1.
2. M. Deaconescu and G. Walls, *Automotives*, in *Groups St Andrews 2009 in Bath*, Vol. 1, Cambridge University Press (2011), pp. 228–243, https://doi.org/10.1017/CBO9780511842467.015.
3. *Extraspecial groups*, classification and exponent distinction, https://finitegroupdatabase.com/c/extraspecial.
