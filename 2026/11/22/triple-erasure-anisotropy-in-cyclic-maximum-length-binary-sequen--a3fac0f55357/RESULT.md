# Triple-erasure anisotropy in cyclic maximum-length binary sequences

## Finding

Let \(m\ge3\), \(F=\mathbb F_{2^m}\), \(\alpha\) a primitive field element, and \(L=2^m-1\). For every \(u\in F^*\) write
\[
 c_u(i)=\operatorname{Tr}_{F/\mathbb F_2}(u\alpha^i)\qquad (0\le i<L).
\]
These are precisely the \(L\) cyclic phases of a binary maximum-length linear recurrence. For a deletion set \(D\subseteq F^*\), define the Boolean coordinate concept class \(\mathcal C_D=\{c_u:u\in F^*\setminus D\}\). A coordinate set is *shattered* when all its binary labelings occur as restrictions of concepts.

Write
\[
 a_{d,k}=\frac{1}{k!}\prod_{j=0}^{k-1}(2^d-2^j),\qquad a_{d,0}=1,
\]
for \(0\le k\le d\), and define the two-sum set
\[
 \Delta D=\{a+b:a,b\in D,\ a\ne b\}.
\]
The complete undeleted shattering polynomial and the top coefficient for **arbitrary** erasures are
\[
 \Phi_{\varnothing}(z)=\sum_{k=0}^{m-1}a_{m,k}z^k,\qquad
 [z^{m-1}]\Phi_D(z)=a_{m-1,m-1}\bigl(2^m-1-|D\cup\Delta D|\bigr).
\]
For exactly one, two or three deleted states, the **entire** shattering polynomial is determined by the following four cases (the cases for three deleted states require distinct elements):
\[
\begin{aligned}
 |D|=1:\quad&\Phi_D(z)=\Phi_{\varnothing}(z)-a_{m-1,m-1}z^{m-1};\\
 |D|=2:\quad&\Phi_D(z)=\Phi_{\varnothing}(z)-3a_{m-1,m-1}z^{m-1};\\
 |D|=3,\ \sum_{u\in D}u\ne0:\quad&\Phi_D(z)=\Phi_{\varnothing}(z)-6a_{m-1,m-1}z^{m-1};\\
 |D|=3,\ \sum_{u\in D}u=0:\quad&\Phi_D(z)=\Phi_{\varnothing}(z)-3a_{m-1,m-1}z^{m-1}-a_{m-2,m-2}z^{m-2}.
\end{aligned}
\]
Thus three erasures forming a binary projective line destroy fewer top-dimensional faces than an independent triple, but they alone destroy some next-to-top faces.

All \((m-1)\)-supports disappear precisely when \(D\cup\Delta D=F^*\). If \(e_m\) is the smallest such number of erased phases, then
\[
 \left\lceil\frac{\sqrt{1+8(2^m-1)}-1}{2}\right\rceil
 \le e_m\le 2^{\lfloor m/2\rfloor}+2^{\lceil m/2\rceil}-2.
\]
The last condition is exactly the classical binary one-saturating-set property, not a new characterization of saturating sets in isolation.

## Assumptions and scope

The trace is the absolute field trace; multiplication, independence, and addition are over \(\mathbb F_2\). Field powers \(\alpha^i\) traverse \(F^*\) once. Erasures remove entire cyclic shifts (hypotheses), **not** bit positions (queries), and the zero state is never an available hypothesis. The theorem is about coordinate-trace shattering of all cyclic phases of a *single* primitive binary linear recurrence, not the different concept family of variable-length factors of an arbitrary infinite word.

The top-coefficient identity holds for every \(D\subseteq F^*\); the complete polynomial specialization is asserted only for \(|D|\le3\). The final numerical bound is on the minimum number of erasures needed to reduce VC dimension below \(m-1\), not on a minimum-distance parameter.

## Proof

**1. Trace duality and baseline.** The bilinear trace form \((u,v)\mapsto\operatorname{Tr}(uv)\) is nondegenerate. For distinct coordinates \(S=\{i_1,\dots,i_k\}\), let \(v_j=\alpha^{i_j}\) and consider the linear restriction map
\[
 T_S:F\longrightarrow \mathbb F_2^k,\qquad
 T_S(u)=(\operatorname{Tr}(uv_1),\dots,\operatorname{Tr}(uv_k)).
\]
If the coordinate vectors are dependent, some nontrivial linear equation holds for every labeling, so \(S\) cannot be shattered. If they are independent, \(T_S\) has rank \(k\) and every fiber has \(2^{m-k}\) elements. Removing the unavailable state \(u=0\) leaves \(2^{m-k}-1\) witnesses for the zero labeling and \(2^{m-k}\) witnesses for every nonzero labeling. Consequently an independent set is shattered with no erasures exactly for \(k\le m-1\). Counting unordered independent \(k\)-sets in \(F\) gives \(a_{m,k}\). No support of size \(m\) can be shattered after erasures, since it already cannot be shattered before erasures.

**2. Arbitrary deletion set at the top rank.** Take \(k=m-1\), with independent \(S\). The kernel \(K=\ker T_S\) has size two, \(K=\{0,w\}\) for a unique \(w\in F^*\). The all-zero labeling has only the witness \(w\). Every nonzero labeling has precisely two witnesses \(u,u+w\), both nonzero. The erased family still shatters \(S\) exactly when \(w\notin D\), and there is no erased pair \(\{u,u+w\}\subset D\). In characteristic two that latter obstruction means \(w\in\Delta D\). Therefore precisely the kernels with \(w\in F^*\setminus(D\cup\Delta D)\) survive. For each fixed \(w\), the possible coordinate vectors are exactly the unordered bases of the \((m-1)\)-dimensional trace-orthogonal hyperplane \(w^\perp\), numbering \(a_{m-1,m-1}\). Different kernels give disjoint sets of supports, proving the top identity.

**3. All layers for at most three erasures.** If \(k\le m-3\), the zero labeling has at least \(2^3-1=7\) nonzero witnesses and each nonzero labeling at least eight, so three deletions cannot affect it. If \(k=m-2\), the zero-label fiber contains exactly three nonzero states: the nonzero elements of the two-dimensional kernel \(K\); all other fibers have four states. With at most two deletions no such support is lost. With three deletions, a support is lost exactly if \(D=K\setminus\{0\}\), meaning the three distinct deleted states sum to zero. Such \(D\) determines one kernel \(K\), and its orthogonal complement has \(a_{m-2,m-2}\) unordered bases. This proves the penultimate correction. In the top formula, a singleton has \(|D\cup\Delta D|=1\), a pair has size three, an independent triple has size six, and a dependent triple has size three. Substituting yields all four polynomial cases, including \(m=3\).

**4. Saturation and robust rank.** The top formula is zero exactly when \(D\cup\Delta D=F^*\), which is the usual binary projective one-saturation criterion. As \(|D\cup\Delta D|\le d+\binom d2\) for \(d=|D|\), full top-layer destruction requires the stated quadratic lower bound. For the upper bound, choose complementary \(\mathbb F_2\)-subspaces \(F=U\oplus W\), with dimensions \(\lfloor m/2\rfloor\) and \(\lceil m/2\rceil\), and delete \(D=(U\setminus\{0\})\cup(W\setminus\{0\})\). Every nonzero field element is either in \(D\) or the sum of a nonzero member of each summand, and therefore belongs to \(\Delta D\). This uses the classical saturating-set construction and completes the bounds.

For completeness, a general robustness consequence of the same fiber sizes is that whenever \(0\le k\le m-1\), deleting at most \(2^{m-k}-2\) states preserves every independent \(k\)-coordinate support. The threshold is sharp for each support: deleting the \(2^{m-k}-1\) nonzero states of its kernel kills its zero labeling.

## Verification

Two self-contained Python programs accompany this result. `check_erasure.py` realizes \(\mathbb F_{2^m}\) as a polynomial quotient and directly constructs the trace-generated cyclic word. `check_erasure_independent.py` instead generates the cyclic word from a binary recurrence, with phase states defined by consecutive register bits. They independently enumerate restrictions to coordinate sets and compare the top and penultimate coefficient formulas. The first checks representative erasure patterns through \(m=5\); the second checks **all 35 three-phase deletions at \(m=3\)**, **all 455 at \(m=4\)**, and six additional three-phase deletions at \(m=5\). Both programs completed without errors in a clean replay.

As spot checks, \(m=4\) has baseline \(1+15z+105z^2+420z^3\), while a dependent three-erasure set gives \(1+15z+102z^2+336z^3\) and an independent triple gives \(1+15z+105z^2+252z^3\). For \(m=5\), the corresponding top coefficients are \(26040\), \(23520\), and \(21000\). The universal statements follow from the trace-fiber proof; the finite programs are corroborating checks, not substitutes for an infinite proof.

Reproduce with `python3 check_erasure.py` and `python3 check_erasure_independent.py` from a directory containing the two files. Neither requires third-party packages.

## Relationship to prior work

Johnson's *Binary strings of finite VC dimension* (2021) studies the VC dimension of infinite strings and their factor incidence structures; its concept family is not the phase-erasure system considered here. Castoldi, Moura, Panario and Stevens (2022), *Ordered Orthogonal Array Construction Using LFSR Sequences*, specifically establish a full-array linear-independence equivalence for LFSR columns (Theorem 14), and discuss the associated independent-vector construction in Section VII-A. Thus the linear-algebra baseline is established prior art rather than claimed novel.

Grynkiewicz and Lev (2008), *1-Saturating Sets, Caps and Round Sets in Binary Spaces*, study the projective criterion that all nonzero points lie in a set or on a secant through two of its points. That classical criterion and the existence of complementary-subspace saturating constructions are not asserted novel. Fontana and Rapallo (2018) analyze deleting one, two or three runs from orthogonal arrays, but their full-text Sections 3–5 establish generalized word-length/aberration formulas and selected tables, rather than a VC shattering-face classification for cyclic LFSR arrays. The assessed contribution is the exact arbitrary-row-erasure effect on the top shattering layer, the complete three-erasure dichotomy across two adjacent dimensions, and their interpretation in the cyclic LFSR concept family. The inspected sources do not state those coefficients or their three-erasure comparison, but an unindexed equivalent combinatorial treatment is possible.

## Limitations

No exact minimum size of binary one-saturating sets is derived beyond the stated bounds; that is an independent finite-geometry problem with existing literature. No full coefficient formula is claimed for general \(|D|\ge4\) below the top layer. Priority beyond the inspected primary papers and accessible research index is not claimed, and this proof has not undergone independent external validation.

## References

1. Hunter R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first posted 2021-01-16. https://arxiv.org/abs/2101.06490
2. André Guerino Castoldi, Lucia Moura, Daniel Panario and Brett Stevens, *Ordered Orthogonal Array Construction Using LFSR Sequences*, arXiv:2208.00333, first posted 2022-07-31. https://arxiv.org/abs/2208.00333
3. David J. Grynkiewicz and Vsevolod F. Lev, *1-Saturating Sets, Caps and Round Sets in Binary Spaces*, arXiv:0811.1322, first posted 2008-11-09. https://arxiv.org/abs/0811.1322
4. Roberto Fontana and Fabio Rapallo, *On the aberrations of mixed level Orthogonal Arrays with removed runs*, arXiv:1809.03759, first posted 2018-09-11. https://arxiv.org/abs/1809.03759
