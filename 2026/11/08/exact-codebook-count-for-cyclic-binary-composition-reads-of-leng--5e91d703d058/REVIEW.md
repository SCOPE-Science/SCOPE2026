# Review of exact cyclic binary four-read composition capacity

## Correctness — PASS
The theorem is for every indexed binary cyclic word of positive length and counts distinct profiles rather than rotation orbits. The run-coordinate identities reconstruct \(a,r,p,q,v_0,v_1,e\) from the 14 entries. A direct integer-composition argument proves the count \(V_r(m,u)\) of feasible length-two run counts. The induced-edge extremal argument on \(C_{2r}\), combined with connected adjacent swaps, proves the entire integer interval of singleton-run adjacency counts; the two-run case is handled separately. Independent exhaustive binary-word enumeration through length 20 agrees with the sum; incidence intervals through \(r=8\) and the short-read threshold through length eight were checked. Finite checks do not independently prove the all-length formula; the unrestricted run proof does.

## Originality — PASS, with residual historical-priority risk
An inspection of Acharya et al., arXiv:1403.2439 (2014), identifies the linear full-substring-composition reconstruction problem, not cyclic fixed-four-read capacity. Kiah, Puleo and Milenkovic, arXiv:1410.8837 (2014), treat ordered substring frequency profiles, a strictly more informative observation model. Ye and Elishco, arXiv:2208.14963 (2022), investigate linear length-limited composition reconstruction and codes, not this exact cyclic spectrum. Searches of the mathematical research index for four-fragment, cyclic composition, and length-limited reconstructions returned the closest related linear two-read results rather than an equivalent or dominating theorem. Existing length-three cyclic profile findings do not imply the extra run-length-two and singleton adjacency coordinates; the distinction first occurs at length eight. Search absence does not establish global priority. An unpublished computation, unindexed table or specialized corollary of a broader formula remains possible.

## Value — PASS
For a noiseless short-read composition channel on circular binary strings, the number of realizable observation profiles is exactly the largest zero-error codebook size. A fixed read cap of four is natural for bounded-resolution sensing; this new count is an exact all-blocklength capacity formula rather than a table of sample values. The structural classification explains a previously invisible adjacency constraint and isolates the shortest length at which four-reads strictly improve distinguishability over three-reads. No downstream theorem or broader generality is claimed.

## Sources and limits
- J. Acharya et al., *String Reconstruction from Substring Compositions*, arXiv:1403.2439, 2014-03-10, https://arxiv.org/abs/1403.2439.
- H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1410.8837, 2014-10-31, https://arxiv.org/abs/1410.8837.
- Z. Ye, O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, 2022-08-31, https://arxiv.org/abs/2208.14963.

Self-review: passed. Independent audit: not yet performed.
