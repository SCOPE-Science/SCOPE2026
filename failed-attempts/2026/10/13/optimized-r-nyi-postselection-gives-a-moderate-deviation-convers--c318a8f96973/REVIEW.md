# Independent mathematical audit

## correctness

PASS

Conditional on the primary source general-alpha inequality -H^up_{1+t} <= n Q^down_{1+t}+((1+t)/t)L and uniform Taylor bound Q^down_{1+t}<=Q^(1)+at+ct^2, substitution t=sqrt(L/n) (permitted if L<=n/4) yields exactly (a+1)sqrt(L/n)+(c+1)L/n. In the same source fidelity inequality, setting K=a+c+1, t=Delta/(2K) for Delta<=K gives Taylor cost <=Delta/2 and t/(1+t)>=Delta/(3K), hence the advertised exponent nDelta^2/(6K). These are correct algebraic estimates; frozen artifacts/verify.py checks those scalar inequalities on finite grids only. Could not independently inspect the full recent paper to validate its quoted noncommutative source equations; the submission itself explicitly treats them as published assumptions. Result is conditional on those precise premises and code restrictions.

## originality

FAIL

FAIL: the exact parameterized all-alpha inequality and the exact fidelity bound are already in the same primary source, whose stated hypotheses cover every t in (0,1/2]. The optimization is elementary balancing of at against L/(nt), and t proportional to Delta for the converse. The claimed window is a routine direct consequence of a strictly stronger earlier parameter-uniform statement, not a new theorem, even though the original authors happened to instantiate t=n^(-1/2) when presenting their less sharp corollary. No new channel/operator inequality or novel converse argument is established.

## value

FAIL

FAIL: choosing a familiar square-root optimizer in a bound of the form at + L/(nt), or proportional-to-gap t for a Chernoff-style exponent, is a routine textbook parameter substitution of the source inequalities. A sharpened displayed big-O rate may be useful to readers, but the package establishes no independently motivated mechanism, structural lemma, sharp cutoff or non-implied invariant that would warrant a separate result under the common value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
