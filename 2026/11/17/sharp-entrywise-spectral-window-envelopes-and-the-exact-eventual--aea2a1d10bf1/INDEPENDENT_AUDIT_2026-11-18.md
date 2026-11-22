# Independent mathematical audit

## correctness

PASS

PASS. Read full spectral-window minimax proof and verify.py. Decompose e^(tA)=uu^T+aQ+(b-a)K with 0<=K<=Q. For i!=j, S=(v_i v_j^T+v_j v_i^T)/2 on u-perp has one positive and one negative eigenvalue (c+-alpha beta)/2; choosing its rank-one positive/negative projections saturates both entry envelopes for all t through a fixed three-level A_K. Strict H(t) monotonicity follows F'(t)=(m²-d²)e^(mt)sinh(dt)>0, giving unique sharp onset and persistent negative witness for all earlier positive times. Independent SciPy exponential of the example u=(3,4,12)/13 and delta=1,L=2 confirmed R=sqrt(170), T~1.7949547597 and sign transitions. n>=3 ensures v_i,v_j independent; no Metzler assumption is imposed.

## originality

PASS

Finite attained three-level spectral-window minimax time differs from infinite-dimensional qualitative positivity work.

## value

PASS

PASS. Exact earliest uniform time when every symmetric generator with a fixed positive dominant eigenvector and prescribed spectral window becomes entrywise positive is a naturally motivated finite spectral/positive-semigroup stability question. The sharp entry envelopes, persistent worst-case three-level matrix and coordinate-imbalance onset identify a genuine structural boundary. These do not merely restate qualitative eventual-positivity results or finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
