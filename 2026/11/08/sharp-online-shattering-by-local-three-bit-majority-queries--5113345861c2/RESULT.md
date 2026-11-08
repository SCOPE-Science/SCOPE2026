# Sharp online shattering by local three-bit majority queries

## Finding
For every integer \(n\ge1\), let the instance domain be the unordered triples \(\binom{[n]}3\). A binary assignment \(x\in\{0,1\}^n\) produces the classifier
\[
h_x(\{i,j,k\})=\mathbf 1\{x_i+x_j+x_k\ge2\}.
\]
Write \(\mathcal M_n=\{h_x:x\in\{0,1\}^n\}\), identifying equal classifiers. The exact Littlestone dimension is
\[
\boxed{\operatorname{Ldim}(\mathcal M_n)=\begin{cases}0,&n\le2,\\1,&n=3,\\n-1,&n\ge4.\end{cases}}
\]
For every \(n\ge4\), a full binary mistake tree of depth \(n-1\) can be constructed so that every terminal branch has a realizing assignment containing both a zero and a one. This strengthened realization property supports the unbounded induction.

## Assumptions and scope
An instance is exactly a three-element subset; repeated indices and ordered triples are excluded. Concepts are their response functions, not the index assignments themselves. The Littlestone dimension is the largest integer \(d\) for which queries may label the internal nodes of a complete binary tree of depth \(d\), so that for every length-\(d\) answer word a *single* classifier realizes all labels on its root-to-leaf path. There is no restriction that queries at different nodes be distinct; in the construction all queries along a path are distinct. The ground-set size \(n\) is arbitrary but finite.

## Proof
**Small sizes.** For \(n\le2\) the domain is empty, so the dimension is zero. For \(n=3\) there is one query and it admits both outcomes, so the dimension is one.

**Universal upper bound.** There are \(2^n\) assignments. For \(n\ge3\) the all-zero assignment and each of the \(n\) assignments with exactly one coordinate equal to one have the same identically-zero triple-majority response function. Hence the number of *distinct* concepts is at most \(2^n-n<2^n\). A shattered tree of depth \(n\) must have at least \(2^n\) distinct realizing functions, since one function cannot realize two different answer words at their first divergent node. Therefore \(\operatorname{Ldim}(\mathcal M_n)\le n-1\) for \(n\ge3\).

**Four-bit base with mixed witnesses.** On coordinates \(1,2,3,4\), query the three triples \(123\), \(124\), \(134\) consecutively (the queries at each depth can be the same on all branches). Every word of three answers is realized by a nonconstant assignment. An explicit table, with the left word listing query answers and the right word listing the four coordinates of a realizing assignment, is:

```
answers   witness
000       1000
001       0011
010       0101
011       1001
100       0110
101       1010
110       1100
111       1110
```

Each row is checked by summing the three selected coordinates. In particular, every row has both a zero and a one. This gives a mixed-witness depth-three tree at \(n=4\).

**Inductive depth increment.** Assume that on \(n\ge4\) coordinates a depth-\(n-1\) tree exists and each length-\(n-1\) answer word has a realizing mixed assignment \(x\in\{0,1\}^n\). Embed the tree unchanged among the first \(n\) coordinates of \([n+1]\). At the old leaf for each answer word, choose indices \(i,j\le n\) such that \(x_i=0\) and \(x_j=1\). Label that leaf by the *new* triple query \(\{i,j,n+1\}\) and attach two children. Extend \(x\) by \(x_{n+1}=b\), where \(b\in\{0,1\}\) denotes the newly requested answer. Every previous answer remains unchanged; the new answer is precisely \(b\), because \(0+1+b\ge2\) if and only if \(b=1\). Both extended assignments are still mixed. Thus the new complete depth-\(n\) tree is shattered and still has mixed witnesses at all leaves. Induction proves \(\operatorname{Ldim}(\mathcal M_n)\ge n-1\) for every \(n\ge4\). The matching upper bound completes the proof.

## Verification
The standalone Python script `verify_majority.py` constructs and checks every path and every mixed terminal witness of the recursive trees through \(n=11\), including a \(1024\)-leaf depth-ten tree. Separately it computes the exact Littlestone ranks from the concept truth tables and a bitset minimax recurrence for all \(1\le n\le8\). The execution results are stored in `verification_output.txt`. The general statement follows from the induction and concept-count argument, not finite extrapolation.

## Relationship to prior work
Ghazi, Golowich, Kumar and Manurangsi (2020) establish *general* upper bounds for the Littlestone dimension under Boolean aggregation of classifiers. Their aggregation model has multiple hypothesis classes acting on the same input; it does not specify this self-indexed family of all assignments queried by coordinate triples or give the exact dimension sequence above. Guingona, Kolesnikov, Nierwinski and Soucy (2021) determine Littlestone dimensions of zero-set families of linear combinations; their linear-zero-set hypotheses differ from this nonlinear local-majority incidence relation. This result isolates the exact adaptive capacity of majority-of-three observations on a latent binary vector.

## Limitations
The result is solely about worst-case *realizable* binary online shattering, not noisy query learning, computationally efficient recovery of the unknown vector, identification complexity, or a complete VC-shattering polynomial. Different assignments can induce the same concept. The historical novelty comparison covered accessible records and the relevant cited sources, but unindexed equivalent treatments under alternative language remain possible. Independent mathematical review has not been carried out.

## References
1. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1 (first public 2020-07-07), especially Introduction and Proposition 2.3; https://arxiv.org/abs/2007.03668.
2. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (first public 2021-09-10), Introduction and Theorem 3.10; https://arxiv.org/abs/2109.04805.
