# Independent mathematical audit

## correctness

PASS

In the sum/difference coordinates U,V, let A and D be the half-sum and half-difference of tanh(β(U±V)/2). Then O1+O2=−2AD/(1−A²) and O2−O1=2D/(1−A²). On U=0 at V>0, A=0 and D=b; the absolute values are smooth locally because O1=−b and O2=b. The branch condition is h(b)=atanh(b)/b=β(1−μ); h is strictly increasing from 1 to infinity. From the two displayed opinion combinations the cross derivatives vanish and the longitudinal eigenvalue is α[h(b)(1−b²)−1]<0 by the integral for atanh(b); the transverse eigenvalue is αb(1−b²)[β−B(b)]. Differentiation gives B'=N/[b²(1−b²)²] and N'=2b[3−b+2(1−b²)atanh(b)]>0, with endpoint limits −1 and 2 for N. Thus B diverges at both ends and has one minimum. Every root with B=β satisfies h<β, and increasing μ strictly decreases b, so the two roots map to the claimed saddle and return-to-stability windows. At β=β* there is one transverse zero and for β<=1 no nonzero branch; the nonhyperbolic endpoints are not assigned a nonlinear stability class. Symmetry gives the same spectra for the negative branch. An independent 65-digit-decimal recomputation found β*=3.73095400142252865873, μ_lo=0.790799809632571036 and μ_hi=0.874098742493055869; finite differences of the two original reward flows at μ=0.8745 gave eigenvalues/α of −0.245472383135032932 and −0.007961757359133581 at both fixed points. Replay: python3 /workspace/review-evidence/replay.py 1. Neither this proof nor the replay applies to the frequency-weighted four-dimensional model or agent-based dynamics.

## originality

PASS

The counterfactual model and prior numerical portrait are credited, not treated as new. The distinct evaluated result is a continuous all-β hyperbolic classification of its nonzero segregated equilibria and a second attracting window in the approximate transition region. The accessible Figure 9 description links the prior plotted equilibria to Eq. (14); the frozen comparison locates the earlier stability description at the first crossing. The full article wording could not be independently reread, so the contradiction with its prose is conditional on the frozen description being exact. Neither the plotted classification as reported nor specifying the original ODE is an existing stability theorem implying the restored window.

## value

PASS

A restored pair of local attractors changes the qualitative bifurcation picture in a motivated existing model, even in a narrow parameter interval. The critical exploration parameter identifies exactly when the stable–saddle–stable pattern occurs over the entire segregated branch. The result makes no unsupported claim about basin size, simulations, or the larger dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
