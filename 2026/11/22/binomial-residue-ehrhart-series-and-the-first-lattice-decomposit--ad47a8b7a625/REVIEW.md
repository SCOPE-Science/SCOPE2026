# Independent mathematical audit

## correctness

PASS

For odd n, det(I+wS)=1+w^n. Multiplying by the alternating geometric sum proves the inverse formula. Each row of this inverse, evaluated on b in {1,...,w}^n and multiplied by 1+w^n, is bounded below by 1 and above by w^n by selecting the respective extreme independently for each sign. Thus the w^n images and zero lie in the half-open coefficient cube; the determinant index proves exhaustiveness. The integer-degree cone lattice is the kernel of coordinate sum modulo w+1, not the entire ambient integer lattice. Splitting coefficients into integral and fractional parts gives the numerator and denominator (1-t)^n and the volume index (1+w^n)/(w+1). The bounded sums fill the interval [n,nw], and complementing every b_i reflects positive degree j to n-j. When w<=n-2, q>=2: the absence of positive representatives below q means every point in those dilates is an integral vertex combination and in degree one only vertices occur. The inequality q<=floor(nw/(w+1)) holds for odd n>=3, w>=2, so degree q has a nonzero representative whose unique fractional coefficients preclude decomposition. For fixed w=2 this yields unbounded q on odd n>=5. Independently checked nine sample parameter pairs by enumerating multiples of the class of e_0 (order 1+w^n by the inverse diagonal coefficient) restricted to k divisible by w+1, rather than constructing the candidate box representatives. For example (7,2) gives 1+21t^3+21t^4 and (11,2) gives 1+11t^4+330t^5+330t^6+11t^7. Replay: python3 /workspace/review_evidence/check_1_2_4.py. The exact proof, not the samples, establishes the uniform claim.

## originality

PASS

Credit antecedent weighted-cycle determinant and inverse, empty unit dilate, failure of IDP, positive-degree symmetry, and the exact five-cycle numerator; the volume also has overlapping same-date coverage. The surviving claim is the complete residue-filtered numerator for every odd size and the first dilation at which a lattice point fails to decompose in the empty range. The prior non-IDP witness is at degree ceil(n/2), strictly later than the claimed first hole when the new threshold applies; the earlier degree-one proof does not enumerate the integral-degree representatives across the cone. No same-date ordering is inferred.

## value

PASS

The full graded residue distribution fills an invariant-level gap for the motivated weighted graph edge simplices; the first hole strengthens an existing yes/no nonnormality result to an exact dilation threshold. At constant weight the threshold can grow without bound, making this a natural explicit family of delayed obstructions and not just a rediscovery that these simplices are non-IDP.

The dated certificate retains the supplied scientific assessment, sources and limitations.
