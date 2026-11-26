# Independent mathematical audit

## correctness

PASS

A forward m-packet shuffle can be drawn by choosing an iid uniform packet word, cutting the input at the word counts, and drawing from the next named packet. Independent inverse stable sorts on fair bits compose to a stable sort on k-bit keys, yielding the forward m=2^k model after inversion. In the forward word construction, conditional on packet t at position i, the original index of the card equals one plus the number of earlier word entries ≤t plus the number of later word entries <t. This is precisely the stated independent pair of binomials. For rows bounded away from the endpoints, the component variance is n v_t(i/n)+O(1) uniformly. The Bernoulli characteristic function bounds the centered product by exp(-c σ²u²) for |u|≤pi, and Taylor expansion at u=O(n^(-1/2)) has cumulative cubic error O(n|u|³). Fourier inversion thus gives both the sharp peak upper bound uniformly in j and the matching asymptotic at j within O(1) of its mean. For a label bounded away from packet interfaces, competing means are linearly far away; even in its own component, rows farther than n^(-2/5) in scaled distance give exponentially small mass by Hoeffding. The column peak therefore has exactly the claimed leading profile, reached asymptotically at the nearest mean row. For excluded columns, the two endpoint components have maximal point probabilities bounded by constants times j^(-1/2) or (n-j+1)^(-1/2): if h trials can yield r successes then h≥r and the binomial peak is O((h+1)^(-1/2)). The other components are O(n^(-1/2)) uniformly. Thus for fixed interface width epsilon the omitted columns cost O((sqrt(epsilon)+epsilon)sqrt(n)+1); the interior integral is first truncated and only becomes full as epsilon decreases to zero. Every permuted guess has the column-capacity upper bound. In the explicit permutation the designated component's mean differs from its guess by t r0/m, so its interior Riemann sum matches the upper bound in the limit. The integrable linear-variance integral evaluates to 2/(sqrt(a_t)+sqrt(a_(t+1))). Independent exact forward-law checks for n=2,…,5 and m=2,4 including composition, and numerical constant evaluation, can be replayed with python3 -B /workspace/audit_checks/1.py. The asymptotic proof does not depend on those finite checks.

## originality

PASS

Pass for the sharp leading constant for one-use-per-label matching and the explicit asymptotically optimal permutation. The forward marginal mixture and the repeated-guess optimal score are established elsewhere and are not credited as new.

## value

PASS

Requiring all labels to be used exactly once is a natural no-feedback variant and genuinely couples positions. Even at one shuffle the restriction changes the leading coefficient from 2/sqrt(pi) to sqrt(2/pi). The theorem quantifies the restriction for each fixed shuffle count, and the constructive permutation attains the optimal leading term without a finite assignment solve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
