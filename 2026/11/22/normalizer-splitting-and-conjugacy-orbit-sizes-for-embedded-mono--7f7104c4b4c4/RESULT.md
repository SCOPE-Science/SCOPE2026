# Normalizer splitting and conjugacy-orbit sizes for embedded monogenic inverse submonoids

## Finding
Let \(n\ge0\), let \(\mathcal I_n\) denote the symmetric inverse monoid of all partial bijections of \([n]\), and let \(S_n\) act by conjugation. For \(f\in\mathcal I_n\), put \(H_f=\langle 1_n,f,f^{-1}\rangle\), an **embedded** inverse submonoid including the ambient full identity. Decompose \(f\) into disjoint directed cycles and directed chains, counting an isolated vertex on which \(f\) is undefined as a one-vertex chain. Let \(a_d\) count directed cycles with \(d\) vertices and \(b_l\) chains with \(l\) vertices, so \(\sum_{d\ge1}d a_d+\sum_{l\ge1}l b_l=n\). Let \(m=\operatorname{lcm}\{d:a_d>0\}\), with empty least common multiple equal to one. Write
\[
Z(f)=\prod_{d\ge1}d^{a_d}a_d!\,\prod_{l\ge1}b_l!,\quad
C(f)=\left(\prod_{d\ge1}C_d\wr S_{a_d}\right)\times\left(\prod_{l\ge1}S_{b_l}\right),
\]
where zero multiplicities contribute trivial factors. The group \(C(f)\) is the centralizer of \(f\) in \(S_n\), of order \(Z(f)\).

**Normalizer theorem.** The normalizer \(N_{S_n}(H_f)=\{\sigma\in S_n:\sigma H_f\sigma^{-1}=H_f\}\) splits as
\[
\boxed{N_{S_n}(H_f)\cong
\begin{cases}
C(f)\rtimes C_2,&\text{if some }b_l>0\text{ with }l\ge2,\\
C(f)\rtimes(\mathbb Z/m\mathbb Z)^\times,&\text{otherwise}.
\end{cases}}
\]
In the first case the nontrivial element of \(C_2\) simultaneously inverts each cyclic rotation and fixes each symmetric-group factor. In the second case a unit \(u\) raises every cyclic rotation to its \(u\)-th power and fixes each symmetric-group factor. These actions use the displayed canonical component coordinates; the factors for length-one cycles and undefined singletons behave in the evident trivial way. Therefore
\[
\boxed{|N_{S_n}(H_f)|=Z(f)\begin{cases}2,&\exists l\ge2:b_l>0,\\\varphi(m),&\forall l\ge2:b_l=0.\end{cases}}
\]

Two embedded monogenic inverse submonoids are conjugate by \(S_n\) if and only if their generating partial bijections have the same pair of cycle and chain vertex-length partitions. Thus every bipartition \((\lambda,\mu)\) of \(n\) determines exactly one conjugacy orbit, with orbit size \(n!/(Z(f)\,g(f))\) where \(g(f)\) is two or \(\varphi(m)\) as above. The number of such orbits is \(\sum_{r=0}^np(r)p(n-r)\), where \(p(0)=1\). This last bipartition formula is a consequence of the *known* conjugacy classification for partial injections, not asserted as a new partition identity. The new structural claim is the full split normalizer and corresponding exact orbit sizes **for the generated embedded submonoids**, including every chain/cycle boundary case.

## Assumptions and scope
All sets and groups here are finite. A directed chain of vertex-length \(l\) has \(l-1\) arrows, so \(b_1\) counts points outside both domain and image of \(f\). A directed cycle of length one is a fixed point in the domain, not a one-vertex undefined chain. Composition and inversion of partial maps use their ordinary definitions, and conjugation by full permutations fixes \(1_n\). For \(n=0\), \(S_0\) is the trivial group and the theorem gives one conjugacy orbit. For the empty partial map on \(n>0\), \(m=1\), \(C(f)=S_n\), and \(N_{S_n}(H_f)=S_n\). Units of \(\mathbb Z/1\mathbb Z\) are interpreted as the trivial group, so \(\varphi(1)=1\).

## Proof
**1. Generator fibers.** Let \(g\in\mathcal I_n\) generate the same inverse submonoid as \(f\). In each chain or cycle component, every nonempty word in \(f,f^{-1}\) is, wherever defined, the signed-exponent displacement by its exponent sum \(t\in\mathbb Z\). If a genuine chain exists and \(|t|\ge2\), that word has strictly fewer arrows on the chain than \(f\), hence smaller total rank; if \(t=0\) it is an idempotent, and cannot generate the nonidempotent \(f\). If \(t=1\) or \(-1\), the word is a restriction of \(f\) or \(f^{-1}\), respectively, since traversing a neighboring edge is necessary for the displacement. Now \(f\) and \(g\) generate each other, so rank monotonicity under multiplication forces \(\operatorname{rank}(f)=\operatorname{rank}(g)\). Such a restriction has equal rank only when it equals \(f\) or \(f^{-1}\). These are different because a genuine chain is oriented. Thus the inverse-generator fiber is precisely \(\{f,f^{-1}\}\).

If there are no genuine chains, \(f\) is a permutation of its support \(D=\operatorname{dom}(f)=\operatorname{im}(f)\), of order \(m\). The nonambient part of \(H_f\) is its cyclic local group (including the partial identity on \(D\)); any other generator has the same support and is \(f^u\) for a unit \(u\in(\mathbb Z/m\mathbb Z)^\times\). This remains valid when \(m=1\), and when \(D=[n]\) the ambient identity and local identity coincide. This generator-fiber fact is also established in the previously published embedded-submonoid studies listed below; it is used here, not claimed as the main novelty.

**2. Reduction of normalizers to centralizers.** For \(\sigma\in S_n\), conjugation is an inverse-monoid automorphism of \(\mathcal I_n\) that fixes \(1_n\). Hence \(\sigma\) normalizes \(H_f\) exactly when \(\sigma f\sigma^{-1}\) is in the generating fiber just classified. The kernel of its action on this fiber is \(C_{S_n}(f)\). In particular the quotient of the normalizer by the centralizer embeds into \(C_2\) in the chain case and into \((\mathbb Z/m\mathbb Z)^\times\) in the group case.

**3. The centralizer.** A permutation commuting with \(f\) must preserve defined and undefined transitions and therefore sends each directed cycle to a cycle of the same vertex-length, and each directed chain to a chain of the same vertex-length. A commuting bijection between cycles of length \(d\) has exactly \(d\) possible phase rotations; between two directed chains there is exactly one map (position-to-position). All such choices are independent. It follows that
\[
C_{S_n}(f)\cong\prod_d(C_d\wr S_{a_d})\times\prod_l S_{b_l},\qquad|C_{S_n}(f)|=Z(f).
\]
This includes length-one components and every zero-multiplicity boundary.

**4. Explicit splitting.** Choose coordinates \((d,i,j)\) on each cycle with \(j\in\mathbb Z/d\mathbb Z\) and \(f(d,i,j)=(d,i,j+1)\). On a chain of length \(l\), choose \((l,i,j)\) with \(1\le j\le l\) and its arrows \(j\mapsto j+1\). If any chain has length at least two, define an involution \(r\in S_n\) by \(r(d,i,j)=(d,i,-j)\) on cycles and \(r(l,i,j)=(l,i,l+1-j)\) on chains. Then \(rfr^{-1}=f^{-1}\). Conjugation by \(r\) reverses each cyclic rotation while leaving component-index permutations unchanged. Moreover \(r\notin C_{S_n}(f)\). By Step 2, \(C_{S_n}(f)\) and \(r\) generate the entire normalizer, giving the asserted semidirect product.

If no chain has length greater than one, for each \(u\in(\mathbb Z/m\mathbb Z)^\times\) define \(s_u(d,i,j)=(d,i,uj)\) on cycles and fix all undefined singleton vertices. Then \(s_uf s_u^{-1}=f^u\), and \(u\mapsto s_u\) is a homomorphism with \(s_us_v=s_{uv}\) and trivial intersection with the centralizer. It gives a section of the normalizer quotient, and conjugation by \(s_u\) raises every cyclic rotation to its \(u\)-th power while fixing permutations of cycle and singleton components. This proves the second splitting and both order formulas.

**5. Conjugacy orbits.** Conjugating \(f\) by a full permutation preserves the pair of cycle/chain partitions, and any two partial injections with the same pair are conjugate by matching their constituent directed components. The generating fiber in Step 1 consists of inverses or coprime powers, which also preserve those partitions. Therefore \(H_f\) and \(H_g\) lie in the same \(S_n\)-orbit precisely when their generating maps have the same bipartition. There is one orbit for every pair of partitions with total size \(n\). Orbit-stabilizer and Steps 3–4 give its size \(n!/(Z(f)g(f))\). All assertions hold simultaneously for every \(n\ge0\).

## Verification
The standalone `verify.py` exhaustively lists the \(1,2,7,34,209,1546\) partial bijections on \(n=0,1,2,3,4,5\) points, respectively. It constructs each distinct inverse submonoid by actual closure under both generators and ambient identity; checks generator fiber sizes; separately forms the full set of its \(S_n\)-conjugates; and compares the orbit size with the formula for the normalizer. The verified numbers of distinct submonoids are \(1,2,6,24,126,838\); the corresponding conjugacy-orbit counts are \(1,2,5,10,20,36\). Run `python3 verify.py` with a standard Python 3 interpreter; success prints `MONOGENIC_INVERSE_NORMALIZER_PROFILE_VERIFIED`. These are finite consistency checks; the infinite assertions rest on the proof above.

## Relationship to prior work
Elliott, Levine and Mitchell (2023) count **isomorphism types** of monogenic inverse submonoids and establish their chain/cycle parameters. Araújo, Kinyon and Konieczny (2018), especially their symmetric-inverse-monoid conjugacy theorem, establish the cycle-and-chain classification of **elements** and hence the bipartition count; neither is a new observation here. Two published later embedded-submonoid studies explicitly establish generator rigidity, exact *labelled* submonoid counts and distributions by maximal chain and cycle period, but leave their conjugacy orbits unclassified. Combining their generator-fiber information with the classical element-conjugacy classification does establish the **number** of submonoid orbits. It does not, by itself, supply the explicit **normalizer group**, its splitting, the action on the centralizer factors or the size of every orbit. Those exact structural invariants are the present contribution. Our published-finding corpus semantic searches, accessible full published treatments and relevant primary works did not identify the same split normalizer statement. This is limited priority evidence, not a proof that it has never appeared under other terminology.

## Limitations
The statement concerns normalizers *inside the ambient symmetric group* of actual one-generated inverse submonoids with ambient identity, not abstract automorphism groups of those submonoids or normalizers inside the full transformation monoid. The purely combinatorial bipartition count and the classical component-centralizer factors are known ingredients rather than separately claimed novelties. Direct enumeration ends at \(n=5\), and an independent mathematical audit has not been performed. A historical specialization of general permutation centralizer/normalizer theory or old monogenic-inverse-semigroup literature may imply the displayed splitting; the search of that larger literature is not exhaustive.

## References
1. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (first posted 2023-03-22), https://arxiv.org/abs/2303.12387, DOI:10.1080/00927872.2023.2214821.
2. J. Araújo, M. Kinyon and J. Konieczny, *Conjugacy in inverse semigroups*, arXiv:1810.03208 (2018), https://arxiv.org/abs/1810.03208.
3. *Embedded monogenic inverse submonoids: a chain-period spectrum and a half-density law*, publicly available 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-embedded-monogenic-inverse-submonoids-a-chain-period-spectrum-an--d8394c30e54e.
4. *Embedded monogenic inverse submonoids: exact census and a square-root nilpotent law*, publicly available 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-embedded-monogenic-inverse-submonoids-exact-census-and-a-square--77e542c8edb6.
