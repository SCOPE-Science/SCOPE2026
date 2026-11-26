# Exact reduction of two-survivor multiset deletion codes to pair packings

## Finding

For all integers \(q\ge2\) and \(n\ge2\), let \(S_q(n,n-2)\) be the maximum number of cardinality-\(n\) multisets over a \(q\)-symbol alphabet that can be uniquely decoded after exactly \(n-2\) arbitrary deletions. Let \(P(q,n,2)\) denote the maximum number of distinct \(n\)-element subsets of a \(q\)-element ground set such that two blocks share at most one element. By convention, \(P(q,n,2)=0\) when \(n>q\). Then

\[
\boxed{S_q(n,n-2)=q+P(q,n,2).}
\]

More precisely, every two-survivor deletion-correcting multiset code admits an injection, preserving the number of its codewords, into one containing all \(q\) constant multisets together with an \(n\)-uniform pair packing. Consequently, some optimal code is always exactly of this form. This does *not* assert that every original optimum has this form.

For \(n=3\), the standard maximum partial Steiner triple-system numbers give a fully explicit formula, with \(q\ge3\):

\[
S_q(3,1)=q+\begin{cases}
q(q-1)/6,&q\equiv1,3\pmod6,\\
q(q-2)/6,&q\equiv0,2\pmod6,\\
(q(q-2)-2)/6,&q\equiv4\pmod6,\\
(q(q-1)-8)/6,&q\equiv5\pmod6.
\end{cases}
\]

For \(q=2\), \(S_2(3,1)=2\). In addition, \(S_q(n,n-2)=q\) whenever \(n>q\), and \(S_q(q,q-2)=q+1\) for all \(q\ge2\).

## Assumptions and scope

An \(n\)-multiset \(x\) is a vector \((x_a)_{a\in\Sigma}\) of nonnegative integers satisfying \(\sum_a x_a=n\), with \(|\Sigma|=q\). Its multiset intersection with \(y\) has size \(\sum_a\min(x_a,y_a)\). Exactly \(n-2\) deletions produce any two-element submultiset of \(x\), so unique decoding is equivalent to

\[
\sum_{a\in\Sigma}\min(x_a,y_a)\le1
\qquad\text{for all distinct codewords }x,y.
\]

An \(n\)-uniform pair packing is a family of \(n\)-element subsets in which each unordered symbol pair appears in at most one block. The number \(P(q,n,2)\) is a classical extremal-design quantity; the theorem reduces a coding optimum to this possibly nontrivial packing optimum, rather than giving a closed numerical expression for \(P(q,n,2)\) at every \(q,n\).

## Proof

**1. Heavy-symbol injection.** Call a codeword *heavy* if some symbol has multiplicity at least two. For each heavy codeword \(x\), choose one such symbol \(a(x)\). If distinct heavy codewords \(x,y\) had \(a(x)=a(y)\), they would share at least two copies of this symbol, contradicting the decoding condition. Therefore \(x\mapsto a(x)\) is injective. In particular, there are at most \(q\) heavy codewords.

**2. Canonical replacement.** Replace each heavy codeword \(x\) by the constant \(n\)-multiset \(a(x)^n\). The new constants are distinct. Any two distinct constants have empty intersection. Every unreplaced codeword is *light*, meaning every symbol has multiplicity at most one; hence its intersection with each constant has size at most one. Pairwise intersections between unreplaced codewords are unchanged. Thus the replacement is an injective, cardinality-preserving transformation to a valid code, with only constant and all-distinct codewords. Any missing constants may be added, again preserving validity, because a constant has intersection at most one with every light word.

**3. Packing upper bound and construction.** The light codewords in the transformed code are characteristic vectors of \(n\)-subsets. For any two, multiset intersection equals ordinary set intersection, which must be at most one. Thus at most \(P(q,n,2)\) light codewords occur. Counting at most \(q\) original heavy codewords proves

\[
|\mathcal C|\le q+P(q,n,2).
\]

Conversely, take all \(q\) constant multisets and the incidence multisets of a maximum \(n\)-uniform pair packing. Two different constants share no symbol; a constant and a packing block share at most one symbol; two packing blocks share at most one symbol. Therefore this is a valid code of size \(q+P(q,n,2)\), proving equality and the normalization assertion.

**4. Triple-system specialization.** When \(n=3\), the packing is precisely a maximum partial Steiner triple system. The known minimum leave has zero edges for \(q\equiv1,3\pmod6\), \(q/2\) edges for \(q\equiv0,2\pmod6\), \((q+2)/2\) edges for \(q\equiv4\pmod6\), and four edges for \(q\equiv5\pmod6\), for \(q\ge3\), as summarized by Demirkale–Donovan–Grannell. Each selected triple covers three symbol pairs. Subtracting the leave size from \(\binom q2\) and dividing by three gives the four cases above. For \(q=2\) no three-element subset exists, so the packing contribution is zero. For \(n>q\) likewise no light word exists; for \(n=q\), the only possible light word uses the entire alphabet, giving one packing block.

## Verification

The supplied \(\texttt{verify.py}\) independently formulates two binary integer programs: maximum independent set on the complete multiset confusability graph, and maximum pair packing with at most one block per unordered symbol pair. It solves both to zero integer-programming gap for 16 small pairs \((q,n)\), including \((7,3)\), \((6,4)\), and \((6,5)\), and checks the predicted equality in every case. The recorded exact results appear in \(\texttt{verify_output.txt}\). These finite computations corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work

Kreindel, Barouch Essayag, and Zabokritskiy (2026, arXiv:2601.05636), Section 3.4, state the same multiset-intersection criterion, establish sharp cases \(q=2,3\) with \(n\ge4\), give a \(q=4,n=3\) five-codeword example, and use a Reiman-type bound elsewhere. The section explicitly leaves the general \(n\le q\), \(q\ge4\) optimum open; its statements do not provide the heavy-symbol normalization or packing identity. Their March 2026 sequel (arXiv:2603.18322) studies Sidon constructions, deletion-ball geometry and volume bounds, not this exact extremal reduction. Kovačević–Tan (arXiv:1612.08837) studies general multiset coding and asymptotic/Sidon constructions.

The extremal \(n\)-subset packing is standard design theory, and the \(n=3\) packing numbers and leave types are known; these design counts are used, not claimed to be newly proved. The proposed contribution is the *coding-to-packing equivalence* and its exact coding consequences. In particular, a known packing theorem by itself says nothing about whether heavy multiset codewords can increase the optimum until the replacement argument is supplied.

## Limitations

The reduction is exact for arbitrary finite \(q,n\ge2\), but determination of the general classical design packing number \(P(q,n,2)\) remains a separate problem. The explicit modular table is only for block size three and uses established design-existence results. No efficient encoder, decoder, or classification of *all* optimal multiset codes is claimed. Finite integer programs do not establish the infinite theorem; the symbolic replacement argument does. Exhaustive priority verification beyond the inspected primary literature and indexed mathematical records is not claimed.

## References

1. A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, first public 2026-01-09, arXiv:2601.05636, https://arxiv.org/abs/2601.05636 (especially Section 3.4).
2. A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, first public 2026-03-18, arXiv:2603.18322, https://arxiv.org/abs/2603.18322.
3. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, first public 2016-12-28, arXiv:1612.08837, https://arxiv.org/abs/1612.08837.
4. F. Demirkale, D. Donovan, and M. Grannell, *Enumerations of maximum partial triple systems on 16 and 17 points*, first public 2017-08-25, arXiv:1708.07646, https://arxiv.org/abs/1708.07646 (Introduction and maximum-leave classifications).
