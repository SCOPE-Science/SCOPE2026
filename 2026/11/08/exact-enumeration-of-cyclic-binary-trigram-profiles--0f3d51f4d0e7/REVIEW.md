# Scientific review: exact enumeration of cyclic binary trigram profiles

## Correctness — PASS
The eight edge-flow balances reduce all possible circular trigram profiles to a uniquely parameterized family. Eulerian-support connectivity excludes all and only disconnected balanced candidates. The connected cases produce a formal generating function; the finite geometric sums prove its rational form. Near \(z=1\), the fifth-order pole gives \(S(n)\sim n^4/288\). Direct and parameter-side enumeration, implemented separately in `verify.py`, agrees for all lengths through \(17\) and all formula coefficients through \(80\). The proof, not finite verification, supports all lengths.

## Originality — PASS, subject to literature uncertainty
Tesler (2017, arXiv:1708.03654) studies de Bruijn multiplicities and, for fixed weights, multicyclic decompositions; his inspected Sections 2 and 9 do not enumerate all realizable connected cyclic binary trigram count vectors. Bernardini et al. (CPM 2022, DOI 10.4230/LIPIcs.CPM.2022.16) study shortest strings with the same **set** of length-\(k\) substrings, not the full circular trigram multiset profile inventory. The closest published result encountered in published-finding corpus concerns linear binary 2-mer multispectra; it does not imply a 3-mer cyclic profile count. An additional de Bruijn multiplicity paper (Steyaert et al., 2020) was checked at abstract level only, so incomplete access and possible unindexed equivalents remain risks.

## Value — PASS
Exact trimer-count profiles are a basic observable in sequencing and k-mer-based reconstruction. The theorem classifies an infinite natural family without hidden restrictions, yields all possible observed signatures and an exact rational generating function, supplies asymptotic information, and determines the maximum size of an exact-trigram-distinguishable circular code.

## Scientific scope and limitations
Binary circular substrings of length three with multiplicity are counted. The proof does not enumerate the sizes of the fibres of the profile map, linear words, higher-alphabet spectra or longer k-mers. No independent scientific audit is asserted.

Self-review: passed. Independent audit: not yet performed.
