# Independent mathematical audit

## correctness

PASS

The centered Hermite ambiguity formula e^{-t/2}L_j(t) reduces the exact Gaussian-relative squared gain to inf_{t>=0} sum w_j L_j(t)^2. The cubic r(u)=u^3-9u²+24u-12 has exactly one real zero u in (3/5,2/3), at which L1(u)=-L3(u), and L2(u)^2 is strictly smaller. Evaluation at this u bounds every allocation by (1-u)^2 and forces w2=0 for equality. With c=3-3u+u²/2 the asserted exact SOS factorization has strictly positive quadratic remainder; independent SymPy polynomial reduction modulo r verified the identity for all t. Contact derivative forces w1=c/(1+c), w3=1/(1+c), proving uniqueness and single contact radius. Numeric root u=0.644698602391879 and optimum 0.126239083142284. No finite t-grid is used to prove the universal claim.

## originality

PASS

Best-of-knowledge: the primary Alaifari–Yang multi-window work gives the Hermite–Laguerre formula and patchwise coverage, not the all-radius weighted squared minimax. Earlier exact h1/h2 allocation or h0/h1/h2 expanding-disk optimization use different window sets/objectives and cannot imply the h1/h3 optimum. Independently checked exact SOS certificate of the new algebraic contact.

## value

PASS

Hermite ambiguity zeros obstruct linear inversion, making global Gaussian-normalized worst-case coverage a natural exact stability-design invariant. The surprising complete h2 exclusion and uniquely certified optimal h1/h3 allocation are a motivated sharp structural design result rather than a gratuitous polynomial minimization; it does not purport to solve nonlinear phase retrieval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
