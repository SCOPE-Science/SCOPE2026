# Independent mathematical audit

## correctness

PASS

PASS: precisely distinguish first y0=f(x[n-1],x0,x1), internal yi=f(y[i-1],xi,x[i+1]) and final y[n-1]=f(y[n-2],x[n-1],y0). Track first output, preceding output and four-bit mask of (old last, next old bit). Existential transitions are logically equivalent to the internal equations and terminal diagonal mask (a,a) enforces the scan seam; each target prefix has one deterministic state so terminal v=number distinct permitted final bits, not number of predecessors. Exact table closure has 26 states, yielding I_n=uT^(n-2)v. Independently reconstructed 26 states from truth table and checked 26 consecutive exact integer residual zeros for Q(z)=1-2z-z²+2z³+z⁴-z⁵ at k=5..30; Cayley-Hamilton for the 26x26 matrix forces all later residues zero. Initial coefficients give boxed series. Principal positive zero of 1-z-2z²+z⁴ (~0.524888) is unique least modulus, with positive nonvanishing residue; asymptotic base 1.905166..., entropy correct. No claim about later sweeps.

## originality

PASS

PASS (qualified): exact scan-order-specific image automaton and generating function are distinct from simultaneous Rule 110 image enumeration and from earlier sequential order-independence/attractor classifications, despite using standard subset construction. Published same-day copy is not independent antecedent; previous exact all-length enumerators of synchronous rule have differing counts and characteristic polynomials.

## value

PASS

PASS: a natural discrete invariant of a canonical sequential cellular automaton is the size and language of one-sweep reachable states. The exact all-length 26-state recognizer, constructive inverse and entropy quantify information loss due to scan order and contrast precisely with simultaneous Rule 110. This is a meaningful infinite-length classification and not the mechanical recitation of known synchronous tables; no universality/long-term dynamics claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
