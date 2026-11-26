# Independent mathematical audit

## correctness

PASS

At p=1 the shorter arc from x to y gives a site with distance sum at most max(delta(x,y),1/3): use a site on the arc, or the nearer gap endpoint if the arc is site-free. Every site has distance sum 1/2 at antipodal pairs. This gives R(1)=1/2 and just the antipodal maximizing locus. For p>1, the p-norm is at most the 1-norm, with strict inequality for a site having both coordinate distances positive; such a site exists at every antipodal pair. Compactness makes the pointwise strict bound uniform for each finite p. For the derivative, the uniform norm expansion holds near distance sum 1/2 because u(log u)^j extends continuously at zero and the sum stays positive. Comparing the arc bound with evaluation at an antipodal pair forces maximizing points within O(epsilon) of that locus. In a symmetry interval 0<=x<=1/6, for y=x+1/2+epsilon t the three first-order terms in the interior are -t-H(x), -t-H(1/6-x), t-H(1/3-x), where H is the distance entropy in RESULT.md. At x=0 the stable opposite slopes are from sites 2/3 and 1/3; at x=1/6 they are from sites 0 and 1/3. In both endpoint limits their entropies are H(1/6), so kinks cannot improve the bound. Maximizing the minimum over t gives loss [H(1/3-x)+max(H(x),H(1/6-x))]/2. Symmetry and strict concavity of H show this decreases to x=1/12 and then increases. At the minimizer t=(H(1/4)-H(1/12))/2 attains the common first-order term and the loss is log(12)/4-5 log(5)/24. With r=max(R(p),1/4)<1/2 the product needs at most three closed balls but each factor needs two. The result concerns prescribed centers, not a global three-center optimum; the inspected numerical script was not executed or used as a continuum certificate.

## originality

PASS

Credit the exact right derivative for the fixed three-site design and the strict covering result down to every p>1 on full circles, not the Manhattan endpoint, the Euclidean design, or the finite-factor counterexample. A distinct catalogue generalization exactly recovers this derivative, but expressly treats the three-site case as an already established separate calculation and claims n>=4 as its new scope. Its text supplies no independently identifiable earlier three-site source; the same-day label is not used to infer priority.

## value

PASS

The exact slope measures the first-order size of the radius window in which this fixed design gives a three-versus-four covering counterexample for connected smooth factors. It resolves a degenerate maximum along an entire antipodal locus by balancing the nearest-site losses, rather than observing strict norm monotonicity or numerically estimating the onset. It does not rely on unproved optimal placement of the three sites.

The dated certificate retains the supplied scientific assessment, sources and limitations.
