# Self-review

## Correctness — PASS

Rule 54 is exactly the stated local Boolean function. The four binary de Bruijn overlap states and displayed edge matrices encode cyclic predecessor configurations bijectively as closed walks, including the short rings. Capping every nonnegative matrix entry at two preserves the question whether the diagonal trace is exactly one. Breadth-first exploration from the identity reaches exactly 410 distinct capped matrices and exhausts both outgoing transitions. Integer arithmetic verifies the 410-coordinate annihilator identity \(T^3\sum_{j=0}^{14}q_jT^{14-j}f=0\), and 17 initial coefficients determine the displayed rational generating function for every positive length. An independently written direct local update enumeration checks all indexed inputs at lengths 1 through 18. The source programs, not an unattested computation log, are essential reproducible evidence.

## Originality — PASS, qualified

Jen (1989, pp. 444–446 and Appendix A, primary PDF inspected) gives preimage recurrences for given linear blocks and a Rule 54 forbidden-block image description, but does not state a cyclic *all-target singleton-fibre enumerator*. Powley's thesis (2009, chapter 9) and the Powley–Stepney (2010) article treat de Bruijn counting of prescribed outputs, especially homogeneous configurations, not counts of how many outputs have one predecessor. Fukś (2003; verified arXiv public upload 2013-05-28) treats sequences of preimages of selected local blocks and multiple time steps. The exact new polynomial ratio is not an immediate evaluation of any displayed earlier theorem; it requires counting words whose associated matrix product has trace exactly one. Dedicated mathematical-record searches for Rule 54 cyclic singleton counts, image sizes, periodic Garden-of-Eden sets, and aliases found no directly equivalent statement. This is a best-knowledge priority judgment, not a proof of uniqueness. The full Powley–Stepney journal article and possible unindexed computational tables remain residual priority risks.

## Mathematical value — PASS

The number of outputs with a unique predecessor is a natural finite-volume inverse-reconstruction invariant, strictly refining the size of the image or the mere existence of Garden-of-Eden states. An explicit all-length rational generating function with a finite integer certificate is not a conventional textbook exercise, a renaming of a tabulated sequence, or a routine increment in a numerical cutoff. It quantifies precisely the unambiguous one-step outputs in a well-studied nonlinear CA. The result does not classify all multiplicities or claim a more general theorem than stated.

## Closest sources, verification boundaries and residual risks

- E. Jen, *Enumeration of Preimages in Cellular Automata* (1989): full relevant sections on local block preimages and Rule 54 image restrictions inspected.
- E. J. Powley, *Global properties of cellular automata* (2009), chapter 9: de Bruijn preimage methods for selected outputs examined.
- E. J. Powley and S. Stepney, *Counting Preimages of Homogeneous Configurations in 1-Dimensional Cellular Automata* (2010): abstract and scope inspected; full journal text not conclusively inspected. The closely related thesis is available.
- H. Fukś, *Sequences of Preimages in Elementary Cellular Automata* (2003): open-access article and dated arXiv record examined.

Exact finite-state certificate and independent length-at-most-18 enumeration are included. Finite direct checks alone would not suffice for all lengths; the proven vector recurrence supplies that step. Independent scientific review and comprehensive historical priority audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
