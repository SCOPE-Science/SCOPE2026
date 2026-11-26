# Independent mathematical audit

## correctness

PASS

At p=G(x), DG(x)h has ith entry beta p_i(h_i−p·h). Convexity of its unhalved L1 norm gives a maximizing cube vertex h with signs + on S and − on its complement. For q=p(S) this produces 4beta q(1−q); the empty and full subsets give zero. For each proper nonempty S let A and B be its two prior sums. Its posterior odds run through [e^(−beta R) A/B,e^(beta R) A/B]: bounds follow by comparing the weighted averages of the exponentials on each side, and exactly the whole interval is realized by scores constant on each side. Minimize absolute log-odds on this interval to get (|log(A/B)|−beta R)_+. Now 4q(1−q)=sech²(log(q/(1−q))/2) and |log(A/B)|=2 artanh(|1−2A/(A+B)|), so optimization over subsets yields the stated rho(c) formula. Convex-segment integration gives the global bound, and rescaling any boundary maximizer toward a constant gives interior points at which small steps in the maximizing sign direction recover the derivative norm as a limit. This establishes a supremum of two-input quotients, not attainment by distinct inputs. At R=0 additive invariance makes the map constant. Equal weights give rho=0 or 1/n and hence the stated threshold and positive-budget limit. For binary-encoded positive integer weights a nonzero imbalance is at least 1/C of the total; its absolute log-odds is at least log((C+1)/(C−1))>2/C>1/C. With beta=1 and R=1/C this proves exact saturation iff PARTITION is positive, with polynomial-length rational parameters.

## originality

PASS

The fixed-posterior sensitivity is already supplied by the sharp fixed-center Hilbert-to-L1 calculation of Cohen–Fausti after differentiation and norm conversion. The supported addition is optimizing this local sensitivity over the positive-radius projective ball around a specified weighted prior, expressing the sharp two-input constant by prior partition discrepancy and giving its binary-input saturation hardness. The checked Hilbert source has the fixed-center finite displacement calculation, not that within-ball two-input optimization. The closest partition-hardness record concerns a different, quadratic simplex map.

## value

PASS

This improves a global robustness constant precisely where the weighted prior prevents balancing any subset under the allowed score budget. It gives an exact dependence on the prior and radius, not just a sufficient bound or a local norm, and identifies an exact saturation decision for which a dimension-free smooth map still encodes a discrete partition problem. The odd/even uniform-prior cases are consequences of the weighted result, not its sole motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
