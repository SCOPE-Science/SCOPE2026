# Independent mathematical audit

## correctness

PASS

In B=(I-G)^(-1), row i is the sum of its new coordinate vector and a combination of earlier rows, whose supports lie strictly before coordinate i. The Euclidean squared norm is therefore 1 plus the square of the row defect. The triangle inequality and the absolute budget give a defect bound of tau^2 times the largest earlier squared row norm. Inductively that is at most sum_{h=1}^{i-1} tau^(2h), attained simultaneously by the bidiagonal chain, also for n=1 with empty defect. This bounds the full class, not just parent forests. The bound ||B||_2<=1+||B-I||_F gives the limsup on division by sqrt(n). The first k+1 columns of each of n-k-1 leaf rows in the comb are identical, with squared norm sum_{h=1}^{k+1} tau^(2h); the normalized input proportional to those coefficients certifies the matching liminf as k tends to infinity with k/n tending to zero. Orthogonality and the absolute budget work over both fields. Unbounded inverse gain gives unbounded condition numbers as ||T||_2>=1 by its diagonal. Independent replay `python /workspace/branches/independent_replay.py 3` checks 585 exact Gaussian-grid matrices and three exact projected lower bounds; the spectral result is asymptotic and no exact finite spectral maximizer is claimed.

## originality

PASS

Classical row and comparison-matrix inverse bounds do not give these sharp mixed-norm laws. The closest distinct indexed result has an exact Euclidean forest extremum for residual powers, not inverse summation. No inspected result gives or implies the squared Frobenius defect extremum together with the sharp coefficient of inverse growth.

## value

PASS

The result quantifies exactly how a dimension-free row budget controls one norm while allowing an inverse gain of sharp order sqrt(n) in another. Exact chain attainment and the different comb construction expose two distinct optimization mechanisms for a motivated triangular-solve design constraint. The result does not claim this worst-case gain for actual ILU factors or convergence of a complete solver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
