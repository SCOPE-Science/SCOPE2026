# Exact automorphism group of a free monadic bounded algebra
## Finding
Let \(F_r\) be the free monadic bounded algebra on \(r\ge 0\) generators, and put \(m=2^r\). Then
\[
\operatorname{Aut}(F_r)\cong
\prod_{k=0}^{m}\left((S_m\times S_k)\wr S_{\binom{m}{k}}\right),
\]
where \(S_0\) and \(S_1\) are trivial and the wreath products use the natural imprimitive action on the \(\binom{m}{k}\) isomorphic blocks. Consequently,
\[
|\operatorname{Aut}(F_r)|=
\prod_{k=0}^{m}
(m!\,k!)^{\binom{m}{k}}\,\binom{m}{k}!.
\]
With natural logarithms, as \(r\to\infty\),
\[
\log |\operatorname{Aut}(F_r)|
=m2^{m-1}\bigl(3\log m+\log 2-3\bigr)
+O\!\left(2^m\log m\right).
\]
Equivalently,
\[
\log |\operatorname{Aut}(F_r)|
=2^{2^r+r-1}\bigl((3r+1)\log 2-3\bigr)
+O\!\left(r2^{2^r}\right).
\]

## Assumptions and scope
A monadic bounded algebra is a Boolean algebra equipped with a distinguished element \(E\) and a unary existential operator satisfying the identities studied by Akishev and Goldblatt. The cited construction realizes \(F_r\) as the complex algebra \(\mathcal P(G_r)\) of a finite marked directed graph. Put \(m=2^r\). For every subset \(J\subseteq\{0,\ldots,m-1\}\), the graph has one block \(G_J\) with \(m\) unmarked vertices and \(|J|\) marked vertices, and every vertex of that block has exactly the marked vertices of the block as its successor set. The graph \(G_r\) is the disjoint union of all \(G_J\).

The automorphism group here is the full algebra automorphism group preserving the Boolean operations, \(E\), and the existential operator. The asymptotic statement is for \(r\to\infty\).

## Proof
Because \(F_r\cong\mathcal P(G_r)\) is a finite powerset Boolean algebra with operators, every algebra automorphism permutes its Boolean atoms, hence the singleton vertices of \(G_r\). Preservation of \(E\) preserves the marked vertices. The directed relation is recoverable from the existential operator by
\[
xRy\quad\Longleftrightarrow\quad x\in\exists\{y\}.
\]
Therefore algebra automorphisms of \(F_r\) are exactly automorphisms of the marked directed graph \(G_r\).

Fix \(J\ne\varnothing\). All vertices in \(G_J\) have the same nonempty successor set, namely the \(|J|\) marked vertices of that block. Hence an automorphism must send all of \(G_J\) onto another block \(G_{J'}\) with \(|J'|=|J|\). Conversely, for a fixed size \(k\), the \(\binom{m}{k}\) blocks with \(|J|=k\) may be permuted arbitrarily. Inside each such block, the \(m\) unmarked vertices may be permuted arbitrarily and independently of the \(k\) marked vertices, which may also be permuted arbitrarily. Thus the contribution for block size \(k\) is
\[
(S_m\times S_k)\wr S_{\binom{m}{k}}.
\]
For \(J=\varnothing\), the block consists of the \(m\) unmarked vertices with empty successor set, giving the same formula at \(k=0\). Distinct values of \(k\) cannot mix because the number of marked successors is invariant. Taking the product over \(k\) proves the group decomposition and the exact order formula.

For the asymptotic, write \(c_k=\binom{m}{k}\) and split
\[
L_m:=\log|\operatorname{Aut}(F_r)|
=2^m\log(m!)+\sum_{k=0}^{m}c_k\log(k!)+\sum_{k=0}^{m}\log(c_k!).
\]
Stirling's formula gives
\[
2^m\log(m!)=m2^m(\log m-1)+O(2^m\log m).
\]
If \(K\sim\operatorname{Bin}(m,1/2)\), then
\[
\sum_k c_k\log(k!)=2^m\,\mathbb E[\log(K!)].
\]
Uniform Stirling bounds give \(\log(k!)=k\log k-k+O(\log(m+1))\). A second-order Taylor expansion of \(x\log x\) about \(m/2\), combined with binomial concentration outside \([m/4,3m/4]\), yields
\[
\mathbb E[K\log K]=\frac m2\log\frac m2+O(1).
\]
Hence
\[
\sum_k c_k\log(k!)
=m2^{m-1}(\log m-\log2-1)+O(2^m\log m).
\]
For the final sum, Stirling gives
\[
\sum_k\log(c_k!)=\sum_k c_k\log c_k-2^m+O(m^2).
\]
Writing \(p_k=c_k/2^m\) and \(H(K)=-\sum_k p_k\log p_k\),
\[
\sum_k c_k\log c_k
=2^m\bigl(m\log2-H(K)\bigr).
\]
Since \(0\le H(K)\le\log(m+1)\), this is
\[
m2^m\log2+O(2^m\log m).
\]
Adding the three estimates gives
\[
L_m=m2^{m-1}(3\log m+\log2-3)+O(2^m\log m),
\]
and substituting \(m=2^r\) gives the stated equivalent form.

## Verification
The accompanying verifier reconstructs the block decomposition, computes the exact product formula for small ranks, and independently brute-forces every permutation preserving the marked set in the \(r=1\) graph. Exactly \(64\) permutations preserve the relation, agreeing with the product formula. It also checks the published vertex count \(3m2^{m-1}\) for the constructed graph and prints the exact automorphism orders for \(r=0,1,2\).

## Relationship to prior work
Akishev and Goldblatt construct the free \(r\)-generated monadic bounded algebra as the complex algebra of the explicitly described graph \(G_r\), and they count its atoms and elements. Their construction partitions the graph into the blocks \(G_J\) used above. The automorphism-group decomposition, exact order formula, and asymptotic derived here are not stated in that source.

## Limitations
The exact group calculation depends on the cited free-algebra graph construction; a different presentation of the same free object gives an isomorphic group but may obscure the block decomposition. The asymptotic records the first two order-\(m2^m\) terms, with an error of order \(2^m\log m\); lower-order terms are not developed here.

## References
Galym Akishev and Robert Goldblatt, *Monadic Bounded Algebras*, manuscript dated 9 June 2010; later published in *Studia Logica* 96(1), 1–40. DOI: 10.1007/s11225-010-9269-z. The free-algebra graph construction is in Section 8, especially the definition of \(G_J\), the disjoint-union construction of \(G_r\), and the conclusion that \(\mathcal P(G_r)\) is freely generated.
