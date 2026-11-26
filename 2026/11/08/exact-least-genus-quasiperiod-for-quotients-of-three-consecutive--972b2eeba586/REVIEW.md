# Independent mathematical audit

## correctness

PASS

In the block N=qa+r, 0<=r<a, no expression can use more than q generators; exactly q gives every excess up to 2q, and fewer cannot exceed q(a+2). Hence the disjoint missing intervals and their exact multiple counts are valid. Writing a=2pm+r and q=tp+s gives the floor summand 2(m-t)+δ_s(r). Summing complete p-blocks and the tail gives the proposed quadratic. Summing remainders of sk modulo p uses every multiple of gcd(p,k) with multiplicity gcd(p,k); subtracting the contribution from exact divisibility in the shifted first floor gives D_p(r). After conversion to polynomials in a, the linear coefficient has period p for p=3 and p>=5 (for p>=5 the two maximal residues of the gcd sum are 0,-2 and cannot be permuted by a nonzero translation), and period 2 at p=4. The constant terms obstruct period p: for odd p both tails at 0,p vanish and the difference is -1/4; for even p, with r=p+1 the tail counts s<p/3 in 0<=s<=p/2-1, giving ceil(p/3), whereas the tail at 1 is empty. The branch difference is the stated strictly positive constant for even p>=4. Any eventual period T and 2p give gcd(T,2p) by equality of branch polynomials on infinite compatible progressions. This and the explicit p=2 parity polynomials give precisely the claimed least periods, including p=4.

## originality

PASS

The supported distinct claim is the all-residue exact genus formula with the sharp least eventual period. Previously treated divisibility branches and the generic root-of-unity genus identity are not new. The frozen comparison understates Liu 2604.26415: it does include the target family on p dividing a. Neither that specialization, nor the closest same-family Frobenius result, yields the stated unrestricted genus-period classification.

## value

PASS

The genus, unlike the Frobenius number, measures every missing element of a quotient. The gcd statistic and separate constant-term obstruction predict exactly which polynomial branches must be distinguished for the first consecutive three-generator family. The genuine period doubling and its exception are structural information, not a finite re-tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
