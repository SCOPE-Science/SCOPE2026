# Rigidity of idempotent-fixing inverse matchings in the top singular rank of an isotone monoid

## Finding

Let \(n\ge4\), and let \(\mathcal O_n\) be the monoid of order-preserving self-maps of the chain \([n]=\{1,\ldots,n\}\). Write \(D\) for its Green class of transformations of rank \(n-1\). A *mutual semigroup inverse* of \(f\) is a map \(g\) with \(fgf=f\) and \(gfg=g\). An *idempotent-fixing involution matching* of \(D\) is a permutation \(\tau:D\to D\) satisfying \(\tau^2=\mathrm{id}\), \(\tau(f)\) is a mutual inverse of \(f\), and \(\tau(e)=e\) for every idempotent \(e\in D\).

**Theorem.** There exists **exactly one** idempotent-fixing involution matching of \(D\). To describe it, write \(f_{j,k}\) for the unique rank-\(n-1\) isotone map whose kernel merges the adjacent positions \(j,j+1\) and whose image is \([n]\setminus\{k\}\), where \(1\le j<n\) and \(1\le k\le n\). Its unique matching is

\[
\tau(f_{j,k})=\begin{cases}
f_{j,k},&k\in\{j,j+1\},\\
f_{k-1,j},&k\ge j+2,\\
f_{k,j+1},&k\le j-1.
\end{cases}
\]

It fixes precisely the \(2(n-1)\) idempotents, has exactly \(\binom{n-1}{2}\) two-cycles, and commutes with reflection of the underlying chain. Equivalently, the mutual-inverse bipartite graph between the two kinds of nonidempotents in \(D\) has **exactly one perfect matching**, even though its vertices can have several inverse partners.

## Assumptions and scope

All maps are total and weakly increasing. Composition is ordinary function composition; the mutual-inverse equations are independent of the side convention. The rank \(n-1\) class is the highest nonunit Green class, of cardinality \(n(n-1)\). The fixed-idempotent requirement is part of the theorem: other involution matchings may move idempotents, and the theorem does not assert uniqueness among those. No conclusion is claimed for other ranks or for a globally defined matching of \(\mathcal O_n\). The range \(n\ge4\) separates this result from the previously treated rank-two case.

## Proof

**1. Encoding and idempotents.** An isotone transformation with rank \(n-1\) has exactly one kernel block of size two, necessarily the adjacent pair \(\{j,j+1\}\); its remaining kernel blocks are singletons. Its image omits exactly one element \(k\). The two parameters uniquely determine the transformation because each consecutive kernel block maps to the corresponding increasing image element. Thus the \(f_{j,k}\) exhaust \(D\). Such a transformation is idempotent exactly when its image contains one representative from each kernel block. Since the image omits one point, this is equivalent to \(k=j\) or \(k=j+1\). There are exactly \(2(n-1)\) idempotents.

**2. Exact inverse criterion.** For isotone maps \(f_{j,k}\) and \(f_{u,v}\),

\[
 f_{u,v}\in V(f_{j,k})\quad\Longleftrightarrow\quad
 v\in\{j,j+1\}\ \text{and}\ k\in\{u,u+1\}.
\]

Indeed, \(fgf=f\) forces the image of \(g\) to be a transversal for the kernel blocks of \(f\): \(g\) restricted to the image of \(f\) must select precisely one point from each such block. Conversely, for isotone maps of equal rank, a transversal of the ordered blocks is aligned in increasing order, so it provides the required section. Apply the same argument to \(gfg=g\). In the present coatom class, saying that \([n]\setminus\{v\}\) is a transversal for the kernel block \(\{j,j+1\}\) is exactly \(v\in\{j,j+1\}\), and symmetrically for the second condition.

**3. Existence.** Partition the nonidempotents into

\[
 R=\{(j,k):k\ge j+2\},\qquad
 L=\{(j,k):k\le j-1\}.
\]

The prescribed matching fixes every idempotent, and sends \((j,k)\in R\) to \((k-1,j)\in L\), while sending \((u,v)\in L\) to \((v,u+1)\in R\). Both transfers are well-defined and inverse to each other. The inverse criterion in step 2 shows that each transferred pair consists of mutual semigroup inverses. Thus \(\tau\) is an idempotent-fixing involution matching.

**4. Uniqueness.** Any idempotent-fixing involution matching must pair every nonidempotent with another nonidempotent: a nonidempotent cannot be fixed by a mutual-inverse matching, and all idempotents have already been fixed. By step 2, a nonidempotent in \(R\) can be inverse only to an element of \(L\), and conversely. Define the bijection

\[
 \psi:L\longrightarrow R,\qquad \psi(u,v)=(v,u+1).
\]

If \(x=(j,k)\in R\) and \(y=(u,v)\in L\) are mutual inverses, the criterion gives \(v\ge j\) and \(u+1\ge k\). Therefore \(\psi(y)\ge x\) *coordinatewise*. A perfect matching between \(R\) and \(L\) would induce a bijection \(b:R\to R\), \(b(x)=\psi(y)\), with \(b(x)\ge x\) coordinatewise. Summing the first coordinates over the finite set \(R\), and then the second coordinates, shows that every inequality must be equality: the sums over all inputs and all outputs of a bijection agree. Hence \(b(x)=x\) for every \(x\in R\), forcing \(y=(k-1,j)\). Therefore the displayed \(\tau\) is the **only** such matching.

**5. Counts and reflection.** The set \(R\) has cardinality \(\sum_{j=1}^{n-2}(n-j-1)=\binom{n-1}{2}\). Each point of \(R\) belongs to one two-cycle paired with \(L\), while the remaining \(2(n-1)\) points are fixed idempotents. Reflection \(\rho(i)=n+1-i\) sends \(f_{j,k}\) to \(f_{n-j,n+1-k}\) by conjugation. Substitution into the explicit formula shows \(\tau(\rho f\rho)=\rho\tau(f)\rho\), proving equivariance.

## Verification

The standalone `verify.py` constructs each \(f_{j,k}\) as an actual tuple-valued transformation and recomputes \(fgf=f\) and \(gfg=g\) by composition for **every ordered pair** in the rank-\(n-1\) class for \(4\le n\le10\). It independently checks the inverse criterion, the formula, the idempotent count, two-cycle count and reflection equivariance. For \(4\le n\le8\), a bit-mask dynamic program **counts all** perfect matchings of the induced nonidempotent inverse graph, obtaining one in each case. Execute `python3 verify.py` from the directory containing the script; compare with `verification_output.txt`. Finite checks do not establish the theorem for arbitrary \(n\); its proof is in the preceding section.

## Relationship to prior work

Higgins's 2026 work establishes that **every** rank class of \(\mathcal O_n\) has a *permutation* inverse matching using balanced weightings of a transversal-incidence relation. It does not establish involutivity, idempotent-fixing, or uniqueness for the top singular class. The present theorem makes those three stronger assertions for that canonical class, with a direct formula and rigidity argument. The 2024 survey of Higgins poses involutive matching questions and distinguishes the orientation-preserving *cycle* semigroup (which admits a natural involution) from the isotone-chain monoid: a matching on the larger cycle-oriented semigroup need not preserve the isotone submonoid. The 2014 paper establishes semigroup inverse-matching foundations and Hall-type existence criteria, not the coatom uniqueness asserted here. Related rank-two constructions apply at a different Green rank when \(n\ge4\).

## Limitations

The fixed-idempotent assumption is essential to the uniqueness assertion. The result does **not** solve existence of involutive matchings on the complete monoid \(\mathcal O_n\), and gives neither a classification of all involution matchings moving idempotents nor a count of general permutation matchings. An equivalent characterization under different terminology could have appeared in the literature; historical priority remains subject to independent evaluation.

## References

- P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912, first version October 1, 2026. https://arxiv.org/abs/2610.01912
- P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum **109** (2024), 141–147. https://doi.org/10.1007/s00233-024-10430-0
- P. M. Higgins, *Permutations of a semigroup that map to inverses*, Semigroup Forum **89** (2014), 169–182. https://doi.org/10.1007/s00233-013-9535-2
- P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, Semigroup Forum **98** (2019), 669–689. https://doi.org/10.1007/s00233-019-10018-z
