# Independent mathematical audit

## correctness

PASS

The symmetric transition has diagonal entry 1−S at the left endpoint. The normalized centered endpoint vector x=(e_1−1/n·1)/sqrt(1−1/n) has Rayleigh quotient 1−nS/(n−1), giving the obstruction on 1^⊥ even if the chain is reducible. Equal feasible masses with S=1/2 give 1/2 on every diagonal and 1/[2(n−1)] off diagonal, hence d_n=(n−2)/[2(n−1)] on 1^⊥. For S=1/2 and δ the deviation from equal masses, Δ=P−P_* is a sum of distance-class Laplacians with coefficients −δ_s; each has degree at most two, so ||Δ||≤B=4sqrt(n−1)||δ||₂. At x its spectral measure has mean zero and second moment ||Δx||²=n||δ||₂²/(n−1) from the endpoint column. If a is the top centered eigenvalue of Δ, integrate (λ+B)(a−λ)≥0 to get this second moment ≤aB. This proves the stated linear deviation bound, with δ=0 handled separately. For S>0, reweight the feasible mass by 1/(2S): P=(1−2S)I+2S Q, so the largest centered eigenvalue gives the stated wasted-mass penalty and scaling cancels in the deviation term. S=0 gives P=I exactly. Either penalty is strict away from the proposed law. Powers, move probability and TV follow from the two orthogonal spectral projections, including the n=2 one-step case.

## originality

PASS

The all-size optimum and stability concern a structured family with one shared displacement weight per distance and rejection at the boundary. The continuous box already supplies the endpoint-obstruction mechanism and uniform-jump analogy. The finite correction, uniqueness over the full proposal-law class and quantitative two-part penalty are not stated or implied by the inspected neighboring results.

## value

PASS

The class isolates a practical Markov-chain constraint: one symmetric proposal law must work from every state despite boundary rejection. The exact finite optimum differs from both the unrestricted and continuous optima, and the stability bound separates losses from outright wasted mass and from choosing the wrong shape. These conclusions are useful beyond recomputing the proposed kernel's eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
