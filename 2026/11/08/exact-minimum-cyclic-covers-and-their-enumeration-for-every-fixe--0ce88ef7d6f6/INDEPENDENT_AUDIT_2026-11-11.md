# Independent mathematical audit

## correctness

PASS

For all integers q>=2,n>=2,1<=k<=n, a circular track with every n-window having exactly k nonzero symbols necessarily repeats its binary support indicator with period dividing n. Every fixed-weight support necklace therefore gives a separate Eulerian overlap-graph component, and each has one mandatory track in a minimum cover. For a necklace of least support period h and a=kh/n positive positions, normalizing outgoing edges gives stochastic matrix whose n-th power is rank one on each support phase. Its nonzero spectrum consists of h-th roots of unity; directed matrix-tree cofactors are exactly s^(a*s^(k-1)-k) where s=q-1. BEST then counts Euler tracks per component as that power times ((s-1)!)^(a*s^(k-1)). Summing a over binary support necklaces yields binom(n-1,k-1), proving the all-parameter global count C=s^(s^(k-1)*binom(n-1,k-1)-kN)*((s-1)!)^(s^(k-1)*binom(n-1,k-1)), N=(1/n)sum_{d|gcd(n,k)}phi(d)binom(n/d,k/d). Independent exact directed-tree cofactors checked several small triples; the universal conclusion rests on reset-spectrum and BEST proof, not experiments.

## originality

PASS

PASS best-of-knowledge: Fixed-weight de Bruijn sequence/universal-cycle literature often uses shorthand encodings or bounded weight rather than unshortened windows with exact fixed nonzero support. A published result covers k=2 only. Arbitrary k requires the general support-necklace reset spectrum and exact per-component spanning-tree count. No inspected stronger theorem implies the arbitrary-k product.

## value

PASS

PASS: A complete exact enumeration for every fixed weight and alphabet size resolves a natural missing classification beyond the known number of support-necklace components. The reset-spectrum computation supplies a reusable nontrivial arborescence invariant, not an arbitrary small numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
