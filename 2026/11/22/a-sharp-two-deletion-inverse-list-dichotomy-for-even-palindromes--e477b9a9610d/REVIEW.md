# Scientific review: A sharp two-deletion inverse-list dichotomy for even palindromes

## Correctness — PASS

The universe is every even palindrome of length \(2m\) on a labeled alphabet of size \(q\ge2\), for integers \(m\ge1\). Deletions are exactly two arbitrary distinct positions; distinct parent words, rather than edit histories, are counted. An even palindrome is a unique one-deletion palindromic supersequence of any admissible odd receiver: the inserted letter is fixed by odd-parity counts, and distinct insertion positions cannot give different palindromes. Palindromic receivers permit a symmetric embedding in any palindrome source, so their inverse count is exactly \(1+m(q-1)\). For nonpalindromic receivers strip equal outer letters, then any source must begin and end with one of the two different core endpoints. Each endpoint choice reduces to the rigid one-insertion palindromic problem and produces at most one parent. This proves at most two. The two-parent family and maximal receiver count are exhibited explicitly. Exhaustive independent two-deletion shadow enumeration and the reconstruction procedure agree for 22 parameter families and 2,609 source words; it verifies all receiver lists within those families. No finite enumeration is used as a substitute for the general proof.

## Originality — PASS, qualified

Full published one-deletion palindrome source graph proofs concern one deletion only, and their single-deletion rigidity is credited as antecedent. A separate full published two-deletion sphere-size polynomial enumerates outgoing descendant counts for arbitrary sources, not the receiver-conditioned inverse lists here. The inspected classical single-deletion survey and broader deletion-code bounds do not imply the palindromic two-deletion inversion theorem. Searches of equivalent insertion formulations, aliases, and receiver-list parameters identified no dominating theorem. This comparison does not establish global uniqueness; unpublished or unindexed prior coverage and incompletely inspected older papers remain risks.

## Mathematical value — PASS

Two-deletion list sizes measure the worst-case synchronization-decoding ambiguity of a natural palindrome-constrained channel. The proof gives a sharp answer uniform in alphabet size and block length; a complete criterion for the maximizing received words; and an explicit finite-branch decoding strategy for all other received words. The sharp discontinuity between palindromic and nonpalindromic received data is structural, rather than a routine special-case substitution. The result does not resolve general optimal multi-deletion code design.

## Closest work and limitations

N. J. A. Sloane, *On Single-Deletion-Correcting Codes* (2002), addresses classical one-deletion code structure. Kulkarni and Kiyavash (2012), *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, address general code-size bounds. Brakensiek, Guruswami and Zbarsky (2015) concern multi-deletion constructions. Published accounts of one-deletion confusability for palindromes and all-alphabet two-deletion descendant sphere distributions are not receiver-conditioned inverse-list theorems. Earlier unindexed coverage remains possible. Exhaustive checks are finite and do not constitute independent formal verification.

Self-review: passed. Independent audit: not yet performed.
