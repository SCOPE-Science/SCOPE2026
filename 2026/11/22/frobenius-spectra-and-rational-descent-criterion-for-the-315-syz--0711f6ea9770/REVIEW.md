# Scientific review — Frobenius spectra and rational-descent criterion for the \(315\) syzygetic tetrads of a Cayley octad

## Correctness — PASS
The construction begins with a classical Frobenius-equivariant Cayley-octad bijection between the 28 bitangents and the 28 unordered edges on eight labels. The theta-characteristic four-sum criterion gives exactly 210 four-cycles plus 105 perfect matchings. All 22 conjugacy types are covered by exact orbit enumeration and independently checked fixed powers in `VERIFY.py`. The criterion excluding exactly octad cycles of lengths 5 and 7 has a constructive proof independent of the numerical table. The theorem is conditional on a stable regular octad and odd characteristic.

## Originality — PASS, provisional
Plaumann–Sturmfels–Vinzant (2010/2011) and Dolgachev (2012) establish the geometric combinatorics; Elsenhans–Jahnel (2017) give the Galois-octad framework; Bergvall (2023) supplies a wider permutation-character perspective. A published integral incidence calculation for all 315 tetrads concerns a different invariant. The complete 22-class Frobenius cycle table, rational-tetrad obstruction, and precise no-rational-bitangent cases are not stated in the inspected texts. The known S8 action logically enables this finite calculation and character theory may encode fixed-point data; older unindexed equivalent tables have not been excluded. No claim of exhaustive historical priority is made.

## Mathematical value — PASS
This resolves a natural arithmetic descent invariant attached to every smooth odd-characteristic plane quartic with a rational Cayley octad: fields of definition of 315 geometric tetrads, their finite étale zeta functions and the precise obstruction to any rational tetrad. It separates descent of a four-bitangent conic configuration from descent of its member bitangent lines, including three sharply characterized types where the former exists and the latter do not.

## Sources and limits
The archive anchor is arXiv:1008.4104 first posted on 2010-08-24; supporting comparisons include Dolgachev (2012), arXiv:1710.07279, and DOI:10.1007/s40879-023-00711-3. The result does not assert realizability of all 22 types over a fixed finite field, nor extend to characteristic two. Explicit table and verification code are in RESULT.md and VERIFY.py.

Self-review: passed. Independent audit: not yet performed.
