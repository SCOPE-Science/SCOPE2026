# Centralizer spectrum and a seven-ninths commutativity law for directed-star Hecke–Kiselman monoids

## Finding

For every integer \(m\ge1\), the oriented-star Hecke–Kiselman monoid \(H_m\) has \(2^m+3^m\) elements. For each element, its complete centralizer cardinality is described by the formulas below. In particular the centralizer enumerator is
\[
P_m(T)=\sum_{s=0}^m\binom ms T^{2^m+3^{m-s}}
+\sum_{u=0}^m\binom mu 2^{m-u}T^{2^u+2^{m-u}3^u}.
\]
As a consequence its center has exactly two elements, and the number of ordered commuting pairs is
\[
C_m=7^m+3\cdot4^m.
\]
The uniform commuting probability is \(C_m/(2^m+3^m)^2\sim(7/9)^m\), a sharp exponential decay law.

## Assumptions and scope

The directed star has hub \(c\) and distinct leaves \(a_1,\ldots,a_m\), with every arrow directed from leaf to hub. The monoid \(H_m\) is presented by the relations
\[
a_i^2=a_i,\quad c^2=c,\quad a_i a_j=a_j a_i,\quad a_i c a_i=c a_i c=a_i c
\]
for distinct leaves \(i,j\). Multiplication is associative. Set \(a_S=\prod_{i\in S}a_i\), with \(a_\varnothing=1\). The order of leaf factors is irrelevant. The centralizer is \(Z_{H_m}(x)=\{y\in H_m:xy=yx\}\).

## Proof

**Normal form.** For any leaf subset \(W\), we first prove \(c a_W c=a_Wc\). This holds for the empty set by \(c^2=c\). If it holds for \(W\) and \(i\notin W\), then
\[
c a_Wa_i c=c a_W c a_i c=a_W c a_i c=a_Wa_i c.
\]
The first equality replaces \(a_i c\) by \(c a_i c\), and the others use the induction hypothesis and \(c a_i c=a_i c\). Consequently all repeated occurrences of \(c\) can be reduced to a single occurrence. Leaf idempotence and commutation then give either \(a_S\), or \(a_U c a_V\). A leaf in both \(U\) and \(V\) can be deleted on the right using \(a_i c a_i=a_i c\); hence \(U\cap V=\varnothing\).

For uniqueness, project to the two-generator monoid \(K=\langle a,c\mid a^2=a,c^2=c,aca=cac=ac\rangle\) by sending each leaf other than \(a_i\) to \(1\). These projections respect all relations. The five words \(1,a,c,ac,ca\) are distinct. For example, as transformations on \(\{0,1,2\}\), with multiplication given by composition, take
\[
a=(0,0,2),\qquad c=(0,1,1),\qquad ac=(0,0,0),\qquad ca=(0,0,1).
\]
These satisfy the displayed relations and are distinct from the identity \((0,1,2)\). Every word in \(K\) reduces to one of those five, so this is an exact model. Under all leaf projections \(a_S\) has coordinate \(a\) or \(1\), whereas \(a_U c a_V\) has coordinate \(ac\), \(ca\), or \(c\), according as the leaf belongs to \(U\), to \(V\), or to neither. This distinguishes all prescribed normal forms. Thus \(|H_m|=2^m+3^m\), and the map \(H_m\hookrightarrow K^m\) given by all projections is injective.

**Centralizers.** Two leaf-only elements commute. In \(K\), among the three hub-containing elements \(c,ac,ca\), only \(ac\) commutes with \(a\), while all three commute with \(1\). Therefore \(a_S\) commutes with precisely \(3^{m-|S|}\) hub-containing elements and all \(2^m\) leaf-only elements. Hence
\[|Z_{H_m}(a_S)|=2^m+3^{m-|S|}.\]

Now fix \(a_U c a_V\), writing \(u=|U|\). In \(K\), the element \(ac\) commutes with both \(1\) and \(a\), but \(c\) and \(ca\) commute only with \(1\) among those two. Thus exactly \(2^u\) leaf-only elements commute with the given hub-containing element. Among the three hub-containing coordinate values, \(ac\) commutes with all three; each of \(c\) and \(ca\) commutes with exactly two (the unique excluded unordered pair is \(\{c,ca\}\)). Independent choices at the leaf coordinates give \(3^u2^{m-u}\) commuting hub-containing elements, whence
\[|Z_{H_m}(a_U c a_V)|=2^u+3^u2^{m-u}.\]
The number of hub-containing elements with fixed \(u\) is \(\binom mu2^{m-u}\); the number of leaf-only elements with \(|S|=s\) is \(\binom ms\). This proves the asserted polynomial \(P_m\).

**Commuting pairs, center, asymptotic.** Summing centralizer sizes over both normal-form classes gives
\[
C_m=\sum_{s=0}^m\binom ms(2^m+3^{m-s})
+\sum_{u=0}^m\binom mu2^{m-u}(2^u+3^u2^{m-u})
=2\cdot4^m+(4^m+7^m)=3\cdot4^m+7^m.
\]
The only central leaf-only element is \(1\), and the only central hub-containing element is \(a_{\{1,\ldots,m\}}c\): for positive \(m\), the individual centralizer formulas attain \(2^m+3^m\) only at these two elements. Finally, division by \(|H_m|^2\) and the inequalities \(4<7<9\) prove the probability and its sharp asymptotic equivalent.

## Verification

The accompanying standalone `checker.py` represents the five-element quotient by transformations, forms the two disjoint normal-form families inside its direct power, and independently enumerates all ordered commutation relations and every element centralizer for \(m=1,2,3,4,5\). It verifies the counts \(19,97,535,3169,19879\). The script checks closure of the proposed representation under multiplication. Its finite tests corroborate but do not replace the arbitrary-\(m\) proof.

## Relationship to prior work

Ganyushkin and Mazorchuk introduced the graph-defined Hecke–Kiselman monoids and established fundamental structural results, including the general finite Dynkin-orientation idempotent count. Collina and D’Andrea investigated their update-system realization; their principal result is for the complete acyclic orientation, not the centralizer spectrum of directed stars. Aragona and D’Andrea proved general normal-form and confluence results, which are compatible with and substantially broader than the normalization step here. The present theorem concerns the full centralizer-size distribution and its sharp commuting-probability limit in the directed-star family. A separately indexed oriented-star endomorphism census studies another invariant of the same object, and could contain supporting reductions; no direct centralizer or commuting-pair formula was identified in the accessible description.

## Limitations

The result is for a *uniformly inward-directed star*, not mixed orientations, arbitrary trees, or arbitrary graphs. The full abstract normal-form argument is supplied here; finite tests alone do not establish the theorem. The originality comparison is limited by incomplete access to the separately indexed star endomorphism record and the possibility that its structural model, or other unpublished calculations, implicitly yields the counts. No claim of independent external validation is made.

## References

1. O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, first arXiv version 2010-06-02, [arXiv:1006.0316](https://arxiv.org/abs/1006.0316), especially §§1 and 5.
2. E. Collina and A. D’Andrea, *A graph-dynamical interpretation of Kiselman’s semigroups*, first arXiv version 2013-11-14, [arXiv:1311.3460](https://arxiv.org/abs/1311.3460), §§1 and 6.
3. R. Aragona and A. D’Andrea, *Normal form in Hecke-Kiselman monoids associated with simple oriented graphs*, first arXiv version 2019-04-24, [arXiv:1904.10745](https://arxiv.org/abs/1904.10745), §§2–4.
