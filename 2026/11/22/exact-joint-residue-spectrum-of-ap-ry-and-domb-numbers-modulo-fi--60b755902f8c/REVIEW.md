# Independent mathematical audit

## correctness

PASS

Reconstructed both digit reductions from the defining unsigned sums. Lucas for binomial(n,j) and the first carry in n+j eliminate precisely the disallowed Apéry terms. For Domb, grouping the multinomial-square sum by two of the four parts gives the stated integer definition by Vandermonde, and only carry-free multinomial terms survive. Independent single-digit evaluation gives (1,1),(0,4),(3,3),(0,1),(1,1). With g marking 3, the diagonal census is (2+g)^L in Z[g]/(g^4-1). Subtracting it from (3+g+g^2)^L leaves a coefficient vector with Fourier values 5^L-3^L, 3^L-1, 0, 0 at 1,-1,i,-i; inversion recovers exact residue labels, counts, bias and L=0. All eight cells are positive at L=3 and padding with digit 4 preserves each pair at infinitely many distinct indices. Fresh replay: python3 -B /workspace/reviews/reproduce.py 4; direct Pascal-residue sum evaluations for 250 indices (complete blocks through L=3) and independent pair-transition checks through L=12 passed. Finite checks are not the all-index proof.

## originality

PASS

Pass the precise ordered full histogram for classical Apéry and unsigned Domb modulo five, not Lucas congruences, Domb-only sign bias or cyclic Fourier inversion. The searched equivalent labels and inspected stronger candidates do not supply the conditioned four-unit census; the reported Domb-only sign work overlaps its mechanism but not the full supported result on available evidence. No priority guarantee.

## value

PASS

For two standard unsigned binomial sums the complete census identifies a rigid cross-sequence constraint: the nonzero Apéry stratum forces exact equality, whereas the zero stratum exhibits exact quadratic-character bias without any order-four component. The missing cells and finite-depth bias, including their crossover in support, are useful baseline data for comparative mod-five behavior; this is more than evaluating the five digit terms or re-proving Lucas. The contribution is a modest explicit classification, not a new congruence technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
