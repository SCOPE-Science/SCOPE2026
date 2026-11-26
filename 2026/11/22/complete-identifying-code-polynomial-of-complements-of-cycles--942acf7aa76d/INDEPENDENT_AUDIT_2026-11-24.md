# Independent mathematical audit

## correctness

PASS

The closed trace is S minus the intersection of S with the distance-two auxiliary edge indexed by v. For n>=5 these edges are distinct and form one odd cycle or two even-case components of length m=n/2. Equal empty edge traces mean at least two unselected edges, and equal singleton traces mean an isolated selected vertex; size-two traces distinguish their unique edges. Distinct traces force |S|>=3, so all closed traces are nonempty. In each auxiliary component runs of unselected vertices are separated by at least two selected vertices and at most one unselected run over the whole graph has length two. This gives the stated binomial expressions by counting ordered selected gaps, marking one of r singleton zero runs in A or the unique double zero run in B. It works for the m=3 components of n=6, for which B is empty. The label weights and factor 2 in the even case follow from the distinguishable components and the global one-defect allowance. At z=1 the generating function for A is -x f'/f and for B is x times the derivative of x^4/f, with f=1-x-x^3. At its positive simple zero rho the pole of x^4/f has coefficient rho^3/(1+3rho^2) in front of (1-x/rho)^(-1); multiplication by the coefficient index gives exactly c m lambda^m. The other two reciprocal roots are conjugate with modulus beta=lambda^(-1/2), and the even-parity cross term is bounded by O(n (lambda beta)^(n/2)), with sqrt(lambda beta)<1.2. Independent subset enumeration of the original closed-neighborhood condition (`python3 /tmp/opencode/frozen_checks.py cycles`) matched every size coefficient for orders 5..16. Independently, a four-state ordinary auxiliary-cycle transition T forbidding 010 has det(I-xT) equal to the first published factor, and det(I-x^2 exterior-square(T)) equal to the second (evaluated symbolically as a 6-by-6 determinant). The original step swaps the parity pairs while advancing one; the differing location of the empty-edge marker is just a cyclic shift in any closed walk. For eigenvalues lambda_i of T this parity-swapping advance has eigenvalues lambda_i and pairs ±sqrt(lambda_i lambda_j), justifying the product determinant. Frozen checker and requirements were inspected, not executed.

## originality

PASS

An earlier exact OLD-cycle polynomial gives precisely the zero-defect portion under an explicit change of weights; existing minimum-size results are not claimed as new. The distinct claim is the full closed-neighborhood identifying-code polynomial on the complement, including the one-defect counts and their growth. No inspected available statement gives those additional terms. The closest complement-cycle minimum paper was not accessible in full, so this is a best-of-knowledge decision rather than blanket priority.

## value

PASS

The graph family already motivates minimum-size questions, and the complete labelled size distribution resolves a different exact invariant. The distinction from ordinary-cycle OLD counts is substantial: one exceptional unselected edge changes the growth by a factor linear in n, on both parities, and can change the minimum degree. The correction is a structural explanation, not just another small computed case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
