# Independent mathematical audit

## correctness

PASS

With normalized monomials, write X and Y for the two damped composition operators. On the nonconstant basis each has singular values given by its exponential factors times sqrt(w_p) or sqrt(w_q), and w_j<=1. Each is in every positive Schatten quasi-ideal (the constant is finite rank), hence so is D=X-Y. On the positive indices let U=X*X+Y*Y (diagonal) and W=X*Y. Then D*D=U-W-W*. The only positive-index action of W is e_(p0 k) to a multiple of e_(q0 k), with squared amplitude r^(2(a q0+b p0)k) w_p(q0 k)w_q(p0 k). Neither W nor W^2 has a diagonal because p0/q0 differs from 1. Thus Tr((D*D)^2)=Tr(U^2)+2||W||_2^2 on the nonconstant subspace; D kills the constant. This independently recovers (1). Solving the input/output rotation equations gives full singular-value phase invariance. From the beta-integral monomial norm, w_j(n)=j^(-alpha-1)+O(1/n); each geometric sum has leading 1/[c(1-r)] and its 1/n remainder is logarithmically bounded. This gives the four terms in (3), and the diagonal trace gives (4). At alpha=0, p=2, q=3, a=b=1 the result is 1/16+1/36+1/12+1/30=149/720. Replay: RESULT.md (1)–(8) and the traced expansion above; verify.py was inspected, not executed and is supplementary. Two nonmaterial textual issues: the literature paragraph calls the invariant a fourth power of the Gram operator, but it is its square; the Hardy-space exclusion is a scope choice, not an obstruction to this argument (setting all monomial norms to one gives the Hardy analogue).

## originality

PASS

The distinct claim is the joint exact compact-difference fourth moment and sharp two-speed radial coefficient on weighted Bergman spaces. Neither the mixed-product collision parametrization itself nor the undamped operator invariants are new. The accessible strongest operator comparisons concern different invariants, settings, or only class membership; none inspected gives the full weighted two-speed quartic trace or its boundary coefficient.

## value

PASS

The fourth moment is the first of the two stated even Schatten moments that detects overlaps between distinct input monomials. Its exact positive, normalized arithmetic contribution determines how much Hilbert–Schmidt diagonal information misses and quantifies the boundary loss of compactness in the two-speed model. This is a useful trace calculation, not a claim of new class theory or a full spectral law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
