# Exact enumeration of binary universal partial words with the joker in third position

## Finding

Let \(N_3(n)\) be the number of **literal, indexed, linear** words over \(\{0,1,\Diamond\}\) with exactly one joker \(\Diamond\), located at position three, in which every binary length-\(n\) word is covered by exactly one length-\(n\) window (a joker can represent either binary letter). For each \(n\ge3\), such a word necessarily has length \(2^n+n-4\). Then

\[
N_3(3)=0,\qquad N_3(4)=4,\qquad N_3(5)=672,
\]

and, for all integers \(n\ge6\),

\[
\boxed{N_3(n)=2^{2^{n-1}-n}\begin{cases}
(3-12\cdot2^{-(n-1)})/14,&n\equiv0\pmod3,\\
(3+4\cdot2^{-(n-1)})/14,&n\equiv1\pmod3,\\
(3+8\cdot2^{-(n-1)})/14,&n\equiv2\pmod3.
\end{cases}}
\]

In particular, \(N_3(n)/2^{2^{n-1}-n}\to3/14\), with an explicitly determined period-three correction. Binary letters are labeled, the word is not considered up to reversal or complementation, and the joker is fixed at the third position.

## Assumptions and scope

A length-\(n\) window without a joker covers one binary word; one containing the joker covers two. These coverages are counted with multiplicity, so exactly-once coverage is required. There is no cyclic wraparound. For \(n\ge3\), the first three windows contain the joker and all later windows do not, giving \(2^n\) total covered words only if the physical word has \(2^n-3\) windows and thus length \(2^n+n-4\). The result concerns one joker at a specified position, not the number of all partial words with arbitrary joker locations.

## Proof

**1. Forced period-three prefixes.** Fix \(n\ge5\) and let the first \(n+2\) positions be
\[a b\,\Diamond\,x_1\cdots x_{n-1}.\]
Each of the first three windows represents two different edges in the binary de Bruijn digraph on the \(2^{n-1}\) length-\(n-1\) vertices. Their six edges must be distinct. For a fixed replacement \(c\in\{0,1\}\) of the joker, the three edges make a directed path from
\[u_c=a b c x_1\cdots x_{n-4}\quad\text{to}\quad s=x_1\cdots x_{n-1}.\]
The remaining ordinary windows must form an Euler trail beginning at \(s\). Deleting the two length-three paths from the balanced de Bruijn digraph leaves net outdegree-minus-indegree \(+2\) at \(s\), \(-1\) at each of \(u_0,u_1\), with cancellations if endpoints coincide. Since an Euler trail starting at \(s\) has net imbalance at most \(+1\) there, \(s=u_c\) for exactly one \(c\). Thus \(x_i\) is the prefix of the infinite periodic word \((abc)^\infty\). The triples \(000\) and \(111\) yield repeated removed edges and cannot occur. Conversely, each of the other six triples gives six distinct edges and the required residual degree pattern, with starting vertex \(s\) and ending vertex \(t=u_{1-c}\). Connectivity is accounted for exactly by the arborescence determinant below; a degree condition alone is not asserted to prove existence.

**2. Counting all completions.** Put \(r=n-1\), let \(V=2^r\), and denote the adjacency matrix of the binary de Bruijn graph by \(A\). Its directed outdegree Laplacian is \(L_0=2I-A\). The in-arborescence count at each fixed root is
\[T_r=2^{2^r-r-1}=2^{2^{n-1}-n}.\]
This is the standard de Bruijn graph matrix-tree evaluation. For each nonconstant triple, order the six removed edges \(e_i=(p_i,q_i)\) by window starting position \(1,2,3\), with replacement \(0,1\) within each. The residual outdegree Laplacian is \(L_0-\sum_i\mathbf e_{p_i}(\mathbf e_{p_i}-\mathbf e_{q_i})^\top\). Let \(t\) be the ending vertex. By the directed matrix-tree theorem and the determinant lemma, the residual rooted arborescence count is
\[\tau_t=T_r\det(I_6-Q),\]
where \(Q\) is the six-by-six matrix defined explicitly next. For \(n\ge6\), all non-isolated residual vertices have outdegree one or two and \(t\) has outdegree one, so the Euler-trail form of the BEST theorem has factorial multiplier one. Thus \(\tau_t\) is exactly the number of literal completions for this triple. The same conclusion for \(n=5\) follows with the endpoint of outdegree zero in two of the six cases.

**3. A six-dimensional exact determinant.** For binary strings \(v,w\) of length \(r\), write
\[H_r(v,w)=\sum_{\ell=1}^{r}2^{\ell-1}\mathbf1\{\operatorname{suffix}_{\ell}(v)=\operatorname{prefix}_{\ell}(w)\}.\]
With \(P=A/2\), one has \(P^r=J\), where \(J\) is the uniform stochastic matrix, and the zero-sum inverse of \(L_0\) is \(\frac12\sum_{k=0}^{r-1}(P^k-J)\). Consequently the rank-six update matrix has entries
\[
Q_{ij}=2^{-r}\bigl(H_r(p_i,p_j)-H_r(q_i,p_j)-H_r(p_i,t)+H_r(q_i,t)\bigr).
\]
This identity is valid for every \(n\ge5\) and is an alternative exact all-length enumeration without any asymptotic or guessed recurrence.

**4. Evaluation.** Put \(X=2^{-r}\). Complementation pairs the triples \(001\leftrightarrow110\), \(010\leftrightarrow101\), \(011\leftrightarrow100\). The following are the exact determinants \(\det(I_6-Q)\) for the representatives of these three pairs, respectively; each listed value appears twice.

| \(n\) modulo \(3\) | \(001\) | \(010\) | \(011\) |
|:--:|:--|:--|:--|
| \(0\) | \((1+2X)(1-4X)/28\) | \((1-4X)/28\) | \((1-2X)(1-4X)/28\) |
| \(1\) | \((1-8X^2)/28\) | \((1+6X)/28\) | \((1-2X+8X^2)/28\) |
| \(2\) | \((1-2X)(1+4X)/28\) | \((1-2X)/28\) | \((1+8X+8X^2)/28\) |

For reproducibility, here is a finite algebraic way to verify the table for **arbitrary** \(n\), rather than extrapolating a finite census. Every state \(p_i,q_i,t\) is periodic with period three outside its initial at most three symbols. For any pair of states, on overlap lengths \(4\le\ell\le r-3\), the indicator in \(H_r\) is either zero or depends only on \(\ell\bmod3\) and \(r\bmod3\); the first three and final three overlap lengths are explicit boundary cases. Summing the interior powers of two in groups of three proves that each entry of \(Q\), for fixed \(r\bmod3\), is affine in \(X\) once \(n\ge9\). Computing the entries at two representatives differing by three therefore determines the affine expression identically, not merely at two numerical lengths. Substitution in the six-by-six determinant gives the displayed table by rational polynomial arithmetic. The included `verify_symbolic.py` performs these exact operations and independently checks the resulting expressions at further representative lengths. Direct substitution separately verifies the table at \(n=6,7,8\).

Summing the three entries, each with multiplicity two, gives respectively \((3-12X)/14\), \((3+4X)/14\) and \((3+8X)/14\), and multiplication by \(T_r\) proves the theorem for \(n\ge6\).

**5. Small cases.** At \(n=3\), a joker in position \(3=n\) is impossible (also by Theorem 3.8 of Chen et al.). At \(n=4\), all four upwords have prefixes `01*010`, `01*011`, `10*100`, `10*101` and each has one completion. For \(n=5\), the six prefixes corresponding to \(001,010,011\) and complements have respectively \(160,64,112,112,64,160\) completions, totaling \(672\). Their rooted determinants can be computed directly on the original de Bruijn graph.

## Verification

Run `python verify_symbolic.py` with SymPy installed to recompute the exact rank-six determinant identities and the three congruence-class sums. Run `python verify_independent.py` for an independent full-word brute-force enumeration at \(n=4\) and full-size integer directed matrix-tree computations at \(n=5,6\). Both programs have been executed successfully. The resulting counts are \(4\), \(672\) and \(12,582,912\) at \(n=4,5,6\), respectively. The infinite claim is established by the overlap periodicity and matrix-tree proof above, not by a finite sample.

## Relationship to prior work

Chen, Kitaev, Mütze and Sun (first publicly released January 25, 2016), in Theorems 3.8 and 3.15, prove nonexistence at the final window position and construct single-joker binary upwords at positions including three. Their inspected Sections 2–3 establish the de Bruijn/Euler-path framework but do not give the complete third-position count. Related enumeration of the *first* and *second* joker positions also does not imply the third-position value, since the relevant deleted-edge configurations and mod-three overlap structure differ. Work on nonbinary universal partial words and on universal partial words for word-patterns concerns different object classes or broader existence questions, not this stated fixed-position enumeration.

## Limitations

The result does not enumerate arbitrary joker positions, multiple jokers, nonbinary alphabets, or cyclic partial words. The normalizations and the \(n=5\) exception are essential. The historical priority comparison is based on specific accessible sources, not on an exhaustive guarantee of absence from every earlier source. No independent external mathematical validation is claimed.

## References

- H. Z. Q. Chen, S. Kitaev, T. Mütze, B. Y. Sun, *On universal partial words*, arXiv:1601.06456v1, first submitted 2016-01-25, https://arxiv.org/abs/1601.06456 .
- B. Goeckner et al., *Universal Partial Words over Non-Binary Alphabets*, arXiv:1611.03928v1, 2016-11-12, https://arxiv.org/abs/1611.03928 .
- H. Z. Q. Chen and S. Kitaev, *On universal partial words for word-patterns and set partitions*, RAIRO ITA 54 (2020), https://doi.org/10.1051/ita/2020004 .
- The directed matrix-tree theorem and the Euler-trail version of the BEST theorem, standard graph-enumeration results.
