# Character-conditioned power stabilization in finite partition-preserving transformation monoids

## Finding

Let a finite nonempty set \(X\) be partitioned into nonempty labelled blocks \(X_1,\dots,X_r\) of sizes \(n_1,\dots,n_r\). Fix a transformation \(\chi:\{1,\dots,r\}\to\{1,\dots,r\}\). Let \(\mathcal T_\chi\) consist of all total transformations \(f:X\to X\) such that \(f(X_i)\subseteq X_{\chi(i)}\). Define the stabilization index \(s(f)\) to be the least integer \(h\ge0\) such that \(f^{h+1}=f^h\), and set \(s(f)=\infty\) if none exists. All powers are ordinary composition, and \(f^0\) is the identity.

**Theorem (complete character-conditioned stabilization profile).** Write \(F=\{j:\chi(j)=j\}\). If \(\chi\) has any directed cycle of length greater than one, no element of \(\mathcal T_\chi\) has finite stabilization index. Otherwise, every block index \(i\) reaches a unique fixed point \(\rho(i)\in F\) after \(d_i\) applications of \(\chi\). Put

\[
 d=\max_i d_i,\qquad H=\max_i\bigl(d_i+n_{\rho(i)}-1\bigr).
\]

Then the set of finite stabilization indices realized in \(\mathcal T_\chi\) is **exactly every integer** \(d,d+1,\ldots,H\) (no gaps). In particular, \(d\) and \(H\) are sharp.

The exact number of transformations with finite stabilization index is

\[
 E_\chi(\boldsymbol n)=
 \prod_{i:\chi(i)\ne i} n_{\chi(i)}^{\,n_i}
 \prod_{j:\chi(j)=j}(n_j+1)^{\,n_j-1}.
\]

For a uniform choice among the \(\prod_i n_{\chi(i)}^{\,n_i}\) members of \(\mathcal T_\chi\), the probability of finite stabilization is

\[
 \Pr(s(f)<\infty\mid\chi)=
 \prod_{j\in F}\frac{(n_j+1)^{n_j-1}}{n_j^{n_j}}.
\]

Thus this probability depends on the fixed-point block sizes and **not** on the sizes of nonfixed blocks, once \(\chi\) is fixed. If \(\chi\) has a nontrivial cycle, the count and probability are zero.

Moreover, the following finite, explicitly extractable multivariate exponential generating function determines the entire distribution of \(s(f)\). For \(h\ge0\), start with \(T_i^{[0]}=x_i\), and recurse

\[
 T_j^{[h+1]}=x_j\exp\!\left(\sum_{i:\chi(i)=j}T_i^{[h]}\right),\qquad
 G_{\chi,h}(\boldsymbol x)=\exp\!\left(\sum_{j\in F}T_j^{[h]}\right).
\]

Then

\[
 A_{\chi,h}(\boldsymbol n)=\left(\prod_{i=1}^r n_i!\right)
 [x_1^{n_1}\cdots x_r^{n_r}]G_{\chi,h}(\boldsymbol x)
 =\#\{f\in\mathcal T_\chi:f^{h+1}=f^h\}.
\]

The number having stabilization index **exactly** \(h\) is \(A_{\chi,h}-A_{\chi,h-1}\), with \(A_{\chi,-1}=0\). For any prescribed subsemigroup \(\mathbb S\) of the full transformation semigroup on the block set, the corresponding count in the partition-preserving semigroup \(\mathcal T_{\mathbb S}=\bigcup_{\chi\in\mathbb S}\mathcal T_\chi\) is the sum over \(\chi\in\mathbb S\), because each map has a unique block character.

## Assumptions and scope

All block sizes are positive integers, the block set is finite and nonempty, and transformations are total. The block character is a specified function, not necessarily an idempotent or an element of a group. The index convention permits \(h=0\), which occurs precisely for the identity transformation. The infinite-index case includes transformations possessing a directed cycle of length greater than one. For a character with nontrivial cycles, every compatible transformation has infinite stabilization index, even though individual point orbits may enter a periodic cycle.

## Proof

**1. Character obstruction.** The character of \(f^k\) is \(\chi^k\), since images of each nonempty block stay in exactly one block under composition. Consequently \(f^{h+1}=f^h\) forces \(\chi^{h+1}=\chi^h\). A finite functional graph of \(\chi\) has this property for some \(h\) exactly when all its directed cycles are fixed points. This proves the zero case.

**2. Rooted-forest criterion.** The functional graph of any finite total transformation consists of directed cycles with rooted incoming trees. Equality \(f^{h+1}=f^h\) holds exactly when every cycle is a fixed point and every point reaches one in at most \(h\) steps. In particular, finite-index transformations are rooted forests, with edges directed towards a root, and every root in block \(j\) requires \(\chi(j)=j\).

**3. Total count and conditional law.** Assume every \(\chi\)-cycle is fixed. For each nonfixed index \(i\), its entire block must map into \(X_{\chi(i)}\), with \(n_{\chi(i)}^{n_i}\) independent choices. These arrows cannot participate in a nontrivial directed cycle, since block indices move strictly along a directed transient path towards a fixed index. In each fixed block \(X_j\), the restriction must instead be a function with only fixed-point cycles. Such functions are exactly directed rooted forests on the \(n_j\) labelled vertices: adjoining one new vertex and joining each root to it gives an ordinary labelled tree on \(n_j+1\) vertices. By the classical Prüfer correspondence their number is \((n_j+1)^{n_j-1}\). Independent multiplication gives \(E_\chi\). Dividing by the unrestricted character-fiber cardinality proves the displayed probability.

**4. Bounds and gap-free index support.** For a point in block \(i\), its block sequence before entering the fixed block is \(i,\chi(i),\ldots,\rho(i)\), and has exactly \(d_i\) transient steps. Once in the fixed block \(\rho(i)\), a path towards a fixed point may traverse at most \(n_{\rho(i)}-1\) further edges before the root, because the vertices on that path are distinct. Therefore \(d\le s(f)\le H\) whenever \(s(f)\) is finite: the lower bound also follows from \(\chi^{s(f)+1}=\chi^{s(f)}\).

For every integer \(h\) with \(d\le h\le H\), pick a block \(i_*\) realizing \(H=d_{i_*}+n_{\rho(i_*)}-1\). Set \(\ell=h-d_{i_*}\), which lies between zero and \(n_{\rho(i_*)}-1\), because \(d_{i_*}\le d\le h\). Select one representative in each transient block on the \(\chi\)-path from \(i_*\) to \(\rho(i_*)\), and build a directed chain of \(\ell\) arrows inside the fixed block \(\rho(i_*)\), ending at a fixed root. Route the selected transient representatives along the block path and into the initial vertex of that chain. For every other nonfixed block vertex, map it to the selected representative of its successor block (or directly to the indicated root/initial chain vertex upon reaching a fixed block); make unused vertices of fixed blocks fixed. Then the selected starting point has path length \(h\). Every other point destined for the selected fixed block has transient depth at most \(d_{i_*}\), because \(i_*\) is a deepest transient block reaching that fixed block (otherwise \(H\) would be larger). Its total path length is at most \(d_{i_*}+\ell=h\). Every point destined for another fixed block reaches a root within \(d\le h\) steps. Thus the constructed map has stabilization index exactly \(h\), proving every intermediate value occurs.

**5. Full height enumeration.** A rooted tree of height at most \(h\), whose root has type \(j\), consists of a root vertex of type \(j\) and an unordered collection of rooted trees of height at most \(h-1\) whose root types \(i\) satisfy \(\chi(i)=j\). The standard labelled exponential formula gives \(T_j^{[h]}=x_j\exp(\sum_{i:\chi(i)=j}T_i^{[h-1]})\). Only types fixed by \(\chi\) can be global roots; a rooted forest is an unordered set of such trees. Thus its EGF is \(G_{\chi,h}\). Taking the coefficient with labelled vertex counts gives \(A_{\chi,h}\). Subtraction yields exact height; summing over disjoint character fibers yields the subsemigroup formula. No inference from finite computation is needed for these identities.

## Verification

The accompanying standard-library program `verify.py` independently computes each finite-truncation coefficient of \(G_{\chi,h}\) using exact rational polynomial arithmetic. It also enumerates compatible total transformations directly, tests \(f^{h+1}=f^h\) point by point, and checks the closed product and the gap-free support criterion. It verified 2,441 separate profile-character-height comparisons with at most six points and at most three blocks. Example: with block sizes \((2,2)\), the character \(\chi=(0,0)\) gives cumulative stabilization counts \(0,6,12,12,12\) at heights \(0,1,2,3,4\); the swap character \((1,0)\) gives zero at every height. The exact theorem is proved above, not extrapolated from the enumeration.

## Relationship to prior work

Sarkar and Singh, arXiv:2310.19414 (2023), introduce and examine the precise character-restricted transformation semigroups and in Proposition 3.9 characterize their idempotents. Their results on regularity, units and Green relations do not provide the character-conditioned power-stabilization spectrum or the displayed coefficient formula. Sarkar and Singh, arXiv:2006.04242 (2020), enumerate idempotents in the block-surjective partition-preserving subsemigroup, a different and more restricted power-index-one situation. The ordinary Cayley formula and labelled-tree exponential formula are classical ingredients and are not claimed as new. The distinction is the complete power-height support, product probability and every-height distribution for arbitrary characters and partition sizes.

## Limitations

No claim is made that rooted-forest enumeration itself is new. The novelty assessment is relative to inspected sources and indexed records; a general multitype functional-digraph enumeration could conceivably imply some formulas by specialization. The results require all blocks to be finite and nonempty; infinite sets, partial transformations and nontrivial eventual periods are outside scope. The reported finite checks cover at most three blocks and six vertices, while the proof applies to all finite partitions. Independent mathematical review has not been performed.

## References

1. M. Sarkar and S. N. Singh, *Semigroups of transformations whose characters belong to a given semigroup*, arXiv:2310.19414, first submitted 2023-10-30. https://arxiv.org/abs/2310.19414.
2. M. Sarkar and S. N. Singh, *On certain semigroups of transformations that preserve a partition*, arXiv:2006.04242, first submitted 2020-06-07. https://arxiv.org/abs/2006.04242.
3. Classical Prüfer correspondence and the labelled combinatorial exponential formula for rooted forests (used as background results, not priority claims).
