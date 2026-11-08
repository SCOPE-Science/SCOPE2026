# Doubling-orbit normal forms and automorphism orders of finite-field permutation evolution algebras

## Finding
Let \(q\) be any prime power, and let \(E\) range over the \(n\)-dimensional \(\mathbb F_q\)-evolution algebras having a natural basis with \(e_i^2=c_i e_{\sigma(i)}\), where \(c_i\in\mathbb F_q^\times\) and \(\sigma\in S_n\). These are precisely the evolution algebras with an invertible monomial structure matrix. Put \(d_\ell=\gcd(q-1,2^\ell-1)\) and \(H_\ell=\mathbb F_q^\times/(\mathbb F_q^\times)^{2^\ell-1}\), a cyclic group of size \(d_\ell\).

A directed cycle of length \(\ell\), written \(e_j^2=c_j e_{j+1}\) with indices modulo \(\ell\), has invariant the orbit under squaring in \(H_\ell\) of
\[
 I_\ell=[c_0^{2^{\ell-1}}c_1^{2^{\ell-2}}\cdots c_{\ell-2}^{2}c_{\ell-1}}].
\]
Two such algebras are isomorphic if and only if for each \(\ell\) the multisets of these squaring orbits agree. Thus a complete normal form is a multiset of pairs (cycle length, squaring orbit).

For a cycle whose squaring orbit has length \(h\), its full algebra automorphism group has order \(d_\ell\ell/h\). If an algebra contains \(m_{\ell,O}\) cycles of length \(\ell\) and orbit type \(O\), and \(h_O=|O|\), then
\[
 |\operatorname{Aut}(E)|=\prod_{\ell,O}\left(\frac{\ell d_\ell}{h_O}\right)^{m_{\ell,O}}m_{\ell,O}!.
\]
Every automorphism is accounted for. The number \(a_\ell(q)\) of isomorphism types of single cycles of length \(\ell\), and the generating function of all types, are
\[
 a_\ell(q)=\frac1\ell\sum_{r=0}^{\ell-1}\gcd(d_\ell,2^r-1),\qquad
 \sum_{n\ge0}K_n(q)t^n=\prod_{\ell\ge1}(1-t^\ell)^{-a_\ell(q)}.
\]
Here \(\gcd(d_\ell,0)=d_\ell\) and \(K_0(q)=1\). Finally the maximum automorphism-group order **within this monomial family** in dimension \(n\) is exactly
\[
 \max_{\substack{m_1,m_2,\ldots\ge0\\\sum_{\ell\ge1}\ell m_\ell=n}}\ \prod_{\ell\ge1}(\ell d_\ell)^{m_\ell}m_\ell!,
\]
achieved by disjoint unions of *unweighted* cycles. No maximum is claimed for arbitrary perfect evolution algebras.

## Assumptions and scope
Throughout \(q\ge2\) is a prime power, \(n\ge1\), and isomorphisms are \(\mathbb F_q\)-linear (not semilinear). An evolution algebra is a commutative not-necessarily-associative algebra with a natural basis whose distinct basis elements multiply to zero. The structure matrix is **monomial** when each row and column has exactly one nonzero entry; the nonzero weights ensure invertibility and hence perfectness \(E^2=E\). Cycles of length one are allowed. No restriction is imposed on the cycle decomposition or on characteristic. The squaring map on \(H_\ell\) is a permutation because \(d_\ell\) is odd and \(2^\ell\equiv1\pmod{d_\ell}\).

## Proof
**1. Isomorphisms preserve permutation cycles.** For any perfect evolution algebra, every natural basis is obtained from another by rescaling and reordering (the standard natural-basis rigidity theorem, references [2,4]). An isomorphism transports a natural basis, so its matrix is monomial. Consequently it conjugates the support permutation and takes a cycle to a cycle of the same length. It cannot mix vertices from distinct cycles linearly.

**2. The invariant for one cycle.** Order a fixed cycle as \(0,\ldots,\ell-1\). Under a diagonal natural-basis change \(e_j'=t_j e_j\), the new nonzero weight is
\[
 c_j'=t_j^2c_j/t_{j+1},\qquad t_j\in\mathbb F_q^\times,
\]
with indices modulo \(\ell\). Choose \(t_{j+1}=t_j^2c_j\) for \(0\le j<\ell-1\). Then the first \(\ell-1\) weights become one, while the final weight becomes
\[
 t_0^{2^\ell-1}\prod_{j=0}^{\ell-1}c_j^{2^{\ell-1-j}}.
\]
Thus diagonal-equivalence classes of an oriented \(\ell\)-cycle are precisely the cosets in \(H_\ell\); completeness follows because this normalization is reversible. A one-step cyclic change of the chosen starting vertex changes \(I_\ell\) to \(I_\ell^2\) modulo \((\mathbb F_q^\times)^{2^\ell-1}\): indeed, for the rotated product \(I_\ell'\), the quotient \(I_\ell^2/I_\ell'=c_0^{2^\ell-1}\). These changes generate every support-preserving graph relabeling of a single directed cycle. This proves the necessary and sufficient orbit invariant, and hence the multiset classification for arbitrary disjoint cycles.

**3. All automorphisms.** A diagonal automorphism of a cycle must obey \(t_{j+1}=t_j^2\) along its edges, with closing condition \(t_0^{2^\ell-1}=1\). Since \(\mathbb F_q^\times\) has order \(q-1\), exactly \(d_\ell\) choices exist. The permissible permutation parts of automorphisms are cyclic rotations stabilizing the class \(I_\ell\) in \(H_\ell\); if the orbit under doubling has size \(h\), there are exactly \(\ell/h\) such rotations. Every permissible rotation has exactly \(d_\ell\) diagonal lifts, yielding order \(d_\ell\ell/h\). For multiple cycles, the kernel is the product of these cyclewise automorphism groups and cycles of identical type can be permuted freely. Choosing identifications among equal-type components gives the wreath product with the appropriate symmetric group, hence the displayed product for the order. Nonisomorphic cycle types cannot be interchanged.

**4. Counting.** The cyclic group \(H_\ell\) of order \(d_\ell\) has exactly \(\gcd(d_\ell,2^r-1)\) elements fixed by the \(r\)-th power of squaring, including for \(r=0\). Squaring has order dividing \(\ell\), so Burnside's lemma gives \(a_\ell(q)\). An isomorphism class is an independent choice of an unlabeled multiset of each of these \(a_\ell(q)\) possible length-\(\ell\) cycle types, with additive dimension; the generating product follows. These are formal power series, with finitely many contributing factors at each degree.

**5. Sharp automorphism maximum inside this family.** For fixed numbers \(m_\ell=\sum_O m_{\ell,O}\), the automorphism formula and \(h_O\ge1\) imply
\[
 \prod_O\left(\frac{\ell d_\ell}{h_O}\right)^{m_{\ell,O}}m_{\ell,O}!
 \le (\ell d_\ell)^{m_\ell}m_\ell!.
\]
The factorial inequality follows by counting partitions of a labeled \(m_\ell\)-set into the stipulated type blocks. The unit class in \(H_\ell\) has orbit size one and represents an unweighted cycle. Taking all \(m_\ell\) cycles of that type attains equality, for every integer partition of \(n\). Maximizing over those partitions proves the formula, including \(n=1\).

**Concrete field-dependent distinction.** For \(q=4\) and \(\ell=2\), \(d_2=3\). Squaring on the cyclic group of order three has orbits \(\{0\}\) and \(\{1,2\}\) in exponent notation. Hence there are exactly two nonisomorphic weighted two-cycles, with automorphism-group orders six and three. This is impossible over an algebraically closed field, where all nonzero weights can be normalized to one, and concretely separates the present finite-field classification from the classical complex result [3].

## Verification
The standalone `CHECK.py` uses cyclic exponent arithmetic in \(\mathbb F_q^\times\); a generator identifies this with \(\mathbb Z/(q-1)\mathbb Z\). It enumerates **every** nonzero weighted permutation structure matrix and every monomial basis change for dimensions and fields \((q,n)=(2,4),(3,4),(4,3),(5,3),(7,3),(8,2),(9,2)\), checks the proposed classification across complete orbits, and compares actual stabilizer sizes with the proposed automorphism formula. It separately checks the Burnside orbit formula for ten field orders and all lengths one through ten. This is exact finite checking, not the proof of the unbounded theorem. The stored output ends in `VERIFY_OK`.

## Relationship to prior work
Wei–Zou [2] establish the general symmetric-group/torus action on invertible evolution-algebra structure matrices and its general finite-field orbit-counting framework; natural-basis monomial rigidity is not new. Khudoyberdiyev–Omirov–Qaralleh [3] establish normalization of nonzero permutation-cycle weights and decomposition into cycles in the complex setting, where roots are available. The 2026 survey [1] discusses permutation-attached algebras and automorphism bounds. The contribution here is the **explicit finite-field obstruction and doubling-orbit normal form**, with the resulting all-dimension product enumeration, each full automorphism-group order, and a sharp maximum **restricted to the monomial family**. The distinct irreducible arithmetic orbit classes in the \(q=4\) example prevent importing complex normalization unchanged. Work [5] studies permutation-attached algebras but its full text was not available during comparison; possible overlap is a priority risk. A general orbit theorem can subsume the qualitative classification implicitly without supplying this explicit arithmetic evaluation.

## Limitations
No conclusion is asserted for perfect evolution algebras with more than one nonzero structure constant per row, or for semilinear isomorphisms. The maximum formula is not the conjectural maximum for all perfect algebras. This does not claim a new general action theorem; its content is an explicit closed arithmetic solution for this natural subclass. The finite checker cannot alone establish the formulas in every dimension. Historical-priority comparisons remain qualified, especially where relevant older full texts were inaccessible.

## References
[1] I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, publicly submitted 2026-10-15. https://arxiv.org/abs/2610.22248
[2] Y. Wei and Y. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368. https://arxiv.org/abs/2310.12368
[3] A. Khudoyberdiyev, B. Omirov, I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993. https://arxiv.org/abs/1307.0993
[4] C. Costoya, P. Mayorga, A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterr. J. Math. 22, 149 (2025), doi:10.1007/s00009-025-02924-0.
[5] A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793. https://arxiv.org/abs/2005.05793
