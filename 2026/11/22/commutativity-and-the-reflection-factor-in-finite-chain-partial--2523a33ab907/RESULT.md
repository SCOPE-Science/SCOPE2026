# Commutativity and the reflection factor in finite-chain partial-isometry monoids

## Finding
For every integer \(n\ge2\), let \(D_n\) be the inverse monoid of all distance-preserving partial injections of the chain \([n]=\{1,\ldots,n\}\), including the empty map. Let \(E_n\) be its idempotents (partial identities). Write
\[
N_n=|D_n|=6\cdot2^n-n^2-4n-5,
\qquad
H_{n,\ell}=2^{n-\ell}10^{\lfloor\ell/2\rfloor}4^{\ell\bmod2}.
\]
The **exact** number \(T_n\) of ordered commuting pairs \((e,f)\in E_n\times D_n\) is
\[
\boxed{T_n=4^n+4\cdot3^n+H_{n,n}+2\sum_{\ell=1}^{n-1}H_{n,\ell}-(5n+3)2^n-n(n-1)2^{n-1}.}
\]
The reflection contribution is genuinely distinct from the translation contribution: a reflected two-point orbit supplies the factor \(10\), versus the translation forest's factor \(3\). Moreover there is a constant \(\rho<1\), for example
\[\rho=\max\{2^{-1/32},(3/4)^{1/20}\},\]
for which, as \(n\to\infty\),
\[
\boxed{\Pr_{f,g\in D_n}(fg=gf)=\frac{4^n}{N_n^2}+O(n^2\rho^n)=\frac1{36}+O(n^2\rho^n).}
\]
In particular, conditioned on commuting, two uniform elements both lie in \(E_n\) with probability tending to one exponentially fast. The equality of products is of partial maps, not merely equality when both maps happen to be defined.

## Assumptions and scope
Composition is ordinary partial-map composition; whether written left or right does not change the commuting relation. A partial injection preserves every distance between elements of its domain. A map of rank at least two has a **unique** global affine extension, either a translation \(p_k(i)=i+k\) or a reflection \(r_c(i)=c-i\) (with coordinates \(i=0,\ldots,n-1\)). The available domain of an extension is its set of coordinates whose images remain in the chain. Translations have \(-n+1\le k\le n-1\); reflections have \(0\le c\le2n-2\). These two extension types agree on no partial map of rank at least two. Every rank-one map admits one extension of each type. Empty maps have every extension. All statements are over ordinary finite sets and require no finite-field or characteristic assumptions.

## Proof
**1. Idempotent centralizer criterion.** Every idempotent of the symmetric inverse monoid is the identity \(e_A\) on a subset \(A\subseteq[n]\). For any partial injection \(f\), the maps \(e_A f\) and \(f e_A\) agree if and only if \(\mathbf1_A(i)=\mathbf1_A(f(i))\) for each \(i\) in the domain of \(f\). Let \(G_f\) be the undirected graph on all \(n\) chain coordinates, with an edge \(\{i,f(i)\}\) whenever \(i\ne f(i)\) and \(f(i)\) is defined. Then precisely \(2^{c(G_f)}\) idempotents commute with \(f\), where \(c\) counts connected components including isolated vertices.

**2. Summing over affine extensions.** Fix a nonzero translation \(p_k\) with \(\ell=n-|k|\) available source positions. Its possible nontrivial undirected edges lie along monotone chains of step \(|k|\) and form a forest. Every chosen subset of \(j\) arrows creates \(j\) distinct forest edges. The weighted sum over domains is therefore \(\sum_{j=0}^{\ell}\binom\ell j2^{n-j}=2^{n-\ell}3^\ell\). For the identity translation, all its restrictions are idempotents, giving the weighted sum \(4^n\). Since every length \(1\le\ell<n\) occurs for two nonzero shifts, the total weight of all translation-extension restrictions, **with multiplicity**, is \(4^n+2\sum_{\ell=1}^{n-1}2^{n-\ell}3^\ell=4^n+4\cdot3^n-6\cdot2^n\).

Now fix a reflection \(r_c\) whose admissible domain interval has \(\ell=n-|c-(n-1)|\) coordinates. It consists of \(\lfloor\ell/2\rfloor\) exchanged pairs and, if \(\ell\) is odd, one fixed point. Every coordinate outside the interval supplies two independent possibilities for \(A\). In an exchanged pair, there are four choices for the restriction domain: none (then four allowed subsets of the pair in \(A\)), either one (two allowed subsets each), or both (two allowed subsets); total weight \(4+2+2+2=10\). A fixed point allows two choices for domain membership and two for membership in \(A\), hence factor \(4\). Thus its weighted sum is exactly \(H_{n,\ell}\). Two reflections have each length \(1\le\ell<n\), while the central reflection alone has length \(n\). Therefore all reflection-extension restrictions together have weight \(H_{n,n}+2\sum_{\ell=1}^{n-1}H_{n,\ell}\).

To correct extension multiplicity, observe there are \(4n-2\) affine extension models total, so the empty map, whose idempotent centralizer has size \(2^n\), was counted \(4n-2\) times instead of once. Every rank-one map \(i\mapsto j\) was counted twice rather than once. If \(i=j\), it centralizes all \(2^n\) idempotents; if \(i\ne j\), exactly \(2^{n-1}\) idempotents. Rank-at-least-two maps were counted exactly once. Subtracting \((4n-3)2^n+n2^n+n(n-1)2^{n-1}\) from the two extension sums gives the displayed exact formula for \(T_n\). The same unweighted extension count, correcting the rank-zero and rank-one overlaps, gives \(N_n=6\cdot2^n-n^2-4n-5\). Finally \(|E_n|=2^n\), so the idempotent–idempotent ordered commuting-pair count is exactly \(4^n\).

**3. Exponential suppression of two nonidempotents.** Use the affine-extension representation to overcount, not undercount, nonidempotent pairs. Fix \(\delta=1/32\). There are at most \(4n\) affine extensions. The total number of restrictions of extensions with admissible interval shorter than \((1-\delta)n\) is at most \(4n\,2^{(1-\delta)n}\). Hence ordered pairs in which either extension is short number \(O(n^2 4^n2^{-\delta n})\).

For each pair of *long* extensions \(p,q\), suppose they are not both the identity translation. A restriction of \(p\) is specified by independent fair membership bits \(A_i\) over its admissible interval, and likewise \(B_i\) for a restriction of \(q\). For every sufficiently large \(n\), at least \(n/3\) central coordinates \(i\) have all of \(i,p(i),q(i)\) in both admissible intervals and do not satisfy \(p(i)=q(i)=i\). This follows directly from the affine formulas: a long translation has displacement less than \(\delta n\), a long reflection has axis within \(\delta n\) of the midpoint, and the middle half of the chain remains inside both admissible intervals; a nonidentity affine isometry has at most one fixed point. At each such \(i\), commutativity requires equality of the two Boolean products
\[B_i A_{q(i)}=A_i B_{p(i)}.\]
Unless \(p(i)=q(i)=i\), its probability is at most \(3/4\): if only one image equals \(i\), this probability is \(3/4\); otherwise the four membership bits are independent and it is \(5/8\). Each coordinate bit \(A_j\) or \(B_j\) occurs in at most two of these conditions as \(i\) varies because \(p,q\) are injective. A greedy conflict-graph selection extracts at least \(n/20\) conditions whose underlying bits are pairwise disjoint (for all sufficiently large \(n\)). Those conditions are independent, so a fixed long model pair commutes with probability at most \((3/4)^{n/20}\). Multiplication by the \(O(n^2)\) model pairs and their \(O(4^n)\) restrictions gives \(O(n^2 4^n(3/4)^{n/20})\) nonidempotent commuting pairs. Together with the short-model bound this is \(O(n^2 4^n\rho^n)\) for the stated \(\rho<1\).

Dividing \(4^n+O(n^24^n\rho^n)\) by \(N_n^2\), where \(N_n/2^n\to6\), proves the claimed limiting probability and the conditional idempotent dominance.

## Verification
An independently coded direct enumeration of distinct partial maps checks \(|D_n|\), \(|E_n|\), all ordered commuting pairs, and the closed expression for \(T_n\) for \(2\le n\le7\). The executable file `check_commutation.py` and observed output `check_output.txt` accompany this result. Computation corroborates but is **not** used to infer the all-\(n\) formulas, which follow from the combinatorial and probabilistic arguments above.

## Relationship to prior work
Kehinde and Umar, arXiv:1101.0049 (first posted 2010-12-30), establish the partial-isometry monoid, order-preserving submonoid, and enumerative properties; their Theorem 3.16 gives the same known total cardinality \(N_n\), which is rederived here solely as a normalization check. Al-Kharousi, Kehinde and Umar (2014) count height, fixed-point, and Green-class strata of the same monoids. Those results do not give idempotent centralizers, reflected orbit weights, or a commuting-pair limit.

An earlier calculation for the **order-preserving submonoid** obtained a commuting-pair limit \(1/9\) and an exact translation–idempotent mixed-pair count; that theorem does not imply the present result for the full monoid. The additional order-reversing elements have fixed-point and two-cycle structures not present in translations. In particular, the factor \(10\) and the exact reflection correction arise from a separate orbit analysis. This work does not claim the older cardinality formula or the order-preserving limit as new.

## Limitations
No closed expression for commuting ordered pairs of two nonidempotents is established. The constant \(\rho\) is an explicit nonoptimal exponential bound, not a sharp rate. The claim is for the full finite-chain partial-isometry monoid only, not arbitrary partial permutations or path-graph partial automorphisms. A historical priority search cannot prove absolute novelty, and variants under different names may exist.

## References
- R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049v1, posted 2010-12-30, https://arxiv.org/abs/1101.0049.
- F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain*, Australasian Journal of Combinatorics 58(3) (2014), 365–375, https://www.academia.edu/126247501/Combinatorial_results_for_certain_semigroups_of_partial_isometries_of_a_finite_chain.
