# Independent mathematical audit

## correctness

PASS

Define u=1, U multiplication by z, Q=I-P_u, M=u-perp and B=(Q U^-1)|_M. Orthogonal Kaczmarz error after measurements e_0,...,e_N equals E_N=U^N B^N Q, so ||E_N||=||B^N|| for N>=1. In coordinate basis D=diag(conjugate atoms) and u_j=sqrt(p_j), complementary adjugate minor gives det(t-B)=sum_j p_j product_{k != j}(t-conjugate atom_k); positive p_j excludes any eigenvector of modulus one on u-perp. Gelfand yields spectral root-rate for m>=2. Nilpotence is equivalent to polynomial t^(m-1); evaluating at nodes yields p_j P’(w_j)=w_j^(m-1); conjugating P’ on the unit circle implies all w_j^m equal, hence regular polygon; then p_j=1/m. Conversely uniform roots make polynomial t^(m-1), and rank counting shows m-1 is minimal common N. Two-atom scalar compression gives norm [1-4p(1-p)sin²(delta/2)]^(N/2). Actual finite numerical verifier inspected and checks these identities on bounded deterministic supports; infinite statement rests on complete algebraic proof, not numerics.

## originality

PASS

Qualitative convergence, strict compression spectral radius below 1, and Gelfand-rate machinery were already known for positive atomic stationary sequences. The new exact weighted root-polynomial factor and complete zero-rate/finite-step rigidity classification are not stated in the checked relevant results; originality is conditional on possible unindexed OPUC or finite-product projection formulations.

## value

PASS

PASS: An explicit sharp rate and complete finite-termination rigidity theorem for arbitrary strictly positive finite atomic Fourier Kaczmarz sequences is a substantive structural classification of a natural recovery problem, beyond qualitative known effectiveness. It separates universal exponential convergence from the singular exactly-terminating regular-polygon design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
