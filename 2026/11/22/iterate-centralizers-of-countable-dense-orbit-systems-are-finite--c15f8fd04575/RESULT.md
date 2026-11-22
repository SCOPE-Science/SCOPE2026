# Iterate centralizers of countable dense-orbit systems are finite wreath products on their units

## Finding

Let \(X\) be an infinite countable compact metrizable space with a **finite** nonempty derived set \(X'\), let \(f:X\to X\) be continuous, and suppose \(f\) has a dense forward orbit. For every integer \(m\ge1\), this result classifies the entire continuous centralizer of the sampled map \(f^m\), and determines its group of invertible elements.

Put \(k=|X'|\), \(d=\gcd(k,m)\), \(q=m/d\), and \(\ell=k/d\). For \(0\le b<\ell\), put
\[
N_b=|\{t\in\{0,\dots,q-1\}:t\equiv b\pmod\ell\}|.
\]
Then the group of homeomorphisms commuting with \(f^m\) is
\[
\boxed{\operatorname{Aut}(X,f^m)\cong
(\prod_{b=0}^{\ell-1}\mathfrak S_{N_b})\wr\mathfrak S_d,\qquad
|\operatorname{Aut}(X,f^m)|=d!\left(\prod_{b=0}^{\ell-1}N_b!\right)^d.}
\]
Here \(\mathfrak S_0\) and \(\mathfrak S_1\) denote the trivial group, and the wreath product is the standard permutation wreath product. In particular,
\[
\operatorname{Aut}(X,f)=\{\mathrm{id}\},\qquad
\operatorname{Aut}(X,f^k)\cong\mathfrak S_k.
\]
Thus passing to a time iterate can create arbitrarily large finite symmetry groups even though the original system has no nonidentity homeomorphism commuting with it.

More generally, all continuous maps \(g:X\to X\) satisfying \(gf^m=f^mg\) have the following exact parameterization, which includes nonsurjective maps. Number the isolated points in orbit order \(x_n=f^n(x_0)\), \(n\ge0\). Number the accumulation points \(p_j\), \(j\in\mathbb Z/k\mathbb Z\), so that \(x_{j+kt}\to p_j\) as \(t\to\infty\). Choose arbitrarily \(a_r\in X\) for \(0\le r<m\), and write its phase \(s_r\in\mathbb Z/k\mathbb Z\) when \(a_r=x_t\) (phase \(t\)) or \(a_r=p_j\) (phase \(j\)). These data yield a continuous commutant precisely when
\[
\boxed{s_r-r\equiv s_{r'}-r'\pmod k\quad\text{whenever }r\equiv r'\pmod d.}
\]
For such data define \(\delta_a=s_r-r\pmod k\) for any \(r\equiv a\pmod d\); the unique commuting map is
\[
g(x_{r+mt})=f^{mt}(a_r)\quad(t\ge0),\qquad
 g(p_j)=p_{j+\delta_{j\bmod d}}.
\]

## Assumptions and scope

The topology is compact metrizable and countable; \(X\) is infinite with \(X''=\varnothing\) and \(1\le k=|X'|<\infty\). The map \(f\) is continuous and has one *forward* dense orbit. No invertibility or expansivity is assumed for \(f\). The centralizer means \(\{g\in C(X,X):gf^m=f^mg\}\). Its units are precisely those elements that are homeomorphisms of \(X\). All formulas hold for every positive integer \(m\) and \(k\), including \(k=1\) and \(m=1\).

The cited dense-orbit classification supplies the orbit model, and the assertions about the centralizers and their wreath-product groups are proved below. The theorem applies to arbitrary realizations of the finite-derived-set dense-orbit systems, not only a particular embedded example.

## Proof

**1. The orbit compactification and its phases.** Let \(x_0\) have dense forward orbit. Every isolated point of \(X\) belongs to that orbit, and no iterate can be a periodic point (else the orbit would become finite). Hence the \(x_n=f^n(x_0)\) are pairwise distinct and are exactly the isolated points. The set of accumulation points of the sequence \((x_n)\) is \(X'\): it is contained in \(X'\) because the isolated points appear only once; conversely each point of \(X'\) is approached by infinitely many distinct isolated points, as the isolated points are dense in the countable compact space. By continuity, \(f(X')=X'\), and because \(X'\) is a finite omega-limit set, it is a single periodic orbit. Index its points so that \(x_{j+kt}\to p_j\), where \(f(p_j)=p_{j+1}\) and all indices on \(p\) are modulo \(k\). This convergence follows from finite-omega-limit phase synchronization (Lemma 2.7 of the reference), or by choosing disjoint neighborhoods of the finitely many accumulation points and applying continuity to their successive visits. It determines the topology: a sequence of *distinct* isolated points converges to \(p_j\) exactly when its indices tend to infinity and are eventually congruent to \(j\pmod k\).

**2. Necessity of the phase compatibility.** Fix \(m\ge1\), \(d=\gcd(k,m)\), and a continuous map \(g\) commuting with \(f^m\). Let \(a_r=g(x_r)\) for \(0\le r<m\). Commutation forces \(g(x_{r+mt})=f^{mt}(a_r)\). Any \(g(p_j)\) must itself be periodic for \(f^m\), because \(p_j\) is periodic; no isolated point is periodic, so \(g(p_j)\in X'\). If \(a_r\) has phase \(s_r\), then for every residue class \(j\equiv r\pmod d\) there are arbitrarily large \(t\) with \(r+mt\equiv j\pmod k\). Along such \(t\), continuity forces
\[
 g(p_j)=p_{j+s_r-r}.
\]
The reachable residue classes are precisely those with \(j\equiv r\pmod d\), because \(m/d\) is relatively prime to \(k/d\). For any two \(r,r'\) congruent modulo \(d\), these limits refer to the same \(p_j\), so \(s_r-r\equiv s_{r'}-r'\pmod k\). This yields the asserted condition and determines \(g\) on \(X'\).

**3. Sufficiency and completeness.** Conversely, choose the \(a_r\) satisfying compatibility, and define \(g\) by the displayed formulas. The formulas immediately commute with \(f^m\) on the isolated points; they do so on \(X'\) because adding \(m\) does not change the index modulo \(d\). They are continuous at every isolated point. Suppose \(x_{n_t}\to p_j\). Eventually \(n_t\equiv j\pmod k\), so for each possible \(r\equiv n_t\pmod m\) the image of \(x_{n_t}\) has phase \(j+\delta_{j\bmod d}\). If a selected \(a_r\) is isolated its index after \(f^{mt}\) tends to infinity; if it is in \(X'\) its images are exactly the prescribed accumulation point. Thus \(g(x_{n_t})\to g(p_j)\), proving continuity (and the criterion also covers sequences already in \(X'\)). The values at all isolated points determine a continuous map uniquely because they form a dense subset. Hence this parameterization is complete.

**4. Units are phase-compatible permutations of the first rays.** A surjective commuting map must hit each isolated point \(x_0,\dots,x_{m-1}\). Such a point can be hit only at the beginning of a ray \(x_r,x_{r+m},\dots\) whose initial image \(a_r\) is isolated, since no later ray image has index below \(m\). There are exactly \(m\) source rays, so surjectivity forces \((a_0,\dots,a_{m-1})=(x_{\pi(0)},\dots,x_{\pi(m-1)})\) for a permutation \(\pi\in\mathfrak S_m\). Conversely every such phase-compatible \(\pi\) maps isolated points bijectively. It permutes the \(d\) residue classes modulo \(d\) (otherwise distinct classes would both have to map into one class of size \(m/d\)); on each such class it induces a cyclic translation of the \(k/d\) accumulation phases. Consequently it maps \(X'\) bijectively as well. Its resulting continuous map is a bijection of a compact space onto a Hausdorff space, hence a homeomorphism. Therefore the group of units is
\[
H_{k,m}=\{\pi\in\mathfrak S_m:\pi(r)-r\equiv\pi(r')-r'\pmod k\text{ when }r\equiv r'\pmod d\}.
\]

**5. The wreath-product identification.** Put \(q=m/d\), \(\ell=k/d\), so \(\gcd(q,\ell)=1\). A permutation \(\pi\in H_{k,m}\) induces some \(\beta\in\mathfrak S_d\) on the \(d\) classes; write
\[
 \pi(a+dt)=\beta(a)+d\sigma_a(t),\qquad 0\le a<d,\quad 0\le t<q,
\]
where each \(\sigma_a\in\mathfrak S_q\). Phase compatibility says \(\sigma_a(t)-t\equiv c_a\pmod\ell\), independently of \(t\). Summing this congruence over all \(t\) gives \(0\equiv q c_a\pmod\ell\), and \(\gcd(q,\ell)=1\) implies \(c_a\equiv0\pmod\ell\). Thus \(\sigma_a\) preserves each residue class modulo \(\ell\); conversely all such \(\sigma_a\) and all \(\beta\) satisfy compatibility. Each \(\sigma_a\) belongs to \(\prod_b\mathfrak S_{N_b}\); the group operation permutes these \(d\) copies under \(\beta\). This is the claimed wreath product and gives the exact cardinality. For \(m=1\) all factors are trivial. For \(m=k\), one has \(d=k,q=\ell=1\), so the group is \(\mathfrak S_k\). \(\square\)

## Verification

The standalone arithmetic implementation in `verification/check_centralizers.py` enumerates every permutation of \(\{0,\dots,m-1\}\) for \(1\le m\le7\) and \(1\le k\le10\), tests the phase congruence directly, and compares group cardinalities against the wreath-product formula. It also checks closure under permutation composition, and explicitly tests the ray-construction commutation/phase behavior at sampled points. Every tested parameter pair agrees. These finite checks provide error detection only; the all-parameter conclusion is established by the proof above.

## Relationship to prior work

Pérez-Remolina and Uzcátegui-Aylwin (2026), Proposition 2.5, Lemma 2.7 and Theorem 7.1, establish the dense-orbit model, finite-cycle phase synchronization and conjugacy classification for rank-two countable compacta. They do not state the entire commuting-map semigroups for all iterates or their automorphism group orders. García-Ferreira, Rodríguez-López and Uzcátegui (2014/2016), as well as García-Ferreira, Rodríguez-López and Tomita (2026), study *Ellis semigroups*, which are pointwise closures of the powers of a single map. This is not the full continuous centralizer of \(f^m\), which also contains permutations of disjoint sampled-time rays that do not belong to the iterate closure. General results on centralizers of smooth or invertible systems do not imply the present noninvertible, scattered-space classification. The group-theoretic wreath decomposition is elementary once the dynamical compatibility criterion is established.

## Limitations

The classification assumes \(X'\) is finite and the orbit is forward dense. It makes no assertion for higher Cantor–Bendixson rank, for maps without a dense orbit, or for commutants in the larger space of discontinuous selfmaps. A literature search cannot certify global historical priority: a specialist result not captured by the consulted databases could already imply the theorem. The computer check is finite and is not an independent proof or independent scholarly audit.

## References

1. J. Pérez-Remolina and C. Uzcátegui-Aylwin, *Countable dynamical systems with a dense orbit*, arXiv:2611.17315v1, publicly posted 12 November 2026, https://arxiv.org/abs/2611.17315.
2. S. García-Ferreira, Y. Rodríguez-López and C. Uzcátegui, *Iterates of dynamical systems on compact metrizable countable spaces*, arXiv:1404.6686 (first posted 2014), https://arxiv.org/abs/1404.6686.
3. S. García-Ferreira, Y. Z. Rodríguez-López and A. H. Tomita, *The Ellis semigroups of discrete dynamical systems on compact countable metrizable spaces*, Semigroup Forum 113 (2026), 53–72, DOI:10.1007/s00233-026-10629-3.
