# Independent mathematical audit

## correctness

PASS

Reconstructed the exact mean by conditioning on the focal vertex's neighbor set. Given degree d>0, the conditional expected score is 1+(d−1)θ+(N−d)σ−d, with θ the adjacency probability of two uniform neighbors and σ that of a uniform neighbor and nonneighbor. Translation invariance gives pθ+(1−p)σ=p. Averaging over D∼Bin(N,p) with isolated score zero leaves (1−θ)P(D≥2). In one coordinate the ordinary difference of two points in [−r,r] has triangular density; the central interval contributes 3/4 and, when r>1/3, the wrapped tails contribute (3r−1)²/(4r²). Independence across coordinates gives θ=ρ^m. Above 1/3 the derivative sign is that of E_N−H_m; the binomial elasticity E_N is nonincreasing in p (constant for N=2), whereas H_m is strictly increasing from 0 to infinity, since rρ' increases and both other factors are nondecreasing. Below 1/3 the mean increases strictly. The coefficient of z in 1/E_N increases strictly from N=2 onward, giving strict left movement of the crossing as N rises. At fixed m, H_m∼27(3/4)^{m−1}(r−1/3)/(2κ_m); monotonicity bounds the displacement by O(E_N(p_m)) so N(r−1/3)→0. Then the exponential factor at the moving root has asymptotic ratio one to (1−p_m)^{N−2}, yielding the stated equivalent. At fixed N the Taylor expansions at 1/2 give locally uniform convergence in c=m(1/2−r); max values cannot escape because the binomial tail is bounded by binom(N,2)e^{−4c} and the geometric factor is O(c) at zero. The limiting (1−t)B_N(t) has the unique maximum by the strictly decreasing product ((1−t)/t)E_N(t). The three-vertex checks follow from B_2=p². The analytic proof is for the annealed expectation only. The frozen checker and its reported finite tests were inspected, not executed.

## originality

PASS

Yuan's exact mean is clearly covered prior work and is not accepted as a new claim. The audited contribution is the all-n,m optimizer, its strict vertex-count ordering, and the two asymptotic optimization laws. The inspected exact-mean theorem does not give those statements; their proof uses a parameter-uniform elasticity comparison and separate asymptotic control at the maximizing root. The only exact indexed optimizer match found is the assigned record itself.

## value

PASS

Radius is the natural design parameter of a canonical geometric graph construction. The optimizer resolves the exact competition between neighborhood closure and sampling enough neighbors, giving a finite-size ordering and quantitatively distinct limiting locations for many vertices versus many dimensions. Knowing the expectation at fixed radius does not answer this design question. No claim about realized graphs or applications is needed for the exact classification to be useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
