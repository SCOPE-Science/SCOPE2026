# Scientific review: exact ternary multiset two-deletion sizes through twenty

## Correctness — PASS

The claim covers exactly the fifteen integer lengths \(6\le n\le20\), a three-symbol multiset alphabet, and two unordered deletions. The deletion-confusability criterion is the elementary identity \(d(u,v)=n-\sum_i\min(u_i,v_i)\): two inputs share a length-\(n-2\) descendant if and only if \(d(u,v)\le2\). Each upper certificate consists of rationally weighted cliques in that confusability graph, covering every input vertex with total weight at least one. For any distance-three code, at most one member lies in each such clique, giving the exact upper bound \(|C|\le\lfloor\sum_Kw_K\rfloor\). A concrete independent witness of matching size is supplied for each length. The standard-library checker reconstructs every finite vertex, checks all certificate edges, every cover inequality, every witness distance, and all rational sums without depending on a solver. All fifteen certificates passed execution.

**Limits:** This finite proof does not establish a formula for arbitrary \(n\), and the numerical optimizer used to discover certificates is not itself part of the proof.

## Originality — PASS against inspected evidence

The nearest primary sources concern the same multiset deletion metric, but their exact results have different scopes. *Perfect Codes in the Discrete Simplex* (arXiv:1307.3142) handles perfect-code existence including a ternary length-four case. *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments* (arXiv:1612.08837), Corollary 16, gives the fixed-alphabet asymptotic, not this finite optimum sequence. *Multiset Deletion-Correcting Codes: Bounds and Constructions* (arXiv:2601.05636) establishes cyclic Sidon classes, binary optima and near-extremal regimes, but does not state the finite exact ternary two-deletion profile. *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes* (arXiv:2603.18322) establishes ball enumerators and general bounds, not these code-size equalities. The claim does not include the established perfect-code, asymptotic or Sidon-construction statements.

**Limits:** Results could already exist under two-packings in finite triangular grids, as unpublished computations, or in unindexed earlier work. The comparison is substantive but is not a proof of global priority.

## Value — PASS

Ternary multisets form the first genuinely two-dimensional multiset coding space. Two deletions are the first nontrivial Sidon-length regime in this dimension. Exact optimum sizes quantify the boundary penalties in small lengths where asymptotic \(n^2/14\) does not decide the answer. Thirteen of the fifteen optima strictly exceed the natural cyclic seven-syndrome construction; at length six the improvement is six codewords instead of four. The finite table is accompanied by direct, machine-checkable witnesses and upper certificates, rather than relying on a solver's claimed optimality.

## Verification and limitations

Run `python3 s3_check.py s3_cert.json`. This validates the exact fifteen finite claims; it does not check unpublished literature or give independent mathematical certification. All references are to primary scientific literature or the attached explicit evidence.

Self-review: passed. Independent audit: not yet performed.
