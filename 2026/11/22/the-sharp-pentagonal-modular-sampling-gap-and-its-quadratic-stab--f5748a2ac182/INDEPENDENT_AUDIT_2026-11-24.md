# Independent mathematical audit

## correctness

PASS

The five-point DFT gives squared norms (2/5)|S_1|^2 and S_0^2/5+(2/5)|S_2|^2 for the two projections, with S_r=sum_j n_j zeta^(rj). For S_0=0, the coefficient polynomial is divisible over Z by 1-z, and its value at zeta is nonzero for nonzero n because the only degree-at-most-four polynomial relation is a multiple of Phi_5 with nonzero augmentation. The two complex embeddings and their conjugates give |S_1|^2|S_2|^2=5|N(beta_n)|, proving the stated product and unit equality condition, and excluding a nonzero integer point of E. For a nearest vector n to f with distance delta, nonzero augmentation gives delta>=1/sqrt(5); n=0 gives delta=||f||. Otherwise orthogonal projection gives (||f||+delta)delta>=2/sqrt(5). Along any unbounded sequence with bounded ||f|| delta, delta tends to zero, proving the lower liminf bound. The two absolute embeddings of 1+zeta+zeta^(-1) are phi and 1/phi. The augmentation-zero coefficient vectors of (1-zeta) times its k-th power give increasing projected lengths r_k and complementary lengths exactly 2/(sqrt(5)r_k). Taking f_k to be the projected vector gives the matching upper liminf. The three nearest-vector cases give amplification at most sqrt(5)B, 1, or (sqrt(5)/2)B(B+sqrt(5)/2), all at most 2B^2 for B>=2. Since r_0<2 and r_(k+1)=phi r_k, the largest r_k<=B strictly exceeds B/phi, proving the stated strict lower bound. The scripts were inspected, not run; exact determinant tests and floating comparisons are supplementary.

## originality

PASS

Best-of-knowledge pass for the sharp folded-distance liminf and explicit radius-dependent inverse growth for this signal plane in its specified Euclidean normalization. Qualitative injectivity is already covered. The product identity and its unit equality mechanism are a direct cyclotomic embedding-norm specialization, not a new ideal-lattice theorem. The distinct claim transfers this product to the actual nearest point of the full integer lattice for arbitrary real signals and pairs that lower bound with a unit sequence and a finite radius cutoff.

## value

PASS

Global injectivity of this natural smallest prime-length nontrivial real first-harmonic model does not reveal the severity of near collisions. The sharp liminf and uniform quadratic growth bounds quantify how conditioning deteriorates with energy, distinguishing the inverse problem from a simple uniqueness check. The exact product makes the near collisions explicit without claiming that standard norm theory is new or that arbitrary sampling has this rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
