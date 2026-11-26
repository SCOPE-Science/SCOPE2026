# Recovering convex equivalence class sizes from same-class tuple-type counts

## Finding

Let \(M=(\mathbb Q^2,<_{\rm lex},E)\), where \(E\) identifies points with the same first coordinate. Let \(A\) be a finite pointwise-named parameter set and let \(m_1,\ldots,m_k\) be the sizes of the equivalence classes represented in \(A\), in their order along the quotient. For \(r\ge1\), let \(C_r(A)\) count complete types over \(A\) of ordered \(r\)-tuples of distinct elements outside \(A\) whose entries all lie in one common equivalence class meeting \(A\). The count pools all represented classes; it is not given a separate count for each class. Then
\[
C_r(A)=r!\sum_{i=1}^k\binom{m_i+r}{r}.
\]
For known \(k\), the first \(k\) such counts determine the unordered multiset \(\{m_1,\ldots,m_k\}\). Neither these pooled counts nor the entire unrefined numerical spectrum recover the order in which the class sizes occur.

The refinement can distinguish bases with the same unrefined counts in every arity. For example, bases with ordered class sizes \((1,3)\) and \((2,2)\) have identical unrefined counts but have \(C_2=26\) and \(C_2=24\), respectively. In contrast, bases with ordered sizes \((1,2)\) and \((2,1)\) have both the same unrefined spectrum and the same pooled counts \(C_r\) for every \(r\).

## Assumptions and scope

The relational language comprises the binary strict order and the binary equivalence relation, with each parameter named separately. The quotient and the order within each class are dense without endpoints. The tuple coordinates are ordered, distinct from each other and disjoint from \(A\). If \(A\) is empty, \(k=0\) and every \(C_r\) is zero; in this case there is nothing to reconstruct. The finite-arity bound stated here is sufficient; no optimality claim is made.

## Proof

In this homogeneous structure a tuple's complete type over \(A\) is specified by its induced finite order and equivalence diagram over the named points. Indeed, diagrams agreeing over \(A\) are related by an automorphism fixing \(A\), and unequal diagrams differ on an atomic formula. In a represented class containing \(m_i\) parameters there are \(m_i+1\) available order gaps. All distributions of \(r\) increasing new points into these gaps are possible by density and absence of endpoints, and the numbers in each gap determine their order diagram. Stars and bars counts these distributions by \(\binom{m_i+r}{r}\). As the tuple entries are distinct, each increasing placement gives \(r!\) assignments of coordinate labels. Since \(r\ge1\), the choices of represented class are disjoint on the space of types. Summing over classes gives the displayed formula.

Put \(p_j=\sum_i m_i^j\), with \(p_0=k\). For \(r\ge1\) the polynomial \(r!\binom{X+r}{r}=\prod_{j=1}^r(X+j)\) is monic of degree \(r\). Thus \(C_r\) is \(p_r\) plus a known linear combination of \(p_0,\ldots,p_{r-1}\). Recover \(p_1,\ldots,p_k\) successively and apply Newton's identities to find the elementary symmetric functions of the \(m_i\). These are the coefficients, with alternating signs, of \(\prod_i(X-m_i)\). Its roots with multiplicity give the unordered multiset. Because the formulas are symmetric in the \(m_i\), the pooled observations alone lose their order.

For comparison, for a nonempty base of size \(n\), the unrefined exponential generating function is \((1-z)^{1-n}/(1-2z)^{k+1}\), the one-equivalence specialization of the nested convex-equivalence spectrum [2]. Thus both pairs of example bases have identical unrefined counts within each pair. Since \(C_2=\sum_i(m_i+1)(m_i+2)\), the first pair gives \(6+20\) versus \(12+12\). The second pair has the same multiset and hence the same entire pooled sequence; the finite structures themselves are not isomorphic because their successive equivalence classes have different sizes in order.

## Verification

The supplied `verify_counts.py` and `verification_output.txt` include a finite check of the examples \((1,3)\) and \((2,2)\), giving 96 unrefined ordered pair types on either base and 26 versus 24 same-class types. The general formula and the reconstruction do not rely on finite enumeration.

## Relationship to prior work

The ordered convex-equivalence Fraïssé model is classical [1]. The unrefined all-arity formula and the ambiguity of unrefined counts belong to the broader nested-equivalence calculation [2]; they provide the comparison here, not an additional claimed result. The refinement separates a particular relation-defined family of types before counting; taking only its pooled cardinalities preserves enough information to recover the unordered sizes that unrefined totals can lose. A different reconstruction via moments is available from unrefined type counts in generic equivalence-constrained graphs [3]; those types carry graph adjacency information and are not the same-class type counts of this ordered structure.

## References

1. A. S. Kechris, V. G. Pestov and S. Todorcevic, *Fraïssé Limits, Ramsey Theory, and Topological Dynamics of Automorphism Groups*, https://arxiv.org/abs/math/0305241.
2. *Sharp finite-arity recovery of nested convex-equivalence profiles over ordered rationals*, Resultary, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-finite-arity-recovery-of-nested-convex-equivalence-profile--68f0b24d2959/RESULT.md.
3. *Moment recovery and unbounded arity separation for generic equivalence-constrained graphs*, Resultary, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-moment-recovery-and-unbounded-arity-separation-for-generic-equiv--be20a8e47188/RESULT.md.
