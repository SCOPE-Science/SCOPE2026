# Independent mathematical audit

## correctness

PASS

For n>=2 and positive q_j with r_k=sum_{j<=k}q_j>=k, the open chamber D_n has positive Lebesgue measure; its boundary is null. The source substitution w_1^2=q_1 z_1^2-(q_1-1)z_2^2, w_j=z_j for j>=2 maps the interior bijectively to itself. The inverse gives sqrt(q_1)|det(dz/dw)|=w_1/sqrt(w_1^2+(q_1-1)w_2^2)<=1, strictly <1 at every interior point if q_1>1 since w_2>0. The transformed quadratic form has coefficients (1,q_1+q_2-1,q_3,...), first prefix 1 and later prefixes r_k. Summation by parts gives transformed Q(w)-sum w_j^2=sum_{k=2}^n(r_k-k)(w_k^2-w_{k+1}^2)>=0, with w_{n+1}=0. Hence integral equality is impossible if q_1>1. If q_1=1 the map is identity, and Q(z)-sum z_j^2=sum_{k=1}^n(r_k-k)(z_k^2-z_{k+1}^2); each square gap is strictly positive on D_n. Equality of the two positive integrals forces every prefix defect zero, whence q_j=1 for all j. Conversely all ones gives equality. For n=1, Gaussian rescaling gives equality for all q_1>0, confirming the sharp dimension boundary. In a nondegenerate orthoscheme, q_j=beta_j^2 and r_k=|b_k|^2. Zwierzyński Proposition 3.2 Eq. (18) identifies the exact local sector ratio as a positive n-constant divided by beta_1 I(q), so equality is equivalent to the integral equality; beta_j>0 then forces beta_j=1, unique standard cube-flag orthoscheme up to orthogonal congruence. Independent symbolic identities in 14 finite dimensions, 2250 exact-rational admissible pointwise tests, 6 exact two-dimensional integral calculations, and independent Git tree reconstruction corroborate but are not substituted for the universal argument.

## originality

FAIL

Decisive same mathematical model prior mathematical coverage: Zwierzyński arXiv:2609.27798v1 (posted Aug 19 2026) already gives in the PROOF of Lemma 3.1 the exact normalized Jacobian comparison (10), prefix-square excess (11), and positive-integrand identity leading to (9). Its n>=2 proof itself implies the iff equality claim without a new lemma: (10) is strict on the entire interior if q_1>1, while with q_1=1 any r_k>k makes (11) strictly greater at every interior w. Therefore integral equality forces q_1=1 and all later prefixes r_k=k, hence every q_j=1. Proposition 3.2 Eq. (18) gives exactly the local orthoscheme quotient reduction with q_j=beta_j^2. Thus the entire submitted orthoscheme rigidity statement is an immediate equality-case corollary of the published pointwise proof, even though the earlier paper does not typeset an independent iff theorem. This is COVERED BY MATHEMATICAL IMPLICATION, not merely a title match or matching extremal example. Karasev arXiv:2505.16247v1 supplies only n=2,3 surface-area inequality and cube attainment, and is not the decisive source. Three Resultary searches returned the assigned listing itself (self-match excluded) and nearby inequivalent geometry items; absence of another hit is not novelty evidence.

## value

PASS

The precise local equality geometry is intrinsically motivated: in the new sharp dimension-free surface-area theorem, every flag contributes an orthoscheme sector quotient, so knowing whether nonstandard orthoschemes attain the sharp local constant is a natural necessary ingredient in studying global equality and quantitative stability. The result identifies a dimension boundary (n=1 non-rigid; n>=2 rigid) and exact all-dimensional extremal geometry, rather than an arbitrary numerical slice. Its analytic derivation is routine from the prior paper and is not an independent original advance, but the equality classification is a mathematically useful structural interpretation of the sharp bound. No global rigidity or deficit modulus is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
