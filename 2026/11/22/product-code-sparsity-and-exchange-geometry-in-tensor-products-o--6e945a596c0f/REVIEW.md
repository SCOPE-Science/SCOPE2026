# Scientific review: total-perfect-code geometry in tensor products of bicliques

## Correctness — PASS

The theorem is proved by a complete component decomposition: a tensor product of \(r\) nonempty bicliques has \(2^{r-1}\) components, each a complete bipartite graph between complementary shore patterns. A total perfect code of a complete bipartite graph necessarily and sufficiently selects one vertex per shore, proving the all-code count and complete exchange graph. The projection argument establishes the product-code distance formula and exact spectrum; the complementary-pattern construction establishes the covering-radius upper bound, and coordinate injectivity gives the matching lower bound under the stated size hypothesis. The proof applies to every integer \(r\ge2\), \(a_i,b_i\ge2\) and contains no asymptotic or unproved computational step.

The extracted C++17 checker exhausts \(2^{16}\) and \(2^{20}\) graph subsets for two independent two-factor examples, reconstructs all code-exchange edges, verifies the distance formula and the radius. The separate Python checker enumerates all four-element code candidates, checks the three-factor product-code distance distribution and independently certifies the sharp large-shore covering-radius construction at arity three. These finite computations corroborate, but do not establish, the infinite theorem.

## Originality — PASS (qualified by historical priority risk)

Abay-Asmerom, Hammack and Taylor (2008), *Total Perfect Codes in Tensor Products of Graphs*, prove an existence criterion for arbitrary tensor products and exhibit that full code counts cannot generally be reconstructed from factor counts alone. The complete six-page publisher PDF was examined, including Theorem 2.1 and its numerical example. It does not enumerate all codes for products of arbitrary bicliques, identify the whole exchange graph, derive the factorwise-code distance spectrum or give the sharp covering radius. Hammack (2006) treats connected components of bipartite graph products, not total-perfect-code geometry. A related exact four-cube code-exchange finding concerns a different connected graph, not the disconnected product of bicliques.

Relevant mathematical-record searches under aliases (total perfect code, efficient open domination, tensor/direct/Kronecker product, code reconfiguration and factorability) revealed no equivalent theorem or stronger published implication. The prior existence theorem and standard component observation are acknowledged as prerequisites rather than attributed as discoveries. The possibility of an unindexed equivalent counting or geometry result remains; this is same-model scholarly review, not independent priority certification.

## Value — PASS

The 2008 primary work explicitly highlights that products can possess total perfect codes not obtained by multiplying factor codes and that code counts have no general factor-count rule. The biclique-factor family gives a natural exact quantitative answer: only \(B\) of \(B^{2^{r-1}}\) valid codes factor, but all feasible codes form one connected Cartesian Hamming graph. The exact separation of product codes by \(2^{r-1}\) exchanges coexists with an upper covering radius \(2^r-2\), sharp for large shores and unconditionally sharp for two factors. Thus factorability has a precise, nontrivial density/distance/approximation trade-off for an infinite product family, rather than a single numerical increment or arbitrary finite slice. The claim is restricted to tensor products of bicliques; no general-factor result is asserted.

## Residual limitations

No classification of general bipartite-factor products is given. For \(r\ge3\) with smaller shores, the exact covering radius is not established. Further unindexed literature or unpublished theses may contain equivalent statements. The finite verification scripts are reproducibility aids, not an external audit.

Self-review: passed. Independent audit: not yet performed.
