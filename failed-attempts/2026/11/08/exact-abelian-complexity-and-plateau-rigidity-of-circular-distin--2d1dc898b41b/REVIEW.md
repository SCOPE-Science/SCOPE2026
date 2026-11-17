# Independent mathematical audit

## correctness

PASS

For q>=3 pairwise distinct runs with total period p, cyclic Parikh windows of residual length r have repeated vectors only in one phase block; sliding changes at phase s iff x_s != x_(s+r). Therefore A(r)=p-sum_i((a_i-r)_++(a_i-p+r)_+) with A(0)=1. Each positive-part summand is convex symmetric; maximizing interval [min(M,p-M),max(M,p-M)] and peak min(p,2(p-M)) follow immediately. Independently enumerated Parikh vectors for every q=3 or 4 run tuple with lengths 1..4 and every residual length, all 320 profiles agreed.

## originality

FAIL

FAIL: A previously published Nov 2 theorem gives exactly the same nonzero-residue cyclic-window formula (Lemma 2, Exact length spectrum), for all cyclic powers and even their terminal linear windows. The asserted plateau is immediate elementary maximization of this same formula; no separate original theorem survives.

## value

FAIL

FAIL: Repeating an already proved exact length-specific Parikh spectrum with its elementary longest-run plateau is covered recomputation, not an independently needed unknown fact. The prior Nov 2 result is strictly broader and has the full period-power aggregate formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
