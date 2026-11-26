# Independent mathematical audit

## correctness

PASS

The rotation by 2^(-s) fixes all the indexed carries simultaneously and toggles the central bit, so it pairs the two central-bit events inside every profile fiber, including when the profile is empty. Independently, the sawtooth kernel follows by reducing the two frequencies to coprime u,v and writing the phase as (i+t)/(uv): the residues modulo u and v are independent uniform for fixed t, and the conditional centered means are (t-1/2)/u and (t-1/2)/v. The integral is therefore 1/(12uv) in the coprime case. In the carry covariance the two central-versus-final-frequency terms cancel, and gcd(d/2,j)=gcd(d,j) gcd(2,b)/2 yields (gcd(2,b)^2-1)/(12a(b-a)). The fair marginals determine all four cells; even b gives strictly positive covariance and excludes each such coordinate from any independent profile. This is a Lebesgue-phase result, not a statement about independent p-adic digits. The recorded checks are bounded; the separately written /workspace/branches/independent-finite-checks.py verified 220 pair cells and 24 balanced complete-profile fibers at d=2,8,12,18,20 using exact integer grids.

## originality

PASS

The distinct contribution is joint independence from the complete maximal profile, with a sharp boundary, not the classical correlation kernel or a separately novel pairwise law. The strongest distinct same-day result covers the pair covariance by specialization, but its second moments do not yield the eventwise theorem. Relative priority of the pairwise statements is not inferred from their shared publication date.

## value

PASS

The whole-profile result answers which simultaneous binomial-ratio tests can be conditioned on without changing the central phase law. It gives an explicit maximal family, works for arbitrarily large profiles without assuming independence among their coordinates, and supplies a strict obstruction for every excluded ratio. It is useful at the phase-model level without asserting a valuation or prime-distribution law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
