# Independent mathematical audit

## correctness

PASS

For S_n=OG(n+1,2n+2) over C in the MINIMAL half-spin embedding, the hyperplane Schubert generator is the one-box strict-partition class. Kresch–Tamvakis classical Pieri (k=1,N'=0) makes its top self-intersection the count of saturated chains from empty partition to strict staircase rho_n; the shifted hook-length formula gives D_n=M!*prod(a!,a=2..n-1)/prod((2a-1)!,a=2..n), M=n(n+1)/2. Apply Legendre v_2(t!)=t-s_2(t): the linear terms cancel since M+sum_{a=2}^{n-1}a=sum_{a=2}^n(2a-1)=n^2-1; s_2(2a-1)=s_2(a-1)+1 makes the digit sums telescope to v_2(D_n)=n-s_2(M). n=1..6 give valuations 0,0,1,2,1,3; for n>=7, M<2^{n-2}, so s_2(M)<=n-2 and no further odd or 2 (mod 4) degrees occur. I independently computed arbitrary-precision factorial degrees, binary valuations, and exhaustive strict-partition chain recurrences for all n=1..15, and reconstructed BOTH original JSON Git blobs and the native Git root tree SHA-1.

## originality

FAIL

The entire geometrically indexed degree sequence and EXACT all-n factorial product already appear in OEIS A003121, which explicitly identifies the numbers as degrees of spinor varieties and shifted staircase tableaux (Burt Totaro comment dated 2002; OEIS all-n factorial formula predates the audited claim). The claimed two-adic valuation is obtained by applying the elementary Legendre factorial valuation to that already published product and using s_2(2a-1)=s_2(a-1)+1. This one standard valuation/telescoping operation implies the COMPLETE claimed formula, hence also both small-residue classifications. Thus lack of an identical printed digit-sum identity is NOT evidence of an original mathematical theorem. Established geometric Pieri/hook results also cover the degree as a prior theorem; there is no unaccounted nonstandard insight beyond this routine specialization.

## value

PASS

The degree of each minimally embedded spinor variety is a canonical enumerative invariant, and exact 2-power divisibility of complementary linear-section counts has useful arithmetic content throughout the natural family, including complete odd-degree and 2 mod 4 cutoffs. The invariant and family are motivated independently of the computation and the formula covers all dimensions. This is a small, readily reusable closed invariant—not a new geometric structural theorem or a major contribution. Its usefulness is separate from originality, which fails because the exact result is a routine implication of the already published degree product.

The dated certificate retains the supplied scientific assessment, sources and limitations.
