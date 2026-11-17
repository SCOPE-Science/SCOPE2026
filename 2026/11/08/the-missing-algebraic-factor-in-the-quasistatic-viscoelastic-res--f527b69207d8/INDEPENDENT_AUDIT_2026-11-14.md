# Independent mathematical audit

## correctness

PASS

For every fixed r>0 and |x|→∞ *in the specified strong-memory quasistatic mixture*, substitute u=e^{-t}. Variance polynomial v(u)=S-Au+B u² has maximum S=(2r+1)/r at u=0 and strictly negative derivative throughout 0<u<1; the endpoint variance defect is linear, so Watson lemma with exponent u^(r-1) yields the exact C|x|^(-2r) Gaussian correction, not a pure Gaussian equivalent. Expansion 1/(2v)-1/(2S)=cu+du² with c=A/(2S²), d=A²/(2S³)-B/(2S²) and amplitude correction A/(2S) gives relative coefficient −(2r+1)^3/[2(r+1)] at x^(-2). Tail integration yields 2CS x^(-(2r+1))exp(−x²/(2S)), and iid extreme value scaling yields Gumbel with squared centering log N−(r+1/2)log log N+log B. Independently checked the symbolic coefficient and mpmath endpoint integrals for r=0.5,1,2 at x=40; ratios 1.0000102,1.0000321,1.0001817 to two-term asymptotic. Original verification source inspected. Domain excludes any claim about finite bath-memory tails, uniformity in r, or dependent sampled trajectories.

## originality

PASS

Source Santra–Das derives the quasistatic mixture and writes a Gaussian-only far-tail expression; the reviewed exact endpoint asymptotic identifies a missing nonconstant polynomial factor, explicit first correction and changed iid maximum loglog centering. Generic Watson/Gumbel tools are known methods and not credited as new.

## value

PASS

A sharp correction to a stated asymptotic equivalent for a physical stationary model matters quantitatively for rare-event probabilities and changes the loglog centering of independent extremes by r loglog N. The mathematical work identifies a nonuniform endpoint mechanism and a concrete error in a current published expression, not merely a generic theorem rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
