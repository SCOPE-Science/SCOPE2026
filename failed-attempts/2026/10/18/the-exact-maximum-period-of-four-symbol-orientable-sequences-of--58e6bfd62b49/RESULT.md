# The exact maximum period of four-symbol orientable sequences of order four

## Finding
For the four-symbol alphabet \(\Sigma=\{0,1,2,3\}\), an *orientable cyclic sequence of order four* is a cyclic word \(S\) of period \(m\) such that its length-four cyclic windows \(w_i=S_iS_{i+1}S_{i+2}S_{i+3}\), indexed modulo \(m\), obey \(w_i\ne w_j\) and \(w_i\ne w_j^R\) for every distinct pair of positions, and \(w_i\ne w_i^R\) for every position. Here \(w^R\) reverses a word. The **largest possible period is exactly \(106\)**:
\[
\max\{m:\text{a four-symbol order-four orientable cyclic word of period }m\text{ exists}\}=106.
\]
An explicit maximizing cyclic word, with the ends joined, is given verbatim in `WITNESS.txt`. The accompanying `verify.py` checks every cyclic window against every reversal pair; it also lists the \(14\) unused reversal pairs. The proof below establishes the universal upper bound, independently of the computational search by which the example was found.

## Assumptions and scope
All symbols are formal letters of \(\Sigma\). Indices of a cyclic word are reduced modulo its period. The orientability condition includes the prohibition on palindromic windows, since reading a palindromic window in either direction cannot determine orientation. Only **ordinary reversal** is considered, not negated reversal. No requirement of symbol balance or further cyclic symmetry is imposed. The result is exact for alphabet size \(4\) and window order \(4\), not a theorem for arbitrary parameters.

## Proof
Let \(F\) be the directed order-three de Bruijn graph after removing all palindromic length-four arcs. Its vertices are triples, and an arc \(a b c d\) runs from \(a b c\) to \(b c d\). Since a four-symbol palindrome has the form \(a b b a\), there are \(4^4-4^2=240\) allowed arcs, or \(120\) two-element reversal pairs \(\{w,w^R\}\).

Suppose \(S\) is an orientable cyclic word of period \(m\). Its \(m\) distinct windows traverse a directed circuit in \(F\). The \(m\) reversed windows traverse a second directed circuit (the reversed cyclic word). By orientability, these two circuits use disjoint arcs. Thus their union \(B\) is a balanced directed subgraph containing \(2m\) arcs and closed under reversal. Its complement \(M=F\setminus B\) is the union of \(r=120-m\) reversal pairs. The graph \(B\) is balanced at every vertex because it is a union of circuits.

For each \(a\in\Sigma\), consider the constant triple vertex \(aaa\). In the full graph \(F\), exactly three nonpalindromic arcs enter it: the words \(baaa\) for \(b\ne a\). In the union \(B\), however, the indegree at \(aaa\) is even: the circuit of reversed windows enters this reversal-fixed vertex as many times as the original circuit leaves it, which equals the number of times the original circuit enters it. Therefore the indegree is at most two, and at least one of the three pairs \(\{aaab,baaa\}\), \(b\ne a\), is omitted. Let \(U\) be all omitted pairs of this type and let \(u=|U|\). Pairs coming from different values of \(a\) are distinct, so \(u\ge4\).

Next let \(T=\{aab:a,b\in\Sigma,\ a\ne b\}\), a set of \(12\) vertices. Every vertex \(aab\in T\) has indegree \(3\) in \(F\): among its four incoming arcs \(caab\), only \(baab\) is palindromic. Every vertex in \(T\) has outdegree \(4\) in \(F\): no arc \(aabc\) is a palindrome since \(a\ne b\). Write \(I_T\) and \(O_T\) for the numbers of missing arcs in \(M\) whose heads and tails, respectively, belong to \(T\). Since \(B\) has equal indegree and outdegree at each vertex and \(F\) has one excess outgoing arc at every vertex of \(T\), we obtain
\[
O_T-I_T=12.
\]
Every missing pair in \(U\) contains an arc \(aaab\) entering \(aab\in T\). Hence \(I_T\ge u\), so \(O_T\ge12+u\).

Conversely, a pair in \(U\) contributes **zero** arcs leaving \(T\), because the tails of its arcs \(aaab\) and \(baaa\) are \(aaa\) and \(baa\), neither of the form \(aab\) with \(a\ne b\). An arbitrary reversal pair outside \(U\) contributes at most one arc leaving \(T\), except for pairs of the form \(\{aabb,bbaa\}\) with \(a\ne b\). To see this, if both a word \(w\) and its reversal start with a repeated but nonconstant doublet, then \(w=aabc\) with \(a\ne b\), and \(w^R=cb aa\) starts with a repeated doublet only if \(c=b\), giving \(w=aabb\). There are exactly \(\binom42=6\) such exceptional reversal pairs. Thus
\[
O_T\le(r-u)+6.
\]
Combining the inequalities yields \(12+u\le r-u+6\), hence \(r\ge6+2u\ge14\). Consequently \(m=120-r\le106\).

Finally, `WITNESS.txt` gives a length-\(106\) cyclic word. The supplied checker examines all its \(106\) length-four cyclic windows; each is nonpalindromic, and their unordered reversal classes are all different. It follows directly that the word is orientable. Distinct windows also exclude every proper period. Therefore \(m=106\) is attainable and the upper bound is sharp. \(\square\)

## Verification
Run `python3 verify.py` from the directory containing `verify.py` and `WITNESS.txt`. It uses the standard library only. It checks the witness length and alphabet; directly constructs and checks every cyclic window; independently constructs all nonpalindromic reversal classes; confirms exactly \(106\) used and \(14\) missing classes; and checks the four distinct uniform-triple omissions and six missing doublet-pair exceptions appearing in the counting argument. The recorded exact output appears in `CHECK_OUTPUT.txt`. The universal upper bound is the human mathematical argument above and does not rest on extrapolating the finite check.

## Relationship to prior work
Mitchell and Wild, *New orientable sequences* (first made public 3 July 2025), Table 6, give a best-known period of \(88\) and an upper bound of \(112\) for alphabet size \(4\), order \(4\), explicitly identifying this case as open. Their 2026 follow-up, *Constructing orientable and negative orientable sequences with asymptotically optimal period* (14 August 2026 version), Table 4, again records \(88\) and \(112\). Gabrić and Sawada's work gives asymptotically optimal cycle-joining constructions (and a specific lower-bound family for this parameter), rather than this exact maximum. The present counting argument strengthens the upper bound to \(106\) and supplies a matching witness.

## Limitations
The result does not determine maxima for other alphabets, other window orders, or the number of distinct maximal cycles. The certificate is an explicit witness plus a self-contained finite verification, not an independently checked formal proof. The novelty comparison is necessarily limited to the inspected references and searchable material; undiscovered equivalent results remain possible. Independent scientific validation has not been performed.

## References
1. C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526 (first public version 3 July 2025), https://arxiv.org/abs/2507.02526 ; Acta Informatica 63 (2026), https://doi.org/10.1007/s00236-026-00528-z . Relevant evidence: Table 6 and the concluding discussion.
2. C. J. Mitchell and P. R. Wild, *Constructing orientable and negative orientable sequences with asymptotically optimal period*, arXiv:2603.18646, https://arxiv.org/abs/2603.18646 . Relevant evidence: 14 August 2026 text, Table 4 and definitions.
3. D. Gabrić and J. Sawada, *Constructing \(k\)-ary Orientable Sequences with Asymptotically Optimal Length*, arXiv:2407.07029, https://arxiv.org/abs/2407.07029 ; author-hosted full text https://www.socs.uoguelph.ca/~sawada/papers/kary-orientable.pdf . Relevant evidence: Theorem 11 and Table 2.
