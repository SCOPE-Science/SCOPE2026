# Cycle profiles of the universal symmetric-group action quandle

## Finding

For every integer \(n\geq1\), let \(Q_n=[n]\times S_n\) carry Kai's action-quandle operation
\[
(x,g)*(y,h)=(x^{g^{-1}h},h^{-1}gh),
\]
where permutations act on the right. For \(h\in S_n\) let \(R_h\) be right translation by any \((y,h)\); it does not depend on \(y\). For each positive integer \(k\), put \(q=h^k\), let \(m_d(q)\) be the number of length-\(d\) cycles of \(q\), and define
\[
 z(q)=\prod_{d=1}^n d^{m_d(q)}m_d(q)!,\qquad
 B_k(q)=\sum_{d=1}^n\#\{\ell:1\leq\ell\leq m_d(q),\ \ell\mid k,\ \gcd(d,k/\ell)=1\}.
\]
Then the exact fixed-point count is
\[
 \boxed{F_h(k):=|\operatorname{Fix}(R_h^k)|=z(h^k)B_k(h^k).}
\]
This formula determines the complete right-translation cycle profile: the number of cycles of length \(m\) in \(R_h\) is
\[
 \boxed{c_m(h)=\frac1m\sum_{d\mid m}\mu(m/d)F_h(d),}
\]
where \(\mu\) is the number-theoretic Möbius function. In particular, for \(n\ge3\), every \(R_h\) has exact order \(\operatorname{lcm}(1,\ldots,n)\). For every \(n\ge1\), if \(\omega(\lambda)\) counts the distinct part sizes in a partition \(\lambda\), then
\[
 \boxed{F_h(1)=z(h)\,\omega(\lambda(h)).}
\]
Consequently, if \(A,B\) are independent uniform elements of \(Q_n\), and \(p(j)\) is the number of integer partitions of \(j\),
\[
 \boxed{\Pr(A*B=A)=\frac{\sum_{j=0}^{n-1}p(j)}{n\,n!}.}
\]

## Assumptions and scope

The group \(S_n\) is the symmetric group on \([n]=\{1,\ldots,n\}\) and acts on the right: \(x^{ab}=(x^a)^b\). All exponents \(k,m,d,\ell\) in the counting formulas are positive integers. The empty multiplicity factors in \(z(q)\) are \(1\), and the empty sums in \(B_k(q)\) are \(0\). The quandle has exactly \(n\,n!\) elements. Its right translations are indexed by the group coordinate \(h\), because the first coordinate \(y\) of the right operand never appears in the operation. The formula includes \(n=1\) and \(n=2\); the stated universal exact-order consequence is proved directly for \(n\ge3\).

The exponent \(\operatorname{lcm}(1,\ldots,n)\) is denoted \(L_n\). Since \(R_h^{L_n}\) is the identity, cycle lengths divide \(L_n\); hence the profile is obtained by evaluating \(F_h(d)\) for divisors \(d\) of \(L_n\) and applying the displayed inversion formula.

## Proof

**1. Iterated right translation.** The action formula gives, by direct induction,
\[
 R_h^k(x,g)=\bigl(x^{g^{-k}h^k},h^{-k}gh^k\bigr).
\]
Thus the pair \((x,g)\) is fixed by \(R_h^k\) precisely when \(g\) centralizes \(q=h^k\) and \(g^k(x)=q(x)\). In particular,
\[
 F_h(k)=\sum_{g\in C_{S_n}(q)}\#\{x\in[n]:g^k(x)=q(x)\}.
\]
The equality of the two conditions follows by applying \(g^k\) to \(x^{g^{-k}q}=x\) after observing \(gq=qg\).

**2. Centralizer block structure.** A permutation \(q\) with \(m_d\) cycles of length \(d\) has centralizer
\[
 C_{S_n}(q)\cong\prod_{d=1}^n\bigl(C_d\wr S_{m_d}\bigr)
\]
of order \(z(q)=\prod_d d^{m_d}m_d!\). In the factor corresponding to length \(d\), an element of the centralizer permutes the \(m_d\) cyclic blocks and rotates each block by an arbitrary element of \(\mathbb Z/d\mathbb Z\). Uniformly sampling a centralizer element makes the block permutation uniform in \(S_{m_d}\), with independent uniform rotations.

Fix a point \(x\) in a specified length-\(d\) block. Let \(\ell\) be the length of the orbit of this block under the sampled block permutation. For each \(1\le\ell\le m_d\), there are exactly \((m_d-1)!\) permutations for which the block containing \(x\) has orbit length \(\ell\). Hence \(\ell\) is uniform on \(\{1,\ldots,m_d\}\). If \(\ell\nmid k\), then \(g^k\) moves \(x\) to a different block, so \(g^k(x)\ne q(x)\).

If \(\ell\mid k\), let \(S\in\mathbb Z/d\mathbb Z\) be the total shift accumulated in one traversal of the \(\ell\)-cycle of blocks. At least one of the independent block rotations occurs with coefficient one in \(S\), so \(S\) is uniform modulo \(d\). The element \(g^k\) rotates the original block through \((k/\ell)S\), whereas \(q\) rotates it through one step. Thus \(g^k(x)=q(x)\) iff
\[
 (k/\ell)S\equiv1\pmod d.
\]
This equation has no solution if \(\gcd(d,k/\ell)>1\), and a unique solution if \(\gcd(d,k/\ell)=1\). In the latter case its probability is \(1/d\). Therefore, for each of the \(d m_d\) points belonging to length-\(d\) blocks,
\[
 \Pr_{g\in C_{S_n}(q)}(g^k(x)=q(x))=
 \frac{1}{d m_d}\#\{\ell\le m_d:\ell\mid k,\gcd(d,k/\ell)=1\}.
\]
Multiplying by \(d m_d\) and then by the centralizer order \(z(q)\), and summing over all \(d\), proves the fixed-point formula.

**3. Complete profiles.** For any finite permutation \(R\), the number of its fixed points under its \(k\)-th power equals \(\sum_{m\mid k}m c_m\), where \(c_m\) is its number of cycles of length \(m\). Ordinary Möbius inversion gives the formula for \(c_m(h)\). To bound the order, note that \(h^{L_n}=g^{L_n}=1\) for all \(h,g\in S_n\), so Step 1 gives \(R_h^{L_n}=1\).

For \(n\ge3\), the center of \(S_n\) is trivial. If \(R_h^k=1\), its second coordinate in Step 1 implies \(h^k\) is central and hence \(h^k=1\). The first coordinate then forces \(g^k\) to fix every letter for every \(g\in S_n\); thus \(g^k=1\) for every \(g\), which implies \(L_n\mid k\). This proves exact order \(L_n\).

**4. Fixed pairs and partition sum.** Put \(k=1\). The only permissible block orbit length is \(\ell=1\), and \(\gcd(d,1)=1\), giving \(B_1(h)=\omega(\lambda(h))\) and \(F_h(1)=z(h)\omega(\lambda(h))\).

For each partition \(\lambda\vdash n\), there are \(n!/z(\lambda)\) permutations having that cycle type. Therefore
\[
 \sum_{h\in S_n}F_h(1)=n!\sum_{\lambda\vdash n}\omega(\lambda).
\]
For every fixed \(h\), the right operand has \(n\) possible choices of its first coordinate, which all give the same right translation. Thus the number of ordered pairs \((A,B)\in Q_n^2\) with \(A*B=A\) is \(n\,n!\sum_{\lambda\vdash n}\omega(\lambda)\).

Double-counting the pairs \((\lambda,d)\) such that \(d\) is a part size present in the partition \(\lambda\), we obtain
\[
 \sum_{\lambda\vdash n}\omega(\lambda)=\sum_{d=1}^n p(n-d)=\sum_{j=0}^{n-1}p(j),
\]
because deleting one occurrence of \(d\) bijects partitions of \(n\) containing \(d\) with partitions of \(n-d\). Divide by \(|Q_n|^2=(n\,n!)^2\) to obtain the probability formula.

## Verification

A standalone Python program, `verify.py`, constructs permutation groups using explicit right-action composition, constructs quandle right translations from the defining operation, iterates them directly, and independently computes the centralizer-cycle formula. It checks every permutation cycle type at degrees \(1\) through \(5\) for powers \(1\) through \(12\), plus two selected types in degree \(6\), giving \(230\) exact fixed-point comparisons. It also independently constructs complete permutation-cycle profiles for all \(11\) cycle-type representatives through degree \(4\), checks the partition-sum count through degree \(5\), and verifies the concrete example below. Run `python3 verify.py`; the recorded output is in `verify_output.txt`.

For example, when \(n=4\) and \(h\) is a four-cycle, the right translation acts on \(96\) points and has exactly
\[
 \boxed{1^4\,2^2\,4^{16}\,12^2}
\]
as its cycle type (notation: four fixed points, two two-cycles, sixteen four-cycles, two twelve-cycles). The weighted sum of cycle lengths is \(4+4+64+24=96\). This example illustrates that a right translation may have cycles whose lengths exceed the order of the indexing permutation \(h\) (which has order four here).

The computations test finite instances only; the displayed proof establishes the formulas for every permitted degree and power.

## Relationship to prior work

Ryoya Kai, *Quandles from group actions and a Cayley-type embedding theorem*, arXiv:2609.17438 (first submission September 15, 2026), introduces the same quandle and proves its embedding property, the structure of the inner automorphism group, and its connected components. Its Lemma 3.6 and Proposition 4.3 provide useful iteration and order context, but do not state a formula for the full right-translation cycle profile or the fixed-pair partition sum. The new calculation of fixed points uses centralizer wreath products and the arithmetic condition \(\gcd(d,k/\ell)=1\), going beyond a restatement of the source's orbit decomposition.

Sam Nelson, *Generalized quandle polynomials*, arXiv:0801.2979, defines invariants based on fixed points of powers of right translations, but does not compute these for the later universal action-quandle family. Lages, Lopes and Vojtěchovský, *A Sufficient Condition for a Quandle to be Latin*, arXiv:2104.10199, study cycle profiles and their implications for latinness, not the present complete family. Earlier homogeneous quandles arising from automorphisms of symmetric groups (Higashitani and Kurihara, arXiv:2005.12057) constitute a different quandle construction; their results do not imply the formula above.

## Limitations

The claim concerns the canonical action quandle associated to the natural symmetric-group action. It does not supply the complete two-variable generalized quandle-polynomial matrix (which requires elementwise rather than merely right-translation fixed-point statistics), nor an automorphism-group classification. It makes no assertion that right-translation profiles distinguish all isomorphism types of quandles. The order assertion is stated only for \(n\ge3\); the main formulas remain valid in degrees \(1\) and \(2\).

The counting step uses the standard wreath-product description of a symmetric-group centralizer, which is classical. The novelty claim is the complete specialization to this particular universal action quandle, not the centralizer formula itself. An equivalent unpublished or differently indexed calculation remains a historical-priority risk. No independent audit has been performed.

## References

1. R. Kai, *Quandles from group actions and a Cayley-type embedding theorem*, arXiv:2609.17438, https://arxiv.org/abs/2609.17438 (first public submission September 15, 2026).
2. S. Nelson, *Generalized quandle polynomials*, arXiv:0801.2979, https://arxiv.org/abs/0801.2979.
3. A. Lages, P. Lopes, P. Vojtěchovský, *A Sufficient Condition for a Quandle to be Latin*, arXiv:2104.10199, https://arxiv.org/abs/2104.10199.
4. A. Higashitani and H. Kurihara, *Homogeneous quandles arising from automorphisms of symmetric groups*, arXiv:2005.12057, https://arxiv.org/abs/2005.12057.
