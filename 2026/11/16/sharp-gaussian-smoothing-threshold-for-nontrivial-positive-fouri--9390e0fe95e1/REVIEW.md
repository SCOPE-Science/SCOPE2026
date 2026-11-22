# Independent mathematical audit

## correctness

PASS

The coefficient vectors A=(1,5,6), B=(3,7,2) factor as (1+2z)(1+3z) and (1+2z)(3+z); |1+3z|=|3+z| on |z|=1 and neither Fourier transform vanishes there. Both have variance 59/144 and incompatible nonzero centered third moments -145/864 and 17/864, ruling out translation/reflection congruence. Gaussian latent-location posterior proportional to (1,lambda u,u^2) has exact Var=(lambda z+4)/(z+lambda)^2, z=u+u^-1>=2; maximizing yields M(lambda)=2/(lambda+2) for lambda<=4 and lambda^2/[4(lambda^2-4)] otherwise. Thus log curvature <=0 precisely t>= M((5/sqrt6)e^(1/(2t))), equivalently t>= unique root (t-1/4)((25/6)e^(1/t)-4)=1 in (1/4,1/3). Strict inequality gives uniform strong logconcavity; the boundary has two zero-curvature positions. The source exact rational checker verifies autocorrelation, cumulants and conditional-variance formula; independently checked autocorrelation [62,35,6], numerical root 0.2548339622562054 and derivative sign. Standardization yields noncongruent near-Gaussian Fourier twins with uniformly converging log Hessians.

## originality

PASS

Algebraic 1D Fourier phase root-reflection and conditional Gaussian-mixture curvature are established methods, and an earlier published symmetric-three-normal result already gives a generic curvature optimizer/threshold. The inspected prior statements do not exhibit a specific nontrivial positive, nonvanishing Fourier-intensity pair that simultaneously survives global strong logconcavity and near-Gaussian normalization with this sharp common threshold. The combined inverse-problem obstruction is a distinct, bounded best-of-knowledge result, with a significant risk that the construction follows routinely from known homometry plus Gaussian smoothing.

## value

PASS

Whether nonvanishing Fourier intensity determines a positive density under strong logconcavity or arbitrarily Gaussian-like global curvature is a natural inverse-problem uniqueness boundary. An explicit inequivalent positive pair with a proved exact shape transition and uniform convergence of log Hessians provides a motivated constructive obstruction; it is not merely a renamed known phase-flip result, though algebraic ingredients are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
