# Independent mathematical audit

## correctness

PASS

For every row stochastic 2×2 letter transition the probability update has slope equal to determinant; strict negativity makes all letter maps decreasing. Upper and lower envelopes satisfy M_{t+1}=U(m_t), m_{t+1}=L(M_t). Both two-step envelope compositions are increasing; each parity subsequence of extrema is monotone. Strict unique winning suffix forces each prefix to be the unique appropriate extremum according to suffix parity. Each letter’s strict max/min region among affine functions is an interval, so a monotone parity input cannot select it in two separated runs. Counting ordered distinct-run labels and positive compositions yields T_q and O_q(n^(2q−2)), including n=1 and odd/even boundaries. Independent brute-force rational PFA verification tested 1080 parameter cases, 775 unique winners. Infinite conclusion rests on envelope/interval proof.

## originality

PASS

Gill 2024 supplies the affine representation and a full binary-alphabet classification, not the q≥3 all-negative-determinant parity run obstruction. Kjos-Hanssen establishes 3-state universality, not a two-state negative-slope restriction. The 2026-10-26 nonnegative-slope classification uses increasing maps and one run per symbol in the full word, not two independently constrained parity subsequences. No exact q≥3 result implying the submitted necessary upper bound was identified; historical priority remains qualified.

## value

PASS

The two-state boundary of probabilistic automatic complexity is a natural unresolved counterpart to three-state universality for arbitrary q. For the structural all-negative determinant subclass, the two-parity no-recurrent-run theorem and polynomial bound provide a precise forbidden-pattern filter, exponentially smaller than q^n, and capture a real orientation-reversal phenomenon rather than simply substituting parameters in the increasing-map case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
