# Independent mathematical audit

## correctness

PASS

The proof works for arbitrary admissible operators, not only scalar tapers. Independently, write D_n=R_{nn} in level blocks, and x_n=Tr(D_n)/r. The (n+1,n) block of the commutator is D_n-D_{n+1}; retaining only these blocks and using the trace Cauchy–Schwarz inequality gives the lower bound r times the scalar Dirichlet energy of x. The scalar problem allows summable infinite tails, but the displayed optimizer is finite. For b=B/r>1, (m+1)/3<b≤(m+2)/3 gives q>0 and −q<p≤q, so all positive cells decrease to zero and the finite sums give x_0=1 and trace B. The discrete Laplacian is −2q on cells 1 through m−1 and −(p+q) at m; expanding about the candidate yields exactly the nonnegative budget, boundary, tail and square terms in the proof. Equality is unique; equality at an operator midpoint would force the difference to commute with the shift, and a compact such difference is zero since T^n is weakly null and isometric. Trace r forces R=P directly and its commutator has squared norm r. At b=(m+2)/3 the parameters (p,q)=(q,q) switch to (−q,q) on the next support, with q=1/[m(m+1)], leaving the profile and first derivative unchanged. The second derivatives jump and m=3b+O(1) gives the leading 4r²/(9B) and the claimed 8/9 ratio. The bundled rational checks are supplemental; the script was read, not executed.

## originality

PASS

Best-of-knowledge pass for the exact trace-constrained formula, unique arbitrary-operator optimizer and cutoff structure, not for the Dirichlet method, multiplicity normalization or qualitative vanishing. The actual positive catalogue comparisons concern different constraints or operators. The strongest cited primary-work descriptions do not imply the trace-budget claim; those full-text comparisons remain incomplete, not negative evidence.

## value

PASS

Quantifies exactly how much trace is needed to make the shift commutator small. It determines the unique unrestricted operator optimum and all support changes; the asymptotic constant demonstrates a strict improvement over the natural linear taper. This is a useful sharp resource benchmark beyond qualitative quasicentrality, despite the elementary character of the scalar optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
