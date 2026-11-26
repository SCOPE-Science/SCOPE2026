# Independent mathematical audit

## correctness

PASS

Coding counts positive-right words once per iterate-fixed point, and no periodic point lands on x_1=0 (the source's 'crosses' should be read as 'hits', not as forbidding successive iterates on opposite sides). After step k an input strand i occupies position i+r_k mod 3; the strand occupying position zero is doubled. Thus the diagonal moduli on residue-zero words are 2^N_0, 2^N_2 and 2^N_1. In a nonzero residue the weighted permutation is a three-cycle with characteristic polynomial λ³−a, a≠0, so it cannot have an all-real spectrum. For P=(I+S)/2 the nontrivial multiplier (1+ω)/2 satisfies Re[λ/(1−λ)]=0, so the symmetric lag covariance cancels and Σ=I/3−11^T/9. The tilted finite matrix for the post-step occupations has leading eigenvalue with zero linear term and Gaussian quadratic term, and its spectral projection tends to the uniform stationary projection; the other modes vanish exponentially. Conditioning on residue zero leaves the CLT and the second-moment bound, since the condition has probability tending to 1/3, and excluding the all-left word costs O(2^−n). The continuous minimum and uniform integrability give the mean coefficient E max of three standard normals divided by √3, equal to √3/(2√π) by integrating 3φΦ² by parts. The uploaded checker was inspected, not executed; its finite matrix enumeration is not the limiting argument.

## originality

FAIL

The theorem is mathematically correct but follows from the prior stronger all-fixed-dimension CLT for the same word-level occupation vector, with a short terminal-mixing reduction to the real periodic ensemble. A separate prior exact census already covers the finite scalar laws. The conclusion is prior-implied, not a claim that the identical conditional asymptotic is printed verbatim or that scholarly priority is settled.

## value

FAIL

The periodic interpretation is useful context, but both the exact scalar law and the fluctuation mechanism are covered. Transferring the prior CLT by omitting o(√n) terminal steps, projecting to a minimum and evaluating a standard Gaussian order statistic leaves no substantial standalone contribution or valuable distinct remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
